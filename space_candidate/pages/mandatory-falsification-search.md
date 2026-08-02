# Claims 1–4 — mandatory falsification route

**Current verdicts: BLOCKED. The fourth route found no valid counterexample.**

This route searches for a counterexample only after three materially different verification attempts left the universal claims LOW-confidence. It restates the exact claims and screens every candidate against the registered assumptions before interpreting its behavior.

For Claims 1–3, twelve unprojected nonnormal Markov SA systems vary shear, mixing, and seed for 150,000 steps. The worst observed tail is promoted by a preregistered selection rule to two new-seed 400,000-step holdouts. Multiple horizons, tail slopes, running-maximum ratios, and first hits of tenfold norm growth are recorded.

For Claim 4, the exact Definition 7.1 TDC update runs at `lambda=0.90` and `0.97` on a 20-state/10-feature off-policy MDP with high importance ratios. F.1/F.2, A invertibility, timescale separation, and absence of projection are checked.

A deliberately unstable ODE must trigger the detector but is rejected for violating B.6. Rank-deficient and projected TDC variants are also rejected. A finite anomaly, overflow, or slow convergence is not a counterexample to an almost-sure asymptotic theorem.

Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`. Environment: Python 3.12 `uv.lock`. Compute: HF `cpu-upgrade`, estimated one core/~15 minutes, selected 8 vCPU/32 GB, no GPU.

The worst search transient grew 31,813.83×, but both 400,000-step holdouts had negative joint-norm and tracking tail slopes. Positive-λ TDC stress cells reduced residuals to .2363–.3676. Finite paths did not contradict the exact almost-sure claims, so Claims 1–4 remain BLOCKED.
