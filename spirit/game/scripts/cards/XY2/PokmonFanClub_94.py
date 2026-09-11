from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='7b2b1bbd-e63e-5b8e-9dd0-57868f627090',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokmonFanClub.Name',
    display_name='Pokémon Fan Club',
    searchable_by=['Pokémon Fan Club', 'Supporter', 'PokmonFanClub'],
    subtypes=['Supporter'],
    collector_number=94,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 Basic Pokémon, reveal them, and put them into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Search your deck for up to 2 Basic Pokémon, reveal them, and put them into your hand. Shuffle your deck afterward.'),
)
