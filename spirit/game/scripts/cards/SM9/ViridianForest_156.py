from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='703e2173-f13f-50ed-9daf-9878cfb83ddc',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ViridianForest.Name',
    display_name='Viridian Forest',
    searchable_by=['Viridian Forest', 'Stadium', 'ViridianForest'],
    subtypes=['Stadium'],
    collector_number=156,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for a basic Energy card, reveals it, and puts it into their hand. Then, that player shuffles their deck. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for a basic Energy card, reveals it, and puts it into their hand. Then, that player shuffles their deck. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
