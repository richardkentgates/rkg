"""What observed evaporation constraints say about the CLASSICAL MASS description.

The corpus earlier carried a relic mass of 1e-5 M_Pl with no source. That figure
is not a relic mass the framework derives. A black hole is followed as
information, and the remnant is the time-information content of what collapsed,
preserved in full; a mass is a classical description of that content rather than
a quantity the remnant carries. This script reports what the measured limits say
about the mass description, so the record shows exactly what does and does not
follow.

Two questions are kept separate:

  1. Does an object at that mass survive Hawking evaporation at all?
      -> the evaporation horizon, a pure calculation from the lifetime

  2. If emission is arrested by the field, can such objects be abundant?
      -> the measured limits on evaporation-powered populations, which
         constrain abundance independently of the mass-loss mechanism

No value here is invented. Every number is either computed from the Hawking
lifetime or transcribed from a published limit.
"""
import numpy as np
import os

G_NEWt = 6.674e-11
C = 2.998e8
HBAR = 1.054571817e-34
M_Pl = 2.176e-8
T_UNIV = 4.35e17          # s
B_HAWK = HBAR * C**4 / (15360 * np.pi * G_NEWt**2)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "evaporation_constraints.txt")

recs = {}


def load(path=DATA):
    section = None
    with open(path) as fh:
        for raw in fh:
            line = raw.strip()
            if not line:
                continue
            if line.startswith("=="):
                section = line.strip("= ").strip()
                continue
            if line.startswith("#"):
                continue
            key, sep, val = line.partition("=")
            if not sep:
                continue
            key = key.strip()
            val = val.split("#")[0].strip()
            if key and val:
                recs.setdefault(section, {})[key] = val


def d(section, key):
    return float(recs[section][key])


load()

print("=" * 78)
print("THE CLASSICAL MASS DESCRIPTION, AGAINST OBSERVED EVAPORATION LIMITS")
print("=" * 78)
print()
print("  An earlier working carried a mass of 1e-5 M_Pl = %.3e g, with no source."
      % (1e-5 * M_Pl * 1000))
print("  It is not a mass the framework derives. This asks what measured data")
print("  say about that SCALE as a classical mass description of the remnant.")
print()

# ----------------------------------------------------------------------
print("-" * 78)
print("1. THE EVAPORATION HORIZON")
print("-" * 78)
M_eh = (3 * B_HAWK * T_UNIV) ** (1.0 / 3.0)
print(f"  Hawking lifetime   tau = M^3 / (3B),  B = {B_HAWK:.4e} kg^3/s")
print(f"  age of the universe     = {T_UNIV:.3e} s")
print()
print(f"  evaporation horizon M_eh = (3 B t)^(1/3)")
print(f"                        = {M_eh:.4e} kg")
print(f"                        = {M_eh*1000:.4e} g")
print(f"                        = {M_eh/M_Pl:.4e} M_Pl")
print()
m_relic = 1e-5 * M_Pl
print(f"  papers relic        = {m_relic*1000:.4e} g = {m_relic/M_Pl:.2e} M_Pl")
print(f"  ratio relic/horizon = {m_relic/M_eh:.4e}")
print()
print("  The relic sits far below the evaporation horizon: an object that")
print("  loses mass as M^-2 at that mass would have completed evaporation long")
print("  ago. Whether the field arrests that loss is the framework's claim;")
print("  the abundance question below does not depend on the answer.")
print()

# ----------------------------------------------------------------------
print("-" * 78)
print("2. MEASURED LIMITS ON EVAPORATION-POWERED POPULATIONS")
print("-" * 78)
print("  These bound how much dark matter may be in objects below the")
print("  horizon, from the radiation they would emit. They are observations.")
print()
for sect, label in (("VOYAGER1", "Voyager 1 e+/e-"),
                    ("AMS02", "AMS-02 positron fraction"),
                    ("INTEGRAL", "INTEGRAL LMC 511 keV")):
    mlim = d(sect, "mass_limit_g") if "mass_limit_g" in recs[sect] else None
    flim = d(sect, "f_pbh_limit")
    mtxt = f"below {mlim:.0e} g" if mlim else "below the horizon"
    print(f"  {label:26s} f < {flim:8.4f}   {mtxt}")
print()
tightest = min(d(s, "f_pbh_limit") for s in ("VOYAGER1", "AMS02", "INTEGRAL"))
print(f"  tightest measured limit   f < {tightest:.4f}  (i.e. under {tightest*100:.1f}%)")
print()
omega_relic = 0.27
print(f"  The corpus attributes Omega_relic = {omega_relic} to these objects.")
print(f"  Measured ceiling on any evaporation-powered population: {tightest:.4f}")
print(f"  -> short by a factor of {omega_relic/tightest:.1f}")
print()
print("  So a relic population at the assumed abundance cannot be composed of")
print("  objects in the mass range these instruments are sensitive to. The")
print("  abundance and the mass cannot both be as assumed.")
print()
print("  SCOPE: this bound is on populations that RADIATE. A remnant carrying")
print("  information rather than mass-energy, whose emission the field arrests,")
print("  is not subject to these limits. The result above excludes a")
print("  MASS-BEARING relic; it does not exclude an INFORMATION-BEARING one.")
print()

