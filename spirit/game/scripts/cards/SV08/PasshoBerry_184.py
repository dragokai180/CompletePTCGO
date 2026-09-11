from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="cd78f22b-da75-5f9d-87da-25c8876359b3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PasshoBerry.Name",
    display_name="Passho Berry",
    searchable_by=["Passho Berry", "Pokémon Tool", "PasshoBerry"],
    subtypes=["Pokémon Tool"],
    collector_number=184,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is damaged by an attack from your opponent's Water Pokémon, it takes 60 less damage (after applying Weakness and Resistance), and discard this card."),
)
