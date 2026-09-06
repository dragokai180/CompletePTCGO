from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities


def _is_team_rockets_archetype(archetype_id) -> bool:
    definition = def_for(archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's ")


def archer_condition(board, player_id):
    ledger = board.turn_state.pokemon_lost_last_turn(player_id)
    return any(_is_team_rockets_archetype(e.get("archetype_id")) for e in ledger)


async def team_rockets_archer(ctx):
    """Each player shuffles their hand into their deck; you draw 5, opponent 3."""
    for pid, count in ((ctx.player_id, 5), (ctx.opponent_id, 3)):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(count, pid)


card = SupporterCardDef(
    guid="0063e060-895d-5494-8243-1756cccc6df5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsArcher.Name",
    display_name="Team Rocket's Archer",
    searchable_by=["Team Rocket's Archer", "Supporter", "TeamRocketsArcher"],
    subtypes=["Supporter"],
    collector_number=170,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=archer_condition,
    effect=team_rockets_archer,
)
