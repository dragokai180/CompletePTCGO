from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='599e6d4f-7a60-578c-a17d-20f2d1c1eef0',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RepeatBall.Name',
    display_name='Repeat Ball',
    searchable_by=['Repeat Ball', 'Item', 'RepeatBall'],
    subtypes=['Item'],
    collector_number=136,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Pokémon with the same name as 1 of your Pokémon in play, reveal it, and put it into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for a Pokémon with the same name as 1 of your Pokémon in play, reveal it, and put it into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
)
