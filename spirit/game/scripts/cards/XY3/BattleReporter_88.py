from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='439780a0-3336-5ebe-99b8-8abfba93d6ea',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BattleReporter.Name',
    display_name='Battle Reporter',
    searchable_by=['Battle Reporter', 'Supporter', 'BattleReporter'],
    subtypes=['Supporter'],
    collector_number=88,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw cards until you have the same number of cards in your hand as your opponent.'),
    condition=standard_trainer_condition('Draw cards until you have the same number of cards in your hand as your opponent.'),
)
