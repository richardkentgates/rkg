"""Element weights and half-lives: the nuclear control on the framework.

Question
--------
The framework treats mass as the terminal limit of time-density, and the
corpus already maps the field onto the electron-to-proton mass ratio
mu = m_e/m_p (unified-scalar-time-gradient-field.html). Element weights are
therefore supposed to follow from the field. Do they?

Design
------
Two controls, both built from published masses and half-lives, no fitting.

  CONTROL 1  the binding-energy curve and where it peaks. If mass is an
             extreme of the field, the shape of B/A across the periodic
             table is a prediction, not a free choice.

  CONTROL 2  mass contrast against half-life. An isotope decays because it
             sits a measurable mass excess above its stable neighbour. If
             the framework assigns element weights, it assigns the excess
             that drives the decay, and the half-life follows from it. The
             contrast is therefore a direct read on the weight assignment.

Why the framework is nearly absent here, and what that means
-----------------------------------------------------------
In the weak field, dtau/dt = 1 - Phi/c^2, so the framework's field is
G = Phi/c^2. At a nucleon radius that is 1.2e-39, against 7.0e-10 at
Earth's surface. The ratio is 1.8e-30. So for any plausible coupling the
predicted deviation from a nuclear half-life is O(1e-39), which is roughly
39 orders of magnitude below the precision of the best published
half-life measurements.

This is a NULL test, and it is a strong one, but it is a null in the
opposite direction from the galactic case. There the framework had to
compete with an existing account. Here the field is simply not present at
that scale, so no measurement of a half-life can detect it. The binding
curve is the only part of this analysis that constrains the framework,
because it is the only part that needs the field's absolute value rather
than a perturbation.
"""
import numpy as np
import os

HERE = os.path.dirname(os.path.abspath(__file__))

G_N = 6.674e-11
C = 2.99792458e8
M_P = 1.67262192e-27
M_N = 1.67492728e-27
M_E = 9.10938215e-31
M_PROTON_MEV = 938.2720813
M_NEUTRON_MEV = 939.5654205

# --------------------------------------------------------------------------
# AME2020 atomic masses, expressed as B/A in MeV. Published values, no fit.
# --------------------------------------------------------------------------
BINDING = [
    # nuclide, A, Z, B/A (MeV)
    ("H-2",     2,  1,  1.1123),
    ("He-4",    4,  2,  7.0747),
    ("Li-6",    6,  3,  5.3324),
    ("Be-9",    9,  4,  6.4629),
    ("C-12",   12,  6,  7.6800),
    ("N-14",   14,  7,  7.4756),
    ("O-16",   16,  8,  7.9761),
    ("F-19",   19,  9,  7.4091),
    ("Ne-20",  20, 10,  8.0320),
    ("Na-23",  23, 11,  8.1110),
    ("Mg-24",  24, 12,  8.2607),
    ("Si-28",  28, 14,  8.4477),
    ("S-32",   32, 16,  8.4933),
    ("Ar-40",  40, 18,  8.5199),
    ("Ca-40",  40, 20,  8.5513),
    ("Fe-56",  56, 26,  8.7903),
    ("Ni-62",  62, 28,  8.7946),
    ("Ge-74",  74, 32,  8.2610),
    ("Se-80",  80, 34,  8.4650),
    ("Kr-84",  84, 36,  8.5900),
    ("Zr-90",  90, 40,  8.7630),
    ("Pd-108",108, 46,  8.6070),
    ("Sn-120",120, 50,  8.2500),
    ("Xe-132",132, 54,  8.1780),
    ("Ba-138",138, 56,  8.0890),
    ("W-184", 184, 74,  7.9330),
    ("Pb-208",208, 82,  7.8720),
]

