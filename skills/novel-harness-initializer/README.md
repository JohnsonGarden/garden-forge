# Novel Harness Initializer

Novel Harness Initializer is a reusable skill for turning a fiction idea or finished outline into a structured novel-writing workspace.

Before asking AI to help write the novel, this skill helps set up the outline, memory, roles, and review process.

I built this skill from my own practical writing experience and refined it through repeated use. It is designed for the point where a writer already has a promising premise or outline, but needs a working production system: project memory, SPEC files, editorial roles, chapter gates, scene cards, reviews, risk controls, style checks, and feedback loops.

In its current form, this harness can help Claude, Codex, and other assistant platforms move novel projects forward with more stability than open-ended prompting.

## Who This Is For

This skill is for fiction writers who already have a premise, outline, rewrite plan, or serialized story idea, and want AI assistance without letting the model take over the work.

## Why This Exists

Short-form fiction, especially serialized web fiction, needs more than a good outline. The outline answers what to write; the harness answers how to keep writing, how to prevent drift, how to review the work, and how to revise without losing the original intent.

Current large language models are powerful, but unconstrained creative writing is still unstable. If you ask GPT, Claude, or another model to "just write the novel," the result often becomes generic, over-explained, emotionally flat, or visibly AI-flavored. A good idea can be flattened into prose that makes you want to close the tab.

This skill exists to reduce that risk.

In my experience, a strong outline plus a serious harness can let AI handle roughly 70% of the repeatable production work: scaffolding, memory, chapter planning, scene cards, review workflows, consistency checks, risk tracking, and revision loops. The remaining 30% still depends on the author's taste: what to keep, what to cut, what feels alive, and what makes the story different from AI slop.

## Why It Works

This harness works because it changes the model's job.

Instead of asking an AI assistant to invent, remember, write, edit, and self-correct all at once, the harness separates the work into stable layers and repeatable steps. Author intent is stored in `SPEC/Me2AI/`. Project state and workflow memory live in `SPEC/AI2AI/`. Chapter work moves through explicit gates: kickoff, RunBrief, scene cards, draft, review, revision, retrospective, and task closure.

That structure gives the model less room to drift. It also gives the author more places to intervene with judgment before the text becomes expensive to repair.

The multi-role review system is equally important. A single AI pass often smooths over problems. Separate editorial roles force the draft to be checked from different angles: structure, character voice, reader retention, continuity, style, and AI-flavor risk. This creates a more reliable production loop, while the actual literary quality still depends on the author.

In practice, the harness turns AI from an uncontrolled ghostwriter into a constrained editorial and drafting system. The author's taste remains necessary, and the workflow makes it easier to apply that taste at the right moments.

## Agent Team Workflow

Agent-team collaboration is one of the better ways to handle complex long-form or serialized creative work. Different stages of fiction production need different kinds of attention: structure, character voice, scene execution, retention risk, continuity, style, and revision discipline.

A fixed `agent.md` file quickly becomes too broad if it tries to handle everything. A useful agent role needs a limited scope and a clear kind of expertise. Small fixes can stay with the main agent. New chapter work, major rewrites, final reviews, and structural decisions should involve a team of specialized roles at the right moment.

This costs more tokens upfront, but it usually saves tokens later. Without role separation, a model can drift in the wrong direction, invent too freely, miss continuity problems, or produce prose that needs repeated human review and repair. A focused agent team creates friction before the expensive mistakes happen.

The point of "multi-agent" work is practical review pressure: every important creative decision should be checked by the right kind of reader before it hardens into draft material.

## Session Discipline

Even with an engineering-style harness, I would avoid giving Claude, Codex, or another assistant a long-running goal that automatically pushes the novel forward for many chapters.

In my practical experience, the harness works best when each fresh session advances one chapter. One chapter per session gives the model a bounded task, keeps the context easier to inspect, and improves compliance with the project rules. It also gives the author enough breathing room to review the result before the next chapter begins.

This rhythm is slower than full automation, but more reliable. For creative writing, reliability matters more than raw throughput. A novel can survive a deliberate workflow; it usually cannot survive several chapters of confident drift.

## What It Creates

- Dual-layer SPEC system:
  - `SPEC/Me2AI/` for stable author intent.
  - `SPEC/AI2AI/` for evolving project state and workflow memory.
- Multi-role editorial workflow.
- Chapter gates: kickoff meeting, RunBrief, scene cards, draft, review, revision, final review, retrospective, and task closure.
- Scene card and review templates.
- Risk controls, AI-flavor checks, style checks, and publishing feedback intake.
- Root project guides such as `AGENTS.md`, `CLAUDE.md`, and `docguide.md`.

## When To Use It

Use this skill when you have:

- a novel premise,
- a short-novel or web-novel outline,
- a rewrite plan,
- a serialized-fiction project,
- or a creative idea that needs production discipline before drafting.

It is especially useful when the outline is strong enough to protect, but the project needs structure before AI assistance becomes reliable.

## Where The Author Still Matters

This harness still leaves the author in charge.

It can organize the project, make AI collaboration more stable, reduce drift, and make repeatable editorial work more controllable. The author's taste, lived judgment, sense of rhythm, and final creative responsibility still have to come from the author.

That part stays with you.

## Usage

See [`SKILL.md`](./SKILL.md) for the callable skill instructions and [`references/`](./references/) for customization and file-map details.
