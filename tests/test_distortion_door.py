"""Giratina's Distortion Door enters from discard and places separate counters."""

import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.tools.effect_smoke import P1, P2


class DistortionDoorTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig

    @staticmethod
    def ability_entry(rig, source, ability):
        return next((entry for entry in compute_legal_actions(
            rig.board, rig.session.turn_state, P1, rig.session.game_id)
            if entry['entityID'] == source.entity_id
            and entry['selectableAction']['actionID'] == ability.ability_id), None)

    async def test_discard_entry_places_one_counter_on_two_distinct_bench_targets(self):
        rig, entities = self.rig('Promo_SM.Giratina_151')
        ability = fixtures.definition('Promo_SM.Giratina_151').abilities[0]
        source = next(card for card in rig.board.find_player_area(P1, 'discard').children
                      if card.archetype_id == fixtures.definition(
                          'Promo_SM.Giratina_151').guid)
        extra = rig.pull_guid(P2, self.filler.guid)
        rig.to_area(extra, P2, 'bench')
        targets = list(rig.board.find_player_area(P2, 'bench').children)
        chosen = targets[:2]
        active = rig.board.active_pokemon(P2)
        hp_before = {card.entity_id: card.get_attribute(AttrID.HP)
                     for card in [*targets, active]}
        entry = self.ability_entry(rig, source, ability)
        self.assertIsNotNone(entry)

        with patch.object(EffectContext, 'choose_cards',
                          AsyncMock(return_value=chosen)) as choose:
            await rig.session._execute_use_ability(P1, source, entry)

        self.assertIn(source, rig.board.find_player_area(P1, 'bench').children)
        choose.assert_awaited_once()
        for target in chosen:
            self.assertEqual(target.get_attribute(AttrID.HP),
                             hp_before[target.entity_id] - 10)
        self.assertEqual(targets[2].get_attribute(AttrID.HP),
                         hp_before[targets[2].entity_id])
        self.assertEqual(active.get_attribute(AttrID.HP),
                         hp_before[active.entity_id])

    async def test_full_bench_hides_discard_ability(self):
        rig, _ = self.rig('Promo_SM.Giratina_151')
        ability = fixtures.definition('Promo_SM.Giratina_151').abilities[0]
        source = next(card for card in rig.board.find_player_area(P1, 'discard').children
                      if card.archetype_id == fixtures.definition(
                          'Promo_SM.Giratina_151').guid)
        bench = rig.board.find_player_area(P1, 'bench')
        while len(bench.children) < 5:
            card = rig.pull_guid(P1, self.filler.guid)
            rig.to_area(card, P1, 'bench')

        self.assertIsNone(self.ability_entry(rig, source, ability))

    async def test_one_opposing_bench_gets_one_counter_without_target_prompt(self):
        rig, _ = self.rig('Promo_SM.Giratina_151')
        ability = fixtures.definition('Promo_SM.Giratina_151').abilities[0]
        source = next(card for card in rig.board.find_player_area(P1, 'discard').children
                      if card.archetype_id == fixtures.definition(
                          'Promo_SM.Giratina_151').guid)
        targets = list(rig.board.find_player_area(P2, 'bench').children)
        rig.to_area(targets[1], P2, 'hand')
        hp_before = targets[0].get_attribute(AttrID.HP)

        with patch.object(EffectContext, 'choose_cards',
                          AsyncMock()) as choose:
            await rig.session._execute_use_ability(
                P1, source, self.ability_entry(rig, source, ability),
            )

        self.assertIn(source, rig.board.find_player_area(P1, 'bench').children)
        self.assertEqual(targets[0].get_attribute(AttrID.HP), hp_before - 10)
        choose.assert_not_awaited()


if __name__ == '__main__':
    unittest.main()
