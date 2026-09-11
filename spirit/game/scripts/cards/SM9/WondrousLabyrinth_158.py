from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='d51677c0-4efd-53b4-b1fb-50b59414cb3e',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.WondrousLabyrinth.Name',
    display_name='Wondrous Labyrinth ◇',
    searchable_by=['Wondrous Labyrinth ◇', 'Stadium', 'Prism Star', 'WondrousLabyrinth'],
    subtypes=['Stadium', 'Prism Star'],
    collector_number=158,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Prism,
    passive=standard_passive("The attacks of non-Fairy Pokémon (both yours and your opponent's) cost Colorless more. Whenever any player plays an Item or Supporter card from their hand, prevent all effects of that card done to this Stadium card. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
    ability=standard_stadium_ability("The attacks of non-Fairy Pokémon (both yours and your opponent's) cost Colorless more. Whenever any player plays an Item or Supporter card from their hand, prevent all effects of that card done to this Stadium card. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
)
