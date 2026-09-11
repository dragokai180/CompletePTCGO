from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='f9b480aa-f3b2-5e27-95aa-b816005f0e33',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BrocksPewterCityGym.Name',
    display_name="Brock's Pewter City Gym",
    searchable_by=["Brock's Pewter City Gym", 'Stadium', 'BrocksPewterCityGym'],
    subtypes=['Stadium'],
    collector_number=54,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Onix-GX (both yours and your opponent's) take 40 less damage from the opponent's attacks (after applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Onix-GX (both yours and your opponent's) take 40 less damage from the opponent's attacks (after applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
