from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='7c7935a3-d73a-522c-bf46-4526b76fc27c',
    key='SM12',
    name='Draw Energy',
    display_name='Draw Energy',
    searchable_by=['Draw Energy', 'Special', 'DrawEnergy'],
    subtypes=['Special'],
    collector_number=209,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[PokemonTypes.COLORLESS],
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card provides Colorless Energy. When you attach this card from your hand to a Pokémon, draw a card.'),
    on_attach=energy_on_attach('This card provides Colorless Energy. When you attach this card from your hand to a Pokémon, draw a card.'),
)
