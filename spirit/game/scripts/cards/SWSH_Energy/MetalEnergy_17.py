from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="747d59d2-7f60-5b20-94d7-4e8eac6ffd85",
    name="Metal Energy",
    display_name="Metal Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=17,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.METAL,
    is_special=False,
    provides=[[PokemonTypes.METAL]],
)
