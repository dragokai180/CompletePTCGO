from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)
from spirit.game.card_effects.energies import boomerang_reattach


card = EnergyCardDef(
    guid='b7240297-72ff-53ce-be7b-66c217daca3f',
    key='XY8',
    name='Burning Energy',
    display_name='Burning Energy',
    searchable_by=['Burning Energy', 'Special', 'BurningEnergy'],
    subtypes=['Special'],
    collector_number=151,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIRE,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.FIRE]],
    passive=standard_passive('This card can only be attached to Fire Pokémon. This card provides Fire Energy only while this card is attached to a Fire Pokémon. If this card is discarded by an attack of the Fire Pokémon this card is attached to, attach this card from your discard pile to that Pokémon after attacking. (If this card is attached to anything other than a Fire Pokémon, discard this card.)'),
    attach_to=energy_attach_to('This card can only be attached to Fire Pokémon. This card provides Fire Energy only while this card is attached to a Fire Pokémon. If this card is discarded by an attack of the Fire Pokémon this card is attached to, attach this card from your discard pile to that Pokémon after attacking. (If this card is attached to anything other than a Fire Pokémon, discard this card.)'),
    discard_if_invalid=True,
    on_discarded_by_carrier_attack=boomerang_reattach,
)
