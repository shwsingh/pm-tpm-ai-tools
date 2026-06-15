# Common Errors and Fixes
# Common Errors

| Error | Root Cause | Fix |
|---|---|---|
| Import streamlit could not be resolved | Wrong VS Code interpreter | Select venv interpreter |
| app.py not found | Wrong folder | cd into project folder |
| GitHub push rejected | Email privacy | Configure GitHub noreply email |
| Typed code in terminal | Wrong context | Put code inside app.py |
| Streamlit module not found | Wrong environment | Activate venv |
| Pyright: `max(dict, key=dict.get)` overload error | dict.get's signature confuses the type checker when used as a key fn | Use `key=lambda s: d[s]` |
| API key in Streamlit sidebar | Key visible on screen; typed into a UI field that could be logged or screenshotted | Load from `.env` via `python-dotenv`; never put secrets in UI inputs |
| API key in shell command in chat | Key appears in conversation history and shell history | Edit `.env` directly in a text editor (`open -e .env`) outside the chat |
| API key hardcoded in source file | Committed to git and visible to anyone with repo access | Always use env vars; confirm `.env` is in `.gitignore` before adding a key |
| Catching all exceptions in retry loop | Masks real API errors (auth, rate limits); wastes tokens retrying the unretryable | Only catch `json.JSONDecodeError` in retry; let API errors surface immediately |
| Discarding `response.content` after tool_use | Agent loop breaks — Claude needs full tool_use blocks in message history | Append full `response.content` (not just text) to messages before sending tool results |
| Batching multiple bugs in one triage tool call | triage_bug contract expects one bug; batch input produces malformed or merged output | System prompt must say "call triage_bug once per bug report" explicitly |
| Running agent and evaluator in the same prompt | Conflicts between generating output and scoring it; produces self-serving scores | Two separate harness calls: agent first, evaluator second with output as input |
| Creating anthropic client inside retry loop | New HTTP connection per retry; adds latency and connection overhead | Create client once per harness call, reuse across retries |
