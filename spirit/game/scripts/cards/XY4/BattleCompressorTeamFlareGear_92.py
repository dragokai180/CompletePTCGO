"""Battle Compressor Team Flare Gear (XY - Phantom Forces 92/119).

  "Search your deck for up to 3 cards and discard them. Shuffle your
   deck afterward."

Brilliant Blender's effect with the ACE SPEC count dialled back from 5 to
3; minimum=0 keeps the "up to" (a whiffed search is a legal resolution),
and deck_nonempty gates the play so it is not offered with an empty deck.

The name carries the "Team Flare Gear" tail because that is the printed
English card name, which is what the client's archetype key is built from
(clean_name -> BattleCompressorTeamFlareGear); the Japanese print shows the
same words as the subtitle next to バトルコンプレッサー.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


async def battle_compressor(ctx):
    """Search your deck for up to 3 cards and discard them. Then shuffle."""
    picks = await ctx.search_deck(
        count=3, minimum=0,
        prompt="Choose up to 3 cards to discard.",
    )
    await ctx.discard_cards(picks)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="2af80aaa-b14a-5472-8a4f-6906f780a5a7",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCompressorTeamFlareGear.Name",
    display_name="Battle Compressor Team Flare Gear",
    searchable_by=[
        "Battle Compressor Team Flare Gear", "Item",
        "BattleCompressorTeamFlareGear",
    ],
    subtypes=["Item"],
    collector_number=92,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=battle_compressor,
)
