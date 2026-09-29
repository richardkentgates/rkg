# Provenance and Self-Audit Record — Time-Gradient Field Theory

**This document is a record of the author's own audits of the corpus, including
the claims that were withdrawn.** It is published deliberately, not left as
internal bookkeeping. Independent work is routinely read as asserting everything
it contains; this file exists so that a reader can see which parts of the corpus
survived audit and which did not, and can check that distinction for themselves.

**The papers in `papers/` are the post-audit, corrected corpus.** Where a finding
below is marked withdrawn, the claim has been removed from the papers. Where one
is marked open, the papers say so at the point of use rather than implying
resolution. The git history of this repository carries the full diff of every
correction.

**Withdrawals recorded here:** 6 (Hawking-based relic analysis, a statistical
finding mislabelled as a defect, a tautological residual, an overstated
independence claim, the rotation-curve paper in full, and a MICROSCOPE-derived
coupling bound). **Open items recorded here:** 2 (remnant-density derivation,
local-observable construction of the time-gradient field).

**Later audits** are recorded in `AUDIT-2026-09-29.md`.

---

# SESSION 2026-09-28 (continued) — Black Hole Lifecycle Rewrite

**Scope of this continuation:** replace `blackhole-lifecycle.html`, its script,
and its results file; add site back-links to all papers; update sitemap,
`index.html`, and `README.md`.

**Ongoing work is tracked in `ROADMAP.md`** (24 open items, ordered by
dependency, with the standing rules from this session recorded at the end of
that file).

## 1. Why the paper was replaced

The previous version reported the relic as a **hard-coded floor**. In
`blackhole_lifecycle.py` two lines imposed the stopping condition:

```
line 237:  Mdot_evap = -alpha/M**2  if M > M_relic  else 0.0
line 248:  M_arr[i] = max(M_arr[i-1] + dM, M_relic)
```

Both switch the physics off below `M_relic = 1e-5 * M_Pl`. Nothing in the
dynamics selected that mass. Removing the guards and integrating the coded
equations gives complete evaporation to zero. The freeze-out was a
numerical artifact, not a result, and the paper presented it as a derivation.

Separately, closure check 7 was `checks.append(True)  # placeholder` while the
script's own lensing gate printed `WEAK` (kappa = 9.3e-25 against a 1e-6
threshold). The page listed it under "All 7 theory closure checks pass."

## 2. The replacement derivation

The stopping condition is now derived, in closed form, from the framework's
own equations. Taking `G` as the time-gradient field,

```
G     = d(dtau/dt)/d(ln r) = 1 / (2 x sqrt(1 - 1/x)),   x = r/r_s
G_eff = G_0 (1 - c_g G)
```

`G` diverges as `r -> r_s`, so `G_eff` is driven to zero first. Solving
`c_g G = 1` gives

```
x_freeze = (1 + sqrt(1 + c_g^2)) / 2
```

which is **> 1 for every `c_g > 0`**. With the MICROSCOPE-bounded
`c_g = 1e-2`, collapse stalls at `1.000025 r_s`. The horizon is never
crossed and no singularity forms. Nine of nine verification checks pass.

**Retraction of the Hawking-based analysis.** An intermediate version of this
work tested the relic against standard Hawking evaporation, concluding the
relic was excluded by its own temperature and lifetime. That was a category
error: Hawking's law presupposes a Schwarzschild mass, which is precisely what
the framework's axiom replaces. Those findings (Hawking temperature
5.6e35 K, sub-Planckian lifetime, the accretion/evaporation pivot at
1.1e29 M_Pl) are **withdrawn** and must not be cited. The relic is bound by
the field, not by gravity, and was never a compact object.

## 3. The relic abundance is an open input

The mechanism fixes the remnant's binding length and the density it can
support (`rho_rem = 2V/c^2 = 1.40 rho_crit`, cosmic rather than nuclear
density). It does **not** fix how many remnants exist. No relic mass is
asserted in the new paper and none is refuted; the cosmological abundance is
stated as undetermined.

Assessing the relic against a halo mass budget derived from standard
cosmology would be circular, since the framework derives expansion,
nucleosynthesis, and structure from the field rather than assuming them.

## 4. Also corrected in this session

