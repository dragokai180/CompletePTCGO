from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='7117ef04-9e42-5aa4-a20e-39951495e458',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHandiwork.Name',
    display_name="Team Rocket's Handiwork",
    searchable_by=["Team Rocket's Handiwork", 'Supporter', 'TeamRocketsHandiwork'],
    subtypes=['Supporter'],
    collector_number=112,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Flip 2 coins. For each heads, discard 2 cards from the top of your opponent's deck."),
    condition=standard_trainer_condition("Flip 2 coins. For each heads, discard 2 cards from the top of your opponent's deck."),
)
