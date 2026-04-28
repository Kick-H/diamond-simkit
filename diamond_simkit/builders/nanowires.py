"""Nanowire builders."""

import numpy as np
from ase import Atoms

from diamond_simkit.builders.bulk import build_bulk_diamond


def build_diamond_nanowire(
    cross_section: str = "square", length: float = 100.0, width: float = 30.0
) -> Atoms:
    """Build a simple nanowire by carving a repeated bulk cell."""
    a = 3.567
    nx = max(2, int(width / a))
    ny = max(2, int(width / a))
    nz = max(2, int(length / a))
    atoms = build_bulk_diamond(a=a, size=(nx, ny, nz))

    pos = atoms.get_positions()
    center = pos[:, :2].mean(axis=0)
    rel = pos[:, :2] - center

    if cross_section == "square":
        keep = (np.abs(rel[:, 0]) <= width / 2) & (np.abs(rel[:, 1]) <= width / 2)
    elif cross_section == "hexagonal":
        x, y = rel[:, 0], rel[:, 1]
        keep = (
            (np.abs(x) <= width / 2)
            & (np.abs(np.sqrt(3) * y + x) <= width)
            & (np.abs(np.sqrt(3) * y - x) <= width)
        )
    else:
        raise ValueError("cross_section must be 'square' or 'hexagonal'")

    return atoms[keep]
