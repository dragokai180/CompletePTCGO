from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='b871a385-b9f5-5edf-bfb5-1cd576a90fcb',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsLecture.Name',
    display_name="Professor Elm's Lecture",
    searchable_by=["Professor Elm's Lecture", 'Supporter', 'ProfessorElmsLecture'],
    subtypes=['Supporter'],
    collector_number=188,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 3 Pokémon with 60 HP or less, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 3 Pokémon with 60 HP or less, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
