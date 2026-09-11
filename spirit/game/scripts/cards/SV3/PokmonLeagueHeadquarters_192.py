from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='e8f78bfd-5a07-572b-a543-4adaeeab84b1',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokmonLeagueHeadquarters.Name',
    display_name='Pokémon League Headquarters',
    searchable_by=['Pokémon League Headquarters', 'Stadium', 'PokmonLeagueHeadquarters'],
    subtypes=['Stadium'],
    collector_number=192,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("Attacks used by each Basic Pokémon in play (both yours and your opponent's) cost Colorless more."),
    ability=standard_stadium_ability("Attacks used by each Basic Pokémon in play (both yours and your opponent's) cost Colorless more."),
)
