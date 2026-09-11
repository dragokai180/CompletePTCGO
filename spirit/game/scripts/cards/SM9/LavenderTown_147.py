from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='6a6dbfa1-4f6d-5511-82d2-6a709d43bb5d',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LavenderTown.Name',
    display_name='Lavender Town',
    searchable_by=['Lavender Town', 'Stadium', 'LavenderTown'],
    subtypes=['Stadium'],
    collector_number=147,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may have their opponent reveal their hand. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Once during each player's turn, that player may have their opponent reveal their hand. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
