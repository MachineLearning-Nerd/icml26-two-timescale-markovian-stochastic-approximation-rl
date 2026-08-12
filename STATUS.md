# Reproduction status

## Paper identity

- OpenReview ID: Iww9TICvKj
- Accepted title: Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning
- Authors: Vagul Mahadevan; Claire Chen; Shuze Daniel Liu; Shangtong Zhang
- arXiv: 2605.31172v1
- Venue: ICML 2026

## Claim status

| Claim | Status | Meaning |
| --- | --- | --- |
| 1 | BLOCKED | Finite nonlinear and adversarial paths do not prove universal almost-sure boundedness. |
| 2 | BLOCKED | Finite tracking and joint-error reductions do not prove an infinite-horizon almost-sure limit. |
| 3 | BLOCKED | Family-specific K certificates do not establish the universal pathwise lemma. |
| 4 | BLOCKED | Positive-lambda TDC evidence is finite and the priority audit is not exhaustive. |
| 5 | VERIFIED_SOURCE_DOMAIN_ONLY | The exact registered source contains the required Appendix B dependency structure; this is not theorem validation. |

## Provenance

- Former repository: icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic
- Target repository: icml26-two-timescale-markovian-stochastic-approximation-rl
- Canonical branch: main
- Registered source SHA-256: 5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd
- Yu (2017) source SHA-256: fa48127d46d01abfc81bf2e737815f9afed5cdae63f5de37993d722c7c002acd
- Evidence-generating commit: 7f24f1dce0b64a254d51e483a4b3f581f4610a6a
- Published Hugging Face Space: DineshAI/Iww9TICvKj
- Published revision: bec3336591285a901d33d2abba824f6e2bc31d8c
- Historical judged head: ba24d26d274d66c8cdb627aa5a324b47d189dfe0
- Historical live score: 5/10

## Execution

- Current phase: documentation_and_branch_normalization
- Next action: normalize GitHub repository and verify remote state
- Compute: Hugging Face cpu-upgrade; 8 vCPU/32 GB advertised; no GPU
- Fixed command: uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py
- Publication status: immutable artifact and manifest already published; repository documentation cleanup in progress

## Interpretation

The repository records implementation-faithful finite evidence and source-domain checks. It does not claim to prove Claims 1–4. The previous score is a judge result for the historical release; any projected score is explicitly a forecast.
