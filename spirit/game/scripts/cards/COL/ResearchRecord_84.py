from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='d31b1943-452c-54a0-b602-16d652bf348f',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ResearchRecord.Name',
    display_name='Research Record',
    searchable_by=['Research Record', 'Item', 'ResearchRecord'],
    subtypes=['Item'],
    collector_number=84,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 4 cards of your deck and put as many of them as you like back on top of your deck in any order. Then, put the remaining cards on the bottom of your deck in any order.'),
    condition=standard_trainer_condition('Look at the top 4 cards of your deck and put as many of them as you like back on top of your deck in any order. Then, put the remaining cards on the bottom of your deck in any order.'),
)
