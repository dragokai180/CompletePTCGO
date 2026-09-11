from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='abfb47e3-f643-5387-bc05-0fb50c181d8f',
    key='HGSS1',
    name='Rainbow Energy',
    display_name='Rainbow Energy',
    searchable_by=['Rainbow Energy', 'Special', 'RainbowEnergy'],
    subtypes=['Special'],
    collector_number=104,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.GRASS,
    is_special=True,
    provides=[[PokemonTypes.GRASS], [PokemonTypes.FIRE], [PokemonTypes.WATER], [PokemonTypes.LIGHTNING], [PokemonTypes.PSYCHIC], [PokemonTypes.FIGHTING], [PokemonTypes.DARKNESS], [PokemonTypes.METAL]],
    passive=standard_passive('Attach Rainbow Energy to 1 of your Pokémon. While in play, Rainbow Energy provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.) When you attach this card from your hand to 1 of your Pokémon, put 1 damage counter on that Pokémon. (While not in play, Rainbow Energy counts as Colorless Energy.)'),
    on_attach=energy_on_attach('Attach Rainbow Energy to 1 of your Pokémon. While in play, Rainbow Energy provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.) When you attach this card from your hand to 1 of your Pokémon, put 1 damage counter on that Pokémon. (While not in play, Rainbow Energy counts as Colorless Energy.)'),
)
