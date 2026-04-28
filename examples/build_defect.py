from diamond_simkit.builders.bulk import build_bulk_diamond
from diamond_simkit.builders.defects import add_substitution, add_vacancy
from diamond_simkit.io.read_write import write_dual_xyz

bulk = build_bulk_diamond(size=(2, 2, 2))
write_dual_xyz(add_vacancy(bulk, index=0), "diamond_vacancy")
write_dual_xyz(add_substitution(bulk, index=1, symbol="N"), "diamond_substitution")
print("Wrote defect structures")
