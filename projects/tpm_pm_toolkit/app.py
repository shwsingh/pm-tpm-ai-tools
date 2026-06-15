import re
import json
import os
import streamlit as st

st.set_page_config(
    page_title="TPM/PM AI Toolkit",
    page_icon="🚀",
    layout="wide"
)

# ── API Key (Day 9+) ──────────────────────────────────────────────────────────
from dotenv import load_dotenv
load_dotenv()
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .hero {
        padding: 32px;
        border-radius: 24px;
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #2563eb 100%);
        color: white;
        margin-bottom: 28px;
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .hero p {
        font-size: 18px;
        opacity: 0.9;
    }

    .card {
        background: #1e293b;
        padding: 24px;
        border-radius: 20px;
        border: 1px solid #334155;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        min-height: 185px;
        transition: 0.2s ease-in-out;
    }

    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 14px 36px rgba(0, 0, 0, 0.3);
    }

    .card h3 {
        margin-top: 0;
        color: #f1f5f9;
    }

    .card p {
        color: #94a3b8;
        font-size: 15px;
    }

    .pill {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        background: #eff6ff;
        color: #1d4ed8;
        font-size: 13px;
        font-weight: 600;
        margin-top: 10px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 700;
        color: #f1f5f9;
        margin-top: 16px;
        margin-bottom: 16px;
    }

    .goal-box {
        background: #1e3a5f;
        border-left: 6px solid #2563eb;
        padding: 18px 22px;
        border-radius: 16px;
        border-top: 1px solid #2d5a8e;
        border-right: 1px solid #2d5a8e;
        border-bottom: 1px solid #2d5a8e;
        margin-bottom: 12px;
        color: #e2e8f0;
    }

    .goal-box b {
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🏆 Challenge Progress")
    st.caption("TPM/PM AI Toolkit Build Journey")

    st.progress(10 / 14)
    st.metric("Overall Progress", "10 / 14 days", "+1 today")

    st.divider()

    st.subheader("✅ Completed")
    st.write("• Day 1 — TPM Dashboard")
    st.write("• Day 2 — Launch Risk Analyzer")
    st.write("• Day 3 — Launch Risk Skill")
    st.write("• Day 4 — PRD Builder Skill")
    st.write("• Day 5 — Bug Triage Agent")
    st.write("• Day 6 — Agent Workflow Pipeline")
    st.write("• Day 7 — Status Report Skill")
    st.write("• Day 8 — Knowledge Base (RAG)")
    st.write("• Day 9 — Feedback Agent + Claude triage")
    st.write("• Day 10 — Dependency Agent")

    st.subheader("🎯 Next Milestone")
    st.info("Day 11 — Evaluation Framework: score AI outputs against golden sets with DeepEval.")

# Header
st.markdown("""
<div class="hero">
    <h1>🚀 TPM/PM AI Toolkit</h1>
    <p>
        An executive-ready workspace for launch management, bug triage,
        PRD creation, status reporting, and customer feedback analysis.
    </p>
</div>
""", unsafe_allow_html=True)

# Executive summary metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Launches Tracked", "12", "+3")
col2.metric("Bugs Reviewed", "248", "+41")
col3.metric("PRDs Drafted", "7", "+2")
col4.metric("Reports Generated", "18", "+5")

st.markdown('<div class="section-title">🧰 Toolkit Modules</div>', unsafe_allow_html=True)

# Cards
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown("""
    <div class="card">
        <h3>📊 Launch Dashboard</h3>
        <p>Track launch readiness, risks, milestones, blockers, and executive-level status in one place.</p>
        <span class="pill">Executive View</span>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
    <div class="card">
        <h3>🐞 Bug Triage</h3>
        <p>Prioritize bugs using impact, severity, launch risk, customer pain, and ownership signals.</p>
        <span class="pill">AI Assisted</span>
    </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown("""
    <div class="card">
        <h3>📝 PRD Builder</h3>
        <p>Create structured product requirement drafts with goals, users, scope, metrics, and risks.</p>
        <span class="pill">Draft Faster</span>
    </div>
    """, unsafe_allow_html=True)

row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown("""
    <div class="card">
        <h3>📣 Status Reports</h3>
        <p>Generate leadership-ready weekly updates with accomplishments, risks, asks, and next steps.</p>
        <span class="pill">Leadership Ready</span>
    </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown("""
    <div class="card">
        <h3>💬 Feedback Analyzer</h3>
        <p>Summarize customer feedback, detect themes, identify sentiment, and convert insights into actions.</p>
        <span class="pill">Customer Signals</span>
    </div>
    """, unsafe_allow_html=True)

with row2_col3:
    st.markdown("""
    <div class="card">
        <h3>✨ Coming Soon</h3>
        <p>Add roadmap planning, meeting summarization, risk detection, and automated launch reviews.</p>
        <span class="pill">Next Build</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">🎯 Today\'s Learning Goals</div>', unsafe_allow_html=True)

goal1, goal2, goal3 = st.columns(3)

with goal1:
    st.markdown("""
    <div class="goal-box">
        <b>1. Improve UX Polish</b><br>
        Make the app feel modern, clean, and executive-friendly.
    </div>
    """, unsafe_allow_html=True)

with goal2:
    st.markdown("""
    <div class="goal-box">
        <b>2. Build Reusable Modules</b><br>
        Create feature sections that can later connect to AI workflows.
    </div>
    """, unsafe_allow_html=True)

with goal3:
    st.markdown("""
    <div class="goal-box">
        <b>3. Prepare for AI Integration</b><br>
        Design the layout so each card can become an AI-powered tool.
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.success("✅ App upgraded successfully. Next step: connect each module to a real AI workflow.")
st.divider()

st.markdown('<div class="section-title">🚦 Day 2: Launch Risk Analyzer</div>', unsafe_allow_html=True)

st.write(
    "Paste raw launch updates below. The analyzer will identify launch health, risks, blockers, "
    "recommendations, and an executive summary."
)

launch_notes = st.text_area(
    "Launch Notes",
    height=220,
    placeholder="Example: Telemetry is incomplete. Security review is pending. Connector testing is delayed by 2 weeks. P1 bugs are still open."
)

if st.button("Analyze Launch Risk"):
    if not launch_notes.strip():
        st.warning("Please enter launch notes first.")
    else:
        notes_lower = launch_notes.lower()

        risks = []
        blockers = []
        recommendations = []

        high_risk_keywords = [
            "blocked", "security", "privacy", "delayed", "delay",
            "missing", "not ready", "incomplete", "p0", "p1"
        ]

        medium_risk_keywords = [
            "dependency", "risk", "pending", "review", "testing", "open"
        ]

        high_hits = [word for word in high_risk_keywords if word in notes_lower]
        medium_hits = [word for word in medium_risk_keywords if word in notes_lower]

        if high_hits:
            health = "Red"
        elif medium_hits:
            health = "Yellow"
        else:
            health = "Green"

        if "security" in notes_lower:
            risks.append("Security review may block launch readiness.")
            blockers.append("Security approval is not complete.")
            recommendations.append("Escalate to the security review owner and confirm approval date.")

        if "privacy" in notes_lower:
            risks.append("Privacy review may block launch readiness.")
            blockers.append("Privacy approval is not complete.")
            recommendations.append("Confirm privacy review owner, SLA, and launch approval path.")

        if "telemetry" in notes_lower or "metrics" in notes_lower:
            risks.append("Telemetry or success metrics may be incomplete.")
            recommendations.append("Prioritize launch-critical telemetry before launch review.")

        if "delayed" in notes_lower or "delay" in notes_lower:
            risks.append("Milestone delay may impact launch timeline.")
            recommendations.append("Confirm revised ETA and evaluate scope reduction.")

        if "testing" in notes_lower:
            risks.append("Testing readiness may be incomplete.")
            recommendations.append("Create test completion plan with owner and deadline.")

        if "p0" in notes_lower or "p1" in notes_lower:
            risks.append("Launch-critical bugs are still open.")
            blockers.append("P0/P1 bugs need closure or explicit launch exception.")
            recommendations.append("Review bug hotlist and define launch-blocking criteria.")

        if "dependency" in notes_lower:
            risks.append("Cross-team dependency may affect launch readiness.")
            recommendations.append("Assign dependency owner and establish escalation path.")

        if not risks:
            risks.append("No major launch risks detected from the provided notes.")
            recommendations.append("Continue monitoring milestones, owners, and launch criteria.")

        st.subheader("Launch Health")

        if health == "Red":
            st.error("🔴 Red - High Risk")
        elif health == "Yellow":
            st.warning("🟡 Yellow - Medium Risk")
        else:
            st.success("🟢 Green - On Track")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Risks Found", len(risks))

        with col2:
            st.metric("Blockers Found", len(blockers))

        with col3:
            st.metric("Health", health)

        st.subheader("Top Risks")
        for risk in risks:
            st.write(f"- {risk}")

        st.subheader("Blockers")
        if blockers:
            for blocker in blockers:
                st.write(f"- {blocker}")
        else:
            st.write("- No hard blockers detected.")

        st.subheader("Recommendations")
        for recommendation in recommendations:
            st.write(f"- {recommendation}")

        st.subheader("Executive Summary")
        st.info(
            f"Launch health is currently **{health}** based on the provided updates. "
            "The main focus areas are risk mitigation, owner clarity, and launch-readiness validation."
        )

st.divider()

st.markdown('<div class="section-title">🐞 Day 5: Bug Triage Agent</div>', unsafe_allow_html=True)

st.write(
    "Paste one or more bug reports. The agent classifies severity, suggests an owner, "
    "and decides whether to escalate to an incident or route to the lead for discussion."
)

P0_KEYWORDS = ["outage", "down", "data loss", "data corruption", "security breach", "pii leak", "revenue stop", "payment failure"]
P1_KEYWORDS = ["broken", "regression", "500 error", "crash", "cannot", "unable", "blocker", "no workaround"]
P2_KEYWORDS = ["minor", "slow", "intermittent", "workaround", "small impact"]
P3_KEYWORDS = ["typo", "cosmetic", "ui glitch", "nit", "polish", "docs"]

COMPONENT_MAP = {
    "checkout": ("Checkout", "Payments team"),
    "payment": ("Checkout", "Payments team"),
    "billing": ("Billing", "Billing team"),
    "auth": ("Auth", "Identity team"),
    "login": ("Auth", "Identity team"),
    "search": ("Search", "Search team"),
    "api": ("API", "Platform team"),
    "mobile": ("Mobile", "Mobile team"),
    "android": ("Mobile", "Mobile team"),
    "ios": ("Mobile", "Mobile team"),
    "web": ("Web", "Frontend team"),
    "ui": ("Web", "Frontend team"),
    "pipeline": ("Data Pipeline", "Data team"),
    "etl": ("Data Pipeline", "Data team"),
}

INCIDENT_KEYWORDS = ["outage", "data loss", "security breach", "pii", "revenue stop"]
AMBIGUITY_KEYWORDS = ["maybe", "sometimes", "not sure", "unclear", "possibly"]

_TRIAGE_SYSTEM = """You are a senior TPM triage assistant. Given a bug report, return ONLY a JSON object
with these exact keys (no markdown, no explanation):
{
  "severity": "P0" | "P1" | "P2" | "P3" | "Unknown",
  "component": string (e.g. "Auth", "Billing", "Checkout", "Mobile", "API", "Unknown"),
  "owner": string (team name, or "Shweta (Lead) - needs discussion" if unclear),
  "priority": "Drop-everything" | "Next-sprint" | "Backlog" | "Needs-lead",
  "next_action": string (one clear action sentence),
  "escalate": boolean,
  "escalate_reason": string (empty string if escalate is false),
  "needs_lead": boolean,
  "needs_lead_reason": string (empty string if needs_lead is false),
  "summary": string (one-line: severity + component + short description)
}

Severity guide: P0 = production down / data loss / security / billing error / revenue impact.
P1 = major feature broken, significant user impact. P2 = degraded but workaround exists.
P3 = minor cosmetic / low impact. Unknown = insufficient info.
Set needs_lead=true when severity is Unknown, evidence is thin (single vague keyword),
or component cannot be determined. Set escalate=true only for P0 or confirmed incidents."""


def triage_with_claude(bug_text: str, api_key: str) -> dict:
    """LLM-backed triage using Claude. Same output contract as triage()."""
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=512,
            system=_TRIAGE_SYSTEM,
            messages=[{"role": "user", "content": f"Bug report:\n{bug_text.strip()}"}]
        )
        raw = response.content[0].text.strip()
        # Strip markdown code fences if present
        if raw.startswith("```"):
            raw = re.sub(r"^```[a-z]*\n?", "", raw)
            raw = re.sub(r"\n?```$", "", raw)
        return json.loads(raw)
    except Exception as e:
        result = triage(bug_text)
        result["_llm_error"] = str(e)
        return result


def triage(bug_text: str) -> dict:
    """Triage a single bug. Heuristic classifier — kept as fallback for Day 9+.

    The contract (input str, output dict with the keys below) is stable so the
    LLM swap-in is a single function replacement.
    """
    text = bug_text.strip()
    if len(text) < 10:
        return {
            "severity": "Unknown",
            "component": "Unknown",
            "owner": "Shweta (Lead) - needs discussion",
            "priority": "Needs-lead",
            "next_action": "Reach out to Shweta as the lead for triage discussion",
            "escalate": False,
            "escalate_reason": "Insufficient information",
            "needs_lead": True,
            "needs_lead_reason": "Bug report is too short to triage",
            "summary": "[NEEDS LEAD] Bug report is too short - request reproduction steps",
        }

    lower = text.lower()

    p0_hits = [k for k in P0_KEYWORDS if k in lower]
    p1_hits = [k for k in P1_KEYWORDS if k in lower]
    p2_hits = [k for k in P2_KEYWORDS if k in lower]
    p3_hits = [k for k in P3_KEYWORDS if k in lower]
    ambiguous_hits = [k for k in AMBIGUITY_KEYWORDS if k in lower]

    if p0_hits:
        severity = "P0"
    elif p1_hits:
        severity = "P1"
    elif p2_hits:
        severity = "P2"
    elif p3_hits:
        severity = "P3"
    else:
        severity = "Unknown"

    component = "Unknown"
    owner = "Unassigned"
    for keyword, (comp, team) in COMPONENT_MAP.items():
        if keyword in lower:
            component = comp
            owner = team
            break

    needs_lead = False
    needs_lead_reason = ""

    if severity == "Unknown":
        needs_lead = True
        needs_lead_reason = "No severity signal in the report"
    elif severity in {"P0", "P1"} and len(p0_hits) + len(p1_hits) < 2:
        needs_lead = True
        needs_lead_reason = f"{severity} severity inferred from a single keyword - evidence is thin"
    elif p2_hits and (p0_hits or "outage" in lower):
        needs_lead = True
        needs_lead_reason = "Conflicting signals - 'minor/workaround' alongside outage-class keywords"
    elif component == "Unknown":
        needs_lead = True
        needs_lead_reason = "Could not identify the affected component"
    elif ambiguous_hits:
        needs_lead = True
        needs_lead_reason = f"Ambiguous language detected: {', '.join(ambiguous_hits)}"

    escalate = False
    escalate_reason = ""
    if not needs_lead:
        if severity == "P0":
            escalate = True
            escalate_reason = "P0 severity - page on-call"
        elif any(k in lower for k in INCIDENT_KEYWORDS):
            escalate = True
            escalate_reason = "Incident keyword detected (outage / data loss / security / PII / revenue stop)"

    if needs_lead:
        owner = "Shweta (Lead) - needs discussion"
        next_action = "Reach out to Shweta as the lead for triage discussion"
        priority = "Needs-lead"
        summary_prefix = "[NEEDS LEAD] "
    elif escalate:
        next_action = "Page on-call"
        priority = "Drop-everything"
        summary_prefix = "[INCIDENT] "
    elif severity == "P1":
        next_action = "Drop-everything for the owning team"
        priority = "Drop-everything"
        summary_prefix = ""
    elif severity == "P2":
        next_action = "File for next sprint"
        priority = "Next-sprint"
        summary_prefix = ""
    elif severity == "P3":
        next_action = "Add to backlog"
        priority = "Backlog"
        summary_prefix = ""
    else:
        next_action = "Request reproduction steps and clarifying details"
        priority = "Needs-lead"
        summary_prefix = "[NEEDS LEAD] "

    short = text if len(text) <= 80 else text[:77] + "..."
    summary = f"{summary_prefix}{severity} - {component} - {short}"

    return {
        "severity": severity,
        "component": component,
        "owner": owner,
        "priority": priority,
        "next_action": next_action,
        "escalate": escalate,
        "escalate_reason": escalate_reason,
        "needs_lead": needs_lead,
        "needs_lead_reason": needs_lead_reason,
        "summary": summary,
    }


bug_input = st.text_area(
    "Bug Report(s)",
    height=220,
    placeholder=(
        "Example 1: The checkout page is throwing 500 errors for all users in the EU region since the last deploy. Revenue is dropping.\n\n"
        "Example 2: Minor UI glitch on the settings page - the toggle is misaligned on Safari.\n\n"
        "(Separate multiple bugs with a blank line.)"
    ),
)

if st.button("Triage Bugs"):
    if not bug_input.strip():
        st.warning("Please paste at least one bug report.")
    else:
        bugs = [b.strip() for b in re.split(r"\n[\s]*\n", bug_input.replace("\r\n", "\n")) if b.strip()]
        if ANTHROPIC_API_KEY:
            st.caption("🤖 Triage powered by Claude (Day 9)")
            results = [triage_with_claude(b, ANTHROPIC_API_KEY) for b in bugs]
        else:
            st.caption("⚙️ Triage using heuristic classifier — add API key in .env for Claude-powered triage")
            results = [triage(b) for b in bugs]

        p1_batch_count = sum(1 for r in results if r["severity"] == "P1")
        if p1_batch_count > 2:
            for r in results:
                if r["severity"] == "P1" and not r["needs_lead"]:
                    r["escalate"] = True
                    r["escalate_reason"] = f"{p1_batch_count} P1 bugs in this batch - possible broader regression"
                    r["next_action"] = "Page on-call"
                    r["priority"] = "Drop-everything"
                    if not r["summary"].startswith("[INCIDENT]"):
                        r["summary"] = "[INCIDENT] " + r["summary"]

        incident_count = sum(1 for r in results if r["escalate"])
        lead_count = sum(1 for r in results if r["needs_lead"])

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Bugs Triaged", len(results))
        with col2:
            st.metric("Incidents", incident_count)
        with col3:
            st.metric("Need Lead", lead_count)
        with col4:
            sev_counts = {s: sum(1 for r in results if r["severity"] == s) for s in ["P0", "P1", "P2", "P3"]}
            top_sev = max(sev_counts, key=lambda s: sev_counts[s]) if any(sev_counts.values()) else "—"
            st.metric("Top Severity", top_sev)

        st.subheader("Triage Results")

        for i, r in enumerate(results, start=1):
            with st.container():
                st.markdown(f"**Bug #{i}**")

                if r["escalate"]:
                    st.error(f"🚨 {r['severity']} INCIDENT - {r['escalate_reason']}")
                elif r["needs_lead"]:
                    st.warning(f"🟠 Needs Lead Review - {r['needs_lead_reason']}")
                elif r["severity"] == "P1":
                    st.warning(f"🟡 {r['severity']} - drop-everything")
                elif r["severity"] == "P2":
                    st.info(f"🔵 {r['severity']} - next-sprint")
                elif r["severity"] == "P3":
                    st.info(f"⚪ {r['severity']} - backlog")
                else:
                    st.info(f"⚪ {r['severity']}")

                c1, c2, c3 = st.columns(3)
                with c1:
                    st.write(f"**Component:** {r['component']}")
                with c2:
                    st.write(f"**Owner:** {r['owner']}")
                with c3:
                    st.write(f"**Priority:** {r['priority']}")

                st.write(f"**Next Action:** {r['next_action']}")
                st.caption(r["summary"])
                st.divider()

        if lead_count > 0:
            st.info(
                f"📩 {lead_count} bug(s) flagged as **Needs Lead Review** - "
                "please reach out to **Shweta (Lead)** for triage discussion before acting."
            )

st.divider()

# ── Day 6: Agent Workflow ────────────────────────────────────────────────────

st.markdown('<div class="section-title">⚙️ Day 6: Agent Workflow</div>', unsafe_allow_html=True)

st.write(
    "Run bugs through a 3-stage pipeline: **Ingest → Triage → Escalation Handler**. "
    "Each stage's output feeds the next. The escalation stage produces actionable artifacts — "
    "an incident summary draft and a Slack-style message — ready to send when MCP is wired on Day 13."
)


def ingest(raw_text: str) -> dict:
    """Stage 1 — parse and validate raw input."""
    # Split on any blank line (handles \n\n, \r\n\r\n, or lines with only whitespace)
    bugs = [b.strip() for b in re.split(r"\n[\s]*\n", raw_text.replace("\r\n", "\n")) if b.strip()]
    valid = [b for b in bugs if len(b) >= 10]
    rejected = [b for b in bugs if len(b) < 10]
    return {
        "valid_bugs": valid,
        "rejected_bugs": rejected,
        "total_parsed": len(bugs),
    }


def run_triage_stage(valid_bugs: list, api_key: str = "") -> list:
    """Stage 2 — triage each valid bug. Uses Claude when api_key provided, heuristic otherwise."""
    results = []
    for bug in valid_bugs:
        if api_key:
            r = triage_with_claude(bug, api_key)
        else:
            r = triage(bug)
        r["original_text"] = bug
        results.append(r)

    # Batch P1 escalation rule: >2 P1s in one batch = likely regression
    p1_count = sum(1 for r in results if r["severity"] == "P1")
    if p1_count > 2:
        for r in results:
            if r["severity"] == "P1" and not r["needs_lead"]:
                r["escalate"] = True
                r["escalate_reason"] = f"{p1_count} P1s in batch — possible regression"
                r["next_action"] = "Page on-call"
                r["priority"] = "Drop-everything"
                if not r["summary"].startswith("[INCIDENT]"):
                    r["summary"] = "[INCIDENT] " + r["summary"]
    return results


def escalation_handler(triage_results: list) -> dict:
    """Stage 3 — generate escalation artifacts for bugs that need action."""
    incidents = [r for r in triage_results if r["escalate"]]
    leads = [r for r in triage_results if r["needs_lead"]]
    routine = [r for r in triage_results if not r["escalate"] and not r["needs_lead"]]

    # Draft incident summary (one per incident bug)
    incident_drafts = []
    for r in incidents:
        draft = (
            f"**[INCIDENT DRAFT]** {r['severity']} — {r['component']}\n\n"
            f"**Summary:** {r['summary']}\n\n"
            f"**Reason:** {r['escalate_reason']}\n\n"
            f"**Suggested Owner:** {r['owner']}\n\n"
            f"**Immediate Action:** {r['next_action']}"
        )
        incident_drafts.append(draft)

    # Slack-style on-call message
    slack_messages = []
    for r in incidents:
        msg = (
            f":rotating_light: *INCIDENT — {r['severity']} / {r['component']}* :rotating_light:\n"
            f"> {r['original_text'][:120]}{'...' if len(r['original_text']) > 120 else ''}\n"
            f"Reason: {r['escalate_reason']}\n"
            f"Assigned to: {r['owner']} | Action: {r['next_action']}"
        )
        slack_messages.append(msg)

    # Lead notification summary
    lead_notification = ""
    if leads:
        items = "\n".join(f"• {r['summary']}" for r in leads)
        lead_notification = (
            f"{len(leads)} bug(s) need your review before action can be taken:\n\n{items}"
        )

    return {
        "incidents": incidents,
        "leads": leads,
        "routine": routine,
        "incident_drafts": incident_drafts,
        "slack_messages": slack_messages,
        "lead_notification": lead_notification,
    }


workflow_input = st.text_area(
    "Bug Report(s) — Workflow Input",
    height=220,
    placeholder=(
        "Paste one or more bug reports, separated by blank lines.\n\n"
        "Example 1: The payment API is returning 500 errors for all EU users since the last deploy. Revenue is dropping fast.\n\n"
        "Example 2: Search results are slow on mobile — takes 8 seconds, workaround is to use the web app.\n\n"
        "Example 3: There is a typo on the settings page — 'Prefrence' should be 'Preference'."
    ),
)

if st.button("Run Agent Workflow"):
    if not workflow_input.strip():
        st.warning("Please paste at least one bug report.")
    else:
        # ── Stage 1: Ingest ──────────────────────────────────────────────────
        with st.expander("Stage 1 — Ingest", expanded=True):
            ingested = ingest(workflow_input)
            c1, c2, c3 = st.columns(3)
            c1.metric("Parsed", ingested["total_parsed"])
            c2.metric("Valid", len(ingested["valid_bugs"]))
            c3.metric("Rejected (too short)", len(ingested["rejected_bugs"]))
            if ingested["rejected_bugs"]:
                st.warning("Rejected: " + " | ".join(ingested["rejected_bugs"]))
            st.success(f"✅ {len(ingested['valid_bugs'])} bug(s) passed ingest and will be triaged.")

        if not ingested["valid_bugs"]:
            st.error("No valid bugs to process.")
        else:
            # ── Stage 2: Triage ──────────────────────────────────────────────
            triage_results = run_triage_stage(ingested["valid_bugs"], api_key=ANTHROPIC_API_KEY)

            with st.expander("Stage 2 — Triage", expanded=True):
                if ANTHROPIC_API_KEY:
                    st.caption("🤖 Triage powered by Claude (Day 9)")
                else:
                    st.caption("⚙️ Triage using heuristic classifier — add API key for Claude-powered triage")
                sev_counts = {}
                for r in triage_results:
                    sev_counts[r["severity"]] = sev_counts.get(r["severity"], 0) + 1

                cols = st.columns(len(sev_counts) + 1)
                cols[0].metric("Total Triaged", len(triage_results))
                for i, (sev, count) in enumerate(sorted(sev_counts.items()), start=1):
                    cols[i].metric(sev, count)

                for i, r in enumerate(triage_results, start=1):
                    label = r["summary"]
                    if r["escalate"]:
                        st.error(f"Bug #{i}: {label}")
                    elif r["needs_lead"]:
                        st.warning(f"Bug #{i}: {label}")
                    elif r["severity"] in ("P1", "P0"):
                        st.warning(f"Bug #{i}: {label}")
                    else:
                        st.info(f"Bug #{i}: {label}")

            # ── Stage 3: Escalation Handler ──────────────────────────────────
            escalation = escalation_handler(triage_results)

            with st.expander("Stage 3 — Escalation Handler", expanded=True):
                e1, e2, e3 = st.columns(3)
                e1.metric("Incidents", len(escalation["incidents"]), delta="Page on-call" if escalation["incidents"] else None)
                e2.metric("Need Lead", len(escalation["leads"]))
                e3.metric("Routine", len(escalation["routine"]))

                if escalation["incident_drafts"]:
                    st.subheader("Incident Drafts")
                    for draft in escalation["incident_drafts"]:
                        st.markdown(draft)
                        st.divider()

                if escalation["slack_messages"]:
                    st.subheader("On-Call Slack Messages")
                    for msg in escalation["slack_messages"]:
                        st.code(msg, language=None)

                if escalation["lead_notification"]:
                    st.subheader("Lead Notification")
                    st.info(escalation["lead_notification"])

                if not escalation["incidents"] and not escalation["leads"]:
                    st.success("✅ All bugs triaged to routine queues — no escalation needed.")

            # Save pipeline output for Day 7 auto-population
            st.session_state["last_pipeline"] = {
                "triage_results": triage_results,
                "escalation": escalation,
            }

st.divider()

# ── Day 7: Status Report Skill ───────────────────────────────────────────────

st.markdown('<div class="section-title">📋 Day 7: Status Report Skill</div>', unsafe_allow_html=True)

st.write(
    "Blockers, risks, and asks are **auto-populated from the last pipeline run** (Day 6). "
    "Review and edit every field, then score the report before confirming."
)

BLOCKER_RED_KEYWORDS = ["blocked", "blocker", "on hold", "security hold", "privacy hold",
                        "p0", "p1", "missed milestone", "overdue", "escalation needed"]
RISK_YELLOW_KEYWORDS = ["at risk", "risk", "delay", "delayed", "pending", "dependency",
                        "waiting", "review needed", "may slip", "concern"]
VAGUE_ASK_WORDS = ["help", "look at", "should review", "need support", "need input",
                   "leadership attention", "someone should"]
WEAK_NEXT_WEEK_WORDS = ["continue", "work on", "progress", "keep working", "ongoing",
                        "follow up", "look into"]


def score_report(team, shipped, blockers, risks, asks, next_week):
    scores = {}
    notes = {}

    fields = {"Team/Launch": team, "Shipped": shipped, "Next Week": next_week}
    empty = [k for k, v in fields.items() if not v.strip()]
    scores["Completeness"] = len(empty) == 0
    notes["Completeness"] = f"Missing: {', '.join(empty)}" if empty else "All required fields filled"

    if not asks.strip() or asks.strip().lower() in ("none", "n/a", "no asks"):
        scores["Ask Specificity"] = True
        notes["Ask Specificity"] = "No asks this week"
    else:
        vague = [w for w in VAGUE_ASK_WORDS if w in asks.lower()]
        scores["Ask Specificity"] = len(vague) == 0
        notes["Ask Specificity"] = f"Vague language: {', '.join(vague)}" if vague else "Asks appear specific"

    blocker_lower = blockers.lower()
    risk_lower = risks.lower()
    has_blocker = any(k in blocker_lower for k in BLOCKER_RED_KEYWORDS) and blocker_lower not in ("none", "n/a", "no blockers")
    has_risk = any(k in risk_lower for k in RISK_YELLOW_KEYWORDS) and risk_lower not in ("none", "n/a", "no risks")
    status = "Red" if has_blocker else "Yellow" if has_risk else "Green"
    scores["Status Accuracy"] = True
    notes["Status Accuracy"] = f"Status derived from content — {status} is consistent"

    all_text = " ".join([shipped, blockers, risks, asks, next_week])
    acronyms = re.findall(r'\b[A-Z]{3,}\b', all_text)
    known = {"TPM", "PM", "PRD", "API", "SDK", "MCP", "RAG", "NLP", "ETL", "SLA",
             "PII", "P0", "P1", "P2", "P3", "UI", "UX", "QA", "MVP", "OKR", "KPI",
             "ETA", "EOD", "EOW", "LGTM", "WIP", "TBD", "VP", "IC", "iOS"}
    unexplained = list(set(a for a in acronyms if a not in known))
    scores["Clarity"] = len(unexplained) == 0
    notes["Clarity"] = f"Unexplained acronyms: {', '.join(unexplained)}" if unexplained else "No unexplained acronyms"

    weak = [w for w in WEAK_NEXT_WEEK_WORDS if w in next_week.lower()]
    scores["Next Week Concreteness"] = len(weak) == 0
    notes["Next Week Concreteness"] = f"Weak language: {', '.join(weak)}" if weak else "Next week items appear concrete"

    return scores, notes, status


def build_report(team, shipped, blockers, risks, asks, next_week, status, week_of):
    sep = "━" * 42

    def bullets(text):
        if not text.strip() or text.strip().lower() in ("none", "n/a"):
            return "• None"
        lines = [l.strip("•- ").strip() for l in text.strip().splitlines() if l.strip()]
        return "\n".join(f"• {l}" for l in lines)

    icon = {"Red": "🔴", "Yellow": "🟡", "Green": "🟢"}[status]
    summary_map = {
        "Red": f"{team} is currently blocked and needs leadership action to stay on track.",
        "Yellow": f"{team} is progressing with risks that should be monitored this week.",
        "Green": f"{team} is on track — no blockers or risks to flag this week.",
    }

    return f"""{sep}
WEEKLY STATUS REPORT
Team / Launch: {team}
Week of: {week_of}
Overall Status: {icon} {status}
{sep}

THIS WEEK
{bullets(shipped)}

BLOCKERS
{bullets(blockers)}

RISKS
{bullets(risks)}

ASKS
{bullets(asks)}

NEXT WEEK
{bullets(next_week)}

SUMMARY
{summary_map[status]}
{sep}"""


def _plain_risk_reason(r):
    """Translate internal needs_lead_reason into exec-readable language."""
    reason = r.get("needs_lead_reason", "").lower()
    component = r.get("component", "Unknown")
    severity = r.get("severity", "Unknown")

    if "no severity signal" in reason or severity == "Unknown":
        return (f"{component}: bug reported with unclear impact — "
                "under lead review to determine priority and owner")
    if "single keyword" in reason or "thin" in reason:
        return (f"{component}: {severity} bug flagged — "
                "evidence is limited, lead review needed before escalating")
    if "conflicting signal" in reason:
        return (f"{component}: bug has mixed severity signals — "
                "lead review needed to confirm priority")
    if "unknown component" in reason or "could not identify" in reason:
        return (f"Unrouted bug: affected area unclear — "
                "lead review needed to assign owner and priority")
    if "ambiguous" in reason:
        return (f"{component}: bug description is ambiguous — "
                "lead review needed to confirm impact before acting")
    # fallback: plain rewrite of whatever the reason is
    return f"{component}: under lead review — {r.get('needs_lead_reason', 'details unclear')}"


def auto_populate_from_pipeline(pipeline):
    """Derive blockers, risks, and asks from last pipeline run in exec-ready language."""
    escalation = pipeline["escalation"]
    triage_results = pipeline["triage_results"]

    blockers_lines = []
    for r in escalation["incidents"]:
        action = r["next_action"].rstrip(".")
        blockers_lines.append(
            f"{r['component']} {r['severity']} incident — on-call paged, {action.lower()}"
        )
    auto_blockers = "\n".join(blockers_lines) if blockers_lines else "None"

    risks_lines = []
    for r in escalation["leads"]:
        risks_lines.append(_plain_risk_reason(r))
    auto_risks = "\n".join(risks_lines) if risks_lines else "None"

    asks_lines = []
    for r in escalation["incidents"]:
        asks_lines.append(
            f"Confirm incident response plan for {r['component']} {r['severity']} outage "
            f"and approve resolution timeline"
        )
    if escalation["leads"]:
        asks_lines.append(
            f"Review {len(escalation['leads'])} bug(s) with unclear priority "
            "and confirm owner and next action before end of week"
        )
    auto_asks = "\n".join(asks_lines) if asks_lines else "None"

    sev_summary = ", ".join(
        f"{r['severity']} ({r['component']})" for r in triage_results
        if not r["needs_lead"] and not r["escalate"]
    )
    auto_shipped = (
        f"Triaged {len(triage_results)} bug(s) through the agent workflow\n"
        f"Routine bugs: {sev_summary if sev_summary else 'none'}"
    )

    return auto_blockers, auto_risks, auto_asks, auto_shipped


# ── Auto-populate defaults from last pipeline run ────────────────────────────
pipeline = st.session_state.get("last_pipeline")

if pipeline:
    st.info("✨ Blockers, risks, and asks auto-populated from the last pipeline run. Review and edit before scoring.")
    default_blockers, default_risks, default_asks, default_shipped = auto_populate_from_pipeline(pipeline)
else:
    st.warning("No pipeline run found — run the Day 6 Agent Workflow above first to auto-populate fields.")
    default_blockers = default_risks = default_asks = default_shipped = ""

# ── Step 1: Review & Edit ─────────────────────────────────────────────────────
st.subheader("Step 1 — Review & Edit")

with st.form("sr_review_form"):
    sr_team = st.text_input("Team / Launch Name", placeholder="e.g. Checkout v2 Launch")
    sr_week = st.text_input("Week of", value="June 9–13, 2026")
    sr_shipped = st.text_area("What shipped this week", value=default_shipped, height=100)
    sr_blockers = st.text_area("Blockers", value=default_blockers, height=100)
    sr_risks = st.text_area("Risks", value=default_risks, height=100)
    sr_asks = st.text_area("Asks from leadership", value=default_asks, height=100)
    sr_next = st.text_area("Next week plan", height=100,
        placeholder="e.g. Ship staging build to QA by Wednesday\nComplete load testing and sign off by Friday")
    preview_clicked = st.form_submit_button("Score & Preview Report")

# ── Step 2: Eval + Confirm ────────────────────────────────────────────────────
if preview_clicked:
    if not sr_team.strip() or not sr_shipped.strip() or not sr_next.strip():
        st.warning("Team name, shipped work, and next week plan are required.")
    else:
        st.subheader("Step 2 — Eval Scores")

        scores, notes, status = score_report(
            sr_team, sr_shipped, sr_blockers, sr_risks, sr_asks, sr_next
        )
        week_label = sr_week.strip() if sr_week.strip() else "Week not specified"

        if status == "Red":
            st.error("🔴 Red — Active blockers detected.")
        elif status == "Yellow":
            st.warning("🟡 Yellow — Risks present.")
        else:
            st.success("🟢 Green — On track.")

        ec1, ec2, ec3, ec4, ec5 = st.columns(5)
        for col, (dim, passed) in zip([ec1, ec2, ec3, ec4, ec5], scores.items()):
            col.metric(dim, "✅ Pass" if passed else "❌ Fail")

        all_pass = all(scores.values())
        if all_pass:
            st.success("✅ Exec-Ready — all five quality dimensions pass.")
        else:
            failed_items = [f"- **{d}**: {notes[d]}" for d, p in scores.items() if not p]
            st.warning(
                "⚠️ Not Exec-Ready — fix these before sending (or confirm anyway):\n\n"
                + "\n".join(failed_items)
            )

        report = build_report(
            sr_team, sr_shipped, sr_blockers, sr_risks, sr_asks, sr_next, status, week_label
        )

        st.subheader("Step 3 — Confirm & Finalize")
        st.caption("Review the report below. Click Confirm to finalize.")
        st.code(report, language=None)

        if st.button("✅ Confirm & Finalize Report", type="primary"):
            st.session_state["finalized_report"] = report
            st.success("Report finalized. Copy it above and send to leadership.")

        if st.session_state.get("finalized_report") == report:
            st.balloons()

st.divider()

# ── Day 8: Knowledge Base (RAG) ──────────────────────────────────────────────

st.markdown('<div class="section-title">📚 Day 8: Knowledge Base</div>', unsafe_allow_html=True)

st.write(
    "Upload TPM docs and search them by question. "
    "Supported formats: `.txt`, `.md`, `.docx`, `.csv` (Google Sheets export). "
    "Today retrieval is keyword-based — Day 9 upgrades to embedding search with Claude."
)


def extract_text_chunks(uploaded_file) -> list[dict]:
    """Extract text chunks from an uploaded file. Returns list of {source, text} dicts."""
    name = uploaded_file.name
    ext = name.rsplit(".", 1)[-1].lower()
    chunks = []

    if ext in ("txt", "md"):
        content = uploaded_file.read().decode("utf-8", errors="ignore")
        paragraphs = re.split(r"\n\s*\n", content)
        for p in paragraphs:
            p = p.strip()
            if len(p) >= 20:
                chunks.append({"source": name, "text": p})

    elif ext == "docx":
        import docx as _docx
        import io
        doc = _docx.Document(io.BytesIO(uploaded_file.read()))
        for para in doc.paragraphs:
            p = para.text.strip()
            if len(p) >= 20:
                chunks.append({"source": name, "text": p})

    elif ext == "csv":
        import io
        import pandas as _pd
        df = _pd.read_csv(io.BytesIO(uploaded_file.read()))
        headers = " | ".join(str(c) for c in df.columns)
        for _, row in df.iterrows():
            row_text = " | ".join(str(v) for v in row.values)
            text = f"{headers}\n{row_text}"
            if len(text) >= 20:
                chunks.append({"source": name, "text": text})

    return chunks


def keyword_search(chunks: list[dict], query: str, top_n: int = 5) -> list[dict]:
    """Score chunks by keyword overlap with query. Returns top_n results."""
    query_tokens = set(re.sub(r"[^\w\s]", "", query.lower()).split())
    if not query_tokens:
        return []

    scored = []
    for chunk in chunks:
        chunk_lower = chunk["text"].lower()
        hits = sum(1 for t in query_tokens if t in chunk_lower)
        if hits > 0:
            score = round(hits / len(query_tokens), 2)
            scored.append({**chunk, "score": score, "hits": hits})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_n]


# Upload
uploaded_files = st.file_uploader(
    "Upload documents",
    type=["txt", "md", "docx", "csv"],
    accept_multiple_files=True,
    help="Google Docs → File → Download → Word (.docx) | Google Sheets → File → Download → CSV"
)

if uploaded_files:
    all_chunks = []
    for f in uploaded_files:
        chunks = extract_text_chunks(f)
        all_chunks.extend(chunks)
        st.caption(f"✅ {f.name} — {len(chunks)} chunk(s) indexed")

    st.session_state["kb_chunks"] = all_chunks
    st.success(f"📖 {len(all_chunks)} chunks indexed from {len(uploaded_files)} document(s)")

kb_chunks = st.session_state.get("kb_chunks", [])

query = st.text_input(
    "Ask a question",
    placeholder="e.g. What are the launch blockers? Who owns the auth component?",
    disabled=len(kb_chunks) == 0
)

if query and kb_chunks:
    results = keyword_search(kb_chunks, query)

    if not results:
        st.warning("No matching chunks found. Try different keywords.")
    else:
        sources = list(dict.fromkeys(r["source"] for r in results))
        c1, c2, c3 = st.columns(3)
        c1.metric("Chunks Returned", len(results))
        c2.metric("Documents Searched", len(set(c["source"] for c in kb_chunks)))
        c3.metric("Top Source", results[0]["source"])

        st.subheader(f"Top {len(results)} Results")
        for i, r in enumerate(results, 1):
            with st.expander(f"[{i}] {r['source']} — Score: {r['score']}", expanded=i == 1):
                st.write(r["text"])

elif len(kb_chunks) == 0 and not uploaded_files:
    st.info("Upload at least one document to enable search.")


# ── Day 9: Feedback Agent ─────────────────────────────────────────────────────

st.markdown('<div class="section-title">💬 Day 9: Feedback Agent</div>', unsafe_allow_html=True)

st.write(
    "Paste customer feedback (one item per paragraph) and Claude will classify sentiment, "
    "extract themes, flag critical issues, and recommend TPM actions."
)

_FEEDBACK_SYSTEM = """You are a senior TPM analyzing customer feedback. Given a list of feedback items,
return ONLY a JSON object (no markdown, no explanation) with this structure:
{
  "items": [
    {
      "text_preview": "<first 80 chars of the feedback>",
      "sentiment": "Positive" | "Negative" | "Neutral" | "Mixed",
      "themes": ["theme1", "theme2"],
      "severity": "P0" | "P1" | "P2" | "P3",
      "action": "Escalate immediately" | "File bug" | "File improvement" | "Monitor" | "No action"
    }
  ],
  "summary": {
    "total": <int>,
    "sentiment_counts": {"Positive": <int>, "Negative": <int>, "Neutral": <int>, "Mixed": <int>},
    "top_themes": ["theme1", "theme2", "theme3"],
    "critical_items": [{"preview": "<text>", "severity": "P0"|"P1", "action": "<action>"}],
    "tpm_next_steps": ["step1", "step2", "step3"]
  }
}

Severity guide: P0 = billing errors, data loss, can't complete a core action, security.
P1 = major feature broken, multiple users affected. P2 = degraded experience, workaround exists.
P3 = minor cosmetic, low-impact. Calibrate carefully — "hard to find button" is P3, not P0."""


def analyze_feedback(feedback_text: str, api_key: str) -> dict:
    """Send feedback to Claude and return structured analysis."""
    import anthropic
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=_FEEDBACK_SYSTEM,
        messages=[{"role": "user", "content": f"Customer feedback items:\n\n{feedback_text.strip()}"}]
    )
    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


