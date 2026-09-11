from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='c996e0ff-54cd-5315-bc79-5af76413ce68',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name',
    display_name='Cynthia',
    searchable_by=['Cynthia', 'Supporter', 'Cynthia'],
    subtypes=['Supporter'],
    collector_number=119,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle your hand into your deck. Then, draw 6 cards.'),
    condition=standard_trainer_condition('Shuffle your hand into your deck. Then, draw 6 cards.'),
)
