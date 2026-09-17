from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import energy_on_attach, standard_passive


card = EnergyCardDef(
    guid="d23c26b2-8e5c-558d-9078-6329162bc497",
    key="SV06",
    name="Luminous Energy",
    display_name="Luminous Energy",
    searchable_by=["Luminous Energy", "Special", "LuminousEnergy"],
    subtypes=["Special"],
    collector_number=226,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareRainbow,
    energy_type=PokemonTypes.GRASS,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.GRASS], [PokemonTypes.FIRE], [PokemonTypes.WATER], [PokemonTypes.LIGHTNING], [PokemonTypes.PSYCHIC], [PokemonTypes.FIGHTING], [PokemonTypes.DARKNESS], [PokemonTypes.METAL]],
    passive=standard_passive("As long as this card is attached to a Pokémon, it provides every type of Energy but provides only 1 Energy at a time.  If the Pokémon this card is attached to has any other Special Energy attached, this card provides Colorless Energy instead."),
)
