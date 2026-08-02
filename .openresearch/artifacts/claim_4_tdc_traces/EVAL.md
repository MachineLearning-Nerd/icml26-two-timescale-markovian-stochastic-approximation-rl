# Evaluator checklist

- Exact claim and quantifiers: `claim_contract.json`
- Source statement and assumptions: `source_audit.md`
- Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`
- Locked environment: Python 3.12, `pyproject.toml`, `uv.lock`
- Executable algorithm: `reproduction/runner.py`
- Independent fail-closed checker: `reproduction/verify.py`
- Historical raw output: `historical_rejected_raw.json`
- Current raw output: `raw_results.json`, extracted from terminal run `df3c8eb3-22f3-478d-82ad-bf41b4335454`
- Independent checker output: `independent_checker_output.json`; executable copy: `claim_verifier.py`
- Negative-control output: `negative_controls` in `raw_results.json`
- CPU/runtime/Git SHA/seeds: `runtime_cpu.json` and the raw cells
- Scope: finite evidence is not presented as proof of the almost-sure theorem

Final verdict: **BLOCKED, LOW confidence.** Exact positive-λ evidence directly fixes the λ=0 proxy, but finite paths and a two-source priority audit do not prove the theorem's almost-sure and global-priority quantifiers.
