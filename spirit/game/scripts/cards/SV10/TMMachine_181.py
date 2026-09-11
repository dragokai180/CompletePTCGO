from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="ecca6db6-927b-5c0f-bc8f-80ec67368173",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TMMachine.Name",
    display_name="TM Machine",
    searchable_by=["TM Machine", "Item", "MEGA", "TMMachine"],
    subtypes=["Item", "MEGA"],
    collector_number=181,
    set_code="SV10",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for up to 3 Pokémon Tool cards that have \"Technical Machine\" in their name, reveal them, and put them into your hand. Then, shuffle your deck."),
)
