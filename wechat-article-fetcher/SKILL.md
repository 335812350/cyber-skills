---
name: wechat-article-fetcher
description: 抓取、归档、保存或转换微信公众号文章，将 `mp.weixin.qq.com` 链接通过 Crawl4AI 导出为 Markdown。Use when Codex receives a WeChat article link, is asked to archive/save/fetch a WeChat article, needs Markdown from a WeChat Official Account article, or needs local image/screenshot/metadata copies.
---

# WeChat Article Fetcher

使用此技能抓取微信公众号文章，并保存一份可迁移归档，包含 Markdown、元数据、页面截图和本地图片副本。

如果用户只发送一个 `mp.weixin.qq.com` 文章链接，也将其视为明确的抓取/归档请求，不需要用户额外说明。

## 运行要求

- 优先使用 Python 3.11+。
- 需要安装 `crawl4ai`，并完成 Playwright 浏览器环境配置。
- 如果缺少 `crawl4ai`，先安装并验证：

```bash
python -m pip install crawl4ai
crawl4ai-setup
crawl4ai-doctor
```

## 默认命令

在 skill 目录下运行内置脚本：

```bash
python scripts/crawl4ai_fetch_wechat.py "<mp.weixin.qq.com article url>" --output ./wechat_articles
```

在 Windows 上，如果 `python` 指向了错误解释器，优先使用可用的 Python 3.11 启动器：

```powershell
py -3.11 scripts\crawl4ai_fetch_wechat.py "<mp.weixin.qq.com article url>" --output .\wechat_articles
```

## 参数

```text
URL                   WeChat article URL
-o, --output PATH     Output root directory, default ./wechat_articles
--filename NAME       Markdown filename, default wechat_article.md
--timeout INTEGER     Page timeout in milliseconds, default 90000
--headless            Run browser headlessly, default
--no-headless         Show browser window
--screenshot          Save article.png, default
--no-screenshot       Skip screenshot
--images              Download body images, default
--no-images           Skip local image copies
--runtime-dir PATH    Crawl4AI internal runtime directory
--json                Print result metadata as JSON
```

默认情况下，脚本会把 Crawl4AI 内部运行文件保存到 `<output>/.crawl4ai_runtime`。如果已经设置 `CRAWL4_AI_BASE_DIRECTORY`，则优先使用该环境变量。需要显式指定时，使用 `--runtime-dir`。

## 输出

每次运行都会创建一个带时间戳的目录：

```text
wechat_articles/
`-- 20260705_002101_crawl4ai/
    |-- wechat_article.md
    |-- crawl4ai_result.json
    |-- article.png
    `-- images/
        |-- 001_image.png
        `-- ...
```

`crawl4ai_result.json` 包含：

- source URL
- success flags
- title
- selected content selector
- Markdown path
- screenshot path
- Crawl4AI runtime directory
- remote `mmbiz.qpic.cn` image links
- local image download results
- warnings and error message
- fetch time

## Markdown 规则

- Markdown 中保留远程图片链接，格式为 `https://mmbiz.qpic.cn/...`。
- 本地图片只作为归档副本保存；不要把 Markdown 里的图片路径改成本地文件路径。
- 将微信页面标题插入为单个 Markdown H1：`# <title>`。
- H1 标题和第一段正文之间必须保留一个空行。
- 正文选择器优先使用 `#js_content`，其次是 `.rich_media_content`，最后是 `#img-content`。
- 如果遇到微信验证页、Markdown 内容过短或图片链接数量为 0，应记录为 warning/failure，不要假装抓取成功。

## 失败处理

如果脚本以非 0 状态退出，或 `crawl4ai_result.json` 中 `success=false`，先检查 `warnings`。常见原因包括：

- 微信验证页或中间页
- 网络问题或页面加载超时
- Playwright 浏览器未安装
- Markdown 低于最低质量阈值
- 未检测到远程 `mmbiz.qpic.cn` 图片链接

如果页面加载较慢，可增加超时时间后重试：

```bash
python scripts/crawl4ai_fetch_wechat.py "<url>" --timeout 120000
```

如果浏览器启动被执行沙箱阻止，请申请在沙箱外运行该命令。
