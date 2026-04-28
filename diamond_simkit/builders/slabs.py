"""Slab and 2D-like builders."""

from ase import Atoms
from ase.build import graphene, surface

from diamond_simkit.builders.bulk import build_bulk_diamond

_SURFACE_MAP = {
    "100": (1, 0, 0),
    "110": (1, 1, 0),
    "111": (1, 1, 1),
}


def build_diamond_slab(
    surface: str = "100",
    layers: int = 8,
    vacuum: float = 15.0,
    size: tuple[int, int, int] = (4, 4, 1),
) -> Atoms:
    """Build a diamond slab for selected Miller surfaces."""
    if surface not in _SURFACE_MAP:
        raise ValueError(f"Unsupported surface '{surface}'. Use one of {list(_SURFACE_MAP)}")
    base = build_bulk_diamond(size=(1, 1, 1))
    slab = surface_fn(base, _SURFACE_MAP[surface], layers, vacuum)
    return slab.repeat(size)


def surface_fn(base: Atoms, miller: tuple[int, int, int], layers: int, vacuum: float) -> Atoms:
    return surface(base, miller, layers=layers, vacuum=vacuum)


def build_graphene_like_sheet(size: tuple[int, int, int] = (4, 4, 1), vacuum: float = 15.0) -> Atoms:
    """Simple graphene-like sheet helper for 2D carbon workflows."""
    sheet = graphene(vacuum=vacuum)
    return sheet.repeat(size)
