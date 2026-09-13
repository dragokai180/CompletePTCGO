from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="48721043-53c5-55a7-a5a7-b02fe85c942a",
    name="Water Energy",
    display_name="Water Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=3,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.WATER,
    is_special=False,
    provides=[[PokemonTypes.WATER]],
)
