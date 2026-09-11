from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ec5d5ca1-5657-5a33-9f80-59e78075246c',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ElectromagneticRadar.Name',
    display_name='Electromagnetic Radar',
    searchable_by=['Electromagnetic Radar', 'Item', 'ElectromagneticRadar'],
    subtypes=['Item'],
    collector_number=169,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if you discard 2 other cards from your hand. Search your deck for up to 2 in any combination of Lightning Pokémon-GX and Lightning Pokémon-EX, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('You can play this card only if you discard 2 other cards from your hand. Search your deck for up to 2 in any combination of Lightning Pokémon-GX and Lightning Pokémon-EX, reveal them, and put them into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
