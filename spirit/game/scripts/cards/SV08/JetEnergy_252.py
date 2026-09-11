from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import energy_on_attach, standard_passive


card = EnergyCardDef(
    guid="fda183f0-978f-5211-aa20-d3d59fdd998d",
    key="SV08",
    name="Jet Energy",
    display_name="Jet Energy",
    searchable_by=["Jet Energy", "Special", "JetEnergy"],
    subtypes=["Special"],
    collector_number=252,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareRainbow,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive("As long as this card is attached to a Pokémon, it provides Colorless Energy.  When you attach this card from your hand to 1 of your Benched Pokémon, switch that Pokémon with your Active Pokémon."),
    on_attach=energy_on_attach("As long as this card is attached to a Pokémon, it provides Colorless Energy.  When you attach this card from your hand to 1 of your Benched Pokémon, switch that Pokémon with your Active Pokémon."),
)
