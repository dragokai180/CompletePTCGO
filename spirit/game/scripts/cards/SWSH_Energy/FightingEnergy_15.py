from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="0d7c55e3-aaea-5f66-9a00-f15292ab9b05",
    name="Fighting Energy",
    display_name="Fighting Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=15,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
    provides=[[PokemonTypes.FIGHTING]],
)
