# Agents

One markdown file per subagent. The filename (minus `.md`) must match the `name` in its
frontmatter, or CI will fail.

## Index

| Agent | What it does |
| --- | --- |
| _nothing published yet_ | |

## Adding one

```bash
cp agents/_template.md agents/my-new-agent.md
```

Set `name: my-new-agent`, list the tools it needs in `tools:`, write the system prompt,
and add a row to the table above.

## Frontmatter

| Field | Required | Notes |
| --- | --- | --- |
| `name` | Yes | Must match the filename. |
| `description` | Yes | What the main loop reads when deciding to delegate. Be specific. |
| `tools` | No | Comma-separated. Omit to inherit everything; narrow it for read-only agents. |
| `model` | No | `haiku`, `sonnet`, or `opus`. Omit to inherit the session model. |

Grant the narrowest tool set that still does the job. A research agent that only needs
`Read, Grep, Glob` should not be able to write files.