if not ANTHROPIC_API_KEY:
    st.warning("Add your Anthropic API key in the sidebar to use the Feedback Agent.")
else:
    feedback_input = st.text_area(
        "Customer Feedback",
        height=220,
        placeholder=(
            "The checkout page keeps crashing on mobile. I've tried three times and lost my cart.\n\n"
            "Love the new dashboard design! Much easier to find what I need.\n\n"
            "My account was charged twice for the same order. This is unacceptable.\n\n"
            "The search results are a bit slow but it eventually loads."
        )
    )

    if st.button("Analyze Feedback", type="primary", disabled=not feedback_input.strip()):
        items_raw = [i.strip() for i in re.split(r"\n\s*\n", feedback_input.replace("\r\n", "\n")) if i.strip()]
        if not items_raw:
            st.error("No feedback items found. Separate each item with a blank line.")
        else:
            with st.spinner(f"Claude is analyzing {len(items_raw)} feedback item(s)..."):
                try:
                    result = analyze_feedback(feedback_input, ANTHROPIC_API_KEY)
                    st.session_state["feedback_analysis"] = result
                except Exception as e:
                    st.error(f"Analysis failed: {e}")

    analysis = st.session_state.get("feedback_analysis")
    if analysis:
        summary = analysis.get("summary", {})
        items = analysis.get("items", [])

        # ── Aggregate metrics ────────────────────────────────────────────────
        st.subheader("Aggregate Summary")
        sc = summary.get("sentiment_counts", {})
        cols = st.columns(5)
        cols[0].metric("Total Items", summary.get("total", len(items)))
        cols[1].metric("Negative", sc.get("Negative", 0))
        cols[2].metric("Positive", sc.get("Positive", 0))
        cols[3].metric("Neutral", sc.get("Neutral", 0))
        cols[4].metric("Mixed", sc.get("Mixed", 0))

        top_themes = summary.get("top_themes", [])
        if top_themes:
            st.markdown("**Top Themes:** " + " · ".join(f"`{t}`" for t in top_themes))

        critical = summary.get("critical_items", [])
        if critical:
            st.markdown("**Critical Items (P0/P1):**")
            for c in critical:
                sev_color = "🔴" if c.get("severity") == "P0" else "🟠"
                st.markdown(f"{sev_color} **[{c.get('severity')}]** {c.get('preview', '')} → _{c.get('action', '')}_")

        next_steps = summary.get("tpm_next_steps", [])
        if next_steps:
            st.markdown("**Recommended TPM Actions:**")
            for i, step in enumerate(next_steps, 1):
                st.markdown(f"{i}. {step}")

        # ── Per-item breakdown ───────────────────────────────────────────────
        st.subheader(f"Per-Item Breakdown ({len(items)} items)")
        sentiment_icon = {"Positive": "✅", "Negative": "❌", "Neutral": "➖", "Mixed": "🔀"}
        severity_icon = {"P0": "🔴", "P1": "🟠", "P2": "🟡", "P3": "🟢"}
        for i, item in enumerate(items, 1):
            sev = item.get("severity", "P3")
            sent = item.get("sentiment", "Neutral")
            label = f"[{i}] {severity_icon.get(sev, '')} {sev} · {sentiment_icon.get(sent, '')} {sent} · {item.get('text_preview', '')[:60]}"
            with st.expander(label, expanded=(sev in {"P0", "P1"} and i <= 3)):
                th = item.get("themes", [])
                st.markdown(f"**Themes:** {', '.join(th) if th else '—'}")
                st.markdown(f"**Severity:** {sev}  |  **Sentiment:** {sent}")
                st.markdown(f"**TPM Action:** {item.get('action', '—')}")


