from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='e63bb517-bde7-5919-a3b4-d5f6b02fceeb',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Wicke.Name',
    display_name='Wicke',
    searchable_by=['Wicke', 'Supporter', 'Wicke'],
    subtypes=['Supporter'],
    collector_number=127,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Each player counts the cards in their hand, shuffles those cards into their deck, then draws that many cards.'),
    condition=standard_trainer_condition('Each player counts the cards in their hand, shuffles those cards into their deck, then draws that many cards.'),
)
