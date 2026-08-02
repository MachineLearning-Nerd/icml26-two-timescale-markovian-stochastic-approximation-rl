# Claims 1, 2, 3, and 5 — nonlinear SA route

**Current theorem verdicts: BLOCKED after four routes.** The route completed successfully and tests the exact no-projection stability, fast tracking, joint convergence, running-maximum, and Appendix B premises. It does not convert finite paths into almost-sure proof.

The committed route uses a nonlinear equilibrium map, dimensions 8/32/64, 17-state Markov noise at three mixing rates, initial scales 1 and 12, and no projection or clipping. It pairs 18 finite paths with analytic certificates for the constructed family's fast/reduced ODEs, infinity scaling limits, and running-maximum bound.

Current code: `reproduction/runner.py`. Independent checker: `reproduction/verify.py`. Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`. Environment: repository Python 3.12 `uv.lock`. Compute: Hugging Face `cpu-upgrade`, estimated one required core, no GPU.

All 18 cells and four destructive controls passed. Maximum empirical K was 1.4465, minimum certificate slack 1.8755, worst tracking ratio .004636, and worst joint ratio .004754. See the canonical [Claim 1](#/current-claim-1), [Claim 2](#/current-claim-2), and [Claim 3](#/current-claim-3) pages.