# ── Day 10: Dependency Agent ──────────────────────────────────────────────────

st.markdown('<div class="section-title">🔗 Day 10: Dependency Agent</div>', unsafe_allow_html=True)

st.write(
    "Track cross-team dependencies for your launch. Add each dependency below, "
    "then let Claude reason across the full graph to identify the critical path, "
    "cascading risks, and prioritized TPM actions."
)

_DEP_SYSTEM = """You are a senior TPM analyzing cross-team launch dependencies.
Given a JSON list of dependencies, return ONLY a JSON object (no markdown, no explanation):
{
  "health": "Green" | "Yellow" | "Red",
  "critical_path": [<list of dep ids that gate the launch>],
  "cascading_risks": [
    {"chain": [<id>, <id>], "description": "<how one blocked dep cascades into others>"}
  ],
  "dependencies": [
    {
      "id": <int>,
      "risk_level": "Low" | "Medium" | "High" | "Critical",
      "reasoning": "<why this risk level>",
      "recommended_action": "<one specific, role-named TPM action>",
      "escalate": <boolean>
    }
  ],
  "tpm_actions": ["<action 1>", "<action 2>", "<action 3>"],
  "exec_summary": "<2-3 sentence exec-ready summary citing top risk and recommendation>"
}

Risk calibration:
- Blocked + on critical path = Critical. At Risk + on critical path = High.
- Blocked but not blocking others = High. At Risk, not on critical path = Medium.
- On Track = Low unless due date is within 3 days.
Cascading risk: if dep A feeds dep B (same provider/dependent chain), and A is blocked/at-risk, flag B too.
TPM actions must be specific: name the teams, name the ask, give a timeframe."""


