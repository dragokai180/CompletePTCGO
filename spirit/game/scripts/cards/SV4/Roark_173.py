from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='50eab561-24b0-5f10-a280-aeda11b61202',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Roark.Name',
    display_name='Roark',
    searchable_by=['Roark', 'Supporter', 'Roark'],
    subtypes=['Supporter'],
    collector_number=173,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw 2 cards. Put a Basic Energy card from your discard pile into your hand.'),
    condition=standard_trainer_condition('Draw 2 cards. Put a Basic Energy card from your discard pile into your hand.'),
)
