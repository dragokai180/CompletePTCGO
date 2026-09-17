from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='61b7bdfa-01c8-5ee4-9b0c-eb8a7032dccf',
    key='SV2',
    name='Reversal Energy',
    display_name='Reversal Energy',
    searchable_by=['Reversal Energy', 'Special', 'ReversalEnergy'],
    subtypes=['Special'],
    collector_number=192,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.GRASS,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.GRASS], [PokemonTypes.FIRE], [PokemonTypes.WATER], [PokemonTypes.LIGHTNING], [PokemonTypes.PSYCHIC], [PokemonTypes.FIGHTING], [PokemonTypes.DARKNESS], [PokemonTypes.METAL], [PokemonTypes.FAIRY]],
    passive=standard_passive("As long as this card is attached to a Pokémon, it provides Colorless Energy.If you have more Prize cards remaining than your opponent, and if this card is attached to an Evolution Pokémon that doesn't have a Rule Box (Pokémon ex, Pokémon V, etc. have Rule Boxes), this card provides every type of Energy but provides only 3 Energy at a time."),
)
