from ase.build import graphene

from diamond_simkit.builders.bulk import build_bulk_diamond
from diamond_simkit.builders.interfaces import build_simple_interface
from diamond_simkit.io.read_write import write_dual_xyz

d = build_bulk_diamond(size=(2, 2, 1))
g = graphene(vacuum=10.0).repeat((2, 2, 1))
interface = build_simple_interface(d, g, gap=2.5)
write_dual_xyz(interface, "diamond_graphene_interface")
print("Wrote interface structure")
