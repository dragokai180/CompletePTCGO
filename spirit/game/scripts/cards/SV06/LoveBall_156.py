from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="b465f9ba-d19f-5525-ae20-07558ae6934a",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LoveBall.Name",
    display_name="Love Ball",
    searchable_by=["Love Ball", "Item", "LoveBall"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for a Pokémon with the same name as 1 of your opponent's Pokémon in play, reveal it, and put it into your hand. Then, shuffle your deck."),
)
