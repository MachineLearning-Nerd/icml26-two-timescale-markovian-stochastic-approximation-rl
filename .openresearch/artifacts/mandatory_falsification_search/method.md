# Method

The SA search constructs six-dimensional linear systems with increasingly nonnormal Hurwitz fast and reduced-slow matrices, bounded zero-mean noise from an 11-state positive Markov kernel, two-timescale Robbins–Monro rates, exact scaling limits, and no projection. Twelve cells use three shear levels, two mixing rates, and two seeds at 150,000 steps. The largest tail norm slope, with maximum growth as tie-breaker, selects a parameter pair before two new-seed 400,000-step holdouts.

The TDC search uses the exact Definition 7.1 update on a 20-state, 10-feature off-policy MDP, positive `lambda` values 0.90 and 0.97, and behavior/target policies chosen to produce substantially larger importance ratios. Every finite MDP, feature-rank, invertibility, learning-rate, and no-projection premise is checked independently.

The detector must recognize a deliberately unstable fast ODE, while rejecting it because B.6 is violated. Rank-deficient and projected TDC controls must also be rejected.

Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`. Environment: Python 3.12 `uv.lock`. Compute: Hugging Face `cpu-upgrade`, no GPU. Estimated demand: one core for about 15 minutes; selected allocation: 8 vCPU/32 GB.
