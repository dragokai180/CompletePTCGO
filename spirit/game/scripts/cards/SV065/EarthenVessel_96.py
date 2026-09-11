from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="6ed6d323-585a-5c20-8364-99bb28871fcf",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarthenVessel.Name",
    display_name="Earthen Vessel",
    searchable_by=["Earthen Vessel", "Item", "Ancient", "EarthenVessel"],
    subtypes=["Item", "Ancient"],
    collector_number=96,
    set_code="SV065",
    regulation_mark="G",
    rarity=Rarities.RareRainbow,
    effect=standard_trainer_effect("You can use this card only if you discard another card from your hand.  Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck."),
)
