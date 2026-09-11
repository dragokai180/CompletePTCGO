from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='2309a562-6e8f-550a-9ad2-733b6873e449',
    key='HGSS4',
    name='Rescue Energy',
    display_name='Rescue Energy',
    searchable_by=['Rescue Energy', 'Special', 'RescueEnergy'],
    subtypes=['Special'],
    collector_number=90,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('Rescue Energy provides Colorless Energy. If the Pokémon this card is attached to is Knocked Out by damage from an attack, put that Pokémon back into your hand. (Discard all cards attached to that Pokémon.)'),
    on_carrier_knocked_out=splash_energy_on_ko,
)
