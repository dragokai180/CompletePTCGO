from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='5c8088f8-340a-5329-851b-45acd1709d9e',
    key='SM10',
    name='Triple Acceleration Energy',
    display_name='Triple Acceleration Energy',
    searchable_by=['Triple Acceleration Energy', 'Special', 'TripleAccelerationEnergy'],
    subtypes=['Special'],
    collector_number=190,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card can only be attached to Evolution Pokémon. If this card is attached to 1 of your Pokémon, discard it at the end of the turn. This card provides ColorlessColorlessColorless Energy only while it is attached to an Evolution Pokémon. If this card is attached to anything other than an Evolution Pokémon, discard this card.'),
    attach_to=energy_attach_to('This card can only be attached to Evolution Pokémon. If this card is attached to 1 of your Pokémon, discard it at the end of the turn. This card provides ColorlessColorlessColorless Energy only while it is attached to an Evolution Pokémon. If this card is attached to anything other than an Evolution Pokémon, discard this card.'),
    discard_if_invalid=True,
)
