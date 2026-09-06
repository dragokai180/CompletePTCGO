from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_basic_pokemon


def _poffin_basic(card) -> bool:
    return is_basic_pokemon(card) and (card.get_attribute(AttrID.HP, 999) or 0) <= 70


card = ItemCardDef(
    guid="55f4491c-b3f5-5730-9c18-8d55f6f35a37",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyPoffin.Name",
    display_name="Buddy-Buddy Poffin",
    searchable_by=["Buddy-Buddy Poffin", "Item", "BuddyBuddyPoffin"],
    subtypes=["Item"],
    collector_number=144,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(
        _poffin_basic, count=2,
        prompt="Choose up to 2 Basic Pokémon with 70 HP or less to put onto your Bench.",
    ),
)
