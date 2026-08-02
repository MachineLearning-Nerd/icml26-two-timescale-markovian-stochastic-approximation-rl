"""Independent fail-closed checks for generated reproduction evidence."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def verify(results: dict) -> None:
    machine = results["machine"]
    if machine["selected_flavor"] != "cpu-upgrade":
        raise AssertionError("run did not report the mandated cpu-upgrade flavor")
    if machine["gpu_device_files_detected"] != 0:
        raise AssertionError("GPU device detected")

    historical = results["historical_regression"]
    if not historical["all_gates_pass"]:
        raise AssertionError("historical cumulative regression failed")

    audit = results["claim_4"]["assumption_audit"]
    required = {
        "behavior_chain_irreducible",
        "behavior_policy_full_support",
        "feature_matrix_full_rank",
        "exact_A_invertible",
        "learning_rates_robbins_monro",
        "timescales_separate",
    }
    missing = required.difference(audit)
    if missing:
        raise AssertionError(f"missing assumption checks: {sorted(missing)}")
    failed = sorted(name for name in required if not audit[name])
    if failed:
        raise AssertionError(f"paper assumptions failed: {failed}")

    cells = results["claim_4"]["cells"]
    positive = [row for row in cells if row["lambda"] > 0]
    if not positive:
        raise AssertionError("lambda=0 is not evidence for eligibility traces")
    if len({row["lambda"] for row in positive}) < 3:
        raise AssertionError("eligibility-trace sweep is incomplete")
    if any(row["projection_or_clipping_used"] for row in cells):
        raise AssertionError("projection or clipping changes the claimed algorithm")
    if max(row["residual_reduction"] for row in positive) >= 0.45:
        raise AssertionError("TDC(lambda) did not sufficiently reduce the exact residual")
    if max(row["final_beta_over_alpha"] for row in cells) >= 0.2:
        raise AssertionError("finite-horizon timescale ratio is too large")
    if max(row["matrix_A_relative_error"] for row in cells) >= 0.14:
        raise AssertionError("sampled A disagrees with the analytic checker")
    if max(row["vector_b_relative_error"] for row in cells) >= 0.14:
        raise AssertionError("sampled b disagrees with the analytic checker")

    controls = results["claim_4"]["negative_controls"]
    expected = {
        "lambda_zero_only": "eligibility traces absent",
        "rank_deficient_features": "Assumption F.2 violated",
        "reducible_behavior_chain": "Assumption F.1 violated",
        "no_timescale_separation": "Assumption B.2 violated",
    }
    for name, reason in expected.items():
        row = controls[name]
        if row != {"accepted": False, "reason": reason}:
            raise AssertionError(f"negative control {name} did not fail as intended")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python reproduction/verify.py RESULTS.json")
    path = Path(sys.argv[1])
    results = json.loads(path.read_text(encoding="utf-8"))
    verify(results)
    print(json.dumps({"status": "PASS", "verified": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
