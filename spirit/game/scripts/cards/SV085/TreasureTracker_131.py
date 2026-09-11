from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="e55640a4-19d4-5e11-b83a-7b5f8966c902",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TreasureTracker.Name",
    display_name="Treasure Tracker",
    searchable_by=["Treasure Tracker", "Item", "ACE SPEC", "TreasureTracker"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=131,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=standard_trainer_effect("You can't have more than 1 ACE SPEC card in your deck. Search your deck for up to 5 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck."),
)
