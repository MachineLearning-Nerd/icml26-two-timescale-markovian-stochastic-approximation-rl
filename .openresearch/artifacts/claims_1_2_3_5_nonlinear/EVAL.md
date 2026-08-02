# Evaluation map

- Exact contracts: `claim_contract.json`
- Source/anchors: `source_audit.md`
- Method and controls: `method.md`
- Executable generator: `reproduction/runner.py`
- Independent fail-closed checker: `reproduction/verify.py`
- Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`
- Environment: Python 3.12, locked by repository `uv.lock`
- Current raw output: accepted only after extraction from the terminal `orx logs` payload
- Verdict limitation: constructed-family certificates do not prove universal almost-sure theorems
