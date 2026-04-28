import pytest

pytest.importorskip("ase")

from diamond_simkit.builders.nanowires import build_diamond_nanowire


@pytest.mark.parametrize("cross_section", ["square", "hexagonal"])
def test_build_nanowire_cross_sections(cross_section):
    atoms = build_diamond_nanowire(cross_section=cross_section, length=20, width=10)
    assert len(atoms) > 0
