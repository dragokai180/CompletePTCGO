from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='f9104671-a5c1-5eb6-b0fe-fad555549982',
    key='SM5',
    name='Unit Energy LightningPsychicMetal',
    display_name='Unit Energy LightningPsychicMetal',
    searchable_by=['Unit Energy LightningPsychicMetal', 'Special', 'UnitEnergyLightningPsychicMetal'],
    subtypes=['Special'],
    collector_number=138,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card provides Colorless Energy. While this card is attached to a Pokémon, it provides Lightning, Psychic, and Metal Energy but provides only 1 Energy at a time.'),
)
