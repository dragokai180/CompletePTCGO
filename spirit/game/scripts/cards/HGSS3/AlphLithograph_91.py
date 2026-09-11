from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='12867848-b64c-5cdd-aa7d-6ab5ce1a7fa4',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AlphLithograph.Name',
    display_name='Alph Lithograph',
    searchable_by=['Alph Lithograph', 'Item', 'AlphLithograph'],
    subtypes=['Item'],
    collector_number=91,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RareSecret,
    attributes={200790: {'type': 'string', 'value': 'THREE'}},
    effect=standard_trainer_effect("Return any Stadium card in play to its player's hand!"),
    condition=standard_trainer_condition("Return any Stadium card in play to its player's hand!"),
)
