from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='06959e7b-0e76-59f4-b155-9834bb527048',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ClawFossilAnorith.Name',
    display_name='Claw Fossil Anorith',
    searchable_by=['Claw Fossil Anorith', 'Item', 'ClawFossilAnorith'],
    subtypes=['Item'],
    collector_number=100,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the bottom 7 cards of your deck. You may reveal an Anorith you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the bottom 7 cards of your deck. You may reveal an Anorith you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
