from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='9c866c37-f841-5f2e-8dc2-d2cbe67375f7',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Penny.Name',
    display_name='Penny',
    searchable_by=['Penny', 'Supporter', 'Penny'],
    subtypes=['Supporter'],
    collector_number=183,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 1 of your Basic Pokémon and all attached cards into your hand.'),
    condition=standard_trainer_condition('Put 1 of your Basic Pokémon and all attached cards into your hand.'),
)
