from diamond_simkit.builders.bulk import build_bulk_diamond
from diamond_simkit.io.read_write import write_dual_xyz

atoms = build_bulk_diamond(a=3.567, size=(2, 2, 2))
write_dual_xyz(atoms, "bulk_diamond")
print("Wrote bulk_diamond.extxyz and bulk_diamond.xyz")
