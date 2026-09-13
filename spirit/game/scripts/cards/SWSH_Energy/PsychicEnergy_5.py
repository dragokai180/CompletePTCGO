from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="1e29bff5-14b4-5897-b6ab-a443155656d5",
    name="Psychic Energy",
    display_name="Psychic Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=5,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
    provides=[[PokemonTypes.PSYCHIC]],
)
