"""Slimy Sliding consumes a declared Retreat even when tails stops the swap."""

import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _retreat_entry
from spirit.tools.effect_smoke import P1, P2


class SlimySlidingRetreatTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_coin_result_controls_swap_but_both_results_use_retreat(self):
        for goodra_path in ('ME4.Goodra_68', 'MEP.Goodra_77'):
            for heads in (False, True):
                with self.subTest(goodra=goodra_path, heads=heads):
                    rig, entities = self.rig('BW1.Snivy_1')
                    self.add(rig, fixtures.definition(goodra_path), P2, 'bench')
                    active = entities['p1_active']
                    replacement = rig.board.find_player_area(P1, 'bench').children[0]
                    energy = rig.board.attached_energies(active)[0]
                    entry = _retreat_entry(
                        rig.board, rig.session.turn_state, P1,
                        rig.session.game_id,
                    )[0]
                    with patch.object(
                        EffectContext, 'flip_coins',
                        AsyncMock(return_value=[heads]),
                    ) as flip:
                        await rig.session._execute_retreat(
                            P1, active, entry,
                            [replacement.entity_id, energy.entity_id],
                        )

                    flip.assert_awaited_once()
                    self.assertTrue(rig.session.turn_state.retreated)
                    self.assertEqual(
                        _retreat_entry(rig.board, rig.session.turn_state,
                                       P1, rig.session.game_id),
                        [],
                    )
                    if heads:
                        self.assertIs(rig.board.active_pokemon(P1), replacement)
                        self.assertIn(energy, rig.board.find_player_area(
                            P1, 'discard').children)
                    else:
                        self.assertIs(rig.board.active_pokemon(P1), active)
                        self.assertIn(energy, rig.board.attached_energies(active))


if __name__ == '__main__':
    unittest.main()
