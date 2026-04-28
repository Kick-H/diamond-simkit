"""Common workflow generation helpers."""

import json
from pathlib import Path

import yaml
from ase import Atoms

from diamond_simkit.io.read_write import write_dual_xyz
from diamond_simkit.io.templates import gpumd_minimize_template, slurm_template
from diamond_simkit.utils.paths import ensure_dir
from diamond_simkit.utils.validation import ensure_file_exists


def write_workflow_bundle(output_dir: str | Path, atoms: Atoms, potential_path: str, meta: dict) -> Path:
    out = ensure_dir(output_dir)
    ensure_file_exists(potential_path, label="Potential file")

    write_dual_xyz(atoms, out / "structure")

    (out / "workflow.json").write_text(json.dumps(meta, indent=2))
    (out / "workflow.yaml").write_text(yaml.safe_dump(meta, sort_keys=False))

    (out / "run.in").write_text(gpumd_minimize_template("structure.xyz", potential_path))
    (out / "submit.sh").write_text(slurm_template(job_name=meta.get("name", "simkit")))
    (out / "postprocess.py").write_text(
        "from ase.io import read\n"
        "atoms = read('structure.xyz')\n"
        "print({'n_atoms': len(atoms), 'formula': atoms.get_chemical_formula()})\n"
    )
    return out
