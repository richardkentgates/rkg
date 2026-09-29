"""Regenerate the decoherence panel that entanglement-formalization.html uses.

The old fig-rotation-decoherence.png paired a rotation curve with a
decoherence plot. The rotation panel belonged to the withdrawn black-hole
lifecycle and is gone from that paper, so the decoherence panel is now
standalone. Generated from the paper's own formula:

    t_dec = eps / (2 A_amp |sin(delta/2)|)
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

EPS    = 1.0        # coherence limit
A_AMP  = 0.25       # field amplitude at the endpoints

delta = np.linspace(0.0, np.pi, 2000)
# avoid the removable singularity at delta = 0 by flooring the sine
s = np.maximum(np.abs(np.sin(delta/2.0)), 1e-12)
t_dec = EPS/(2.0*A_AMP*s)
# below the Planck time the decoherence description is not meaningful
t_Pl = 5.391e-44
valid = t_dec > t_Pl
delta_v, t_v = delta[valid], t_dec[valid]

fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=150)
ax.semilogy(delta_v, t_v, color="#2d8cf0", linewidth=2.2,
            label=r"$t_{\mathrm{dec}} = \epsilon / (2A_{\mathrm{amp}}|\sin(\delta/2)|)$")
ax.axhline(t_Pl, color="#990900", linestyle="--", linewidth=1.2,
           label="Planck time (below this, decoherence is not meaningful)")
ax.set_xlabel(r"phase difference $\delta$  (radians)")
ax.set_ylabel(r"decoherence time $t_{\mathrm{dec}}$  (s)")
ax.set_title("Decoherence Time vs Phase Difference", fontsize=13, pad=12)
ax.set_xlim(0, np.pi)
# the delta->0 divergence spans ~80 decades; clip the axis so the physical
# range is readable while keeping the Planck-time floor visible
ax.set_ylim(t_Pl*0.5, 1e4)
ax.grid(alpha=0.3, linestyle=":")
ax.legend(fontsize=8, loc="lower left", framealpha=0.95)
fig.tight_layout()
out = "fig-decoherence.png"
fig.savefig(out)
plt.close(fig)

print(f"{out} written  ({len(delta_v)} of {len(delta)} points above the Planck time)")
print(f"  t_dec at delta=pi : {t_dec[-1]:.6e} s")
print(f"  Planck time       : {t_Pl:.6e} s")
crossings = delta[~valid]
if len(crossings):
    print(f"  crossing below Planck time at delta ~ {crossings[-1]:.6f} rad")
else:
    print("  t_dec stays above the Planck time across the full delta range")
