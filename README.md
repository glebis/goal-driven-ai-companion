# Goal-Driven AI companion

A dialogue-first companion that helps you explore what matters across life, choose a focus, and find a useful next step. Russian by default; English on request.

It starts by explaining that it collects your chosen personal context and where the host processes it. In cloud Cowork, conversations and session files are processed and stored in Anthropic's cloud. Saving a separate profile is optional; declining a save does not stop the host retaining the conversation. Share only what you are comfortable disclosing. Review the [cloud-service risks and benefits guide](https://agency-lab.glebkalinin.com/library/ru/cloud-services-risks) before sharing sensitive information.

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

**Cloud Cowork: run from the public repository**

Paste this into a Cowork task:

```text
Склонируй публичный репозиторий https://github.com/glebis/goal-driven-ai-companion
(git clone --depth 1), прочитай skills/companion/SKILL.md целиком и дальше веди
диалог строго по нему, как будто вызван /goal-driven-ai:companion. Остальные файлы
(references/, templates/, skills/lab-*) читай только тогда, когда SKILL.md на них ссылается.
Ничего не рассказывай про установку, сразу начни разговор.
```

This loads instructions for this task; it is not a persistent plugin installation. It requires Git and access to GitHub in the session. The clone contains public code, not your private profile. If the clone is blocked, report that limitation rather than claiming to have loaded the skill.

Cowork supports skills and plugins, but not every dependency works in the cloud sandbox. Local MCP servers run through desktop capabilities, not inside the cloud sandbox; they need the desktop app and may be restricted by your organization. Follow [Claude's plugin instructions](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) for a persistent installation. Compatibility of every bundled course route in cloud Cowork has not been verified; the dialogue route does not imply local tool installation or local-only storage.

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

Talk in text or use your agent’s existing voice mode. Save a profile and weekly goals as Markdown in a destination you choose when useful, with an optional goal brief in your project’s `AGENTS.md`. Saving is optional; the companion asks before writing. A cloud session file is not a device-local file; if only cloud storage is available, request a download and keep your own copy.

This package provides coaching instructions, references, and templates. Voice availability depends on your agent. It does not include a web chat service or automatically schedule work.

## License

[MIT](LICENSE).
