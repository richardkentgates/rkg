# SPARC rotation curves — vendored data

**Source:** Lelli, F., McGaugh, S. S., & Schombert, J. M. (2019).
"SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and
Accurate Rotation Curves." *Astronomical Journal* 152, 157.
<https://ui.adsabs.harvard.edu/abs/2019AJ....152..157L>

**Upstream:** <https://astroweb.case.edu/SPARC/> (also mirrored at
<https://zenodo.org/records/16284118>)

**Retrieved:** 2026-09-28

**Licence:** Creative Commons Attribution 4.0 (CC BY 4.0). The SPARC database
is released under CC BY 4.0; redistribution with attribution is permitted.
If you use these data, cite the SPARC master paper above, and consider citing
the original rotation-curve sources listed in Table 1 of the SPARC sample.

## Files

| File | Bytes | MD5 | Contents |
|---|---|---|---|
| `Rotmod_LTG.zip` | 110737 | `e4c8b92766026770ed35e5889064e12b` | 175 `*_rotmod.dat` files, one per galaxy |
| `SPARC_Lelli2016c.mrt` | 28259 | `6181df386bfc05868a3700c196e800da` | Galaxy sample table, incl. references to original sources |

Verify with:

```sh
md5sum Rotmod_LTG.zip SPARC_Lelli2016c.mrt
```

## Format of `*_rotmod.dat`

ASCII, whitespace-delimited. Lines beginning `#` are comments. Columns:

| # | Symbol | Units | Meaning |
|---|---|---|---|
| 1 | `Rad` | kpc | Galactocentric radius |
| 2 | `Vobs` | km/s | Observed circular velocity (inclination-corrected) |
| 3 | `errV` | km/s | Uncertainty on `Vobs` |
| 4 | `Vgas` | km/s | Gas contribution, in quadrature |
| 5 | `Vdisk` | km/s | Stellar disk contribution, in quadrature |
| 6 | `Vbul` | km/s | Bulge contribution, in quadrature |
| 7 | `SBdisk` | L/pc² | Disk surface brightness at 3.6 μm |
| 8 | `SBbul` | L/pc² | Bulge surface brightness at 3.6 μm |

`Vgas`, `Vdisk`, `Vbul` are the **baryonic** components. The total baryonic
contribution is

```
Vbar = sqrt(Vgas² + Vdisk² + Vbul²)
```

Any excess of `Vobs` over `Vbar` at large radius is what a dark component must
supply. A header comment in each file gives the distance in Mpc.

## Why this data is vendored

Results that depend on a live URL can change when the remote file changes.
The rotation-curve analysis in this repository reads only the copy in this
directory, so the numbers it reports are reproducible from a clean checkout
with no network access.
