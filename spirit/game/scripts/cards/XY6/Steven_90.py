from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='1d911495-bac3-5000-b31b-4be666caca7e',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Steven.Name',
    display_name='Steven',
    searchable_by=['Steven', 'Supporter', 'Steven'],
    subtypes=['Supporter'],
    collector_number=90,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Supporter card and a basic Energy card, reveal them, and put them into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Search your deck for a Supporter card and a basic Energy card, reveal them, and put them into your hand. Shuffle your deck afterward.'),
)
