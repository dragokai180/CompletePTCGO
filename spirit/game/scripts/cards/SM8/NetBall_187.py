from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='5e41116c-5c19-58bb-9c05-9fa66e3aa013',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.NetBall.Name',
    display_name='Net Ball',
    searchable_by=['Net Ball', 'Item', 'NetBall'],
    subtypes=['Item'],
    collector_number=187,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Basic Grass Pokémon or a Grass Energy card, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for a Basic Grass Pokémon or a Grass Energy card, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
