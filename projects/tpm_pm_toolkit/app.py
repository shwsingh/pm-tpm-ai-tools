import streamlit as st

st.set_page_config(
    page_title="TPM/PM AI Toolkit",
    page_icon="🚀",
    layout="wide"
)

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
        background: white;
        padding: 24px;
        border-radius: 20px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        min-height: 185px;
        transition: 0.2s ease-in-out;
    }

    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 14px 36px rgba(15, 23, 42, 0.12);
    }

    .card h3 {
        margin-top: 0;
        color: #0f172a;
    }

    .card p {
        color: #475569;
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
        color: #0f172a;
        margin-top: 16px;
        margin-bottom: 16px;
    }

    .goal-box {
        background: #ffffff;
        border-left: 6px solid #2563eb;
        padding: 18px 22px;
        border-radius: 16px;
        border-top: 1px solid #e5e7eb;
        border-right: 1px solid #e5e7eb;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🏆 Challenge Progress")
    st.caption("TPM/PM AI Toolkit Build Journey")

    st.progress(0.65)
    st.metric("Overall Progress", "65%", "+15% this week")

    st.divider()

    st.subheader("✅ Completed")
    st.write("• Streamlit setup")
    st.write("• Toolkit structure")
    st.write("• Core feature cards")

    st.subheader("🚧 In Progress")
    st.write("• AI workflows")
    st.write("• Executive dashboard")
    st.write("• Polished UX")

    st.subheader("🎯 Next Milestone")
    st.info("Build the first working AI-powered TPM workflow.")

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
    "and decides whether to escalate to an incident or route to the lead for discussion. "
    "Today the classifier is heuristic; the LLM-backed version ships on Day 9."
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


def triage(bug_text: str) -> dict:
    """Triage a single bug. Heuristic today; LLM-backed on Day 9.

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
        bugs = [b.strip() for b in bug_input.split("\n\n") if b.strip()]
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