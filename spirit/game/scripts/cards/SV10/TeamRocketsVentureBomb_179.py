from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="5460e3d4-49af-5cb8-afd6-415e1e42a87b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsVentureBomb.Name",
    display_name="Team Rocket's Venture Bomb",
    searchable_by=["Team Rocket's Venture Bomb", "Item", "TeamRocketsVentureBomb"],
    subtypes=["Item"],
    collector_number=179,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Flip a coin. If heads, put 2 damage counters on 1 of your opponent's Pokémon. If tails, put 2 damage counters on your Active Pokémon."),
)
