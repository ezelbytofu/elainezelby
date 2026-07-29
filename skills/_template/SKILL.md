---
name: _template
description: One or two sentences on what this skill does, followed by the concrete situations that should trigger it. Include the actual phrases a user would type, e.g. "Use when the user says 'audit my landing page', 'check page performance', or pastes a URL and asks how it converts." This description is the only thing Claude sees when deciding whether to load the skill, so vague summaries mean the skill never fires.
---

# Skill Name

One paragraph on what this does and the problem it solves. Assume the reader is Claude
mid-task, not a human browsing a repo.

## When to use this

- Concrete trigger situation
- Another concrete trigger situation

## When NOT to use this

- Adjacent case that should route elsewhere, and where it should go instead

## Inputs

What the skill needs before it can start. If something is missing, say whether to ask the
user or infer a default.

| Input | Required | Notes |
| --- | --- | --- |
| Example input | Yes | Where it comes from |

## Steps

1. First step. Be specific about tools and commands rather than describing intent.
2. Second step.
3. Third step.

## Output

What the skill produces, and in what format. If it writes files, say where.

## References

Long detail lives in `references/` so it only loads when needed:

- `references/example.md` - what's in it and when to read it

## Notes

Anything easy to get wrong: rate limits, gotchas, edge cases worth calling out.
