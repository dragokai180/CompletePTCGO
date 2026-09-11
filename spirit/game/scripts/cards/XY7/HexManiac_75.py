from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)
from spirit.game.card_effects.standard_era import hex_maniac_effect


card = SupporterCardDef(
    guid='20a7e210-a23e-591b-96d4-807b0e9c6c50',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HexManiac.Name',
    display_name='Hex Maniac',
    searchable_by=['Hex Maniac', 'Supporter', 'HexManiac'],
    subtypes=['Supporter'],
    collector_number=75,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=hex_maniac_effect,
)
