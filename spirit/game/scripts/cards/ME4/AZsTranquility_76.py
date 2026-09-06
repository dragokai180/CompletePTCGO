from spirit.game.data_utils import SupporterCardDef, is_pokemon_ex
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench


async def azs_tranquility(ctx):
    """Switch your Active Pokemon with 1 of your Benched Pokemon. If you moved
    a Pokemon ex to your Bench in this way, heal 80 damage from that
    Pokemon."""
    active = ctx.my_active()
    target = await ctx.choose_pokemon(ctx.my_bench(), "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    if active is not None and is_pokemon_ex(active.archetype_id):
        await ctx.heal(80, active)


card = SupporterCardDef(
    guid="c4b06e35-21cf-5405-90fd-f87b4dd1a80b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AZsTranquility.Name",
    display_name="AZ's Tranquility",
    searchable_by=["AZ's Tranquility","Supporter","AZsTranquility"],
    subtypes=["Supporter"],
    collector_number=76,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=azs_tranquility,
    condition=player_has_bench,
)
