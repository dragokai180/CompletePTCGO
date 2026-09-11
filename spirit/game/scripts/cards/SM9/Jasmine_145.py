from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='cde7cd61-daf1-5a13-8cc7-0440b28d8ca5',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Jasmine.Name',
    display_name='Jasmine',
    searchable_by=['Jasmine', 'Supporter', 'Jasmine'],
    subtypes=['Supporter'],
    collector_number=145,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for a Metal Pokémon, reveal it, and put it into your hand. If you go second and it's your first turn, search for 5 Metal Pokémon instead of 1. Then, shuffle your deck."),
    condition=standard_trainer_condition("Search your deck for a Metal Pokémon, reveal it, and put it into your hand. If you go second and it's your first turn, search for 5 Metal Pokémon instead of 1. Then, shuffle your deck."),
)
