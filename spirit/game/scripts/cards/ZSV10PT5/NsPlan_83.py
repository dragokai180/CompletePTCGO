from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.models.board import BoardState


def ns_plan_condition(board, player_id):
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(BoardState.attached_energies(p) for p in bench.children)


async def ns_plan(ctx):
    """Move up to 2 Energy from your Benched Pokémon to your Active Pokémon."""
    active = ctx.my_active()
    bench = ctx.my_bench()
    if active is None or not bench:
        return
    await ctx.move_energy_freely(
        bench, [active], max_count=2,
        prompt="Choose an Energy to move to your Active Pokémon",
    )


card = SupporterCardDef(
    guid="e7a79eec-dc57-536d-8161-1b06dc3a4dcc",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsPlan.Name",
    display_name="N's Plan",
    searchable_by=["N's Plan","Supporter","NsPlan"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=ns_plan,
    condition=ns_plan_condition,
)
