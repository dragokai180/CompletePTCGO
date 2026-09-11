from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='bae61bae-a03e-5bf1-be33-0805061bff01',
    key='SM11',
    name='Recycle Energy',
    display_name='Recycle Energy',
    searchable_by=['Recycle Energy', 'Special', 'RecycleEnergy'],
    subtypes=['Special'],
    collector_number=212,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card provides Colorless Energy. If this card is discarded from play, put it into your hand instead of the discard pile.'),
)
