# ICML 2026 — Convergence of Two-Timescale Markovian Stochastic Approximations

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-two-timescale-markovian-stochastic-approximation-rl/blob/main/notebooks/two_timescale_reproduction.py)

This repository is a claim-by-claim reproduction and audit record for [Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning](https://arxiv.org/abs/2605.31172).

The honest campaign outcome is:

- Claims 1–4 are BLOCKED: finite experiments, source parsing, and priority checks do not establish universal almost-sure theorems or an exhaustive priority claim.
- Claim 5 is VERIFIED_SOURCE_DOMAIN_ONLY: the exact registered paper source contains the required Appendix B dependency structure. This is not a proof of the theorems.
- The previous live judged score was 5/10. The 5–6/10 range below is a forecast, not a new judge result.

The old judged logbook used a d=3 linear stochastic-approximation example and lambda=0 TDC. That material remains preserved and labeled as a historical rejected baseline. The current campaign adds nonlinear scaling, positive-lambda eligibility traces, proof-dependency reconstruction, and a mandatory falsification search.

## Paper and artifact record

| Field | Record |
| --- | --- |
| Accepted paper | Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning |
| Authors | Vagul Mahadevan, Claire Chen, Shuze Daniel Liu, and Shangtong Zhang |
| Venue | International Conference on Machine Learning (ICML 2026) |
| arXiv | [2605.31172v1](https://arxiv.org/abs/2605.31172) |
| OpenReview | [Iww9TICvKj](https://openreview.net/forum?id=Iww9TICvKj) |
| Final repository | MachineLearning-Nerd/icml26-two-timescale-markovian-stochastic-approximation-rl |
| Former repository | icml26-repro-Iww9TICvKj-convergence-of-two-timescale-markovian-stochastic-approximations-with-applic |
| Canonical branch | main |
| Published artifact | [DineshAI/Iww9TICvKj](https://huggingface.co/spaces/DineshAI/Iww9TICvKj/tree/bec3336591285a901d33d2abba824f6e2bc31d8c) |
| Published revision | bec3336591285a901d33d2abba824f6e2bc31d8c |
| Historical judged head | ba24d26d274d66c8cdb627aa5a324b47d189dfe0 |
| Registered source | arXiv e-print, 78,416 bytes |
| Registered source SHA-256 | 5cdcc002ca92551c2ab4e0753e8a454ed18e04e9162e9a08257ed88bbee8e3fd |
| Yu (2017) audit source SHA-256 | fa48127d46d01abfc81bf2e737815f9afed5cdae63f5de37993d722c7c002acd |
| Compute | Hugging Face cpu-upgrade; 8 vCPU/32 GB advertised; no GPU |
| Evidence-generating command | uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py |

## What the paper is doing

The paper studies coupled fast and slow stochastic-approximation recursions under Markovian noise. It removes common projection and compact-noise shortcuts and controls the fast iterate using a sample-path bound tied to the running maximum of the slow iterate. The theory is applied to off-policy TDC with genuine eligibility traces, including positive trace parameter lambda.

The important distinction for this repository is between:

- a finite experiment that follows the paper's recurrence and assumptions;
- a source audit that checks what the registered paper actually states;
- a mathematical proof of a universal almost-sure theorem.

Only the first two are implemented here. The third remains open for Claims 1–4.

## Claim ledger

| Claim | Paper statement | How the result is produced | Evidence | Status |
| --- | --- | --- | --- | --- |
| 1 | Theorem 3.2: under Appendix B assumptions, the unprojected two-timescale iterates are bounded almost surely. | The runner constructs nonlinear fast/slow systems, checks encoded assumptions and negative controls, and records path maxima. The falsification route then searches nonnormal systems and promotes the worst calibration regime to fresh long holdouts. | 18 nonlinear cells; 12 adversarial cells; two 400,000-step holdouts; calibration growth reached 31,813.83 times the initial norm before declining. | BLOCKED — finite paths do not prove a universal almost-sure bound. |
| 2 | Theorem 3.3: fast tracking and joint convergence occur almost surely. | The same nonlinear runner records tracking and joint errors at multiple horizons. Holdouts record tail slopes and tracking slopes under the selected stress regime. | Nonlinear joint reduction stayed below 0.00476 in the scaled grid; holdout tracking slopes were about -0.882. | BLOCKED — finite convergence trends do not prove an infinite-horizon almost-sure limit. |
| 3 | Lemma 3.1: a path-dependent finite K controls the fast iterate for every time index. | The runner computes analytic family-specific K certificates and empirical running-max ratios. The adversarial route searches for large ratios without silently adding projection or clipping. | Family certificates passed; maximum nonlinear empirical K was 1.4465; adversarial search reached K 79.57 without a valid counterexample. | BLOCKED — constructed families do not cover the universal lemma. |
| 4 | Theorem 7.2: exact unprojected off-policy TDC(lambda) converges almost surely, with a related priority claim. | The TDC route derives A, b, C, and D from finite MDPs, checks Appendix F and A invertibility, runs positive lambda without projection, and records residuals and eligibility traces. Stress cells use high importance ratios. | Positive lambda values .25, .55, .85, .90, and .97; maximum trace norm 12,723; maximum importance ratio 5.02; no valid counterexample. | BLOCKED — faithful finite evidence is not a general proof, and the priority audit is not exhaustive. |
| 5 | The analysis depends on the complete Appendix B premise set, including unique stationarity and beta(n)/alpha(n) tending to zero. | The source route downloads the exact arXiv e-print, verifies its SHA-256, parses all six assumption environments in source order, checks theorem references, and applies destructive negative controls. | 78,416-byte source archive; all six labels and dependencies found; removing the timescale formula or mislabeling B.3 is rejected. | VERIFIED_SOURCE_DOMAIN_ONLY — verifies the registered source structure, not external premises or theorem validity. |

## How claims are produced

Every route follows the same evidence chain:

1. Pin the paper or comparison source by URL, revision, byte count, and SHA-256.
2. Write a machine-readable claim contract with assumptions, observable quantities, controls, and limitations.
3. Execute the route through reproduction/runner.py.
4. Run negative controls that must reject projection, missing assumptions, broken proof edges, rank deficiency, equal time scales, reducible chains, or unstable ODEs where applicable.
5. Save raw JSON under reports/reproduction/raw.
6. Apply the fail-closed verifier and the published release manifest.
7. Compare the immutable published artifact with its recorded revision.
8. Assign the status from the strongest statement the evidence supports, rather than from the most favorable observed trend.

The finite routes are therefore useful evidence about implementation fidelity and stress behavior. They do not silently upgrade an empirical trend into an almost-sure theorem.

## Repository map

| Path | Purpose |
| --- | --- |
| reproduction/runner.py | Rebuilds the historical, nonlinear SA, TDC, source, proof, and falsification routes. |
| reproduction/verify.py | Fail-closed verification helper for an aggregate result record. |
| reports/reproduction/report.md | Illustrated technical report with results, controls, and limitations. |
| reports/reproduction/raw/claims-1-2-3-nonlinear.json | Nonlinear SA cells, assumption audit, certificates, and finite outcomes. |
| reports/reproduction/raw/claim-4-tdc.json | Positive-lambda TDC evidence and negative controls. |
| reports/reproduction/raw/claim-5-source.json | Hash-pinned Appendix B source-domain audit. |
| reports/reproduction/raw/proof-route.json | Paper/Yu source graph and omitted-lemma audit. |
| reports/reproduction/raw/falsification-route.json | Nonnormal SA and high-ratio TDC falsification search. |
| reports/reproduction/raw/historical-baseline.json | Reconstructed judged d=3 and lambda=0 baseline. |
| reports/reproduction/raw/run-metadata.json | Evidence-generating run, machine, checker, and cost metadata. |
| notebooks/two_timescale_reproduction.py | Self-contained tutorial and experiment notebook. |
| space_candidate/ | Immutable published Space candidate with its own SHA256SUMS.txt manifest. |
| evidence/branch-audit.md | Former branch purposes, tips, ancestry, and normalization decision. |
| STATUS.md | Machine-readable project handoff and current claim statuses. |
| AUTONOMOUS_STATE.json | Checkpoint for continuing the audit without losing provenance. |

## Reproduce or inspect

From the repository root, the evidence-generating command is:

    uv sync --frozen --no-dev && uv run --frozen python reproduction/runner.py

The command uses the pinned uv.lock environment. It is a research run and can take substantial CPU time; the committed raw JSON files and report are the recorded campaign output.

To verify the published candidate's byte manifest:

    cd space_candidate
    sha256sum -c SHA256SUMS.txt

The source-domain verdict can be inspected directly in reports/reproduction/raw/claim-5-source.json. The full branch and experiment provenance is in [evidence/branch-audit.md](evidence/branch-audit.md).

## Branch policy

The old repository used eight orx-prefixed branches as experiment workspaces. All eight tips were ancestors of main, so they added labels and provenance but no independent final history. Their purposes and exact tips are preserved in [evidence/branch-audit.md](evidence/branch-audit.md).

The normalized public repository keeps one canonical branch: main. This makes the public surface easier to navigate while retaining the scientific branch audit in the repository itself.

## Limitations

- Finite trajectories cannot establish a statement quantified over all time with probability one.
- Analytic certificates were constructed for the implemented nonlinear family, not for every process covered by the theorem.
- The source audit verifies stated dependency structure, not whether every external application satisfies each premise.
- The proof route reconstructs source-level dependencies and detects the paper's explicitly omitted technical lemma; it is not a kernel-checked proof.
- The Yu (2017) priority comparison is a two-source primary audit, not an exhaustive literature search.
- The historical score is a judge result for the earlier release. Any 5–6/10 discussion is a forecast only.
- All recorded jobs used CPU; no GPU result is claimed.

## Citation

Please cite the accepted ICML paper when using this reproduction record:

    @inproceedings{mahadevan2026convergence,
      title={Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning},
      author={Vagul Mahadevan and Claire Chen and Shuze Daniel Liu and Shangtong Zhang},
      booktitle={International Conference on Machine Learning},
      year={2026},
      url={https://openreview.net/forum?id=Iww9TICvKj}
    }

The arXiv record is [2605.31172](https://arxiv.org/abs/2605.31172).

## Thank you

Thank you to Vagul Mahadevan, Claire Chen, Shuze Daniel Liu, and Shangtong Zhang for the theoretical work and for making the paper's assumptions, proof structure, and reinforcement-learning application concrete enough to audit. This repository is an independent reproduction and documentation effort; the authors are not responsible for its code, interpretations, or status labels.
