from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ecd02bff-1f02-5744-a64a-fdc1387d71da',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Electropower.Name',
    display_name='Electropower',
    searchable_by=['Electropower', 'Item', 'Electropower'],
    subtypes=['Item'],
    collector_number=172,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("During this turn, your Lightning Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("During this turn, your Lightning Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
