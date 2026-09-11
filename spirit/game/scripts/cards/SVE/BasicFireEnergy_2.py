from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='fb3dbaba-4e13-5115-9605-2052ec1d9f1a',
    key='SVE',
    name='Basic Fire Energy',
    display_name='Basic Fire Energy',
    searchable_by=['Basic Fire Energy', 'Basic', 'BasicFireEnergy'],
    subtypes=['Basic'],
    collector_number=2,
    set_code='SVE',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
    provides=[[PokemonTypes.FIRE]],
)
