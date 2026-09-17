from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='8c8945f3-43a7-560c-9c0a-80cabe04ad53',
    key='XY5',
    name='Wonder Energy',
    display_name='Wonder Energy',
    searchable_by=['Wonder Energy', 'Special', 'WonderEnergy'],
    subtypes=['Special'],
    collector_number=144,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FAIRY,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.FAIRY]],
    passive=standard_passive("This card can only be attached to Fairy Pokémon. This card provides Fairy Energy only while this card is attached to a Fairy Pokémon. Prevent all effects of your opponent's attacks, except damage, done to the Fairy Pokémon that this card is attached to. (Existing effects are not removed.) (If this card is attached to anything other than a Fairy Pokémon, discard this card.)"),
    attach_to=energy_attach_to("This card can only be attached to Fairy Pokémon. This card provides Fairy Energy only while this card is attached to a Fairy Pokémon. Prevent all effects of your opponent's attacks, except damage, done to the Fairy Pokémon that this card is attached to. (Existing effects are not removed.) (If this card is attached to anything other than a Fairy Pokémon, discard this card.)"),
    discard_if_invalid=True,
)
