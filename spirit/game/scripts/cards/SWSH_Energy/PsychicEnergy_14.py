from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="87927e3b-61d0-5547-a827-339fefaf74e7",
    name="Psychic Energy",
    display_name="Psychic Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=14,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
    provides=[[PokemonTypes.PSYCHIC]],
)
