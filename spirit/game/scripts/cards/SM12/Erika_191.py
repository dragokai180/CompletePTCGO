from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='300486c6-3ec5-5def-85b2-26398321ac90',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name',
    display_name='Erika',
    searchable_by=['Erika', 'Supporter', 'Erika'],
    subtypes=['Supporter'],
    collector_number=191,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Each player may draw up to 3 cards. You draw first.'),
    condition=standard_trainer_condition('Each player may draw up to 3 cards. You draw first.'),
)
