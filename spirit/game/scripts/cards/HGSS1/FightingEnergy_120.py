from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='5e69f9a3-6819-5a5b-92be-35f05526e547',
    key='HGSS1',
    name='Fighting Energy',
    display_name='Fighting Energy',
    searchable_by=['Fighting Energy', 'Basic', 'FightingEnergy'],
    subtypes=['Basic'],
    collector_number=120,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
    provides=[[PokemonTypes.FIGHTING]],
)
