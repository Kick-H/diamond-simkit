# diamond-simkit

A minimal but extensible Python toolkit for diamond-related atomistic structure generation,
workflow templating, and basic analysis.

## Features (v0.1)
- Builders for bulk diamond, slabs, nanowires, simple defects, and simple interfaces.
- Workflow generators for single-crystal benchmark, mechanics, and thermal transport templates.
- Basic structure analysis helper.
- Optional wrappers for calorine, OVITO/ovitos, and MDAnalysis with helpful errors if missing.

## Installation

```bash
pip install -e .
```

Optional extras:

```bash
pip install -e .[test,analysis,calorine,ovito]
```

## Quick examples

```python
from diamond_simkit.builders.bulk import build_bulk_diamond
from diamond_simkit.workflows.single_crystal import generate_single_crystal_workflow

atoms = build_bulk_diamond(a=3.567, size=(2, 2, 2))
generate_single_crystal_workflow("runs/single_crystal", "./nep.txt")
```

See `examples/` for more scripts.

## API highlights

- `build_bulk_diamond(a=3.567, size=(2, 2, 2))`
- `build_diamond_slab(surface="100", layers=8, vacuum=15.0, size=(4, 4, 1))`
- `build_diamond_nanowire(cross_section="square", length=100.0, width=30.0)`
- `add_vacancy(atoms, index=None)`
- `add_substitution(atoms, index, symbol)`
- `build_simple_interface(diamond_atoms, other_atoms, gap=2.0)`
- `generate_single_crystal_workflow(output_dir, potential_path, reference_data=None)`
- `generate_mechanics_workflow(output_dir, atoms, potential_path)`
- `generate_thermal_transport_workflow(output_dir, atoms, potential_path)`
- `run_basic_structure_analysis(atoms)`

## I/O conventions
- Structures are written in both `.extxyz` and `.xyz` where workflow generators are used.
- Workflow metadata/config files are JSON + YAML.
- GPUMD-style input templates and shell job scripts are generated as plain text.

## Extension points
- Add new builders in `diamond_simkit/builders/`.
- Add new analysis modules in `diamond_simkit/analysis/`.
- Add richer workflow templates in `diamond_simkit/workflows/`.

## Notes
- This is a lightweight skeleton and does not run expensive simulations.
- NEP potential paths are always provided by the caller (no hard-coded potential file).
