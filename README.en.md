<div align="center">

[中文](./README.md) · **English**

# 🧰 Cyber Skills

#### A collection of AI skills and prompts I organize and use

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-8-10B981?style=for-the-badge)](#-skills)
[![Prompts](https://img.shields.io/badge/Prompts-3-F59E0B?style=for-the-badge)](#-prompts)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![OpenCode](https://img.shields.io/badge/OpenCode-Skill-3B82F6?style=flat-square)
![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-8B5CF6?style=flat-square)

</div>

This repository collects Skills and Prompts I use for AI-assisted work. Some entries are from original creators and some are my own working notes; entries that belong to an original creator are marked in their descriptions.

- **Skills** — Structured instruction sets that agents load directly. Follows the [Agent Skills](https://agentskills.io) open standard. Works with Claude Code, Codex, OpenCode, and OpenClaw
- **Prompts** — A single block of text you paste into ChatGPT / Claude / Gemini / any chat. No installation needed

---

## 📋 Index

### Skills

> Grouped into three areas. The first is the full AI development workflow, broken into stages; the other two are standalone capabilities.
> Entries marked **External** live upstream — follow the link in Notes to install them. Everything else can be cloned from this repo.
> Rows marked ⭐ are the set 黄同学h actually uses.

**1. AI development workflow**

> The end-to-end path from a requirement to a merge. `ai-dev-workflow` is the flow itself; the three stages below each have their own skill set.

| Name | One-liner | Notes |
|---|---|---|
| 🧭 [**ai-dev-workflow**](#-ai-dev-workflow) | Runs requirements through align → spec → implement → end-to-end self-test → cross-review, with five "thinking shortcuts" built in; small changes can skip the flow | This repo · Reference: 黄同学h · [Original post](https://x.com/huangtongxueh/status/2108577165306687938) |

**1.1 Planning & requirements** — clarify the requirement and settle the design before writing code

| Name | One-liner | Notes |
|---|---|---|
| 🧠 ⭐ [**think**](https://github.com/tw93/Waza/tree/main/plugins/waza/skills/think) | Turns a rough idea into a decision-complete plan before coding | External · tw93/Waza |
| 🔥 ⭐ [**grill-me**](#-grill-me) | Makes the agent relentlessly question your plan or design until the requirements are clear | This repo · Original: Matt Pocock · [MIT Notice](./grill-me/NOTICE) |
| 📐 [**grill-with-docs**](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) | Relentless interviewing that also produces ADRs and a glossary as it goes | External · mattpocock/skills |

**1.2 Implementation** — write code against the agreed design, no re-litigating requirements

| Name | One-liner | Notes |
|---|---|---|
| ⚙️ ⭐ [**implement**](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement) | Implements an already-agreed spec or ticket without re-litigating requirements | External · mattpocock/skills |

**1.3 Review & wrap-up** — pre-merge checks, cut over-engineering, reconcile docs and hand off

| Name | One-liner | Notes |
|---|---|---|
| ✅ ⭐ [**check**](https://github.com/tw93/Waza/tree/main/plugins/waza/skills/check) | Reviews diffs and PRs against acceptance criteria, then handles merge and release follow-through | External · tw93/Waza |
| 🪶 ⭐ [**ponytail**](https://github.com/DietrichGebert/ponytail) | Strips AI over-engineering so the diff stays small enough to read | External · DietrichGebert/ponytail |
| 🧹 [**neat-freak**](#-neat-freak) | After a session, run `/neat` to reconcile your project docs, CLAUDE.md, and agent memory with the code | This repo · Original: 数字生命卡兹克 · [Article (Chinese)](https://mp.weixin.qq.com/s/tg1wd-iN2gWHWhXdY0faeg) |
| 🤝 ⭐ [**handoff**](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) | Compacts the current conversation into a handoff document for another agent or session | External · mattpocock/skills |

**2. Writing & research** — content production and research, outside the coding flow

| Name | One-liner | Notes |
|---|---|---|
| ✍️ [**khazix-writer**](#-khazix-writer) | Makes the agent write long-form Chinese articles in the voice of 数字生命卡兹克 | This repo · Original: 数字生命卡兹克 · [Article (Chinese)](https://mp.weixin.qq.com/s/AtxGrii_K-nzkwUM9SNhEg) |
| 🔭 [**hv-analysis**](#-hv-analysis) | Drop a product/company/concept into it and get a 10k–30k word PDF research report | This repo · Original: 数字生命卡兹克 · [Article (Chinese)](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |

**3. Tools & system** — runtime, disk, skill discovery and other utilities

| Name | One-liner | Notes |
|---|---|---|
| 🧭 [**find-skills**](#-find-skills) | Helps the agent search, vet, and recommend skills from the open ecosystem | This repo |
| 💬 [**wechat-article-fetcher**](#-wechat-article-fetcher) | Fetches and archives WeChat Official Account articles as Markdown, with metadata, screenshots, and image copies | This repo |
| 🧹 [**disk-cleaner**](#-disk-cleaner) | When C:/D: is full, scans with WizTree and uses AI analysis to produce a tiered cleanup plan; every item waits for your approval before acting, with automatic backup and rollback | This repo · Original: iziqing · [Source](https://github.com/iziqing/-disk-cleaner) · [MIT Notice](./disk-cleaner/NOTICE) |

### Prompts

| Name | One-liner | Notes |
|---|---|---|
| 🔭 [**hv-analysis (Prompt edition)**](#-hv-analysis-prompt-edition) | Lighter version of the skill above — paste it into any Deep Research model | Original: 数字生命卡兹克 · [Article (Chinese)](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |
| 🧰 [**Codex project development system prompt**](#-codex-project-development-system-prompt) | Adds a plan-review-implement workflow for larger Codex coding tasks | [Prompt](./prompts/codex项目开发系统提示词.md) |
| 🧠 [**Thinking shortcuts**](#-thinking-shortcuts) | Five methodology prompts: first principles / adversarial review / ablation / Occam's razor / high cohesion, with companion skills | Reference: 黄同学h · [Original post](https://x.com/huangtongxueh/status/2108577165306687938) |

---

## 📦 Install

In any agent that supports Skills (Claude Code, Codex, OpenClaw…), just say:

```
Install this skill: https://github.com/335812350/cyber-skills/tree/main/<skill-name>
```

Replace `<skill-name>` with the one you want — e.g. `neat-freak`, `hv-analysis`, `khazix-writer`, `grill-me`, `find-skills`, `wechat-article-fetcher`, `disk-cleaner`, `ai-dev-workflow`. The agent will clone it into the right directory for you.

Skills marked **External** (`think`, `check`, `implement`, `handoff`, `grill-with-docs`, `ponytail`) are not in this repo — install them from the upstream links in the index so there is only one copy to maintain.

---

## ✨ Skills

<a id="-skills"></a>

**1. AI development workflow** — the end-to-end path from a requirement to a merge

> External skills in this group: `think`, `grill-with-docs`, `implement`, `check`, `ponytail`, `handoff`. They live upstream — see the index above.

<table>
<tr><td>

### 🧭 ai-dev-workflow

> Reference: 黄同学h, "入职大厂两个月，我的 AI 开发心得". An executable distillation of the original methodology, not the article text.

> *"When the model changes, the workflow has to shed weight too."*

A development workflow for **iterating on an existing project**. It does not start by writing code — it first decides whether the change is worth running a process at all:

- One line, a field, a validation rule → just do it, skip the flow
- A single-module feature → align → implement → self-test → self-review
- Cross-module or architectural → run all five steps

**The five steps**

1. **Align** — feed real material (PRD, meeting notes, chat logs) and keep asking about goals, boundaries, and trade-offs. Stop when the remaining questions no longer change the direction of implementation.
2. **Write it down** — put the problem, scope, key decisions, and acceptance criteria into a spec or `CONTEXT.md`.
3. **Implement** — split complex work into independently acceptable issues; only genuinely independent parts go to parallel subagents.
4. **Self-test end to end** — one-command environments, the ability to drive the real business flow, read-only DB and log access, and the repeatable parts packaged as scripts or a CLI. **Tools provide evidence; they do not define the correct answer.**
5. **Review** — acceptance criteria before test results; focus on permissions, concurrency, retries, consistency, migrations and rollback; re-check new abstractions with Occam's razor.

**Five built-in thinking shortcuts**

First principles · Adversarial review · Ablation · Occam's razor · High cohesion / low coupling — each with a sentence you can say verbatim, used to specify *how* to think rather than a fixed script.

**Good for**

- Fuzzy requirements or competing designs that need pressure-testing first
- Letting the agent run end-to-end tests instead of piling up unit tests
- Reviewing AI-written code without reading every line

**Not for**

- One-off scripts, config edits, copy changes — anything with no real uncertainty
- Teams with no test environment yet; the skill tells you what to build, it cannot build it

→ [SKILL.md](./ai-dev-workflow/SKILL.md) · [Full notes](./ai-dev-workflow/references/huang-ai-dev-notes.md) · [Original post](https://x.com/huangtongxueh/status/2108577165306687938)

</td></tr>
</table>

**1.1 Planning & requirements** — clarify the requirement and settle the design before writing code

<table>
<tr><td>

### 🔥 grill-me

> Original: Matt Pocock. Imported from the source skill as-is. The source repository is MIT licensed.

> *"Slow down while clarifying the requirement so implementation can move faster."*

An extremely small but useful requirements-clarification skill. Instead of jumping straight into a plan, it keeps questioning your plan or design: which branch of the decision tree should be chosen, what depends on what, and which details are still underspecified. If the codebase can answer a question, the agent should inspect the codebase instead.

**Good for**

- Complex refactors, cross-module changes, file moves, and other tasks with many decision branches
- Clarifying requirements, boundaries, dependencies, and risks before writing a plan
- Cases where the agent seems to understand the task, but you want to stress-test that understanding first

**Usage notes**

`grill-me` only asks questions. After the interview, ask the agent to write the conclusions into a `plan.md`, then review or cross-check that plan before implementation. For large tasks, this keeps the execution context cleaner and reduces avoidable rework.

→ [SKILL.md](./grill-me/SKILL.md) · [Source](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) · [MIT Notice](./grill-me/NOTICE)

</td></tr>
</table>

**1.2 Implementation** — write code against the agreed design, no re-litigating requirements

> Not hosted here — use the external `implement` skill; see the index above.

**1.3 Review & wrap-up** — pre-merge checks, cut over-engineering, reconcile docs and hand off

<table>
<tr><td>

### 🧹 neat-freak

> Original: 数字生命卡兹克. The description below is adapted from the original public introduction.

> *"If I don't run /neat before closing the window, I get itchy. Like there's something stuck in my throat."*

After every session, run `/neat`. It reconciles whatever you changed in this conversation against three layers of project knowledge: **docs**, **root CLAUDE.md / AGENTS.md**, and the **agent's memory system**. Outputs a change summary at the end.

**Why you'd want this**

You've probably hit this: code has been through 7-8 iterations but the README is still v1.0.0. Memory says you're using SQLite when you actually switched to PostgreSQL months ago. CLAUDE.md lists routes that no longer match the actual server.

The agent isn't getting dumber — your docs and memory are. neat-freak's job is to clean it up.

**It touches three layers**

- Project root CLAUDE.md / AGENTS.md (read by the AI in this project)
- Project docs/ and README (read by teammates and downstream developers)
- The agent's own memory system (read by future you across sessions)

These three layers have different audiences and don't overlap. That's exactly why the original author wasn't satisfied with Claude Code's AutoDream — it only touched memory, leaving the docs to rot.

**How to trigger**

```
/neat            # direct command
sync up          # natural language
tidy up docs     # natural language
整理一下          # 中文
```

**🌐 Cross-platform**: Claude Code · Codex · OpenCode · OpenClaw

[![ClawHub](https://img.shields.io/badge/ClawHub-v1.0.1-EC4899?style=flat-square)](https://clawhub.ai)
[![Tessl](https://img.shields.io/badge/Tessl-0.1.1-3B82F6?style=flat-square)](https://tessl.io/registry/khazix-skills/neat-freak)

→ [SKILL.md](./neat-freak/SKILL.md) · [Article (Chinese)](https://mp.weixin.qq.com/s/tg1wd-iN2gWHWhXdY0faeg)

</td></tr>
</table>

**2. Writing & research** — content production and research, outside the coding flow

<table>
<tr><td>

### ✍️ khazix-writer

> Original: 数字生命卡兹克. The description below is adapted from the original public introduction.

> *"A knowledgeable normal person earnestly talking about something that moved them."*

The writing skill behind 数字生命卡兹克's Chinese long-form articles. Once installed, the agent tries to write in **his voice, rhythm, and list of banned phrases**.

> ⚠️ **Note for English readers**: This skill produces **Chinese** long-form articles (公众号 / WeChat-style). If your output language is English, this isn't for you. But you might find the methodology interesting as a reference for how to encode a personal voice into a skill.

**Good for**

You've read his Chinese articles, like the style, and want your AI to write in the same voice. Hand it a PDF, a transcript, or a news link — it'll turn it into a long-form piece.

**Not good for**

You want "good general writing." This skill takes a position. It **refuses** corporate jargon, **refuses** "first... second... finally" structures, **refuses** "in today's rapidly evolving AI landscape" openings. If your target reader actually likes that stuff, this skill isn't for you.

**What's inside**

- Complete style rules (rhythm, narrative, judgment, rhetoric)
- A four-layer self-check system (structure, rhythm, content, language)
- A curated style example library the AI can match against

[![ClawHub](https://img.shields.io/badge/ClawHub-v1.0.0-EC4899?style=flat-square)](https://clawhub.ai)
[![Tessl](https://img.shields.io/badge/Tessl-0.1.1-3B82F6?style=flat-square)](https://tessl.io/registry/khazix-skills/khazix-writer)

→ [SKILL.md](./khazix-writer/SKILL.md) · [Article (Chinese)](https://mp.weixin.qq.com/s/AtxGrii_K-nzkwUM9SNhEg)

</td></tr>
</table>

<table>
<tr><td>

### 🔭 hv-analysis (Horizontal-Vertical Analysis)

> Original: 数字生命卡兹克. The description below is adapted from the original public introduction.

> *"Vertical axis chases time depth, horizontal axis chases simultaneous breadth. They cross to give you the verdict."*

Want to actually understand what a product / company / concept / person is about? Hand it over.

It runs two threads in parallel: **vertical** — tells the subject's story from inception to the present moment, like a narrative; **horizontal** — lays out every major competitor at the current moment for comparison. When the two cross, you see things that neither current-state nor history alone would show you.

The output is a **typeset PDF research report**, 10,000–30,000 words.

**Good for**

- Competitor research / understanding a new concept / company background research
- Front-loaded research before writing or strategy work
- Wanting to understand a domain from scratch

**Not good for**

- A simple definition lookup — overkill, just ask in regular chat
- Writing a long-form article — that's [khazix-writer](#-khazix-writer)'s job

[![ClawHub](https://img.shields.io/badge/ClawHub-v1.0.0-EC4899?style=flat-square)](https://clawhub.ai)
[![Tessl](https://img.shields.io/badge/Tessl-published-3B82F6?style=flat-square)](https://tessl.io/registry/khazix-skills/hv-analysis)

→ [SKILL.md](./hv-analysis/SKILL.md) · [Article (Chinese)](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA)

</td></tr>
</table>

**3. Tools & system** — runtime, disk, skill discovery and other utilities

<table>
<tr><td>

### 🧭 find-skills

> *"When you don't know which Skill to install, let it search the ecosystem first."*

A skill that helps agents discover, evaluate, and install useful skills from the open skills ecosystem.

**Good for**

- Checking whether an existing Skill already covers a task
- Searching by keywords like React, testing, deployment, or docs
- Having the agent evaluate candidates before recommending an install

**What it does**

- Checks the [skills.sh](https://skills.sh/) leaderboard first
- Runs `npx skills find <query>` for targeted searches
- Filters candidates by install count, source reputation, and GitHub stars
- Returns install commands and links for follow-up reading

→ [SKILL.md](./find-skills/SKILL.md) · [skills.sh](https://skills.sh/)

</td></tr>
</table>

<table>
<tr><td>

### 💬 wechat-article-fetcher

> *"Give the agent a WeChat article link and let it save a portable local archive."*

A skill for archiving WeChat Official Account articles. When a user sends an `mp.weixin.qq.com` article link, the agent treats it as a fetch/archive request and exports the article to Markdown through the included Crawl4AI script.

**Good for**

- Saving WeChat articles as Markdown for reading, writing, or knowledge-base workflows
- Keeping article metadata, a page screenshot, and local copies of body images
- Migrating WeChat article content into a local project folder

**What it does**

- Prioritizes the main WeChat article body and inserts a single Markdown H1 title
- Keeps remote `mmbiz.qpic.cn` image URLs in the Markdown
- Saves local images, screenshot, crawl result JSON, and Markdown into a timestamped archive folder
- Records warnings or failures for verification pages, short content, or missing image links instead of pretending the fetch succeeded

**Requirements**

Requires Python 3.11+, `crawl4ai`, and a configured Playwright browser environment. After setup, run:

```bash
python scripts/crawl4ai_fetch_wechat.py "<mp.weixin.qq.com article url>" --output ./wechat_articles
```

→ [SKILL.md](./wechat-article-fetcher/SKILL.md) · [Script](./wechat-article-fetcher/scripts/crawl4ai_fetch_wechat.py)

</td></tr>
</table>

<table>
<tr><td>

### 🧹 disk-cleaner

> Original: iziqing. Imported from the source skill as-is. The source repository is MIT licensed.

> *"Back up before deleting; nothing moves without your approval."*

When your C: or D: drive is full, the agent scans it with WizTree, runs two layers of analysis (pattern library + knowledge base), and produces a **tiered cleanup plan** — every item lists path, size, what it is, and what happens if you delete it, numbered so you can approve items one by one. Nothing is touched until you approve, everything is backed up before deletion, and a rollback restores backups in one step.

**Good for**

- A red system drive where you want to reclaim space safely, without risky deletions
- Huge single files (kernel dumps, Chrome on-device AI models, half-finished downloads) eating space and hiding from view
- Keeping the backup around for an observation period after cleanup, deleting it only once things look fine

**Safety design**

- In any permission mode, the cleanup plan must be approved by the user before execution; silence is not consent
- Backup failure aborts the cleanup; rollback runs via `backup.py restore`
- A red-line list spells out what this run will never touch; files the pattern library can't classify are never assumed deletable

**Requirements**

Requires Windows, administrator privileges (for the automatic WizTree scan), and Python. See [SKILL.md](./disk-cleaner/SKILL.md) for the full workflow.

→ [SKILL.md](./disk-cleaner/SKILL.md) · [Source](https://github.com/iziqing/-disk-cleaner) · [MIT Notice](./disk-cleaner/NOTICE)

</td></tr>
</table>

---

## 📝 Prompts

<a id="-prompts"></a>

<table>
<tr><td>

### 🔭 hv-analysis (Prompt edition)

> Original: 数字生命卡兹克. The description below is adapted from the original public introduction.

A **lighter version** of the hv-analysis skill above — a single prompt you paste into any Deep Research model (ChatGPT Deep Research, Gemini Deep Research, Grok Deep Search, Claude Research). No installation required.

About 30 minutes to a 10k+ word research report.

Good for people who haven't picked up Claude Code / Codex yet but still want to try the method.

→ [横纵分析法.md](./prompts/横纵分析法.md) · [Article (Chinese)](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA)

</td></tr>
</table>

<table>
<tr><td>

### 🧰 Codex project development system prompt

A system prompt for Codex-based project development. It turns larger tasks into a fixed workflow: plan first, review with Codex, revise feasibility, then implement.

It asks the agent to detect large tasks, create `./md/plan-{feature}-{date}.md`, run a non-interactive Codex review, revise into an executable Plan v2, break implementation down to file / class / method-level To-Dos, and then produce implementation and review records after coding.

Useful when you want stronger engineering guardrails around complex project changes instead of letting the agent jump straight into code.

→ [codex项目开发系统提示词.md](./prompts/codex项目开发系统提示词.md)

</td></tr>
</table>

<table>
<tr><td>

### 🧠 Thinking shortcuts

> Reference: 黄同学h, "入职大厂两个月，我的 AI 开发心得". A distilled version of the methodology prompts, with the original examples.

> *"Instead of hard-coding a full thinking process, tell the model how to think."*

Five sentences, each switching to a different mode of thinking. Copy one and replace the placeholder:

| Method | Prompt |
|---|---|
| **First principles** | `Do not keep designing around "<the existing plan>". Start from first principles: why is this a problem, and what is the minimal necessary solution?` |
| **Adversarial review** | `Run an adversarial review of this design. Prioritize counterexamples that could overturn its core assumptions.` |
| **Ablation** | `Design ablation experiments for these optimizations and determine where the real gain comes from.` |
| **Occam's razor** | `Re-examine this design with Occam's razor and remove every mechanism that is not necessary to meet the requirements.` |
| **High cohesion, low coupling** | `Review the responsibility boundary of <ServiceName> under high cohesion / low coupling. Do not split for the sake of splitting.` |

**Why short prompts work**: these methodologies are already heavily represented in training data. The model does not lack knowledge of *how* to think — it only needs you to pick which way. A few hundred lines of workflow often just makes the model walk the script even when a step is unnecessary.

**Combined**

```
Start from first principles, run an adversarial review of the current design, verify core
mechanisms with ablation experiments, apply Occam's razor, and keep the code high-cohesion.
```

Five cognitive moves: redefine the problem → attack the assumptions → verify the contribution → remove complexity → clean up boundaries.

**Companion skills**

| Stage | Skill |
|---|---|
| Requirements not aligned yet | `grill-me` |
| Design / is it worth building | `think` |
| Design review / code review | `check` or `code-review` |
| Removing over-engineering | `ponytail` |
| Module boundaries | `codebase-design` or `domain-modeling` |
| Ablation | None yet — needs a real, runnable performance harness |

Full templates, original examples and when-to-use notes are in the file.

→ [思维快捷键.md](./prompts/思维快捷键.md) · [AI dev workflow](./ai-dev-workflow/SKILL.md) · [Original post](https://x.com/huangtongxueh/status/2108577165306687938)

</td></tr>
</table>

---

## 🌟 About

I'm 赛博包工头. My WeChat public account is 「赛博包工头」.

This repository collects Skills and Prompts I use for AI-assisted work. Entries that belong to original creators are marked in their own sections. If they help you, a ⭐ is appreciated. Questions or suggestions welcome in Issues / Discussions.

---

<div align="center">

[MIT License](./LICENSE) · Free to use, modify, and redistribute

Made by 赛博包工头

</div>
