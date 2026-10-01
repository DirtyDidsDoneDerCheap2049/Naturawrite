# Naturawrite

[简体中文](README.md)

Naturawrite is a writing and editing skill for reducing AI phrasing in Chinese and English. It fixes awkward sentences, removes padding and unsupported claims, and makes the flow of an argument easier to follow.

The name combines **natural** and **write**.

## Scope

Use it to edit articles, reports, emails, product descriptions, and technical documentation, or to draft new text for a specified audience and purpose. Editing preserves the original genre, tone, facts, and necessary technical terms. Writing samples can guide vocabulary, syntax, and rhythm.

Formal text can remain formal, without invented experiences, forced casual language, or deliberate mistakes. AI authorship detection is outside the skill’s scope, and passing AI detectors is not guaranteed.

## Installation

Run this command from the repository directory:

```sh
npx skills add . --global --agent codex --skill naturawrite
```

To install from GitHub, run:

```sh
npx skills add DirtyDidsDoneDerCheap2049/naturawrite --global --agent codex --skill naturawrite
```

To install for another tool, replace `codex` with its Skills CLI agent name, such as `claude-code` or `opencode`. Omit `--global` to install for the current project. You can also download the repository and copy its directory to `~/.codex/skills/naturawrite/` for Codex, or to the corresponding skills directory for another tool. Other options are described in the [Skills CLI documentation](https://github.com/vercel-labs/skills). The repository also includes Claude Code plugin manifests.

## Usage

```text
Use $naturawrite to edit this passage. Preserve technical terms and supported facts, and return only the revised text.
```

For file edits, specify the path and the sections to edit. The skill edits prose while preserving code blocks, commands, metadata, paths, structured data, and link targets. It returns the revised text by default; ask for a comparison or editing notes if needed.

When drafting new text, provide the audience, purpose, and known facts. You can also include writing samples to guide the style. Personal experiences in a sample are included in a new draft only when explicitly requested.

The full rules are in [SKILL.md](SKILL.md), with an overview in the [Chinese README](README.md#26-项编辑检查) and examples in [examples.md](examples.md).

## Acknowledgements

Some rules in this skill come from [Humanizer](https://github.com/blader/humanizer), including checks 2–10, 13–17, and 19–20 in the overview. They were selected, adapted, and rewritten; the skill also grew in part from problems and shortcomings noticed while using Humanizer.

The selection process was inspired by [AI Manuscript Repair](https://github.com/eglantine-shell/ai-repair): fix ordinary language problems through editing, rather than deliberately imitating human habits to reduce AI phrasing. This avoids turning AI into a cosplay of humans that makes people uncomfortable. The project supplied an editorial approach; no code, prompt, or rule text was copied from it.

The remaining principles are original rules developed through the author’s discussions with GPT 5.6. They address reader-appropriate vocabulary, structural correspondence in analogies, matching expression precision to evidence, separating facts from mechanism hypotheses, matching lexical and syntactic complexity in Chinese, defensive explanations, thought-driven structure, continuity of omitted subjects, informative headings, and removing unnecessary reasoning traces. These principles also extend and reshape some of the retained Humanizer rules.

This project uses the [MIT License](LICENSE), which preserves Humanizer’s original copyright notice.
