from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="c865accf-3750-57ca-b3ae-9a5d4ec1ce80",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGreatBall.Name",
    display_name="Team Rocket's Great Ball",
    searchable_by=["Team Rocket's Great Ball", "Item", "TeamRocketsGreatBall"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Flip a coin. If heads, search your deck for an Evolution Team Rocket's Pokémon, reveal it, and put it into your hand. If tails, search your deck for a Basic Team Rocket's Pokémon, reveal it, and put it into your hand. Then, shuffle your deck."),
)
