from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='c8c2dc4b-0221-54d0-8527-000577a20677',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EnergyReturner.Name',
    display_name='Energy Returner',
    searchable_by=['Energy Returner', 'Item', 'EnergyReturner'],
    subtypes=['Item'],
    collector_number=74,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your discard pile for 4 basic Energy cards, show them to your opponent, and shuffle them into your deck.'),
    condition=standard_trainer_condition('Search your discard pile for 4 basic Energy cards, show them to your opponent, and shuffle them into your deck.'),
)
