#!/usr/bin/env python3
"""TPM Copilot MCP Server — Day 13.

Exposes TPM resources, tools, and prompts to Claude Desktop (or any MCP client).

Resources:
  tpm://launch-checklist   — live launch checklist
  tpm://risk-register      — active risk register
  tpm://capacity-plan      — team capacity plan

Tools:
  analyze_launch_risk      — score a launch description for risk
  generate_status_report   — draft an exec status report from bullet inputs
  create_escalation        — create a structured escalation from incident details

Prompts:
  launch_readiness_review  — guided launch readiness conversation
  weekly_exec_update       — guided weekly exec update conversation
"""

import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DATA_DIR = Path(__file__).parent / "data"

mcp = FastMCP("TPM Copilot")


# ── Resources ────────────────────────────────────────────────────────────────

@mcp.resource("tpm://launch-checklist")
def launch_checklist() -> str:
    """Current launch checklist with gate status."""
    return (DATA_DIR / "launch_checklist.md").read_text()


@mcp.resource("tpm://risk-register")
def risk_register() -> str:
    """Active risk register with likelihood, impact, and mitigations."""
    return (DATA_DIR / "risk_register.md").read_text()


@mcp.resource("tpm://capacity-plan")
def capacity_plan() -> str:
    """Team capacity plan and work breakdown for the current period."""
    return (DATA_DIR / "capacity_plan.md").read_text()


# ── Tools ────────────────────────────────────────────────────────────────────

@mcp.tool()
def analyze_launch_risk(
    feature_name: str,
    description: str,
    launch_date: str,
    dependencies: str = "",
    known_risks: str = "",
) -> str:
    """Score a launch for risk across 5 dimensions and return a structured assessment.

    Args:
        feature_name: Name of the feature or product being launched.
        description: What the launch does and who it affects.
        launch_date: Target launch date (e.g. 2026-07-01).
        dependencies: Comma-separated list of teams or systems this depends on.
        known_risks: Any risks already identified by the team.
    """
    HIGH_RISK_KEYWORDS = [
        "payment", "billing", "auth", "authentication", "gdpr", "privacy",
        "delete", "migration", "database", "prod", "production", "all users",
        "breaking change", "deprecat", "security", "pii", "compliance",
    ]
    MEDIUM_RISK_KEYWORDS = [
        "beta", "rollout", "experiment", "a/b", "new market", "third party",
        "external api", "webhook", "async", "queue", "cache", "cron",
    ]

    text = f"{feature_name} {description} {known_risks}".lower()
    dep_count = len([d for d in dependencies.split(",") if d.strip()])

    high_hits = [k for k in HIGH_RISK_KEYWORDS if k in text]
    med_hits  = [k for k in MEDIUM_RISK_KEYWORDS if k in text]

    tech_score      = min(5, 1 + len(high_hits) * 2 + len(med_hits))
    dep_score       = min(5, 1 + dep_count)
    timeline_score  = 2
    rollback_score  = 3 if not high_hits else 4
    user_impact     = min(5, 1 + len(high_hits) + (1 if "all users" in text else 0))

    overall = round((tech_score + dep_score + timeline_score + rollback_score + user_impact) / 5, 1)
    level = "HIGH" if overall >= 3.5 else "MEDIUM" if overall >= 2.5 else "LOW"

    result = {
        "feature": feature_name,
        "launch_date": launch_date,
        "overall_risk": level,
        "score": overall,
        "dimensions": {
            "technical_complexity": tech_score,
            "dependency_count": dep_score,
            "timeline_pressure": timeline_score,
            "rollback_complexity": rollback_score,
            "user_impact": user_impact,
        },
        "risk_signals": high_hits + med_hits,
        "dependency_count": dep_count,
        "recommendation": (
            "Block launch — resolve HIGH signals before proceeding." if level == "HIGH"
            else "Proceed with caution — add monitoring and rollback plan." if level == "MEDIUM"
            else "Clear to launch — standard monitoring applies."
        ),
    }
    return json.dumps(result, indent=2)


