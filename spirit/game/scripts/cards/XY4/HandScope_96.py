from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='90f305ed-6ccb-5e8a-9a38-23aa6cc73527',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HandScope.Name',
    display_name='Hand Scope',
    searchable_by=['Hand Scope', 'Item', 'HandScope'],
    subtypes=['Item'],
    collector_number=96,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent reveals his or her hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Your opponent reveals his or her hand. You may play as many Item cards as you like during your turn (before your attack).'),
)
