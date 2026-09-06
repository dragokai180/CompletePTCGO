from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import TeraRulePassive


async def sob(ctx):
    """20. Then lock the Defending Pokémon's retreat for the opponent's next
    turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


async def torrential_pump(ctx):
    """100. You may shuffle 3 Energy from this Pokémon into your deck. If
    you do, this attack also deals 120 damage to 1 of your opponent's
    Benched Pokémon (no W/R for Benched)."""
    await ctx.deal_damage()

    energies = list(ctx.attached_energies(ctx.attacker))
    if len(energies) < 3:
        return
    if not await ctx.ask_yes_no(
        "Shuffle 3 Energy attached to this Pokémon into your deck?"
    ):
        return
    picks = await ctx.choose_cards(
        energies, 3,
        prompt="Choose 3 Energy attached to this Pokémon to shuffle into your deck."
    )
    if not picks:
        return
    await ctx.shuffle_into_deck(picks, player_id=ctx.player_id)

    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon to take 120 damage."
    )
    if target is not None:
        await ctx.deal_damage(120, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="b333f468-fb6c-4fd8-a977-10857c348e36",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WellspringMaskOgerponex.Name",
    display_name="Wellspring Mask Ogerpon ex",
    searchable_by=[
        "Wellspring Mask Ogerpon ex",
        "Basic",
        "ex",
        "Tera",
        "WellspringMaskOgerponex",
    ],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=64,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=1017,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Sob",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=sob,
        ),
        Attack(
            title="Torrential Pump",
            game_text=(
                "You may shuffle 3 Energy attached to this Pokémon into your deck. "
                "If you do, this attack also does 120 damage to 1 of your opponent's "
                "Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)"
            ),
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=torrential_pump,
        ),
    ],
)

