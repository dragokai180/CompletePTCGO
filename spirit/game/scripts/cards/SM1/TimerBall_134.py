from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='4b3ceeb2-1e9f-50b9-b82f-7a3c962117a3',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TimerBall.Name',
    display_name='Timer Ball',
    searchable_by=['Timer Ball', 'Item', 'TimerBall'],
    subtypes=['Item'],
    collector_number=134,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip 2 coins. For each heads, search your deck for an Evolution Pokémon, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Flip 2 coins. For each heads, search your deck for an Evolution Pokémon, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
