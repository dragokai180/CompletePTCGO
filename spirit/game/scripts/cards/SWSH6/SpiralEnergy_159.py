from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME, SpiralEnergyPassive,
    cure_paralysis_on_attach, is_rapid_strike,
)

card = EnergyCardDef(
    guid="864d97da-55bc-5a68-95d2-6f0c01b5dce9",
    key="SWSH6",
    name="Spiral Energy",
    display_name="Spiral Energy",
    searchable_by=["Spiral Energy", "Special", "Rapid Strike"],
    subtypes=["Special", "Rapid Strike"],
    collector_number=159,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[],
    provides=ALL_TYPES_ONE_AT_A_TIME,
    attach_to=is_rapid_strike,
    discard_if_invalid=True,
    passive=SpiralEnergyPassive(),
    on_attach_anywhere=cure_paralysis_on_attach,
)
