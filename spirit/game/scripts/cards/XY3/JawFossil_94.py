from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='98f9f9d7-d9ab-5369-af62-c82c5b553100',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.JawFossil.Name',
    display_name='Jaw Fossil',
    searchable_by=['Jaw Fossil', 'Item', 'JawFossil'],
    subtypes=['Item'],
    collector_number=94,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the bottom 7 cards of your deck. You may reveal a Tyrunt you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the bottom 7 cards of your deck. You may reveal a Tyrunt you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
