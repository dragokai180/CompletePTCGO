from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='ed4d4c30-6603-572f-ae29-8ed0102f0daf',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Ryme.Name',
    display_name='Ryme',
    searchable_by=['Ryme', 'Supporter', 'Ryme'],
    subtypes=['Supporter'],
    collector_number=194,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Draw 3 cards. Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)"),
    condition=standard_trainer_condition("Draw 3 cards. Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)"),
)
