from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,
)


card = EnergyCardDef(
    guid='495d53df-e84d-5eaf-9104-d6389dddac5f',
    key='SM6',
    name='Unit Energy FightingDarknessFairy',
    display_name='Unit Energy FightingDarknessFairy',
    searchable_by=['Unit Energy FightingDarknessFairy', 'Special', 'UnitEnergyFightingDarknessFairy'],
    subtypes=['Special'],
    collector_number=118,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[PokemonTypes.COLORLESS],
    provides=[[PokemonTypes.COLORLESS]],
    passive=standard_passive('This card provides Colorless Energy. While this card is attached to a Pokémon, it provides Fighting, Darkness, and Fairy Energy but provides only 1 Energy at a time.'),
)
