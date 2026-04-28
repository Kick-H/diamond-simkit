import pytest

pytest.importorskip("ase")

from diamond_simkit.builders.slabs import build_diamond_slab


@pytest.mark.parametrize("surface", ["100", "110", "111"])
def test_build_diamond_slab_surfaces(surface):
    atoms = build_diamond_slab(surface=surface, layers=4, size=(1, 1, 1))
    assert len(atoms) > 0
