from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import count_prizes_remaining


async def lillies_determination(ctx):
    """Shuffle your hand into your deck. Then, draw 6 cards. If you have
    exactly 6 Prize cards remaining, draw 8 cards instead."""
    n = 8 if count_prizes_remaining("mine")(ctx) == 6 else 6
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(n)


card = SupporterCardDef(
    guid="52b10a5e-fc89-52fe-9ba8-57f2c1800380",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesDetermination.Name",
    display_name="Lillie's Determination",
    searchable_by=["Lillie's Determination","Supporter","LilliesDetermination"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=lillies_determination
)
