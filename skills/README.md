# Skills

Each subfolder is one Claude Code skill. The folder name must match the `name` in that
skill's `SKILL.md` frontmatter, or CI will fail.

## Index

| Skill | What it does |
| --- | --- |
| _nothing published yet_ | |

## Adding one

```bash
cp -R skills/_template skills/my-new-skill
```

Then edit `skills/my-new-skill/SKILL.md`, set `name: my-new-skill`, write a description
that names the situations that should trigger it, and add a row to the table above.

Check it before committing:

```bash
python3 scripts/validate-frontmatter.py
```

## Layout

```
skills/my-skill/
├── SKILL.md       # required
├── references/    # optional, loaded on demand
└── scripts/       # optional
```

Keep `SKILL.md` short. Anything long or rarely needed belongs in `references/` so it stays
out of context until the skill actually reaches for it.
