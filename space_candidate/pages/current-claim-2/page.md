# Claim 2 — Theorem 3.3 convergence

## Exact claim

Under Appendix B, `||x_n − λ(y_n)|| → 0` almost surely and the joint iterate converges to `(λ(y*), y*)`. The quantifier is an infinite-horizon almost-sure limit for the general recursion.

Source: arXiv:2605.31172v1, Theorem 3.3, HTML anchor `#S3.Thmtheorem3`, source SHA-256 `5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd`.

## Assumptions and four routes

The nonlinear constructed family has a globally Lipschitz, positively homogeneous absolute-value term, exact scaling factorization, fast equilibrium map, stable reduced ODE, positive finite-state Markov kernels, and separated learning rates. Routes comprise the historical linear check, the nonlinear scaling grid, proof-dependency reconstruction, and mandatory nonnormal falsification search.

## Raw observed evidence

- Across the 18 nonlinear cells, the worst final/initial tracking ratio was .004636 and the worst joint ratio was .004754.
- At dimension 64 and stickiness .96, final tracking errors were .010890 and .012608; joint errors were .011933 and .013589.
- The two promoted adversarial holdouts had tracking tail slopes −.8824 and −.8817. Their absolute final tracking errors remained 83.63 and 153.09 after large nonnormal transients.
- Equal-timescale and unstable-ODE mutations were rejected for violating B.2 and B.6.

Download [nonlinear raw JSON](../../raw/claims-1-2-3-nonlinear.json), [falsification raw JSON](../../raw/falsification-route.json), and [proof-route JSON](../../raw/proof-route.json).

## Code, checker, and reproducibility

[runner.py](../../current/runner.py) implements the recursion and horizon measurements; [verify.py](../../current/verify.py) independently enforces assumptions, grids, controls, and non-inflated verdicts. Fixed command: `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`; Python 3.12 [uv.lock](../../current/uv.lock). Git SHA `7f24f1dce0b64a254d51e483a4b3f581f4610a6a`; seeds 4101–4102, 7001–7002, 8101–8102; HF `cpu-upgrade`; 652.200 s cumulative runtime; no GPU. [Checker output](../../checker/independent-checker.json).

## Limitations and verdict

Multiple horizons and holdout slopes avoid choosing a horizon from the theorem's conclusion, but they cannot establish an infinite-horizon almost-sure limit. The proof source contains one explicitly omitted technical argument and no formal certificate.

**Verdict: BLOCKED. Confidence: LOW.**
