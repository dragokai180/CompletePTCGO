from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="b79ec477-fa6a-570b-88c1-2bf01dd91003",
    name="Fairy Energy",
    display_name="Fairy Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=9,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.FAIRY,
    is_special=False,
    provides=[[PokemonTypes.FAIRY]],
)
