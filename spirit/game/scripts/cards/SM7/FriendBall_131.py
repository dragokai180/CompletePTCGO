from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='37bc31bf-b9da-5c15-b5bf-f8e0d25aead8',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FriendBall.Name',
    display_name='Friend Ball',
    searchable_by=['Friend Ball', 'Item', 'FriendBall'],
    subtypes=['Item'],
    collector_number=131,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for a Pokémon with the same type as 1 of your opponent's Pokémon in play, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Search your deck for a Pokémon with the same type as 1 of your opponent's Pokémon in play, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack)."),
)