# ----------------------------------------------------------------------
print("-" * 78)
print("3. WHAT THIS DOES AND DOES NOT SETTLE")
print("-" * 78)
print()
print("  SETTLED, by measurement:")
print("    * An abundant population of Hawking-evaporating compact objects")
print("      below ~1e16 g is excluded to better than 1 part in 1000.")
print("    * A mass of 1e-5 M_Pl is far below the evaporation horizon and")
print("      carries no empirical support as a mass description.")
print("    * Omega_relic = 0.27 cannot be supplied by evaporation-powered")
print("      objects of that mass.")
print()
print("  NOT SETTLED, and requiring the framework's own physics:")
print("    * The remnant mass, if the field arrests evaporation. The freeze-out")
print("      condition fixes the FIELD at which collapse stalls; the mass that")
print("      follows depends on the field amplification law under compression,")
print("      which is not yet specified.")
print("    * The abundance. No equation in the corpus produces a number density.")
print()
print("  These two are separate, and both remain open. The data above removes")
print("  the possibility that a relic could be both this light and this common")
print("  while still carrying the mass. See section 4.")
print()

# ----------------------------------------------------------------------
print("-" * 78)
print("4. INFORMATION-BEARING REMNANTS ARE NOT EXCLUDED")
print("-" * 78)
print()
print("  Gravity is the time-density gradient G. A black hole at formation")
print("  holds a Bekenstein information content at its horizon,")
print()
print("      I = 2 pi R E / (hbar c ln 2) = 4 pi G M^2 / (hbar c ln 2)")
print()
print("  which is conservative. Nothing is lost when the field switches")
print("  gravity off at freeze-out; the time-density that the mass was")
print("  supporting transfers to the field, which is what its negative")
print("  stress rho_G + 3P_G < 0 describes. Mass-energy goes into the")
print("  ejecta; preserved time-density stays in the field.")
print()
print("  A remnant that carries information rather than mass-energy carries")
print("  no fixed mass, so it presents no target to a limit of this kind.")
print()
print("  The corpus makes two distinct claims and the data separates them:")
print()
print("    (a) relics are pressureless remnants that cluster as dark matter")
print("        -> needs a remnant MASS. Excluded at the assumed abundance.")
print()
print("    (b) the field is the clustered component; relics mark where")
print("        collapse stalled, and the field carries the energy")
print("        -> needs no remnant mass. Not bound by these limits.")
print()
print("  The Bekenstein content supports (b): under (b) nothing must be")
print("  radiated, and the preservation law is exactly what the mechanism")
print("  delivers. Under (a) that same law is a liability, because a remnant")
print("  of that mass must either radiate or be exotic.")
print()
print("  Under (b) the open question moves from relic mass to field energy")
print("  density. The field carries energy in the framework, and the")
print("  potential used in this corpus is set to 0.7 rho_crit, the value")
print("  fixed by DESI. Relic abundance stops being the constrained quantity.")
print()

# ----------------------------------------------------------------------
out = os.path.join(HERE, "relic_abundance_results.txt")
with open(out, "w") as fh:
    fh.write("# Relic mass and abundance, bounded by observed evaporation limits\n")
    fh.write("# Generated by relic_abundance.py\n")
    fh.write("# Limits transcribed in evaporation_constraints.txt\n")
    fh.write("#\n")
    fh.write("# HAWKING LIFETIME\n")
    fh.write(f"# B_HAWK = {B_HAWK:.6e} kg^3/s\n")
    fh.write(f"# t_universe = {T_UNIV:.6e} s\n")
    fh.write(f"# evaporation_horizon_kg = {M_eh:.6e}\n")
    fh.write(f"# evaporation_horizon_g = {M_eh*1000:.6e}\n")
    fh.write(f"# evaporation_horizon_Mpl = {M_eh/M_Pl:.6e}\n")
    fh.write("#\n")
    fh.write("# CORPUS RELIC\n")
    fh.write(f"# relic_mass_kg = {m_relic:.6e}\n")
    fh.write(f"# relic_mass_g = {m_relic*1000:.6e}\n")
    fh.write(f"# relic_over_horizon = {m_relic/M_eh:.6e}\n")
    fh.write(f"# assumed_omega_relic = {omega_relic}\n")
    fh.write("#\n")
    fh.write("# MEASURED LIMITS ON EVAPORATION-POWERED POPULATIONS\n")
    for sect, label in (("VOYAGER1", "voyager1"),
                        ("AMS02", "ams02"),
                        ("INTEGRAL", "integral")):
        mlim = d(sect, "mass_limit_g") if "mass_limit_g" in recs[sect] else None
        fh.write(f"# {label}_mass_limit_g = {mlim if mlim else 'n/a'}\n")
        fh.write(f"# {label}_f_limit = {d(sect,'f_pbh_limit'):.6f}\n")
    fh.write(f"# tightest_f_limit = {tightest:.6f}\n")
    fh.write(f"# omega_relic_over_tightest = {omega_relic/tightest:.6f}\n")
print(f"\n  {os.path.basename(out)} written")
