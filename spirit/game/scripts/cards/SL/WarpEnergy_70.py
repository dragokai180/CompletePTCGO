from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='8e2b17db-c7ca-5621-8d26-4ad523d425fd',
    key='SL',
    name='Warp Energy',
    display_name='Warp Energy',
    searchable_by=['Warp Energy', 'Special', 'WarpEnergy'],
    subtypes=['Special'],
    collector_number=70,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card provides Colorless Energy. When you attach this card from your hand to your Active Pokémon, switch that Pokémon with 1 of your Benched Pokémon.'),
    on_attach=energy_on_attach('This card provides Colorless Energy. When you attach this card from your hand to your Active Pokémon, switch that Pokémon with 1 of your Benched Pokémon.'),
)