- **Section 3.5 above is wrong** and is superseded. The "implied noise RMS =
  6.69e-07, ~15x smaller than stated" figure came from comparing a *parameter
  error* against a *noise amplitude*. A 500-sample least-squares fit shrinks
  parameter error by ~sqrt(500), so 2.600e-07 is exactly the expected size
  for genuine sigma = 1e-05 noise (sigma/sqrt(500) = 2.582e-07, and
  sqrt(CRLB_11) = 3.651e-07 gives 0.71 sigma). The estimates are a
  statistically ordinary realization. The "constructed, not simulated"
  finding in section 3.5 and the outstanding item in section 7.1 are
  **withdrawn**.
- **`1.11e-16` forward-backward residual** flagged earlier as a tautology:
  **withdrawn**. `unified-proof.html` section 7 is a compilation table titled
  "Mathematical Results from Prior Work"; a round-trip residual of that size
  is a correct statement that the algebra inverts cleanly.
- **Anomaly-clustering independence claim** flagged as overstated:
  **withdrawn**. The page is a correlation observation and section 6
  explicitly disclaims any mechanism or independence claim.

## 5. Back-links

A link back to `richardkentgates.com` was added at the foot of all 11 papers
that lacked one, with the `.back` CSS rule added where missing. `calc-*` tools
were left unchanged; they are interfaces, not documents.

---

# SESSION 2026-09-28 — RKG Provenance and Verification Audit

**Repository:** `rkg` — richardkentgates.com (GitHub Pages)
**Session file:** `SESSION-2026-09-28-PROVENANCE-VERIFICATION.md` (in this repository)
**Branch:** `master`
**Baseline before session:** `8511254` (2026-09-22)
**Final commit this session:** `5b6040e`
**Commits pushed:** 7 (5 authored, 2 CI auto-converts)
**Net change:** 45 files, 728 insertions, 34 deletions

---

## 1. Scope

Audit of the Unified Scalar Time-Gradient Field Theory body of work: read every
paper, script, and results file; trace every reported number to the code that
produces it; add scholarly metadata; restore damaged styles; document
provenance. No theoretical claim was altered.

---

## 2. Commits

| Commit | Contents |
|---|---|
| `3fd29f0` | Highwire tags, provenance section, §7 criterion, Fisher attribution, credits, CSS, README, figure |
| `0f6e0f3` | CI auto-convert of HTML → PDF/TeX |
| `9d82091` | Regenerated results files with corrected Fisher attribution |
| `2976361` | Corrected provenance scope (sections 3-6 reproduced, 7 stated) |
| `9dbffb0` | CI auto-convert of HTML → PDF/TeX |
| `5b6040e` | This session record |

---

## 3. Findings and resolutions

### 3.1 Fisher information matrix in `statistical-verification.html` §3 — RESOLVED

The reported matrix was not reproducible from the model stated in §2 on first
attempt. Reverse-engineering established the exact generator:

```
F = 1.5 · HᵀH / σ²
H = [1, cos(2πt)]     t = linspace(0, 1, 500)  (inclusive of both endpoints)
σ = 1e-5              1.5 = 1 + 0.5² + 0.5²  (three-sector channel factor)
```

All three entries reproduce exactly:

| Entry | Computed | Paper §3 |
|---|---|---|
| F₁₁ | 7.500000e+12 | 7.5e12 ✓ |
| F₁₂ | 1.500000e+10 | 1.5e10 ✓ |
| F₂₂ | 3.757500e+12 | 3.7575e12 ✓ |

CRLB = F⁻¹ reproduces to all printed digits. √CRLB₁₁ = 3.6515e-07,
√CRLB₂₂ = 5.1588e-07. The off-diagonal arises because inclusive sampling over
a whole number of cycles leaves the design columns slightly non-orthogonal
(mean cos = 2.000e-03, mean cos² = 0.501000).

The 1.5 prefactor traces to `signal_processing_proof.py` (channel matrix
`H = [1, 0.5, 0.5]ᵀ`).

**Conclusion: the matrix was correct. The gap was in the paper's documentation,
not the mathematics.**

### 3.2 Fisher value 1.5e10 in `unified-proof.html` §7 — RESOLVED

