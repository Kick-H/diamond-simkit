from diamond_simkit.builders.bulk import build_bulk_diamond
from diamond_simkit.workflows.mechanics import generate_mechanics_workflow
from diamond_simkit.workflows.single_crystal import generate_single_crystal_workflow
from diamond_simkit.workflows.thermal_transport import generate_thermal_transport_workflow

potential_path = "./nep.txt"  # user supplied
atoms = build_bulk_diamond(size=(2, 2, 2))

generate_single_crystal_workflow("workflows/single_crystal", potential_path)
generate_mechanics_workflow("workflows/mechanics", atoms, potential_path)
generate_thermal_transport_workflow("workflows/thermal", atoms, potential_path)
print("Generated workflow templates")
