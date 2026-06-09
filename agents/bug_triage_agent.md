# Bug Triage Agent

## Purpose

The Bug Triage Agent is the first agent in the AI TPM Copilot. It consumes the `bug_triage` skill, applies it to one or more incoming bug reports, and produces structured triage output that can be reviewed, escalated, or piped into a downstream workflow.

This is the first artifact in the project that has the *shape* of an agent rather than a skill. A skill defines what the work looks like; an agent decides when to do the work, which tools to use, and what to do with the result.

---

## Skill(s) Used

* `skills/bug_triage.md`

---

## Agent Contract

### Input

A single bug report as free text, or a list of bug reports.

### Output

For each bug:

* Severity (P0, P1, P2, P3)
* Component
* Suggested Owner
* Priority label (Drop-everything, Next-sprint, Backlog)
* Suggested Next Action
* Escalate to Incident? (Yes/No with reason)
* Triage Summary (one line)

---

## Planner Pattern

The agent follows a simple planner-executor loop:

1. **Parse** — read the incoming bug report.
2. **Classify** — apply the `bug_triage` skill rules to assign severity, component, and owner.
3. **Decide** — apply the escalation rules to determine if this bug becomes an incident.
4. **Respond** — emit structured output.

Today (Day 5) steps 2 and 3 are implemented with heuristics. The contract for the LLM-backed version (Day 9) is the same; only the implementation of step 2 changes.

---

## Tools

* `triage()` function in `projects/tpm_pm_toolkit/app.py` — the implementation of step 2.

Tools planned but not yet wired (later days):

* Jira MCP — to read existing tickets and write new triage results.
* GitHub MCP — to attach triage labels to issues.
* PagerDuty integration — to trigger an incident when escalation is required.

---

## Memory

No persistent memory in v1. Each triage call is stateless.

Planned for later days:

* Per-team triage history (Day 8 RAG corpus).
* Recently-seen-symptom memory to detect repeat bugs.

---

## Escalation Rules

The agent escalates a bug to an incident when any of the following hold:

* Severity = P0.
* The bug mentions "outage", "data loss", "security breach", "PII", or "revenue stop".
* More than two P1 bugs are submitted in the same triage batch (sign of a broader regression).

When the agent escalates, the suggested next action is overridden with "Page on-call" and the triage summary is prefixed with `[INCIDENT]`.

---

## Routing to Lead

When a bug cannot be triaged confidently, the agent routes it to **Shweta (Lead)** for further discussion instead of guessing.

Route to Lead when any of the following hold:

* The bug report is ambiguous, vague, or missing key signals (no component, no user impact, no environment).
* The keyword signals conflict (e.g., "minor" appears alongside "outage").
* The bug mentions multiple unrelated components and the agent cannot pick a primary owner.
* The suggested severity is P0 or P1 but the evidence is thin (only one keyword hit).
* The bug spans security or privacy *and* a non-security component (cross-functional review needed).

When routed to Lead, the agent:

* Sets Suggested Owner to "Shweta (Lead) — needs discussion".
* Sets Suggested Next Action to "Reach out to Shweta as the lead for triage discussion".
* Prefixes the Triage Summary with `[NEEDS LEAD]`.
* Does not auto-escalate to an incident even if P0 keywords are present — Lead decides.

The routing decision is itself a signal: if more than 20% of bugs route to Lead in a week, the agent's triage rules need tightening.

---

## Failure Modes and Guardrails

* The agent never writes to external systems in v1 (no Jira, no PagerDuty calls). Output is advisory only.
* If the bug report is empty or shorter than 10 characters, the agent returns "Insufficient information — request reproduction steps" instead of guessing.
* The agent never assigns severity above P1 when fewer than two P0 keywords are present, to avoid false-incident escalations.

---

## Evaluation

Day 5 evaluation is manual: run a small set of representative bugs through the agent and confirm severity, owner, and escalation are reasonable. Day 11 will add DeepEval against a golden set of labeled bugs.

---

## Status

* v1 (Day 5): Heuristic implementation with LLM-swap stub.
* v2 (Day 9): LLM-backed classification using Claude Sonnet via the Anthropic SDK.
* v3 (Day 11): DeepEval-scored and gated by a golden set.
* v4 (Day 13): MCP-wired to Jira and GitHub for real ticket reads and writes.
