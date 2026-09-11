from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='813dd652-74ad-5d69-9f3c-04f131aec2b2',
    key='SVE',
    name='Basic Psychic Energy',
    display_name='Basic Psychic Energy',
    searchable_by=['Basic Psychic Energy', 'Basic', 'BasicPsychicEnergy'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='SVE',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
    provides=[[PokemonTypes.PSYCHIC]],
)