def analyze_dependencies(deps: list, api_key: str) -> dict:
    import anthropic
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=_DEP_SYSTEM,
        messages=[{"role": "user", "content": f"Dependencies:\n{json.dumps(deps, indent=2)}"}]
    )
    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


# ── Dependency input form ────────────────────────────────────────────────────
if "dependencies" not in st.session_state:
    st.session_state["dependencies"] = []

with st.form("add_dependency", clear_on_submit=True):
    st.markdown("**Add a Dependency**")
    fc1, fc2 = st.columns(2)
    dep_team = fc1.text_input("Dependent team", placeholder="e.g. Checkout")
    prov_team = fc2.text_input("Provider team", placeholder="e.g. Auth")
    deliverable = st.text_input("Deliverable", placeholder="e.g. SSO token refresh API")
    fd1, fd2 = st.columns(2)
    due_date = fd1.text_input("Due date", placeholder="e.g. 2026-06-20")
    status = fd2.selectbox("Status", ["On Track", "At Risk", "Blocked"])
    add_dep = st.form_submit_button("Add Dependency")

if add_dep:
    if not dep_team.strip() or not prov_team.strip() or not deliverable.strip():
        st.warning("Dependent team, provider team, and deliverable are required.")
    else:
        new_dep = {
            "id": len(st.session_state["dependencies"]) + 1,
            "dependent_team": dep_team.strip(),
            "provider_team": prov_team.strip(),
            "deliverable": deliverable.strip(),
            "due_date": due_date.strip() or "TBD",
            "status": status,
        }
        st.session_state["dependencies"].append(new_dep)
        st.success(f"Added: {dep_team} ← {prov_team}: {deliverable}")

