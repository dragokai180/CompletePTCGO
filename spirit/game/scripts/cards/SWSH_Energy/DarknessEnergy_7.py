from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="742c12f9-72a6-5afe-87a3-1f44e4fa95c6",
    name="Darkness Energy",
    display_name="Darkness Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=7,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
    provides=[[PokemonTypes.DARKNESS]],
)
