# Claims 1–4 — proof-dependency reconstruction

**Current verdicts: BLOCKED. The third route completed, but it is not a formal proof certificate.**

This route is deliberately different from the two numerical routes. It hash-pins and parses the complete paper TeX, reconstructs Lemma 3.1 → Theorem 3.2 → Theorem 3.3 → Theorem 7.2, and checks each terminal statement and dependency edge. For TDC, it also hash-pins Yu (2017) and checks the primary source's constrained two-timescale GTDb scope and single-timescale-only unconstrained result.

Three destructive controls remove a terminal bound, a theorem edge, and the primary-source scope statement. All must fail. The exact TDC recursion is checked to contain the eligibility trace and no projection operator.

This is not a formal proof certificate: the source audit cannot kernel-check the analytic arguments, the paper explicitly omits one technical-lemma proof, and two papers do not exhaust the priority literature. If it passes, Claims 1–4 remain LOW-confidence and proceed to the mandatory fourth falsification route.

Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`. Environment: Python 3.12 `uv.lock`. Compute: Hugging Face `cpu-upgrade`, one estimated required core, 8 vCPU/32 GB selected, no GPU.
