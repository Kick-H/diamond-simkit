import pytest

ase = pytest.importorskip("ase")

from diamond_simkit.builders.bulk import build_bulk_diamond


def test_build_bulk_diamond():
    atoms = build_bulk_diamond(size=(1, 1, 1))
    assert len(atoms) > 0
    assert "C" in atoms.get_chemical_formula()
