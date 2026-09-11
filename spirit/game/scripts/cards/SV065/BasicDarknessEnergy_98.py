from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import energy_on_attach, standard_passive


card = EnergyCardDef(
    guid="b96cad3e-efd4-51ed-bb6f-a217e7e99d64",
    key="SV065",
    name="Basic Darkness Energy",
    display_name="Basic Darkness Energy",
    searchable_by=["Basic Darkness Energy", "Basic", "BasicDarknessEnergy"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SV065",
    regulation_mark=None,
    rarity=Rarities.RareRainbow,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
    provides=[[PokemonTypes.DARKNESS]],
)
