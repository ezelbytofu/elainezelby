# Scheduled tasks

Jobs designed to run on a cron rather than be invoked by hand. Same shape as a skill (a
folder containing `SKILL.md`), but they install to `~/.claude/scheduled-tasks/` instead of
`~/.claude/skills/`, and each one assumes a recurring schedule.

The folder name must match the `name` in frontmatter, or CI will fail.

## Index

| Task | Cadence | What it does |
| --- | --- | --- |
| [`ramp-receipt-submitter`](ramp-receipt-submitter/) | Daily | Finds open Ramp receipt requests in Gmail, pulls the matching vendor invoice, submits it as a hash-verified attachment, and archives only after Ramp confirms the match. |

## Installing

```bash
cp -R scheduled-tasks/TASK-NAME ~/.claude/scheduled-tasks/
```

Then schedule it. Most of these declare a suggested cron at the bottom of their `SKILL.md`.

## A note on placeholders

These tasks touch real accounts, so the published versions use `<PLACEHOLDER>` tokens for
anything account-specific: email addresses, ad account IDs, mailbox keys. Each task has a
Setup table listing what to fill in. Fill them in **after** copying to `~/.claude/`, so the
real values never end up back in this repo.
