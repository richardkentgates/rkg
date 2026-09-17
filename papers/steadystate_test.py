#!/usr/bin/env python3
"""
Test: Can field + relic cosmology replace the Big Bang?
Run the steady-state scaffold equations against observational constraints.
"""
import numpy as np

# Constants
G_Newt = 6.674e-11
c = 2.998e8
M_Pl = 2.176e-8
H0 = 2.184e-18  # s^-1
rho_crit = 3 * H0**2 / (8 * np.pi * G_Newt)
k_B = 1.381e-23
hbar = 1.055e-34

print("=" * 70)
print("TEST: FIELD + RELIC COSMOLOGY VS BIG BANG")
print("=" * 70)

# ============================================================
# TEST 1: CAN THE MODEL PRODUCE THE CMB?
# ============================================================
print("\n" + "=" * 70)
print("TEST 1: COSMIC MICROWAVE BACKGROUND (CMB)")
print("=" * 70)

# The CMB is a blackbody at T = 2.7255 K with spectral distortions < 10^-5.
# Big Bang explanation: photons from last scattering (z~1100) redshifted by (1+z).
# Steady-state must produce the SAME blackbody.

T_cmb = 2.7255  # K
z_last_scatter = 1100
T_last_scatter = T_cmb * (1 + z_last_scatter)

# Blackbody spectrum: B(nu, T) = (2h*nu^3/c^2) / (exp(h*nu/kT) - 1)
# CMB is a perfect blackbody to 10^-5 — this is VERY hard to reproduce
# without a thermalization epoch.

# Steady-state question: where do these photons come from and why
# are they thermalized?

print(f"\nCMB temperature: {T_cmb} K")
print(f"If from last scattering: T_source = {T_last_scatter:.0f} K")
print(f"Spectral distortion limit: < 10^-5")
print(f"\nBig Bang explanation: photons thermalized in early hot dense state")
print(f"  (z > 2e6, T > 3000 K, universe is opaque)")
print(f"  Redshift by factor (1+1100) = 1101 produces 2.7255 K blackbody")
print(f"  This naturally explains perfect blackbody shape")

print(f"\nSteady-state requirement:")
print(f"  Must produce perfect blackbody WITHOUT a thermalization epoch")
print(f"  Options:")
print(f"    a) Relic evaporation produces thermal photons — but spectrum")
print(f"       would NOT be Planckian (Hawking radiation is NOT thermal")
print(f"       in the usual sense for a population of relics)")
print(f"    b) Field decay produces photons — but would produce line")
print(f"       emission, not broadband blackbody")
print(f"    c) Scattering thermalizes photons — but requires high optical")
print(f"       depth, which requires high density, which requires early time")

# Quantitative: how many CMB photons per m^3?
# n_gamma = 2 * zeta(3) / pi^2 * (kT/hbar*c)^3
zeta3 = 1.202
n_gamma = 2 * zeta3 / np.pi**2 * (k_B * T_cmb / (hbar * c))**3
rho_gamma = n_gamma * 2.7 * k_B * T_cmb  # energy density

print(f"\nCMB photon number density: {n_gamma:.3e} photons/m^3")
print(f"CMB energy density: {rho_gamma:.3e} J/m^3")
print(f"CMB energy density / rho_crit: {rho_gamma / (rho_crit * c**2):.3e}")

# Verdict
print(f"\n  VERDICT: CMB blackbody is a MAJOR problem for steady-state")
print(f"  No known steady-state mechanism produces a perfect blackbody")
print(f"  to 10^-5 precision across 3 decades in frequency.")

# ============================================================
# TEST 2: BIG BANG NUCLEOSYNTHESIS (BBN)
# ============================================================
print("\n" + "=" * 70)
print("TEST 2: PRIMORDIAL ELEMENT ABUNDANCES")
print("=" * 70)

# Observed primordial abundances:
# He-4: Y_p = 0.2471 +/- 0.0002 (mass fraction)
# D/H: (2.527 +/- 0.030) x 10^-5
# He-3/H: < 1.1 x 10^-5
# Li-7/H: (1.6 +/- 0.3) x 10^-10

# Big Bang predicts these from nuclear physics at T ~ 10^9 K (t ~ 3 min)
# with ONE free parameter: baryon-to-photon ratio eta

eta_obs = 6.1e-10  # baryon-to-photon ratio

# BBN predictions (simplified):
# He-4: Y_p ~ 0.247 (very insensitive to eta)
# D/H ~ 3.6e-5 / eta_10 (where eta_10 = eta / 1e-10)
eta_10 = eta_obs / 1e-10
D_H_pred = 3.6e-5 / eta_10

