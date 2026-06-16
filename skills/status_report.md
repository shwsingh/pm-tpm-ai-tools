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

### Prerequisite Gate (not scored, but required)
All six input fields are present and non-empty (or explicitly "None" for optional fields).
All seven output sections are present in the report. A report missing any field or section
is returned for completion before scoring begins.

### Scored Dimensions

A status report is scored across five quality dimensions. Each is pass/fail.
A report is **Exec-Ready** only when all five pass.

---

### 1. Ask Specificity
Every ask makes clear what leadership needs to do, who specifically should do it, and
by when. Vague asks waste exec time and get ignored.

- ✅ Pass — each ask is: verb + named owner + decision point or deadline
- ❌ Fail — any ask uses passive language ("need alignment", "leadership should review"),
  is missing an owner, or doesn't distinguish what the TPM is handling vs what needs a decision

---

### 2. Status Accuracy
The status color must reflect the actual content — not the author's optimism.
Green means genuinely on track: no blockers, no risks that could move the timeline.
Yellow means something is at risk: a dependency slipping, a review pending, a blocker that
has a workaround but hasn't been resolved. Red means something is actively broken with no
current mitigation.

- ✅ Pass — color matches the severity of blockers and risks described in the content
- ❌ Fail — Green with any active blocker; Red with no concrete problem named;
  Yellow when a hard blocker exists with no mitigation (should be Red)

---

### 3. Impact Clarity
Every blocker and risk must name the downstream consequence — what breaks, slips, or
gets blocked if this is not resolved. Reporting a fact without its impact leaves leadership
unable to prioritize.

- ✅ Pass — each blocker/risk connects to a consequence: "X is blocked → Y launch slips",
  "Risk: API latency → checkout conversion drops on launch day"
- ❌ Fail — any blocker or risk is reported as a standalone fact with no downstream impact
  stated ("Auth integration is delayed", "API performance is a concern")

---

### 4. Next Week Concreteness
Next week items are deliverables with a completion signal — not ongoing activities.
A done state must be implied or explicit.

- ✅ Pass — each item names what will be delivered and what "done" looks like:
  "Complete auth integration and ship to staging by Friday"
- ❌ Fail — any item uses activity language: "continue working on", "make progress on",
  "look into", "investigate" — these describe effort, not outcomes

---

### 5. Exec Readability
A new VP joining the team must be able to read this report cold and know what is happening,
what is at risk, and what they are being asked to do — without follow-up questions.

- ✅ Pass — no unexplained acronyms, no team-internal jargon, no sentences that require
  prior context; the one-line summary alone communicates the week's status
- ❌ Fail — any acronym used without expansion on first use; jargon that assumes the reader
  knows the team's internal names, tools, or history

---

## Exec-Ready Bar

A report is **Exec-Ready** when all five scored dimensions pass.
A report is **Not Exec-Ready** when any dimension fails — the failing dimension and the
specific reason are surfaced so the TPM knows exactly what to fix before sending.

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
