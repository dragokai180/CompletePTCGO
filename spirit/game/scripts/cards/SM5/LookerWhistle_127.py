from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='be2917bb-9f22-5f45-9c31-37495b84cc06',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LookerWhistle.Name',
    display_name='Looker Whistle',
    searchable_by=['Looker Whistle', 'Item', 'LookerWhistle'],
    subtypes=['Item'],
    collector_number=127,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 cards named Looker, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for up to 2 cards named Looker, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
