<div align="center">

[中文](./README.md) · **English**

# 🧰 Cyber Skills

#### A collection of AI skills and prompts I organize and use

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-4-10B981?style=for-the-badge)](#-skills)
[![Prompts](https://img.shields.io/badge/Prompts-2-F59E0B?style=for-the-badge)](#-prompts)
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

| Name | One-liner | Notes |
|---|---|---|
| 🧹 [**neat-freak**](#-neat-freak) | After a session, run `/neat` to reconcile your project docs, CLAUDE.md, and agent memory with the code | Original: 数字生命卡兹克 · [Article (Chinese)](https://mp.weixin.qq.com/s/tg1wd-iN2gWHWhXdY0faeg) |
| 🔭 [**hv-analysis**](#-hv-analysis) | Drop a product/company/concept into it and get a 10k–30k word PDF research report | Original: 数字生命卡兹克 · [Article (Chinese)](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |
| ✍️ [**khazix-writer**](#-khazix-writer) | Makes the agent write long-form Chinese articles in the voice of 数字生命卡兹克 | Original: 数字生命卡兹克 · [Article (Chinese)](https://mp.weixin.qq.com/s/AtxGrii_K-nzkwUM9SNhEg) |
| 🧭 [**find-skills**](#-find-skills) | Helps the agent search, vet, and recommend skills from the open ecosystem | Skill |

### Prompts

| Name | One-liner | Notes |
|---|---|---|
| 🔭 [**hv-analysis (Prompt edition)**](#-hv-analysis-prompt-edition) | Lighter version of the skill above — paste it into any Deep Research model | Original: 数字生命卡兹克 · [Article (Chinese)](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |
| 🧰 [**Codex project development system prompt**](#-codex-project-development-system-prompt) | Adds a plan-review-implement workflow for larger Codex coding tasks | [Prompt](./prompts/codex项目开发系统提示词.md) |

---

## 📦 Install

In any agent that supports Skills (Claude Code, Codex, OpenClaw…), just say:

```
Install this skill: https://github.com/335812350/cyber-skills/tree/main/<skill-name>
```

Replace `<skill-name>` with the one you want — e.g. `neat-freak`, `hv-analysis`, `khazix-writer`, `find-skills`. The agent will clone it into the right directory for you.

---

## ✨ Skills

<a id="-skills"></a>

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

---

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

---

## 🌟 About

I'm 赛博包工头. My WeChat public account is 「赛博包工头」.

This repository collects Skills and Prompts I use for AI-assisted work. Entries that belong to original creators are marked in their own sections. If they help you, a ⭐ is appreciated. Questions or suggestions welcome in Issues / Discussions.

---

<div align="center">

[MIT License](./LICENSE) · Free to use, modify, and redistribute

Made by 赛博包工头

</div>
