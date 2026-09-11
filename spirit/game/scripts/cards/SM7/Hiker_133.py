from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='5c0b86c8-f5b9-54aa-9692-2488c3ecc3c8',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Hiker.Name',
    display_name='Hiker',
    searchable_by=['Hiker', 'Supporter', 'Hiker'],
    subtypes=['Supporter'],
    collector_number=133,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Look at the top 5 cards of either player's deck and choose 1 of them. That player shuffles the other cards back into their deck. Then, put the card you chose on top of that deck."),
    condition=standard_trainer_condition("Look at the top 5 cards of either player's deck and choose 1 of them. That player shuffles the other cards back into their deck. Then, put the card you chose on top of that deck."),
)
