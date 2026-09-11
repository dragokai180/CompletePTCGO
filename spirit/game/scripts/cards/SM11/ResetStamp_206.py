from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='3e8493ff-cb8a-56ea-9246-910bd2e970ad',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ResetStamp.Name',
    display_name='Reset Stamp',
    searchable_by=['Reset Stamp', 'Item', 'ResetStamp'],
    subtypes=['Item'],
    collector_number=206,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent shuffles their hand into their deck and draws a card for each of their remaining Prize cards. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Your opponent shuffles their hand into their deck and draws a card for each of their remaining Prize cards. You may play as many Item cards as you like during your turn (before your attack).'),
)
