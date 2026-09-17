from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='69def66f-8b0b-5255-84ac-334cde669a32',
    key='XY5',
    name='Shield Energy',
    display_name='Shield Energy',
    searchable_by=['Shield Energy', 'Special', 'ShieldEnergy'],
    subtypes=['Special'],
    collector_number=143,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.METAL]],
    passive=standard_passive("This card can only be attached to Metal Pokémon. This card provides Metal Energy only while this card is attached to a Metal Pokémon. Any damage done to the Metal Pokémon this card is attached to by an opponent's attack is reduced by 10 (after applying Weakness and Resistance). (If this card is attached to anything other than a Metal Pokémon, discard this card.)"),
    attach_to=energy_attach_to("This card can only be attached to Metal Pokémon. This card provides Metal Energy only while this card is attached to a Metal Pokémon. The attacks of your opponent's Pokémon do 10 less damage to the Metal Pokémon this card is attached to (before applying Weakness and Resistance). (If this card is attached to anything other than a Metal Pokémon, discard this card.)"),
    discard_if_invalid=True,
)
