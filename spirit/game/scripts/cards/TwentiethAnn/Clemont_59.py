from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='4ea788ee-a424-53d9-99c6-b7709a2b0fa4',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Clemont.Name',
    display_name='Clemont',
    searchable_by=['Clemont', 'Supporter', 'Clemont'],
    subtypes=['Supporter'],
    collector_number=59,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 4 Lightning Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Search your deck for up to 4 Lightning Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.'),
)
