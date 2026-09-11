from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='2d508c1f-20bd-592d-a839-2043f63b4385',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Winona.Name',
    display_name='Winona',
    searchable_by=['Winona', 'Supporter', 'Winona'],
    subtypes=['Supporter'],
    collector_number=96,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 3 Colorless Pokémon and put them into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Search your deck for up to 3 Colorless Pokémon and put them into your hand. Shuffle your deck afterward.'),
)
