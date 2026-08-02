"""Historical judged-baseline reconstruction.

This node intentionally recreates the small numerical scope criticized by the
2026-07-30 judge. It never promotes finite paths to theorem verification.
"""

from __future__ import annotations

import json
import math
import os
import platform
import time
from pathlib import Path

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / ".openresearch/artifacts/historical_baseline/generated"


def stationary_distribution(P: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eig(P.T)
    index = int(np.argmin(np.abs(values - 1.0)))
    pi = np.real(vectors[:, index])
    if np.sum(pi) < 0:
        pi = -pi
    return pi / np.sum(pi)


def linear_model() -> dict[str, np.ndarray]:
    dim = 3
    states = 5
    P = np.full((states, states), 0.06)
    np.fill_diagonal(P, 0.76)
    A = np.diag([1.7, 1.9, 2.1])
    A += 0.06 * (np.ones((dim, dim)) - np.eye(dim))
    B = np.array([[0.22, -0.06, 0.03], [0.04, 0.18, -0.05], [-0.02, 0.07, 0.20]])
    C = np.diag([1.25, 1.45, 1.65])
    D = np.array([[0.10, 0.02, 0.00], [-0.03, 0.08, 0.02], [0.01, -0.02, 0.09]])
    c = np.array([0.30, -0.18, 0.12])
    e = np.array([-0.10, 0.16, -0.08])
    pi = stationary_distribution(P)
    grid = np.arange(states)[:, None]
    dims = np.arange(1, dim + 1)[None, :]
    noise_x = np.sin((grid + 1) * dims * 0.73)
    noise_y = np.cos((grid + 1.5) * dims * 0.61)
    noise_x -= pi @ noise_x
    noise_y -= pi @ noise_y
    noise_x *= 0.22 / np.max(np.linalg.norm(noise_x, axis=1))
    noise_y *= 0.20 / np.max(np.linalg.norm(noise_y, axis=1))
    return {"P": P, "A": A, "B": B, "C": C, "D": D, "c": c, "e": e,
            "noise_x": noise_x, "noise_y": noise_y}


def linear_equilibrium(model: dict[str, np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    A, B, C, D, c, e = (model[k] for k in ("A", "B", "C", "D", "c", "e"))
    A_inv_B = np.linalg.solve(A, B)
    A_inv_c = np.linalg.solve(A, c)
    slow = C - D @ A_inv_B
    y_star = np.linalg.solve(slow, D @ A_inv_c + e)
    x_star = np.linalg.solve(A, B @ y_star + c)
    return x_star, y_star


def run_linear(seed: int, steps: int = 35_000) -> dict[str, float | int | bool]:
    model = linear_model()
    rng = np.random.default_rng(seed)
    x = rng.normal(0.0, 2.2, 3)
    y = rng.normal(0.0, 1.8, 3)
    initial = np.r_[x, y]
    state = int(rng.integers(5))
    x_star, y_star = linear_equilibrium(model)
    max_z = float(np.linalg.norm(initial))
    max_y = float(np.linalg.norm(y))
    empirical_k = float(np.linalg.norm(x) / (1.0 + max_y))
    for n in range(steps):
        state = int(rng.choice(5, p=model["P"][state]))
        alpha = 0.72 / ((n + 40.0) ** 0.55)
        beta = 0.52 / ((n + 40.0) ** 0.85)
        fast = -model["A"] @ x + model["B"] @ y + model["c"] + model["noise_x"][state]
        slow = -model["C"] @ y + model["D"] @ x + model["e"] + model["noise_y"][state]
        x += alpha * fast
        y += beta * slow
        max_y = max(max_y, float(np.linalg.norm(y)))
        empirical_k = max(empirical_k, float(np.linalg.norm(x) / (1.0 + max_y)))
        max_z = max(max_z, float(np.linalg.norm(np.r_[x, y])))
    tracking = float(np.linalg.norm(x - np.linalg.solve(model["A"], model["B"] @ y + model["c"])))
    joint = float(np.linalg.norm(np.r_[x - x_star, y - y_star]))
    return {
        "seed": seed,
        "dimension_fast": 3,
        "dimension_slow": 3,
        "steps": steps,
        "initial_z_norm": float(np.linalg.norm(initial)),
        "max_z_norm": max_z,
        "final_tracking_error": tracking,
        "final_joint_error": joint,
        "empirical_K": empirical_k,
        "final_beta_over_alpha": beta / alpha,
        "projection_or_clipping_used": False,
    }


def tdc_model() -> dict[str, np.ndarray | int]:
    states = 5
    P = np.zeros((states, states))
    for s in range(states):
        P[s, s] = 0.25
        P[s, (s + 1) % states] = 0.55
        P[s, (s + 2) % states] = 0.20
    mu = np.array([0.62, 0.38])
    target = np.empty((states, 2))
    for s in range(states):
        target[s] = [0.30 + 0.08 * math.sin(s), 0.70 - 0.08 * math.sin(s)]
    angles = 2.0 * math.pi * np.arange(states) / states
    Phi = np.column_stack([np.ones(states), np.sin(angles), np.cos(angles)])
    Phi /= np.linalg.norm(Phi, axis=0, keepdims=True)
    reward = np.column_stack([0.2 * np.cos(angles) - 0.05, 0.3 * np.sin(angles + 0.2) + 0.1])
    return {"P": P, "mu": mu, "target": target, "Phi": Phi, "reward": reward, "states": states}


def tdc_reference(model: dict[str, np.ndarray | int], gamma: float = 0.82) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    P = model["P"]
    mu = model["mu"]
    target = model["target"]
    Phi = model["Phi"]
    reward = model["reward"]
    pi = stationary_distribution(P)
    A = np.zeros((3, 3))
    b = np.zeros(3)
    for s in range(int(model["states"])):
        for a in range(2):
            rho = target[s, a] / mu[a]
            for nxt in range(int(model["states"])):
                weight = pi[s] * mu[a] * P[s, nxt]
                A += weight * rho * np.outer(Phi[s], gamma * Phi[nxt] - Phi[s])
                b += weight * rho * reward[s, a] * Phi[s]
    return A, b, -np.linalg.solve(A, b)


def run_tdc(seed: int, steps: int = 45_000) -> dict[str, float | int | bool]:
    model = tdc_model()
    P, mu, target, Phi, reward = (model[k] for k in ("P", "mu", "target", "Phi", "reward"))
    A, b, theta_star = tdc_reference(model)
    rng = np.random.default_rng(seed)
    theta = np.zeros(3)
    nu = np.zeros(3)
    state = int(rng.integers(int(model["states"])))
    initial_residual = float(np.linalg.norm(b))
    min_rho = math.inf
    max_rho = 0.0
    for t in range(steps):
        action = int(rng.choice(2, p=mu))
        nxt = int(rng.choice(int(model["states"]), p=P[state]))
        rho = float(target[state, action] / mu[action])
        delta = float(reward[state, action] + 0.82 * Phi[nxt] @ theta - Phi[state] @ theta)
        alpha = 0.64 / ((t + 80.0) ** 0.58)
        beta = 0.52 / ((t + 80.0) ** 0.76)
        e_trace = Phi[state]
        nu += alpha * (rho * delta * e_trace - Phi[state] * float(Phi[state] @ nu))
        theta += beta * (rho * delta * e_trace - rho * 0.82 * Phi[nxt] * float(e_trace @ nu))
        state = nxt
        min_rho = min(min_rho, rho)
        max_rho = max(max_rho, rho)
    residual = float(np.linalg.norm(A @ theta + b))
    return {
        "seed": seed,
        "states": 5,
        "features": 3,
        "lambda": 0.0,
        "steps": steps,
        "theta_reference_error": float(np.linalg.norm(theta - theta_star)),
        "fixed_point_residual": residual,
        "residual_reduction": residual / initial_residual,
        "min_importance_ratio": min_rho,
        "max_importance_ratio": max_rho,
        "max_eligibility_trace_norm": float(np.max(np.linalg.norm(Phi, axis=1))),
        "projection_or_clipping_used": False,
    }


def machine_info() -> dict[str, object]:
    affinity = len(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else os.cpu_count()
    return {
        "backend": "hf",
        "selected_flavor": "cpu-upgrade",
        "estimated_required_cores": 1,
        "actual_logical_cpus": os.cpu_count(),
        "actual_cpu_affinity": affinity,
        "platform": platform.platform(),
        "python": platform.python_version(),
        "gpu_device_files_detected": len(list(Path("/dev").glob("nvidia*"))),
    }


def main() -> None:
    started = time.perf_counter()
    machine = machine_info()
    if machine["gpu_device_files_detected"] != 0:
        raise AssertionError("GPU device detected in CPU-only campaign")
    linear = [run_linear(seed) for seed in range(8)]
    tdc = [run_tdc(seed) for seed in range(5)]
    model = linear_model()
    pi = stationary_distribution(model["P"])
    slow_matrix = model["C"] - model["D"] @ np.linalg.solve(model["A"], model["B"])
    gates = {
        "claim_1_toy_stability": max(row["max_z_norm"] for row in linear) < 20.0,
        "claim_2_toy_convergence": float(np.median([row["final_joint_error"] for row in linear])) < 0.7
        and float(np.median([row["final_tracking_error"] for row in linear])) < 0.15,
        "claim_3_toy_running_max_bound": max(row["empirical_K"] for row in linear) < 10.0,
        "claim_4_lambda_zero_proxy": float(np.median([row["residual_reduction"] for row in tdc])) < 0.75,
        "claim_5_partial_assumption_audit": float(np.max(np.abs(pi @ model["P"] - pi))) < 1e-12
        and max(row["final_beta_over_alpha"] for row in linear) < 0.08
        and float(np.min(np.real(np.linalg.eigvals(model["A"])))) > 0
        and float(np.min(np.real(np.linalg.eigvals(slow_matrix)))) > 0,
    }
    results = {
        "schema_version": 1,
        "artifact_status": "Historical rejected baseline",
        "judge_sha": "ba24d26d274d66c8cdb627aa5a324b47d189dfe0",
        "scope": {"linear_dimension": [3, 3], "linear_paths": 8, "tdc_states_features": [5, 3], "tdc_lambdas": [0.0]},
        "machine": machine,
        "linear_paths": linear,
        "tdc_paths": tdc,
        "summary": {
            "max_z_norm": max(row["max_z_norm"] for row in linear),
            "median_final_tracking_error": float(np.median([row["final_tracking_error"] for row in linear])),
            "median_final_joint_error": float(np.median([row["final_joint_error"] for row in linear])),
            "max_empirical_K": max(row["empirical_K"] for row in linear),
            "median_tdc_theta_reference_error": float(np.median([row["theta_reference_error"] for row in tdc])),
            "median_tdc_residual_reduction": float(np.median([row["residual_reduction"] for row in tdc])),
        },
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "scientific_verdict": "BLOCKED",
        "limitation": "Finite d=3 paths and lambda=0 TDC are scoped corroboration only; they cannot prove universal almost-sure claims.",
    }
    results["runtime_seconds"] = time.perf_counter() - started
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("ORX_EVIDENCE_BEGIN")
    print(json.dumps(results, indent=2, sort_keys=True))
    print("ORX_EVIDENCE_END")
    if not results["all_gates_pass"]:
        failed = [name for name, passed in gates.items() if not passed]
        raise AssertionError(f"historical baseline gates failed: {failed}")


if __name__ == "__main__":
    main()
