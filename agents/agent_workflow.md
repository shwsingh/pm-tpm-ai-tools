# Agent Workflow — Bug → Triage → Escalation

## Purpose

The Agent Workflow is the Day 6 orchestration layer. It chains the Bug Triage Agent into a
3-stage pipeline so that bugs flow automatically from raw input to classified output to
actionable escalation artifacts.

This is the first multi-step agent in the AI TPM Copilot. Each stage has a defined input
contract, an output contract, and passes its output directly to the next stage.

---

## Stages

### Stage 1 — Ingest

**Input:** Raw free text (one or more bug reports, separated by blank lines).

**Output:**
- `valid_bugs` — list of bug strings ≥ 10 characters
- `rejected_bugs` — list of strings too short to triage
- `total_parsed` — integer count of all parsed segments

**Purpose:** Validate and normalize input before anything downstream runs.

---

### Stage 2 — Triage

**Input:** `valid_bugs` list from Stage 1.

**Output:** List of triage dicts (same contract as the Day 5 `triage()` function), each
augmented with `original_text` for downstream display.

**Purpose:** Classify severity, component, owner, and escalation need for each bug.
Also applies the batch P1 rule: if >2 P1s arrive in one batch, they are escalated
as a likely regression.

Implementation today is heuristic; the LLM swap-in is a single function replacement on Day 9.

---

### Stage 3 — Escalation Handler

**Input:** Triage results list from Stage 2.

**Output:**
- `incidents` — bugs where `escalate = True`
- `leads` — bugs where `needs_lead = True`
- `routine` — all other bugs
- `incident_drafts` — one markdown incident summary per incident bug
- `slack_messages` — one Slack-style on-call message per incident bug
- `lead_notification` — plain-text summary of all lead-review bugs

**Purpose:** Convert triage labels into actionable artifacts. Today these are draft text;
on Day 13 (MCP), the Slack messages will be posted and the incident drafts will create
Jira tickets automatically.

---

## Pipeline Contract

```
raw_text
  → ingest()        → { valid_bugs, rejected_bugs, total_parsed }
  → run_triage_stage() → [ triage_result, ... ]
  → escalation_handler() → { incidents, leads, routine, drafts, slack_messages, lead_notification }
```

Each function is pure (no side effects) and composable. The full pipeline can be
unit-tested by calling each stage function independently.

---

## Failure Modes and Guardrails

- If all bugs are rejected at ingest (all < 10 chars), the pipeline stops after Stage 1.
- The escalation handler never writes to external systems in v1 — all output is advisory.
- Batch P1 escalation only triggers at > 2 P1s to avoid false positives from a 2-bug report.

---

## Planned Upgrades

| Day | Upgrade |
|-----|---------|
| Day 9  | LLM-backed `triage()` replaces the heuristic classifier |
| Day 11 | DeepEval golden-set evaluation wired to Stage 2 output |
| Day 13 | MCP integration: Slack post + Jira ticket creation from Stage 3 artifacts |

---

## Status

- v1 (Day 6): Heuristic pipeline, all output advisory, no external system writes.