# ── Dependency table ─────────────────────────────────────────────────────────
deps = st.session_state["dependencies"]

if deps:
    status_icon = {"On Track": "🟢", "At Risk": "🟡", "Blocked": "🔴"}
    st.subheader(f"Dependencies ({len(deps)})")

    header_cols = st.columns([1, 2, 2, 3, 2, 2])
    for col, label in zip(header_cols, ["#", "Dependent", "Provider", "Deliverable", "Due", "Status"]):
        col.markdown(f"**{label}**")

    for d in deps:
        row = st.columns([1, 2, 2, 3, 2, 2])
        row[0].write(d["id"])
        row[1].write(d["dependent_team"])
        row[2].write(d["provider_team"])
        row[3].write(d["deliverable"])
        row[4].write(d["due_date"])
        row[5].write(f"{status_icon.get(d['status'], '')} {d['status']}")

    col_clear, col_analyze = st.columns([1, 3])
    if col_clear.button("Clear All"):
        st.session_state["dependencies"] = []
        st.session_state.pop("dep_analysis", None)
        st.rerun()

    if not ANTHROPIC_API_KEY:
        st.warning("Add your Anthropic API key in `.env` to run Claude dependency analysis.")
    elif col_analyze.button("Analyze Dependencies", type="primary"):
        with st.spinner("Claude is reasoning across your dependency graph..."):
            try:
                result = analyze_dependencies(deps, ANTHROPIC_API_KEY)
                st.session_state["dep_analysis"] = result
            except Exception as e:
                st.error(f"Analysis failed: {e}")

