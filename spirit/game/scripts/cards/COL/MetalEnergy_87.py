from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='007ea16e-dd75-58c7-bc8d-4ceea30d433e',
    key='COL',
    name='Metal Energy',
    display_name='Metal Energy',
    searchable_by=['Metal Energy', 'Special', 'MetalEnergy'],
    subtypes=['Special'],
    collector_number=87,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    provides=[[PokemonTypes.METAL]],
    passive=standard_passive("Damage done by attacks to the Pokémon that Metal Energy attached to is reduced by 10 (after applying Weakness and Resistance). Ignore this effect if the Pokémon that Metal Energy is attached to isn't Metal. Metal Energy provides Metal Energy. (Doesn't count as a basic Energy card.)"),
)
