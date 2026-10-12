"""Restrictions on card categories played from the hand."""
import unittest
from unittest.mock import AsyncMock, Mock

from tests import test_hgss_rules as fixtures
from spirit.game.session.passives import energy_attachment_blocked, trainer_play_blocked
from spirit.tools.effect_smoke import P1, P2


class HandPlayRestrictorTests(unittest.TestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_ruler_of_the_night_blocks_all_three_categories_only_for_opponent(self):
        for honchkrow in (
            'SM10.HonchkrowGX_109',
            'SM10.HonchkrowGX_202',
            'SM10.HonchkrowGX_223',
        ):
            with self.subTest(honchkrow=honchkrow):
                rig, entities = self.rig(honchkrow)
                stadium = self.add(rig, fixtures.definition('SV1.Mesagoza_178'), P2, 'hand')
                tool = self.add(rig, fixtures.definition('SM8.FairyCharmPsychic_175'), P2, 'hand')
                item = self.add(rig, self.item, P2, 'hand')
                supporter = self.add(rig, fixtures.definition('SM1.Hau_120'), P2, 'hand')
                energy = self.add(rig, fixtures.definition('SM4.CounterEnergy_100'), P2, 'hand')
                basic_energy = self.add(rig, fixtures.definition('Free_Energy.PsychicEnergy_5'), P2, 'hand')
                own_stadium = self.add(rig, fixtures.definition('SV1.Mesagoza_178'), P1, 'hand')
                opponent_active = rig.board.active_pokemon(P2)

                self.assertTrue(trainer_play_blocked(rig.board, P2, stadium))
                self.assertTrue(trainer_play_blocked(rig.board, P2, tool))
                self.assertTrue(energy_attachment_blocked(rig.board, P2, energy, opponent_active))
                self.assertFalse(trainer_play_blocked(rig.board, P2, item))
                self.assertFalse(trainer_play_blocked(rig.board, P2, supporter))
                self.assertFalse(energy_attachment_blocked(rig.board, P2, basic_energy, opponent_active))
                self.assertFalse(trainer_play_blocked(rig.board, P1, own_stadium))

                rig.to_area(entities['target'], P1, 'bench')
                self.assertFalse(trainer_play_blocked(rig.board, P2, stadium))
                self.assertFalse(trainer_play_blocked(rig.board, P2, tool))
                self.assertFalse(energy_attachment_blocked(rig.board, P2, energy, opponent_active))

    def test_other_stadium_and_item_restrictors(self):
        for path, card_path, blocked_on_bench in (
            ('SM7.Regice_45', 'SV1.Mesagoza_178', False),
            ('SV065.Copperajah_42', 'SV1.Mesagoza_178', False),
            ('XY5.Ninetales_21', 'SV1.Mesagoza_178', True),
            ('SV09.Tyranitar_95', None, False),
        ):
            with self.subTest(path=path):
                rig, entities = self.rig(path)
                card = self.add(rig, fixtures.definition(card_path) if card_path else self.item, P2, 'hand')
                self.assertTrue(trainer_play_blocked(rig.board, P2, card))
                rig.to_area(entities['target'], P1, 'bench')
                self.assertEqual(trainer_play_blocked(rig.board, P2, card), blocked_on_bench)


class CoinRestrictorTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_hand_restrictor_activates_only_on_heads(self):
        for path, title, blocks_all_trainers in (
            ('SM9.Psyduck_26', 'Headache', True),
            ('XY1.Krookodile_71', 'Bother', False),
        ):
            for heads in (False, True):
                with self.subTest(path=path, heads=heads):
                    rig, entities, ctx = self.ctx(path, title)
                    supporter = self.add(rig, fixtures.definition('SM1.Hau_120'), P2, 'hand')
                    stadium = self.add(rig, fixtures.definition('SV1.Mesagoza_178'), P2, 'hand')
                    item = self.add(rig, self.item, P2, 'hand')
                    ctx.flip_coins = AsyncMock(return_value=[heads])
                    ctx.deal_damage = AsyncMock()
                    ctx.lock_plays = Mock()

                    await ctx.ability.effect(ctx)

                    self.assertEqual(ctx.lock_plays.call_count, int(heads))
                    if heads:
                        player_id, predicate = ctx.lock_plays.call_args.args
                        self.assertEqual(player_id, P2)
                        self.assertTrue(predicate(supporter))
                        self.assertEqual(predicate(stadium), blocks_all_trainers)
                        self.assertEqual(predicate(item), blocks_all_trainers)


if __name__ == '__main__':
    unittest.main()
