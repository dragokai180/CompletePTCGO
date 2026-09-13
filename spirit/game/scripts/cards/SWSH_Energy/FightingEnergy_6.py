from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d9575e4f-c7da-5847-b724-132ce0e115fd",
    name="Fighting Energy",
    display_name="Fighting Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=6,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
    provides=[[PokemonTypes.FIGHTING]],
)
