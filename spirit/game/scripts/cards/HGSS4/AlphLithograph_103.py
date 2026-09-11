from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='69295f38-dcd3-5cc6-8633-0d9a8f716d64',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AlphLithograph.Name',
    display_name='Alph Lithograph',
    searchable_by=['Alph Lithograph', 'Item', 'AlphLithograph'],
    subtypes=['Item'],
    collector_number=103,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareSecret,
    attributes={200790: {'type': 'string', 'value': 'FOUR'}},
    effect=standard_trainer_effect('LOOK AT ALL OF YOUR FACE DOWN PRIZE CARDS!'),
    condition=standard_trainer_condition('LOOK AT ALL OF YOUR FACE DOWN PRIZE CARDS!'),
)
