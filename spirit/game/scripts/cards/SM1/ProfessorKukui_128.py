from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='1a6ed5b9-7cf5-5a75-a2dd-8cce5b230615',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorKukui.Name',
    display_name='Professor Kukui',
    searchable_by=['Professor Kukui', 'Supporter', 'ProfessorKukui'],
    subtypes=['Supporter'],
    collector_number=128,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw 2 cards. During this turn, your Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
    condition=standard_trainer_condition("Draw 2 cards. During this turn, your Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
)
