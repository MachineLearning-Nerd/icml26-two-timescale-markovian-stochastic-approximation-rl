# Branch and experiment audit

This record preserves the purpose of every former experiment branch before the public repository is normalized. The branch names were useful while the campaign was running, but they are not needed as separate public entry points after the evidence has been merged into main.

Observed repository state before normalization: 2026-08-13.

## Branch ledger

| Former branch | Tip | Purpose | Ancestor of main |
| --- | --- | --- | --- |
| main | 4a66b0196028c48a3fc88b38e30eda28fc08d944 | Public cumulative report and final reproduction provenance. | Yes |
| orx/historical-judged-baseline-reconstruction | 381bc33d2e04aec9314fae159c6680ee44ef407b | Reconstruct the historical d=3 and lambda=0 judged baseline and preserve its rejected status. | Yes |
| orx/exact-tdc-traces-and-cumulative-verifier | 36b7b05195c1a54d5acece02c4e1ba5c5f62f36c | Add exact Definition 7.1 TDC traces and cumulative verification. | Yes |
| orx/nonlinear-sa-scaling-and-assumption-certificates | 0b543919d750e03e9c4af73df7d7000b62a313ed | Add nonlinear dimensions, Markov mixing regimes, and family-specific assumption certificates. | Yes |
| orx/hash-pinned-assumption-source-verifier | 33a1d38448d4d6a955e174c89cae526b1f85653b | Pin the paper source by hash and verify Appendix B dependency labels. | Yes |
| orx/proof-dependency-reconstruction | f447c935f9339516415d6273e8f7a2f30729c574 | Reconstruct the paper/Yu proof graph and identify source-level proof obligations. | Yes |
| orx/mandatory-falsification-search | 7f24f1dce0b64a254d51e483a4b3f581f4610a6a | Search nonnormal SA and high-ratio TDC regimes for valid assumption-satisfying counterexamples. | Yes |
| orx/evaluator-visible-release-candidate | e1ddb9a44ebc37743b6d0f94b5300612910a2c38 | Add cumulative release gates, canonical traversal, protected-file checks, and upload-manifest checks. | Yes |
| orx/post-publication-exact-revision-audit | 4a1f325caf2a4f9a6c8831e7ea5c1cdca4b563c4 | Re-download the immutable Hugging Face revision and compare published bytes and evidence hashes. | Yes |

## What this means

All eight former orx tips were reachable from main. There were no branch-only commits that needed to be rescued separately. The branch labels represent experiment provenance, not competing scientific conclusions.

The public normalization therefore keeps only main and retains this table, the raw JSON contracts, and the report as the durable provenance layer. The old branch names should not be used as links after cleanup; this file is the canonical internal crosswalk.

## Attribution policy

The normalized history is attributed to MachineLearning-Nerd with the account's GitHub no-reply identity. The cleanup does not change scientific evidence or the immutable Hugging Face publication; it only makes repository ownership, branch naming, and commit attribution consistent.
