from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


async def brilliant_blender(ctx):
    """Search your deck for up to 5 cards and discard them. Then shuffle."""
    picks = await ctx.search_deck(
        count=5, minimum=0,
        prompt="Choose up to 5 cards to discard.",
    )
    await ctx.discard_cards(picks)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="aec550bb-f88c-50df-b674-3706730046cf",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrilliantBlender.Name",
    display_name="Brilliant Blender",
    searchable_by=["Brilliant Blender", "Item", "ACE SPEC", "BrilliantBlender"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=164,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    condition=deck_nonempty,
    effect=brilliant_blender,
)
