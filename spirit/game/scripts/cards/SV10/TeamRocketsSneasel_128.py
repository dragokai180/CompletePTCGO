from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def strike_the_sleeper(ctx):
    """20 damage to a Benched Pokémon for each damage counter on that Pokémon."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is None:
        return
    counters = max(0, (ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)) // 10)
    if counters:
        await ctx.deal_damage(20 * counters, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="e44cff16-5fb4-5d29-963e-6efc3bcf70e7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsSneasel.Name",
    display_name="Team Rocket's Sneasel",
    searchable_by=["Team Rocket's Sneasel", "Basic", "TeamRocketsSneasel"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=215,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Strike the Sleeper",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon for each damage counter on that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2},
            effect=strike_the_sleeper,
        ),
    ],
)
