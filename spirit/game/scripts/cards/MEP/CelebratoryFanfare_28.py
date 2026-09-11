from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="ecbe95b0-989d-5f4e-a187-91b84a6462e3",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CelebratoryFanfare.Name",
    display_name="Celebratory Fanfare",
    searchable_by=["Celebratory Fanfare", "Stadium", "CelebratoryFanfare"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    passive=standard_passive("Once during each player's turn, that player may heal 10 damage from each of their Pokémon. If a player healed any damage in this way, their turn ends."),
    ability=standard_stadium_ability("Once during each player's turn, that player may heal 10 damage from each of their Pokémon. If a player healed any damage in this way, their turn ends."),
)
