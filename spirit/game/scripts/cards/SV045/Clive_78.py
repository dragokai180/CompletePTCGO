from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='947eb103-dcce-563c-ba56-b9ea4e067858',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Clive.Name',
    display_name='Clive',
    searchable_by=['Clive', 'Supporter', 'Clive'],
    subtypes=['Supporter'],
    collector_number=78,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent reveals their hand, and you draw 2 cards for each Supporter card you find there.'),
    condition=standard_trainer_condition('Your opponent reveals their hand, and you draw 2 cards for each Supporter card you find there.'),
)