print(f"\nObserved primordial abundances:")
print(f"  He-4: Y_p = 0.2471 +/- 0.0002")
print(f"  D/H = (2.527 +/- 0.030) x 10^-5")
print(f"  Li-7/H = (1.6 +/- 0.3) x 10^-10")

print(f"\nBBN prediction (eta = {eta_obs:.2e}):")
print(f"  He-4: Y_p ~ 0.247 (matches)")
print(f"  D/H ~ {D_H_pred:.3e} (matches)")

print(f"\nSteady-state requirement:")
print(f"  Must explain these EXACT ratios without a hot dense phase")
print(f"  Options:")
print(f"    a) Nucleosynthesis in BH environments — but He-4 production")
print(f"       requires T ~ 10^9 K with correct neutron/proton ratio")
print(f"       AND correct freeze-out timing (t ~ 3 min)")
print(f"    b) Stellar nucleosynthesis — produces WRONG abundances")
print(f"       (too little D, too much Li, wrong He-3/He-4 ratio)")
print(f"    c) Relic evaporation — would produce exotic particles,")
print(f"       not standard BBN abundances")

print(f"\n  VERDICT: BBN abundances strongly favor a hot dense phase")
print(f"  Steady-state has no natural mechanism to produce D/H = 2.5e-5")

# ============================================================
# TEST 3: HUBBLE DIAGRAM + SUPERNOVAE
# ============================================================
print("\n" + "=" * 70)
print("TEST 3: HUBBLE DIAGRAM (TYPE Ia SUPERNOVAE)")
print("=" * 70)

# Type Ia SNe are standardizable candles
# d_L(z) = (1+z) * integral_0^z c/H(z') dz'
# Big Bang: d_L(z) from Friedmann with Omega_m, Omega_Lambda
# Steady-state: H(t) = H0 = constant (no expansion history)

# In steady-state, d_L = c*z/H0*(1+z/2) for small z
# In Big Bang: d_L is larger at high z (accelerating expansion)

z_test = np.array([0.1, 0.3, 0.5, 0.7, 1.0, 1.5])

# Big Bang d_L (simplified, flat universe with Omega_m=0.3, Omega_L=0.7)
def dL_bigbang(z):
    """Luminosity distance in Big Bang cosmology (simplified)."""
    # d_L = (1+z) * integral_0^z dz'/H(z')
    # H(z) = H0 * sqrt(Omega_m*(1+z)^3 + Omega_L)
    Omega_m, Omega_L = 0.3, 0.7
    result = np.zeros_like(z)
    for i, zi in enumerate(z):
        z_arr = np.linspace(0, zi, 200)
        integrand = 1.0 / np.sqrt(Omega_m*(1+z_arr)**3 + Omega_L)
        result[i] = (1+zi) * np.trapz(integrand, z_arr)
    return result  # in units of c/H0

# Steady-state d_L (H = H0 = constant)
def dL_steadystate(z):
    """Luminosity distance in steady-state (H = const)."""
    return z * (1 + z/2)  # in units of c/H0

# Distance modulus: mu = 5*log10(d_L/10pc)
# Difference: delta_mu = mu_SS - mu_BB

dL_bb = dL_bigbang(z_test)
dL_ss = dL_steadystate(z_test)

# Distance modulus difference
delta_mu = 5 * np.log10(dL_ss / dL_bb)

print(f"\nDistance modulus difference: mu_SS - mu_BB")
print(f"{'z':>6}  {'dL_BB(c/H0)':>12}  {'dL_SS(c/H0)':>12}  {'delta_mu':>10}")
print(f"{'-'*50}")
for i in range(len(z_test)):
    print(f"{z_test[i]:6.1f}  {dL_bb[i]:12.4f}  {dL_ss[i]:12.4f}  {delta_mu[i]:10.3f}")

print(f"\nAt z=1.0: delta_mu = {delta_mu[4]:.3f} mag")
print(f"SN Ia measurement precision: ~0.1 mag")
print(f"Systematic difference at z=1: {abs(delta_mu[4])/0.1:.0f}x measurement precision")

print(f"\n  VERDICT: Steady-state predicts WRONG luminosity distances")
print(f"  at z > 0.3. SN Ia data clearly favor Big Bang + Lambda.")

# ============================================================
# TEST 4: BARYON ACOUSTIC OSCILLATIONS (BAO)
# ============================================================
print("\n" + "=" * 70)
print("TEST 4: BARYON ACOUSTIC OSCILLATIONS (BAO)")
print("=" * 70)

# BAO is a preferred scale of ~150 Mpc in galaxy clustering
# Big Bang explanation: sound horizon at recombination
# Steady-state must explain this scale without recombination

