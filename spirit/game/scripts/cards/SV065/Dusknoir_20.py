from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def cursed_blast_13(ctx):
    """Once during your turn: place 13 damage counters, then KO yourself."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose a Pokémon")
    if target is None:
        return
    await ctx.place_damage_counters(13, [target])
    await ctx.knock_out(ctx.source)


async def shadow_bind(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="c2ff5f84-7357-490f-a665-9ae38e8895e7",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=355,
    abilities=[
        Ability(
            title="Cursed Blast",
            game_text=(
                "Once during your turn, you may put 13 damage counters on 1 "
                "of your opponent's Pokémon. If you use this Ability, this "
                "Pokémon is Knocked Out."
            ),
            activation=Activations.ONCE_PER_TURN,
            effect=cursed_blast_13,
        ),
        Attack(
            title="Shadow Bind",
            game_text=(
                "During your opponent's next turn, the Defending Pokémon can't retreat."
            ),
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=shadow_bind,
        ),
    ],
)