@mcp.tool()
def generate_status_report(
    project_name: str,
    status_color: str,
    accomplishments: str,
    next_week: str,
    blockers: str = "",
    metrics: str = "",
) -> str:
    """Draft an exec-ready status report from structured bullet inputs.

    Args:
        project_name: Name of the project or initiative.
        status_color: Overall status — GREEN, YELLOW, or RED.
        accomplishments: Bullet list of this week's completions (newline-separated).
        next_week: Bullet list of next week's priorities (newline-separated).
        blockers: Any blockers or risks needing exec attention (optional).
        metrics: Key metrics to highlight, e.g. 'DAU: 1200 (+15%)' (optional).
    """
    color_emoji = {"GREEN": "🟢", "YELLOW": "🟡", "RED": "🔴"}.get(status_color.upper(), "⚪")

    acc_lines = "\n".join(
        f"- {line.strip().lstrip('-').strip()}"
        for line in accomplishments.strip().splitlines() if line.strip()
    )
    next_lines = "\n".join(
        f"- {line.strip().lstrip('-').strip()}"
        for line in next_week.strip().splitlines() if line.strip()
    )

    report = f"""# {project_name} — Weekly Status

**Status:** {color_emoji} {status_color.upper()}

## This Week
{acc_lines}
"""
    if metrics.strip():
        metric_lines = "\n".join(
            f"- {m.strip()}" for m in metrics.strip().splitlines() if m.strip()
        )
        report += f"\n## Key Metrics\n{metric_lines}\n"

    report += f"\n## Next Week\n{next_lines}\n"

    if blockers.strip():
        blocker_lines = "\n".join(
            f"- {b.strip().lstrip('-').strip()}"
            for b in blockers.strip().splitlines() if b.strip()
        )
        report += f"\n## Blockers / Needs Attention\n{blocker_lines}\n"

    report += "\n---\n*Generated by AI TPM Copilot MCP Server*"
    return report


@mcp.tool()
def create_escalation(
    incident_title: str,
    severity: str,
    impact: str,
    timeline: str,
    owner: str,
    ask: str,
    context: str = "",
) -> str:
    """Create a structured escalation document for exec or on-call routing.

    Args:
        incident_title: Short title of the incident or issue.
        severity: SEV1 / SEV2 / SEV3.
        impact: Who and what is affected (users, revenue, systems).
        timeline: When it started and key events so far.
        owner: Current owner and on-call lead.
        ask: What decision or action is needed from escalation target.
        context: Additional background (optional).
    """
    sev_map = {
        "SEV1": ("🔴", "CRITICAL — Immediate exec attention required"),
        "SEV2": ("🟠", "HIGH — Response within 1 hour"),
        "SEV3": ("🟡", "MEDIUM — Response within 4 hours"),
    }
    emoji, label = sev_map.get(severity.upper(), ("⚪", "UNKNOWN"))

    doc = f"""# ESCALATION: {incident_title}

**Severity:** {emoji} {severity.upper()} — {label}
**Owner:** {owner}
**Escalated:** Now

## Impact
{impact}

## Timeline
{timeline}
"""
    if context.strip():
        doc += f"\n## Context\n{context}\n"

    doc += f"""
## Ask
{ask}

---
*Created by AI TPM Copilot MCP Server · Requires immediate acknowledgment for SEV1/SEV2*
"""
    return doc


# ── Prompts ──────────────────────────────────────────────────────────────────

@mcp.prompt()
def launch_readiness_review(feature_name: str, launch_date: str) -> str:
    """Start a guided launch readiness review conversation with Claude."""
    checklist = (DATA_DIR / "launch_checklist.md").read_text()
    risks = (DATA_DIR / "risk_register.md").read_text()

    return f"""You are an expert TPM conducting a launch readiness review for **{feature_name}** targeting **{launch_date}**.

Use the following reference documents to ground your review:

<launch_checklist>
{checklist}
</launch_checklist>

<risk_register>
{risks}
</risk_register>

Walk the user through the following gates in order:
1. **Engineering Readiness** — are all must-have items checked off?
2. **Quality & Evaluation** — are eval scores meeting bar?
3. **Documentation** — is customer-facing and internal documentation complete?
4. **Risk Assessment** — are all HIGH risks mitigated or accepted?
5. **Stakeholder Sign-off** — who still needs to approve?

For each gate: state current status, flag any open items, and give a clear GO / NO-GO recommendation.
End with an overall launch recommendation and the single most important action to unblock it."""


@mcp.prompt()
def weekly_exec_update(project_name: str, week_ending: str) -> str:
    """Start a guided weekly executive update conversation with Claude."""
    capacity = (DATA_DIR / "capacity_plan.md").read_text()
    risks = (DATA_DIR / "risk_register.md").read_text()

    return f"""You are an expert TPM helping draft the weekly executive update for **{project_name}** for the week ending **{week_ending}**.

Reference documents:

<capacity_plan>
{capacity}
</capacity_plan>

<risk_register>
{risks}
</risk_register>

Ask the user for:
1. This week's top 3 accomplishments
2. Any metrics or KPIs to highlight
3. Next week's top priorities
4. Any blockers needing exec attention

Then draft a concise exec status report (GREEN / YELLOW / RED) that:
- Leads with status color and one-line summary
- Uses bullet points, not paragraphs
- Flags only risks that need exec action
- Ends with a clear ask if one exists

Keep the total report under 250 words."""


if __name__ == "__main__":
    mcp.run()
