from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="bfa47baa-7bbc-5476-85bb-c7cd8c06c96c",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotoStick.Name",
    display_name="Roto-Stick",
    searchable_by=["Roto-Stick", "Item", "RotoStick"],
    subtypes=["Item"],
    collector_number=127,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Look at the top 4 cards of your deck. You may reveal any number of Supporter cards you find there and put them into your hand. Shuffle the other cards back into your deck."),
)
