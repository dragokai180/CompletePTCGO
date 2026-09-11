from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='28440831-0696-58c2-acd5-1ba1ea9f1721',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PuzzleofTime.Name',
    display_name='Puzzle of Time',
    searchable_by=['Puzzle of Time', 'Item', 'PuzzleofTime'],
    subtypes=['Item'],
    collector_number=109,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You may play 2 Puzzle of Time cards at once.\n• If you played 1 card, look at the top 3 cards of your deck and put them back in any order.\n• If you played 2 cards, put 2 cards from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('You may play 2 Puzzle of Time cards at once.\n• If you played 1 card, look at the top 3 cards of your deck and put them back in any order.\n• If you played 2 cards, put 2 cards from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)
