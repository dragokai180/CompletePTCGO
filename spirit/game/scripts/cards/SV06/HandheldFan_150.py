from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _handheld_fan_trigger(ctx):
    """Move an Energy from the Attacking Pokémon to 1 of their Benched Pokémon."""
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    energies = ctx.attached_energies(attacker)
    bench = ctx.opponent_bench()
    if not energies or not bench:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy to move from the Attacking Pokémon",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon",
    )
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonToolCardDef(
    guid="c6235417-32ec-5ada-b8f8-1111fb414bf6",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HandheldFan.Name",
    display_name="Handheld Fan",
    searchable_by=["Handheld Fan","Pokémon Tool","Tool","HandheldFan"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=150,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Handheld Fan",
            game_text=(
                "If the Pokémon this card is attached to is in the Active Spot "
                "and is damaged by an attack from your opponent's Pokémon "
                "(even if this Pokémon is Knocked Out), move an Energy from "
                "the Attacking Pokémon to 1 of your opponent's Benched Pokémon."
            ),
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_handheld_fan_trigger,
        ),
    ],
)
