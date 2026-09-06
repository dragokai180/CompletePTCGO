from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def _other_player(board, player_id):
    return next((pid for pid in board.player_ids if pid != player_id), None)


def hand_trimmer_playable(board, player_id):
    """Playable if someone will actually discard after this card leaves hand."""
    hand = board.find_player_area(player_id, "hand")
    my_count = len(hand.children) if hand else 0
    opponent = _other_player(board, player_id)
    opp_hand = board.find_player_area(opponent, "hand") if opponent else None
    opp_count = len(opp_hand.children) if opp_hand else 0
    return opp_count > 5 or my_count > 6


async def hand_trimmer(ctx):
    """Each player discards until they have 5 cards; opponent discards first."""
    for pid in (ctx.opponent_id, ctx.player_id):
        excess = len(ctx.hand(pid)) - 5
        if excess > 0:
            await ctx.discard_from_hand(
                excess, minimum=excess, player_id=pid,
                prompt="Discard cards until you have 5 cards in your hand.",
            )


card = ItemCardDef(
    guid="aae207ce-e0a0-5f25-8063-2e1c66e4d901",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HandTrimmer.Name",
    display_name="Hand Trimmer",
    searchable_by=["Hand Trimmer","Item","HandTrimmer"],
    subtypes=["Item"],
    collector_number=150,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=hand_trimmer,
    condition=hand_trimmer_playable,
)
