"""Telepathic Psychic Energy respects the live Bench limit on attachment."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition

from spirit.game.session.effects import resolve_energy_on_attach
from spirit.game.session.passives import effective_bench_capacity
from spirit.tools.effect_smoke import P1


class TelepathicPsychicEnergyTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_benches_two_psychic_pokemon_without_crashing(self):
        rig, entities = self.rig('BW1.Munna_48')
        energy = self.add(rig, definition('ME3.TelepathicPsychicEnergy_88'), P1, 'hand')
        basics = [self.add(rig, definition('BW1.Munna_48'), P1, 'deck')
                  for _ in range(2)]
        bench = rig.board.find_player_area(P1, 'bench')
        before = len(bench.children)
        rig.session.prompt_card_chooser = AsyncMock(
            return_value=[card.entity_id for card in basics])

        rig.attach(energy, entities['target'])
        await resolve_energy_on_attach(rig.session, P1, energy, entities['target'])

        self.assertEqual(len(bench.children), before + 2)
        self.assertTrue(all(card in bench.children for card in basics))
        self.assertEqual(rig.session.prompt_card_chooser.await_args.args[3], 2)

    async def test_expanded_bench_uses_effective_capacity(self):
        rig, entities = self.rig('BW1.Munna_48')
        energy = self.add(rig, definition('ME3.TelepathicPsychicEnergy_88'), P1, 'hand')
        bench = rig.board.find_player_area(P1, 'bench')
        while len(bench.children) < 5:
            self.add(rig, self.filler, P1, 'bench')
        self.assertEqual(len(bench.children), 5)
        stadium = self.add(rig, definition('XY6.SkyField_89'), P1, 'hand')
        rig.board.move_card(
            stadium.entity_id,
            rig.board.find_global_area('activeStadium').entity_id)
        self.assertGreater(effective_bench_capacity(rig.board, P1), 5)
        basics = [self.add(rig, definition('BW1.Munna_48'), P1, 'deck')
                  for _ in range(2)]
        rig.session.prompt_card_chooser = AsyncMock(
            return_value=[card.entity_id for card in basics])

        rig.attach(energy, entities['target'])
        await resolve_energy_on_attach(rig.session, P1, energy, entities['target'])

        self.assertEqual(len(bench.children), 7)
        self.assertTrue(all(card in bench.children for card in basics))

    async def test_full_bench_skips_search(self):
        rig, entities = self.rig('BW1.Munna_48')
        energy = self.add(rig, definition('ME3.TelepathicPsychicEnergy_88'), P1, 'hand')
        bench = rig.board.find_player_area(P1, 'bench')
        while len(bench.children) < effective_bench_capacity(rig.board, P1):
            self.add(rig, self.filler, P1, 'bench')
        rig.session.prompt_card_chooser = AsyncMock()

        rig.attach(energy, entities['target'])
        await resolve_energy_on_attach(rig.session, P1, energy, entities['target'])

        self.assertEqual(len(bench.children), effective_bench_capacity(rig.board, P1))
        rig.session.prompt_card_chooser.assert_not_awaited()
