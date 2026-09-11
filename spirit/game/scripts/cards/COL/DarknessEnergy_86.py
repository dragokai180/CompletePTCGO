from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='0acf436e-d510-5a48-91cd-1fb325273bb1',
    key='COL',
    name='Darkness Energy',
    display_name='Darkness Energy',
    searchable_by=['Darkness Energy', 'Special', 'DarknessEnergy'],
    subtypes=['Special'],
    collector_number=86,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS]],
    passive=standard_passive("If the Pokémon Darkness Energy is attached to attacks, the attack does 10 more damage to the Active Pokémon (before applying Weakness and Resistance). Ignore this Effect if the Pokémon that Darkness Energy is attached to isn't Darkness. Darkness Energy provides Darkness Energy. (Doesn't count as a basic Energy card.)"),
)
