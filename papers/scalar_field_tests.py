#!/usr/bin/env python3
"""
Unified Scalar Time-Gradient Field Theory
Forward tests, backward reconstruction, and Fisher information estimates.
"""

import numpy as np

# ── Model definitions ──────────────────────────────────────────────────────

def G(t):
    """Scalar field: G(t) = 1e-3 + 1e-4 * cos(2πt)"""
    return 1e-3 + 1e-4 * np.cos(2 * np.pi * t)

# ── Parameters ─────────────────────────────────────────────────────────────

lambda_0 = 1.0
g0 = 1.0
a0 = 1.0
c_lambda = 1.0
c_g = 0.5

# ── 1. Forward tests ───────────────────────────────────────────────────────

t = np.linspace(0, 1, 500)
G_t = G(t)

lambda_eff = lambda_0 * (1 + c_lambda * G_t)
g_eff = g0 * (1 + c_g * G_t)
a_eff = a0 * (1 + c_g * G_t)

forward_data = np.column_stack([t, lambda_eff, g_eff, a_eff])
np.savetxt(
    "/home/richard/Public/Projects/time/forward_results.txt",
    forward_data,
    header="t  lambda_eff(t)  g_eff(t)  a_eff(t)",
    fmt="%.8f",
    delimiter="\t",
)
print("forward_results.txt written")

# ── 2. Backward reconstruction ─────────────────────────────────────────────

G_recon = (lambda_eff - lambda_0) / (c_lambda * lambda_0)

backward_data = np.column_stack([t, G_recon])
np.savetxt(
    "/home/richard/Public/Projects/time/backward_results.txt",
    backward_data,
    header="t  G_recon(t)",
    fmt="%.8f",
    delimiter="\t",
)
print("backward_results.txt written")

# ── 3. Fisher information reconstruction ────────────────────────────────────

rng = np.random.default_rng(42)

# Define3 independent measurement streams
# Stream 0: decay (c=1.0, Y0=1.0, sigma=0.0005)
# Stream 1: gravity (c=0.5, Y0=1.0, sigma=0.0003)
# Stream 2: inertia (c=0.3, Y0=1.0, sigma=0.0004)
streams = [
    {"Y0": 1.0, "c": 1.0, "sigma": 0.0005},
    {"Y0": 1.0, "c": 0.5, "sigma": 0.0003},
    {"Y0": 1.0, "c": 0.3, "sigma": 0.0004},
]

N = len(streams)
n_points = len(t)

# Generate noisy measurements
Y = np.zeros((N, n_points))
for i, s in enumerate(streams):
    noise = rng.normal(0, s["sigma"], n_points)
    Y[i] = s["Y0"] * (1 + s["c"] * G_t) + noise

# Fisher information
F = sum(s["Y0"] ** 2 * s["c"] ** 2 / s["sigma"] ** 2 for s in streams)
cramer_rao_bound = 1.0 / F

# Optimized reconstruction G_hat(t)
numerator = np.zeros(n_points)
denominator = 0.0
for i, s in enumerate(streams):
    w = s["c"] * s["Y0"] / s["sigma"] ** 2
    numerator += w * (Y[i] - s["Y0"])
    denominator += s["Y0"] ** 2 * s["c"] ** 2 / s["sigma"] ** 2

G_hat = numerator / denominator

fisher_data = np.column_stack([t, G_t, G_hat])
np.savetxt(
    "/home/richard/Public/Projects/time/fisher_results.txt",
    fisher_data,
    header=f"t  G_true(t)  G_hat(t) | Fisher F={F:.4f}  Cramer-Rao sigma_G^2>={cramer_rao_bound:.6e}",
    fmt="%.8f",
    delimiter="\t",
)

# Print summary
print("fisher_results.txt written")
print(f"\n{'='*60}")
print(f"Fisher Information F = {F:.4f}")
print(f"Cramer-Rao bound   σ_G^2 >= {cramer_rao_bound:.6e}")
print(f"Cramer-Rao bound   σ_G   >= {np.sqrt(cramer_rao_bound):.6e}")
print(f"G_hat mean         = {np.mean(G_hat):.6e}")
print(f"G_true mean        = {np.mean(G_t):.6e}")
print(f"Recon error (RMS)  = {np.sqrt(np.mean((G_hat - G_t)**2)):.6e}")
print(f"{'='*60}")
print("\nAll forward, backward, and Fisher computations complete.")
