from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='7fac0e1a-7bd6-558b-990a-cb6425f0a791',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Falkner.Name',
    display_name='Falkner',
    searchable_by=['Falkner', 'Supporter', 'Falkner'],
    subtypes=['Supporter'],
    collector_number=180,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw 2 cards. If you have a Stadium in play, draw 2 more cards.'),
    condition=standard_trainer_condition('Draw 2 cards. If you have a Stadium in play, draw 2 more cards.'),
)
