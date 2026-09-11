from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='e8649a0c-d2c5-5642-9348-08ae57e58148',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RedCard.Name',
    display_name='Red Card',
    searchable_by=['Red Card', 'Item', 'RedCard'],
    subtypes=['Item'],
    collector_number=124,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent shuffles his or her hand into his or her deck and draws 4 cards. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Your opponent shuffles his or her hand into his or her deck and draws 4 cards. You may play as many Item cards as you like during your turn (before your attack).'),
)
