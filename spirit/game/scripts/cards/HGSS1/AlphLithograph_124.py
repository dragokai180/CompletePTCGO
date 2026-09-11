from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='b37c6301-5c0e-50d6-a240-a9b3d0f94a34',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AlphLithograph.Name',
    display_name='Alph Lithograph',
    searchable_by=['Alph Lithograph', 'Item', 'AlphLithograph'],
    subtypes=['Item'],
    collector_number=124,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareSecret,
    attributes={200790: {'type': 'string', 'value': 'ONE'}},
    effect=standard_trainer_effect("Look at your opponent's hand!"),
    condition=standard_trainer_condition("Look at your opponent's hand!"),
)
