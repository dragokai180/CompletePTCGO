from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ea39c280-408d-597b-9a7d-d7586e5ea8e2',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.OrderPad.Name',
    display_name='Order Pad',
    searchable_by=['Order Pad', 'Item', 'OrderPad'],
    subtypes=['Item'],
    collector_number=131,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Flip a coin. If heads, search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
