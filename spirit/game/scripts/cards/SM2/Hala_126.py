from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='d32bcd94-b172-596f-af42-3a5df001fec5',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Hala.Name',
    display_name='Hala',
    searchable_by=['Hala', 'Supporter', 'Hala'],
    subtypes=['Supporter'],
    collector_number=126,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle your hand into your deck. If you have used your GX attack, draw 7 cards. If not, draw 4 cards.'),
    condition=standard_trainer_condition('Shuffle your hand into your deck. If you have used your GX attack, draw 7 cards. If not, draw 4 cards.'),
)
