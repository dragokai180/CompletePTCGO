from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5b6b2809-bd01-5e14-963a-24973bd08d35",
    name="Fire Energy",
    display_name="Fire Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=11,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.FIRE,
    is_special=False,
    provides=[[PokemonTypes.FIRE]],
)
