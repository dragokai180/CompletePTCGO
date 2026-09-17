from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='bfab5dfb-d17a-5dd9-86df-ab0632aebafe',
    key='XY3',
    name='Herbal Energy',
    display_name='Herbal Energy',
    searchable_by=['Herbal Energy', 'Special', 'HerbalEnergy'],
    subtypes=['Special'],
    collector_number=103,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.GRASS,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.GRASS]],
    passive=standard_passive('This card can only be attached to Grass Pokémon. This card provides Grass Energy only while this card is attached to a Grass Pokémon. When you attach this card from your hand to 1 of your Grass Pokémon, heal 30 damage from that Pokémon. (If this card is attached to anything other than a Grass Pokémon, discard this card.)'),
    attach_to=energy_attach_to('This card can only be attached to Grass Pokémon. This card provides Grass Energy only while this card is attached to a Grass Pokémon. When you attach this card from your hand to 1 of your Grass Pokémon, heal 30 damage from that Pokémon. (If this card is attached to anything other than a Grass Pokémon, discard this card.)'),
    discard_if_invalid=True,
    on_attach=energy_on_attach('This card can only be attached to Grass Pokémon. This card provides Grass Energy only while this card is attached to a Grass Pokémon. When you attach this card from your hand to 1 of your Grass Pokémon, heal 30 damage from that Pokémon. (If this card is attached to anything other than a Grass Pokémon, discard this card.)'),
)
