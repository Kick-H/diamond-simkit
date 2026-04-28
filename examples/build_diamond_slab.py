from diamond_simkit.builders.slabs import build_diamond_slab
from diamond_simkit.io.read_write import write_dual_xyz

atoms = build_diamond_slab(surface="111", layers=6, vacuum=12.0, size=(2, 2, 1))
write_dual_xyz(atoms, "diamond_slab")
print("Wrote diamond_slab.extxyz and diamond_slab.xyz")
