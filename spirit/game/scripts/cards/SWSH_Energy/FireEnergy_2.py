from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="733ccbe3-2af0-5c0e-949a-d7bf3daf2786",
    name="Fire Energy",
    display_name="Fire Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=2,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.FIRE,
    is_special=False,
    provides=[[PokemonTypes.FIRE]],
)
