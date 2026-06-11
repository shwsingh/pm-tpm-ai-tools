# Status Report Skill

## Purpose

Generate a structured, exec-ready weekly status report from raw TPM inputs.

This skill is used by TPMs to turn scattered weekly updates — shipped work, blockers,
risks, asks, and next-week plans — into a clean leadership report that can be sent
directly to a VP or director without editing.

---

## Input

Six structured fields:

| Field | Description |
|-------|-------------|
| `team_or_launch` | Team name or launch name this report covers |
| `shipped` | What was completed or shipped this week (free text) |
| `blockers` | Active blockers preventing progress (free text, or "None") |
| `risks` | Risks on the horizon that leadership should know about (free text, or "None") |
| `asks` | Explicit asks from leadership — decisions, approvals, unblocks needed |
| `next_week` | What the team plans to deliver next week |

---

## Output

### Status Color
One of: `Red` / `Yellow` / `Green`

Derived from blocker and risk signals:
- **Red** — active hard blockers, P0/P1 bugs open, security/privacy holds, missed milestone
- **Yellow** — risks present, dependencies at risk, reviews pending, delays possible
- **Green** — no blockers, no open risks, on track

### Exec Report
A formatted report with these sections:

1. **Header** — team/launch name, week, overall status
2. **This Week** — bullet list of what shipped
3. **Blockers** — bullet list, or "No blockers this week"
4. **Risks** — bullet list, or "No risks to flag"
5. **Asks** — bullet list of explicit asks from leadership, or "No asks this week"
6. **Next Week** — bullet list of planned deliverables
7. **One-Line Summary** — single sentence suitable for a leadership roll-up

---

## Evaluation Rules

A status report is scored across five quality dimensions. Each is pass/fail today;
Day 11 will add numeric scoring via DeepEval.

### 1. Completeness
All six input fields are present and non-empty (or explicitly "None" for optional fields).
All seven output sections are present in the report.

- ✅ Pass — all sections present, no section is blank or missing
- ❌ Fail — any section is empty, skipped, or filled with placeholder text

### 2. Ask Specificity
Every ask names **what** is needed, **who** should act, and **by when** if time-sensitive.
Vague asks ("need help", "leadership should look at this") fail.

- ✅ Pass — each ask is actionable: verb + owner + deadline or decision point
- ❌ Fail — any ask is vague, passive, or missing an owner

### 3. Status Accuracy
The status color must match the actual severity of blockers and risks described.
A Green status with active blockers is always wrong. A Red with no blockers is always wrong.

- ✅ Pass — color is consistent with the blocker/risk content
- ❌ Fail — color contradicts the content (e.g. Green + active blocker, Red + nothing wrong)

### 4. Clarity
The report contains no internal jargon, acronyms without expansion, or sentences that
require context to understand. A new VP joining the team should be able to read it
cold in under 60 seconds.

- ✅ Pass — plain language, no unexplained shorthand, readable in under 60 seconds
- ❌ Fail — jargon present, acronyms unexplained, or summary requires prior context

### 5. Next Week Concreteness
Next week items are deliverables with a completion signal — not activities.
"Complete auth integration and ship to staging" passes. "Continue working on auth" fails.

- ✅ Pass — each next-week item names a deliverable and implies a done state
- ❌ Fail — any item uses "continue", "work on", or "progress" without a completion signal

---

## Exec-Ready Bar

A report is **Exec-Ready** when all five eval dimensions pass.
A report is **Not Exec-Ready** when any dimension fails — the failing dimension is surfaced
so the TPM knows exactly what to fix before sending.

---

## Expected Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEKLY STATUS REPORT
Team / Launch: <name>
Week of: <date>
Overall Status: 🔴 Red | 🟡 Yellow | 🟢 Green
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THIS WEEK
• <shipped item 1>
• <shipped item 2>

BLOCKERS
• <blocker> — Owner: <owner if known>

RISKS
• <risk>

ASKS
• <specific ask: verb + owner + deadline>

NEXT WEEK
• <deliverable with completion signal>

SUMMARY
<One sentence suitable for a leadership roll-up.>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Notes

- Today (Day 7) the status color, formatting, and eval scores are heuristic (keyword-based).
- Day 9 will add LLM-backed summarization — Claude rewrites the one-line summary and
  flags ask specificity failures automatically.
- Day 11 adds DeepEval numeric scoring against a golden set of exec-ready reports.
- The output contract (fields, sections, format, eval dimensions) is stable across all versions.
