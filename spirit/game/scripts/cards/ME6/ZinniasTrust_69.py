from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench


async def zinnias_trust(ctx):
    """Switch your Active Pokémon with 1 of your Benched Pokémon. Then, choose
    1 Energy attached to the Pokémon that moved to the Bench and move it to
    the new Active Pokémon."""
    bench = ctx.my_bench()
    if not bench:
        return
    outgoing = ctx.my_active()
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    if outgoing is None:
        return
    energies = ctx.attached_energies(outgoing)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy to move to the new Active Pokémon.",
    )
    if picks:
        await ctx.move_energy(picks[0], target)


card = SupporterCardDef(
    guid="19905582-4c07-5c0e-9658-318060274e55",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ZinniasTrust.Name",
    display_name="Zinnia's Trust",
    searchable_by=["Zinnia's Trust","Supporter","ZinniasTrust"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=player_has_bench,
    effect=zinnias_trust,
)