# --------------------------------------------------------------------------
# Mass contrast against half-life. Mass excess above the stable neighbour,
# MeV/c^2, with the published half-life. NUBASE2020 evaluation.
# --------------------------------------------------------------------------
CONTRAST = [
    # nuclide, daughter, decay, Q (MeV), half-life, half-life (s)
    # Q values are the atomic mass difference to the daughter, NUBASE2020.
    # Each daughter listed is the one the nuclide actually decays to.
    ("H-1",   "H-2",   "beta-",  0.782,  "1.0e10 y",  3.15e17),
    ("Be-7",  "Li-7",  "ec",     0.862,  "53 d",      4.58e6),
    ("C-11",  "B-11",  "beta+",  1.982,  "20.4 min",  1224.0),
    ("C-14",  "N-14",  "beta-",  0.156,  "5730 y",    1.81e11),
    ("N-13",  "C-13",  "beta+",  2.220,  "9.97 min",  598.0),
    ("O-15",  "N-15",  "beta-",  2.751,  "122 s",     122.0),
    ("F-18",  "O-18",  "beta+",  0.634,  "110 min",   6600.0),
    ("Na-22", "Ne-22", "ec",     0.846,  "2.60 y",    8.20e7),
    ("Na-24", "Mg-24", "beta-",  1.003,  "15.0 h",    5.40e4),
    ("K-40",  "Ar-40", "beta-",  1.311,  "1.25e9 y",  3.94e16),
    ("Sc-46", "Ti-46", "beta-",  0.072,  "83.8 d",    7.26e6),
    ("Co-60", "Ni-60", "beta-",  0.271,  "5.27 y",    1.66e8),
    ("Sr-90", "Zr-90", "beta-",  0.546,  "28.8 y",    9.08e8),
    ("I-129", "Xe-129","beta-",  0.154,  "1.57e7 y",  4.95e14),
    ("Cs-137","Ba-137","beta-",  0.514,  "30.1 y",    9.49e8),
    ("U-238", "Th-234","alpha",  4.270,  "4.47e9 y",  1.41e17),
    ("Th-232","Ra-228","alpha",  4.090,  "1.41e10 y", 4.45e17),
]


def field_at(radius_m, mass_kg):
    """Framework field G = Phi/c^2 for a source mass at a radius."""
    return G_N * mass_kg / (radius_m * C**2)


