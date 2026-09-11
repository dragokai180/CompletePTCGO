from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='af3cefab-7d0b-5df3-a403-f80dec3701c3',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Iono.Name',
    display_name='Iono',
    searchable_by=['Iono', 'Supporter', 'Iono'],
    subtypes=['Supporter'],
    collector_number=185,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Each player shuffles their hand and puts it on the bottom of their deck. If either player put any cards on the bottom of their deck in this way, each player draws a card for each of their remaining Prize cards.'),
    condition=standard_trainer_condition('Each player shuffles their hand and puts it on the bottom of their deck. If either player put any cards on the bottom of their deck in this way, each player draws a card for each of their remaining Prize cards.'),
)
