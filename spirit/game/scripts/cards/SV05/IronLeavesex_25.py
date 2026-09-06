from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def rapid_vernier(ctx):
    """On play from hand onto the Bench: you may switch this Pokemon with
    your Active; if you do, you may move any amount of Energy from your
    other Pokemon onto this one."""
    if not await ctx.ask_yes_no("Switch this Pokémon with your Active Pokémon?"):
        return
    if not await ctx.switch_active(ctx.player_id, ctx.source):
        return
    others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    if not others or not any(ctx.attached_energies(p) for p in others):
        return
    if await ctx.ask_yes_no(
        "Move any amount of Energy from your other Pokémon to this Pokémon?"
    ):
        await ctx.move_energy_freely(others, [ctx.source])


card = PokemonCardDef(
    guid="85d9153e-076b-5096-b201-c399fee69cc5",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronLeavesex.Name",
    display_name="Iron Leaves ex",
    searchable_by=["Iron Leaves ex", "Basic", "ex", "Future", "IronLeavesex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=25,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1010,
    abilities=[
        Ability(
            title="Rapid Vernier",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may switch it with your Active Pokémon. If you do, you may move any amount of Energy from your other Pokémon to this Pokémon.",
            trigger=Triggers.ON_PLAY,
            effect=rapid_vernier,
        ),
        Attack(
            title="Prism Edge",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            locks_next_turn=True,
        ),
    ],
)
