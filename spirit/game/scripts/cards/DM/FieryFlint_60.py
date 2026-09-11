from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ac6e3f7b-147d-5e49-93da-042959e0f6e6',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name',
    display_name='Fiery Flint',
    searchable_by=['Fiery Flint', 'Item', 'FieryFlint'],
    subtypes=['Item'],
    collector_number=60,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if you discard 2 other cards from your hand. Search your deck for up to 4 Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('You can play this card only if you discard 2 other cards from your hand. Search your deck for up to 4 Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
