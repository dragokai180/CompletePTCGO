"""Aurora Energy's hand cost also applies to Ability attachments."""

import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext, resolve_activated_ability
from spirit.tools.effect_smoke import P1


class AuroraCrazyCodeTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_crazy_code(self):
        rig, entities = self.rig('SM10.PorygonZ_157')
        source = entities['target']
        ability = next(a for a in fixtures.definition('SM10.PorygonZ_157').abilities
                       if a.title == 'Crazy Code')
        for card in list(rig.board.find_player_area(P1, 'hand').children):
            rig.to_area(card, P1, 'deck')
        energy = self.add(rig, fixtures.definition('SWSH1.AuroraEnergy_186'),
                          P1, 'hand')
        return rig, source, ability, energy

    async def test_crazy_code_pays_aurora_cost_before_attaching(self):
        for temple in (False, True):
            with self.subTest(temple=temple):
                rig, source, ability, energy = self.setup_crazy_code()
                fodder = self.add(rig, self.filler, P1, 'hand')
                if temple:
                    stadium = self.add(
                        rig, fixtures.definition('SWSH10.TempleofSinnoh_155'),
                        P1, 'hand')
                    rig.board.move_card(
                        stadium.entity_id,
                        rig.board.find_global_area('activeStadium').entity_id)
                rig.session.prompt_entity_picker = AsyncMock(
                    side_effect=lambda pid, sid, cards, *args, **kwargs:
                        [cards[0].entity_id])

                await resolve_activated_ability(rig.session, P1, source, ability)

                self.assertIn(energy, rig.board.attached_energies(source))
                self.assertIn(fodder,
                              rig.board.find_player_area(P1, 'discard').children)
                self.assertNotIn(fodder,
                                 rig.board.find_player_area(P1, 'hand').children)

    async def test_crazy_code_does_not_offer_aurora_without_discard(self):
        rig, source, ability, energy = self.setup_crazy_code()
        rig.session.prompt_entity_picker = AsyncMock()

        await resolve_activated_ability(rig.session, P1, source, ability)

        self.assertIn(energy, rig.board.find_player_area(P1, 'hand').children)
        rig.session.prompt_entity_picker.assert_not_awaited()

    async def test_aurora_from_discard_has_no_hand_cost(self):
        rig, source, _, energy = self.setup_crazy_code()
        rig.to_area(energy, P1, 'discard')
        ctx = EffectContext(rig.session, P1, source, None)

        self.assertTrue(await ctx.attach_energy(energy, source))
        self.assertIn(energy, rig.board.attached_energies(source))


if __name__ == '__main__':
    unittest.main()
