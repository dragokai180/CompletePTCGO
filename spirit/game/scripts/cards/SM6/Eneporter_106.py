from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='e4d8a65f-5efa-58de-97f0-f0528cbe0716',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Eneporter.Name',
    display_name='Eneporter',
    searchable_by=['Eneporter', 'Item', 'Eneporter'],
    subtypes=['Item'],
    collector_number=106,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Move a Special Energy from 1 of your opponent's Pokémon to another of their Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Move a Special Energy from 1 of your opponent's Pokémon to another of their Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
