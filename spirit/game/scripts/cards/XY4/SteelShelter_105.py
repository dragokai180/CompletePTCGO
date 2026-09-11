from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='32608b93-6a75-5185-88d7-2e7ab660357d',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SteelShelter.Name',
    display_name='Steel Shelter',
    searchable_by=['Steel Shelter', 'Stadium', 'SteelShelter'],
    subtypes=['Stadium'],
    collector_number=105,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Each Metal Pokémon (both yours and your opponent's) can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pokémon.) This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Each Metal Pokémon (both yours and your opponent's) can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pokémon.) This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
