# Launch Risk Analysis Skill

## Purpose

Analyze launch updates and determine launch readiness.

This skill is used by TPMs to identify:

* Risks
* Blockers
* Escalations
* Recommendations
* Executive summaries

---

## Input

Raw launch notes.

Example:

Telemetry is incomplete.

Security review is pending.

Connector testing is delayed by two weeks.

P1 bugs remain open.

---

## Output

### Launch Health

One of:

* Green
* Yellow
* Red

---

### Risks

List the top launch risks.

---

### Blockers

List launch blockers.

---

### Recommendations

Recommend actions required before launch.

---

### Executive Summary

Provide a concise leadership summary.

---

## Risk Evaluation Rules

### Red

Use Red if:

* Security approval missing
* Privacy approval missing
* P0 or P1 bugs open
* Launch blocked
* Major dependency blocked

---

### Yellow

Use Yellow if:

* Testing incomplete
* Dependency risk exists
* Milestone slipping

---

### Green

Use Green if:

* No critical blockers
* Launch criteria met

---

## Expected Output Format

Launch Health:
RED

Risks:
1.
2.

Blockers:
1.
2.

Recommendations:
1.
2.

Executive Summary:
...
