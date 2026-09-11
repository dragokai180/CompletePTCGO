from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='724a30bb-19c2-58fc-8719-cb20ccaa5826',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Morty.Name',
    display_name='Morty',
    searchable_by=['Morty', 'Supporter', 'Morty'],
    subtypes=['Supporter'],
    collector_number=186,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if 1 of your Psychic Pokémon was Knocked Out during your opponent's last turn. Your opponent reveals their hand. Choose 2 cards you find there. Your opponent shuffles those cards into their deck."),
    condition=standard_trainer_condition("You can play this card only if 1 of your Psychic Pokémon was Knocked Out during your opponent's last turn. Your opponent reveals their hand. Choose 2 cards you find there. Your opponent shuffles those cards into their deck."),
)
