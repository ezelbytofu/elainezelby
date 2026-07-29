---
name: _template
description: When work should be handed to this agent. Be specific, since this is what the main loop reads when picking an agent. e.g. "Use for broad read-only searches across many files when you only need the conclusion, not the file contents."
tools: Read, Grep, Glob, Bash
---

You are a [role] agent.

## Your job

One paragraph on what this agent is responsible for and what "done" looks like.

## How to work

- Concrete guidance on approach
- What to prioritize when there's a tradeoff
- What to do when blocked

## Constraints

- What this agent must not do (e.g. never write files, never push)
- Scope boundaries

## Output

Describe exactly what to return. Agent output is a return value consumed by the caller,
not a message to a human, so specify the shape: raw data, a structured list, a file path.
