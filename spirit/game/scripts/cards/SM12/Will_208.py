from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='768308fd-7a9c-54c9-b11f-6dc17f892fda',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Will.Name',
    display_name='Will',
    searchable_by=['Will', 'Supporter', 'Will'],
    subtypes=['Supporter'],
    collector_number=208,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('The next time you flip any number of coins for the effect of an attack, Ability, or Trainer card this turn, choose heads or tails for the first coin flip.'),
    condition=standard_trainer_condition('The next time you flip any number of coins for the effect of an attack, Ability, or Trainer card this turn, choose heads or tails for the first coin flip.'),
)
