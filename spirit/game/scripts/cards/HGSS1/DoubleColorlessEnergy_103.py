from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='b0db8602-c03c-5a9d-9319-944b9bd85909',
    key='HGSS1',
    name='Double Colorless Energy',
    display_name='Double Colorless Energy',
    searchable_by=['Double Colorless Energy', 'Special', 'DoubleColorlessEnergy'],
    subtypes=['Special'],
    collector_number=103,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
    passive=standard_passive('Double Colorless Energy provides ColorlessColorless Energy.'),
)
