# Day 14 Design Decisions — Executive TPM Copilot

## What we built
The capstone: a unified Executive TPM Copilot interface with live GitHub data, Claude-generated exec briefing, and combined MCP server config for Claude Desktop.

## Decision 1: Commit history as the live data source

**Chose:** Pull last 14 commits via GitHub REST API and feed them into Claude.

**Why:** The repo has no open issues or PRs — but 14 commits, one per day, are the build log. Claude reads them and produces a velocity analysis, milestone summary, and exec briefing. More meaningful than empty issue lists.

**Alternative considered:** Create fake issues to demo GitHub MCP — rejected as inauthentic.

## Decision 2: Single Claude call for Executive Briefing, not agent loop

**Chose:** One `messages.create()` call with commit history as context.

**Why:** The briefing task is pure summarisation — there's no decision about which tool to call, no iteration needed. The agent loop from Day 12 adds overhead (multiple API calls, tool schemas) with no benefit for a read-only synthesis task. Right tool for the right job.

## Decision 3: Auto-resolve GitHub token via `gh auth token`

**Chose:** Try `GITHUB_TOKEN` env var first, then fall back to `gh auth token` CLI.

**Why:** Most developers using this repo will have `gh` authenticated but won't have set a separate `GITHUB_TOKEN`. Auto-resolving via `gh auth token` means zero manual setup for the most common case.

## Decision 4: Combined MCP config block (both servers in one JSON)

**Chose:** Show a single `mcpServers` block with `tpm-copilot` + `github` together.

**Why:** The value of Day 14 is the combination — TPM data and GitHub data in one Claude Desktop conversation. Showing them separately would undersell the integration. One copy-paste connects both.

## Decision 5: Challenge Complete panel as explicit capstone moment

**Chose:** Full-width 14/14 progress bar and metrics at the bottom of the app.

**Why:** The app has grown to 14 sections over 14 days. Without an explicit end marker, the capstone moment is invisible. The panel gives closure and makes the completed scope legible at a glance.
