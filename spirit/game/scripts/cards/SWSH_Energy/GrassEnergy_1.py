from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="44d4229c-6f68-5aeb-a875-400c0c36d3d8",
    name="Grass Energy",
    display_name="Grass Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=1,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.GRASS,
    is_special=False,
    provides=[[PokemonTypes.GRASS]],
)
