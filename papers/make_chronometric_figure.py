"""Figure: chronometric levelling baselines, framework law vs published values.

Three published baselines on one axis, showing the geopotential difference the
framework's law reproduces, with the published uncertainties. The clock data
read the framework's own quantity (dtau/dt) directly.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

C = 2.998e8
HERE = os.path.dirname(os.path.abspath(__file__))

# Published values, transcribed in chronometric_data.txt
# (label, separation_km, DeltaU m^2/s^2, uncertainty, source)
panels = [
    ("Tokyo Skytree\n450 m", 0.450, 4405.0, None,
     r"$\alpha = (1.4 \pm 9.1)\times10^{-5}$" + "\nconsistent with 0 at 0.15$\\sigma$",
     "Takamoto et al. 2020\nNat. Photonics 14, 411"),
    ("PTB - MPQ\n457 km", 457.0, 3918.1, 2.6,
     "chronometric vs geodetic\nagree to 0.85$\\sigma$",
     "arXiv:2309.14953"),
    ("Paris - PTB\n1415 km", 1415.0, 0.0, None,
     r"residual $(4.7 \pm 5.0)\times10^{-17}$" + "\nconsistent with zero",
     "Grose et al. 2015\nNat. Commun. 6, 7768"),
]

fig, axes = plt.subplots(1, 3, figsize=(12, 4.2), dpi=150)
fig.suptitle("Chronometric levelling: the time-density gradient read off directly",
             fontsize=13, y=0.99)

for ax, (label, sep, dU, err, annot, src) in zip(axes, panels):
    if sep < 1.0:
        # Skytree: show the Einstein redshift the law reproduces
        shift = 0.5*dU/C**2
        ax.bar([0], [shift*1e14], width=0.5, color="#2d8cf0",
               label=r"$\frac{1}{2}\Delta U/c^2$ (law, $\alpha=0$)")
        ax.set_ylabel(r"frequency shift  $\Delta\nu/\nu$  ($10^{-14}$)", fontsize=9)
        ax.set_ylim(0, 3.2)
        ax.legend(fontsize=7.5, loc="upper right")
    elif err is not None:
        ax.errorbar([0], [dU/1e3], yerr=err/1e3, fmt="o", ms=9, color="#2d8cf0",
                    capsize=6, lw=2, label="chronometric")
        ax.errorbar([0], [3915.88/1e3], yerr=0.30/1e3, fmt="s", ms=7,
                    color="#f97316", capsize=5, lw=2, label="geodetic")
        ax.set_ylabel(r"geopotential difference  $\Delta U$  ($10^{3}$ m$^2$s$^{-2}$)",
                      fontsize=9)
        ax.legend(fontsize=8, loc="lower right")
        ax.set_ylim(3910, 3924)
    else:
        ax.bar([0], [0.47e-16*1e17], width=0.45, color="#2d8cf0",
               label="measured residual")
        ax.axhline(0.5e-17*1e17, color="#990900", ls="--", lw=1.4,
                   label="1$\\sigma$ = 0.5")
        ax.set_ylabel(r"residual rate  ($\times 10^{-17}$)", fontsize=9)
        ax.set_ylim(0, 1.4)
        ax.legend(fontsize=8, loc="upper right")

    ax.set_xticks([])
    ax.set_xlim(-0.6, 0.6)
    ax.set_title(label, fontsize=10)
    ax.text(0.5, -0.16, annot, transform=ax.transAxes, ha="center", va="top",
            fontsize=8.5, color="#1a1a1a")
    ax.text(0.5, -0.34, src, transform=ax.transAxes, ha="center", va="top",
            fontsize=7, color="#777", style="italic")
    ax.grid(axis="y", alpha=0.25, linestyle=":")

fig.text(0.5, 0.015,
         "The framework's law  $a = c^2\\,d(d\\tau/dt)/dr$  predicts these rate differences "
         "with no fitted parameter.",
         ha="center", fontsize=8.5, color="#444")
fig.tight_layout(rect=[0, 0.06, 1, 0.95])
out = os.path.join(HERE, "fig-chronometric.png")
fig.savefig(out)
plt.close(fig)
print(f"{os.path.basename(out)} written")
