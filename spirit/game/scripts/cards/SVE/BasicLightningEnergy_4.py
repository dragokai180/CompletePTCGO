from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='2621ddb4-6c54-54dc-9b4c-9f22d61ce74c',
    key='SVE',
    name='Basic Lightning Energy',
    display_name='Basic Lightning Energy',
    searchable_by=['Basic Lightning Energy', 'Basic', 'BasicLightningEnergy'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='SVE',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
    provides=[[PokemonTypes.LIGHTNING]],
)
