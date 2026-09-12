"""Two physical cards, one LEGEND Pokemon: legal play and zone transitions."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import prize_value
from spirit.game.legend import complementary_halves
from spirit.game.session.effects import EffectContext, is_evolution_pokemon, split_pokemon_stack
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.game.session.passives import compute_damage
from spirit.tools.effect_smoke import P1, P2


# Reuse fixtures without inheriting (and duplicating) the older test methods.
class LegendTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def pair(self, rig, zone='hand'):
        return [self.add(rig, definition('HGSS1.LugiaLEGEND_' + str(n)), P1, zone)
                for n in (113, 114)]

    async def test_only_complementary_halves_are_playable(self):
        rig, e = self.rig('HGSS1.LugiaLEGEND_113')
        first = self.add(rig, definition('HGSS1.LugiaLEGEND_113'), P1, 'hand')
        duplicate = self.add(rig, definition('HGSS1.LugiaLEGEND_113'), P1, 'hand')
        def offered():
            return {entry['entityID'] for entry in compute_legal_actions(
                rig.board, rig.session.turn_state, P1, rig.session.game_id)}
        self.assertFalse(complementary_halves(first, duplicate))
        self.assertNotIn(first.entity_id, offered())
        second = self.add(rig, definition('HGSS1.LugiaLEGEND_114'), P1, 'hand')
        self.assertIn(first.entity_id, offered())
        self.assertIn(second.entity_id, offered())
        for _ in range(2):
            self.add(rig, self.filler, P1, 'bench')
        self.assertNotIn(first.entity_id, offered())

    async def test_manual_pair_play_from_either_half(self):
        for clicked in (0, 1):
            with self.subTest(clicked=clicked):
                rig, e = self.rig('HGSS1.LugiaLEGEND_113')
                first, second = self.pair(rig)
                rig.session._fire_triggered_abilities = AsyncMock(return_value=False)
                rig.session.fire_pokemon_benched_triggers = AsyncMock()
                await rig.session._execute_play_basic(P1, (first, second)[clicked])
                self.assertIs(first.parent, rig.board.find_player_area(P1, 'bench'))
                self.assertIs(second.parent, first)
                self.assertEqual(len(rig.board.pokemon_in_play(P1)), 5)
                self.assertIn(first.entity_id, rig.session.turn_state.entered_play_turn)
                rig.session._fire_triggered_abilities.assert_awaited_once()
                rig.session.fire_pokemon_benched_triggers.assert_not_awaited()

    async def test_pair_validation_is_atomic(self):
        rig, e = self.rig('HGSS1.LugiaLEGEND_113')
        first, second = self.pair(rig)
        ctx = EffectContext(rig.session, P1, first, None)
        rig.to_area(second, P1, 'deck')
        self.assertFalse(await ctx.put_legend(first, second))
        self.assertIs(first.parent, rig.board.find_player_area(P1, 'hand'))
        rig.to_area(second, P1, 'hand')
        for _ in range(2):
            self.add(rig, self.filler, P1, 'bench')
        self.assertFalse(await ctx.put_legend(first, second))
        self.assertIs(second.parent, first.parent)

    async def test_legend_is_not_evolution_but_both_halves_return(self):
        rig, e = self.rig('HGSS1.LugiaLEGEND_113')
        first, second = self.pair(rig)
        ctx = EffectContext(rig.session, P1, first, None)
        self.assertTrue(await ctx.put_legend(first, second))
        self.assertFalse(is_evolution_pokemon(first))
        self.assertIsNone(await rig.session.perform_devolution(first))
        line, attachments = split_pokemon_stack(first)
        self.assertCountEqual(line, [first, second])
        self.assertEqual(attachments, [])
        await ctx.put_in_hand(line)
        self.assertTrue(all(c.parent is rig.board.find_player_area(P1, 'hand') for c in line))

    async def test_prizes_and_dual_weakness(self):
        for path, count in [('HGSS1.LugiaLEGEND_113', 1), ('HGSS1.HoOhLEGEND_111', 1),
                            ('HGSS2.SuicuneEnteiLEGEND_94', 2)]:
            self.assertEqual(prize_value(definition(path).guid), count)
        rig, e = self.rig('HGSS2.RaikouSuicuneLEGEND_92')
        defender = self.add(rig, definition('HGSS2.SuicuneEnteiLEGEND_94'), P2, 'bench')
        rig.to_area(e['p2_active'], P2, 'discard')
        rig.to_area(defender, P2, 'activePokemonArea')
        self.assertEqual(compute_damage(rig.board, e['target'], defender, 30).amount, 120)
        e['target'].set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        self.assertEqual(compute_damage(rig.board, e['target'], defender, 30).amount, 60)

    async def test_legend_box_rejects_duplicate_half_and_uses_real_capacity(self):
        for mode in ('duplicate', 'full', 'valid'):
            with self.subTest(mode=mode):
                rig, e = self.rig('HGSS3.LegendBox_75', 'trainer')
                deck = rig.board.find_player_area(P1, 'deck')
                for card in list(deck.children):
                    rig.to_area(card, P1, 'discard')
                first, second = self.pair(rig, 'deck')
                if mode == 'duplicate':
                    rig.to_area(second, P1, 'discard')
                    second = self.add(rig, definition('HGSS1.LugiaLEGEND_113'), P1, 'deck')
                if mode == 'full':
                    while len(rig.board.find_player_area(P1, 'bench').children) < 5:
                        self.add(rig, self.filler, P1, 'bench')
                rig.session._fire_triggered_abilities = AsyncMock(return_value=False)
                ctx = EffectContext(rig.session, P1, e['target'], None)
                await definition('HGSS3.LegendBox_75').effect(ctx)
                if mode == 'valid':
                    self.assertIs(second.parent, first)
                    rig.session._fire_triggered_abilities.assert_awaited_once()
                else:
                    self.assertIs(first.parent, deck)
                    self.assertIs(second.parent, deck)
                    rig.session._fire_triggered_abilities.assert_not_awaited()