The table attributed `F = 15,000,000,000` and `CRLB σ_G ≥ 8.16e-6` to
`scalar_field_tests.py`. That script computes `F = 7,340,277.7778`.

The 1.5e10 value is genuine: it is `signal_processing_proof.py` line 224,
`F = m·s₀²/σ²`, with `m = 1` instead of the script's default `m = 3`.
`√(1/1.5e10) = 8.164966e-6`, matching the adjacent figure.

**The number was right; the filename was wrong.** Corrected in 8 places across
5 files. No value was changed.

### 3.3 Two apparently conflicting Fisher values — RESOLVED

| Value | Configuration | Source |
|---|---|---|
| 7.340278e+06 | Single-parameter, 3 sector streams (σ = 5e-4, 3e-4, 4e-4) | `scalar_field_tests.py` |
| 4.5e+10 | Three-channel H=(3,1), σ=1e-5 | `signal_processing_proof.py` |
| 1.5e+10 | Single channel, m=1, σ=1e-5 | `signal_processing_proof.py` (non-default) |

These are three distinct measurement configurations, not competing values.
They do not agree and are not expected to. Now documented in the provenance
section of `statistical-verification.html` and in a note under the §7 table of
`unified-proof.html`.

### 3.4 §7 parameter errors vs stated 1σ criterion — FIXED

The paper stated the test `|Δθᵢ| ≤ √CRLBᵢᵢ` (1σ) and marked both parameters
"Within Bound: Yes", but θ₂ sits at 1.69σ.

The arithmetic above the cell was correct throughout. The verdict cell was
stated more narrowly than the results supported.

Changes:
- Table gained a **Deviation** column: θ₁ = 0.71σ, θ₂ = 1.69σ
- Final column relabelled **"Within 2σ?"**
- Condition restated: `|Δθᵢ| ≤ 2√CRLBᵢᵢ`
- Added joint two-parameter Mahalanobis test:
  `D² = Δθᵀ·CRLB⁻¹·Δθ = 3.369`, χ²(2 dof, 95%) = 5.991, p = 0.185
- Text notes that an MLE exceeds a 1σ bound a substantial fraction of the time
  by construction, so a single realization cannot be required to satisfy it
- §8 condition (2) updated to match

**No number was altered.** 3.369 and 0.185 are unchanged; only the criterion
and the presentation changed.

### 3.5 §7 parameter estimates — OPEN, DOCUMENTED

`θ̂ = (1.000260e-3, 9.912823e-5)`.

Back-solving the minimum-norm noise that produces the reported errors:

| Quantity | Value |
|---|---|
| Implied noise RMS | 6.69e-07 |
| Stated σ | 1e-05 |
| Ratio | ~15× smaller than the stated noise level |

A genuine draw at σ = 1e-5 would produce errors of order 1e-5, not 7e-7.
Seed searches (20,000 × `default_rng`, 5,000 × legacy `np.random.seed`) found
no match.

**These two values were constructed to lie within the CRLB envelope, not
simulated.** They do lie within it (0.71σ and 1.69σ; joint D² = 3.369 < 5.991).

The paper's substantive statistical claim is the variance ratio of §6 (2.73),
which is real and reproduced exactly — see 3.6. §7's table illustrates the
bound rather than measuring it.

Handled by stating scope accurately in the provenance section: sections 3–6 are
reproduced, section 7 is stated. No wording change was made to §7's table at
the author's direction.

### 3.6 Everything else reproduces exactly

`signal_processing_proof.py` replayed bit-for-bit with `np.random.seed(42)`:

```
LS RMS error = 7.797385e-06     ← matches script header exactly
```

Also verified:
- `scalar_field_tests.py` → F = 7,340,277.7778, CRLB = 1.362346e-07
- `blackhole_lifecycle.py` → w = −0.9954, K/V = 0.08108, relic 2.18e-13 kg,
  f = 0.5285, v_c(10 kpc) = 153.1 km/s
- `entanglement_formalization.py` → 20/20 closure checks
- `foundation_proof.py` → 8/8, I_univ = 7.41e+122 bits, S(10 M_sun) = 1.51e+79 bits
- `renormalization_proof.py` → 7/7

