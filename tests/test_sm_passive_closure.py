"""Outcome and timing coverage for the remaining SM passive review flags."""
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from tests import test_sm_knockout_timing as ko_helpers
from tests import test_sm_swsh_final_trainers as helpers
from spirit.game.attributes import AttrID, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.data_utils import Attack
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _ability_entries, ability_condition_met
from spirit.game.session.passives import retreat_energy_destination, attack_coin_reroll_offered
from spirit.tools.effect_smoke import P1, P2


class PassiveClosureTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    energy = helpers.RemainingTrainerTests.energy
    attack_context = ko_helpers.SmKnockoutTimingTests.attack_context

    async def test_victory_star_rerolls_attack_coins_once_without_manual_action(self):
        rig, e = self.rig('SM2.Victini_10')
        self.add(rig, fixtures.definition('SM2.Victini_10'), P1, 'bench')
        ts = rig.session.turn_state
        ts.active_player_id = P1
        ctx = EffectContext(rig.session, P1, e['target'], Attack(title='Coins', cost={}, damage=10))
        self.assertFalse(_ability_entries(rig.board, ts, P1, 'test', rig.board.pokemon_in_play(P1)))
        self.assertTrue(attack_coin_reroll_offered(rig.board, P1, ctx.attacker))
        self.assertFalse(attack_coin_reroll_offered(rig.board, P2, ctx.defender))
        ctx.ask_yes_no = AsyncMock(return_value=True)
        with patch('spirit.game.session.effects.random.choice', side_effect=[1, 1, 0, 0, 1]):
            self.assertEqual(await ctx.flip_coins(2), [True, True])
            self.assertEqual(await ctx.flip_coins(1), [False])
        ctx.ask_yes_no.assert_awaited_once()
        self.assertTrue(ts.attack_coin_reroll_used)

    async def test_victory_star_does_not_reroll_tool_or_defensive_coins(self):
        rig, e = self.rig('SM2.Victini_10')
        rig.session.turn_state.active_player_id = P1
        for ability, source in ((None, None), (Attack(title='Hit', cost={}, damage=10), e['target'])):
            ctx = EffectContext(rig.session, P1, e['target'], ability)
            ctx.ask_yes_no = AsyncMock(return_value=True)
            await ctx.flip_coins(1, source=source)
            ctx.ask_yes_no.assert_not_awaited()

    async def test_trick_coin_reroll_is_exclusive_to_tool_holder(self):
        rig, e = self.rig('XY4.TrickCoin_108', 'trainer')
        holder = rig.board.active_pokemon(P1)
        rig.attach(e['target'], holder)
        self.assertTrue(attack_coin_reroll_offered(rig.board, P1, holder))
        other = self.add(rig, self.filler, P1, 'bench')
        self.assertFalse(attack_coin_reroll_offered(rig.board, P1, other))

    async def test_lost_out_requires_opposing_attack_damage_and_moves_entire_stack(self):
        for counters in (False, True):
            rig, e = self.rig('SM8.TyranitarGX_121')
            ctx = EffectContext(rig.session, P1, e['target'], Attack(title='Hit', cost={}, damage=1000))
            victim = ctx.defender
            attached = self.energy(rig, pid=P2)
            rig.attach(attached, victim)
            await ctx.deal_damage(1000, target=victim, as_counters=counters)
            await rig.session.resolve_knockouts(ctx)
            destination = rig.board.find_player_area(P2, 'discard' if counters else 'lostZone')
            self.assertIs(victim.parent, destination)
            self.assertIs(attached.parent, destination)

    async def test_grim_marking_only_active_attack_ko_and_distributes_four_counters(self):
        for bench, counters in ((False, False), (True, False), (False, True)):
            rig, e = self.rig('SM12.Dusknoir_85')
            victim = e['target']
            if bench: rig.to_area(victim, P1, 'bench')
            ctx = self.attack_context(rig, victim)
            with patch.object(EffectContext, 'place_damage_counters', new_callable=AsyncMock) as place:
                await ctx.deal_damage(1000, target=victim, as_counters=counters)
                await rig.session.resolve_knockouts(ctx)
            if not bench and not counters:
                place.assert_awaited_once()
                self.assertEqual(place.call_args.args[0], 4)
                self.assertTrue(all(p.owning_player_id == P2 for p in place.call_args.args[1]))
            else: place.assert_not_awaited()

    async def test_last_pattern_discards_two_random_opposing_cards_only_for_attack_ko(self):
        for counters in (False, True):
            rig, e = self.rig('HF.Arbok_27')
            ctx = self.attack_context(rig, e['target'])
            before = list(ctx.hand(P2))
            own = list(ctx.hand(P1))
            await ctx.deal_damage(1000, target=e['target'], as_counters=counters)
            await rig.session.resolve_knockouts(ctx)
            self.assertEqual(len([c for c in before if c in ctx.discard_pile(P2)]), 0 if counters else 2)
            self.assertTrue(all(c in ctx.hand(P1) for c in own))

    async def test_natural_cure_requires_hand_attachment_to_its_holder(self):
        for from_hand, receiver_is_holder in ((True, True), (False, True), (True, False)):
            rig, e = self.rig('DM.Combusken_5')
            holder = e['target']
            holder.set_attribute(AttrID.SPECIAL_CONDITIONS, [CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]])
            ctx = EffectContext(rig.session, P1, holder, None)
            receiver = holder if receiver_is_holder else ctx.my_bench()[0]
            energy = self.energy(rig)
            await ctx.attach_energy(energy, receiver)
            if from_hand: await rig.session.fire_energy_attached_triggers(P1, energy, receiver)
            self.assertEqual(bool(holder.get_attribute(AttrID.SPECIAL_CONDITIONS)), not (from_hand and receiver_is_holder))

    async def test_dashing_pouch_returns_only_its_holders_retreat_payment(self):
        rig, e = self.rig('SM4.DashingPouch_92', 'trainer')
        holder = rig.board.active_pokemon(P1)
        rig.attach(e['target'], holder)
        ctx = EffectContext(rig.session, P1, holder, Attack(title='Discard', cost={}, damage=10))
        basic = self.energy(rig)
        special = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), P1, 'hand')
        for c in (basic, special):
            rig.attach(c, holder)
            self.assertEqual(retreat_energy_destination(rig.board, holder, c), 'hand')
            self.assertNotEqual(retreat_energy_destination(rig.board, ctx.defender, c), 'hand')
        await ctx.discard_cards([basic, special])
        self.assertTrue(all(c in ctx.discard_pile() for c in (basic, special)))

    async def test_reactive_counters_require_active_opposing_attack_damage(self):
        for path, count in (('DM.Druddigon_45', 3), ('Promo_SM.AlolanSandslashGX_236', 3), ('SM11.Slaking_170', 4)):
            for bench, counters in ((False, False), (True, False), (False, True)):
                rig, e = self.rig(path)
                victim = e['target']
                if bench: rig.to_area(victim, P1, 'bench')
                ctx = self.attack_context(rig, victim)
                ctx.attacker.set_attribute(AttrID.HP, 400)
                await ctx.deal_damage(10, target=victim, as_counters=counters)
                for action in list(ctx.deferred_actions): await action()
                self.assertEqual(400-ctx.attacker.get_attribute(AttrID.HP), count*10 if not bench and not counters else 0)

    async def test_ear_ringing_bell_and_poison_barb_require_holder_active_and_damage(self):
        for path, status in (('SM11.EarRingingBell_194', SpecialConditions.CONFUSED), ('SM1.PoisonBarb_124', SpecialConditions.POISONED)):
            for bench, counters in ((False, False), (True, False), (False, True)):
                rig, e = self.rig(path, 'trainer')
                victim = rig.board.active_pokemon(P1)
                rig.attach(e['target'], victim)
                if bench: rig.to_area(victim, P1, 'bench')
                ctx = self.attack_context(rig, victim)
                await ctx.deal_damage(10, target=victim, as_counters=counters)
                for action in list(ctx.deferred_actions): await action()
                self.assertEqual(CLIENT_SPECIAL_CONDITION_NAMES[status] in (ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), not bench and not counters)

    async def test_charmed_charm_only_matching_tool_on_holder_and_optional(self):
        for matches, receiver_is_holder, accept in ((True, True, True), (False, True, True), (True, False, True), (True, True, False)):
            rig, e = self.rig('Promo_SM.TapuLele_152')
            rig.session.turn_state.active_player_id = P1
            ctx = EffectContext(rig.session, P1, e['target'], None)
            path = 'SM8.FairyCharmPsychic_175' if matches else 'SM3.WishfulBaton_128'
            tool = self.add(rig, fixtures.definition(path), P1, 'hand')
            receiver = e['target'] if receiver_is_holder else self.add(rig, self.filler, P1, 'bench')
            rig.attach(tool, receiver)
            with patch.object(EffectContext, 'ask_yes_no', AsyncMock(return_value=accept)) as ask:
                await rig.session.fire_tool_attached_triggers(P1, tool, receiver)
            self.assertEqual(ask.await_count, int(matches and receiver_is_holder))
            self.assertEqual(CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED] in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), matches and receiver_is_holder and accept)

    async def test_lillies_poke_doll_bottoms_only_itself_from_active(self):
        rig, e = self.rig('SM12.LilliesPokDoll_197', 'trainer')
        doll = e['target']
        d = fixtures.definition('SM12.LilliesPokDoll_197')
        ability = d.abilities[0]
        rig.to_area(doll, P1, 'bench')
        self.assertFalse(ability_condition_met(ability, rig.board, P1, doll))
        rig.to_area(rig.board.active_pokemon(P1), P1, 'hand')
        rig.to_area(doll, P1, 'activePokemonArea')
        self.assertTrue(ability_condition_met(ability, rig.board, P1, doll))
        energy = self.energy(rig)
        tool = self.add(rig, fixtures.definition('SM3.WishfulBaton_128'), P1, 'hand')
        rig.attach(energy, doll); rig.attach(tool, doll)
        ctx = EffectContext(rig.session, P1, doll, ability)
        await ability.effect(ctx)
        self.assertIs(ctx.deck()[0], doll)
        self.assertIn(energy, ctx.discard_pile())
        self.assertIn(tool, ctx.discard_pile())
        self.assertFalse(ctx.knockouts)

    async def test_commotion_hits_all_own_bench_not_opponent(self):
        for bench, counters in ((False, False), (True, False), (False, True)):
            rig, e = self.rig('DM.Gyarados_20')
            victim = e['target']
            if bench: rig.to_area(victim, P1, 'bench')
            ctx = self.attack_context(rig, victim)
            targets = [p for p in rig.board.pokemon_in_play(P1) if p is not victim]
            before = {p: p.get_attribute(AttrID.HP) for p in targets}
            await ctx.deal_damage(10, target=victim, as_counters=counters)
            for action in list(ctx.deferred_actions): await action()
            for p, hp in before.items(): self.assertEqual(hp-p.get_attribute(AttrID.HP), 20 if not bench and not counters else 0)
