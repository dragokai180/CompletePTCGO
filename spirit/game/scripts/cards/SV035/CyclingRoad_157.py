from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='adbcba36-4bf2-519f-a3cc-23f3f588dbc5',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CyclingRoad.Name',
    display_name='Cycling Road',
    searchable_by=['Cycling Road', 'Stadium', 'CyclingRoad'],
    subtypes=['Stadium'],
    collector_number=157,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may discard a Basic Energy card from their hand in order to draw a card."),
    ability=standard_stadium_ability("Once during each player's turn, that player may discard a Basic Energy card from their hand in order to draw a card."),
)
