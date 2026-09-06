"""Double Colorless Energy (SM - Sun & Moon 136/149).

Special Energy.

  "Double Colorless Energy provides [C][C] Energy."

Double Turbo Energy without the drawback: the same
provides=[[COLORLESS, COLORLESS]], and no passive at all, since nothing
on this card reduces damage. It also carries none of Double Dragon
Energy's baggage -- no attach_to restriction and so no
discard_if_invalid, because it goes on anything.

The single provides group is what makes it pay two Colorless at once.
One group means one indivisible package: a cost asking for a single [C]
still spends the whole card, which is the printed behaviour.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="69735f07-7c96-5723-a8f8-81b6e5e604e5",
    key="SM1",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special", "DoubleColorlessEnergy"],
    subtypes=["Special"],
    collector_number=136,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
)
