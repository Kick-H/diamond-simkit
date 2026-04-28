"""Interface constructors."""

import numpy as np
from ase import Atoms


def build_simple_interface(diamond_atoms: Atoms, other_atoms: Atoms, gap: float = 2.0) -> Atoms:
    """Stack two structures along z with a gap."""
    d = diamond_atoms.copy()
    o = other_atoms.copy()
    d_zmax = np.max(d.positions[:, 2])
    o_zmin = np.min(o.positions[:, 2])
    o.positions[:, 2] += d_zmax - o_zmin + gap
    combined = d + o
    cell = combined.cell.array.copy()
    cell[2, 2] = max(cell[2, 2], np.max(combined.positions[:, 2]) + gap)
    combined.set_cell(cell)
    combined.set_pbc((True, True, False))
    return combined
