from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='ead80a62-5434-5b9b-a67f-7fe883f93502',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamStarGrunt.Name',
    display_name='Team Star Grunt',
    searchable_by=['Team Star Grunt', 'Supporter', 'TeamStarGrunt'],
    subtypes=['Supporter'],
    collector_number=195,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put an Energy attached to your opponent's Active Pokémon on top of their deck."),
    condition=standard_trainer_condition("Put an Energy attached to your opponent's Active Pokémon on top of their deck."),
)
