from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='2ffa760e-0269-5e53-bf88-8108384c4f88',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Sophocles.Name',
    display_name='Sophocles',
    searchable_by=['Sophocles', 'Supporter', 'Sophocles'],
    subtypes=['Supporter'],
    collector_number=123,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard 2 cards from your hand. If you do, draw 4 cards.'),
    condition=standard_trainer_condition('Discard 2 cards from your hand. If you do, draw 4 cards.'),
)
