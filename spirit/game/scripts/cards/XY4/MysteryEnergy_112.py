from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='e85fead9-af5a-5f80-a84b-dede2d56e2d3',
    key='XY4',
    name='Mystery Energy',
    display_name='Mystery Energy',
    searchable_by=['Mystery Energy', 'Special', 'MysteryEnergy'],
    subtypes=['Special'],
    collector_number=112,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=True,
    provides=[[PokemonTypes.PSYCHIC]],
    passive=standard_passive('This card can only be attached to Psychic Pokémon. This card provides Psychic Energy only while this card is attached to a Psychic Pokémon. The Retreat Cost of the Pokémon this card is attached to is ColorlessColorless less. (If this card is attached to anything other than a Psychic Pokémon, discard this card.)'),
    attach_to=energy_attach_to('This card can only be attached to Psychic Pokémon. This card provides Psychic Energy only while this card is attached to a Psychic Pokémon. The Retreat Cost of the Pokémon this card is attached to is ColorlessColorless less. (If this card is attached to anything other than a Psychic Pokémon, discard this card.)'),
    discard_if_invalid=True,
)
