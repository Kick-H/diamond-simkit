"""ASE-native analysis helpers."""

from ase import Atoms


def run_basic_structure_analysis(atoms: Atoms) -> dict:
    """Return lightweight structure statistics."""
    if len(atoms) == 0:
        raise ValueError("Atoms object is empty")
    lengths = atoms.cell.lengths()
    return {
        "n_atoms": len(atoms),
        "formula": atoms.get_chemical_formula(),
        "cell_lengths": [float(x) for x in lengths],
        "pbc": [bool(x) for x in atoms.pbc],
    }
