from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='3e2c8e76-01f3-5f57-85d1-57f5c67d0def',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Looker.Name',
    display_name='Looker',
    searchable_by=['Looker', 'Supporter', 'Looker'],
    subtypes=['Supporter'],
    collector_number=126,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw 3 cards from the bottom of your deck.'),
    condition=standard_trainer_condition('Draw 3 cards from the bottom of your deck.'),
)
