from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='e085f783-c8aa-5678-962b-31ab4192df39',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name',
    display_name='Energy Switch',
    searchable_by=['Energy Switch', 'Item', 'EnergySwitch'],
    subtypes=['Item'],
    collector_number=91,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Move a basic Energy card attached 1 of your Pokémon to another of your Pokémon.'),
    condition=standard_trainer_condition('Move a basic Energy card attached 1 of your Pokémon to another of your Pokémon.'),
)
