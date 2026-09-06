from spirit.game.data_utils import ItemCardDef, has_rule_box
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


def _no_rule_box_pokemon(card):
    return is_pokemon_card(card) and not has_rule_box(
        getattr(card, "archetype_id", None) or ""
    )


card = ItemCardDef(
    guid="cfe3652f-f0bb-5537-a894-023145a0c454",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokPad.Name",
    display_name="Poké Pad",
    searchable_by=["Poké Pad", "Item", "PokPad"],
    subtypes=["Item"],
    collector_number=198,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    effect=search_to_hand(
        _no_rule_box_pokemon, count=1, minimum=0, reveal=True,
        prompt="Choose a Pokémon that doesn't have a Rule Box.",
    ),
)
