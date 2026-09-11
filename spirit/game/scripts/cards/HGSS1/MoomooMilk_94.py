from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='7c4974db-2ae3-5fff-a125-f35ca250271b',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MoomooMilk.Name',
    display_name='Moomoo Milk',
    searchable_by=['Moomoo Milk', 'Item', 'MoomooMilk'],
    subtypes=['Item'],
    collector_number=94,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose 1 of your Pokémon. Flip 2 coins. For each heads, remove 3 damage counters from that Pokémon.'),
    condition=standard_trainer_condition('Choose 1 of your Pokémon. Flip 2 coins. For each heads, remove 3 damage counters from that Pokémon.'),
)
