from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='50075202-c637-561a-8e05-fa7a17ddf93f',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Korrina.Name',
    display_name='Korrina',
    searchable_by=['Korrina', 'Supporter', 'Korrina'],
    subtypes=['Supporter'],
    collector_number=95,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Fighting Pokémon and an Item card, reveal them, and put them into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Search your deck for a Fighting Pokémon and an Item card, reveal them, and put them into your hand. Shuffle your deck afterward.'),
)
