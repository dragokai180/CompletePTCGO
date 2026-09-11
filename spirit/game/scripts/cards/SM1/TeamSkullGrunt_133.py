from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='f720cf14-1b8b-5fff-a6c5-f214c017a59e',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamSkullGrunt.Name',
    display_name='Team Skull Grunt',
    searchable_by=['Team Skull Grunt', 'Supporter', 'TeamSkullGrunt'],
    subtypes=['Supporter'],
    collector_number=133,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent reveals their hand. Discard 2 Energy cards from it.'),
    condition=standard_trainer_condition('Your opponent reveals their hand. Discard 2 Energy cards from it.'),
)
