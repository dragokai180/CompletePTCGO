from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='648dacce-e658-5a62-8070-3236c9551900',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GreedyDice.Name',
    display_name='Greedy Dice',
    searchable_by=['Greedy Dice', 'Item', 'GreedyDice'],
    subtypes=['Item'],
    collector_number=102,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if you took it as a face-down Prize card, before you put it into your hand. Flip a coin. If heads, take 1 more Prize card. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('You can play this card only if you took it as a face-down Prize card, before you put it into your hand. Flip a coin. If heads, take 1 more Prize card. You may play as many Item cards as you like during your turn (before your attack).'),
)
