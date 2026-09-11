from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='90a64659-080d-5a8b-827a-cad7ebd89506',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Poppy.Name',
    display_name='Poppy',
    searchable_by=['Poppy', 'Supporter', 'Poppy'],
    subtypes=['Supporter'],
    collector_number=193,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Move up to 2 Energy from 1 of your Pokémon to another of your Pokémon.'),
    condition=standard_trainer_condition('Move up to 2 Energy from 1 of your Pokémon to another of your Pokémon.'),
)
