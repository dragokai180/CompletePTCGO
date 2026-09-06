from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_bench

async def pokemon_catcher(ctx):
    """Flip a coin. If heads, switch in 1 of your opponent's Benched Pokemon to
    the Active Spot."""
    if not (await ctx.flip_coins(1, "Pokémon Catcher"))[0]:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose your opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)

card = ItemCardDef(
    guid="dd6dc060-90a6-595d-aa14-12b465e4ddf0",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pokémon Catcher","Item","PokemonCatcher"],
    subtypes=["Item"],
    collector_number=82,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    effect=pokemon_catcher,
    condition=opponent_has_bench
)
