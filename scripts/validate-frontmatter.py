#!/usr/bin/env python3
"""Validate frontmatter across skills/ and agents/.

Checks that every skill and agent declares a name and description, that declared
names match their file or folder name, and that no obvious secret has been
committed. Exits non-zero on any error so CI fails loudly.

Run from the repo root:  python3 scripts/validate-frontmatter.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
AGENTS = ROOT / "agents"
TASKS = ROOT / "scheduled-tasks"

# Minimum description length. Short descriptions cause skills to never trigger.
MIN_DESCRIPTION = 40

# Frontmatter keys that name an env var rather than holding a value.
KEY_NAME_FIELDS = {"requires-keys"}

# Patterns that look like a real credential rather than a placeholder.
SECRET_PATTERNS = [
    (re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}"), "Anthropic API key"),
    (re.compile(r"sk-[A-Za-z0-9]{32,}"), "OpenAI-style API key"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}"), "Slack token"),
    (re.compile(r"ghp_[A-Za-z0-9]{30,}"), "GitHub personal access token"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key ID"),
    (re.compile(r"pat-(?:na|eu)\d?-[A-Za-z0-9\-]{20,}"), "HubSpot private app token"),
]

errors = []
warnings = []
found_by_kind = {}


def split_frontmatter(text, path):
    """Return the raw frontmatter block, or None if absent/malformed."""
    if not text.startswith("---"):
        errors.append(f"{path}: missing YAML frontmatter (file must start with '---')")
        return None
    end = text.find("\n---", 3)
    if end == -1:
        errors.append(f"{path}: frontmatter opened but never closed with '---'")
        return None
    return text[3:end]


def parse_frontmatter(block):
    """Minimal top-level key parser. Good enough for name/description/tools."""
    fields = {}
    current = None
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if match and not line.startswith((" ", "\t")):
            current = match.group(1)
            fields[current] = match.group(2).strip()
        elif current and line.startswith((" ", "\t")):
            fields[current] = (fields[current] + " " + line.strip()).strip()
    return fields


def check_secrets(text, path):
    for pattern, label in SECRET_PATTERNS:
        if pattern.search(text):
            errors.append(f"{path}: looks like a committed {label}. Remove it and rotate the key.")


def check(path, expected_name, kind):
    text = path.read_text(encoding="utf-8")
    check_secrets(text, path.relative_to(ROOT))

    block = split_frontmatter(text, path.relative_to(ROOT))
    if block is None:
        return
    fields = parse_frontmatter(block)
    rel = path.relative_to(ROOT)

    name = fields.get("name", "").strip()
    if not name:
        errors.append(f"{rel}: frontmatter is missing 'name'")
    elif name != expected_name:
        errors.append(f"{rel}: name '{name}' does not match {kind} name '{expected_name}'")

    description = fields.get("description", "").strip()
    if not description:
        errors.append(f"{rel}: frontmatter is missing 'description'")
    elif len(description) < MIN_DESCRIPTION:
        warnings.append(
            f"{rel}: description is only {len(description)} chars. "
            "Short descriptions mean the skill rarely triggers; name the situations that should invoke it."
        )

    for field in KEY_NAME_FIELDS:
        value = fields.get(field, "")
        if "=" in value:
            errors.append(f"{rel}: '{field}' should list key names only, never values")

    if name and name != "_template":
        found_by_kind.setdefault(kind, []).append((name, description))


for root, kind in ((SKILLS, "skill"), (TASKS, "scheduled task")):
    if not root.is_dir():
        continue
    for folder in sorted(p for p in root.iterdir() if p.is_dir()):
        skill_file = folder / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{root.name}/{folder.name}/: no SKILL.md found")
            continue
        check(skill_file, folder.name, kind)

if AGENTS.is_dir():
    for agent_file in sorted(AGENTS.glob("*.md")):
        if agent_file.name == "README.md":
            continue
        check(agent_file, agent_file.stem, "agent")

for warning in warnings:
    print(f"warning: {warning}")
for error in errors:
    print(f"error: {error}")

tally = ", ".join(
    f"{len(found_by_kind.get(k, []))} {k}(s)" for k in ("skill", "agent", "scheduled task")
)
print(
    f"\nChecked {tally} (templates excluded): "
    f"{len(errors)} error(s), {len(warnings)} warning(s)."
)

sys.exit(1 if errors else 0)
