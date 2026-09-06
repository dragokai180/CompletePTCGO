from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def carmine(ctx):
    """Discard your hand and draw 5 cards. Playable on your first turn."""
    await ctx.discard_cards(list(ctx.hand()))
    await ctx.draw_cards(5)


card = SupporterCardDef(
    guid="a01d0152-bdda-4c8a-8fc1-327fef2a0cdb",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Carmine.Name",
    display_name="Carmine",
    searchable_by=["Carmine", "Supporter", "Carmine"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    usable_first_turn=True,
    effect=carmine,
)
