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
