---
name: lab-context
description: "Create, view, or update the shared Goal-Driven AI working profile and course learning context. Use for «обнови профиль», «что я освоил», or existing Lab Coach profile requests."
---

# Course profile

Profile creation and goal planning use `companion` as the single onboarding flow. When invoked directly, follow that skill's dialogue and persistence instructions; do not restart a fixed interview.

## User control

The person can skip any question or change to any subject at any time. Follow the new subject without demanding completion of this course flow or an explanation. Do not turn a topic change into a saved-goal update. Context can include any user-chosen area of life, not only work. Use the companion's expanding-then-narrowing conversation when the focus is unclear; skip broad exploration for an already clear request.

## Shared companion context

Default to Russian; switch to English only on request. Use the current conversation and the user-selected context folder, following [companion persistence](../companion/references/persistence.md). Default save suggestion: `~/goal-driven-ai-context/`. Reuse its `profile.md` and dated `goals/` records; never create a second profile or infer facts from the user's role. Ask one useful question per turn. Saving is optional and requires the user's scoped request or approval. Preserve existing language and unrelated contents.

If the user already has a Lab Coach folder, offer to use that explicitly supplied folder. Read legacy `profile.md`, `goals.md`, `projects.md`, `tools-learned.md`, and `.config.md` there without moving or rewriting them. Propose any schema migration for review; preserve originals and unknown fields. Do not search the home directory or require a migration to continue coaching.

## Learning context

Read only the configured folder. Ask what changed and update only confirmed details. Track tool familiarity in optional `tools-learned.md` (tried/comfortable/confident are user-reported estimates), active projects in `projects.md`, and the selected cohort in the profile's course section. Do not assign experience ratings automatically. Existing `.config.md` cohort values can be used without conversion.

Weekly outcomes remain in dated `goals/` files, not a competing `goals.md` checklist. Legacy goals remain readable; explicitly confirm which one is current before acting. Summarize a proposed update in dialogue; write only when requested. A declined save must still allow course practice and review.
