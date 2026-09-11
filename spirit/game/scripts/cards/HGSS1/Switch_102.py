from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='edc5ffe5-03b0-516c-9656-794d88323516',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name',
    display_name='Switch',
    searchable_by=['Switch', 'Item', 'Switch'],
    subtypes=['Item'],
    collector_number=102,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Switch 1 of your Active Pokémon with 1 of your Benched Pokémon.'),
    condition=standard_trainer_condition('Switch 1 of your Active Pokémon with 1 of your Benched Pokémon.'),
)
