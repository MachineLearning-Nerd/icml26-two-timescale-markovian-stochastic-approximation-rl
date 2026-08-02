# Method

The HF runner downloads and hash-pins the paper and Yu (2017) TeX archives. It slices proof regions by exact section anchors, then checks terminal equations and dependency edges independently of the experimental modules. It also checks Yu's own scope statements rather than trusting the new paper's priority narrative.

Negative controls remove the Lemma 3.1 terminal bound, the Theorem 7.2 → Theorem 3.3 edge, and Yu's unconstrained-scope statement. Each mutation must make its associated predicate false.

Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`

Environment: repository Python 3.12 `uv.lock`. Compute: Hugging Face `cpu-upgrade`, no GPU. Estimated scientific need: one core; selected allocation: 8 vCPU/32 GB.
