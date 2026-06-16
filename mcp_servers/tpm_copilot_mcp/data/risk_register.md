# Risk Register — AI TPM Copilot v1.0

**Last Updated:** 2026-06-16  
**Owner:** Shweta Singh

## Active Risks

| ID | Risk | Likelihood | Impact | Severity | Owner | Mitigation |
|----|------|-----------|--------|----------|-------|-----------|
| R-01 | Claude API rate limits under concurrent load | Medium | High | HIGH | Engineering | Add exponential backoff in AgentHarness; cache repeated calls |
| R-02 | MCP server not stable for Claude Desktop demo | Low | High | HIGH | Shweta | Test with Claude Desktop beta before Day 14 demo |
| R-03 | Multi-agent loop exceeds token budget on complex requests | Medium | Medium | MEDIUM | Engineering | Cap at 5 iterations; add token warning threshold at 80% |
| R-04 | Knowledge Base chunking misses context across chunk boundaries | Medium | Medium | MEDIUM | Engineering | Overlap chunks by 20%; add retrieval confidence score |
| R-05 | Eval scores inconsistent across Claude model versions | Low | Medium | LOW | Engineering | Pin model version in AgentHarness; log model used per eval |
| R-06 | Demo environment missing ANTHROPIC_API_KEY | Low | High | MEDIUM | Shweta | Add env check on app startup; surface clear error message |

## Resolved Risks

| ID | Risk | Resolution |
|----|------|-----------|
| R-07 | Output contract breaks when swapping heuristic for LLM | Resolved Day 9 — contract defined Day 5, LLM swap was one function change |
| R-08 | Agent loop crashes on tool error | Resolved Day 12 — errors continue loop, don't abort |

## Risk Trend
- Week 1: 2 high risks (API costs, no eval framework) → both resolved
- Week 2: Focus shifted to integration risks (MCP, multi-agent stability)
- Current: 2 HIGH, 2 MEDIUM, 1 LOW active
