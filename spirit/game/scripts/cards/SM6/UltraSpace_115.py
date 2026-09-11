from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='275ec1de-d82c-5643-8416-eb4529477822',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.UltraSpace.Name',
    display_name='Ultra Space',
    searchable_by=['Ultra Space', 'Stadium', 'UltraSpace'],
    subtypes=['Stadium'],
    collector_number=115,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may search their deck for an Ultra Beast card, reveal it, put it into their hand, and shuffle their deck. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Once during each player's turn, that player may search their deck for an Ultra Beast card, reveal it, put it into their hand, and shuffle their deck. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
