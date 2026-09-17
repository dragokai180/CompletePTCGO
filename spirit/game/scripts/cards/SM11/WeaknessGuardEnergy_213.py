from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='82c44a85-69c0-5db6-8c25-2eb386245373',
    key='SM11',
    name='Weakness Guard Energy',
    display_name='Weakness Guard Energy',
    searchable_by=['Weakness Guard Energy', 'Special', 'WeaknessGuardEnergy'],
    subtypes=['Special'],
    collector_number=213,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[PokemonTypes.COLORLESS],
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card provides Colorless Energy. The Pokémon this card is attached to has no Weakness.'),
)
