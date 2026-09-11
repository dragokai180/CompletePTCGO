from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='c91261c9-93cc-515f-990f-575006157dfc',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamFlareGrunt.Name',
    display_name='Team Flare Grunt',
    searchable_by=['Team Flare Grunt', 'Supporter', 'TeamFlareGrunt'],
    subtypes=['Supporter'],
    collector_number=129,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard an Energy attached to your opponent's Active Pokémon."),
    condition=standard_trainer_condition("Discard an Energy attached to your opponent's Active Pokémon."),
)
