from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='dc28221b-6481-5d1c-b2a9-209682844fad',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DamageMover.Name',
    display_name='Damage Mover',
    searchable_by=['Damage Mover', 'Item', 'DamageMover'],
    subtypes=['Item'],
    collector_number=58,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Move 3 damage counters from 1 of your Pokémon to another of your Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Move 3 damage counters from 1 of your Pokémon to another of your Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
