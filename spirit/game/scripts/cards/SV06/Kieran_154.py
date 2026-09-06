from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _KieranDamageBoostPassive(Passive):
    """Your attacks do +30 to the opponent's Active ex/V this turn."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.attacker is None:
            return
        if carrier_pokemon(carrier) is not calc.attacker:
            return
        subs = subtypes_for(calc.target.archetype_id)
        # Kieran's rider only cares about ex and (non-VSTAR) V.
        if "ex" in subs or "V" in subs:
            calc.amount += 30


async def kieran_effect(ctx):
    bench = ctx.my_bench()
    can_switch = bool(bench)

    if can_switch:
        choice = await ctx.choose(
            "Choose 1:",
            [
                "Switch your Active Pokémon with 1 of your Benched Pokémon.",
                "During this turn, attacks used by your Pokémon do 30 more damage "
                "to your opponent's Active Pokémon ex and Active Pokémon V "
                "(before applying Weakness and Resistance).",
            ],
        )
    else:
        choice = 1

    # Option 0 = Switch; option 1 = Damage boost.
    if choice == 0:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
        return

    # Otherwise apply the +30 damage modifier for this turn only.
    for p in ctx.my_pokemon_in_play():
        ctx.add_temporary_passive(
            p,
            _KieranDamageBoostPassive(),
            expires_after_turn=ctx.session.turn_state.turn_number,
        )


card = SupporterCardDef(
    guid="8f3c96b5-167e-4bd8-8447-4902a10c7029",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kieran.Name",
    display_name="Kieran",
    searchable_by=["Kieran", "Supporter", "Kieran"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=kieran_effect,
)

