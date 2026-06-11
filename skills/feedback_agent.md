# Feedback Agent Skill

## Purpose

Analyze a batch of customer feedback items and surface actionable TPM insights:
sentiment, recurring themes, severity signals, and recommended actions. Replaces
manual feedback review with a structured, LLM-powered analysis pass.

---

## Input

- One or more customer feedback items (free text, one per paragraph)
- Optional: product area context (e.g. "Checkout", "Auth", "Mobile app")

---

## Output

### Per feedback item:
- **Sentiment**: Positive / Negative / Neutral / Mixed
- **Key themes**: up to 3 keywords or short phrases
- **Severity signal**: P0 (data loss / billing / can't use product) → P3 (minor annoyance)
- **TPM action**: one of: Escalate immediately | File bug | File improvement | Monitor | No action

### Aggregate summary:
- Sentiment distribution (count per category)
- Top 5 recurring themes across all items
- Critical items (P0 / P1) that need immediate attention
- Recommended TPM next steps (3 bullet points max)

---

## Evaluation Rules

A feedback analysis is **Good** when:
- [ ] Every item has a sentiment label and at least one theme
- [ ] Severity is calibrated — "hard to find the button" is never P0
- [ ] Critical items (P0/P1) are surfaced in the aggregate summary
- [ ] TPM actions are specific enough to act on (not just "investigate")
- [ ] Aggregate themes reflect actual patterns, not single-item noise

---

## Expected Output Format

```
FEEDBACK ANALYSIS — 8 items analyzed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sentiment: 2 Positive | 5 Negative | 1 Neutral

Top Themes: checkout errors, slow load time, missing confirmation email,
            confusing UI, payment failure

Critical Items (P0/P1):
  • [P0] "My payment was charged twice and I can't get a refund" → Escalate to Billing team immediately
  • [P1] "App crashes every time I try to checkout" → File P1 bug for Mobile/Checkout

Recommended TPM Actions:
  1. Escalate double-charge reports to Billing — potential data integrity issue
  2. File P1 bug: checkout crash on mobile (3 reports in last 24h)
  3. Add confirmation email to launch checklist — multiple users report missing it
```

---

## Claude Integration

- Model: `claude-sonnet-4-6`
- Prompt style: structured JSON output request
- System prompt sets the TPM context and output schema
- Each item analyzed in a single batch request (not per-item API calls)

---

## Upgrade Path

- Day 12: Multi-agent — Feedback Agent feeds findings to Escalation Agent
- Day 13: MCP integration — pull feedback directly from Slack/Zendesk
