from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='889f550f-ffa6-5873-9433-1cf8c8f15db5',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Xerosic.Name',
    display_name='Xerosic',
    searchable_by=['Xerosic', 'Supporter', 'Xerosic'],
    subtypes=['Supporter'],
    collector_number=110,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Choose a Pokémon Tool or Special Energy card attached to a Pokémon in play (yours or your opponent's) and discard it."),
    condition=standard_trainer_condition("Choose a Pokémon Tool or Special Energy card attached to a Pokémon in play (yours or your opponent's) and discard it."),
)
