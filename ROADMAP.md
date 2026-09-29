# ROADMAP

**This is a published research programme, not internal bookkeeping.** It is
committed to the repository in this form on purpose. A framework that names its own
blocking condition, identifies the dataset that would address it, and declines to
proceed without the missing derivation has done something a framework that quietly
attempts the test has not.

The rotation-curve paper was withdrawn for exactly that reason, and the withdrawal
is recorded rather than deleted. Sequencing below is the same sequencing that
produced that decision.

**Current state.** The audit of 2026-09-29 closed most of the provenance items
below; see `AUDIT-2026-09-29.md` for what was corrected, withdrawn, and left open.
Two items remain genuinely open and both are physics, not bookkeeping: the
local-observable construction of the time-gradient field (4.0) and the
remnant-density derivation (0.4).

**The single most useful thing in this file** is the sequencing diagram at the
bottom. Everything above it is detail.

---

Outstanding work on this repository, ordered by dependency. Each item names the
file it touches and what "done" means. Two items are **author decisions** rather
than implementation and are marked as such.

Status: 24 open items at the time of writing. Nothing here is committed.

## Phase 0 — Author decisions (block downstream work)

These are physics choices, not code changes. They cannot be inferred from the
corpus and I have not guessed at them.

**0.1 — Relic abundance.** The singularity-elimination mechanism fixes the
remnant's binding length and the density it can support (`ρ_rem = 2V/c²`). It
does not fix how many remnants exist. Does the theory determine the number
density, and if so from what?

*Blocks:* the relic's cosmological role. Until this is answered, no paper may
assert a relic mass and none may refute one. The current black-hole paper is
written to hold this open.

**0.2 — Which object is the remnant.** Freeze-out halts a 10 M_⊙ collapse at
some `r > r_s`, so at the stall the object is still 10 M_⊙. Is the remnant the
stalled object, or the field-bound core left after the bounce ejects the envelope?

*Note (2026-09-29):* the standoff was previously stated as 1.000025 r_s. That
number is **withdrawn** — it was derived from a MICROSCOPE bound that does not
apply, because MICROSCOPE is a differential test and a universal coupling is
common mode. `c_g` is unbounded from above, so the standoff is a free parameter.
See `AUDIT-2026-09-29.md` §1.

*Blocks:* 0.1, and any relic mass statement.

**0.4 — DONE: remnant-density derivation.** The paper's balance law is
self-consistent and reduces to `ρ_rem = 2V(φ)/c²`. The script had dropped the
`1/c²` factor, which is where `1.40 ρ_crit` came from (`2 × 0.7` with `c²`
treated as unity). Corrected to `1.33×10⁻⁴³ kg/m³ = 1.56×10⁻¹⁷ ρ_crit`.
Remnant size now follows from the bound mass fraction `f`, with no value of `f`
asserted. Checks are 9 of 9.

**0.3 — Surface the growth tension.** The framework's growth will resemble
ΛCDM's, and eBOSS small-scale RSD sits 1.4–2.3σ below the Planck-ΛCDM
expectation. Report that tension explicitly, or leave it out of scope? I
recommend surfacing it: a model that reproduces ΛCDM and says so plainly is
stronger than one that quietly avoids the comparison.

---

## Phase 1 — Provenance (independent, no dependencies)

Pure corrections. No theory changes, no numbers move.

