from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='19baa988-4599-57a9-a76f-6c7d9fd87212',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TrickShovel.Name',
    display_name='Trick Shovel',
    searchable_by=['Trick Shovel', 'Item', 'TrickShovel'],
    subtypes=['Item'],
    collector_number=98,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Look at the top card of either player's deck. You may discard that card or return it to the top of the deck. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Look at the top card of either player's deck. You may discard that card or return it to the top of the deck. You may play as many Item cards as you like during your turn (before your attack)."),
)
