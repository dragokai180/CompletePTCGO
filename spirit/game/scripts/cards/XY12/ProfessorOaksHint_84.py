from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='50303223-e9c7-5a18-bb74-27048380401a',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksHint.Name',
    display_name="Professor Oak's Hint",
    searchable_by=["Professor Oak's Hint", 'Supporter', 'ProfessorOaksHint'],
    subtypes=['Supporter'],
    collector_number=84,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw cards until you have 7 cards in your hand. Your turn ends.'),
    condition=standard_trainer_condition('Draw cards until you have 7 cards in your hand. Your turn ends.'),
)
