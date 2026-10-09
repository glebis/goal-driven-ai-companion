# Goal-Driven AI companion

A dialogue-first companion that helps you build a working profile, choose a weekly goal, and start a useful task with an agent. Russian by default; English on request.

## Install

**Claude Code**

```text
/plugin marketplace add glebis/agency-plugins
/plugin install goal-driven-ai@agency-plugins
/goal-driven-ai:companion
```

**Codex** (requires Node.js)

```sh
npx skills add glebis/goal-driven-ai-companion --agent codex -g -y
```

Then open a new chat and invoke `$companion`. This installs all five skills so course coaching is available too.

## Included skills

- `companion`: dialogue, profile, weekly goal, and first agent task.
- `lab-context`: updates to the same profile and learning context.
- `lab-homework`: practice grounded in the course curriculum and your goal.
- `lab-review`: evidence-based feedback on a conversation or selected transcript.
- `lab-setup`: selected lesson tools, with installation review and verification.

In Claude Code, use `/goal-driven-ai:companion` or a direct command such as `/goal-driven-ai:lab-homework`. Enter slash commands inside Claude Code. In Codex, use `$companion` or `$lab-homework`. Russian is the default; English is available on request. Existing Lab Coach users can keep using their selected context folder; there is no automatic migration or deletion. No separate Lab Coach install is required. Design skills remain optional external tools.

## How it works

Talk in text or use your agent’s existing voice mode. Save a profile and weekly goals as local Markdown when useful, with an optional goal brief in your project’s `AGENTS.md`. Saving is optional; the companion asks before writing.

This package provides coaching instructions, references, and templates. Voice availability depends on your agent. It does not include a web chat service or automatically schedule work.

## License

[MIT](LICENSE).
