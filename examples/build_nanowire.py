from diamond_simkit.builders.nanowires import build_diamond_nanowire
from diamond_simkit.io.read_write import write_dual_xyz

atoms = build_diamond_nanowire(cross_section="hexagonal", length=40.0, width=12.0)
write_dual_xyz(atoms, "diamond_nanowire")
print("Wrote diamond_nanowire.extxyz and diamond_nanowire.xyz")
