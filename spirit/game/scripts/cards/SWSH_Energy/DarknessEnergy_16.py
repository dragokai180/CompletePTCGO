from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7fae7190-f2a4-5103-bacf-0fef01671f00",
    name="Darkness Energy",
    display_name="Darkness Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=16,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
    provides=[[PokemonTypes.DARKNESS]],
)
