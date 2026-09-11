from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='883291ab-0eaa-59b2-859c-e472233579ea',
    key='HGSS1',
    name='Water Energy',
    display_name='Water Energy',
    searchable_by=['Water Energy', 'Basic', 'WaterEnergy'],
    subtypes=['Basic'],
    collector_number=117,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False,
    provides=[[PokemonTypes.WATER]],
)
