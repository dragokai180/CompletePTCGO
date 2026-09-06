"""Rapid Strike Energy (SWSH - Battle Styles 182/163), the secret print.

Same card as 140; see that file for the rules and why the stub was wrong.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.scripts.cards.SWSH5.RapidStrikeEnergy_140 import (
    RAPID_STRIKE_PROVIDES, is_rapid_strike,
)

card = EnergyCardDef(
    guid="57d1f07b-1683-5680-b861-dae0746d804f",
    key="SWSH5",
    name="Rapid Strike Energy",
    display_name="Rapid Strike Energy",
    searchable_by=["Rapid Strike Energy", "Special", "Rapid Strike"],
    subtypes=["Special", "Rapid Strike"],
    collector_number=182,
    set_code="SWSH5",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=is_rapid_strike,
    discard_if_invalid=True,
    provides=RAPID_STRIKE_PROVIDES,
)
