from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='7c3fbfb4-e8e8-5fba-aa41-921b5747b179',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FadedTown.Name',
    display_name='Faded Town',
    searchable_by=['Faded Town', 'Stadium', 'FadedTown'],
    subtypes=['Stadium'],
    collector_number=73,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("At any time between turns, put 2 damage counters on each Mega Evolution Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("At any time between turns, put 2 damage counters on each Mega Evolution Pokémon. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
