from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='8d39e07c-2ead-54f4-9f11-c6a2f6e6c6a9',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DomeFossilKabuto.Name',
    display_name='Dome Fossil Kabuto',
    searchable_by=['Dome Fossil Kabuto', 'Item', 'DomeFossilKabuto'],
    subtypes=['Item'],
    collector_number=96,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the bottom 7 cards of your deck. You may reveal a Kabuto you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the bottom 7 cards of your deck. You may reveal a Kabuto you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