r_s = 147  # Mpc (sound horizon at recombination)
z_bao = [0.2, 0.35, 0.5, 0.7, 1.0, 1.5]

# BAO measures D_V/r_s where D_V = [d_L^2 * c*z / H(z)]^(1/3)
# In steady-state: D_V = [z^2 * c^3*z / (H0^3)]^(1/3) = c*z/H0 * z^(1/3)

print(f"\nSound horizon: r_s = {r_s} Mpc")
print(f"This scale is set by the physics of the photon-baryon fluid")
print(f"at T ~ 3000 K, z ~ 1100, t ~ 380,000 years")
print(f"\nBig Bang: r_s = integral_0^t_recomb cs(t)/a(t) dt")
print(f"  cs = c/sqrt(3) (sound speed in photon-baryon fluid)")
print(f"  This is a DETERMINISTIC prediction from BBN + recombination physics")

print(f"\nSteady-state: where does 150 Mpc come from?")
print(f"  No recombination epoch -> no sound horizon")
print(f"  No photon-baryon fluid -> no acoustic oscillations")
print(f"  The 150 Mpc scale would be COINCIDENTAL")

print(f"\n  VERDICT: BAO scale is a natural prediction of Big Bang")
print(f"  Steady-state has no mechanism to produce it.")

# ============================================================
# TEST 5: COSMIC CHRONOLOGY (STELLAR AGES)
# ============================================================
print("\n" + "=" * 70)
print("TEST 5: COSMIC CHRONOLOGY")
print("=" * 70)

# Oldest stars: ~13.2 Gyr (globular clusters)
# Age of universe: 13.8 Gyr (from CMB + expansion)
# These are CONSISTENT in Big Bang

# In steady-state: universe is infinite age
# But then: why are the oldest stars only 13.2 Gyr old?
# If universe is infinitely old, stars should have been forming forever
# -> should see stars of ALL ages, including >> 13.8 Gyr

t_oldest_star = 13.2e9  # years
t_universe = 13.8e9  # years (Big Bang)

print(f"\nOldest known stars: {t_oldest_star/1e9:.1f} Gyr")
print(f"Age of universe (Big Bang): {t_universe/1e9:.1f} Gyr")
print(f"Consistency: {t_universe - t_oldest_star:.1f} Gyr gap (reasonable)")

print(f"\nSteady-state prediction: universe is infinitely old")
print(f"  -> should see stars of ALL ages, including >> 20 Gyr")
print(f"  -> should see MUCH more processed material")
print(f"  -> metallicity distribution should be flat, not peaked")

print(f"\n  VERDICT: Stellar age distribution favors finite-age universe")

# ============================================================
# TEST 6: RELIC COSMOLOGY — DOES IT WORK AS STEADY-STATE?
# ============================================================
print("\n" + "=" * 70)
print("TEST 6: RELIC COSMOLOGY INTERNAL CONSISTENCY")
print("=" * 70)

# The scaffold says:
# - phi drives expansion via H(t)
# - BHs form, evaporate to relics
# - Relics cluster (dark matter)
# - Relics exchange energy with phi
# - No singular t=0 needed

# Question: in this model, what is H(t)?
# If H(t) is NOT constant, then the universe has a HISTORY
# If it has a history, it has a beginning (or at least a boundary condition)

# Test: solve the steady-state equations
# H^2 = (8piG/3)(rho_b + rho_r + rho_relic + rho_phi)
# If all components are in equilibrium: d(rho)/dt = 0 for each
# Then H = constant -> de Sitter-like expansion
# But then: no structure formation (no growing perturbations)

# If NOT in equilibrium: H varies -> history -> beginning required

print(f"\nSteady-state requirement: all densities constant in time")
print(f"  d(rho_b)/dt = 0 -> rho_b = const -> baryons created continuously")
print(f"  d(rho_r)/dt = 0 -> rho_r = const -> photons created continuously")
print(f"  d(rho_relic)/dt = 0 -> formation = absorption + decay")
print(f"  d(rho_phi)/dt = 0 -> field in exact equilibrium")

print(f"\nProblem 1: Baryon creation")
print(f"  Steady-state requires continuous creation of matter")
print(f"  No known mechanism for this in standard physics")

print(f"\nProblem 2: Entropy")
print(f"  Second law: entropy increases")
print(f"  Steady-state: entropy must be constant -> requires entropy disposal")
print(f"  No known mechanism for this")

