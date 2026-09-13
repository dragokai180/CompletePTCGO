from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="b5c555fb-79c9-56cd-a25a-c6dd6af50214",
    name="Grass Energy",
    display_name="Grass Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=10,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.GRASS,
    is_special=False,
    provides=[[PokemonTypes.GRASS]],
)
