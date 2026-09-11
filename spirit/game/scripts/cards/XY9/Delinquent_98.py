from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='69bcc164-329e-5742-b18a-d8992a01cef1',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Delinquent.Name',
    display_name='Delinquent',
    searchable_by=['Delinquent', 'Supporter', 'Delinquent'],
    subtypes=['Supporter'],
    collector_number=98,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard any Stadium card in play. If you do, your opponent discards 3 cards from his or her hand.'),
    condition=standard_trainer_condition('Discard any Stadium card in play. If you do, your opponent discards 3 cards from his or her hand.'),
)