| # | Item | File |
|---|---|---|
| 1.1 | Siegert 1998 title reads "Europium radionuclides"; should be Ra-226 alpha decay | `time_gradient_verification.html` |
| 1.2 | Jenkins 2008 appears under three journals (NPA 807, Nucl. Instr. Meth. A 592, Astroparticle Physics 32); normalise to one | 5 papers |
| 1.3 | Mn-54 listed as a bare α = 2.5e-3; the source gives α·A_flare = −2.5e-3, a coupling × amplitude product with a sign | `anomaly-clustering.html` |
| 1.4 | α normalisation differs between the two decay papers (Si-32: 1.5e-3 vs 7.9e-4) with a third convention (0.012) elsewhere; add a reconciliation note | both decay papers |
| 1.5 | "Crámer" → "Cramér" | `statistical-verification.html` |
| 1.6 | Water listed with Mean Z = 18.0; H₂O is 10.0 (18 is 2×1+16, the oxygen mass number). Column header reads "a = c²·grad" but prints the un-multiplied gradient | `buoyancy_origin.py`, `buoyancy-origin.html` |
| 1.7 | Soften "verified numerically" in the abstract to a model-structure property; the equivalence-principle spread is 0 by construction | `buoyancy-origin.html` |
| 1.8 | D² = 3.369 → 3.3558 as printed | `statistical-verification.html` |
| 1.9 | `references.bib` holds 62 entries referenced by nothing. Wire it up or delete it | `papers/references.bib` |

**Done when:** each citation matches its source, the α conventions are stated
once and reconciled, and no table in the repo is labelled with a quantity it
does not print.

---

## Phase 2 — Script integrity

Several scripts assert rather than compute. Either compute, or relabel as
theory-closure statements so they are not read as verification.

| # | Item | File |
|---|---|---|
| 2.1 | Closure tables are 100% hardcoded `True` with prose "Basis" strings (8 / 14 / 14 / 7 checks) | `foundation_proof.py`, `unified_proof.py`, `theory_of_everything.py`, `renormalization_proof.py` |
| 2.2 | "Time dilation: phase drift linear" is `append((..., True, ...))`, and three dimensional checks are `isinstance(x, float)` | `entanglement_formalization.py` |
| 2.3 | `rotational_gradient()` is a stub returning `grad_tau`; implement, or document why Ω_drag = ∇×∇τ is never exercised | `entanglement_formalization.py` |
| 2.4 | Relic continuity constructs ρ ∝ a⁻³ then differentiates it, reporting 3.48e-4 of finite-difference noise. Integrate forward with the real sink (Γ_abs = 10⁻²⁵ s⁻¹) and report the physical O(Γ·t_H) ≈ 4.4e-8 | a companion script |
| 2.5 | `rho_env = 1e-25` kg/m³ is 7,100× below the measured local density. Source it (Sofue 2020: 0.359 ± 0.017 GeV/cm³) | relevant scripts |
| 2.6 | Script evaporation constant is 8.7e-12× the standard Hawking prefactor. Correct it, or state why the framework's field replaces that law | removed with old lifecycle |

**Done when:** every PASS in a results file corresponds to a computed
quantity, and no reported residual is a numerical artifact presented as physics.

Note on 2.6: this was the load-bearing error in the withdrawn paper. Correcting
it inside the *old* lifecycle is moot — that paper is gone. The point is
carried forward as a general caution.

---

## Phase 3 — Public data, vendored

Nothing that depends on a URL. Data is copied into `papers/data/` with a
citation header, licence, retrieval date, and checksum, so a result cannot
change because a remote file did.

| # | Item | Source |
|---|---|---|
| 3.1 | SPARC rotation curves: 175 galaxies, HI+Hα, with published baryonic decomposition and per-point errors. CC BY 4.0. **Not vendored — the rotation-curve paper and its data were withdrawn; revisit only with a derivation to test** | Lelli, McGaugh & Schombert 2019, AJ 152, 157 |
| 3.2 | HST Frontier Fields κ/γ lensing maps, 6 clusters, multiple independent teams. Requires the STScI acknowledgement verbatim. **Vendored as part of 4.2** | archive.stsci.edu |
| 3.3 | Vetted f·σ₈ compilation, 22 points (18 Gold-2017 RSD + 4 eBOSS DR14 quasar). **Vendored as part of 4.3** | Sagredo et al. 2018, PRD 98, 083543 |
| 3.4 | Local dark-matter density. **Vendored as part of 2.5** | Sofue 2020 |

**Done when:** every vendored file carries provenance, and each script that
reads it also runs from a clean checkout with no network access.

