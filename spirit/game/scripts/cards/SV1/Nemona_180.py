from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='6d6b1175-2be7-5dec-b03f-927ccfe538a3',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Nemona.Name',
    display_name='Nemona',
    searchable_by=['Nemona', 'Supporter', 'Nemona'],
    subtypes=['Supporter'],
    collector_number=180,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    effect=standard_trainer_effect('Draw 3 cards.'),
    condition=standard_trainer_condition('Draw 3 cards.'),
)
