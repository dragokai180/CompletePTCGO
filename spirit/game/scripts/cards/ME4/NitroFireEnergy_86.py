from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import energy_on_attach, standard_passive


card = EnergyCardDef(
    guid="f37baa9f-6e68-5ced-b448-25a5c47d7844",
    key="ME4",
    name="Nitro Fire Energy",
    display_name="Nitro Fire Energy",
    searchable_by=["Nitro Fire Energy", "Special", "NitroFireEnergy"],
    subtypes=["Special"],
    collector_number=86,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.FIRE,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.FIRE]],
    passive=standard_passive("As long as this card is attached to a Pokémon, it provides Fire Energy.\n \nIf this card is discarded by an effect of an attack used by the Fire Pokémon this card is attached to, put this card into your hand after attack damage and effects."),
)
