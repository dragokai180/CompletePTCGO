from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ae06480a-3ec4-5e2e-b6d1-f08c84e3a9d6",
    name="Water Energy",
    display_name="Water Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=12,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.WATER,
    is_special=False,
    provides=[[PokemonTypes.WATER]],
)
