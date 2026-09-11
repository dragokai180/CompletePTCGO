from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='9d2c32d3-8b21-5c68-852e-e501a033cb86',
    key='HGSS1',
    name='Fire Energy',
    display_name='Fire Energy',
    searchable_by=['Fire Energy', 'Basic', 'FireEnergy'],
    subtypes=['Basic'],
    collector_number=116,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
    provides=[[PokemonTypes.FIRE]],
)
