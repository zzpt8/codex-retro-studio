---
name: codex-retro-studio
description: Chinese end-to-end Codex retrospective workflow that combines review of what happened inside Codex with report restructuring and PPVI-style visual packaging. Use when the user asks for daily, weekly, deep weekly, or monthly review of Codex threads, outputs, unfinished work, usage patterns, or next actions, especially when they also want a report, page draft, long image, presentation draft, or polished retrospective artifact. Trigger on requests such as "开始每日复盘", "开始周复盘", "深度复盘", "近一个月复盘", "输出报告", or "出长图". Do not use for personal life journaling, generic design critique without retrospective content, or standalone UI styling tasks that should go directly to `ppvi`.
---

# Codex Retro Studio

## Overview

Use this skill as the top-level retrospective orchestrator.

It is not just a review skill and not just a design skill. It handles the full chain:

```text
Codex work review
-> report restructuring
-> PPVI-style visual critique
-> long-image or page-ready draft
```

## Core Positioning

Treat this skill as the combined workflow above two existing capabilities:

- `codex-daily-review` answers: what happened in Codex, what shipped, what is unfinished, and what to do next.
- `ppvi` answers: how to compress, structure, and visually express that review so it is readable and presentable.

Do not merge their bodies mechanically. Use this skill to orchestrate them in sequence.

Keep the review honest first. Only then package it.

## Hard Boundaries

Do not use this skill when:

- the user wants personal journaling rather than Codex work review
- the user only wants visual restyling with no retrospective content
- the user only wants a standalone design system opinion
- the user only wants to write to Obsidian or a goal journal

In those cases:

- use `codex-daily-review` for plain Codex review without packaging
- use `ppvi` for design-only critique or visual decision-making
- use `goal-journal` for personal goal journaling

## Review Scope

Review what the user did inside Codex:

- threads
- tasks
- files and deliverables
- decisions
- blockers
- reusable rules
- unfinished work
- usage patterns

Do not drift into personal life review unless the user explicitly asks.

Do not write to Obsidian, `goal-journal`, or reminders unless the user separately asks.

## Source Priority

Use context in this order:

1. Current conversation and visible tool results
2. Codex thread tools
3. User-provided notes, file paths, or pasted summaries

If thread tools are available, inspect recent threads before judging.

If thread tools fail, fall back to local evidence such as:

- files created in the current workspace
- pasted thread summaries
- output artifacts already generated
- explicit user notes about shipped results

## Modes

Choose the lightest mode that satisfies the request.

- `chat review`
  - Use when the user only wants the retrospective in chat.
- `report review`
  - Use when the user wants a report, page, deck draft, or structured handoff.
- `visual packaging`
  - Use when the user wants long image, page structure, visual polish, or PPVI-style rework.

Default to `chat review` unless the user explicitly asks for report, page, long image, visual version, or design refinement.

## Supported Time Windows

- `daily`
- `weekly`
- `deep weekly`
- `monthly`

If the user says:

- `开始每日复盘` or `今日复盘` -> daily
- `开始周复盘` or `周复盘` -> weekly
- `深度复盘` or `深度周复盘` -> deep weekly
- `近一个月复盘` or `月度复盘` -> monthly

## Default Workflow

When the user asks for report-grade output, follow this order:

```text
1. chat review
2. report draft
3. PPVI-style visual review
4. long-image or page-ready draft
```

Do not jump directly from thread summaries to visual artifact.

Before moving from one stage to the next, ask one quiet question internally:

```text
Do I have enough evidence to justify the next layer,
or am I about to decorate weak judgment?
```

## Stage 1: Chat Review

First produce the raw retrospective.

For `daily`, output:

```text
今日 Codex 复盘：
- 今天完成了什么：
- 产出了什么文件/方案/结论：
- 今天最有价值的一步：

未收尾事项：
- 还没完成：
- 卡住/出错：
- 需要用户补充或确认：

可复用沉淀：
- 可以复用的提示词/流程：
- 可以固化成 skill/自动化/模板的东西：

明日接续：
- 明天优先接的 1 条线：
- 最小下一步：
- 暂时不要继续消耗的事：
```

For `weekly`, output:

```text
本周 Codex 总结：
- 本周主要推进了哪些线：
- 本周真正落地的产出：
- 本周只是探索/规划、还没落地的部分：

项目/线程复盘：
- 线程或项目 1：
- 线程或项目 2：
- 线程或项目 3：

使用方式复盘：
- 这周你主要怎么用 Codex：
- 哪些用法效率高：
- 哪些用法在浪费上下文或来回返工：

问题模式：
- 反复卡住的地方：
- 信息不足或决策不清的地方：
- 工具/环境问题：

系统改进建议：
- 该补到 prompt / skill / AGENTS.md / 模板里的规则：
- 值得固化的流程或命令：
- 建议停止重复的低价值动作：

下周建议：
- 下周主线：
- 下周 3 个关键动作：
- 建议归档/暂停的线：
- 下周建议采用的 Codex 工作方式：
```

