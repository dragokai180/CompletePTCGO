from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='78ef6670-b1f2-537d-9da9-f631e193cb2f',
    key='SM5',
    name='Unit Energy GrassFireWater',
    display_name='Unit Energy GrassFireWater',
    searchable_by=['Unit Energy GrassFireWater', 'Special', 'UnitEnergyGrassFireWater'],
    subtypes=['Special'],
    collector_number=137,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card provides Colorless Energy. While this card is attached to a Pokémon, it provides Grass, Fire, and Water Energy but provides only 1 Energy at a time.'),
)