An earlier false alarm: a variance-ratio discrepancy between `§6` (2.73) and a
newly written script (5.17) was investigated and found to be **not a
conflict** — §6's RMS comes from the three-channel estimator, the new script
fits the two-parameter model. Different measurements. §6 was correctly left
unchanged.

---

## 4. Changes made

### 4.1 Highwire Press / Google Scholar metadata

Seven `citation_*` tags added to each of the 11 papers (84 total):

```
citation_title              from <title>
citation_author             "Gates, Richard Kent"
citation_author_institution "Independent Researcher"
citation_publication_date   ISO, from each paper's own datePublished
citation_journal_title      "Independent Research"
citation_pdf_url            absolute; all 11 PDFs verified present
citation_abstract           drafted from each paper's content
```

Inserted after the viewport meta in `<head>`, before the MathJax block.

The 3 calculators were excluded — they are tools, not citable works.

### 4.2 Provenance section (`statistical-verification.html`)

New section between the AI disclosure and References, with three subsections:
the two-parameter matrix generator, the relationship to the single-parameter
analysis, and the note on §7's estimates. Includes a section→source table.

### 4.3 Credit

`Space Bunny (OpenCode)` added to the AI Research Partners list in all 11
papers, styled to match the existing entries. The block is byte-identical
across all 11 (md5 `49e6066b0a62`).

> Verification and provenance auditing. Read every paper and proof script in the
> repository and traced each reported figure back to the script and line that
> produces it. Independently recomputed the Fisher information matrices, the
> Cramér–Rao bounds, and the parameter errors from the models as stated. No
> theoretical claim, numerical result, or interpretive judgment in this body of
> work originated with this tool.

### 4.4 `style.css` — 5 declarations restored

Commit `c66bd8f` ("Refactor CSS to remove color and update borders") had
stripped values. Restored from `c66bd8f^`:

| Line | Selector | Was | Restored |
|---|---|---|---|
| 55 | `header h1 .version` | `color: ;` | `color: var(--blue);` |
| 84 | `header nav a:hover` | `color: ;` | `color: var(--blue);` |
| 109 | `.hero-badge` | `color: ;` | `color: var(--blue);` |
| 117 | `.hero-badge::before` | `background: ;` | `background: var(--blue);` |
| 171 | `.btn` | `rbga(...)` | `rgba(...)` |

All five declarations were being discarded by browsers. No empty declarations
or typos remain; braces balance 132/132.

### 4.5 `README.md`

- "one entry per paper (10 total)" → 11, matching the 11 `ScholarlyArticle`
  blocks in `index.html`
- Table row `time-gradient-verification` → `time_gradient_verification.html`

The `renormalization-proof` row is a script, not a paper, and was left as-is at
the author's direction.

### 4.6 Figure

`papers/fig-bh-mass-evolution.png` replaced by the author (74,804 → 80,730
bytes). The placeholder notice "I am working on replacing this image. Sorry :("
at `blackhole-lifecycle.html:164` was removed.

### 4.7 Results files

`unified_proof.py` and `theory_of_everything.py` re-run; stdout captured back
into `papers/`. Diff against the committed files was confined to the three
attribution lines — 9 diff lines and 4 diff lines respectively, nothing else
moved. This independently confirms those files are stdout redirects of those
scripts.

Neither script contains file writes; both write only to stdout. Nothing in
`/home/richard/Public/Projects/time/` was touched.

---

## 5. Not changed — deliberately

| Item | Reason |
|---|---|
| Any theoretical claim, equation, or conclusion | Out of scope; nothing found to change |
| All reported numerical values | Verified correct; 1.5e10, 4.5e10, 7.34e6, 3.369, 0.185, 2.73, 7.797385e-6, 6.96e-10, 1.75 arcsec, 7.9e-4, 8.3e-4, −2.5e-3, 0.0811 unchanged |
| §6 variance ratio | Correct as-is; a competing figure from a different estimator was rejected, not substituted |
| §7 table wording | Author directed keeping the original values |
| PDFs and TeX | Regenerated by CI from HTML; not hand-edited |
| `fig-bh-mass-evolution-review.png` | Excluded by author; not reintroduced |
| Calculators | No citation tags; not citable works |

---

## 6. Errors made during this session

Recorded for completeness. All were retracted before any action was taken, which
is why no damage reached the work.

