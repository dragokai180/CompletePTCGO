from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='886ab84e-6600-575e-bf9e-5cd670cba2c4',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DaisysHelp.Name',
    display_name="Daisy's Help",
    searchable_by=["Daisy's Help", 'Supporter', 'DaisysHelp'],
    subtypes=['Supporter'],
    collector_number=158,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw 2 cards. Look at your face-down Prize cards.'),
    condition=standard_trainer_condition('Draw 2 cards. Look at your face-down Prize cards.'),
)
