"""Propagation's activation is the opt-in; no second confirmation."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1


class PropagationConfirmationTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_both_prints_return_directly_to_hand(self):
        for path in ('BW9.Exeggcute_4', 'BW10.Exeggcute_102'):
            with self.subTest(path=path):
                rig, e = self.rig('BW1.Snivy_1')
                card = self.add(rig, definition(path), P1, 'discard')
                ability = definition(path).abilities[0]
                ctx = EffectContext(rig.session, P1, card, ability)
                ctx.ask_yes_no = AsyncMock(return_value=False)
                await ability.effect(ctx)
                ctx.ask_yes_no.assert_not_awaited()
                self.assertIn(card, ctx.hand())
                self.assertNotIn(card, ctx.discard_pile())
