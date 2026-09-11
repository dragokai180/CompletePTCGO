from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='878bdf8b-e25d-5433-8d07-3715f4cdedf5',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SailFossil.Name',
    display_name='Sail Fossil',
    searchable_by=['Sail Fossil', 'Item', 'SailFossil'],
    subtypes=['Item'],
    collector_number=98,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the bottom 7 cards of your deck. You may reveal an Amaura you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the bottom 7 cards of your deck. You may reveal an Amaura you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
