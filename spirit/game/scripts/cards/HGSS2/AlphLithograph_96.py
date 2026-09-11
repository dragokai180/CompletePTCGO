from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='c68e7922-eacb-5303-be3d-5b329584d262',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AlphLithograph.Name',
    display_name='Alph Lithograph',
    searchable_by=['Alph Lithograph', 'Item', 'AlphLithograph'],
    subtypes=['Item'],
    collector_number=96,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareSecret,
    attributes={200790: {'type': 'string', 'value': 'TWO'}},
    effect=standard_trainer_effect('Shuffle your deck!'),
    condition=standard_trainer_condition('Shuffle your deck!'),
)
