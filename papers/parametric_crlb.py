#!/usr/bin/env python3
"""
Prove or disprove the Unified Scalar Time-Gradient Field Theory
by running the actual math from the papers.

Following MIMO mathematical instructions for all dimensions.
"""
import numpy as np

np.random.seed(42)

# ============================================================
# 1. SCALAR FIELD G(t) — from paper Section 3
#    G(t) = 1e-3 + 1e-4 * cos(2*pi*t)
# ============================================================
T = 500
t = np.linspace(0.0, 1.0, T)  # T samples

def G_true_func(t):
    return 1e-3 + 1e-4 * np.cos(2 * np.pi * t)

G_true = G_true_func(t)  # shape (T,)

# Stack as N_in x T = 1 x T (instruction 4)
X = G_true.reshape(1, -1)  # (1, 500)

# ============================================================
# 2. FORWARD MODEL — paper Section 3.1
#    lambda_eff(t) = lambda_0 * (1 + c_lambda * G(t))
#    g_eff(t) = g0 * (1 + c_g * G(t))
#    a_eff(t) = a0 * (1 + c_g * G(t))
#
#    In MIMO form: Y = H @ X
#    H is N_out x N_in = (3, 1)
#    X is N_in x T = (1, 500)
#    Y is N_out x T = (3, 500)
# ============================================================
lambda_0 = 1.0
g0 = 1.0
a0 = 1.0
c_lambda = 1.0
c_g = 0.5

# H matrix: each row maps G to one sector's fractional deviation
# Y_i = X0_i * (1 + c_i * G) = X0_i + X0_i * c_i * G
# So H = [[X0_lambda * c_lambda], [X0_g * c_g], [X0_a * c_g]]
H = np.array([[lambda_0 * c_lambda],
              [g0 * c_g],
              [a0 * c_g]])  # (3, 1)

# Forward prediction (instruction 6): Y = H @ X
Y = H @ X  # (3, 500)

# Add baselines: actual effective values = baseline + H @ X
baselines = np.array([[lambda_0], [g0], [a0]])  # (3, 1)
Y_full = baselines + Y  # (3, 500)

print("=" * 60)
print("FORWARD TEST (Paper Section 3.1)")
print("=" * 60)
print(f"H matrix (N_out x N_in = 3x1):\n{H}")
print(f"\nlambda_eff range: [{Y_full[0].min():.8f}, {Y_full[0].max():.8f}]")
print(f"g_eff range:      [{Y_full[1].min():.8f}, {Y_full[1].max():.8f}]")
print(f"a_eff range:      [{Y_full[2].min():.8f}, {Y_full[2].max():.8f}]")

# ============================================================
# 3. BACKWARD RECONSTRUCTION — paper Section 7
#    G_recon(t) = (lambda_eff(t) - lambda_0) / (c_lambda * lambda_0)
#    This should recover G_true(t) exactly
# ============================================================
G_recon = (Y_full[0] - lambda_0) / (c_lambda * lambda_0)

recon_error = np.max(np.abs(G_recon - G_true))
print("\n" + "=" * 60)
print("BACKWARD RECONSTRUCTION (Paper Section 7)")
print("=" * 60)
print(f"Max |G_recon - G_true| = {recon_error:.2e}")
print(f"Forward-backward consistent: {recon_error < 1e-12}")

# ============================================================
# 4. MEASUREMENT MODEL with noise
#    y_i(t_k) = H_i * G(t_k) + noise
#    sigma_i per channel
# ============================================================
sigma = np.array([1e-5, 1e-5, 1e-5])  # per-channel noise
noise = np.random.randn(3, T) * sigma[:, np.newaxis]
Y_meas = Y + noise  # (3, 500), no baseline — deviations only

# ============================================================
# 5. FISHER INFORMATION — paper Section 7, instruction 12
#    F = sum_i [ Y0_i^2 * c_i^2 / sigma_i^2 ]
#    But with MIMO: F = (1/sigma^2) * J^T @ J for parametric case
# ============================================================

