# Evaluator guide

Locate `mandatory_falsification_search` in `ORX_EVIDENCE`. Check the exact contracts and anchors, all SA and TDC assumption flags, the search and holdout horizons, first-hit field, positive traces, and all rejected controls. Confirm `valid_counterexample_found: false` unless a complete assumption-satisfying mathematical contradiction is present.

If no valid counterexample is established, Claims 1–4 must be exactly `BLOCKED`. This route completes the required fourth attempt but does not turn finite non-discovery into theorem verification.
