#!/usr/bin/env python3
"""Figure: SPARC rotation curves with the framework gravity law fitted to data.

Panels show observed V_obs with published errors, the baryons-only prediction,
and the fit with one free parameter (enclosed halo mass at r_max). Real data,
real error bars. Generated from the vendored SPARC archive.
"""
import numpy as np
import zipfile, io, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

G_NEWt = 6.674e-11
KPC = 3.086e19
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "Rotmod_LTG.zip")

def load_one(name):
    with zipfile.ZipFile(DATA) as z:
        R, V, EV, VG, VD, VB = [], [], [], [], [], []
        with z.open(name) as fh:
            for raw in io.TextIOWrapper(fh, encoding="utf-8", errors="replace"):
                if raw.startswith("#"):
                    continue
                p = raw.split()
                if len(p) < 6:
                    continue
                R.append(float(p[0])); V.append(float(p[1])); EV.append(float(p[2]))
                VG.append(float(p[3])); VD.append(float(p[4])); VB.append(float(p[5]))
    return tuple(np.array(a) for a in (R, V, EV, VG, VD, VB))

def vbar_of(VG, VD, VB):
    return np.sqrt(VG**2 + VD**2 + VB**2)

def halo_v(r_kpc, m_at_rmax, rmax_kpc, r_s_kpc=20.0):
    r = np.atleast_1d(np.asarray(r_kpc, float)) * KPC
    r_s = r_s_kpc * KPC
    rmax = rmax_kpc * KPC
    f = lambda t: np.log(1.0 + t) - t / (1.0 + t)
    x = r / r_s
    denom = f(rmax / r_s) - f(1e-3)
    shape = np.clip((f(x) - f(1e-3)) / denom, 0.0, 1.0)
    m = m_at_rmax * shape
    order = np.argsort(r)
    ms = np.maximum.accumulate(m[order])
    mo = np.empty_like(m); mo[order] = ms
    return np.sqrt(G_NEWt * mo / r) / 1000.0

def fit(R, V, EV, vbar):
    rmax = float(R[-1])
    chi_b = np.sum(((V - vbar) / np.maximum(EV, 1.0))**2)
    best, bc = 1e41, chi_b
    for lm in np.linspace(np.log10(1e37), np.log10(1e44), 500):
        m = 10.0**lm
        p = np.sqrt(vbar**2 + halo_v(R, m, rmax)**2)
        c = np.sum(((V - p) / np.maximum(EV, 1.0))**2)
        if np.isfinite(c) and c < bc:
            bc, best = c, m
    return best, bc

with zipfile.ZipFile(DATA) as z:
    names = [n for n in z.namelist() if n.endswith("_rotmod.dat")]

# Selection: galaxies with enough points (n>=30) and a reasonable fit
# (RMS < 25 km/s), then one each from four quartiles of V_flat so the panels
# span the sample rather than showing the extremes. Criterion is stated in the
# paper; galaxies excluded by it are counted in rotation_curves_results.txt.
res_path = os.path.join(HERE, "rotation_curves_results.txt")
rows = []
if os.path.exists(res_path):
    with open(res_path) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) >= 8 and p[0] != "galaxy":
                try:
                    rows.append(dict(g=p[0], n=int(p[1]), vflat=float(p[2]),
                                     rms=float(p[4])))
                except ValueError:
                    pass
elig = [r for r in rows if r["n"] >= 30 and r["rms"] < 25.0]
elig.sort(key=lambda r: r["vflat"])
q = max(len(elig)//4, 1)
picks = [elig[i] for i in (0, q, 2*q, 3*q) if i < len(elig)]
targets = [r["g"] for r in picks]
avail = set(n.replace("_rotmod.dat", "") for n in names)
targets = [t for t in targets if t in avail]
if len(targets) < 4:
    targets = sorted(avail)[:4]

fig, axes = plt.subplots(2, 2, figsize=(11, 8.5), dpi=150)
fig.suptitle("SPARC rotation curves: framework gravity law $a=c^2\\,d(d\\tau/dt)/dr$ "
             "+ one pressureless parameter", fontsize=13, y=0.98)

for ax, g in zip(axes.ravel(), targets):
    R, V, EV, VG, VD, VB = load_one(g + "_rotmod.dat")
    if len(R) < 6:
        ax.axis("off"); continue
    vbar = vbar_of(VG, VD, VB)
    m_fit, chi = fit(R, V, EV, vbar)
    pred = np.sqrt(vbar**2 + halo_v(R, m_fit, float(R[-1]))**2)
    ax.errorbar(R, V, yerr=EV, fmt="o", ms=3.2, lw=0.8, color="#1a1a1a",
                elinewidth=0.7, capsize=1.5, label="observed $V_{obs}$ (SPARC)", zorder=3)
    ax.plot(R, vbar, color="#f97316", lw=1.8, label="baryons only", zorder=2)
    ax.plot(R, pred, color="#2d8cf0", lw=2.2,
            label="baryons + pressureless halo", zorder=4)
    rms = np.sqrt(np.mean((V - pred)**2))
    ax.set_title(f"{g}   RMS = {rms:.1f} km/s", fontsize=10)
    ax.set_xlabel("radius (kpc)", fontsize=9)
    ax.set_ylabel("$V_c$ (km/s)", fontsize=9)
    ax.grid(alpha=0.25, linestyle=":")
    ax.tick_params(labelsize=8)

axes[0, 0].legend(fontsize=7.5, loc="lower right", framealpha=0.95)
fig.text(0.5, 0.015,
         "Data: Lelli, McGaugh & Schombert 2019, AJ 152, 157 (CC BY 4.0), vendored in papers/data/",
         ha="center", fontsize=8, color="#555")
fig.tight_layout(rect=[0, 0.03, 1, 0.96])
out = os.path.join(HERE, "fig-sparc-rotation-curves.png")
fig.savefig(out)
plt.close(fig)
print(f"{os.path.basename(out)} written")
print("  panels:", ", ".join(targets))
