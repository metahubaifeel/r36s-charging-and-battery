#!/usr/bin/env python3
"""Draw docs/06-charging-checklist.png for this repository.

Run from the repository root:  python3 tools/make-checklist.py

The image is drawn from literal rectangles and text — no image model is involved
anywhere in this repository. Every photograph in docs/ is a real photograph of a
real unit, cropped and downscaled only.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "docs", "06-charging-checklist.png")


def box(ax, x, y, w, h, text, fc, fs=10, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.010,rounding_size=0.02",
                                linewidth=1.1, facecolor=fc, edgecolor="#1b1b1b", zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            zorder=3, linespacing=1.55, fontweight=weight)


def arrow(ax, x, y1, y2):
    ax.add_patch(FancyArrowPatch((x, y1), (x, y2), arrowstyle="-|>", mutation_scale=13,
                                 linewidth=1.2, color="#4a4a4a", zorder=1))


fig, ax = plt.subplots(figsize=(11.5, 9.0), dpi=170)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ax.text(0.5, 0.968, "R36S: the charging light is on but the percentage will not rise",
        ha="center", fontsize=13.5, fontweight="bold")
ax.text(0.5, 0.932, "Work top to bottom. Stop at the first row that moves the on-screen battery figure.",
        ha="center", fontsize=9.6, color="#4a4a4a")

rows = [
    ("1", "Is the cable in the port marked DC?\nThat input is rated 5 V / 2 A, not the OTG port.",
     "The indicator can light from either port.\nThe board silkscreen labels both.", "#eaf2fb"),
    ("2", "Is it an A-to-C cable on a 5 V / 1 A or\n5 V / 2 A supply, not C-to-C on a PD brick?",
     "A C-to-C cable needs CC pull-down\nresistors inside the device. Many\nhandhelds do not fit them.", "#eaf2fb"),
    ("3", "Does that supply keep the port alive at low\ncurrent instead of cutting it off?",
     "Multiport bricks and power banks drop\na port when the draw falls below a\nthreshold, often tens of milliamps.", "#fdf3e3"),
    ("4", "Does the same cable charge a phone at a\nnormal rate?",
     "Swapping the cable is the cheapest\ntest there is. Charge-only and worn\ncables fail exactly here.", "#fdf3e3"),
    ("5", "After 30-60 minutes on the DC port, does the\non-screen percentage move at all?",
     "If a known-good supply moves nothing,\nthe fault is inside the unit: charge IC,\nconnector, or the cell itself.", "#fbeaea"),
]
ytop, bh, pitch = 0.868, 0.098, 0.153
for i, (n, q, note, col) in enumerate(rows):
    y = ytop - i * pitch
    box(ax, 0.035, y - bh, 0.60, bh, f"{n}.  {q}", col, fs=10.0)
    ax.text(0.655, y - bh / 2, note, fontsize=8.3, color="#3a3a3a", va="center", linespacing=1.6)
    if i < len(rows) - 1:
        arrow(ax, 0.335, y - bh - 0.004, y - pitch + 0.006)
y = ytop - len(rows) * pitch
box(ax, 0.035, y - 0.078, 0.60, 0.078,
    "6.  Still nothing?  Stop guessing —\nuse the two measurements in the article.",
    "#e8f5e9", fs=9.8, weight="bold")
ax.text(0.655, y - 0.039, "A red, green or violet light only tells you\npower is present. It is not a battery gauge.",
        fontsize=8.3, color="#3a3a3a", va="center", linespacing=1.6)
fig.savefig(OUT, bbox_inches="tight", facecolor="white")
print("wrote", OUT)
