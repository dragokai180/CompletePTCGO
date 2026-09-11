from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='d55a84b8-e829-59e9-b5ad-4385c293296b',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name',
    display_name='Gym Badge',
    searchable_by=['Gym Badge', 'Item', 'GymBadge'],
    subtypes=['Item'],
    collector_number=203,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    effect=standard_trainer_effect('Flip a coin until you get tails. For each heads, draw a card. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Flip a coin until you get tails. For each heads, draw a card. You may play as many Item cards as you like during your turn (before your attack).'),
)
