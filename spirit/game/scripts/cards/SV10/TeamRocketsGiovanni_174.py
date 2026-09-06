from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


def _is_team_rockets(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's ")


def giovanni_condition(board, player_id):
    active = board.active_pokemon(player_id)
    if active is None or not _is_team_rockets(active):
        return False
    my_bench = [
        p for p in board.pokemon_in_play(player_id)
        if not is_in_active_spot(p) and _is_team_rockets(p)
    ]
    if not my_bench:
        return False
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return False
    return any(not is_in_active_spot(p) for p in board.pokemon_in_play(opponent))


async def team_rockets_giovanni(ctx):
    """Switch your Active Team Rocket's with a Benched Team Rocket's; if you do,
    switch in 1 of your opponent's Benched Pokémon."""
    bench = [p for p in ctx.my_bench() if _is_team_rockets(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose your new Active Team Rocket's Pokémon"
    )
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    opp_bench = ctx.opponent_bench()
    if not opp_bench:
        return
    opp_target = await ctx.choose_pokemon(
        opp_bench, "Choose the opponent's new Active Pokémon"
    )
    if opp_target is not None:
        await ctx.switch_active(ctx.opponent_id, opp_target)


card = SupporterCardDef(
    guid="1d21c21f-ec82-513a-8b41-7e4ec93cc7e9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGiovanni.Name",
    display_name="Team Rocket's Giovanni",
    searchable_by=["Team Rocket's Giovanni", "Supporter", "TeamRocketsGiovanni"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=giovanni_condition,
    effect=team_rockets_giovanni,
)
