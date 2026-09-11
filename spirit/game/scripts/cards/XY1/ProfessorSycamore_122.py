from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='0eec28a7-2241-57ec-87ca-469cac9aa9db',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSycamore.Name',
    display_name='Professor Sycamore',
    searchable_by=['Professor Sycamore', 'Supporter', 'ProfessorSycamore'],
    subtypes=['Supporter'],
    collector_number=122,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard your hand and draw 7 cards.'),
    condition=standard_trainer_condition('Discard your hand and draw 7 cards.'),
)
