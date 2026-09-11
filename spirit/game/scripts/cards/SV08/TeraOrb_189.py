from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="5ea73d73-f074-565b-b0ea-6e93160dca68",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeraOrb.Name",
    display_name="Tera Orb",
    searchable_by=["Tera Orb", "Item", "TeraOrb"],
    subtypes=["Item"],
    collector_number=189,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for a Tera Pokémon, reveal it, and put it into your hand. Then, shuffle your deck."),
)
