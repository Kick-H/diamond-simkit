from pathlib import Path

import pytest

pytest.importorskip("ase")

from diamond_simkit.builders.bulk import build_bulk_diamond
from diamond_simkit.workflows.mechanics import generate_mechanics_workflow
from diamond_simkit.workflows.single_crystal import generate_single_crystal_workflow
from diamond_simkit.workflows.thermal_transport import generate_thermal_transport_workflow


def test_workflow_directories_and_templates(tmp_path: Path):
    potential = tmp_path / "nep.txt"
    potential.write_text("dummy nep")
    atoms = build_bulk_diamond(size=(1, 1, 1))

    out1 = generate_single_crystal_workflow(tmp_path / "single", str(potential))
    out2 = generate_mechanics_workflow(tmp_path / "mech", atoms, str(potential))
    out3 = generate_thermal_transport_workflow(tmp_path / "thermal", atoms, str(potential))

    for out in [out1, out2, out3]:
        assert (out / "structure.xyz").exists()
        assert (out / "workflow.json").exists()
        assert (out / "run.in").exists()
