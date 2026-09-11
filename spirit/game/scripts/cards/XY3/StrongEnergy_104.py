from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, standard_passive,
)


card = EnergyCardDef(
    guid='fc0679c9-79b4-5356-96e0-621c6296dabb',
    key='XY3',
    name='Strong Energy',
    display_name='Strong Energy',
    searchable_by=['Strong Energy', 'Special', 'StrongEnergy'],
    subtypes=['Special'],
    collector_number=104,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIGHTING,
    is_special=True,
    provides=[[PokemonTypes.FIGHTING]],
    passive=standard_passive("This card can only be attached to Fighting Pokémon. This card provides Fighting Energy only while this card is attached to a Fighting Pokémon. The attacks of the Fighting Pokémon this card is attached to do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). (If this card is attached to anything other than a Fighting Pokémon, discard this card.)"),
    attach_to=energy_attach_to("This card can only be attached to Fighting Pokémon. This card provides Fighting Energy only while this card is attached to a Fighting Pokémon. The attacks of the Fighting Pokémon this card is attached to do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). (If this card is attached to anything other than a Fighting Pokémon, discard this card.)"),
    discard_if_invalid=True,
)
