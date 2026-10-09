# Goal-Driven AI companion

A dialogue-first companion that helps you explore what matters across life, choose a focus, and find a useful next step. Russian by default; English on request.

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

- `companion`: user-led context, expanding-then-narrowing coaching, optional goals and agent tasks.
- `lab-context`: updates to the same profile and learning context.
- `lab-homework`: practice grounded in the course curriculum and your goal.
- `lab-review`: evidence-based feedback on a conversation or selected transcript.
- `lab-setup`: selected lesson tools, with installation review and verification.

In Claude Code, use `/goal-driven-ai:companion` or a direct command such as `/goal-driven-ai:lab-homework`. Enter slash commands inside Claude Code. In Codex, use `$companion` or `$lab-homework`. Russian is the default; English is available on request. Existing Lab Coach users can keep using their selected context folder; there is no automatic migration or deletion. No separate Lab Coach install is required. Design skills remain optional external tools.

## Your conversation

Choose any subject, skip any question, or change topics at any time. The companion explores broadly, then helps you choose a focus (the T-shaped coaching approach). Weekly goals and saving are optional. Ask for critical/Pareto mode to challenge scope and find a smaller useful approach; 80/20 is a heuristic, not a promise.

## How it works

Talk in text or use your agent’s existing voice mode. Save a profile and weekly goals as local Markdown when useful, with an optional goal brief in your project’s `AGENTS.md`. Saving is optional; the companion asks before writing.

This package provides coaching instructions, references, and templates. Voice availability depends on your agent. It does not include a web chat service or automatically schedule work.

## License

[MIT](LICENSE).
