from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="0f6e5cd3-8943-5782-9a16-e95168fca714",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyCoin.Name",
    display_name="Energy Coin",
    searchable_by=["Energy Coin", "Item", "EnergyCoin"],
    subtypes=["Item"],
    collector_number=81,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Flip 2 coins. If both of them are heads, search your deck for a Basic Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck."),
)
