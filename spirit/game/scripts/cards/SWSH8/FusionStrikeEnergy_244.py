from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME, FusionStrikeEnergyPassive, is_fusion_strike,
)

card = EnergyCardDef(
    guid="a1be9557-4439-5c31-8c90-51a75824090f",
    key="SWSH8",
    name="Fusion Strike Energy",
    display_name="Fusion Strike Energy",
    searchable_by=["Fusion Strike Energy", "Fusion Strike", "Special"],
    subtypes=["Fusion Strike", "Special"],
    collector_number=244,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[],
    provides=ALL_TYPES_ONE_AT_A_TIME,
    attach_to=is_fusion_strike,
    discard_if_invalid=True,
    passive=FusionStrikeEnergyPassive(),
)
