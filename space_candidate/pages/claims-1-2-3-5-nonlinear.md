# Claims 1, 2, 3, and 5 — nonlinear SA route

**Current theorem verdicts: BLOCKED while the nonlinear child run is pending.** The page tests the exact no-projection stability, fast tracking, joint convergence, running-maximum, and Appendix B premises. It does not convert finite paths into almost-sure proof.

The committed route uses a nonlinear equilibrium map, dimensions 8/32/64, 17-state Markov noise at three mixing rates, initial scales 1 and 12, and no projection or clipping. It pairs 18 finite paths with analytic certificates for the constructed family's fast/reduced ODEs, infinity scaling limits, and running-maximum bound.

Current code: `reproduction/runner.py`. Independent checker: `reproduction/verify.py`. Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`. Environment: repository Python 3.12 `uv.lock`. Compute: Hugging Face `cpu-upgrade`, estimated one required core, no GPU.

Four destructive controls must be rejected: reducible Markov noise (B.1), equal timescales (B.2), unstable fast ODE (B.6), and projection-enabled execution (algorithm mismatch). Raw paths, CPU allocation, runtime, checker output, Git SHA, and final limitations will be placed inline only after the run answers the predeclared contract.
