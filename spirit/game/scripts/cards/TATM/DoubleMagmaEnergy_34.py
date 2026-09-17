from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='cf3d6a67-253e-5727-b284-ce8ba6540fb8',
    key='TATM',
    name='Double Magma Energy',
    display_name='Double Magma Energy',
    searchable_by=['Double Magma Energy', 'Special', 'DoubleMagmaEnergy'],
    subtypes=['Special'],
    collector_number=34,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIGHTING,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.FIGHTING, PokemonTypes.FIGHTING]],
    passive=standard_passive('This card can only be attached to Team Magma Pokémon. Discard this card at the end of the turn you attached it. This card provides FightingFighting Energy only while it is attached to a Team Magma Pokémon. (If this card is attached to anything other than a Team Magma Pokémon, discard this card.)'),
    attach_to=energy_attach_to('This card can only be attached to Team Magma Pokémon. Discard this card at the end of the turn you attached it. This card provides FightingFighting Energy only while it is attached to a Team Magma Pokémon. (If this card is attached to anything other than a Team Magma Pokémon, discard this card.)'),
    discard_if_invalid=True,
)
