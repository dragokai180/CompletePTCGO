from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='818de1d4-6a4e-585f-af57-b03b0b3a7dd9',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name',
    display_name='Lusamine',
    searchable_by=['Lusamine', 'Supporter', 'Lusamine'],
    subtypes=['Supporter'],
    collector_number=96,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 2 in any combination of Supporter and Stadium cards from your discard pile into your hand.'),
    condition=standard_trainer_condition('Put 2 in any combination of Supporter and Stadium cards from your discard pile into your hand.'),
)
