from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="3cd8104d-bec6-523f-88db-9ea26e408770",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumioseCity.Name",
    display_name="Lumiose City",
    searchable_by=["Lumiose City", "Stadium", "LumioseCity"],
    subtypes=["Stadium"],
    collector_number=77,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may search their deck for a Basic Pokémon and put it onto their Bench. Then, that player shuffles their deck. If a player searches their deck in this way, their turn ends."),
    ability=standard_stadium_ability("Once during each player's turn, that player may search their deck for a Basic Pokémon and put it onto their Bench. Then, that player shuffles their deck. If a player searches their deck in this way, their turn ends."),
)
