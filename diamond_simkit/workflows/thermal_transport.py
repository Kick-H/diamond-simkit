"""Thermal transport workflow template generation."""

from pathlib import Path

from ase import Atoms

from diamond_simkit.workflows.common import write_workflow_bundle


def generate_thermal_transport_workflow(
    output_dir: str | Path, atoms: Atoms, potential_path: str
) -> Path:
    meta = {
        "name": "thermal_transport_template",
        "potential_path": potential_path,
        "targets": ["thermal_conductivity", "thermal_diffusivity"],
    }
    return write_workflow_bundle(output_dir, atoms, potential_path, meta)
