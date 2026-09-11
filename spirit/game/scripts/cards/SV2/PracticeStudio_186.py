from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='9a22b83b-1602-5a98-9ecd-6d55c80164dd',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PracticeStudio.Name',
    display_name='Practice Studio',
    searchable_by=['Practice Studio', 'Stadium', 'PracticeStudio'],
    subtypes=['Stadium'],
    collector_number=186,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("The attacks of Stage 1 Pokémon (both yours and your opponent's) do 10 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance)."),
    ability=standard_stadium_ability("The attacks of Stage 1 Pokémon (both yours and your opponent's) do 10 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance)."),
)
