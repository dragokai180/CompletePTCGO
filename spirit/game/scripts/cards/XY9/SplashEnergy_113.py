from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='c7a9536c-e7b4-5e84-803b-f96379054d56',
    key='XY9',
    name='Splash Energy',
    display_name='Splash Energy',
    searchable_by=['Splash Energy', 'Special', 'SplashEnergy'],
    subtypes=['Special'],
    collector_number=113,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.WATER,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.WATER]],
    passive=standard_passive("This card can only be attached to Water Pokémon. This card provides Water Energy only while this card is attached to a Water Pokémon. If the Water Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put that Pokémon into your hand. (Discard all cards attached to it.) (If this card is attached to anything other than a Water Pokémon, discard this card.)"),
    attach_to=energy_attach_to("This card can only be attached to Water Pokémon. This card provides Water Energy only while this card is attached to a Water Pokémon. If the Water Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put that Pokémon into your hand. (Discard all cards attached to it.) (If this card is attached to anything other than a Water Pokémon, discard this card.)"),
    discard_if_invalid=True,
    on_carrier_knocked_out=splash_energy_on_ko,
)
