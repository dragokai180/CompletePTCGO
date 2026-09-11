from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='b3f7ca8f-d81a-5893-b7e7-c9e7bc56799a',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ReservedTicket.Name',
    display_name='Reserved Ticket',
    searchable_by=['Reserved Ticket', 'Item', 'ReservedTicket'],
    subtypes=['Item'],
    collector_number=147,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, search your deck for a card, shuffle your deck, then put that card on top of it. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Flip a coin. If heads, search your deck for a card, shuffle your deck, then put that card on top of it. You may play as many Item cards as you like during your turn (before your attack).'),
)