For `deep weekly` and `monthly`, prioritize:

- core output
- highest ROI lines
- low-ROI but high-consumption lines
- project closure vs expansion
- usage pattern diagnosis
- context waste
- next operating changes

Minimum evidence rules:

- separate shipped work from planned work
- name at least one concrete file, artifact, or confirmed outcome when possible
- if a line is inference rather than confirmed evidence, phrase it as inference

## Stage 2: Report Draft

If the user wants a report, convert the retrospective into:

- title
- one-sentence judgment
- key findings
- evidence blocks
- operating recommendations

Prefer outcome grouping over chronology.

Name what truly shipped. Separate it from planning, research, and tool exploration.

Default report structure:

- title
- one-sentence judgment
- three key conclusions
- evidence blocks
- usage-pattern diagnosis
- next actions

## Stage 3: PPVI-Style Visual Review

Apply these five filters:

1. `克制优雅`
   - delete repeated explanation
   - keep only elements with a reason
2. `灰阶为基`
   - use color only as emphasis
   - do not build the page around loud color
3. `严格层级`
   - one dominant judgment per screen block
   - keep typography levels clear
4. `密度呼吸`
   - compress related items
   - do not over-card or over-paragraph
5. `图示穿插`
   - convert logic into cards, matrices, before/after, causal chains, and action grids

During this stage, explicitly answer:

- what hurts readability most
- what should be deleted
- what should be merged
- what should become a diagram
- what should become a card or matrix

Preferred conversions:

- repeated findings -> merged bullet group
- long explanation -> causal chain
- multiple status items -> status matrix
- contrast between good and bad usage -> split comparison block
- next steps -> 3-item action grid

## Stage 4: Long-Image or Page Draft

When the user asks for visual output, produce one of:

- long-image HTML draft
- web page structure draft
- report page / slide structure

Prefer:

- narrow reading width
- strong vertical pacing
- one judgment per section
- clear separation between `项目层` and `使用方式层`

Suitable blocks include:

- cover judgment
- three key conclusions
- evidence blocks
- project status matrix
- high/low efficiency comparison
- causal chain friction screen
- next-step action matrix

Default section order for `long-image`:

```text
1. cover judgment
2. three key conclusions
3. shipped vs explored matrix
4. project status block
5. usage-pattern diagnosis
6. friction causal chain
7. next-step action grid
```

Default section order for `page draft`:

```text
1. page title + one-sentence judgment
2. key conclusions band
3. evidence section
4. project layer section
5. workflow / usage layer section
6. next actions section
```

For each section, include only:

- `section goal`
- `core message`
- `recommended visual form`
- `content bullets`

If the user asks for HTML or page-ready output, structure each section using this mini-template:

```text
Section:
- goal:
- message:
- visual:
- content:
```

Visual form chooser:

- one strong judgment -> headline block
- multiple project statuses -> matrix
- contrast between shipped and drift -> comparison table
- repeated causes -> causal chain
- next actions -> 3-column action grid

Monthly output should add one more screen:

- `trend summary`
  - compare what actually closed, what kept expanding, and what kept consuming context

Do not make more than 7 sections unless the user explicitly asks for a deck or full report page set.

Avoid:

- screenshot-of-chat style output
- giant paragraphs pasted into cards
- chronology-first layouts
- loud decorative color
- mixing project status and behavior diagnosis in one block

## Delivery Rules

If the user says `输出报告`, include:

1. chat review
2. report draft

If the user says `输出报告和长图版`, include:

1. chat review
2. report draft
3. visual review
4. long-image draft

If the user only wants a quick review, stop after chat review.

If the user asks for a page or long image but the review itself is still weak, say so directly and produce a lighter structure draft rather than overclaiming polish.

## Tone

- Start with real progress, then point out drift or waste.
- Be warm but direct.
- Do not use generic productivity encouragement.
- End with one concrete next action inside Codex.

## Trigger Examples

```text
开始每日复盘
开始周复盘
开始周复盘，并输出报告和长图版
开始深度复盘
近一个月复盘，并做成长图
复盘这周 Codex 做了什么，再包装成页面稿
```

## Failure Modes

Watch for these common mistakes:

- calling busy exploration "real output"
- turning weak evidence into strong judgment
- skipping the report stage and jumping straight to visuals
- overusing PPVI language without actually restructuring information
- producing too many next actions instead of forcing prioritization
