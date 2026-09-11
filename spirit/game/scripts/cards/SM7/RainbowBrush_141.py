from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='e52193d6-c1c9-5bf1-910b-2786a41ef753',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RainbowBrush.Name',
    display_name='Rainbow Brush',
    searchable_by=['Rainbow Brush', 'Item', 'RainbowBrush'],
    subtypes=['Item'],
    collector_number=141,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose an Energy card attached to 1 of your Pokémon. Search your deck for a basic Energy card and switch it with that card. Shuffle the first Energy card into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Choose an Energy card attached to 1 of your Pokémon. Search your deck for a basic Energy card and switch it with that card. Shuffle the first Energy card into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
