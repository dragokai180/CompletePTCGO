from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='aefd08c6-46e8-5f44-bad9-b34a691eefce',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LetterofEncouragement.Name',
    display_name='Letter of Encouragement',
    searchable_by=['Letter of Encouragement', 'Item', 'LetterofEncouragement'],
    subtypes=['Item'],
    collector_number=189,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if any of your Pokémon were Knocked Out during your opponent's last turn. Search your deck for up to 3 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck."),
    condition=standard_trainer_condition("You can use this card only if any of your Pokémon were Knocked Out during your opponent's last turn. Search your deck for up to 3 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck."),
)
