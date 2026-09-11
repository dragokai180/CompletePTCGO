from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)
from spirit.game.card_effects.standard_era import karen_condition, karen_effect


card = SupporterCardDef(
    guid='c84a5de9-5c43-5ec4-997e-5c6dfb670cf0',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Karen.Name',
    display_name='Karen',
    searchable_by=['Karen', 'Supporter', 'Karen'],
    subtypes=['Supporter'],
    collector_number=177,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    effect=karen_effect,
    condition=karen_condition,
)
