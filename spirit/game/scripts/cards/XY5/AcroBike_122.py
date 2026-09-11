from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='09c2a182-8a5a-5c10-acac-589fd1281f95',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name',
    display_name='Acro Bike',
    searchable_by=['Acro Bike', 'Item', 'AcroBike'],
    subtypes=['Item'],
    collector_number=122,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 2 cards of your deck and put 1 of them into your hand. Discard the other card. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the top 2 cards of your deck and put 1 of them into your hand. Discard the other card. You may play as many Item cards as you like during your turn (before your attack).'),
)
