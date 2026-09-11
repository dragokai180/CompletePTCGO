from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='898e598a-6135-5505-95eb-2a9d57f7c277',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Saguaro.Name',
    display_name='Saguaro',
    searchable_by=['Saguaro', 'Supporter', 'Saguaro'],
    subtypes=['Supporter'],
    collector_number=187,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose up to 2 of your Pokémon and heal 50 damage from each of them.'),
    condition=standard_trainer_condition('Choose up to 2 of your Pokémon and heal 50 damage from each of them.'),
)
