from spirit.game.data_utils import PokemonCardDef, Attack, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


from spirit.game.card_effects.attacks_common import previous_attack_matches


def _other_rapid_strike_attacked_last_turn(ctx):
    return previous_attack_matches(ctx.board, ctx.player_id, subtype="Rapid Strike", exclude=ctx.attacker)


async def cross_fist(ctx):
    """100, plus 160 to 1 opposing Benched if another Rapid Strike attacked last turn."""
    await ctx.deal_damage()
    if not _other_rapid_strike_attacked_last_turn(ctx):
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is not None:
        await ctx.deal_damage(160, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="b48e308d-0f44-5423-ade8-47bbe16f48c3",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    display_name="Zeraora V",
    searchable_by=["Zeraora V", "Basic", "V", "Rapid Strike", "ZeraoraV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=53,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Cross Fist",
            game_text="If 1 of your other Rapid Strike Pok\u00e9mon used an attack during your last turn, this attack also does 160 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=cross_fist,
        ),
    ],
)
