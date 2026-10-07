"""Card effects use the current Bench limit when Stadiums change it."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures

from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import effective_bench_capacity
from spirit.tools.effect_smoke import P1, P2


class FixedBenchCapacityEffectsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def set_bench(self, rig, owner, count, stadium):
        bench = rig.board.find_player_area(owner, 'bench')
        while len(bench.children) < count:
            self.add(rig, self.filler, owner, 'bench')
        field = self.add(rig, fixtures.definition(stadium), P1, 'hand')
        rig.board.move_card(
            field.entity_id,
            rig.board.find_global_area('activeStadium').entity_id,
        )
        return bench

    async def test_phantump_uses_extra_sky_field_slot(self):
        rig, entries = self.rig('SWSH2.Phantump_14')
        bench = self.set_bench(rig, P1, 7, 'XY6.SkyField_89')
        target = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1,
                          'discard')
        attack = next(a for a in fixtures.definition('SWSH2.Phantump_14').abilities
                      if a.title == 'Dark Guidance')
        ctx = EffectContext(rig.session, P1, entries['target'], attack)
        ctx.choose_cards = AsyncMock(return_value=[target])

        await attack.effect(ctx)

        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)
        self.assertEqual(len(bench.children), 8)
        self.assertIn(target, bench.children)

    async def test_orbeetle_search_is_limited_by_live_capacity(self):
        for stadium, occupied, space in (
            ('XY6.SkyField_89', 7, 1),
            ('SWSH9.CollapsedStadium_137', 4, 0),
        ):
            with self.subTest(stadium=stadium):
                rig, entries = self.rig('SWSH5.Orbeetle_65')
                bench = self.set_bench(rig, P1, occupied, stadium)
                attacker = entries['target']
                for _ in range(2):
                    energy = self.add(
                        rig, fixtures.definition('BW1.PsychicEnergy_109'),
                        P1, 'hand',
                    )
                    rig.attach(energy, attacker)
                targets = [self.add(rig, fixtures.definition('BW1.Serperior_5'),
                                    P1, 'deck') for _ in range(2)]
                attack = next(a for a in fixtures.definition('SWSH5.Orbeetle_65').abilities
                              if a.title == 'Evomancy')
                ctx = EffectContext(rig.session, P1, attacker, attack)
                ctx.search_deck = AsyncMock(return_value=targets[:space])
                ctx.shuffle_deck = AsyncMock()

                await attack.effect(ctx)

                self.assertEqual(len(bench.children), occupied + space)
                if space:
                    self.assertEqual(ctx.search_deck.await_args.kwargs['count'], space)
                    self.assertIn(targets[0], bench.children)
                else:
                    ctx.search_deck.assert_not_awaited()

    def test_battle_vip_pass_condition_uses_live_capacity(self):
        for stadium, occupied, playable in (
            ('XY6.SkyField_89', 5, True),
            ('SWSH9.CollapsedStadium_137', 4, False),
        ):
            with self.subTest(stadium=stadium):
                rig, _ = self.rig('BW1.Snivy_1')
                self.set_bench(rig, P1, occupied, stadium)
                rig.session.turn_state.turn_number = 1
                card = fixtures.definition('SWSH8.BattleVIPPass_225')
                self.assertEqual(card.condition(rig.board, P1), playable)

    async def test_captivating_poke_puff_uses_opponents_extra_slot(self):
        rig, _ = self.rig('BW1.Snivy_1')
        bench = self.set_bench(rig, P2, 7, 'XY6.SkyField_89')
        targets = [self.add(rig, fixtures.definition('BW1.Snivy_1'),
                            P2, 'hand') for _ in range(2)]
        card = fixtures.definition('XY11.CaptivatingPokPuff_99')
        source = self.add(rig, card, P1, 'hand')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.is_trainer_effect = True
        ctx.choose_cards = AsyncMock(return_value=targets[:1])

        await card.effect(ctx)

        self.assertEqual(ctx.choose_cards.await_args.args[1], 1)
        self.assertEqual(len(bench.children), 8)
        self.assertIn(targets[0], bench.children)
        self.assertIn(targets[1], ctx.hand(P2))

    async def test_accompanying_flute_uses_opponents_extra_slot(self):
        rig, _ = self.rig('BW1.Snivy_1')
        bench = self.set_bench(rig, P2, 7, 'XY6.SkyField_89')
        targets = [self.add(rig, fixtures.definition('BW1.Snivy_1'),
                            P2, 'deck') for _ in range(2)]
        card = fixtures.definition('SV06.AccompanyingFlute_142')
        source = self.add(rig, card, P1, 'hand')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.is_trainer_effect = True
        ctx.deck_top = lambda count, player_id: targets
        ctx.reveal_cards = AsyncMock()
        ctx.choose_cards = AsyncMock(return_value=targets[:1])
        ctx.shuffle_deck = AsyncMock()

        await card.effect(ctx)

        self.assertEqual(ctx.choose_cards.await_args.args[1], 1)
        self.assertEqual(len(bench.children), 8)
        self.assertIn(targets[0], bench.children)
        self.assertIn(targets[1], ctx.deck(P2))


if __name__ == '__main__':
    unittest.main()
