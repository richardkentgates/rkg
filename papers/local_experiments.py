"""Local experiments as tests of the framework's own observable.

Framework law:      a = c^2 * d(dtau/dt)/dr
Field:              G = d(dtau/dt)/d(ln r)
Regulated coupling: G_eff = G_0 (1 - c_g G)

Every number is transcribed in local_experiment_data.txt from a published
result. Nothing is fitted and no cosmological input appears. The question
this script answers is narrow and answerable: what does each published
local experiment actually constrain on the framework's free parameter c_g,
and do the constraints agree?

Why local experiments
---------------------
A galaxy at Planck resolution is 7.9e167 cells, which is not computable
(1e147 Gyr at an idealised exascale rate). So galactic prediction is
out of reach with the arithmetic available. It is worth being clear that
this is a resolution limit, not an intelligence limit: the law is local,
so it can be tested wherever a proper-time rate can be read, and that is
in laboratories and on clocks, not in a galaxy.

The three kinds of constraint
-----------------------------
  FIRST derivative   a = c^2 d(dtau/dt)/dr        clocks, gravimeters
  SECOND derivative  curvature of dtau/dt          atom interferometers
  DIFFERENTIAL       two bodies, same place        MICROSCOPE

The second-derivative and differential tests are new here. The corpus has
used clocks only.
"""
import numpy as np
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "local_experiment_data.txt")

# ----------------------------------------------------------------------
# load the transcribed values
# ----------------------------------------------------------------------
D = {}
with open(DATA) as fh:
    for line in fh:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' not in line:
            continue
        k, v = line.split('=', 1)
        k = k.strip()
        v = v.split('#')[0].strip().rstrip(',')
        try:
            D[k] = float(v)
        except ValueError:
            pass

C = D['C_LIGHT']
G_E = D['G_EARTH']
R_E = D['R_EARTH']


def G_at_earth_surface():
    """The framework's field at Earth's surface, from the local potential.

    In the weak field dtau/dt = 1 - Phi/c^2, so
        G = d(dtau/dt)/d(ln r) = Phi/c^2
    and at the surface Phi = -G_E * R_E.
    """
    return G_E * R_E / C**2


def g_from_G(c_g, G):
    """Fractional change in the effective coupling, (1 - c_g G)."""
    return c_g * G


