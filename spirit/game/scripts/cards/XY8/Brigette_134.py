from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='562e45e6-0f03-5a12-b9b3-9be90088ecb3',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Brigette.Name',
    display_name='Brigette',
    searchable_by=['Brigette', 'Supporter', 'Brigette'],
    subtypes=['Supporter'],
    collector_number=134,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for 1 Basic Pokémon-EX or 3 Basic Pokémon (except for Pokémon-EX) and put them onto your Bench. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Search your deck for 1 Basic Pokémon-EX or 3 Basic Pokémon (except for Pokémon-EX) and put them onto your Bench. Shuffle your deck afterward.'),
)
