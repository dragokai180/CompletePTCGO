from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='6fafe67a-8bf7-5115-adf4-c47bc8d4dcea',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Clavell.Name',
    display_name='Clavell',
    searchable_by=['Clavell', 'Supporter', 'Clavell'],
    subtypes=['Supporter'],
    collector_number=177,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    effect=standard_trainer_effect('Search your deck for up to 3 Basic Pokémon with 120 HP or less, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 3 Basic Pokémon with 120 HP or less, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
