from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='7a08de01-1838-54b5-9af3-1231a99e11b2',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Tierno.Name',
    display_name='Tierno',
    searchable_by=['Tierno', 'Supporter', 'Tierno'],
    subtypes=['Supporter'],
    collector_number=39,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    effect=standard_trainer_effect('Draw 3 cards.'),
    condition=standard_trainer_condition('Draw 3 cards.'),
)
