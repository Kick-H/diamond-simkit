"""Structure I/O wrappers."""

from pathlib import Path
from ase import Atoms
from ase.io import read, write


def read_structure(path: str | Path) -> Atoms:
    return read(str(path))


def write_structure(atoms: Atoms, path: str | Path) -> None:
    write(str(path), atoms)


def write_dual_xyz(atoms: Atoms, output_stem: str | Path) -> None:
    stem = Path(output_stem)
    write(str(stem.with_suffix(".extxyz")), atoms)
    write(str(stem.with_suffix(".xyz")), atoms)