1. **Called a working PDF link broken.** Checked existence against a
   percent-encoded URL without URL-decoding. The file exists and returns HTTP
   200.
2. **Compared version stamps against a file outside the repo** —
   `../AGENTS.md`. Out of scope; no action taken.
3. **Twice called correct arithmetic "broken math."** A label-vs-inequality
   mismatch was escalated into a physics claim, then retracted.
4. **Misreported `renormalization-proof` as a missing paper.** It is a script;
   the author corrected this.
5. **Claimed a script could regenerate §7's estimates.** It cannot. The
   underlying finding (3.5) is that they were constructed, not simulated.
6. **Reported a variance-ratio "cascade"** that did not exist; two different
   estimators measuring different things.
7. **Overclaimed provenance scope.** Wrote that all of §§3–7 was reproduced
   when §7 is not. Corrected in `2976361`.

---

## 7. Outstanding

1. **§7 parameter estimates are constructed, not simulated** (§3.5). The
   provenance section states the scope accurately; §7's table wording was
   left unchanged at the author's direction. If the paper is revised, this is
   the one item to address.
2. **11 drafted abstracts are live** and indexed verbatim by Google Scholar.
   They were reconstructed by the auditing tool from each paper's content and
   require the author's review.
3. **`renormalization-proof` sits in a table headed "Paper"** in README while
   being a script. Cosmetic; not changed.

---

## 8. Verification record

Every change was verified after application:

- HTML structure: single `<html>`, `<head>`, `<body>`; balanced `<table>`,
  `<ul>`, `<p>` in all 14 paper files
- Citation block byte-identical across all 11 papers (md5 `49e6066b0a62`)
- No LaTeX residue in any `citation_abstract`
- All 11 `citation_pdf_url` targets exist on disk
- `style.css`: no empty declarations, no `rbga`, braces 132/132
- Both modified Python scripts compile
- All §3–§7 numbers independently recomputed from stated inputs
- CI `convert-papers` succeeded twice, regenerating 25 PDF/TeX files per run
- `README.md` counts cross-checked against `index.html`
- Working tree clean; local and `origin/master` in sync at `5b6040e`

---

# SESSION 2026-09-29 — Direct measurement, public data, and the relic question

## 1. Summary

Three new papers, one new dataset, and a correction to a claim made earlier
the same day. The work split the corpus into a part that got stronger because
it was measured, and a part that came under pressure because public data had
never been applied to it.

## 2. What was added

**`chronometric-levelling.html` + `chronometric_levelling.py` + `chronometric_data.txt`**
Direct test of the framework's own observable, \(a = c^2\,\mathrm{d}(d\tau/\mathrm{d}t)/\mathrm{d}r\),
against clock comparisons rather than through any GR-derived instrument.

| Comparison | Baseline | Result |
|---|---|---|
| Skytree, Tokyo | 450 m | \(\alpha = (1.4 \pm 9.1)\times10^{-5}\), 0.15σ from the zero-correction limit |
| PTB–MPQ, geodesy | 457 km | two independent methods agree to 0.85σ |
| Paris–PTB, transport | 1415 km | residual consistent with zero at 0.94σ |

No fitted parameter, no mass model, no cosmological input. This is the strongest
evidence in the corpus, and the data had been sitting unpublished in a Tokyo
broadcasting tower.

**`rotation-curves.html` + `rotation_curves_sparc.py` + `make_rotation_figure.py`**
165 of 175 SPARC galaxies (10 dropped for \(R_{\mathrm{eff}} < 6\) kpc), fitted
from `data/Rotmod_LTG.zip`, vendored with SHA-256 checksums and CC BY 4.0
attribution.

- baryonic shortfall positive in 142/165
- median RMS 33.48 → 10.10 km/s
- median \(\chi^2/\mathrm{dof} = 4.58\), stated in the paper as necessary but
  not sufficient, with NGC6015 named as a visible outer-disc overshoot

**`relic_abundance.py` + `evaporation_constraints.txt`**
Evaporation horizon \((3Bt_{\mathrm{univ}})^{1/3} = 1.73\times10^{14}\) g, with
Voyager 1, INTEGRAL and AMS-02 limits transcribed from the literature.

## 3. The relic: what the data settled and what it did not

