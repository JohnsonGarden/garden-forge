---
name: novel-harness-initializer
description: Use when initializing, scaffolding, or upgrading a fiction/novel writing project with a reusable AI writing harness, dual-layer SPEC system, multi-agent editorial workflow, chapter gates, scene cards, review templates, risk controls, style checks, or publishing feedback loops.
---

# Novel Harness Initializer

## Purpose

Initialize a complete AI-assisted novel-writing project harness from an initial fiction idea: dual-layer SPEC, multi-agent editorial team, chapter workflow gates, scene cards, scoring, risk controls, style checks, feedback loops, and reusable project memory.

Use this for new fiction projects, rewrites, short-novel conversions, serialized web novels, or any request like "给这个小说项目搭一套 harness / SPEC / 多智能体创作工程".

## Fast Path

1. Gather or infer the minimum project brief and convert it into project-specific seed material, not generic placeholders:
   - project title
   - initial idea seed
   - target form: short novel / long novel / series
   - target length and hard cap
   - core intent/theme
   - primary reader promise
   - core cast or "to be decided"
   - platform or publication context
2. Run the bundled initializer when filesystem access is available:

```bash
python3 "$SKILL_DIR/scripts/init_novel_harness.py" \
  --root /path/to/workspace \
  --name "新版小说工程" \
  --title "小说标题" \
  --form "短篇/长篇/系列" \
  --target-length "45万-55万字" \
  --hard-cap "60万字" \
  --initial-idea "小说初始创意、人物、世界、冲突或改写目标" \
  --core-intent "一句话立意" \
  --reader-promise "读者为什么追下去" \
  --platform "发布平台或阅读场景" \
  --taboo-changes "不能改的设定、关系、立意或结局方向"
```

If `SKILL_DIR` is unavailable, locate this skill folder and call `scripts/init_novel_harness.py` directly.

3. After generation, open the new project’s root `docguide.md` for the directory map, then `AGENTS.md` for operating rules, then fill `SPEC/Me2AI/*.md` with author-specific material before drafting chapters.

## Required Harness Shape

Create these top-level directories:

- `SPEC/Me2AI/`: stable author intent and macro requirements.
- `SPEC/AI2AI/`: AI-maintained workflow, state, reviews, logs, and templates.
- `SPEC/AI2AI/创作工具/`: reusable quality tools.
- `SPEC/AI2AI/会议纪要/`: per-chapter kickoff and retrospective meeting minutes.
- `agents/`: role cards for the virtual writing team.
- `novel/`: chapter manuscripts.
- `briefs/`: per-chapter RunBriefs.
- `scene_cards/`: scene-level plans.
- `reviews/`: chapter reviews and scores.
- `handoffs/`: agent-to-agent handoffs.
- `publish_feedback/`: platform data and reader feedback intake.
- `style_examples/`: positive/negative style examples.

Create root `docguide.md` as the model-facing project directory guide. Keep operating rules in root `AGENTS.md` and compatibility notes in `CLAUDE.md`.

Create `SPEC/AI2AI/会议纪要与任务看板.md` as the slim chapter gate, task, and meeting-index board. Full kickoff and retrospective minutes must live under `SPEC/AI2AI/会议纪要/`, one file per meeting. Never append full meeting transcripts or long retrospectives to the board.

For the full file inventory and each file’s purpose, read `references/file-map.md`.

## Workflow Gates

Every formal chapter must pass:

```text
context loading
  -> chapter kickoff meeting
  -> RunBrief
  -> scene cards
  -> draft
  -> creation-tool checks
  -> multi-agent review
  -> chapter scorecard
  -> editor decision
  -> revision
  -> final review
  -> chapter retrospective
  -> task closure
  -> AI2AI state updates
```

Do not let a generated harness skip chapter kickoff, RunBrief, scene cards, review, retrospective, or task closure.

## Agent Team

Default permanent agents:

- 主编: direction, arbitration, final approval.
- 架构师: structure, pacing, plot economy, foreshadowing.
- 执行主笔作家: chapter drafting and revision.
- 人设与对白专员: character consistency and voice.
- 去AI写作风格审查专员: AI-ish prose, clichés, over-explanation.
- 模拟读者: retention, boredom, emotional pull.
- 平台留存与数据分析师: titles, opening, ending hooks, feedback.
- 连续性与档案官: state files, continuity, tasks, decision memory.

Optional temporary experts are defined in the generated `临时专家智能体机制.md` and should be called only for specific risks.

## Customization Rules

- Keep author intent and the initial idea seed stable in `Me2AI`; keep evolving project memory in `AI2AI`.
- Replace all placeholder text before first serious chapter writing.
- Seed the harness from the initial idea: form, length cap, intent, reader promise, likely risks, and first-chapter readiness should already reflect the project.
- Preserve project-specific stylistic rules in root `AGENTS.md`.
- Add genre-specific agents only when the genre truly needs them.
- Do not copy another novel’s plot, names, or world details into the new harness.

Use `references/customization-guide.md` when adapting for genre, length, or platform.

## Verification

After initialization:

```bash
find "$PROJECT_DIR" -type f | sort
git diff --check -- "$PROJECT_DIR"
```

Then verify:

- `AGENTS.md` points to all required SPEC, tools, and agent files.
- root `docguide.md` exists and describes the generated directory map.
- all directories contain at least one file.
- `SPEC/AI2AI/会议纪要与任务看板.md` exists and contains only chapter gates, task status, and meeting indexes.
- meeting minutes are stored under `SPEC/AI2AI/会议纪要/`, not appended indefinitely to one large AI2AI file.
- no unresolved `{{PLACEHOLDER}}` remains except in templates intended for future chapters.
- chapter workflow mentions creation tools, scorecard, kickoff meeting, retrospective, and task closure.
