# elainezelby

A personal collection of [Claude Code](https://claude.com/claude-code) skills and agents that I've built and actually use.

Everything here is general purpose and portable. Company-specific work lives in a separate private repo.

## What's in here

| Directory | What it holds |
| --- | --- |
| [`skills/`](skills/) | Claude Code skills. Each is a folder containing a `SKILL.md` plus any supporting references or scripts. |
| [`agents/`](agents/) | Subagent definitions. A single markdown file per agent, with YAML frontmatter. |
| [`scheduled-tasks/`](scheduled-tasks/) | Jobs meant to run on a cron rather than be invoked by hand. Same folder-plus-`SKILL.md` shape as a skill, but installs to `~/.claude/scheduled-tasks/`. |
| [`scripts/`](scripts/) | Repo tooling (frontmatter validation, etc). |

## Skills

| Skill | What it does |
| --- | --- |
| [`linkedin-ads-campaigns`](skills/linkedin-ads-campaigns/) | Opinionated B2B LinkedIn Ads playbook: qualifying the offer, funnel design, Campaign Manager setup, creative rules, benchmarks, and the outreach layer that converts leads. Six reference docs loaded on demand. |
| [`marketing-psychology-analyzer`](skills/marketing-psychology-analyzer/) | Audits marketing copy, ads, landing pages, and positioning against persuasion frameworks from Cialdini, Carnegie, Gladwell, and Schwartz. Returns a scorecard, an emotion map, and ranked recommendations. |

## Agents

| Agent | What it does |
| --- | --- |
| _nothing published yet_ | |

## Scheduled tasks

| Task | What it does |
| --- | --- |
| [`ramp-receipt-submitter`](scheduled-tasks/ramp-receipt-submitter/) | Daily: finds open Ramp receipt requests in Gmail, pulls the matching vendor invoice, submits it as a hash-verified attachment, and archives only after Ramp confirms the match. |

## Installing

Claude Code loads skills and agents from two places:

- **User level** (`~/.claude/`) makes them available in every project.
- **Project level** (`.claude/` in a repo) scopes them to that project only.

Clone and install everything at the user level:

```bash
git clone https://github.com/ezelbytofu/elainezelby.git
```

```bash
mkdir -p ~/.claude/skills ~/.claude/agents && cp -R elainezelby/skills/* ~/.claude/skills/ && cp -R elainezelby/agents/* ~/.claude/agents/
```

Or install a single skill:

```bash
cp -R elainezelby/skills/SKILL-NAME ~/.claude/skills/
```

Start a new Claude Code session afterwards so the new files get picked up. The `_template` folder is scaffolding, not a real skill, so skip it when copying selectively.

## Writing a new skill

A skill is a folder whose name matches the `name` in its frontmatter:

```
skills/my-skill/
├── SKILL.md            # required: the instructions Claude reads
├── references/         # optional: detailed docs loaded on demand
└── scripts/            # optional: helper scripts the skill can run
```

`SKILL.md` starts with YAML frontmatter:

```markdown
---
name: my-skill
description: What it does, and the specific situations that should trigger it. This field is the only thing Claude sees when deciding whether to load the skill, so be concrete about trigger phrases.
---

# My Skill

Instructions go here.
```

The `description` does all the work of getting the skill invoked at the right moment. Write it as "does X. Use when the user says Y or Z" rather than a vague summary. Copy [`skills/_template/`](skills/_template/) as a starting point.

Keep `SKILL.md` itself reasonably short and push long detail into `references/`, so it only gets pulled into context when it's actually needed.

## Writing a new agent

An agent is a single markdown file in `agents/`, with frontmatter declaring its name, description, and the tools it can reach:

```markdown
---
name: my-agent
description: When to hand work to this agent.
tools: Read, Grep, Glob, Bash
---

System prompt for the agent goes here.
```

See [`agents/_template.md`](agents/_template.md).

## API keys

Nothing in this repo contains credentials, and nothing should. Skills that need an API key declare it in frontmatter under `requires-keys` and read it from the environment at runtime:

```yaml
requires-keys: [APIFY_TOKEN, EXA_API_KEY]
```

Actual values live in `~/.env` and stay out of git. The `.gitignore` blocks `.env` files, but that's a backstop, not a substitute for checking a diff before committing.

## Validation

A GitHub Action runs on every push and pull request to check that each skill and agent has valid frontmatter and that folder names match declared names. Run it locally before pushing:

```bash
python3 scripts/validate-frontmatter.py
```

## License

MIT. See [LICENSE](LICENSE).
