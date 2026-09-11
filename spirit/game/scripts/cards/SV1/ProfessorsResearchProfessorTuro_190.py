from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='4f341586-b7d6-57e6-8554-7d98c69c7d5b',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorTuro.Name',
    display_name="Professor's Research (Professor Turo)",
    searchable_by=["Professor's Research (Professor Turo)", 'Supporter', 'ProfessorsResearchProfessorTuro'],
    subtypes=['Supporter'],
    collector_number=190,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    effect=standard_trainer_effect('Discard your hand and draw 7 cards.'),
    condition=standard_trainer_condition('Discard your hand and draw 7 cards.'),
)
