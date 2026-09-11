from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='7b7cf959-8bdc-5a5d-8058-fce3ee6c3e20',
    key='HGSS1',
    name='Psychic Energy',
    display_name='Psychic Energy',
    searchable_by=['Psychic Energy', 'Basic', 'PsychicEnergy'],
    subtypes=['Basic'],
    collector_number=119,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
    provides=[[PokemonTypes.PSYCHIC]],
)
