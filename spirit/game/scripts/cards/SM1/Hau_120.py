from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='f471107c-e923-58bd-830c-34517922bfad',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name',
    display_name='Hau',
    searchable_by=['Hau', 'Supporter', 'Hau'],
    subtypes=['Supporter'],
    collector_number=120,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw 3 cards.'),
    condition=standard_trainer_condition('Draw 3 cards.'),
)
