from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='24a74c0e-4d7d-5bd4-8f8d-e71304f32c1c',
    key='HGSS1',
    name='Darkness Energy',
    display_name='Darkness Energy',
    searchable_by=['Darkness Energy', 'Basic', 'DarknessEnergy'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
    provides=[[PokemonTypes.DARKNESS]],
)
