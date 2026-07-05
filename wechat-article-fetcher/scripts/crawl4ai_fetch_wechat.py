#!/usr/bin/env python
"""Fetch WeChat Official Account articles with Crawl4AI.

Primary output is Crawl4AI markdown with remote mmbiz.qpic.cn image URLs.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import contextlib
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urldefrag, urlparse
from urllib.request import Request, urlopen


VERIFY_KEYWORDS = ("环境异常", "去验证", "完成验证后即可继续访问")
IMAGE_RE = re.compile(r"https://mmbiz\.qpic\.cn/[^\s)\"'>]+")
TITLE_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
MIN_MARKDOWN_LENGTH = 3000


def configure_crawl4ai_base_directory(output: str, runtime_dir: str | None = None) -> str:
    """Keep Crawl4AI runtime files near the output unless the caller overrides it."""
    if runtime_dir:
        base_dir = Path(runtime_dir)
    elif os.environ.get("CRAWL4_AI_BASE_DIRECTORY"):
        base_dir = Path(os.environ["CRAWL4_AI_BASE_DIRECTORY"])
    else:
        base_dir = Path(output) / ".crawl4ai_runtime"
    base_dir.mkdir(parents=True, exist_ok=True)
    os.environ["CRAWL4_AI_BASE_DIRECTORY"] = str(base_dir)
    return str(base_dir)


def configure_stdio() -> None:
    """Avoid Windows GBK crashes when Crawl4AI returns unicode text."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def import_crawl4ai() -> tuple[Any, Any, Any, Any]:
    try:
        from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
    except ImportError as exc:
        raise SystemExit(
            "Crawl4AI is required for this script.\n"
            "Install and verify it with:\n"
            "  python -m pip install crawl4ai\n"
            "  crawl4ai-setup\n"
            "  crawl4ai-doctor"
        ) from exc
    return AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a mp.weixin.qq.com article as Crawl4AI markdown."
    )
    parser.add_argument("url", help="WeChat article URL, e.g. https://mp.weixin.qq.com/s/...")
    parser.add_argument(
        "-o",
        "--output",
        default="./wechat_articles",
        help="Output root directory. A <timestamp>_crawl4ai subdirectory is created inside it.",
    )
    parser.add_argument(
        "--filename",
        default="wechat_article.md",
        help="Markdown filename inside the generated article directory.",
    )
    parser.add_argument("--timeout", type=int, default=90000, help="Page timeout in milliseconds.")
    parser.add_argument("--headless", dest="headless", action="store_true", default=True)
    parser.add_argument("--no-headless", dest="headless", action="store_false")
    parser.add_argument("--screenshot", dest="screenshot", action="store_true", default=True)
    parser.add_argument("--no-screenshot", dest="screenshot", action="store_false")
    parser.add_argument("--images", dest="images", action="store_true", default=True)
    parser.add_argument("--no-images", dest="images", action="store_false")
    parser.add_argument(
        "--runtime-dir",
        default=None,
        help=(
            "Directory for Crawl4AI internal runtime files. Defaults to "
            "<output>/.crawl4ai_runtime unless CRAWL4_AI_BASE_DIRECTORY is already set."
        ),
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print result metadata as JSON. The metadata file is always saved.",
    )
    return parser.parse_args()


