from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='cc04ff4f-1f85-5756-a89b-1280113a5999',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BurnedTower.Name',
    display_name='Burned Tower',
    searchable_by=['Burned Tower', 'Stadium', 'BurnedTower'],
    subtypes=['Stadium'],
    collector_number=71,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. Once during each player's turn, that player may flip a coin. If heads, the player searches his or her discard pile for a basic Energy card, shows it to his or her opponent, and put it into his or her hand."),
    ability=standard_stadium_ability("This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. Once during each player's turn, that player may flip a coin. If heads, the player searches his or her discard pile for a basic Energy card, shows it to his or her opponent, and put it into his or her hand."),
)
