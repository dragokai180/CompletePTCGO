from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='c99c0fbc-4d36-5a02-9238-012dcc9f9a13',
    key='HGSS1',
    name='Metal Energy',
    display_name='Metal Energy',
    searchable_by=['Metal Energy', 'Basic', 'MetalEnergy'],
    subtypes=['Basic'],
    collector_number=122,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False,
    provides=[[PokemonTypes.METAL]],
)
