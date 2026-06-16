#!/usr/bin/env python3
"""Use Claude Opus to redesign the build timeline as polished HTML."""

import anthropic
import sys

client = anthropic.Anthropic()

TIMELINE_DATA = """
The AI TPM Copilot is a 14-day vibe-coding challenge by Shweta Singh (Senior Manager, TPM at Google).
Each day adds one capability toward a multi-agent AI TPM Copilot.

GitHub: https://github.com/shwsingh/pm-tpm-ai-tools
Blog: https://shwsingh.github.io/pm-tpm-ai-tools/
Component Reference: https://shwsingh.github.io/pm-tpm-ai-tools/components.html

PHASES:

--- Phase 1: Foundation (Days 0–4, color: #3b82f6 blue) ---

Day 0 — Repo + 14-Day Plan [tag: Setup]
Desc: Repository setup, 14-day curriculum, project structure and commit conventions defined.

Day 1 — TPM Dashboard Homepage [tag: UI]
Desc: Streamlit app with module cards for every planned capability — a living homepage that grows with the project.

Day 2 — Launch Risk Analyzer [tag: Heuristic]
Desc: Keyword-based risk scoring across High / Medium / Low tiers. No LLM — fast, explainable, zero API cost.
Insight: First working TPM tool. Proved the output contract before adding AI.

Day 3 — First Skill Spec [tag: Skill]
Desc: Wrote launch_risk_analysis.md — the first prompt-style behavior contract with input, output schema, and eval rules.
Insight: Skills are specs, not code. Consumed by agents in later days.

Day 4 — PRD Builder Skill [tag: Skill]
Desc: Skill spec for exec-ready PRDs including agent-critical sections. Worked example with a senior-PM critique loop.

--- Phase 2: Skills & Agents (Days 5–8, color: #f59e0b amber) ---

Day 5 — Bug Triage Agent + Blog Launch [tag: Agent]
Desc: First agent — heuristic classifier with stable output contract (severity, owner, escalate). Route-to-Lead safety net. GitHub Pages blog launched.
Bullets:
- Output contract designed before any LLM — paid off through Day 12
- Route-to-Lead: confidence boundary as a first-class output
- Week 1 blog post published

Day 6 — Agent Workflow — 3-Stage Pipeline [tag: Orchestration]
Desc: Ingest → Triage → Escalation Handler. Pure functions, stage outputs feed next stage via session state. Draft incident summaries and on-call messages.
Insight: Code orchestrates Claude — the deliberate contrast to Day 12's agent loop.

Day 7 — Status Report Skill [tag: Skill]
Desc: Structured form → exec report → 5-dimension quality eval. Status color derived from content, not self-reported. Catches optimism bias.
Bullets:
- Rubric: Ask Specificity, Status Accuracy, Impact Clarity, Next Week Concreteness, Exec Readability
- Each criterion: wrong example + right example

Day 8 — Knowledge Base [tag: RAG Foundation]
Desc: Upload .txt, .md, .docx, .csv. Chunked and keyword-searched. No vector DB needed — chunking strategy matters more than the scorer at this scale.

--- Phase 3: LLM & Orchestration (Days 9–12, color: #22c55e green) ---

Day 9 — Feedback Agent + First Claude Calls [tag: LLM]
Desc: Heuristic triage swapped for Claude — one function change, zero pipeline changes. Feedback Agent: per-item sentiment, themes, severity, action + aggregate TPM next steps.
Insight: The Day 5 contract meant the LLM swap touched nothing downstream.

Day 10 — Dependency Agent [tag: LLM]
Desc: Structured form for cross-team dependencies. Claude reasons over the full graph — critical path, cascading risks, TPM actions. One call, not one per dependency.
Insight: Cascade detection requires seeing the full graph at once.

Day 11 — AgentHarness + Evaluation Framework [tag: Infrastructure]
Desc: All Claude calls unified through a single AgentHarness. Claude-as-judge scores any output against skill spec rules — criterion by criterion, pass/fail with reason.
Bullets:
- Retry on JSON parse failure only — API errors surface immediately
- Two-call eval pattern: agent produces, evaluator scores
- Token dashboard: cumulative cost visible across the session

Day 12 — Multi-Agent Orchestrator [tag: Multi-Agent]
Desc: Free-text TPM request → agent loop → Claude picks tools → executes → synthesizes exec briefing. Every tool call visible: input, result, token count.
Bullets:
- 4 tools: triage_bug, analyze_feedback, analyze_dependencies, search_knowledge_base
- Max 5 iterations. Tool errors continue the loop, don't crash it
Insight: First surface where Claude orchestrates itself — not the code.

--- Shipped alongside: Infrastructure & Docs (color: #a855f7 purple) ---

Infra — Git Hook + CLAUDE.md Enforcement [tag: Automation]
Desc: post-commit hook fires on every Day N commit. Checks 4 tracking files were updated. Warns with fix command if missing — catches documentation drift at commit time.

Docs — Blog + Component Reference + Timeline [tag: Publishing]
Desc: GitHub Pages blog with Week 1 and Week 2 posts. Component reference — tabbed card view with role, impact, source links, hover tooltips. This timeline page.

--- Coming Soon: Days 13–14 ---

Day 13 — MCP Server Integration [tag: MCP]
Desc: Real MCP server exposing TPM resources, tools, and prompts. Wired to Claude Desktop. Live data replaces structured forms.

Day 14 — Executive TPM Copilot [tag: Full Demo]
Desc: One interface. All agents. Harness + loops + MCP + multi-agent in a single end-to-end executive workflow.

Progress: 12 of 14 days complete (85.7%)
"""

