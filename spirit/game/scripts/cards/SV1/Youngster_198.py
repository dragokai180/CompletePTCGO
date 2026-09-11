from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='9e454373-0ca6-5331-a74e-5efac6f13590',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Youngster.Name',
    display_name='Youngster',
    searchable_by=['Youngster', 'Supporter', 'Youngster'],
    subtypes=['Supporter'],
    collector_number=198,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle your hand into your deck. Then, draw 5 cards.'),
    condition=standard_trainer_condition('Shuffle your hand into your deck. Then, draw 5 cards.'),
)
