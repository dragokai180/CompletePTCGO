from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="d3cca382-b136-5cb8-9d32-7744b74f21b9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Postwick.Name",
    display_name="Postwick",
    searchable_by=["Postwick", "Stadium", "Postwick"],
    subtypes=["Stadium"],
    collector_number=154,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("Attacks used by Hop's Pokémon (both yours and your opponent's) do 30 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance)."),
    ability=standard_stadium_ability("Attacks used by Hop's Pokémon (both yours and your opponent's) do 30 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance)."),
)
