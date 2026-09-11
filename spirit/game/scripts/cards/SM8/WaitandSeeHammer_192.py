from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='47ea1480-4391-564a-bf66-9431401a4f86',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.WaitandSeeHammer.Name',
    display_name='Wait and See Hammer',
    searchable_by=['Wait and See Hammer', 'Item', 'WaitandSeeHammer'],
    subtypes=['Item'],
    collector_number=192,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if you go second, and only on your first turn. Discard an Energy from 1 of your opponent's Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("You can use this card only if you go second, and only on your first turn. Discard an Energy from 1 of your opponent's Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
