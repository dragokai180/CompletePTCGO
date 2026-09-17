"""Outcomes for survival, reactive conditions, and post-KO Energy transfers."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import DamageCalc
from spirit.tools.effect_smoke import P1, P2


class GenericPassiveClauses(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_full_hp_survival_does_not_discard_the_pokemon(self):
        for path, title in (('SM8.Donphan_112', 'Sturdy'),
                            ('SV085.Pikachuex_179', 'Resolute Heart'),
                            ('ZSV10PT5.Crustle_52', 'Sturdy')):
            for damaged in (False, True):
                rig, e, ctx = self.ctx(path, title)
                maximum = ctx.max_hp(ctx.source)
                if damaged:
                    ctx.source.set_attribute(AttrID.HP, maximum - 10)
                calc = DamageCalc(rig.board, ctx.defender, ctx.source, maximum + 100)
                result = await ctx.ability.passive.damage_interceptor(ctx, calc, ctx.source, ctx.source)
                self.assertEqual(result, None if damaged else maximum - 10)
                self.assertEqual(ctx.deferred_actions, [])

    async def test_survival_tool_still_discards_only_itself(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        tool = self.add(rig, fixtures.definition('XY3.FocusSash_91'), P1, 'hand')
        rig.attach(tool, ctx.source)
        ctx.source.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIGHTING.value])
        calc = DamageCalc(rig.board, ctx.defender, ctx.source, 500)
        passive = def_for(tool.archetype_id).passive
        result = await passive.damage_interceptor(ctx, calc, ctx.source, tool)
        self.assertEqual(result, ctx.source.get_attribute(AttrID.HP) - 10)
        ctx.discard_cards = AsyncMock()
        for action in ctx.deferred_actions:
            await action()
        ctx.discard_cards.assert_awaited_once_with([tool])

    async def test_conditional_dodges_require_condition_and_heads(self):
        for path, title in (('SV4.Spinda_151', 'Tangled Feet'),
                            ('SV06.Fezandipiti_96', 'Adrena-Pheromone')):
            for eligible, heads in ((False, True), (True, False), (True, True)):
                rig, e, ctx = self.ctx(path, title)
                for energy in list(rig.board.attached_energies(ctx.source)):
                    rig.to_area(energy, P1, 'discard')
                if eligible and title == 'Tangled Feet':
                    ctx.source.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Confused'])
                elif eligible:
                    energy = self.add(rig, def_for(self.energies[PokemonTypes.DARKNESS.value]), P1, 'hand')
                    rig.attach(energy, ctx.source)
                ctx.flip_coins = AsyncMock(return_value=[heads])
                calc = DamageCalc(rig.board, ctx.defender, ctx.source, 30)
                result = await ctx.ability.passive.damage_interceptor(ctx, calc, ctx.source, ctx.source)
                self.assertEqual(result, 0 if eligible and heads else None)
                self.assertEqual(ctx.flip_coins.await_count, int(eligible))

    async def test_destiny_burst_waits_for_actual_knockout(self):
        for active, lethal, heads in ((True, True, True), (True, True, False),
                                     (True, False, True), (False, True, True)):
            rig, e, ctx = self.ctx('XY1.Voltorb_44', 'Destiny Burst')
            if not active:
                rig.to_area(ctx.source, P1, 'bench')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.deal_damage = AsyncMock()
            damage = ctx.max_hp(ctx.source) if lethal else 10
            calc = DamageCalc(rig.board, ctx.defender, ctx.source, damage)
            await ctx.ability.passive.damage_interceptor(ctx, calc, ctx.source, ctx.source)
            ctx.flip_coins.assert_not_awaited()
            for action in ctx.deferred_actions:
                await action()
            ctx.deal_damage.assert_not_awaited()
            if lethal:
                ctx.ko_from_attack = True
                ctx.was_active_at_ko = active
                ctx.ko_attacker = ctx.defender
                await ctx.ability.passive.on_knocked_out(ctx, ctx.source, ctx.source)
            self.assertEqual(ctx.deal_damage.await_count, int(active and lethal and heads))
            if ctx.deal_damage.await_count:
                self.assertEqual(ctx.deal_damage.call_args.args[0], 50)
                self.assertTrue(ctx.deal_damage.call_args.kwargs['as_counters'])
                self.assertFalse(ctx.deal_damage.call_args.kwargs['is_attack'])

    async def test_random_discard_reaction_is_not_duplicated_at_knockout(self):
        for path, title in (('Promo_XY.Absol_178', 'Lamentation'),
                            ('SV4.CursedDuster_161', None)):
            for lethal in (False, True):
                rig, e, ctx = self.ctx('Promo_XY.Absol_178', 'Lamentation')
                carrier = ctx.source
                passive = ctx.ability.passive
                if title is None:
                    carrier = self.add(rig, fixtures.definition(path), P1, 'hand')
                    rig.attach(carrier, ctx.source)
                    passive = def_for(carrier.archetype_id).passive
                ctx.discard_cards = AsyncMock()
                calc = DamageCalc(rig.board, ctx.defender, ctx.source, 500 if lethal else 10)
                await passive.damage_interceptor(ctx, calc, ctx.source, carrier)
                for action in ctx.deferred_actions:
                    await action()
                if lethal:
                    ctx.ko_from_attack = True
                    ctx.was_active_at_ko = True
                    ctx.knocked_out_attachments = [carrier] if title is None else []
                    await passive.on_knocked_out(ctx, ctx.source, carrier)
                self.assertEqual(ctx.discard_cards.await_count, int(title is not None or lethal))

    async def test_electrical_grounding_moves_only_one_eligible_energy(self):
        for attack_ko, accept in ((False, True), (True, False), (True, True)):
            rig, e, ctx = self.ctx('SV035.Raichu_26', 'Electrical Grounding')
            victim = ctx.my_bench()[0]
            lightning = self.add(rig, def_for(self.energies[PokemonTypes.LIGHTNING.value]), P1, 'discard')
            fire = self.add(rig, def_for(self.energies[PokemonTypes.FIRE.value]), P1, 'discard')
            ctx.knocked_out_attachments = [lightning, fire]
            ctx.ko_from_attack = attack_ko
            ctx.ask_yes_no = AsyncMock(return_value=accept)
            ctx.choose_cards = AsyncMock(return_value=[lightning])
            ctx.attach_energy = AsyncMock(return_value=True)
            await ctx.ability.passive.on_knocked_out(ctx, victim, ctx.source)
            self.assertEqual(ctx.attach_energy.await_count, int(attack_ko and accept))
            if ctx.attach_energy.await_count:
                self.assertEqual(ctx.choose_cards.call_args.args[:2], ([lightning], 1))
                ctx.attach_energy.assert_awaited_once_with(lightning, ctx.source)

    async def test_grounding_preserves_special_energy_type_at_knockout(self):
        rig, e, ctx = self.ctx('SV035.Raichu_26', 'Electrical Grounding')
        victim = ctx.my_bench()[0]
        energy = self.add(rig, fixtures.definition('BW4.PrismEnergy_93'), P1, 'discard')
        ctx.knocked_out_attachments = [energy]
        ctx.knocked_out_energy_types = {energy.entity_id: {PokemonTypes.LIGHTNING.value}}
        ctx.ko_from_attack = True
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.choose_cards = AsyncMock(return_value=[energy])
        ctx.attach_energy = AsyncMock(return_value=True)
        await ctx.ability.passive.on_knocked_out(ctx, victim, ctx.source)
        ctx.attach_energy.assert_awaited_once_with(energy, ctx.source)

    async def test_divers_catch_uses_type_at_knockout(self):
        for was_water in (False, True):
            rig, e, ctx = self.ctx('SV10.Huntail_55', "Diver's Catch")
            victim = ctx.my_bench()[0]
            victim.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
            energy = self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]), P1, 'discard')
            ctx.knocked_out_pokemon = victim
            ctx.knocked_out_attachments = [energy]
            ctx.knocked_out_types = [PokemonTypes.WATER.value if was_water else PokemonTypes.FIRE.value]
            ctx.ko_from_attack = True
            ctx.ask_yes_no = AsyncMock(return_value=True)
            ctx.put_in_hand = AsyncMock()
            await ctx.ability.passive.on_knocked_out(ctx, victim, ctx.source)
            if was_water:
                ctx.put_in_hand.assert_awaited_once_with([energy], reveal=False)
            else:
                ctx.put_in_hand.assert_not_awaited()

    async def test_heavy_baton_checks_retreat_cost_before_knockout(self):
        for cost, active, attack_ko in ((3, True, True), (4, False, True),
                                      (4, True, False), (4, True, True)):
            rig, e, base_ctx = self.ctx('BW1.Snivy_1', 'Tackle')
            victim = base_ctx.source
            tool = self.add(rig, fixtures.definition('SV05.HeavyBaton_151'), P1, 'discard')
            energy = self.add(rig, def_for(self.energies[PokemonTypes.GRASS.value]), P1, 'discard')
            ctx = EffectContext(rig.session, P1, tool, None)
            ctx.knocked_out_pokemon = victim
            ctx.knocked_out_attachments = [tool, energy]
            ctx.knocked_out_retreat_cost = cost
            ctx.was_active_at_ko = active
            ctx.ko_from_attack = attack_ko
            ctx.choose_cards = AsyncMock(return_value=[energy])
            ctx.choose_pokemon = AsyncMock(return_value=ctx.my_bench()[0])
            ctx.attach_energy = AsyncMock(return_value=True)
            await def_for(tool.archetype_id).passive.on_knocked_out(ctx, victim, tool)
            self.assertEqual(ctx.attach_energy.await_count, int(cost == 4 and active and attack_ko))


if __name__ == '__main__':
    unittest.main()
