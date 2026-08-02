# Claim 5 — Appendix B dependency audit

**Current verdict: VERIFIED on the complete registered source domain.**

The exact tested statement is that the paper's convergence analysis relies on its Appendix B premises, including the unique-stationary-distribution requirement and the two-timescale limit `beta(n)/alpha(n) -> 0`. This is a source-structure claim, so the complete registered TeX domain can be checked exhaustively.

The verifier downloads `https://export.arxiv.org/e-print/2605.31172v1` with an explicit User-Agent and requires SHA-256 `5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd`. It checks all six Appendix B assumption labels, B.3's status as a remark, Theorem 3.3's dependency declaration, and all six dependencies in the TDC proof. Removing the B.2 limit or relabeling B.3 must make verification fail.

Current code: `reproduction/runner.py`. Independent checker: `reproduction/verify.py`. Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`. Environment: repository Python 3.12 `uv.lock`. Compute: Hugging Face `cpu-upgrade`, one estimated required core, selected 8-vCPU allocation, no GPU.

All source predicates and both destructive controls passed on HF `cpu-upgrade`; see [the canonical Claim 5 page](#/current-claim-5). Limitation: this verifies the exact dependency statement, not that every external problem instance satisfies the premises.
