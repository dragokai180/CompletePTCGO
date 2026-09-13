from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="339e2675-efd0-5ccf-91ac-603712b8aadb",
    name="Lightning Energy",
    display_name="Lightning Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=13,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
    provides=[[PokemonTypes.LIGHTNING]],
)
