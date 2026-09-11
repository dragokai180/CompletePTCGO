from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='cf211409-753a-597d-8e7c-4dd579656076',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Whitney.Name',
    display_name='Whitney',
    searchable_by=['Whitney', 'Supporter', 'Whitney'],
    subtypes=['Supporter'],
    collector_number=193,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw a card. Then, draw 2 cards for each other Whitney in your discard pile.'),
    condition=standard_trainer_condition('Draw a card. Then, draw 2 cards for each other Whitney in your discard pile.'),
)