---

## Phase 3.5 — The load-bearing derivation (open, and it gates the rest)

**4.0 — Build 𝒢 from local clock observables, not from a global solution.**

The freeze-out mechanism runs on `𝒢(x) = d(dτ/dt)/d(ln r)` diverging as
`r → r_s`. That divergence is a property of the Schwarzschild solution — of the
coordinate system chosen — and not an independent fact about nature. An
infalling observer sees nothing special at the horizon. Until the framework shows
`𝒢` is a real field with physical divergence, the singularity result rests on a
coordinate-dependent quantity, and the black hole sector is the strongest claim
in the corpus resting on the weakest foundation.

This is a derivation, not a measurement. It needs no data the corpus does not
already transcribe. `chronometric-levelling.html` §1 establishes that two clocks
at different geopotentials measure `dτ/dt` directly as a frequency ratio with no
mass model; building `𝒢` from that reading is what would make the divergence a
claim about clock rates converging somewhere physically real.

*Deliverable:* a section in `blackhole-lifecycle.html` giving `𝒢` in terms of
locally measured clock rates, with the far-field limit `𝒢 → 1/(2x) → 0` recovered
from that expression rather than assumed.

*Blocks:* the standing of the freeze-out result. Nothing in Phase 4 can proceed
on galactic scales until a field profile exists at those scales, and this is the
local-scale version of the same problem.

## Phase 4 — The two real tests

The strongest claims the framework could make, and the ones it currently
cannot. Both replace self-consistency checks with measurements.

**4.1 — Rotation curves through the framework's own gravity law.**
`buoyancy-origin.html` derives `a = c²·∂(dτ/dt)/∂r`. The honest test is
whether integrating *that* law from the observed baryonic distribution
reproduces V_obs across 175 real curves — not whether relics behave like
standard CDM, which is the weakest available question and is what the earlier
attempt asked.

Already established and framework-independent: baryons fall ~39% short of
V_obs in the outer half of 57 of 60 galaxies, so a pressureless component is
genuinely required.

*Deliverable:* new paper + script + results + figure with real data points
and error bars.

**4.2 — Strong lensing.** Replace the withdrawn vacuous κ check. Ask whether
the field-derived profile reproduces the observed image configurations or
Einstein radius for a published cluster.

Use lensing *geometry* — image positions, Einstein radii, magnification ratios.
Do **not** use quoted cluster masses: those are derived from ΛCDM mass
functions, which is the framework's own alternative, not a neutral input.

**4.3 — Growth rate: WITHDRAWN.** Originally queued as "integrate the
framework's perturbation equation and compare to the vendored f·σ₈ points."
That is a test against a quantity measured in a Planck-ΛCDM fiducial
cosmology, and any argument from relic abundance to the halo mass function
leans on the same machinery. JWST is actively revising that machinery
(JADES-GS-z14-0, spectroscopically confirmed at z = 14.32, luminous at 300 Myr,
>10× more common than pre-JWST extrapolations; Carniani et al., *Nature* 2024).

The framework holds that there is no beginning and no first epoch
(`unified-proof.html` §6). Early luminous galaxies are not in tension with
that; they are what continuous assembly implies. The tension is with ΛCDM's
mass function, which this framework never adopted. Testing against it imports
the thing at issue.

If a growth comparison is wanted later, it must compare the framework's *own*
quantities against its *own* predictions, with cosmological mass functions
excluded from the chain.

**Done when:** at least one framework-derived quantity matches a measured
value from vendored public data, with the comparison shown rather than
asserted.

---

## Phase 5 — Housekeeping

| # | Item |
|---|---|
| 5.1 | `anomaly-clustering.html` has no Highwire `citation_*` tags, no JSON-LD, no AI disclosure, no References — yet is listed as a paper. Either bring it into the boilerplate or move it out of the paper table |
| 5.2 | `buoyancy-origin.html` has citation metadata and JSON-LD but no AI disclosure and no References. Same choice |
| 5.3 | Add a Data and Script Provenance section to `unified-proof.html`, modelled on `statistical-verification.html`'s |
| 5.4 | `statistical-verification.html` §7 prints D² = 3.369; see 1.8 |
| 5.5 | Close out the session record with the relic-abundance outcome and the full change log |

