from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='72f9116a-7cc5-5e36-ab5e-bf1cc295dd8b',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TownStore.Name',
    display_name='Town Store',
    searchable_by=['Town Store', 'Stadium', 'TownStore'],
    subtypes=['Stadium'],
    collector_number=196,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    passive=standard_passive("Once during each player's turn, that player may search their deck for a Pokémon Tool card, reveal it, and put it into their hand. Then, that player shuffles their deck."),
    ability=standard_stadium_ability("Once during each player's turn, that player may search their deck for a Pokémon Tool card, reveal it, and put it into their hand. Then, that player shuffles their deck."),
)
