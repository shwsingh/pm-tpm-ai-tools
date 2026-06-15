# Dependency Agent Contract

## Purpose

Reason across a set of cross-team dependencies to identify critical path blockers,
cascading risk chains, and produce prioritized TPM actions.

---

## Skills Used

- `dependency_agent` (this agent's own skill spec)

---

## Input Contract

```json
[
  {
    "id": 1,
    "dependent_team": "Checkout",
    "provider_team": "Auth",
    "deliverable": "SSO token refresh API",
    "due_date": "2026-06-20",
    "status": "At Risk"
  }
]
```

---

## Output Contract

```json
{
  "health": "Red" | "Yellow" | "Green",
  "critical_path": [1, 3],
  "cascading_risks": [
    {"chain": [1, 2], "description": "Auth SSO delay blocks Checkout which blocks Mobile launch"}
  ],
  "dependencies": [
    {
      "id": 1,
      "risk_level": "High",
      "reasoning": "SSO token refresh is on critical path; Auth team has open P1 bug",
      "recommended_action": "Schedule Auth + Checkout sync by EOD Friday to align on workaround",
      "escalate": true
    }
  ],
  "tpm_actions": [
    "Escalate Auth SSO delay to eng leads — blocks 2 downstream teams",
    "Request daily status from Auth until SSO is green",
    "Draft contingency plan: can Checkout launch without SSO for non-enterprise users?"
  ],
  "exec_summary": "3 of 5 dependencies are at risk. Auth SSO delay is the critical blocker cascading into Checkout and Mobile. Immediate escalation recommended."
}
```

---

## Planner Pattern

```
Parse deps → Identify blockers → Trace cascades → Rank by impact → Generate actions → Summarize
```

---

## Failure Modes

| Failure | Handling |
|---------|---------|
| No blocked/at-risk deps | Return Green health, no escalations |
| Circular dependency detected | Flag in cascading_risks, note as misconfiguration |
| Missing due dates | Treat as unknown risk, flag for TPM to clarify |
| All deps blocked | Return Red, escalate all, exec summary flags launch at risk |

---

## MCP Upgrade Path (Day 13)

Today: manual input via Streamlit form.
Day 13: Jira/Linear MCP tool pulls dependency tickets automatically.
