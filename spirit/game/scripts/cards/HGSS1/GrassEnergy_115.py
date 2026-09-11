from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='2f5fb781-5f6c-5832-b872-c49f6e486e66',
    key='HGSS1',
    name='Grass Energy',
    display_name='Grass Energy',
    searchable_by=['Grass Energy', 'Basic', 'GrassEnergy'],
    subtypes=['Basic'],
    collector_number=115,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
    provides=[[PokemonTypes.GRASS]],
)
