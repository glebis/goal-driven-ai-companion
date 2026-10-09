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

Then invoke `$companion`.

## How it works

Talk in text or use your agent’s existing voice mode. Save a profile and weekly goals as local Markdown when useful, with an optional goal brief in your project’s `AGENTS.md`. Saving is optional; the companion asks before writing.

This package provides coaching instructions, references, and templates. Voice availability depends on your agent. It does not include a web chat service or automatically schedule work.

## License

[MIT](LICENSE).
