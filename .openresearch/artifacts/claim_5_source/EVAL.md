# Evaluator guide

Run the fixed command and locate `claim_5_source` in the line beginning `ORX_EVIDENCE`. Confirm the exact source hash, all structural booleans, assumption count, and both rejected mutations. The final line must report `ORX_CHECKER` as PASS and the process must exit nonzero after any failed predicate.

Durable outputs: `raw_results.json`, `independent_checker_output.json`, `claim_verifier.py`, and `runtime_cpu.json`. Negative controls are embedded under `negative_controls` in the raw output.

Final verdict: **VERIFIED, HIGH confidence** on the complete registered source domain. Limitation: this does not assert that every external application satisfies the paper's premises.
