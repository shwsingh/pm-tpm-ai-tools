# Bug Triage Skill

## Purpose

Classify and prioritize an incoming bug report so a TPM or on-call engineer can act on it within minutes.

This skill is used by TPMs, EMs, and on-call engineers to:

* Assign a severity (P0, P1, P2, P3)
* Identify the affected component
* Suggest an owning team
* Recommend a next action
* Flag whether the bug should escalate to an incident

---

## Input

A raw bug report.

Example:

The checkout page is throwing 500 errors for all users in the EU region since the last deploy. Revenue is dropping.

---

## Output

### Severity

One of:

* P0 — production outage, data loss, security breach, or revenue stop
* P1 — major feature broken, large user impact, no clean workaround
* P2 — minor feature broken, workaround exists
* P3 — cosmetic, nice-to-have, or low-impact

---

### Component

The system or surface area affected.

Examples: Checkout, Auth, Billing, Search, API, Mobile, Web, Data Pipeline.

---

### Suggested Owner

The team or role most likely to own the fix.

Examples: Payments team, Platform team, Frontend team, SRE.

---

### Priority

A short label combining severity and business impact:

* Drop-everything
* Next-sprint
* Backlog

---

### Suggested Next Action

One concrete next step (e.g., "Page on-call", "File for next sprint", "Add reproduction steps").

---

### Escalate to Incident?

Yes or No, with a one-line reason.

---

### Needs Lead Review?

Yes or No. Set to Yes when the bug is ambiguous, signals conflict, or the severity is high but evidence is thin. When Yes, the recommended owner becomes "Shweta (Lead)" and the next action is "Reach out to Shweta as the lead for triage discussion".

---

## Triage Evaluation Rules

### P0

Use P0 if any of these are true:

* Production is down
* Data loss or corruption
* Security or privacy breach
* Revenue stop or payment failure at scale
* SLA breach with customer escalation

→ Escalate to incident. Page on-call.

---

### P1

Use P1 if any of these are true:

* Major feature is broken for a large user segment
* No clean workaround
* Regression from a recent release
* Cross-team dependency blocked

→ Drop-everything for the owning team. Do not page on-call unless trending toward P0.

---

### P2

Use P2 if any of these are true:

* Minor feature is broken
* Workaround exists
* Affects a small user segment

→ Next-sprint.

---

### P3

Use P3 if any of these are true:

* Cosmetic only
* Internal-only tooling
* Documentation gap

→ Backlog.

---

## Expected Output Format

Severity:
P0 | P1 | P2 | P3

Component:
...

Suggested Owner:
...

Priority:
Drop-everything | Next-sprint | Backlog

Suggested Next Action:
...

Escalate to Incident?:
Yes | No — reason

Needs Lead Review?:
Yes | No — reason (when Yes, owner = "Shweta (Lead)")

Triage Summary:
One-line summary suitable for a Slack channel or ticket title.
