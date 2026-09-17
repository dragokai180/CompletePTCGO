from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='18067340-de24-5600-9414-57fe907d07c7',
    key='SM4',
    name='Counter Energy',
    display_name='Counter Energy',
    searchable_by=['Counter Energy', 'Special', 'CounterEnergy'],
    subtypes=['Special'],
    collector_number=100,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[PokemonTypes.COLORLESS],
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive("This card provides Colorless Energy. If you have more Prize cards remaining than your opponent, and if this card is attached to a Pokémon that isn't a Pokémon-GX or Pokémon-EX, this card provides every type of Energy but provides only 2 Energy at a time."),
)