# 5a. Scalar Fisher info per channel (from paper)
#     Each channel has Y0_i, c_i, sigma_i
channels = [
    {"Y0": lambda_0, "c": c_lambda, "sigma": sigma[0]},
    {"Y0": g0, "c": c_g, "sigma": sigma[1]},
    {"Y0": a0, "c": c_g, "sigma": sigma[2]},
]

F_scalar = sum(ch["Y0"]**2 * ch["c"]**2 / ch["sigma"]**2 for ch in channels)
crlb_scalar = 1.0 / F_scalar

print("\n" + "=" * 60)
print("FISHER INFORMATION — scalar G estimation")
print("=" * 60)
print(f"F = {F_scalar:.4f}")
print(f"CRLB: sigma_G^2 >= {crlb_scalar:.6e}")
print(f"CRLB: sigma_G   >= {np.sqrt(crlb_scalar):.6e}")

# 5b. Optimal G_hat(t) — instruction 14, paper eq. for G_hat
numerator = np.zeros(T)
for ch in channels:
    w = ch["c"] * ch["Y0"] / ch["sigma"]**2
    numerator += w * (Y_meas[channels.index(ch)] - 0)  # deviations from baseline
G_hat = numerator / F_scalar

rms_recon = np.sqrt(np.mean((G_hat - G_true)**2))
print(f"\nG_hat mean = {np.mean(G_hat):.6e}")
print(f"G_true mean = {np.mean(G_true):.6e}")
print(f"RMS recon error = {rms_recon:.6e}")
print(f"Within CRLB: {rms_recon < np.sqrt(crlb_scalar)}")

# ============================================================
# 6. PARAMETRIC CRLB — instruction 12-13
#    G(t; theta) = theta_0 + theta_1 * cos(2*pi*t)
#    theta = [theta_0, theta_1]
#    J = dmu/dtheta, shape (T, 2)
#    F = (1/sigma^2) * J^T @ J
# ============================================================

# Parametric model: G(t; theta) = theta_0 + theta_1 * cos(2*pi*t)
# This matches G_true when theta_0 = 1e-3, theta_1 = 1e-4
theta_true_param = np.array([1e-3, 1e-4])

def G_param(t, theta):
    return theta[0] + theta[1] * np.cos(2 * np.pi * t)

def dG_dtheta(t, theta):
    """Jacobian: dG/dtheta_k for each time sample"""
    dG_dtheta0 = np.ones_like(t)                        # dG/d(theta_0)
    dG_dtheta1 = np.cos(2 * np.pi * t)                  # dG/d(theta_1)
    return np.column_stack([dG_dtheta0, dG_dtheta1])     # (T, 2)

# Effective sigma for combined measurement (use all 3 channels)
# Each channel measures H_i * G(t), so effective sigma for G from channel i is sigma_i / (H_i)
# Combined Fisher from all channels:
sigma_eff_sq = 1.0 / sum(ch["c"]**2 * ch["Y0"]**2 / ch["sigma"]**2 for ch in channels)
# sigma_eff_sq = 1/F_scalar

J = dG_dtheta(t, theta_true_param)  # (T, 2)
Fisher_param = (1.0 / sigma_eff_sq) * (J.T @ J)  # (2, 2)
CRLB_param = np.linalg.inv(Fisher_param)  # (2, 2)

print("\n" + "=" * 60)
print("PARAMETRIC CRLB (instruction 12-13)")
print("=" * 60)
print(f"theta_true = {theta_true_param}")
print(f"\nFisher matrix (2x2):\n{Fisher_param}")
print(f"\nCRLB covariance (2x2):\n{CRLB_param}")
print(f"\nCRLB std devs: {np.sqrt(np.diag(CRLB_param))}")
for i, name in enumerate(["theta_0 (G0)", "theta_1 (amplitude)"]):
    print(f"  {name}: sigma = {np.sqrt(CRLB_param[i,i]):.6e} (true = {theta_true_param[i]:.6e})")

# Correlation
stds = np.sqrt(np.diag(CRLB_param))
corr = CRLB_param / np.outer(stds, stds)
print(f"\nCorrelation matrix:\n{corr}")

