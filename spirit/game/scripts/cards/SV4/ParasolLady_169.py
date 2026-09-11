from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='2012bb05-1b6c-5c3b-aefd-3f055e3b3b49',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ParasolLady.Name',
    display_name='Parasol Lady',
    searchable_by=['Parasol Lady', 'Supporter', 'ParasolLady'],
    subtypes=['Supporter'],
    collector_number=169,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Shuffle your hand into your deck. Then, draw 4 cards. If you go second and it's your first turn, draw 8 cards instead."),
    condition=standard_trainer_condition("Shuffle your hand into your deck. Then, draw 4 cards. If you go second and it's your first turn, draw 8 cards instead."),
)
