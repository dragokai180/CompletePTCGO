from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='a5e0c70a-ae34-542b-bbab-8a774b4b9348',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name',
    display_name='Mt. Coronet',
    searchable_by=['Mt. Coronet', 'Stadium', 'MtCoronet'],
    subtypes=['Stadium'],
    collector_number=130,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may put 2 Metal Energy cards from their discard pile into their hand. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Once during each player's turn, that player may put 2 Metal Energy cards from their discard pile into their hand. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
