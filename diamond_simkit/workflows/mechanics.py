"""Mechanical workflow template generation."""

from pathlib import Path

from ase import Atoms

from diamond_simkit.workflows.common import write_workflow_bundle


def generate_mechanics_workflow(output_dir: str | Path, atoms: Atoms, potential_path: str) -> Path:
    meta = {
        "name": "mechanics_template",
        "potential_path": potential_path,
        "models": ["nanowire_indentation", "i_beam_like", "tension_compression"],
    }
    return write_workflow_bundle(output_dir, atoms, potential_path, meta)
