from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='f3008ce7-df97-543e-834c-3fd6d4df7bf2',
    key='HGSS3',
    name='Metal Energy',
    display_name='Metal Energy',
    searchable_by=['Metal Energy', 'Special', 'MetalEnergy'],
    subtypes=['Special'],
    collector_number=80,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    provides=[[PokemonTypes.METAL]],
    passive=standard_passive("Damage done by attacks to the Pokémon that Metal Energy is attached to is reduced by 10 (after applying Weakness and Resistance). Ignore this effect if the Pokémon that Metal Energy is attached to isn't Metal Metal Energy provides Metal Energy. (Doesn't count as a basic Energy card.)"),
)
