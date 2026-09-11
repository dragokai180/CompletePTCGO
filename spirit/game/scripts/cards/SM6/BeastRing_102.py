from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='a5a09892-5089-5bc2-a07f-6aa5ec14e659',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BeastRing.Name',
    display_name='Beast Ring',
    searchable_by=['Beast Ring', 'Item', 'BeastRing'],
    subtypes=['Item'],
    collector_number=102,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    effect=standard_trainer_effect('You can play this card only if your opponent has exactly 3 or 4 Prize cards remaining. Search your deck for up to 2 basic Energy cards and attach them to 1 of your Ultra Beasts. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('You can play this card only if your opponent has exactly 3 or 4 Prize cards remaining. Search your deck for up to 2 basic Energy cards and attach them to 1 of your Ultra Beasts. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
