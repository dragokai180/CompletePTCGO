"""Effects for gallery prints without an existing non-gallery implementation."""

from spirit.game.data_utils import is_pokemon_v, subtypes_for
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.card_effects.bw_era import _BWTurnShield


async def professor_burnet(ctx):
    cards = await ctx.search_deck(count=2, minimum=0,
                                  prompt="Choose up to 2 cards to discard")
    if cards:
        await ctx.discard_cards(cards)
    await ctx.shuffle_deck()


async def icicle_shot(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        ctx.lock_retreat(ctx.defender)


async def crystal_star(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _BWTurnShield(prevent_all=True))


class ProtectiveDNAPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing and calc.attacker is not None
                and calc.target.owning_player_id == carrier.owning_player_id
                and "VSTAR" in subtypes_for(calc.attacker.archetype_id)):
            calc.amount = max(0, calc.amount - 30)


async def max_drain(ctx):
    await ctx.deal_damage()
    await ctx.heal(30, ctx.attacker)


async def psychic_javelin(ctx):
    await ctx.deal_damage()
    candidates = [p for p in ctx.opponent_bench() if is_pokemon_v(p.archetype_id)]
    if candidates:
        target = await ctx.choose_pokemon(candidates, "Choose an opponent's Benched Pokémon V")
        if target is not None:
            await ctx.deal_damage(60, target=target, apply_modifiers=False)


async def star_force(ctx):
    amount = count_energy("self")(ctx) + count_energy("defender")(ctx)
    await ctx.deal_damage(60 * amount)


async def deoxys_psychic(ctx):
    await ctx.deal_damage(30 + 30 * count_energy("defender")(ctx))
