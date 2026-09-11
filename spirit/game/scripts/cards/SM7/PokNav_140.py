from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='04c8d539-e29e-5004-9b73-2a8b785cbc48',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokNav.Name',
    display_name='PokéNav',
    searchable_by=['PokéNav', 'Item', 'PokNav'],
    subtypes=['Item'],
    collector_number=140,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 3 cards of your deck. You may reveal a Pokémon or Energy card you find there and put it into your hand. Put the other cards back in any order. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the top 3 cards of your deck. You may reveal a Pokémon or Energy card you find there and put it into your hand. Put the other cards back in any order. You may play as many Item cards as you like during your turn (before your attack).'),
)
