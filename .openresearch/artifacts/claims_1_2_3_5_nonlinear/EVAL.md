# Evaluation map

- Exact contracts: `claim_contract.json`
- Source/anchors: `source_audit.md`
- Method and controls: `method.md`
- Executable generator: `reproduction/runner.py`
- Independent fail-closed checker: `reproduction/verify.py`
- Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`
- Environment: Python 3.12, locked by repository `uv.lock`
- Current raw output: `raw_results.json`, extracted from the accepted terminal log payload
- Independent checker output: `independent_checker_output.json`; executable copy: `claim_verifier.py`
- Negative-control output: `negative_controls` in `raw_results.json`
- CPU/runtime/Git SHA/seeds: `runtime_cpu.json` and raw cells
- Verdict limitation: constructed-family certificates do not prove universal almost-sure theorems

Final verdicts: Claims 1–3 are **BLOCKED, LOW confidence** after four routes. Claim 5's source-domain dependency endpoint is **VERIFIED, HIGH confidence** in its dedicated artifact. The nonlinear results are faithful scoped corroboration, never a universal proof.
