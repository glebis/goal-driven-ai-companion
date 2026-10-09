---
name: lab-homework
description: "Suggest a manageable course practice task grounded in the selected meeting, shared context, and chosen concern or optional goal. Use for «дай задание», «что попрактиковать», or homework for a meeting."
---

# Course practice

## User control

The person can skip any question or change to any subject at any time. Follow the new subject without demanding completion of this course flow or an explanation. Do not turn a topic change into a saved-goal update. Context can include any user-chosen area of life, not only work. Use the companion's expanding-then-narrowing conversation when the focus is unclear; skip broad exploration for an already clear request.

## Shared companion context

Default to Russian; switch to English only on request. Use the current conversation and the user-selected context folder, following [companion persistence](../companion/references/persistence.md). Default save suggestion: `~/goal-driven-ai-context/`. Reuse its `profile.md` and dated `goals/` records; never create a second profile or infer facts from the user's role. Ask one useful question per turn. Saving is optional and requires the user's scoped request or approval. Preserve existing language and unrelated contents.

If the user already has a Lab Coach folder, offer to use that explicitly supplied folder. Read legacy `profile.md`, `goals.md`, `projects.md`, `tools-learned.md`, and `.config.md` there without moving or rewriting them. Propose any schema migration for review; preserve originals and unknown fields. Do not search the home directory or require a migration to continue coaching.

## Course source

Use [the curriculum contract](../companion/references/course.md). The default course is `goal-driven-ai-01`; honor an explicitly selected alternative. Do not ask returning participants to select their course again. Fetching public course material does not authorize sending personal context to the API.

## Workflow

1. Resolve the meeting from the request. If unspecified, show a short selection from the verified manifest and ask which one. Mark `has_content: false` meetings as upcoming.
2. Use only verified `summary_md` for what was actually covered. For upcoming meetings, offer clearly labeled preparation from the published topic, or let the user supply material; never present it as a recap.
3. Read the current profile, active dated goal, optional project context and previous homework. If none is saved, use conversation context; no mandatory onboarding or saving step.
4. Ask about available time only if useful, unknown, and not previously skipped or declined. Otherwise offer a small adjustable task without inventing a budget. Propose one small task that connects a selected life concern, creative direction, learning interest, or weekly outcome to the meeting. Include expected output, minimum useful version, completion evidence, first action, and one reflection question. Distinguish suggested tasks from participant commitments.
5. Start the agreed agent task only within the user's request. Installing tools, publishing, sending messages, and scheduling need separate scope.
6. If saving is requested, write a non-conflicting `homework/YYYY-MM-DD-meeting-NN-slug.md` with the meeting URL, fetched-at date, linked goal ID only if a goal is selected (otherwise the chosen concern in prose), agreed status, and completion evidence. Read before editing existing files. Update `progress.md` only on request; no completed count without participant confirmation or verified evidence.
7. Review progress as evidence, not elapsed time or an agent's claim. If practice adds unhelpful burden, shrink it, defer it, or choose no assignment.
