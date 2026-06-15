# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

This is a **14-day learning challenge repo**, not a production codebase. Each day adds one capability toward an "AI TPM Copilot." Build state is intentionally incremental — early days use plain Python heuristics; AI/LLM/agent/RAG/MCP integrations are scheduled for later days per [`challenge/14_day_plan.md`](challenge/14_day_plan.md). When asked to add a feature, check the day plan first — the requested capability may be deliberately deferred to a specific day.

## Commands

```bash
# Activate the virtualenv (it's checked in at venv/, do not recreate)
source venv/bin/activate

# Run the app (only one app exists)
streamlit run projects/tpm_pm_toolkit/app.py
```

No test runner, linter, or formatter is configured. There is no `requirements.txt` — Streamlit is the only runtime dependency. DeepEval is scheduled for Day 11 (see `.deepeval/` placeholder).

## Architecture

### Single-file Streamlit app
`projects/tpm_pm_toolkit/app.py` is the entire application — one file, no modules, no routing. New "modules" advertised on the homepage cards (Bug Triage, PRD Builder, etc.) are **not yet implemented**; they're UI placeholders. Each completed day appends a new section to the bottom of `app.py` (e.g. Day 2 added the Launch Risk Analyzer section starting at line ~226). Follow this append-pattern rather than refactoring into separate files unless explicitly asked.

### Heuristics today, AI later
The Day 2 Launch Risk Analyzer uses **keyword matching against hardcoded lists** (`high_risk_keywords`, `medium_risk_keywords`) — no LLM calls. Don't "improve" this by adding API calls; AI integration is a later-day milestone. Do not introduce `anthropic`, `openai`, or LLM SDKs without confirming it matches the current day's scope.

### Skills are markdown specs, not code
Files in `skills/` (e.g. `launch_risk_analysis.md`) are **prompt-style behavior specifications** — input/output contracts, evaluation rules, expected output formats. They are not imported or executed by `app.py`. They're designed to be consumed by future agents (Day 5+). When adding a skill, follow the structure of `skills/launch_risk_analysis.md`: Purpose → Input → Output sections → Evaluation Rules → Expected Output Format.

### Day wrap — update these 5 things before every "Day N" commit

**This is a hard rule. Do not commit a `Day N - ...` message without completing all 5.**

1. `challenge/progress_tracker.md` — new Day N section: Status, Built (bullet list), Key design decisions (numbered), Lessons
2. `challenge/14_day_plan.md` — mark Day N ✅ Done
3. `README.md` — bump the shields.io badge numerator, add row to Current Application table, add line to build timeline, update architecture diagram
4. `lessons_learned/common_errors.md` — add any new anti-patterns discovered during the day
5. `design_decisions/dayN_*.md` — new file with design decisions, alternatives considered, and rationale

A git hook at `.git/hooks/post-commit` (installed via `bash scripts/install-hooks.sh`) will warn after any `Day N` commit if files 1–3 or 5 are missing. If you see that warning, run `git add <files> && git commit --amend --no-edit`.

### Lessons learned convention
After finishing a day, capture non-obvious learnings in `lessons_learned/` (see `day1_day2_lessons.md` for tone — short, first-person, what surprised the user). Errors and their fixes go in `lessons_learned/common_errors.md`.

## Commit style

Recent history uses `Day N - <short description>` or `<verb> <what>` (e.g. `Day 3 - Add launch risk analysis skill`, `Update README for Day 3 completion`). Keep messages tied to the day's milestone when relevant.
