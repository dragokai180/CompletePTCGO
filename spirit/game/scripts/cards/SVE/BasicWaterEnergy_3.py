from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='4dadbf5e-2885-5f61-9171-e2d5f2cd67d3',
    key='SVE',
    name='Basic Water Energy',
    display_name='Basic Water Energy',
    searchable_by=['Basic Water Energy', 'Basic', 'BasicWaterEnergy'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='SVE',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False,
    provides=[[PokemonTypes.WATER]],
)
