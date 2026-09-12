from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import (
    SingleStrikeEnergyPassive, is_single_strike,
)

card = EnergyCardDef(
    guid="29bb9bbb-02ca-5e9a-8dc4-6b8ec78bbc53",
    key="SWSH5",
    name="Single Strike Energy",
    display_name="Single Strike Energy",
    searchable_by=["Single Strike Energy", "Special", "Single Strike"],
    subtypes=["Special", "Single Strike"],
    collector_number=141,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIGHTING,
    is_special=True,
    provides=[[PokemonTypes.FIGHTING], [PokemonTypes.DARKNESS]],
    attach_to=is_single_strike,
    discard_if_invalid=True,
    passive=SingleStrikeEnergyPassive(),
)
