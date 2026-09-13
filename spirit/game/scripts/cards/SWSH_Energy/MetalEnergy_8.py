from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c040e3cc-02d0-550b-927b-75b379c17a6a",
    name="Metal Energy",
    display_name="Metal Energy",
    key="SWSH_Energy",
    set_code="SWSH_Energy",
    collector_number=8,
    rarity=Rarities.Common,
    subtypes=["Basic"],
    energy_type=PokemonTypes.METAL,
    is_special=False,
    provides=[[PokemonTypes.METAL]],
)
