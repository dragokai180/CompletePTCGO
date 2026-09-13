from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e0a5604c-9c5b-5815-a42e-8bf75db31770",
    name="Lightning Energy",
    display_name="Lightning Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=4,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
    provides=[[PokemonTypes.LIGHTNING]],
)
