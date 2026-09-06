from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


def _other_player(board, player_id):
    return next((pid for pid in board.player_ids if pid != player_id), None)


def xerosics_machinations_playable(board, player_id):
    opponent = _other_player(board, player_id)
    if opponent is None:
        return False
    hand = board.find_player_area(opponent, "hand")
    return bool(hand) and len(hand.children) > 3


async def xerosics_machinations(ctx):
    """Your opponent discards cards until they have 3 cards in their hand."""
    excess = len(ctx.hand(ctx.opponent_id)) - 3
    if excess <= 0:
        return
    await ctx.discard_from_hand(
        excess, minimum=excess, player_id=ctx.opponent_id,
        prompt="Discard cards until you have 3 cards in your hand.",
    )


card = SupporterCardDef(
    guid="adecffaa-a40b-5190-aa8d-0aca5542ddaf",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.XerosicsMachinations.Name",
    display_name="Xerosic's Machinations",
    searchable_by=["Xerosic's Machinations","Supporter","XerosicsMachinations"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=xerosics_machinations,
    condition=xerosics_machinations_playable,
)
