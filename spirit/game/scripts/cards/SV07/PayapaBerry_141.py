from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="f755d55b-27d3-5dbc-87f6-17ea6b487896",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PayapaBerry.Name",
    display_name="Payapa Berry",
    searchable_by=["Payapa Berry", "Pokémon Tool", "PayapaBerry"],
    subtypes=["Pokémon Tool"],
    collector_number=141,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is damaged by an attack from your opponent's Psychic Pokémon, it takes 60 less damage (after applying Weakness and Resistance), and discard this card."),
)
