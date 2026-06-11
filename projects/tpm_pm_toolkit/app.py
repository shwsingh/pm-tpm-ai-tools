import re
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


def run_triage_stage(valid_bugs: list) -> list:
    """Stage 2 — triage each valid bug using the Day 5 triage() function."""
    results = []
    for bug in valid_bugs:
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
            triage_results = run_triage_stage(ingested["valid_bugs"])

            with st.expander("Stage 2 — Triage", expanded=True):
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

st.divider()

# ── Day 7: Status Report Skill ───────────────────────────────────────────────

st.markdown('<div class="section-title">📋 Day 7: Status Report Skill</div>', unsafe_allow_html=True)

st.write(
    "Fill in your weekly updates below. The skill generates a structured, exec-ready "
    "status report and scores it across five quality dimensions."
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
    """Score a status report across the 5 eval dimensions. Returns scores dict + status color."""
    scores = {}
    notes = {}

    # 1. Completeness
    fields = {"Team/Launch": team, "Shipped": shipped, "Next Week": next_week}
    empty = [k for k, v in fields.items() if not v.strip()]
    scores["Completeness"] = len(empty) == 0
    notes["Completeness"] = f"Missing: {', '.join(empty)}" if empty else "All required fields filled"

    # 2. Ask Specificity
    if not asks.strip() or asks.strip().lower() in ("none", "n/a", "no asks"):
        scores["Ask Specificity"] = True
        notes["Ask Specificity"] = "No asks this week"
    else:
        vague = [w for w in VAGUE_ASK_WORDS if w in asks.lower()]
        scores["Ask Specificity"] = len(vague) == 0
        notes["Ask Specificity"] = f"Vague language detected: {', '.join(vague)}" if vague else "Asks appear specific"

    # 3. Status Accuracy (evaluated after color is determined below)
    blocker_lower = blockers.lower()
    risk_lower = risks.lower()
    has_blocker = any(k in blocker_lower for k in BLOCKER_RED_KEYWORDS) and blockers.strip().lower() not in ("none", "n/a", "no blockers")
    has_risk = any(k in risk_lower for k in RISK_YELLOW_KEYWORDS) and risks.strip().lower() not in ("none", "n/a", "no risks")

    if has_blocker:
        status = "Red"
    elif has_risk:
        status = "Yellow"
    else:
        status = "Green"

    scores["Status Accuracy"] = True  # always accurate since we derive it from content
    notes["Status Accuracy"] = f"Status derived from content — {status} is consistent"

    # 4. Clarity — flag unexplained all-caps acronyms (3+ chars)
    import re as _re
    all_text = " ".join([shipped, blockers, risks, asks, next_week])
    acronyms = _re.findall(r'\b[A-Z]{3,}\b', all_text)
    known = {"TPM", "PM", "PRD", "API", "SDK", "MCP", "RAG", "NLP", "ETL", "SLA",
             "PII", "P0", "P1", "P2", "P3", "UI", "UX", "QA", "MVP", "OKR", "KPI",
             "ETA", "EOD", "EOW", "LGTM", "WIP", "TBD", "TBD", "VP", "IC", "iOS"}
    unexplained = list(set(a for a in acronyms if a not in known))
    scores["Clarity"] = len(unexplained) == 0
    notes["Clarity"] = f"Unexplained acronyms: {', '.join(unexplained)}" if unexplained else "No unexplained acronyms detected"

    # 5. Next Week Concreteness
    weak = [w for w in WEAK_NEXT_WEEK_WORDS if w in next_week.lower()]
    scores["Next Week Concreteness"] = len(weak) == 0
    notes["Next Week Concreteness"] = f"Weak language: {', '.join(weak)}" if weak else "Next week items appear concrete"

    return scores, notes, status


def build_report(team, shipped, blockers, risks, asks, next_week, status, week_of):
    """Assemble the formatted exec report string."""
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


with st.form("status_report_form"):
    sr_team = st.text_input("Team / Launch Name", placeholder="e.g. Checkout v2 Launch")
    sr_week = st.text_input("Week of", placeholder="e.g. June 9–13, 2026")
    sr_shipped = st.text_area("What shipped this week", height=100,
        placeholder="e.g. Completed auth integration\nFixed P1 checkout bug on iOS")
    sr_blockers = st.text_area("Blockers", height=80,
        placeholder="e.g. Security review on hold — waiting for approval from InfoSec team\nOr: None")
    sr_risks = st.text_area("Risks", height=80,
        placeholder="e.g. Third-party API dependency may delay launch by 1 week\nOr: None")
    sr_asks = st.text_area("Asks from leadership", height=80,
        placeholder="e.g. Approve launch exception for known P2 bug by June 13\nOr: None")
    sr_next = st.text_area("Next week plan", height=100,
        placeholder="e.g. Ship staging build to QA by Wednesday\nComplete load testing and sign off by Friday")
    submitted = st.form_submit_button("Generate Status Report")

if submitted:
    if not sr_team.strip() or not sr_shipped.strip() or not sr_next.strip():
        st.warning("Team name, shipped work, and next week plan are required.")
    else:
        scores, notes, status = score_report(sr_team, sr_shipped, sr_blockers, sr_risks, sr_asks, sr_next)
        week_label = sr_week.strip() if sr_week.strip() else "Week not specified"
        report = build_report(sr_team, sr_shipped, sr_blockers, sr_risks, sr_asks, sr_next, status, week_label)

        # Status banner
        if status == "Red":
            st.error("🔴 Red — Active blockers detected. Leadership action needed.")
        elif status == "Yellow":
            st.warning("🟡 Yellow — Risks present. Monitor closely.")
        else:
            st.success("🟢 Green — On track. No blockers or risks.")

        # Eval scores
        st.subheader("Quality Eval")
        all_pass = all(scores.values())
        ec1, ec2, ec3, ec4, ec5 = st.columns(5)
        for col, (dim, passed) in zip([ec1, ec2, ec3, ec4, ec5], scores.items()):
            col.metric(dim, "✅ Pass" if passed else "❌ Fail")

        if all_pass:
            st.success("✅ Exec-Ready — all five quality dimensions pass.")
        else:
            failed = [f"**{d}**: {notes[d]}" for d, p in scores.items() if not p]
            st.warning("⚠️ Not Exec-Ready — fix before sending:\n\n" + "\n\n".join(failed))

        # Report
        st.subheader("Generated Report")
        st.code(report, language=None)