# ── Analysis results ─────────────────────────────────────────────────────────
analysis = st.session_state.get("dep_analysis")
if analysis and deps:
    health = analysis.get("health", "Unknown")
    health_color = {"Green": "🟢", "Yellow": "🟡", "Red": "🔴"}.get(health, "⚪")

    st.divider()
    st.subheader("Dependency Analysis")

    h1, h2, h3, h4 = st.columns(4)
    h1.metric("Overall Health", f"{health_color} {health}")
    h2.metric("Critical Path", len(analysis.get("critical_path", [])))
    h3.metric("Cascading Risks", len(analysis.get("cascading_risks", [])))
    escalate_count = sum(1 for d in analysis.get("dependencies", []) if d.get("escalate"))
    h4.metric("Escalations Needed", escalate_count)

    exec_summary = analysis.get("exec_summary", "")
    if exec_summary:
        st.info(f"**Exec Summary:** {exec_summary}")

    cascades = analysis.get("cascading_risks", [])
    if cascades:
        st.markdown("**Cascading Risk Chains:**")
        for c in cascades:
            chain_ids = " → ".join(f"Dep #{i}" for i in c.get("chain", []))
            st.warning(f"⛓️ {chain_ids}: {c.get('description', '')}")

    tpm_actions = analysis.get("tpm_actions", [])
    if tpm_actions:
        st.markdown("**Prioritized TPM Actions:**")
        for i, action in enumerate(tpm_actions, 1):
            st.markdown(f"{i}. {action}")

    st.subheader("Per-Dependency Risk Breakdown")
    risk_icon = {"Low": "🟢", "Medium": "🟡", "High": "🟠", "Critical": "🔴"}
    dep_map = {d["id"]: d for d in deps}

    for item in analysis.get("dependencies", []):
        dep_id = item.get("id")
        original = dep_map.get(dep_id, {})
        risk = item.get("risk_level", "Unknown")
        label = (
            f"{risk_icon.get(risk, '⚪')} Dep #{dep_id} — "
            f"{original.get('dependent_team', '?')} ← {original.get('provider_team', '?')}: "
            f"{original.get('deliverable', '?')}"
        )
        with st.expander(label, expanded=item.get("escalate", False)):
            st.markdown(f"**Risk:** {risk}  |  **Status:** {original.get('status', '?')}  |  **Due:** {original.get('due_date', '?')}")
            st.markdown(f"**Reasoning:** {item.get('reasoning', '—')}")
            if item.get("escalate"):
                st.error(f"🚨 Escalate — {item.get('recommended_action', '')}")
            else:
                st.markdown(f"**Action:** {item.get('recommended_action', '—')}")

elif not deps:
    st.info("Add at least one dependency above to get started.")