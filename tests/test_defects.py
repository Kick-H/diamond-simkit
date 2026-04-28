import pytest

pytest.importorskip("ase")

from diamond_simkit.builders.bulk import build_bulk_diamond
from diamond_simkit.builders.defects import add_substitution, add_vacancy


def test_add_vacancy_and_substitution():
    atoms = build_bulk_diamond(size=(2, 2, 2))
    vac = add_vacancy(atoms, index=0)
    sub = add_substitution(atoms, index=0, symbol="N")

    assert len(vac) == len(atoms) - 1
    assert sub[0].symbol == "N"
