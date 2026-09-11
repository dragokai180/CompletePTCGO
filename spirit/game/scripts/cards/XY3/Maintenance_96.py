from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='9ea50b4a-94e5-5594-bd1d-f5bf360a35c6',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name',
    display_name='Maintenance',
    searchable_by=['Maintenance', 'Item', 'Maintenance'],
    subtypes=['Item'],
    collector_number=96,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Shuffle 2 cards from your hand into your deck. (If you can't shuffle 2 cards into your deck, you can't play this card.) Then, draw a card. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Shuffle 2 cards from your hand into your deck. (If you can't shuffle 2 cards into your deck, you can't play this card.) Then, draw a card. You may play as many Item cards as you like during your turn (before your attack)."),
)
