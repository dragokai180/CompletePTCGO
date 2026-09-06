from spirit.game.data_utils import SupporterCardDef, has_rule_box
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


def _no_rule_box_pokemon(card):
    return is_pokemon_card(card) and not has_rule_box(
        getattr(card, "archetype_id", None) or ""
    )


async def gwynn(ctx):
    """Discard up to 2 Pokemon that don't have a Rule Box from your hand, and
    draw 3 cards for each card you discarded in this way."""
    discarded = await ctx.discard_from_hand(
        2, minimum=0, predicate=_no_rule_box_pokemon,
        prompt="Discard up to 2 Pokémon that don't have a Rule Box.",
    )
    if discarded:
        await ctx.draw_cards(3 * len(discarded))


card = SupporterCardDef(
    guid="43a98a04-dde4-5acc-804c-3aa04affe131",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gwynn.Name",
    display_name="Gwynn",
    searchable_by=["Gwynn","Supporter","Gwynn"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=gwynn,
)
