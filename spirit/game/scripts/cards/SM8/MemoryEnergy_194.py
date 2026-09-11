from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='f72469c6-2c68-59fa-9d02-d4a610e5a512',
    key='SM8',
    name='Memory Energy',
    display_name='Memory Energy',
    searchable_by=['Memory Energy', 'Special', 'MemoryEnergy'],
    subtypes=['Special'],
    collector_number=194,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card provides Colorless Energy. The Pokémon this card is attached to can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)'),
)
