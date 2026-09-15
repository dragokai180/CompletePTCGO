"""No-Prize rules must override bonuses without changing other knockouts."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Attack
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2, GameOver


class LilliesPokeDollKnockoutTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_doll(self, owner=P1, bench=False):
        rig, _ = self.rig('SM12.ArceusDialgaPalkiaGX_156')
        # Keep ordinary Basics on both sides unless a test installs ADP.
        for pid in (P1, P2):
            for card in list(rig.board.pokemon_in_play(pid)):
                rig.to_area(card, pid, 'hand')
            self.add(rig, self.filler, pid, 'activePokemonArea')
            self.add(rig, self.filler, pid, 'bench')
            self.add(rig, self.filler, pid, 'bench')
        if not bench:
            rig.to_area(rig.board.active_pokemon(owner), owner, 'hand')
        doll = self.add(rig, fixtures.definition('SM12.LilliesPokDoll_197'),
                        owner, 'bench' if bench else 'activePokemonArea')
        doll.set_attribute(AttrID.HP, 30)
        attacker_id = P2 if owner == P1 else P1
        return rig, doll, attacker_id

    def context(self, rig, attacker_id):
        return EffectContext(rig.session, attacker_id,
                             rig.board.active_pokemon(attacker_id),
                             Attack(title='Audit hit', cost={}, damage=1000))

    async def enable_altered_creation(self, rig, attacker_id):
        definition = fixtures.definition('SM12.ArceusDialgaPalkiaGX_156')
        rig.to_area(rig.board.active_pokemon(attacker_id), attacker_id, 'hand')
        adp = self.add(rig, definition, attacker_id, 'activePokemonArea')
        for kind in (PokemonTypes.METAL, PokemonTypes.WATER):
            rig.attach_energy_type(attacker_id, adp, kind.value)
        gx = next(a for a in definition.abilities if a.title == 'Altered Creation-GX')
        await gx.effect(EffectContext(rig.session, attacker_id, adp, gx))

    async def test_altered_creation_cannot_award_prizes_for_either_players_doll(self):
        for owner in (P1, P2):
            with self.subTest(owner=owner):
                rig, doll, attacker_id = self.setup_doll(owner)
                await self.enable_altered_creation(rig, attacker_id)
                ctx = self.context(rig, attacker_id)
                with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
                    await ctx.deal_damage(1000, target=doll)
                    await rig.session.resolve_knockouts(ctx)
                prizes.assert_not_awaited()
                self.assertIn(doll, ctx.discard_pile(owner))
                self.assertIsNotNone(rig.board.active_pokemon(owner))

    async def test_attack_and_turn_watcher_bonuses_cannot_bypass_doll(self):
        for bonus in ('attack', 'watcher'):
            with self.subTest(bonus=bonus):
                rig, doll, attacker_id = self.setup_doll()
                ctx = self.context(rig, attacker_id)
                if bonus == 'attack':
                    ctx.extra_prizes = 2
                else:
                    rig.session.turn_state.extra_prize_watchers.append(
                        {'player_id': attacker_id, 'prizes': 1})
                with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
                    await ctx.deal_damage(1000, target=doll)
                    await rig.session.resolve_knockouts(ctx)
                prizes.assert_not_awaited()

    async def test_doll_does_not_block_prizes_for_simultaneous_bench_knockout(self):
        rig, doll, attacker_id = self.setup_doll()
        await self.enable_altered_creation(rig, attacker_id)
        other = rig.board.find_player_area(P1, 'bench').children[0]
        ctx = self.context(rig, attacker_id)
        with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
            await ctx.deal_damage(1000, target=doll)
            await ctx.deal_damage(1000, target=other)
            await rig.session.resolve_knockouts(ctx)
        prizes.assert_awaited_once_with(attacker_id, 1, destination='hand')

    async def test_knockout_discards_attachments_and_preserves_bench_or_promotes(self):
        for bench, counters in ((False, False), (True, False), (False, True)):
            with self.subTest(bench=bench, counters=counters):
                rig, doll, attacker_id = self.setup_doll(bench=bench)
                old_active = rig.board.active_pokemon(P1)
                rig.attach_energy_type(P1, doll, PokemonTypes.WATER.value)
                tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P1, 'hand')
                rig.attach(tool, doll)
                attachments = list(doll.children)
                ctx = self.context(rig, attacker_id)
                with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
                    await ctx.deal_damage(1000, target=doll, as_counters=counters)
                    await rig.session.resolve_knockouts(ctx)
                prizes.assert_not_awaited()
                self.assertTrue(all(c in ctx.discard_pile(P1) for c in [doll] + attachments))
                if bench:
                    self.assertIs(rig.board.active_pokemon(P1), old_active)
                else:
                    self.assertIsNotNone(rig.board.active_pokemon(P1))
                    self.assertIsNot(rig.board.active_pokemon(P1), doll)

    async def test_numerical_reduction_does_not_disable_altered_creation_bonus(self):
        rig, doll, attacker_id = self.setup_doll()
        rig.to_area(doll, P1, 'hand')
        victim = rig.board.find_player_area(P1, 'bench').children[0]
        rig.to_area(victim, P1, 'activePokemonArea')
        tool = self.add(rig, fixtures.definition('BW9.LifeDew_107'), P1, 'hand')
        rig.attach(tool, victim)
        await self.enable_altered_creation(rig, attacker_id)
        ctx = self.context(rig, attacker_id)
        prizes = rig.board.find_player_area(attacker_id, 'prizePile')
        before = len(prizes.children)
        await ctx.deal_damage(1000, target=victim)
        await rig.session.resolve_knockouts(ctx)
        self.assertEqual(len(prizes.children), before - 1)

    async def test_attack_bonus_still_applies_without_a_no_prize_rule(self):
        rig, doll, attacker_id = self.setup_doll()
        rig.to_area(doll, P1, 'hand')
        victim = rig.board.find_player_area(P1, 'bench').children[0]
        rig.to_area(victim, P1, 'activePokemonArea')
        ctx = self.context(rig, attacker_id)
        ctx.extra_prizes = 2
        prizes = rig.board.find_player_area(attacker_id, 'prizePile')
        before = len(prizes.children)
        await ctx.deal_damage(1000, target=victim)
        await rig.session.resolve_knockouts(ctx)
        self.assertEqual(len(prizes.children), before - 3)

    async def test_last_doll_loses_by_empty_field_without_awarding_prizes(self):
        rig, doll, attacker_id = self.setup_doll()
        for card in list(rig.board.find_player_area(P1, 'bench').children):
            rig.to_area(card, P1, 'hand')
        ctx = self.context(rig, attacker_id)
        with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes, \
                patch.object(rig.session, 'end_game', wraps=rig.session.end_game) as end:
            with self.assertRaises(GameOver):
                await ctx.deal_damage(1000, target=doll)
                await rig.session.resolve_knockouts(ctx)
        prizes.assert_not_awaited()
        self.assertEqual(end.call_args.args[0], attacker_id)


if __name__ == '__main__':
    unittest.main()
