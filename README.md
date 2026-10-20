<div align="center">

**中文** · [English](./README.en.md)

# 🧰 Cyber Skills

#### 我整理和使用的一些 Skills 和 Prompt，统一放在这里

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-8-10B981?style=for-the-badge)](#-skills)
[![Prompts](https://img.shields.io/badge/Prompts-3-F59E0B?style=for-the-badge)](#-prompts)
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
| 🔥 [**grill-me（拷问我）**](#-grill-me拷问我) | 需求还不够清楚时，让 Agent 连续追问，把计划和设计里的分叉一个个问透 | 原作：Matt Pocock · [Source](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) · [MIT Notice](./grill-me/NOTICE) |
| 🧭 [**find-skills（技能发现）**](#-find-skills技能发现) | 不知道该装哪个 Skill 时，让 Agent 先去开放生态里帮你找、筛、推荐 | Skill |
| 💬 [**wechat-article-fetcher（公众号文章抓取）**](#-wechat-article-fetcher公众号文章抓取) | 把微信公众号文章抓取、归档并导出为 Markdown，同时保存元数据、截图和图片副本 | Skill |
| 🧹 [**disk-cleaner（磁盘清理）**](#-disk-cleaner磁盘清理) | C 盘/D 盘爆满时，用 WizTree 扫描 + AI 分析出一份分级清理方案，每项等你批准才动手，删前自动备份可回滚 | 原作：iziqing · [Source](https://github.com/iziqing/-disk-cleaner) · [MIT Notice](./disk-cleaner/NOTICE) |
| 🧭 [**ai-dev-workflow（AI 开发工作流）**](#-ai-dev-workflowai-开发工作流) | 拿到需求后按「对齐 → 沉淀 Spec → 实现 → 端到端自测 → 交叉审查」推进，内置五个思维快捷键；小改动可直接跳过流程 | 参考：黄同学h · [X 原文](https://x.com/huangtongxueh/status/2108577165306687938) |

### Prompts

| 名字 | 一句话 | 备注 |
|---|---|---|
| 🔭 [**横纵分析法（Prompt 版）**](#-横纵分析法prompt-版) | 上面那个 Skill 的轻量版，复制粘贴到任何 Deep Research 模型里就能跑 | 原作：数字生命卡兹克 · [公众号文章](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |
| 🧰 [**Codex 项目开发系统提示词**](#-codex-项目开发系统提示词) | 给 Codex 项目开发加一套“大型任务先规划、评审、再实现”的流程约束 | [Prompt](./prompts/codex项目开发系统提示词.md) |
| 🧠 [**思维快捷键**](#-思维快捷键) | 五句方法论 Prompt：第一性原理 / 对抗性审查 / 消融实验 / 奥卡姆剃刀 / 高内聚低耦合，附配套技能映射 | 参考：黄同学h · [X 原文](https://x.com/huangtongxueh/status/2108577165306687938) |

---

## 📦 安装方式

在 Claude Code、Codex、OpenClaw 等支持 Skill 的 Agent 里，直接说：

```
帮我安装这个 skill：https://github.com/335812350/cyber-skills/tree/main/<skill-name>
```

把 `<skill-name>` 换成你想装的那个，比如 `neat-freak`、`hv-analysis`、`khazix-writer`、`grill-me`、`find-skills`、`wechat-article-fetcher`、`disk-cleaner`、`ai-dev-workflow`。Agent 会自己 clone 到对应目录，不用你操心路径。

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

### 🔥 grill-me（拷问我）

> 原作：Matt Pocock。已按源文件原样引入，源仓库为 MIT License。

> *"需求越清晰，执行效果才会越好。慢一点把需求问清楚，实现时才能快一点。"*

这是一个极简但很有效的需求澄清 Skill。它不会上来就写方案，而是围绕你的计划或设计持续追问：每个决策分叉怎么选、依赖关系是什么、哪些细节还没说清楚。如果问题能通过读代码回答，它会优先去代码库里找答案。

**适合**

- 复杂项目级重构、跨模块改造、文件迁移这类分叉很多的任务
- 写 plan 之前，把需求、边界、依赖、风险先问透
- 你觉得“需求大概懂了”，但还担心 Agent 执行时理解偏掉

**实测感受**

相比普通 `/plan` 或 brainstorming，它的提问会更多、更细。复杂重构里可能会连续问十几个到二十个问题，把“文件挪到哪里、跨模块依赖怎么处理、循环依赖怎么拆、测试要不要跟着迁移、哪些函数合并或解耦”这些细节提前摊开。

**使用建议**

`grill-me` 本身只负责追问，不一定会自动沉淀文档。问完之后，最好让 Agent 把结论写入 `plan.md`，再做一次 review 或交叉验证；如果任务很大，可以清空上下文后按这份计划执行，保持实现阶段上下文干净。

→ [SKILL.md](./grill-me/SKILL.md) · [Source](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) · [MIT Notice](./grill-me/NOTICE)

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
<table>
<tr><td>

### 💬 wechat-article-fetcher（公众号文章抓取）

> *"给 Agent 一个微信公众号链接，让它把文章保存成可迁移的本地归档。"*

这是一个面向微信公众号文章归档的 Skill。只要用户发送 `mp.weixin.qq.com` 文章链接，Agent 就会把它识别为抓取/归档请求，并通过内置 Crawl4AI 脚本导出 Markdown。

**适合**

- 把公众号文章保存为 Markdown，方便二次阅读、整理或进入写作流程
- 同步保存文章元数据、页面截图和正文图片副本
- 需要把微信文章内容迁移到本地知识库或项目资料夹

**它会做什么**

- 优先抓取微信正文区域，并插入单个 Markdown H1 标题
- 保留 Markdown 中的远程 `mmbiz.qpic.cn` 图片链接
- 将本地图片、截图、抓取结果 JSON 和 Markdown 放入带时间戳的归档目录
- 遇到微信验证页、内容过短或图片缺失时记录 warning/failure，避免误报成功

**运行要求**

需要 Python 3.11+、`crawl4ai` 和 Playwright 浏览器环境。安装后可运行：

```bash
python scripts/crawl4ai_fetch_wechat.py "<mp.weixin.qq.com article url>" --output ./wechat_articles
```

→ [SKILL.md](./wechat-article-fetcher/SKILL.md) · [脚本](./wechat-article-fetcher/scripts/crawl4ai_fetch_wechat.py)

</td></tr>
</table>

---
<table>
<tr><td>

### 🧹 disk-cleaner（磁盘清理）

> 原作：iziqing。已按源文件原样引入，源仓库为 MIT License。

> *"删前必备份，没批复不动手。"*

C 盘 / D 盘爆满时，让 Agent 用 WizTree 快速扫描磁盘，再结合模式库和知识库做两层分析，输出一份**分级清理方案**——每项写清路径、大小、是什么、删了会怎样，逐条编号等你批复。批准之后才动手，删之前自动备份，出问题可以一键回滚。

**适合**

- 系统盘飘红、想安全回收空间但怕误删
- 单个巨型文件（内核转储、Chrome 端侧 AI 模型、半成品下载）占了大量空间却找不到
- 清理完想保留备份观察一段时间，确认没事再删

**安全设计**

- 任何权限模式下，清理方案都必须经用户确认才执行，沉默不算同意
- 备份失败则中止清理；回滚通过 `backup.py restore` 一键恢复
- 红线清单明确列出本次绝不碰的目录；模式库认不出的文件一律不预设可删

**运行要求**

需要 Windows、管理员权限（用于 WizTree 自动扫描）和 Python。流程细节见 [SKILL.md](./disk-cleaner/SKILL.md)。

→ [SKILL.md](./disk-cleaner/SKILL.md) · [Source](https://github.com/iziqing/-disk-cleaner) · [MIT Notice](./disk-cleaner/NOTICE)

</td></tr>
</table>

---
<table>
<tr><td>

### 🧭 ai-dev-workflow（AI 开发工作流）

> 参考：黄同学h《入职大厂两个月，我的 AI 开发心得》。以下是按原文方法论提炼的执行版，非原文全文。

> *"模型变了，工作流也要跟着做减法。"*

一套面向**已有项目迭代**的开发流程。它不会一上来就写代码，而是先判断这次改动值不值得走流程：

- 改一行、改个字段 → 直接改 + 自测，跳过流程
- 单模块小需求 → 对齐 → 实现 → 自测 → 自查
- 跨模块 / 有架构决策 → 走完整五步

**五步**

1. **对齐** — 喂真实材料（PRD、会议纪要、聊天记录），连续追问目标、边界和取舍。停止条件是：剩下的问题已经不会显著改变实现方向。
2. **沉淀** — 结论写进 Spec / `CONTEXT.md`，只记问题、范围、关键决策、验收标准。
3. **实现** — 复杂需求拆成可独立验收的 Issue；只有能独立推进的才交给 subagent 并行。
4. **自测** — 给 Agent 一个能跑通的端到端环境：一键起环境、能操作业务、能查库表和日志、流程固化成 CLI/Skill。**工具提供证据，不定义正确答案。**
5. **审查** — 先看验收标准再看测试；重点检查权限、并发、重试、一致性、迁移回滚；新增抽象再过一遍奥卡姆剃刀。

**内置五个思维快捷键**

第一性原理 · 对抗性审查 · 消融实验 · 奥卡姆剃刀 · 高内聚低耦合。每种都附了可以直接说出口的短句，用来指定"以什么方式思考"，而不是写死一套流程。

**适合**

- 需求说不清、方案有分歧，想先把问题问透再动手
- 想让 AI 自己跑端到端测试，而不是只堆单元测试
- Review AI 写的代码，但不想逐行读完

**不适合**

- 一次性脚本、改配置、改文案这类没有不确定性的任务
- 团队还没有测试环境——这个技能只能告诉你该搭什么，搭不了环境本身

→ [SKILL.md](./ai-dev-workflow/SKILL.md) · [完整笔记](./ai-dev-workflow/references/huang-ai-dev-notes.md) · [X 原文](https://x.com/huangtongxueh/status/2108577165306687938)

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

<table>
<tr><td>

### 🧠 思维快捷键

> 参考：黄同学h《入职大厂两个月，我的 AI 开发心得》。以下为方法论 Prompt 的提炼版，附原文示例。

> *"与其给模型写死一套完整的思考流程，不如告诉它应该以什么方式思考。"*

五句话，分别切换五种思考方式。每句都能直接复制，把括号里的内容换掉即可：

| 方法 | 一句话 Prompt |
|---|---|
| **第一性原理** | `不要基于「<既定方案>」继续设计。从第一性原理分析这个问题，以及最小必要的解决方案。` |
| **对抗性审查** | `对这个方案做一次对抗性审查，优先寻找能推翻核心假设的反例。` |
| **消融实验** | `给这几个优化设计消融实验，判断真正的收益来自哪里。` |
| **奥卡姆剃刀** | `用奥卡姆剃刀重新审查这个设计，在满足需求的前提下删除所有非必要机制。` |
| **高内聚低耦合** | `按高内聚、低耦合原则审查 <服务名> 的职责边界，不要为了拆而拆。` |

**为什么短句有效**：这些方法论在训练数据里已经高度标准化。模型不缺"怎么想"的知识，
缺的只是你指定这次用哪一种。手写几百行 Workflow，模型反而会沿着流程空转。

**组合用法**

```
从第一性原理重新分析，对当前方案做对抗性审查；核心机制必须通过消融实验验证；
方案遵循奥卡姆剃刀，代码保持高内聚、低耦合。
```

对应五种认知动作：重新定义问题 → 攻击假设 → 验证贡献 → 删除复杂度 → 整理边界。

**配套 Skill**

| 阶段 | 配哪个 |
|---|---|
| 需求还没对齐 | `grill-me` |
| 方案设计 / 判断值不值得做 | `think` |
| 方案评审 / Code Review | `check` 或 `code-review` |
| 清理过度设计 | `ponytail` |
| 模块边界设计 | `codebase-design` 或 `domain-modeling` |
| 消融实验 | 无现成 Skill，需要真实可跑的性能测试环境 |

完整的模板、原文示例和适用场景见文件。

→ [思维快捷键.md](./prompts/思维快捷键.md) · [AI 开发工作流](./ai-dev-workflow/SKILL.md) · [X 原文](https://x.com/huangtongxueh/status/2108577165306687938)

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