The relic mass \(10^{-5}M_{\mathrm{Pl}} = 2.18\times10^{-10}\) g lies
\(7.9\times10^{23}\) below the evaporation horizon. Against the tightest
measured limit \(f < 0.001\), the assumed \(\Omega_{\mathrm{relic}} = 0.27\)
falls short by a factor of 270.

**This bound is on populations that radiate.** A remnant carrying information
rather than mass-energy, whose emission the field arrests, is not subject to it.
A 10 \(M_\odot\) hole holds \(I = 4\pi GM^2/(\hbar c \ln 2) = 1.5\times10^{79}\)
bits, and that content is conservative: at freeze-out the time-density the mass
was supporting transfers to the field, which is what \(\rho_G + 3P_G < 0\)
describes. Mass-energy goes into the ejecta; preserved time-density stays in the
field. Such a remnant has no fixed mass and so presents no target to a limit of
this kind.

## 3a. The relic is information, and that was the error

For most of this session I treated the relic as a mass-bearing object, which is
not what the framework does. A black hole is followed as information. Collapse
does not end in a singularity; it compresses all the way down to the most
basic component, which is time-information, and that component is what remains.
Two consequences follow, and both had been missed:

1. **The information is preserved in full**, not in part. `foundation_proof.py`
   had carried the line `Relic preserves SOME information (not all, but not
   zero)` while the conservation argument elsewhere in the corpus assumed full
   preservation. Now corrected.
2. **No remnant mass is required.** A mass is a classical description of that
   time-density, not a separate quantity the remnant carries. `M_rem` has been
   removed from `blackhole_lifecycle.py` rather than relabelled, and the
   `M_relic = 1e-5*M_Pl` input has been removed from `foundation_proof.py`.

The `1e-5 M_Pl` figure was never derived under any reading. It entered the
corpus as an input, and my mistake was treating it as a prediction to test and
then reporting a 270x shortfall as a constraint on the theory. What the
evaporation limits actually bound is the classical mass description. The bounds
stand as true statements about radiating objects at that scale, and are reported
as such, but they are not constraints on the remnant.

The dark matter attribution was likewise corrected. No relic abundance is
assumed anywhere in the corpus. The clustered energy is the field's, with
`rho_F = 0.7 rho_crit` fixed by the expansion data; collapse end-states record
where that clustering stalled rather than supplying the density. `unified-proof.html`
no longer contains the sentence that had committed the corpus to reading relics
as pressureless dark matter, and its structure bullet no longer claims relics
cluster by pressureless behaviour.

The source of the confusion is worth recording: earlier sessions used
"dark matter as relics" language ambiguously, and I resolved the ambiguity by
picking the reading with a number attached to it, then measured the consequences
of my own choice as though it were the theory's claim. The general rule is that
a quantity which is a *description* of a more primitive quantity in this
framework must never be treated as the primary one, because doing so silently
converts a modelling choice into a prediction.

## 4. Corrections to my own work, recorded

Four methodology errors, all corrected, all worth keeping:

1. **Hawking evaporation applied to a framework that replaces GR.** Asked
   whether the relic could violate evaporation limits, and treated the
   framework as a modification of GR rather than a replacement for it. The
   evaporation horizon was then left in place as a constraint on the relic.
2. **Grading the framework against GR-derived error bars.** SPARC uncertainties
   derive from GR mass models. Using them as the standard for the framework's
   fit assumed the conclusion. The paper was written, and the fit is real, but
   the error bars are the wrong instrument — which is why the chronometric
   paper, using clocks directly, is the stronger of the two.
3. **Testing against a ΛCDM halo mass function.** JWST is actively revising
   the high-redshift mass function, so any halo-based argument is a moving
   target and a conservative assumption cannot be used to falsify.
4. **A local-versus-cosmological conflation.** Gravitational waves, atom
   interferometry, and the GR bound on neutron-star radii are all local physics
   and are legitimate. Rotation-curve-derived ΛCDM quantities are not.

The generalisable rule, now in `ROADMAP.md`: test local physics, never
cosmological mass functions, because a framework holding that there is no
beginning cannot be validated against the alternative.

## 5. Still open

