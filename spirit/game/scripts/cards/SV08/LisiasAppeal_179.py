from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, SpecialConditions
from spirit.game.session.effects import is_basic_pokemon


def _has_benched_basic(board, player_id):
    area = board.find_player_area(player_id, "bench")
    return bool(area) and any(is_basic_pokemon(p) for p in area.children)


def lisias_appeal_playable(board, player_id):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    return _has_benched_basic(board, opponent)


async def lisias_appeal(ctx):
    """Switch in 1 of the opponent's Benched Basic Pokémon; it is Confused."""
    bench = [p for p in ctx.opponent_bench() if is_basic_pokemon(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose your opponent's new Active Pokémon"
    )
    if target is None:
        return
    if not await ctx.switch_active(ctx.opponent_id, target):
        return
    await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)


card = SupporterCardDef(
    guid="37c19bf5-83f3-54bb-af42-ef76ab2d407b",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LisiasAppeal.Name",
    display_name="Lisia's Appeal",
    searchable_by=["Lisia's Appeal","Supporter","LisiasAppeal"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=lisias_appeal,
    condition=lisias_appeal_playable,
)
