# Guide for contributors

Naturawrite is an agent skill written in Markdown. The repository has no build step; its package checks validate the prompt and manifests.

## Source files

- `SKILL.md` is the prompt loaded by agents.
- `README.md` documents installation, use, scope, patterns, and attribution.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` expose the package to Claude Code.
- `agents/openai.yaml` provides Codex-compatible display metadata.
- `scripts/validate-package.py` checks shared version and pattern data.
- `examples.md` contains generic examples only; do not place personal documents there.

## Rules for changes

Keep `SKILL.md` and the README pattern table in sync. Number checks from 1 without gaps. Add a new check only when an existing check cannot express the decision; prefer folding related guidance into an existing check.

Keep the same version in `SKILL.md` under `metadata.version`, the latest `CHANGELOG.md` entry, and `.claude-plugin/plugin.json`. Do not add a top-level `version` field to `SKILL.md`.

Keep the skill portable across agents. Do not make the prompt depend on a specific tool, operating system, repository layout, personal project, or user's biography.

Before release, run the package validator, the skill-discovery check, and Claude Code plugin validation. The validation commands are listed in `CONTRIBUTING.md`.

## Writing standards

Use plain language in prompts and documentation. Keep technical terms where they carry necessary precision. Do not add a rule merely because one phrase appeared in one bad draft. A change should improve a repeatable editing decision and preserve the writer's facts, purpose, and deliberate style.
