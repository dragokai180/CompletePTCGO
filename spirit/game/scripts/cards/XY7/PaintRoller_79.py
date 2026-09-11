from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='b15e2067-8360-58c1-b37c-ffea09f3bcd5',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PaintRoller.Name',
    display_name='Paint Roller',
    searchable_by=['Paint Roller', 'Item', 'PaintRoller'],
    subtypes=['Item'],
    collector_number=79,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard any Stadium card in play. Then, draw a card. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Discard any Stadium card in play. Then, draw a card. You may play as many Item cards as you like during your turn (before your attack).'),
)
