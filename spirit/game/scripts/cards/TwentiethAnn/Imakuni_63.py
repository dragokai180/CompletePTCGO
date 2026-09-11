from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='341cc365-8750-5f9e-b179-09265beb7dac',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Imakuni.Name',
    display_name='Imakuni?',
    searchable_by=['Imakuni?', 'Supporter', 'Imakuni'],
    subtypes=['Supporter'],
    collector_number=63,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your Active Pokémon is now Confused.'),
    condition=standard_trainer_condition('Your Active Pokémon is now Confused.'),
)
