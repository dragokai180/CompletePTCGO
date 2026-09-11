from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='b43d09c8-ab22-5d3b-af7f-6f3481608951',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Gladion.Name',
    display_name='Gladion',
    searchable_by=['Gladion', 'Supporter', 'Gladion'],
    subtypes=['Supporter'],
    collector_number=95,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Look at your face-down Prize cards and put 1 of them into your hand. Then, shuffle this Gladion into your remaining Prize cards and put them back face down. If you didn't play this Gladion from your hand, it does nothing."),
    condition=standard_trainer_condition("Look at your face-down Prize cards and put 1 of them into your hand. Then, shuffle this Gladion into your remaining Prize cards and put them back face down. If you didn't play this Gladion from your hand, it does nothing."),
)