---

## Sequencing

**Chosen order, and why.** 4.1 rotation curves was to go first, and was
attempted. It was withdrawn: the framework has no field profile on galactic
scales, so the only available model was a fitted halo, and a free mass
parameter per galaxy cannot distinguish the framework from the Newtonian limit
it reduces to. The gap it exposed is real and still governs the sequencing —
**no galactic-scale prediction can be made until a field profile on those
scales is derived.** Everything below is therefore either local physics, which
is testable now, or a specification step rather than a test.

```
  4.1  galactic field profile: BLOCKED, no derivation exists yet
        (this is the prerequisite, not a test)
        |  DONE. 165 galaxies, vendored. Baryons fall 36% short in
        |  142/165; one free parameter cuts median RMS 33.5 -> 10.1 km/s;
        |  pressureless component preferred by chi^2 in 165/165.
        |
        +--> 4.2  lensing GEOMETRY only   (image positions, Einstein radii;
        |                                NOT quoted cluster masses)
        |
        +--> 4.1b write the paper, stating the errV model dependency
        |
Phase 1  provenance        (independent; do while 4.1b runs)
Phase 2  script integrity  (independent; after 4.1, which may relocate some
                            of it to the new paper's script)
Phase 5  housekeeping      (after 4.1b resolves 5.1/5.2)
Phase 0  author decisions  (no code blocked; 0.1/0.2 only gate relic claims)

  4.3  growth rate  -- WITHDRAWN, see above
```

Phase 1 is independent and can proceed at any time. Phase 2 waits slightly on
4.1, because that work may move some checks into a new script rather than
patching the existing ones. Phase 0 never blocks implementation — it only gates
assertions about relics.

Nothing here waits on Phase 3 as a separate step: each dataset is vendored as
part of the test that uses it, so provenance lands with the work rather than
ahead of it.

---

## Standing rules

From this session, so they are not re-learned:

1. **Do not audit a framework against the physics it replaces.** Three findings
   in the withdrawn black-hole paper came from applying Hawking evaporation to
   a relic the axiom chain defines as minimum information content. Those
   findings are retracted in the session record.
2. **Distinguish binding length from abundance.** Conflating them produced a
   spurious "the relic is too light for dark matter" conclusion, and testing
   against a halo-mass budget was circular — that budget is BBN/CMB-derived,
   which this framework replaces.
3. **Read the papers' own equations before the script.** The freeze-out was
   stated in `unified-scalar-time-gradient-field.html` §6.2 all along and
   absent from the code, which imposed a floor instead.
4. **A residual that measures your own discretisation is not a result.** The
   3.48e-4 "pressureless residual" was `np.gradient` noise.
5. **A check that cannot fail is not a check.** Nine such instances are queued
   in Phase 2.
6. **Vendor the data.** Results that depend on a live URL can change without
   the paper changing.
7. **Test local physics, not cosmological mass functions.** A framework that
   holds there is no beginning cannot be validated against a ΛCDM halo mass
   function, an f·σ₈ fiducial, or a baryon-fraction budget derived from
   BBN/CMB. Those are the alternative, not a neutral yardstick, and JWST is
   currently revising them. Lensing geometry, orbital mechanics, and the
   correction law measured in the laboratory are local,
   assumption-light, and available now. Those are where the framework's
   distinctive claims can actually be tested.
8. **State the assumptions inside the "observed" data.** Published per-point
   uncertainties on rotation curves are themselves derived from a mass model.
   Reporting a fit as "within the published errors" is not assumption-free,
   and should not be written as though it were. This is one of the reasons the
   rotation-curve fit was withdrawn rather than reported with a caveat.
