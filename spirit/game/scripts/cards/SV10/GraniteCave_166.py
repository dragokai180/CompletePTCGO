from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="0ae9dcf7-9f11-584a-95d1-171e08b5a36f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GraniteCave.Name",
    display_name="Granite Cave",
    searchable_by=["Granite Cave", "Stadium", "GraniteCave"],
    subtypes=["Stadium"],
    collector_number=166,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("Steven's Pokémon (both yours and your opponent's) take 30 less damage from attacks from the opponent's Pokémon (after applying Weakness and Resistance)."),
    ability=standard_stadium_ability("Steven's Pokémon (both yours and your opponent's) take 30 less damage from attacks from the opponent's Pokémon (after applying Weakness and Resistance)."),
)
