from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='b818ec09-ef33-5424-bd54-16aa869707a6',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name',
    display_name='Peeking Red Card',
    searchable_by=['Peeking Red Card', 'Item', 'PeekingRedCard'],
    subtypes=['Item'],
    collector_number=97,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent reveals their hand. You may have your opponent count the cards in their hand, shuffle those cards into their deck, then draw that many cards. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Your opponent reveals their hand. You may have your opponent count the cards in their hand, shuffle those cards into their deck, then draw that many cards. You may play as many Item cards as you like during your turn (before your attack).'),
)
