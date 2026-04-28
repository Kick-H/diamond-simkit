"""Single-crystal benchmark workflow template."""

from pathlib import Path

from diamond_simkit.builders.bulk import build_bulk_diamond
from diamond_simkit.workflows.common import write_workflow_bundle


def generate_single_crystal_workflow(
    output_dir: str | Path, potential_path: str, reference_data: dict | None = None
) -> Path:
    atoms = build_bulk_diamond()
    meta = {
        "name": "single_crystal_benchmark",
        "potential_path": potential_path,
        "reference_data": reference_data or {},
        "targets": [
            "lattice_constant",
            "cohesive_energy",
            "elastic_constants",
            "heat_capacity",
            "phonon_related",
        ],
    }
    return write_workflow_bundle(output_dir, atoms, potential_path, meta)
