from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='4de1e30b-73fc-5ed3-815d-69d6aa6ac57f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BeachCourt.Name',
    display_name='Beach Court',
    searchable_by=['Beach Court', 'Stadium', 'BeachCourt'],
    subtypes=['Stadium'],
    collector_number=167,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Retreat Cost of each Basic Pokémon in play (both yours and your opponent's) is Colorless less."),
    ability=standard_stadium_ability("The Retreat Cost of each Basic Pokémon in play (both yours and your opponent's) is Colorless less."),
)
