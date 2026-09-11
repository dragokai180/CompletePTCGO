from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='40fa2b61-b005-5839-8432-f96e46f5ceeb',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HelixFossilOmanyte.Name',
    display_name='Helix Fossil Omanyte',
    searchable_by=['Helix Fossil Omanyte', 'Item', 'HelixFossilOmanyte'],
    subtypes=['Item'],
    collector_number=102,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the bottom 7 cards of your deck. You may reveal an Omanyte you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the bottom 7 cards of your deck. You may reveal an Omanyte you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
