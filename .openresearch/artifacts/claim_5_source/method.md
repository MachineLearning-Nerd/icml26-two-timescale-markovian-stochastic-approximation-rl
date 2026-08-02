# Method

The cumulative fixed runner downloads the registered arXiv source archive on Hugging Face with the explicit User-Agent `OpenResearch-Reproduction/1.0 (source verifier)`. It rejects any archive whose SHA-256 differs from the preregistered digest, reads `main.tex` directly from the in-memory archive, and parses the six exact Appendix B labels.

The independent checker requires every declared source predicate and an exact assumption-environment count of six. Two negative controls mutate the source in memory: one removes the B.2 ratio limit and one changes the B.3 remark into an assumption. Each must be rejected.

Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`

Environment: Python 3.12 under the repository `uv.lock`. Compute: Hugging Face `cpu-upgrade`, no GPU. Estimated requirement: one CPU core; selected allocation: 8 vCPU, 32 GB RAM.
