# garden-forge

Practical AI workflows, assistant skills, and reusable project scaffolds.

`garden-forge` is my public workspace for building and sharing small, useful AI-native resources: assistant skills, project templates, workflow scaffolds, automation patterns, and documentation assets.

This repository is not a single application or product. It is a growing collection of reusable building blocks created from real AI-assisted work.

The name reflects the way I use this repo:

- **Garden**: ideas grow through iteration, pruning, and recombination.
- **Forge**: useful tools are shaped by repeated use, pressure, and refinement.

## What this repository is for

This repo is intended to collect resources that help turn vague ideas into structured, repeatable workflows.

Typical resources may include:

- **Assistant skills**  
  Portable instructions, scripts, and workflow packages for AI assistants.

- **Project scaffolds**  
  Reusable folder structures and initialization scripts for complex AI-assisted work.

- **Templates**  
  Product documents, design documents, review checklists, prompt frameworks, and operating guides.

- **Workflow experiments**  
  Practical experiments that may later become reusable tools or documented patterns.

- **Reference docs**  
  Notes, examples, and conventions that make the resources easier to understand and reuse.

## Current status

This repository is in an early stage.

Most top-level directories are intentionally reserved for future open-source resources. The first substantial published resource is currently under `skills/`.

## Featured resource

### Novel Harness Initializer

Path:

```text
skills/novel-harness-initializer/
````

`novel-harness-initializer` is an assistant skill for bootstrapping a structured AI-assisted novel-writing workspace.

It is designed for long-form fiction projects where a simple prompt is not enough. Instead of asking an AI assistant to “just write the novel,” the skill initializes a project harness with:

* stable author-facing specifications
* AI-facing project memory
* editorial roles
* chapter gates
* scene cards
* review templates
* continuity tracking
* handoff documents
* publishing feedback loops
* anti-drift and anti-“AI flavor” controls

The goal is to make long-form AI-assisted writing more structured, inspectable, and repeatable.

See:

```text
skills/novel-harness-initializer/README.md
skills/novel-harness-initializer/SKILL.md
```

## Repository structure

```text
garden-forge/
├── docs/
│   └── General documentation and notes
├── projects/
│   └── Larger standalone experiments or project workspaces
├── skills/
│   └── Reusable assistant skills and workflow packages
├── templates/
│   └── Reusable document, product, and workflow templates
├── LICENSE
└── README.md
```

## Design principles

Resources in this repository generally follow a few principles.

### 1. Practical before theoretical

The resources here are meant to be used in real workflows. They may contain scripts, templates, folder conventions, prompts, or operating rules, but the goal is always practical execution.

### 2. Structure over one-shot prompting

Many AI workflows fail because everything is compressed into a single prompt. This repo favors durable structures: project folders, state files, checklists, review gates, and reusable conventions.

### 3. Human intent remains primary

AI assistants are useful, but they should not silently rewrite the user’s goals. Resources here try to separate stable human intent from temporary AI execution state.

### 4. Iteration is expected

Most resources start as working drafts. They are refined through repeated use rather than designed perfectly upfront.

### 5. Small tools are valuable

Not every open-source contribution needs to be a full platform. A well-scoped skill, template, or workflow can still save meaningful time.

## How to use this repository

Browse the relevant directory based on what you need:

* Use `skills/` if you are looking for assistant-compatible workflows.
* Use `templates/` if you are looking for reusable document or process templates.
* Use `projects/` if you are looking for larger experiments.
* Use `docs/` for supporting documentation and notes.

Each mature resource should include its own local `README.md` with usage instructions.

## Roadmap

Planned future additions may include:

* more assistant skills
* product management templates
* AI workflow templates
* prompt engineering patterns
* design and documentation scaffolds
* examples generated from real use cases
* lightweight automation scripts

This roadmap is intentionally flexible. New resources will be added when they become useful enough to share.

## License

This repository is licensed under the MIT License.

See `LICENSE` for details.