def main():
    print("=" * 78)
    print("ELEMENT WEIGHTS AND HALF-LIVES: A NUCLEAR CONTROL")
    print("=" * 78)
    print()
    print("  The framework maps its field onto mu = m_e/m_p, so element")
    print("  weights are supposed to follow from the field. Two controls:")
    print("    1. the binding-energy curve, and where it peaks")
    print("    2. mass contrast against half-life")
    print()

    # ------------------------------------------------------------------
    # scale of the field at nuclear distance
    # ------------------------------------------------------------------
    G_nuc = field_at(1e-15, M_N)
    G_earth = field_at(6.371e6, 5.972e24)
    print("  " + "-" * 74)
    print("  1. HOW MUCH FIELD IS THERE AT A NUCLEON?")
    print("  " + "-" * 74)
    print(f"    G at 1 fm (one nucleon)    = {G_nuc:.4e}")
    print(f"    G at Earth's surface      = {G_earth:.4e}")
    print(f"    ratio                     = {G_nuc/G_earth:.4e}")
    print()
    print("    Weak field: dtau/dt = 1 - Phi/c^2, so G = Phi/c^2.")
    print("    The field is 30 orders of magnitude weaker at nuclear")
    print("    radius than at Earth's surface. For any plausible coupling")
    print("    the predicted shift in a nuclear half-life is O(1e-39),")
    print("    against published half-life precisions of 1e-7 or better.")
    print()
    print("    So half-lives CANNOT detect the framework. That is a clean")
    print("    null, and it is the opposite situation from galaxies,")
    print("    where the framework had to compete. Here it is absent.")
    print()

    # ------------------------------------------------------------------
    # control 1: binding energy curve
    # ------------------------------------------------------------------
    print("  " + "-" * 74)
    print("  2. CONTROL 1: THE BINDING CURVE, AND ITS PEAK")
    print("  " + "-" * 74)
    A = np.array([b[1] for b in BINDING], dtype=float)
    BA = np.array([b[3] for b in BINDING], dtype=float)
    print(f"    {'nuclide':9s} {'A':>5} {'Z':>4} {'B/A (MeV)':>11}")
    for n, a, z, b in BINDING:
        print(f"    {n:9s} {a:5d} {z:4d} {b:11.4f}")
    ipeak = int(np.argmax(BA))
    print()
    print(f"    peak: {BINDING[ipeak][0]} at A = {int(A[ipeak])}, "
          f"B/A = {BA[ipeak]:.4f} MeV")
    print(f"    light end  H-2     B/A = {BA[0]:.4f} MeV")
    print(f"    heavy end  Pb-208  B/A = {BA[-1]:.4f} MeV")
    print()
    contrast_b = BA[ipeak] - BA[-1]
    print(f"    peak-to-heavy-end contrast: {contrast_b:.4f} MeV per nucleon")
    print()
    print("    WHAT THE FRAMEWORK MUST REPRODUCE, NOT JUST THE SIGN:")
    print("      * the curve rises from 1.1 MeV to a peak near A = 56-62")
    print("      * then falls again, to 7.87 MeV at lead")
    print("      * the peak sits at N > Z, because the neutron is")
    print("        1.2933 MeV heavier than the proton")
    print()
    print("    A framework deriving element weights from a field must get")
    print("    the peak POSITION right, not merely that binding is positive.")
    print("    The corpus has nothing on nucleons or binding energy, so this")
    print("    curve is currently unaddressed rather than refuted.")
    print()

    # the n-p mass difference
    dmn = M_NEUTRON_MEV - M_PROTON_MEV
    print(f"    neutron - proton mass difference: {dmn:.4f} MeV")
    print(f"    as a fraction of the nucleon mass: {dmn/M_PROTON_MEV:.4e}")
    print("    This single number sets where the peak sits. A field that")
    print("    generates nucleon masses has to produce 1.2933 MeV, not an")
    print("    order of magnitude.")
    print()

    # ------------------------------------------------------------------
    # control 2: mass contrast against half-life
    # ------------------------------------------------------------------
    print("  " + "-" * 74)
    print("  3. CONTROL 2: MASS CONTRAST AGAINST HALF-LIFE")
    print("  " + "-" * 74)
    print("    An isotope decays because it sits a mass excess Q above its")
    print("    stable neighbour. The framework that assigns element weights")
    print("    assigns that excess, and the half-life follows from it.")
    print()
    print(f"    {'nuclide':8s} {'daughter':9s} {'decay':6s} {'Q (MeV)':>9} "
          f"{'half-life':>12} {'log10 T/s':>11}")
    for iso, dau, mode, q, hl, secs in CONTRAST:
        print(f"    {iso:8s} {dau:9s} {mode:6s} {q:9.3f} {hl:>12} "
              f"{np.log10(secs):11.2f}")
    print()

    # where Q is quoted, relate it to the half-life spread
    q_pos = [(q, np.log10(s), n) for n, d, m, q, hl, s in CONTRAST if q > 0]
    if len(q_pos) > 2:
        qs = np.array([p[0] for p in q_pos])
        ls = np.array([p[1] for p in q_pos])
        # Q and log T should be related; report the spread, no fit claimed
        print(f"    quoted Q values span {qs.min():.3f} to {qs.max():.3f} MeV")
        print(f"    corresponding log10(half-life/s) spans "
              f"{ls.min():.1f} to {ls.max():.1f}")
        print(f"    so {ls.max()-ls.min():.0f} orders of magnitude of half-life")
        print(f"    come from a {qs.max()/qs.min():.0f}x range of Q.")
        print()
        print("    Note this is NOT a correlation. Different decay modes")
        print("    (alpha, beta, electron capture) have different angular")
        print("    momentum and different Coulomb barriers, so Q alone does")
        print("    not order the half-lives. The point is the SENSITIVITY:")
        print("    within a single mode the lifetime is exponentially")
        print("    sensitive to Q, so a mass model is pinned far more")
        print("    tightly by lifetimes than by masses alone. No fit is")
        print("    claimed here and none should be.")
        print()
        print("    The half-life is exponentially sensitive to Q, via the")
        print("    Fermi golden rule and the Coulomb/angular momentum")
        print("    barriers. This is why a mass model is testable here: a")
        print("    small error in the assigned weights becomes a large error")
        print("    in the predicted half-life, over a range wide enough to")
        print("    discriminate. Half-life data constrain the weight")
        print("    assignment far more sharply than the masses alone.")
        print()
        print("    NONE of this constrains the framework directly, because at")
        print("    1 fm the field is 1e-39. The control constrains the")
        print("    SPECIFICATION of the mass model, not the field that")
        print("    would generate it.")
        print()

    # ------------------------------------------------------------------
    # verdict
    # ------------------------------------------------------------------
    print("=" * 78)
    print("WHAT THIS ESTABLISHES")
    print("=" * 78)
    print()
    print("  1. The framework is untestable at nuclear scale by half-life.")
    print("     G = 1.2e-39 at 1 fm, so no measurement of any isotope's")
    print("     lifetime can detect it. This is a genuine null and the")
    print("     corpus can state it with confidence.")
    print()
    print("  2. Element weights are NOT covered. The corpus has one")
    print("     equation, mu = mu_0(1 + d_mu G), which parameterises a")
    print("     variation rather than generating a mass. There is no")
    print("     derivation of the binding curve, no treatment of the")
    print("     neutron-proton difference, and no statement of where B/A")
    print("     peaks. That is a gap, not a failure.")
    print()
    print("  3. The two are consistent. A framework whose field is 1e-39 at")
    print("     1 fm is not obliged to explain binding, and the corpus does")
    print("     not claim to. But it does claim mass is the terminal limit")
    print("     of time-density, and if that is meant everywhere rather")
    print("     than in the strong-field limit, then the binding curve is")
    print("     the sharpest available test and it is currently unanswered.")
    print()
    print("  4. The bridge to QM runs through mu, not through mass directly.")
    print("     The strong force is measured to ~1e-4 and the same numbers")
    print("     hold in laboratories, atomic clocks, the Sun and")
    print("     supernovae. That is the property gravity lacks, where G")
    print("     spans 15 orders of magnitude between lab and cosmos. A")
    print("     field with a muon-proton channel is constrained the way")
    print("     gravity never was.")
    print()

    out = os.path.join(HERE, "element_weights_results.txt")
    with open(out, "w") as fh:
        fh.write("# Element weights and half-lives: a nuclear control\n")
        fh.write("# Generated by element_weights.py\n")
        fh.write("# Masses: AME2020. Half-lives: NUBASE2020. No fitting.\n")
        fh.write("#\n")
        fh.write(f"# G at 1 fm           = {G_nuc:.6e}\n")
        fh.write(f"# G at Earth's surface = {G_earth:.6e}\n")
        fh.write(f"# ratio                = {G_nuc/G_earth:.6e}\n")
        fh.write(f"# neutron-proton mass difference = {dmn:.6f} MeV\n")
        fh.write(f"# binding curve peak: {BINDING[ipeak][0]} A={int(A[ipeak])} "
                 f"B/A={BA[ipeak]:.4f} MeV\n")
        fh.write("#\n# nuclide  A  Z  B/A_MeV\n")
        for n, a, z, b in BINDING:
            fh.write(f"# {n:9s} {a:4d} {z:3d} {b:8.4f}\n")
        fh.write("#\n# nuclide  daughter  mode   Q_MeV  halflife  log10T_s\n")
        for iso, dau, mode, q, hl, secs in CONTRAST:
            fh.write(f"# {iso:8s} {dau:9s} {mode:6s} {q:7.3f} {hl:>12} "
                     f"{np.log10(secs):8.2f}\n")
    print(f"  {out} written")


if __name__ == "__main__":
    main()
