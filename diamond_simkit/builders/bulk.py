"""Bulk structure builders."""

from ase import Atoms
from ase.build import bulk


def build_bulk_diamond(a: float = 3.567, size: tuple[int, int, int] = (2, 2, 2)) -> Atoms:
    """Build cubic diamond bulk supercell."""
    atoms = bulk("C", crystalstructure="diamond", a=a, cubic=True)
    return atoms.repeat(size)
