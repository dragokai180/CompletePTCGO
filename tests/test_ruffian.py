"""Ruffian discards each available attachment category independently."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class RuffianTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_each_available_attachment_is_discarded(self):
        for number in (157, 181):
            for tool_present, energy_present in ((True, False), (False, True), (True, True)):
                with self.subTest(number=number, tool=tool_present, energy=energy_present):
                    path = f'SV09.Ruffian_{number}'
                    rig, entities = self.rig(path, 'trainer')
                    card = fixtures.definition(path)
                    target = rig.board.active_pokemon(P2)
                    attachments = []
                    if tool_present:
                        tool = self.add(rig, fixtures.definition('SV2.BraveryCharm_173'), P2, 'hand')
                        rig.attach(tool, target)
                        attachments.append(tool)
                    if energy_present:
                        energy = self.add(rig, fixtures.definition('SV05.MistEnergy_161'), P2, 'hand')
                        rig.attach(energy, target)
                        attachments.append(energy)
                    self.assertTrue(card.condition(rig.board, P1))

                    ctx = EffectContext(rig.session, P1, entities['target'], None)
                    ctx.choose_pokemon = AsyncMock(return_value=target)
                    ctx.choose_cards = AsyncMock(side_effect=lambda pool, *_args, **_kwargs: list(pool[:1]))
                    await card.effect(ctx)
                    self.assertEqual(ctx.choose_cards.await_count, len(attachments))
                    for attachment in attachments:
                        self.assertIn(attachment, ctx.discard_pile(P2))

    async def test_requires_an_eligible_attachment(self):
        rig, _ = self.rig('SV09.Ruffian_157', 'trainer')
        self.assertFalse(fixtures.definition('SV09.Ruffian_157').condition(rig.board, P1))
