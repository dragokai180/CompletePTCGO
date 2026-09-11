from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="8e5ffe8b-aca0-5e3a-948a-46e550b263ae",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CallBell.Name",
    display_name="Call Bell",
    searchable_by=["Call Bell", "Item", "CallBell"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if you go second, and only during your first turn.  Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck."),
)
