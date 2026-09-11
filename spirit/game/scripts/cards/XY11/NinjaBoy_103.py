from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='c3d648fc-4092-59c9-89a1-ac8b7d792683',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.NinjaBoy.Name',
    display_name='Ninja Boy',
    searchable_by=['Ninja Boy', 'Supporter', 'NinjaBoy'],
    subtypes=['Supporter'],
    collector_number=103,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose 1 of your Basic Pokémon in play. Search your deck for a Basic Pokémon and switch it with that Pokémon. (Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon.) Shuffle the first Pokémon into your deck.'),
    condition=standard_trainer_condition('Choose 1 of your Basic Pokémon in play. Search your deck for a Basic Pokémon and switch it with that Pokémon. (Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon.) Shuffle the first Pokémon into your deck.'),
)
