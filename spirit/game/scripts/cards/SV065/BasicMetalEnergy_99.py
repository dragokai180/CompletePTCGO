from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import energy_on_attach, standard_passive


card = EnergyCardDef(
    guid="b3e671a6-3256-5245-baee-698ecd61a053",
    key="SV065",
    name="Basic Metal Energy",
    display_name="Basic Metal Energy",
    searchable_by=["Basic Metal Energy", "Basic", "BasicMetalEnergy"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SV065",
    regulation_mark=None,
    rarity=Rarities.RareRainbow,
    energy_type=PokemonTypes.METAL,
    is_special=False,
    provides=[[PokemonTypes.METAL]],
)
