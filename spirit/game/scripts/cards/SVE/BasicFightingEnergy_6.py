from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='8b9d2568-a7ad-5805-afd4-ee48b2bfa28c',
    key='SVE',
    name='Basic Fighting Energy',
    display_name='Basic Fighting Energy',
    searchable_by=['Basic Fighting Energy', 'Basic', 'BasicFightingEnergy'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SVE',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
    provides=[[PokemonTypes.FIGHTING]],
)
