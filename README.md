<div align="center">

**中文** · [English](./README.en.md)

# 🧰 Cyber Skills

#### 我整理和使用的一些 Skills 和 Prompt，统一放在这里

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-4-10B981?style=for-the-badge)](#-skills)
[![Prompts](https://img.shields.io/badge/Prompts-2-F59E0B?style=for-the-badge)](#-prompts)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![OpenCode](https://img.shields.io/badge/OpenCode-Skill-3B82F6?style=flat-square)
![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-8B5CF6?style=flat-square)

</div>

这个仓库用来整理我在 AI 协作开发里常用的 Skills 和 Prompts。部分内容来自原作者，部分是自用沉淀；属于原作者的条目会在对应说明里明确标注。

- **Skills** — Agent 能直接加载的结构化指令集，遵循 [Agent Skills](https://agentskills.io) 开放标准。Claude Code、Codex、OpenCode、OpenClaw 都能装
- **Prompts** — 一段提示词，复制粘贴到 ChatGPT / Claude / Gemini 任何对话里就能用，不需要安装

---

## 📋 目录

### Skills

| 名字 | 一句话 | 备注 |
|---|---|---|
| 🧹 [**neat-freak（洁癖）**](#-neat-freak洁癖) | 干完活跑一下 `/neat`，自动把你这次改的东西跟项目文档、CLAUDE.md、Agent 记忆全部对齐 | 原作：数字生命卡兹克 · [公众号文章](https://mp.weixin.qq.com/s/tg1wd-iN2gWHWhXdY0faeg) |
| 🔭 [**hv-analysis（横纵分析法）**](#-hv-analysis横纵分析法) | 想搞懂一个产品/公司/概念是怎么回事，丢给它，给你一份万字 PDF 研究报告 | 原作：数字生命卡兹克 · [公众号文章](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |
| ✍️ [**khazix-writer（卡兹克写作）**](#-khazix-writer卡兹克写作) | 装上之后，Agent 按数字生命卡兹克的口吻和节奏写公众号长文 | 原作：数字生命卡兹克 · [公众号文章](https://mp.weixin.qq.com/s/AtxGrii_K-nzkwUM9SNhEg) |
| 🧭 [**find-skills（技能发现）**](#-find-skills技能发现) | 不知道该装哪个 Skill 时，让 Agent 先去开放生态里帮你找、筛、推荐 | Skill |

### Prompts

| 名字 | 一句话 | 备注 |
|---|---|---|
| 🔭 [**横纵分析法（Prompt 版）**](#-横纵分析法prompt-版) | 上面那个 Skill 的轻量版，复制粘贴到任何 Deep Research 模型里就能跑 | 原作：数字生命卡兹克 · [公众号文章](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |
| 🧰 [**Codex 项目开发系统提示词**](#-codex-项目开发系统提示词) | 给 Codex 项目开发加一套“大型任务先规划、评审、再实现”的流程约束 | [Prompt](./prompts/codex项目开发系统提示词.md) |

---

## 📦 安装方式

在 Claude Code、Codex、OpenClaw 等支持 Skill 的 Agent 里，直接说：

```
帮我安装这个 skill：https://github.com/335812350/cyber-skills/tree/main/<skill-name>
```

把 `<skill-name>` 换成你想装的那个，比如 `neat-freak`、`hv-analysis`、`khazix-writer`、`find-skills`。Agent 会自己 clone 到对应目录，不用你操心路径。

---

## ✨ Skills

<a id="-skills"></a>

<table>
<tr><td>

### 🧹 neat-freak（洁癖）

> 原作：数字生命卡兹克。以下说明基于原作者公开介绍整理。

> *"每次任务做完要退出窗口的时候，如果不跑一遍 /neat，我就浑身难受，如坐针毡如芒刺背如鲠在喉。"*

每次你在 Agent 里干完一件事，跑一下 `/neat`，它会把你这次会话改的东西，跟项目里的**文档**、**CLAUDE.md / AGENTS.md**、**Agent 记忆**全部对齐一遍，最后给你一份变更摘要。

**为什么需要这个**

你大概也遇到过：代码都迭代了七八轮，文档还是最初那一版；记忆里写着用 SQLite，其实你早换 PostgreSQL 了；CLAUDE.md 里的接口列表跟实际路由对不上。Agent 看着这些过期信息，越用越笨。

不是模型变笨，是文档和记忆脑腐了。neat-freak 就是清这个的。

**它会动哪三层东西**

- 项目根的 CLAUDE.md / AGENTS.md（给当前 AI 看的）
- 项目的 docs/ 和 README（给同事和其他人看的）
- Agent 自己的记忆系统（给跨会话的自己看的）

这三层受众不同，职责不重叠，得分别处理。这也是原作者当时不满意 Claude Code 那个 AutoDream 的原因——它只动记忆，不动文档。

**怎么触发**

```
/neat            # 直接命令
整理一下          # 自然语言
同步一下          # 自然语言
sync up          # English
```

**🌐 跨平台**：Claude Code · Codex · OpenCode · OpenClaw

[![ClawHub](https://img.shields.io/badge/ClawHub-v1.0.1-EC4899?style=flat-square)](https://clawhub.ai)
[![Tessl](https://img.shields.io/badge/Tessl-0.1.1-3B82F6?style=flat-square)](https://tessl.io/registry/khazix-skills/neat-freak)

→ [SKILL.md](./neat-freak/SKILL.md) · [公众号讲解](https://mp.weixin.qq.com/s/tg1wd-iN2gWHWhXdY0faeg)

</td></tr>
</table>

<table>
<tr><td>

### 🔭 hv-analysis（横纵分析法）

> 原作：数字生命卡兹克。以下说明基于原作者公开介绍整理。

> *"纵向追时间深度，横向追同期广度，最终交汇出判断。"*

想搞懂一个产品 / 公司 / 概念 / 人物到底是怎么回事，丢给它就行。

它会同时跑两条线：**纵向**把研究对象从诞生讲到当下，像讲故事一样把演变讲完整；**横向**把同期所有主要竞品摆出来逐一对比。最后两条线一交叉，能看出一些只看现状或只看历史看不出来的东西。

最后给你一份**排版精美的 PDF 研究报告**，10,000–30,000 字。

**适合**

- 调研竞品 / 调研一个新概念 / 调研一个公司
- 写作前期需要系统性的素材准备
- 对一个领域想从零搞懂

**不适合**

- 单纯查个名词解释 — 那种问题用普通对话就行，杀鸡用牛刀
- 写公众号文章 — 那个用下面的 khazix-writer

[![ClawHub](https://img.shields.io/badge/ClawHub-v1.0.0-EC4899?style=flat-square)](https://clawhub.ai)
[![Tessl](https://img.shields.io/badge/Tessl-published-3B82F6?style=flat-square)](https://tessl.io/registry/khazix-skills/hv-analysis)

→ [SKILL.md](./hv-analysis/SKILL.md) · [公众号讲解](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA)

</td></tr>
</table>

<table>
<tr><td>

### ✍️ khazix-writer（卡兹克写作）

> 原作：数字生命卡兹克。以下说明基于原作者公开介绍整理。

> *"有见识的普通人在认真聊一件打动他的事。"*

这是数字生命卡兹克用于公众号长文写作的 skill。装上之后，Agent 会尽量复刻他的口吻、节奏和禁忌词。

**适合**

你看过他公众号「数字生命卡兹克」的文章，觉得风格还行，想让你的 AI 也照着这个调子写东西。比如丢一篇 PDF / 一段语音转文字 / 一个新闻链接，让它写成长文。

**不适合**

你想要的是"通用好文笔"。这个 skill 是有立场的——它会**拒绝**写「赋能、抓手、闭环」、**拒绝**「首先...其次」、**拒绝**「在当今 AI 快速发展的时代」、**拒绝**「说白了 / 本质上 / 换句话说」。如果你的目标读者就好这一口，那这个 skill 不适合你。

**它会做什么**

- 完整的写作风格规则（节奏、叙事、判断、修辞）
- 四层自检体系（结构、节奏、内容、文字）
- 一套风格示例库（可以让 AI 直接对照）

[![ClawHub](https://img.shields.io/badge/ClawHub-v1.0.0-EC4899?style=flat-square)](https://clawhub.ai)
[![Tessl](https://img.shields.io/badge/Tessl-0.1.1-3B82F6?style=flat-square)](https://tessl.io/registry/khazix-skills/khazix-writer)

→ [SKILL.md](./khazix-writer/SKILL.md) · [公众号讲解](https://mp.weixin.qq.com/s/AtxGrii_K-nzkwUM9SNhEg)

</td></tr>
</table>

---

<table>
<tr><td>

### 🧭 find-skills（技能发现）

> *"不知道该装哪个 Skill 的时候，先让它帮你找一圈。"*

这是一个专门帮 Agent 在开放 Skill 生态里发现、筛选和安装合适技能的 Skill。

**适合**

- 想知道某个任务有没有现成 Skill
- 想按 React、测试、部署、文档等关键词搜索 Skill
- 想让 Agent 对候选 Skill 做质量判断，再给你安装建议

**它会做什么**

- 优先查看 [skills.sh](https://skills.sh/) 榜单
- 用 `npx skills find <query>` 搜索相关 Skill
- 根据安装量、来源声誉、GitHub stars 做基础筛选
- 给出安装命令和学习链接

→ [SKILL.md](./find-skills/SKILL.md) · [skills.sh](https://skills.sh/)

</td></tr>
</table>

---
## 📝 Prompts

<a id="-prompts"></a>

<table>
<tr><td>

### 🔭 横纵分析法（Prompt 版）

> 原作：数字生命卡兹克。以下说明基于原作者公开介绍整理。

上面那个 hv-analysis Skill 的**轻量版**——一段 prompt，复制粘贴到任何支持 Deep Research 的模型里就能跑（ChatGPT Deep Research、Gemini Deep Research、Grok Deep Search、Claude Research 都行），不需要安装任何东西。

半小时左右出一份万字级研究报告。

适合还没开始用 Claude Code / Codex 这类带 Skill 系统的 Agent，但又想体验一下这个方法论的人。

→ [横纵分析法.md](./prompts/横纵分析法.md) · [公众号讲解](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA)

</td></tr>
</table>

<table>
<tr><td>

### 🧰 Codex 项目开发系统提示词

一段面向 Codex 项目开发的系统提示词，用来把大型任务固定成“方案先行 → Codex 评审 → 可行性校正 → 再实现”的流程。

它会要求 Agent 先识别大型任务，创建 `./md/plan-{功能名称}-{日期}.md`，经过非交互 Codex review 和 Plan v2 修订后，再拆解到文件 / 类 / 方法级 To-Do，并在实现完成后生成实施文档和代码审查记录。

适合需要更强工程约束的项目协作场景，避免 Agent 直接开写复杂需求，最后才发现方案不对。

→ [codex项目开发系统提示词.md](./prompts/codex项目开发系统提示词.md)

</td></tr>
</table>

---

## 🌟 关于

我是赛博包工头，公众号「赛博包工头」。

这个仓库用来整理我在 AI 协作开发里常用的 Skills 和 Prompts。涉及原作者的内容，会在对应条目中标注；如果对你有帮助，给个 ⭐ 就行。有问题或建议，欢迎在 Issues / Discussions 里说一声。

---

<div align="center">

[MIT License](./LICENSE) · 自由使用 / 修改 / 再分发

Made by 赛博包工头

</div>
