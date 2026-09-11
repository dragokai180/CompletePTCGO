from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='615041ff-89b0-5924-830e-a810d82285ad',
    key='SM6',
    name='Beast Energy ◇',
    display_name='Beast Energy ◇',
    searchable_by=['Beast Energy ◇', 'Special', 'Prism Star', 'BeastEnergy'],
    subtypes=['Special', 'Prism Star'],
    collector_number=117,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Prism,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive("This card provides Colorless Energy. While this card is attached to an Ultra Beast, it provides every type of Energy but provides only 1 Energy at a time. The attacks of the Ultra Beast this card is attached to do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
)
