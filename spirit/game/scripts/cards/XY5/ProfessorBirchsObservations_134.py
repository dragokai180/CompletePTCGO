from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='96ce1699-6cd9-5e75-8112-fd1d12abe42a',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirchsObservations.Name',
    display_name="Professor Birch's Observations",
    searchable_by=["Professor Birch's Observations", 'Supporter', 'ProfessorBirchsObservations'],
    subtypes=['Supporter'],
    collector_number=134,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle your hand into your deck and flip a coin. If heads, draw 7 cards. If tails, draw 4 cards.'),
    condition=standard_trainer_condition('Shuffle your hand into your deck and flip a coin. If heads, draw 7 cards. If tails, draw 4 cards.'),
)
