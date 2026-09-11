from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='7a3a1e37-bc5d-5013-97ab-eb2d8be9d33c',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MoonlitHill.Name',
    display_name='Moonlit Hill',
    searchable_by=['Moonlit Hill', 'Stadium', 'MoonlitHill'],
    subtypes=['Stadium'],
    collector_number=81,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may discard a Basic Psychic Energy card from their hand in order to heal 30 damage from each of their Pokémon."),
    ability=standard_stadium_ability("Once during each player's turn, that player may discard a Basic Psychic Energy card from their hand in order to heal 30 damage from each of their Pokémon."),
)
