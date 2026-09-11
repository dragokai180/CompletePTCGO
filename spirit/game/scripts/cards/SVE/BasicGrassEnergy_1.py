from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='8a9eba81-b73f-57f5-ad14-e8e8549dbda1',
    key='SVE',
    name='Basic Grass Energy',
    display_name='Basic Grass Energy',
    searchable_by=['Basic Grass Energy', 'Basic', 'BasicGrassEnergy'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SVE',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
    provides=[[PokemonTypes.GRASS]],
)
