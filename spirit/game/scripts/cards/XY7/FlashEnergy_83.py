from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='695127e4-2bf0-5ceb-855f-ed7aea962aa0',
    key='XY7',
    name='Flash Energy',
    display_name='Flash Energy',
    searchable_by=['Flash Energy', 'Special', 'FlashEnergy'],
    subtypes=['Special'],
    collector_number=83,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=True,
    provides=[[PokemonTypes.LIGHTNING]],
    passive=standard_passive('This card can only be attached to Lightning Pokémon. This card provides Lightning Energy only while this card is attached to a Lightning Pokémon. The Lightning Pokémon this card is attached to has no Weakness. (If this card is attached to anything other than a Lightning Pokémon, discard this card.)'),
    attach_to=energy_attach_to('This card can only be attached to Lightning Pokémon. This card provides Lightning Energy only while this card is attached to a Lightning Pokémon. The Lightning Pokémon this card is attached to has no Weakness. (If this card is attached to anything other than a Lightning Pokémon, discard this card.)'),
    discard_if_invalid=True,
)