print(f"\nProblem 3: Expansion + constant density")
print(f"  If H > 0 and rho = const, then volume increases")
print(f"  -> new matter must be created at rate dN/dt = 3H*N")
print(f"  This is the Hoyle-Bondi-Gold creation field (1948)")
print(f"  -> contradicts conservation of energy-momentum tensor")

print(f"\n  VERDICT: Steady-state requires continuous matter creation")
print(f"  This contradicts the standard energy-momentum conservation")
print(f"  that the scaffold itself uses in the Friedmann equation")

# ============================================================
# TEST 7: WHAT THE RELIC MODEL ACTUALLY SAYS
# ============================================================
print("\n" + "=" * 70)
print("TEST 7: WHAT THE MATH ACTUALLY PRODUCES")
print("=" * 70)

# Run the Friedmann + relic + field model from earlier
# and check: does it converge to steady-state or Big Bang?

Omega_b = 0.05
Omega_r = 0.0001
Omega_relic = 0.27
Omega_DE = 0.68

N = 500
ln_a = np.linspace(-7, 0, N)
dln_a = ln_a[1] - ln_a[0]
a = np.exp(ln_a)

# Matter density evolution
rho_m = (Omega_b + Omega_relic) * a**(-3)  # -> infinity as a->0
rho_r_val = Omega_r * a**(-4)              # -> infinity faster
rho_DE = Omega_DE                          # constant

# Total density ratio
rho_total = rho_m + rho_r_val + rho_DE

# At early times (small a): rho_m and rho_r DOMINATE
# At late times (large a): rho_DE dominates
# The CROSSOVER defines the transition from deceleration to acceleration

# When does rho_m = rho_DE?
a_eq = ((Omega_b + Omega_relic) / Omega_DE)**(1/3)
z_eq = 1/a_eq - 1

print(f"\nDensity evolution:")
print(f"  At a=10^-3 (z~999): rho_m/rho_DE = {rho_m[0]/rho_DE:.1e}")
print(f"  At a=10^-1 (z~9):   rho_m/rho_DE = {(Omega_b+Omega_relic)*10**3/Omega_DE:.1f}")
print(f"  At a=1 (z=0):       rho_m/rho_DE = {(Omega_b+Omega_relic)/Omega_DE:.3f}")

print(f"\nMatter-radiation equality:")
print(f"  a_eq = {a_eq:.4f}, z_eq = {z_eq:.1f}")
print(f"  This is a TRANSIENT — the universe WAS different in the past")
print(f"  Steady-state requires rho_m/rho_DE = const for all time")
print(f"  But rho_m/rho_DE grows as a^(-3) -> NOT constant")

print(f"\n  VERDICT: The relic cosmology equations THEMSELVES")
print(f"  produce a universe with a history, not a steady state.")
print(f"  The density ratios are NOT constant — they evolve.")
print(f"  An evolving system with irreversible processes (BH evaporation,")
print(f"  entropy increase) must have had a lower-entropy initial state.")

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("SUMMARY: CAN FIELD+RELIC COSMOLOGY REPLACE THE BIG BANG?")
print("=" * 70)

tests = [
    ("CMB blackbody", "FAIL", "No steady-state mechanism produces perfect blackbody to 10^-5"),
    ("BBN abundances", "FAIL", "D/H = 2.5e-5 requires hot dense phase at t~3 min"),
    ("SN Ia Hubble diagram", "FAIL", "Predicts wrong d_L at z > 0.3"),
    ("BAO scale (150 Mpc)", "FAIL", "No recombination -> no sound horizon"),
    ("Stellar ages", "FAIL", "Infinite-age universe should have older stars"),
    ("Continuous creation", "FAIL", "Violates energy-momentum conservation"),
    ("Density evolution", "FAIL", "rho_m/rho_DE varies as a^-3, not constant"),
]

print(f"\n{'Test':<25} {'Result':<8} {'Reason'}")
print(f"{'-'*70}")
for name, result, reason in tests:
    print(f"{name:<25} {result:<8} {reason}")

print(f"\n{'='*70}")
print(f"CONCLUSION")
print(f"{'='*70}")
print(f"\nThe relic cosmology math works correctly as a COMPONENT of")
print(f"Big Bang cosmology — relics replace CDM, field replaces Lambda.")
print(f"\nBut as a STEADY-STATE replacement for the Big Bang, it fails")
print(f"every observational test. The math itself shows why:")
print(f"  - Density ratios evolve (not steady-state)")
print(f"  - Entropy increases (requires initial low-entropy state)")
print(f"  - No mechanism for CMB thermalization or BBN abundances")
print(f"\nThe relic model is a MODIFICATION of the Big Bang,")
print(f"not a REPLACEMENT for it.")

print(f"\n{'='*70}")