def main():
    print("=" * 78)
    print("LOCAL EXPERIMENTS AGAINST THE FRAMEWORK'S OWN OBSERVABLE")
    print("=" * 78)
    print()
    print("  a = c^2 d(dtau/dt)/dr,   G = d(dtau/dt)/d(ln r),")
    print("  G_eff = G_0 (1 - c_g G)")
    print()
    print("  Every input transcribed from a published result. No fitted")
    print("  parameter, no cosmological input, no mass model.")
    print()

    G_E_surface = G_at_earth_surface()
    print(f"  The field at Earth's surface, G = Phi/c^2:")
    print(f"    G = {G_E_surface:.4e}")
    print(f"    so a coupling c_g = 1 gives a fractional shift in G_eff of")
    print(f"      {g_from_G(1.0, G_E_surface):.4e}")
    print()

    results = []

    # ------------------------------------------------------------------
    # 1. Skytree: first derivative, 450 m
    # ------------------------------------------------------------------
    h = D['SKYTREE_HEIGHT_M']
    a = D['SKYTREE_ALPHA']
    a_sig = D['SKYTREE_ALPHA_SIGMA']
    # alpha is the fractional deviation of the measured rate difference from
    # the zero-correction limit, so it bounds c_g * G directly.
    G_here = G_E_surface
    # The clocks measure a fractional deviation of the rate, and the
    # framework's correction to that rate is c_g * G. So c_g < alpha / G.
    c_g_limit = a_sig / G_here
    results.append(("Skytree 450 m", "first derivative", a_sig, c_g_limit,
                    D['SKYTREE_SIGMA']))
    print("  " + "-" * 74)
    print("  1. SKYTREE, TOKYO  (first derivative, 450 m)")
    print("  " + "-" * 74)
    print(f"    alpha = ({a:.1f} +/- {a_sig:.1f}) e-5")
    print(f"    consistent with the zero-correction limit at {D['SKYTREE_SIGMA']:.2f} sigma")
    print(f"    bounds  c_g * G  <  {a_sig:.2e}")
    print(f"    G = {G_here:.3e} at Earth's surface, so:")
    print(f"      c_g  <  {c_g_limit:.3e}")
    print()

    # ------------------------------------------------------------------
    # 2. PTB - MPQ: first derivative, 457 km
    # ------------------------------------------------------------------
    bl = D['PTB_MPQ_BASELINE_KM'] * 1000.0
    du = D['PTB_MPQ_DU']
    du_sig = D['PTB_MPQ_DU_SIGMA']
    # fractional agreement between two methods
    frac = du_sig / du
    c_g_limit = frac / G_here
    results.append(("PTB-MPQ 457 km", "first derivative", frac, c_g_limit,
                    D['PTB_MPQ_SIGMA']))
    print("  " + "-" * 74)
    print("  2. PTB - MPQ  (first derivative, 457 km)")
    print("  " + "-" * 74)
    print(f"    geopotential difference {du:.1f} +/- {du_sig:.1f} m^2/s^2")
    print(f"    the two methods agree to {D['PTB_MPQ_SIGMA']:.2f} sigma")
    print(f"    fractional agreement {frac:.3e}")
    print(f"      c_g  <  {c_g_limit:.3e}")
    print()

    # ------------------------------------------------------------------
    # 3. Paris - PTB: first derivative, 1415 km, residual vs zero
    # ------------------------------------------------------------------
    res = D['PARIS_PTB_RESIDUAL']
    res_sig = D['PARIS_PTB_SIGMA_VAL']
    # Same structure: fractional residual divided by the field.
    c_g_limit = res_sig / G_here
    results.append(("Paris-PTB 1415 km", "first derivative", res_sig,
                    c_g_limit, 1.0))
    print("  " + "-" * 74)
    print("  3. PARIS - PTB  (first derivative, 1415 km)")
    print("  " + "-" * 74)
    print(f"    residual ({res:.1f} +/- {res_sig:.1f}) e-17, consistent with zero")
    print(f"      c_g  <  {c_g_limit:.3e}")
    print()

    # ------------------------------------------------------------------
    # 4. Overstreet: second derivative, gravity gradient
    # ------------------------------------------------------------------
    dg = D['OVERSTREET_DG_OVER_G']
    syst = D['OVERSTREET_SYST_FRAC']
    # T_zz at Earth's surface is -2 G_E / R_E. The measurement reaches this
    # to a relative dg/g, so the fractional uncertainty on the gradient is dg.
    Tzz = -2 * G_E / R_E
    grad_unc = dg * Tzz
    print("  " + "-" * 74)
    print("  4. OVERSTREET 2018  (second derivative)")
    print("  " + "-" * 74)
    print(f"    dual-species atom interferometer reads T_zz = d^2(dtau/dt)/dz^2")
    print(f"    T_zz at Earth's surface = 2 g / R = {Tzz:.4e} 1/s^2")
    print(f"    relative precision dg/g = {dg:.1e} per shot")
    print(f"    -> uncertainty on T_zz = {abs(grad_unc):.3e} 1/s^2")
    print(f"    systematics suppressed to {syst:.0e} of the signal")
    print()
    print("    This is the framework's observable at second order: the")
    print("    curvature of the time-density rate, read directly by atoms")
    print("    in free fall. The corpus has previously used clocks, which")
    print("    read the first derivative only.")
    print()

    # ------------------------------------------------------------------
    # 5. MICROSCOPE: differential, two bodies at one place
    # ------------------------------------------------------------------
    eta_lim = D['MICROSCOPE_LIMIT']
    sep = D['MICROSCOPE_SEPARATION_CM'] / 100.0
    # eta is the fractional difference in acceleration of two bodies made of
    # different materials, colocated. A field-gradient effect that varies
    # across the 21 cm separation would mimic it.
    # dG/dr ~ G / R, so over sep: dG ~ G * sep / R
    dG_over_sep = G_here * sep / R_E
    c_g_limit = eta_lim / dG_over_sep
    results.append(("MICROSCOPE 21 cm", "differential", eta_lim, c_g_limit, 1.0))
    print("  " + "-" * 74)
    print("  5. MICROSCOPE  (differential, two bodies, 21 cm apart)")
    print("  " + "-" * 74)
    print(f"    eta(Ti,Pt) = {D['MICROSCOPE_ETA']:.1e} "
          f"+/- {D['MICROSCOPE_STAT']:.1e} (stat) +/- {D['MICROSCOPE_SYST']:.1e} (syst)")
    print(f"    no violation at {eta_lim:.1e}")
    print()
    print("    The framework gives two co-located bodies the same dtau/dt and")
    print("    so the same acceleration, predicting eta = 0 exactly. MICROSCOPE")
    print("    is therefore a direct test: any field variation across the")
    print("    21 cm instrument separation would appear as a spurious eta.")
    print(f"    field variation over 21 cm: dG ~ {dG_over_sep:.3e}")
    print(f"      c_g  <  {c_g_limit:.3e}")
    print()

    # ------------------------------------------------------------------
    # 6. Cold-atom gravimeter, measured vertical gradient
    # ------------------------------------------------------------------
    kE = D['AQG_GRAD_K_E'] * 1e-8      # kE = 10 nm/s^2 per cm = 1e-8 1/s^2
    sd = D['AQG_GRAD_SD_K_E'] * 1e-8
    print("  " + "-" * 74)
    print("  6. COLD-ATOM GRAVIMETER, Larzac  (first derivative)")
    print("  " + "-" * 74)
    print(f"    vertical gradient over {D['AQG_HEIGHT_SEP_M']} m: "
          f"{D['AQG_GRAD_K_E']:.3f} +/- {D['AQG_GRAD_SD_K_E']:.3f} kE")
    print(f"    = {kE:.3e} 1/s^2   (1 kE = 1e-8 1/s^2)")
    print(f"    this is -2G/R = {-2*G_E/R_E:.3e} 1/s^2 to "
          f"{abs(kE - (-2*G_E/R_E))/abs(-2*G_E/R_E)*100:.1f}%")
    print()
    print("    A measured Earth gravity gradient, by cold atoms, agreeing")
    print("    with 2G/R. This is an absolute check on the first derivative")
    print("    of dtau/dt using matter rather than clocks.")
    print()

    # ------------------------------------------------------------------
    # 7. Birmingham gradiometer
    # ------------------------------------------------------------------
    sens = D['BIRMINGHAM_SENS_E'] * 1e-9
    print("  " + "-" * 74)
    print("  7. BIRMINGHAM COLD-ATOM GRADIOMETER  (second derivative)")
    print("  " + "-" * 74)
    print(f"    sensitivity {D['BIRMINGHAM_SENS_E']:.0f} E after "
          f"{D['BIRMINGHAM_INTEGRATION_MIN']:.0f} min, 1 E = 1e-9 1/s^2")
    print(f"    = {sens:.2e} 1/s^2")
    print(f"    as a fraction of T_zz = {Tzz:.3e}: {sens/abs(Tzz):.2e}")
    print()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print("=" * 78)
    print("DO THE CONSTRAINTS AGREE?")
    print("=" * 78)
    print()
    print(f"  {'experiment':>18} {'kind':>20} {'c_g <':>12}")
    for name, kind, meas, cg, sig in results:
        print(f"  {name:>18} {kind:>20} {cg:12.3e}")
    print()
    tightest = min(results, key=lambda t: t[3])
    loosest = max(results, key=lambda t: t[3])
    print(f"  tightest constraint: {tightest[0]}  c_g < {tightest[3]:.3e}")
    print(f"  loosest constraint: {loosest[0]}  c_g < {loosest[3]:.3e}")
    print()
    print("  Every one of these is an upper limit, and none requires a nonzero")
    print("  value. Read together they push c_g toward zero, which means the")
    print("  framework is indistinguishable from the limit it reduces to across")
    print("  every local test available. That is the honest result and it is a")
    print("  real limitation, not a confirmation:")
    print()
    print("    None of these experiments distinguishes a = c^2 d(dtau/dt)/dr")
    print("    from a = g. The clocks test the first derivative, the")
    print("    interferometers the second, MICROSCOPE the difference between two")
    print("    co-located bodies, and in all three the framework's prediction")
    print("    coincides with the zero-correction limit. What the data confirm")
    print("    is that the framework passes every test it faces without")
    print("    contradiction, not that the field does anything.")
    print()
    print("  The singularity result does not depend on this. It rests on G")
    print("  diverging at the horizon, so c_g G = 1 is reached for any c_g > 0.")
    print("  A small c_g means the divergence is steep, not that the coupling is")
    print("  absent. The two statements are consistent, and separating them is")
    print("  the work the framework has not yet done.")
    print()
    print("  What would distinguish them. A test in which the field and the")
    print("  mass disagree, rather than a null. The Eotvos result is a null by")
    print("  construction, since the framework gives co-located bodies identical")
    print("  dtau/dt. A measurement of the second derivative at a precision")
    print("  that resolved the difference between c^2 d(dtau/dt)/dr and g would")
    print("  not, and no such measurement exists at present.")
    print()

    out = os.path.join(HERE, "local_experiment_results.txt")
    with open(out, "w") as fh:
        fh.write("# Local experiments against the framework's observable\n")
        fh.write("# Generated by local_experiments.py\n")
        fh.write("# Inputs transcribed in local_experiment_data.txt\n")
        fh.write(f"# G at Earth's surface = {G_E_surface:.6e}\n")
        fh.write(f"# T_zz at Earth's surface = {Tzz:.6e} 1/s^2\n")
        fh.write("#\n")
        fh.write(f"# {'experiment':>18} {'kind':>20} {'c_g_limit':>13}\n")
        for name, kind, meas, cg, sig in results:
            fh.write(f"# {name:>18} {kind:>20} {cg:13.4e}\n")
        fh.write(f"#\n# tightest: {tightest[0]} c_g < {tightest[3]:.4e}\n")
    print(f"  {out} written")


if __name__ == "__main__":
    main()
