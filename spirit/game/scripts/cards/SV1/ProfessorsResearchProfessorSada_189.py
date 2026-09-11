from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='7f3d1151-4e54-55b4-90f0-277d08bb70a8',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorSada.Name',
    display_name="Professor's Research (Professor Sada)",
    searchable_by=["Professor's Research (Professor Sada)", 'Supporter', 'ProfessorsResearchProfessorSada'],
    subtypes=['Supporter'],
    collector_number=189,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    effect=standard_trainer_effect('Discard your hand and draw 7 cards.'),
    condition=standard_trainer_condition('Discard your hand and draw 7 cards.'),
)
