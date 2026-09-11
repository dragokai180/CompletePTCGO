from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="a7ade2a0-bf73-5738-a9d9-91e516caa63c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskBall.Name",
    display_name="Dusk Ball",
    searchable_by=["Dusk Ball", "Item", "DuskBall"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Look at the bottom 7 cards of your deck. You may reveal a Pokémon you find there and put it into your hand. Shuffle the other cards back into your deck."),
)
