from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='73a1519e-35c6-58e7-aec5-7afb86491ea0',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Grusha.Name',
    display_name='Grusha',
    searchable_by=['Grusha', 'Supporter', 'Grusha'],
    subtypes=['Supporter'],
    collector_number=184,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw cards until you have 5 cards in your hand. If none of your Pokémon have any Energy attached, draw cards until you have 7 cards in your hand instead.'),
    condition=standard_trainer_condition('Draw cards until you have 5 cards in your hand. If none of your Pokémon have any Energy attached, draw cards until you have 7 cards in your hand instead.'),
)
