from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='ad33f68c-d32f-5a5c-a25d-b02887a37b9e',
    key='HGSS1',
    name='Lightning Energy',
    display_name='Lightning Energy',
    searchable_by=['Lightning Energy', 'Basic', 'LightningEnergy'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
    provides=[[PokemonTypes.LIGHTNING]],
)
