from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='748f89bd-79fe-52cc-b070-6e6441e4ece0',
    key='SV2',
    name='Therapeutic Energy',
    display_name='Therapeutic Energy',
    searchable_by=['Therapeutic Energy', 'Special', 'TherapeuticEnergy'],
    subtypes=['Special'],
    collector_number=193,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[],
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive("As long as this card is attached to a Pokémon, it provides Colorless Energy.The Pokémon this card is attached to recovers from being Asleep, Confused, or Paralyzed and can't be affected by those Special Conditions."),
)
