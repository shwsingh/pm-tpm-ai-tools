# Knowledge Base Skill (RAG)

## Purpose

Upload TPM documents and search them by question. Returns the most relevant chunks
from uploaded docs so a TPM can quickly find answers without reading every document.

This is the first RAG (Retrieval-Augmented Generation) skill in the AI TPM Copilot.
Today retrieval is keyword-based; Day 9 upgrades to embedding-based similarity search
with Claude generating a synthesized answer from retrieved chunks.

---

## Supported Formats

| Format | Source |
|--------|--------|
| `.txt` | Any plain text export |
| `.md` | Markdown docs, README files |
| `.docx` | Google Docs (File → Download → Word), Word docs |
| `.csv` | Google Sheets (File → Download → CSV), Excel exports |

---

## Input

- One or more uploaded documents (any supported format)
- A free-text question or search query

---

## Output

### Per matched chunk:
- Source document name
- Chunk text (paragraph or row)
- Relevance score (keyword match count today; embedding cosine similarity on Day 9)

### Summary:
- Number of documents searched
- Number of chunks returned
- Top source document

---

## Chunking Strategy

| Format | Chunk unit |
|--------|-----------|
| `.txt` / `.md` | Paragraph (split on blank lines) |
| `.docx` | Paragraph (one per Word paragraph object) |
| `.csv` | Row (one chunk per data row, headers prepended) |

Minimum chunk length: 20 characters. Shorter chunks are discarded.

---

## Retrieval — Today (Heuristic)

1. Tokenize the query into keywords (lowercase, strip punctuation)
2. For each chunk, count how many query keywords appear in the chunk text
3. Score = keyword hit count / total query keywords (0.0 – 1.0)
4. Return top N chunks with score > 0, sorted by score descending

---

## Retrieval — Day 9 Upgrade (Embeddings)

1. Embed all chunks using Claude or a dedicated embedding model at upload time
2. Embed the query at search time
3. Score = cosine similarity between query embedding and each chunk embedding
4. Return top N chunks by cosine similarity
5. Claude generates a synthesized answer citing the top chunks

The chunk storage contract (source, text, score) is stable across both versions.

---

## Evaluation Rules

A retrieval result is **Good** when:
- [ ] Top chunk directly answers the question or contains the key term
- [ ] Source document is correctly attributed
- [ ] No chunk is returned with score = 0 (pure noise)
- [ ] Results are ordered by relevance, not document order

---

## Expected Output Format

```
Found 3 relevant chunks across 2 documents

──────────────────────────────────────
[1] Source: prd_ai_tpm_copilot.md | Score: 0.75
"The agent harness requires a planner, a set of tools, and an output contract..."

[2] Source: launch_checklist.txt | Score: 0.50
"Security review must be completed 5 business days before launch..."

[3] Source: team_roster.csv | Score: 0.25
"Name: Shweta Singh | Role: TPM Lead | Team: Platform"
──────────────────────────────────────
```

---

## Notes

- Day 8: keyword retrieval, no LLM, no persistent storage (session only)
- Day 9: embedding retrieval + Claude answer synthesis
- Day 13: Google Drive MCP integration — docs auto-ingest without manual upload
