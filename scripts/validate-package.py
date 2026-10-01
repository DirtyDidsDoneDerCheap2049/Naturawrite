#!/usr/bin/env python3
"""Validate package identity, versions, local links, and public-file scope."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    required = (
        "SKILL.md", "README.md", "README.en.md", "LICENSE", "CHANGELOG.md",
        "CONTRIBUTING.md", "examples.md", "AGENTS.md", "agents/openai.yaml",
        ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
        ".github/workflows/validate.yml",
    )
    for relative in required:
        require((ROOT / relative).is_file(), f"Missing package file: {relative}")

    skill = read("SKILL.md")
    metadata = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    require(metadata is not None, "SKILL.md must start with YAML frontmatter")
    header = metadata.group(1)
    require(re.search(r"(?m)^name: naturawrite$", header) is not None,
            "Set the skill name to naturawrite")
    require(re.search(r"(?m)^description:\s*\S", header) is not None,
            "Add a skill description")
    version_match = re.search(r'(?m)^  version: "(\d+\.\d+\.\d+)"$', header)
    require(version_match is not None, "Add metadata.version in SKILL.md")
    version = version_match.group(1)

    plugin = json.loads(read(".claude-plugin/plugin.json"))
    marketplace = json.loads(read(".claude-plugin/marketplace.json"))
    require(plugin.get("name") == "naturawrite" and plugin.get("skills") == ["./"],
            "Use one root skill in the Naturawrite plugin")
    require(plugin.get("version") == version, "Plugin and skill versions differ")
    require(marketplace.get("name") == "naturawrite", "Marketplace name differs")
    entries = marketplace.get("plugins", [])
    require(len(entries) == 1 and entries[0].get("name") == "naturawrite"
            and entries[0].get("source") == "./", "Fix the marketplace plugin entry")

    readme = read("README.md")
    require(read("CHANGELOG.md").split("## ", 1)[1].startswith(version + " "),
            "Changelog latest version differs")
    ui = read("agents/openai.yaml")
    require("$naturawrite" in ui, "UI default_prompt must invoke $naturawrite")
    require("Naturawrite" in ui, "UI display name differs")

    numbers = [int(n) for n in re.findall(r"(?m)^### (\d+)\. ", skill)]
    require(numbers and numbers == list(range(1, len(numbers) + 1)),
            "Number skill checks consecutively from 1")
    table = [int(n) for n in re.findall(r"(?m)^\| (\d+) \|", readme)]
    require(numbers == table, "README check table differs from SKILL.md")
    require(len(numbers) == 26, "Review the check count before changing the package")

    files = [p for p in ROOT.rglob("*") if p.is_file()
             and not any(part in {".git", "__pycache__"} for part in p.relative_to(ROOT).parts)]
    require([p.relative_to(ROOT).as_posix() for p in files if p.name == "SKILL.md"]
            == ["SKILL.md"], "Keep one SKILL.md at the package root")
    for path in files:
        require(not path.is_symlink(), f"Package contains a symlink: {path.name}")
        require(path.suffix.lower() not in {".pdf", ".xlsx", ".zip", ".jsonl"},
                f"Unexpected personal or release artifact in package: {path.name}")
        if path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py"}:
            content = path.read_text(encoding="utf-8")
            windows_path = r"(?<![A-Za-z])(?:[A-Z]:\\|[A-Z]:/(?!/))"
            require(re.search(windows_path, content) is None,
                    f"Absolute Windows path found: {path.relative_to(ROOT)}")
            require(re.search(r"(?i)BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY", content) is None,
                    f"Private key found: {path.relative_to(ROOT)}")
        if path.suffix.lower() == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", content):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                local_target = target.split("#", 1)[0]
                require((path.parent / local_target).exists(),
                        f"Broken local link in {path.relative_to(ROOT)}: {target}")

    require("Copyright (c) 2025 Siqi Chen" in read("LICENSE"),
            "Preserve the upstream MIT copyright notice")
    print(f"Naturawrite {version}: {len(numbers)} checks; package validation passed")


if __name__ == "__main__":
    main()
