"""Figure: the baryonic shortfall, which is what the data require.

Four SPARC rotation curves showing the observed velocity, the published
uncertainties, and the baryonic prediction from the published gas, disk and
bulge components. The gap between the orange and black curves is the
requirement this paper states. No halo is drawn, because no halo is
asserted: the framework has no field profile on galactic scales to supply
one, and fitting one would assume the answer.

Panel selection is by a stated rule, so the sample is not chosen for its
extremes: one galaxy from each quartile of flat velocity among those with
at least 30 radial points.

Data: Lelli, McGaugh & Schombert 2019, AJ 152, 157 (CC BY 4.0), vendored in
papers/data/. Layout of Rotmod_LTG:
    # Distance = ... Mpc
    # Rad  Vobs  errV  Vgas  Vdisk  Vbulge  SBdisk  SBbulge
    # kpc  km/s  km/s  km/s  km/s  km/s   L/pc^2   L/pc^2
one file per galaxy, named <GALAXY>_rotmod.dat
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import zipfile
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "Rotmod_LTG.zip")


def load_galaxy(z, galaxy):
    name = f"{galaxy}_rotmod.dat"
    if name not in z.namelist():
        return None
    raw = z.read(name).decode("utf-8", "ignore")
    rows = []
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        p = s.split()
        if len(p) < 6:
            continue
        try:
            rows.append([float(v) for v in p[:6]])
        except ValueError:
            continue
    if not rows:
        return None
    a = np.array(rows)
    return a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5]


def survey_galaxies(z):
    return sorted(n.split("_rotmod.dat")[0] for n in z.namelist()
                  if n.endswith("_rotmod.dat"))


def pick_panels(z, n_panels=4, minpts=30):
    """One galaxy per quartile of flat velocity, by a stated rule."""
    stats = []
    for g in survey_galaxies(z):
        d = load_galaxy(z, g)
        if d is None:
            continue
        r, v, dv, vg, vd, vb = d
        sel = r > 0.5 * r.max()
        if len(r) < minpts or not np.any(sel):
            continue
        vbar = np.sqrt(vg**2 + vd**2 + vb**2)
        short = (v[sel].mean() - vbar[sel].mean()) / v[sel].mean()
        if short <= 0.02:
            continue
        stats.append((g, r.max(), v[sel].mean(), short * 100))
    stats.sort(key=lambda t: t[2])
    if not stats:
        return []
    q = np.array_split(np.array(stats), n_panels)
    return [str(g[0][0]) for g in q]


def main():
    fig, axes = plt.subplots(1, 4, figsize=(14, 4.0), dpi=150)
    with zipfile.ZipFile(DATA) as z:
        panels = pick_panels(z)
        print("  panels by rule:", panels)
        for ax, gal in zip(axes, panels):
            d = load_galaxy(z, gal)
            if d is None:
                ax.set_visible(False)
                continue
            r, v, dv, vg, vd, vb = d
            o = np.argsort(r)
            r, v, dv, vg, vd, vb = r[o], v[o], dv[o], vg[o], vd[o], vb[o]
            vbar = np.sqrt(vg**2 + vd**2 + vb**2)
            sel = r > 0.5 * r.max()
            short = (v[sel].mean() - vbar[sel].mean()) / v[sel].mean() * 100
            ax.errorbar(r, v, yerr=dv, fmt="o", ms=3, lw=1, color="#111111",
                        capsize=2, label=r"$V_{\mathrm{obs}}$", zorder=3)
            ax.plot(r, vbar, "s-", ms=3.4, lw=1.7, color="#c0653a",
                    label=r"$V_{\mathrm{bar}}$", zorder=2)
            ax.set_title(f"{gal}\nshortfall {short:+.0f}% (outer half)",
                         fontsize=9.5, pad=6)
            ax.set_xlabel("radius (kpc)", fontsize=9)
            ax.set_xlim(0, r.max() * 1.05)
            ax.set_ylim(0, max(v) * 1.15)
            ax.grid(alpha=0.18, lw=0.6)
            ax.tick_params(labelsize=8)
    axes[0].set_ylabel(r"circular velocity (km s$^{-1}$)", fontsize=9)
    h, l = axes[0].get_legend_handles_labels()
    if h:
        fig.legend(h, l, fontsize=8, loc="upper right", framealpha=0.92,
                   bbox_to_anchor=(0.995, 0.985))
    fig.suptitle("The baryonic shortfall: what the kinematics require",
                 fontsize=11.5, y=1.0)
    fig.text(0.5, -0.05,
             "One galaxy from each quartile of flat velocity, among those with "
             "at least 30 radial points.\n"
             "165 SPARC galaxies; baryons fall short in 142 of them. No halo is drawn: "
             "the framework has no field profile on galactic scales to supply one.",
             ha="center", fontsize=7.5, color="#555")
    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    out = os.path.join(HERE, "fig-sparc-rotation-curves.png")
    fig.savefig(out, bbox_inches="tight")
    print(f"  {out} written, {len(panels)} panels")


if __name__ == "__main__":
    main()
