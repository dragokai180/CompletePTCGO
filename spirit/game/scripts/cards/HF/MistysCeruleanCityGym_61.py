from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='b418c08c-3243-5178-9945-39d37e5730f1',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MistysCeruleanCityGym.Name',
    display_name="Misty's Cerulean City Gym",
    searchable_by=["Misty's Cerulean City Gym", 'Stadium', 'MistysCeruleanCityGym'],
    subtypes=['Stadium'],
    collector_number=61,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The attacks of Starmie-GX (both yours and your opponent's) do 40 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("The attacks of Starmie-GX (both yours and your opponent's) do 40 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