def text_or_empty(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def markdown_text(markdown: Any) -> str:
    if isinstance(markdown, str):
        return markdown
    for attr in ("fit_markdown", "raw_markdown", "markdown"):
        value = getattr(markdown, attr, None)
        if isinstance(value, str) and value.strip():
            return value
    return str(markdown or "")


def normalize_markdown(markdown: str) -> str:
    normalized = markdown.replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\A(#\s+.+?)\n(?!\n)", r"\1\n\n", normalized, count=1)


def title_injection_js(css_selector: str) -> str:
    selector = json.dumps(css_selector)
    return f"""
(() => {{
  const selector = {selector};
  const titleEl = document.querySelector('#activity-name, .rich_media_title, h1');
  const title = titleEl && titleEl.textContent ? titleEl.textContent.trim() : '';
  if (!title) return;
  window.__crawl4ai_wechat_title = title;
  const container = document.querySelector(selector);
  if (!container || container.querySelector('[data-crawl4ai-wechat-title="true"]')) return;
  const h1 = document.createElement('h1');
  h1.setAttribute('data-crawl4ai-wechat-title', 'true');
  h1.textContent = title;
  container.insertBefore(h1, container.firstChild);
}})();
"""


def title_from_markdown(markdown: str) -> str:
    match = TITLE_RE.search(markdown)
    return text_or_empty(match.group(1)) if match else ""


def safe_filename(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*\s]+', "_", value.strip())
    if not value.lower().endswith(".md"):
        value += ".md"
    return value[:120].strip("_") or "wechat_article.md"


def extract_image_links(markdown: str) -> list[str]:
    seen: set[str] = set()
    links: list[str] = []
    for match in IMAGE_RE.findall(markdown):
        if match not in seen:
            seen.add(match)
            links.append(match)
    return links


def image_extension(url: str, content_type: str = "") -> str:
    query = parse_qs(urlparse(url).query)
    fmt = text_or_empty(query.get("wx_fmt", [""])[0]).lower()
    if fmt in {"jpeg", "jpg"}:
        return ".jpg"
    if fmt in {"png", "gif", "webp", "bmp"}:
        return f".{fmt}"
    content_type = content_type.split(";", 1)[0].strip().lower()
    return {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/bmp": ".bmp",
    }.get(content_type, ".jpg")


def download_images(
    image_links: list[str],
    article_dir: Path,
    timeout_seconds: int,
    warnings: list[str],
) -> tuple[str | None, list[dict[str, Any]]]:
    if not image_links:
        return None, []

    images_dir = article_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Referer": "https://mp.weixin.qq.com/",
    }

    for index, raw_url in enumerate(image_links, start=1):
        url, _fragment = urldefrag(raw_url)
        record: dict[str, Any] = {
            "index": index,
            "url": raw_url,
            "success": False,
            "filename": None,
            "path": None,
            "error": None,
        }
        last_error = None
        for attempt in range(1, 4):
            try:
                request = Request(url, headers=headers)
                with urlopen(request, timeout=timeout_seconds) as response:
                    data = response.read()
                    ext = image_extension(url, response.headers.get("Content-Type", ""))
                filename = f"{index:03d}_image{ext}"
                path = images_dir / filename
                path.write_bytes(data)
                record.update(
                    {
                        "success": True,
                        "filename": filename,
                        "path": str(path),
                        "size": len(data),
                        "attempts": attempt,
                    }
                )
                break
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                if attempt < 3:
                    time.sleep(0.5 * attempt)
        if not record["success"]:
            record["error"] = last_error
            warnings.append(f"image download failed for index {index}: {record['error']}")
        results.append(record)

    return str(images_dir), results


def validate_markdown(markdown: str, result_success: bool) -> tuple[bool, list[str], list[str]]:
    warnings: list[str] = []
    image_links = extract_image_links(markdown)
    stripped = markdown.strip()

    if not result_success:
        warnings.append("crawl4ai reported result.success=false")
    if len(stripped) < MIN_MARKDOWN_LENGTH:
        warnings.append(f"markdown length is below {MIN_MARKDOWN_LENGTH}: {len(stripped)}")
    if any(keyword in markdown for keyword in VERIFY_KEYWORDS):
        warnings.append("wechat verification/interstitial keywords detected")
    if not image_links:
        warnings.append("no remote mmbiz.qpic.cn image links detected")

    passed = result_success and bool(stripped) and not any(
        warning.startswith("wechat verification") for warning in warnings
    )
    passed = passed and len(stripped) >= MIN_MARKDOWN_LENGTH and bool(image_links)
    return passed, warnings, image_links


def result_title(result: Any) -> str:
    metadata = getattr(result, "metadata", {}) or {}
    if isinstance(metadata, dict):
        return text_or_empty(metadata.get("title", ""))
    return ""


def decode_screenshot(screenshot: Any) -> bytes | None:
    if not screenshot:
        return None
    if isinstance(screenshot, bytes):
        return screenshot
    if isinstance(screenshot, str):
        try:
            return base64.b64decode(screenshot)
        except Exception:
            return None
    return None


def cache_mode_disabled(CacheMode: Any) -> Any:
    return getattr(CacheMode, "DISABLED", getattr(CacheMode, "BYPASS", None))


def cache_mode_bypass(CacheMode: Any) -> Any:
    return getattr(CacheMode, "BYPASS", cache_mode_disabled(CacheMode))


def failure_score(markdown: str, result_success: bool, image_links: list[str]) -> tuple[int, int, int, int]:
    has_verification = int(any(keyword in markdown for keyword in VERIFY_KEYWORDS))
    return (int(result_success), -has_verification, len(image_links), len(markdown.strip()))


async def crawl_once(
    url: str,
    css_selector: str,
    args: argparse.Namespace,
    cache_mode: Any,
) -> tuple[Any, str]:
    AsyncWebCrawler, BrowserConfig, _CacheMode, CrawlerRunConfig = import_crawl4ai()

    browser_config = BrowserConfig(
        headless=args.headless,
        viewport_width=1920,
        viewport_height=1800,
        java_script_enabled=True,
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
    )
    run_config = CrawlerRunConfig(
        cache_mode=cache_mode,
        page_timeout=args.timeout,
        wait_for="css:#js_content",
        wait_for_images=True,
        scan_full_page=True,
        js_code=title_injection_js(css_selector),
        screenshot=args.screenshot,
        remove_overlay_elements=True,
        css_selector=css_selector,
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=run_config)
    return result, normalize_markdown(markdown_text(getattr(result, "markdown", "")))


async def crawl_selectors(
    args: argparse.Namespace,
    cache_mode: Any,
    cache_warnings: list[str],
) -> tuple[Any, str, str, list[str], list[str], bool]:
    selectors = ("#js_content", ".rich_media_content", "#img-content")
    best_candidate: tuple[tuple[int, int, int, int], Any, str, str, list[str], list[str]] | None = None

    for index, selector in enumerate(selectors):
        result, markdown = await crawl_once(args.url, selector, args, cache_mode)
        passed, warnings, image_links = validate_markdown(
            markdown, bool(getattr(result, "success", False))
        )
        warnings = cache_warnings + warnings
        score = failure_score(markdown, bool(getattr(result, "success", False)), image_links)
        candidate = (score, result, markdown, selector, warnings, image_links)
        if best_candidate is None or score > best_candidate[0]:
            best_candidate = candidate
        if passed:
            if index > 0:
                warnings.insert(0, f"used alternate selector {selector}")
            return result, markdown, selector, warnings, image_links, True

    if best_candidate is None:
        raise RuntimeError("crawl did not return any selector candidate")
    _score, result, markdown, selector, warnings, image_links = best_candidate
    warnings.append("all selectors failed: #js_content, .rich_media_content, #img-content")
    return result, markdown, selector, warnings, image_links, False


async def crawl_with_retries(args: argparse.Namespace) -> tuple[Any, str, str, list[str], list[str], bool]:
    _AsyncWebCrawler, _BrowserConfig, CacheMode, _CrawlerRunConfig = import_crawl4ai()
    disabled_mode = cache_mode_disabled(CacheMode)
    bypass_mode = cache_mode_bypass(CacheMode)

    cache_warnings: list[str] = []
    if disabled_mode is bypass_mode:
        cache_warnings.append("CacheMode.DISABLED is unavailable; used CacheMode.BYPASS")

    try:
        return await crawl_selectors(args, disabled_mode, cache_warnings)
    except Exception as exc:
        if disabled_mode is bypass_mode:
            raise
        bypass_warnings = [
            f"CacheMode.DISABLED failed with {type(exc).__name__}: {exc}; retried with CacheMode.BYPASS"
        ]
        return await crawl_selectors(args, bypass_mode, bypass_warnings)


def write_outputs(
    result: Any,
    markdown: str,
    selector: str,
    warnings: list[str],
    image_links: list[str],
    passed: bool,
    args: argparse.Namespace,
) -> dict[str, Any]:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    article_dir = Path(args.output) / f"{timestamp}_crawl4ai"
    article_dir.mkdir(parents=True, exist_ok=True)

    md_path = article_dir / safe_filename(args.filename)
    md_path.write_text(markdown, encoding="utf-8")

    images_dir = None
    downloaded_images: list[dict[str, Any]] = []
    if args.images:
        images_dir, downloaded_images = download_images(
            image_links,
            article_dir,
            max(10, min(60, args.timeout // 1000)),
            warnings,
        )

    screenshot_path = None
    if args.screenshot:
        screenshot_bytes = decode_screenshot(getattr(result, "screenshot", None))
        if screenshot_bytes:
            screenshot_path = article_dir / "article.png"
            screenshot_path.write_bytes(screenshot_bytes)
        else:
            warnings.append("screenshot was requested but no screenshot data was returned")

    metadata = {
        "url": args.url,
        "success": passed,
        "crawl4ai_success": bool(getattr(result, "success", False)),
        "title": result_title(result) or title_from_markdown(markdown),
        "selector": selector,
        "output_dir": str(article_dir),
        "output_markdown": str(md_path),
        "output_screenshot": str(screenshot_path) if screenshot_path else None,
        "crawl4ai_base_directory": os.environ.get("CRAWL4_AI_BASE_DIRECTORY"),
        "markdown_length": len(markdown),
        "image_link_count": len(image_links),
        "image_links": image_links,
        "images_dir": images_dir,
        "downloaded_image_count": sum(1 for image in downloaded_images if image.get("success")),
        "downloaded_images": downloaded_images,
        "warnings": warnings,
        "error_message": getattr(result, "error_message", None),
        "fetch_time": datetime.now().isoformat(),
    }
    json_path = article_dir / "crawl4ai_result.json"
    metadata["output_json"] = str(json_path)
    json_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    return metadata


async def async_main() -> int:
    args = parse_args()
    configure_crawl4ai_base_directory(args.output, args.runtime_dir)
    if args.json:
        with contextlib.redirect_stdout(sys.stderr):
            result, markdown, selector, warnings, image_links, passed = await crawl_with_retries(args)
    else:
        result, markdown, selector, warnings, image_links, passed = await crawl_with_retries(args)
    metadata = write_outputs(result, markdown, selector, warnings, image_links, passed, args)

    if args.json:
        print(json.dumps(metadata, ensure_ascii=False, indent=2))
    else:
        status = "ok" if passed else "failed"
        print(f"status: {status}")
        print(f"markdown: {metadata['output_markdown']}")
        print(f"metadata: {metadata['output_json']}")
        if metadata.get("output_screenshot"):
            print(f"screenshot: {metadata['output_screenshot']}")
        if warnings:
            print("warnings:")
            for warning in warnings:
                print(f"- {warning}")

    return 0 if passed else 2


def main() -> None:
    configure_stdio()
    raise SystemExit(asyncio.run(async_main()))


if __name__ == "__main__":
    main()
