from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='ad690ba9-8bfe-51d9-940a-38035f427dd5',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LifeForest.Name',
    display_name='Life Forest ◇',
    searchable_by=['Life Forest ◇', 'Stadium', 'Prism Star', 'LifeForest'],
    subtypes=['Stadium', 'Prism Star'],
    collector_number=180,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Prism,
    passive=standard_passive("Once during each player's turn, that player may heal 60 damage and remove all Special Conditions from 1 of their Grass Pokémon. Whenever any player plays an Item or Supporter card from their hand, prevent all effects of that card done to this Stadium card. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
    ability=standard_stadium_ability("Once during each player's turn, that player may heal 60 damage and remove all Special Conditions from 1 of their Grass Pokémon. Whenever any player plays an Item or Supporter card from their hand, prevent all effects of that card done to this Stadium card. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
)
