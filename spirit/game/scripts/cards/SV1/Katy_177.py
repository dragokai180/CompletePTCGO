from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='97c80094-c35b-5cf7-a0ba-b8bcf0e9d1be',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Katy.Name',
    display_name='Katy',
    searchable_by=['Katy', 'Supporter', 'Katy'],
    subtypes=['Supporter'],
    collector_number=177,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle your hand into your deck. Then, draw 8 cards. Your turn ends.'),
    condition=standard_trainer_condition('Shuffle your hand into your deck. Then, draw 8 cards. Your turn ends.'),
)