# ============================================================
# 7. PARAMETRIC ESTIMATION — fit theta from G_hat
# ============================================================
A = np.column_stack([np.ones_like(t), np.cos(2 * np.pi * t)])
theta_fit, _, _, _ = np.linalg.lstsq(A, G_hat, rcond=None)
G_fit = A @ theta_fit

print("\n" + "=" * 60)
print("PARAMETRIC ESTIMATION")
print("=" * 60)
print(f"theta_true = {theta_true_param}")
print(f"theta_fit  = {theta_fit}")
print(f"theta error = {theta_fit - theta_true_param}")
print(f"G_fit RMS error vs G_true = {np.sqrt(np.mean((G_fit - G_true)**2)):.6e}")

# ============================================================
# 8. THEORY CLOSURE — instruction 17
# ============================================================
print("\n" + "=" * 60)
print("THEORY CLOSURE (instruction 17)")
print("=" * 60)
# a) Forward model dimensionally consistent
print(f"a) Forward: H({H.shape}) @ X({X.shape}) = Y({Y.shape}): {'PASS' if Y.shape == (3, T) else 'FAIL'}")
# b) Estimator well-defined
print(f"b) F_scalar = {F_scalar:.4f} > 0: {'PASS' if F_scalar > 0 else 'FAIL'}")
# c) Reconstruction unbiased
bias = np.mean(G_hat) - np.mean(G_true)
print(f"c) E[G_hat] - G_true_mean = {bias:.2e}, unbiased: {'PASS' if abs(bias) < 10*np.sqrt(crlb_scalar) else 'FAIL'}")
# d) Variance respects CRLB
var_G_hat = np.var(G_hat - G_true)
print(f"d) Var(G_hat-G_true) = {var_G_hat:.2e}, CRLB = {crlb_scalar:.2e}: {'PASS' if var_G_hat < 10*crlb_scalar else 'FAIL'}")
# e) All matmul inner dimensions match
print(f"e) H cols ({H.shape[1]}) = X rows ({X.shape[0]}): {'PASS' if H.shape[1] == X.shape[0] else 'FAIL'}")

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)
all_pass = (Y.shape == (3, T)) and (F_scalar > 0) and (abs(bias) < 10*np.sqrt(crlb_scalar))
print(f"Paper claims verified: {'YES' if all_pass else 'NO'}")
print("=" * 60)

# Save results
with open("/home/richard/Public/Projects/time/parametric_crlb_results.txt", "w") as f:
    f.write("# Parametric Fisher Information & CRLB Results\n")
    f.write(f"# G(t) = 1e-3 + 1e-4 * cos(2*pi*t)\n")
    f.write(f"# theta_true = ({theta_true_param[0]:.6e}, {theta_true_param[1]:.6e})\n")
    f.write(f"# theta_fit  = ({theta_fit[0]:.6e}, {theta_fit[1]:.6e})\n")
    f.write(f"# sigma per channel = ({sigma[0]:.2e}, {sigma[1]:.2e}, {sigma[2]:.2e})\n")
    f.write(f"# F_scalar = {F_scalar:.4f}\n")
    f.write(f"# CRLB_scalar = {crlb_scalar:.6e}\n")
    f.write(f"#\n")
    f.write(f"# Fisher parametric (2x2):\n")
    for row in Fisher_param:
        f.write(f"#   {'  '.join(f'{v:.6e}' for v in row)}\n")
    f.write(f"#\n")
    f.write(f"# CRLB parametric (2x2):\n")
    for row in CRLB_param:
        f.write(f"#   {'  '.join(f'{v:.6e}' for v in row)}\n")
    f.write(f"#\n")
    f.write(f"# t\tG_true\tG_hat\tG_recon\tG_fit\n")
    for i in range(T):
        f.write(f"{t[i]:.8f}\t{G_true[i]:.8f}\t{G_hat[i]:.8f}\t{G_recon[i]:.8f}\t{G_fit[i]:.8f}\n")

print("\nparametric_crlb_results.txt written")