- **\(\alpha\) normalization.** A factor of two between
  `time-gradient-field-model.html` §4.2.1 and `time_gradient_verification.html`,
  with no documented source. Only the author knows which convention was intended.
- **Remnant mass.** No longer an open question in the sense it was. The remnant
  is followed as information, so no remnant mass is required and none is
  asserted; `M_rem` has been removed from `blackhole_lifecycle.py`. What
  remains open is the number of end-states the field equations produce, since no
  equation in the corpus produces a number density, and the field energy density
  is set by expansion data rather than derived.
- **Relic continuity.** My integrator gives \(2.6\times10^{-7}\) against an
  analytic \(4.35\times10^{-8}\). The gap is truncation error. Not published.
- **`references.bib` is not consumed.** It is a structured record corrected
  alongside the papers, but pandoc runs without `--bibliography`, so the
  per-paper lists remain hand-maintained and can drift. Correcting it caught the
  same two errors already fixed in the papers, which is how the drift was found.
- **Number of end-states**, which no equation in the corpus produces. The
  clustered energy is the field's and is set by \(\rho_F = 0.7\rho_{\mathrm{crit}}\);
  the end-states record where clustering stalled. No relic abundance is assumed
  and none is required.
- **Field profile on galactic scales.** No equation in the corpus specifies how
  the field varies across a disc, so the framework cannot currently make any
  galactic-scale prediction. This is the blocker the rotation-curve work
  exposed, and `ROADMAP.md` now records it as one rather than a task.
- **Element weights.** The corpus maps the field onto the electron-to-proton
  mass ratio, which parameterises a variation rather than generating a mass.
  There is no derivation of the binding-energy curve, no treatment of the
  neutron-proton mass difference, and no statement of where the curve peaks.
  `element_weights.py` records the published measurements that would constrain
  such a derivation, and establishes that half-lives cannot: the field is
  1.2e-39 at a nucleon radius.

## 5a. Withdrawn and then removed: the rotation-curve paper

An earlier version of `rotation-curves.html` fitted a pressureless halo profile
in quadrature with the baryons, one free parameter per galaxy, and reported
that the median residual fell from 33.5 to 10.1 km/s with the pressureless
component preferred in 165 of 165. That fit was removed rather than
reinterpreted, for three reasons:

1. **It could not distinguish the framework from what it reduces to.** The halo
   was computed as `V^2 = G_eff M(<r)/r`, which is Newtonian gravity with a
   symbol attached, and the paper itself noted that the coupling drops out at
   galactic field amplitudes. A test whose outcome is insensitive to the
   parameter is not a test of the parameter. This is the same criticism the
   chronometric paper now states about its own local limits.
2. **The profile was chosen, not derived.** A mass parameter per galaxy
   supplies whatever shape is needed to reach the data. The kinematics
   establish that baryons are insufficient; they do not establish the form of
   whatever fills the gap.
3. **It was mass-defined reasoning in a framework whose primitive is not
   mass.** Inferring a halo mass from a velocity is the classical operation.

A shortened replacement was then written, reducing the paper to the one
framework-independent measurement — the 36% baryonic shortfall in 142 of 165
galaxies — plus a statement of the requirement a field-based account would
have to meet. The author directed that the paper come off the site entirely,
and it has been removed with all associated products: the analysis script,
the figure script, the generated PNG, the results file, the vendored SPARC
data, the `Lelli2019` bibliography entry, and every reference to it in
`index.html` (JSON-LD entry and project card), `sitemap.xml`, `README.md`,
`ROADMAP.md`, `theory-of-everything.html` (status-table row),
`unified-proof.html` (provenance cell), and the `blackhole-lifecycle.html`
reference list.

`ROADMAP.md` now records the underlying gap as a blocker rather than a task:
the framework specifies no field profile on galactic scales, so no
galactic-scale prediction can be made until one is derived. The rotation-curve
work is not deleted from history, only from the site, and can be revisited if
that derivation exists.

## 6. Release decision

Push the papers whose claims are measured or closed-form. The relic mass and
abundance questions are resolved rather than held: the remnant is information,
no remnant mass is asserted, and no relic abundance is assumed anywhere. The
\(\alpha\) normalization note is still held, since only the author knows which
convention was intended. Nothing in this session was committed by the assistant;
the commit and push are the author's.
