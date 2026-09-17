from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='483ce702-6169-5dbe-9e8d-8f08a8a1bf52',
    key='TATM',
    name='Double Aqua Energy',
    display_name='Double Aqua Energy',
    searchable_by=['Double Aqua Energy', 'Special', 'DoubleAquaEnergy'],
    subtypes=['Special'],
    collector_number=33,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.WATER,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.WATER, PokemonTypes.WATER]],
    passive=standard_passive('This card can only be attached to Team Aqua Pokémon. Discard this card at the end of the turn you attached it. This card provides WaterWater Energy only while it is attached to a Team Aqua Pokémon. (If this card is attached to anything other than a Team Aqua Pokémon, discard this card.)'),
    attach_to=energy_attach_to('This card can only be attached to Team Aqua Pokémon. Discard this card at the end of the turn you attached it. This card provides WaterWater Energy only while it is attached to a Team Aqua Pokémon. (If this card is attached to anything other than a Team Aqua Pokémon, discard this card.)'),
    discard_if_invalid=True,
)
