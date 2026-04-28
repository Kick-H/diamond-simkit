"""Template generators for simple workflow files."""


def gpumd_minimize_template(structure_file: str, potential_file: str) -> str:
    return f"""# Example GPUMD-like input (template)
potential {potential_file}
read_xyz {structure_file}
minimize 1e-6 5000
"""


def slurm_template(job_name: str, command: str = "python postprocess.py") -> str:
    return f"""#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --time=00:10:00
#SBATCH --ntasks=1

{command}
"""
