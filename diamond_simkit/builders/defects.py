"""Defect editing functions."""

import random
from ase import Atoms


def add_vacancy(atoms: Atoms, index: int | None = None) -> Atoms:
    """Remove one atom from a copy of atoms."""
    defective = atoms.copy()
    if len(defective) == 0:
        raise ValueError("Cannot add vacancy to empty Atoms object")
    idx = random.randrange(len(defective)) if index is None else index
    del defective[idx]
    return defective


def add_substitution(atoms: Atoms, index: int, symbol: str) -> Atoms:
    """Substitute one atom species in a copy of atoms."""
    defective = atoms.copy()
    defective[index].symbol = symbol
    return defective
