from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='aeb5c2c2-5fa2-5bd2-a7a9-1e7521f2172f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Mesagoza.Name',
    display_name='Mesagoza',
    searchable_by=['Mesagoza', 'Stadium', 'Mesagoza'],
    subtypes=['Stadium'],
    collector_number=178,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may flip a coin. If heads, that player searches their deck for a Pokémon, reveals it, and puts it into their hand. Then, that player shuffles their deck."),
    ability=standard_stadium_ability("Once during each player's turn, that player may flip a coin. If heads, that player searches their deck for a Pokémon, reveals it, and puts it into their hand. Then, that player shuffles their deck."),
)
