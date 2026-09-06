from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench


async def scramble_switch(ctx):
    """Switch your Active with a Benched Pokémon; you may then move any
    amount of Energy from the Pokémon you moved to the Bench onto the new
    Active."""
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    old_active = ctx.my_active()
    if not await ctx.switch_active(ctx.player_id, target):
        return
    if old_active is None or not ctx.attached_energies(old_active):
        return
    if await ctx.ask_yes_no(
        "Move any amount of Energy from the Pokémon you moved to the Bench "
        "to the new Active Pokémon?"
    ):
        await ctx.move_energy_freely([old_active], [target])


card = ItemCardDef(
    guid="e94305e4-2cef-595b-aa6d-ad6c0063ca72",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScrambleSwitch.Name",
    display_name="Scramble Switch",
    searchable_by=["Scramble Switch","Item","ACE SPEC","ScrambleSwitch"],
    subtypes=["Item","ACE SPEC"],
    collector_number=186,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=scramble_switch,
    condition=player_has_bench,
)
