# Claim 5 — Appendix B dependency structure

## Exact claim

The paper's convergence analysis relies on the Appendix B premises, including a unique invariant probability measure for the Markov noise chain and the two-timescale requirement `β(n)/α(n) → 0`. This claim is about the registered paper source, so its complete finite TeX domain can be checked exhaustively.

Source: Appendix B, arXiv:2605.31172v1. Download URL `https://export.arxiv.org/e-print/2605.31172v1`; archive SHA-256 `5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd`; 78,416 bytes; retrieved 2026-08-02 with explicit User-Agent.

## Exhaustive method and raw evidence

The verifier reads `main.tex` from the hash-matched in-memory archive and checks all six labeled assumption environments in source order:

1. stationary distribution;
2. learning ratios;
3. H/G scaling limit structure;
4. Lipschitz and expectation control;
5. stable ODEs and uniform mean scaling limits;
6. weighted LLN.

B.3 is correctly detected as a remark, not an assumption. B.1 contains `unique invariant probability measure`; B.2 contains the exact β/α limit. Theorem 3.3 declares the full assumption range, and the TDC proof references all six labels. The exact assumption-environment count is six.

Two destructive controls failed as intended: removing the B.2 limit was rejected with `B.2 timescale formula missing`; converting B.3 from a remark to an assumption was rejected with `B.3 source type changed`.

Download the complete [source-audit raw JSON](../../raw/claim-5-source.json).

## Code, checker, and reproducibility

[runner.py](../../current/runner.py), independent [verify.py](../../current/verify.py), fixed command `uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py`, Python 3.12 [uv.lock](../../current/uv.lock), evidence Git SHA `7f24f1dce0b64a254d51e483a4b3f581f4610a6a`. No stochastic seed is needed for the exhaustive parser; cumulative regression seeds remain in [metadata](../../raw/run-metadata.json). HF `cpu-upgrade`, job reported no GPU, total cumulative runtime 652.200 s. [Checker output](../../checker/independent-checker.json).

## Limitations and verdict

This verifies what premises the paper states and invokes. It does not claim every external application satisfies those premises; that separate question is audited per constructed experiment.

**Verdict: VERIFIED. Confidence: HIGH. Expected points: 2/2 as a forecast, not a judge result.**
