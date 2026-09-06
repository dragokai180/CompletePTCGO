from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_water_pokemon


def surfer_playable(board, player_id):
    area = board.find_player_area(player_id, "bench")
    return bool(area) and any(is_water_pokemon(p) for p in area.children)


async def surfer(ctx):
    """Switch your Active Pokémon with 1 of your Benched Water Pokémon."""
    bench = [p for p in ctx.my_bench() if is_water_pokemon(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Water Pokémon to switch into the Active Spot"
    )
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = SupporterCardDef(
    guid="84949575-1331-5aeb-a7a0-eea43ad24c47",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Surfer.Name",
    display_name="Surfer",
    searchable_by=["Surfer","Supporter","Surfer"],
    subtypes=["Supporter"],
    collector_number=187,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=surfer,
    condition=surfer_playable,
)
