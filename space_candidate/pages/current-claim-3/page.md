# Claim 3 — Lemma 3.1 running-maximum control

## Exact claim

Under the Appendix B premises, there exists a sample-path-dependent finite constant `K` such that `||x_n|| ≤ K(1+||y_n^max||)` for every n, almost surely. One finite empirical maximum is not the universal lemma.

Source: arXiv:2605.31172v1, Lemma 3.1, HTML anchor `#S3.Thmtheorem1`, registered source SHA-256 `5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd`.

## Assumptions, certificate, and controls

For the nonlinear family, a contractive fast recursion yields a conservative analytic K from matrix and noise bounds. Every cell checks this K against all recorded iterates. The source route checks the exact terminal `K=C1 C2 C3` sentence; removing it causes the source verifier to fail. The adversarial route independently tracks the running ratio under nonnormal dynamics.

## Raw observed evidence

- Nonlinear family: maximum empirical K 1.4465; minimum analytic-certificate slack 1.8755.
- Adversarial search: maximum empirical running ratio 79.567 across severe transients; no finite-path violation of its recorded maximum.
- Promoted holdouts: empirical K 28.839 and 14.493 through 400k steps.
- Removing the Lemma 3.1 terminal bound was rejected with reason `Lemma 3.1 terminal bound missing`.

Download [nonlinear certificates and paths](../../raw/claims-1-2-3-nonlinear.json), [proof controls](../../raw/proof-route.json), and [adversarial paths](../../raw/falsification-route.json).

## Code, checker, and reproducibility

[runner.py](../../current/runner.py), independent [verify.py](../../current/verify.py), fixed command `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`, Python 3.12 [uv.lock](../../current/uv.lock), Git SHA `7f24f1dce0b64a254d51e483a4b3f581f4610a6a`. Seeds 4101–4102, 7001–7002, 8101–8102. HF `cpu-upgrade`, 652.200 s cumulative runtime, zero GPU devices. [Checker output](../../checker/independent-checker.json).

## Limitations and verdict

The analytic K certifies the constructed family only. A measured running maximum is tautologically finite at finite horizon and cannot establish one finite K for all n on almost every path.

**Verdict: BLOCKED. Confidence: LOW.**
