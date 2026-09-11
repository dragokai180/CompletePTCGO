from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='172259ba-93c5-5c01-b424-44d02a31d83c',
    key='XY1',
    name='Fairy Energy',
    display_name='Fairy Energy',
    searchable_by=['Fairy Energy', 'Basic', 'FairyEnergy'],
    subtypes=['Basic'],
    collector_number=140,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FAIRY,
    is_special=False,
    provides=[[PokemonTypes.FAIRY]],
)