DESIGN_PROMPT = f"""You are a senior UX designer and frontend engineer. Design a stunning, professional, publication-quality HTML page for a 14-day AI project build timeline.

CONTENT DATA:
{TIMELINE_DATA}

DESIGN REQUIREMENTS — apply ALL of these:

1. VISUAL LANGUAGE: Use a dark theme (#09090b background). Think Linear.app, Vercel dashboard, or a high-end developer blog. Clean, editorial, minimal but impactful.

2. LAYOUT CONCEPT — "Editorial Chapter Timeline":
   - Full-width PHASE CHAPTER HEADERS (spanning the viewport) with a subtle colored left border stripe and the phase name, date range, and a one-line theme. These are section dividers, not just labels.
   - Each day entry uses a 3-column layout: [large day number (120px, bold, phase-colored, 60-80px font)] | [subtle vertical divider line] | [content area]
   - NO card boxes — entries are open rows with generous padding and bottom border separators. More like Linear's changelog than a kanban board.
   - Phase color bleeds as a subtle left border on each entry row within that phase.
   - For "Infrastructure & Docs" entries: show them as a condensed horizontal strip after Phase 3, not part of the day numbering.

3. TYPOGRAPHY:
   - Day number: 64px, font-weight 900, phase color, line-height 1, opacity 0.9
   - Title: 18px, font-weight 700, white
   - Tag pill: tiny, 10px uppercase letter-spacing, rounded, phase-tinted background and color
   - Description: 14px, color #a1a1aa (zinc-400), line-height 1.7
   - Bullets: 13px, #71717a (zinc-500), with a phase-colored dot prefix
   - Insight line: 13px italic, phase color, with a left colored border, indented — like a pull quote

4. PROGRESS SECTION at top:
   - Big number: "12/14" in huge type (say 80px), white
   - Subtitle: "days complete"
   - Inline progress bar: thin (4px), full width, gradient from phase 1 color to phase 3 color, rounded
   - Row of 14 numbered circles (01–14), filled/colored for completed, outlined for coming soon — this replaces the text badges

5. PHASE CHAPTER HEADERS:
   - Full viewport width (negative margin or width: 100vw), 1px tall colored left stripe
   - Phase number in large muted text (like "01" "02" "03")
   - Phase name in bold white
   - Date range in muted text
   - One-line theme description in muted text
   - Background: subtle gradient from the phase color at 6% opacity to transparent

6. COMING SOON section:
   - Visual treatment: entries are dimmed (opacity: 0.35), day numbers show as just outlines, dashed left border, a small "COMING SOON" badge
   - A small estimated completion note like "Est. completion: Week 3"

7. NAV BAR: sticky, dark, with links to Blog, Component Reference, GitHub. Logo/brand on left.

8. HOVER STATES:
   - Each entry row: left border brightens to full phase color (0.15s ease), background gets a very subtle phase-tinted wash
   - Day number slightly scales up (scale: 1.05, 0.1s ease)

9. NO card boxes. NO shadows on cards. Entries are rows, not cards.

10. FOOTER: Simple, centered, small text. Links to blog and github.

Generate a complete, self-contained HTML file. No external dependencies except Google Fonts (use Inter). All CSS must be inline in a <style> tag. The JavaScript (if any) is minimal.

The file should be polished enough to publish directly as a portfolio piece. Every pixel matters. Think of the best-designed developer changelog or build log you've ever seen.

Output ONLY the complete HTML. No explanation, no markdown fences.
"""

print("Calling Claude Opus 4.7 to design the timeline...", file=sys.stderr)

with client.messages.stream(
    model="claude-opus-4-7",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[{"role": "user", "content": DESIGN_PROMPT}],
) as stream:
    html = stream.get_final_message()

# Extract the text content
result = ""
for block in html.content:
    if block.type == "text":
        result += block.text

# Strip markdown fences if present
if result.strip().startswith("```"):
    lines = result.strip().split("\n")
    # Remove first and last fence lines
    if lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    result = "\n".join(lines)

output_path = "/Users/shwetasingh/Documents/pm-tpm-ai-tools/docs/timeline_preview.html"
with open(output_path, "w") as f:
    f.write(result)

print(f"Written to {output_path}", file=sys.stderr)
print(f"Usage: input={html.usage.input_tokens} output={html.usage.output_tokens}", file=sys.stderr)
