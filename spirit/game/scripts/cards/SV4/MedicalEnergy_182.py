from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='e019489d-abe6-5bed-aef5-91b1219a4a1d',
    key='SV4',
    name='Medical Energy',
    display_name='Medical Energy',
    searchable_by=['Medical Energy', 'Special', 'MedicalEnergy'],
    subtypes=['Special'],
    collector_number=182,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('As long as this card is attached to a Pokémon, it provides Colorless Energy.  When you attach this card from your hand to 1 of your Pokémon, heal 30 damage from that Pokémon.'),
    on_attach=energy_on_attach('As long as this card is attached to a Pokémon, it provides Colorless Energy.  When you attach this card from your hand to 1 of your Pokémon, heal 30 damage from that Pokémon.'),
)
