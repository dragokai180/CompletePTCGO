from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='f7f04d60-e7bd-5505-afa0-fa7a659625b4',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name',
    display_name='Here Comes Team Rocket!',
    searchable_by=['Here Comes Team Rocket!', 'Supporter', 'HereComesTeamRocket'],
    subtypes=['Supporter'],
    collector_number=113,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareSecret,
    effect=standard_trainer_effect('Each player turns all of his or her Prize cards face up. (Those Prize cards remain face up for the rest of the game.)'),
    condition=standard_trainer_condition('Each player turns all of his or her Prize cards face up. (Those Prize cards remain face up for the rest of the game.)'),
)
