"""Returning an Active is not a Knock Out, but still requires a replacement."""
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext, full_stack
from spirit.game.session.game_session import GameOver
from spirit.tools.effect_smoke import P1, P2


SESSION = "spirit.game.session.game_session"


class EmptyActivePromotionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig

    async def play_return(self, path, *, bench_target=False, heads=True, damaged=False):
        rig, e = self.rig(path, "trainer")
        active = rig.board.active_pokemon(P1)
        bench = list(rig.board.find_player_area(P1, "bench").children)
        target = bench[0] if bench_target else active
        if damaged:
            target.set_attribute(AttrID.HP, target.get_attribute(AttrID.HP) - 10)
        stack = list(full_stack(target))
        with patch.object(EffectContext, "flip_coins", new=AsyncMock(return_value=[heads])), \
                patch.object(EffectContext, "choose_pokemon", new=AsyncMock(return_value=target)), \
                patch.object(rig.session, "_promote_new_active",
                             wraps=rig.session._promote_new_active) as promote:
            ended = await rig.session._execute_play_trainer(P1, e["target"])
        return rig, e, active, bench, stack, promote, ended

    async def test_every_super_scoop_up_print_promotes_after_heads(self):
        root = Path(__file__).resolve().parents[1] / "spirit/game/scripts/cards"
        paths = sorted(root.glob("*/SuperScoopUp_*.py"))
        self.assertGreaterEqual(len(paths), 7)
        for path in paths:
            with self.subTest(card=str(path.relative_to(root))):
                rig, e, old, bench, stack, promote, ended = await self.play_return(
                    f"{path.parent.name}.{path.stem}")
                promote.assert_awaited_once_with(P1)
                self.assertIn(rig.board.active_pokemon(P1), bench)
                self.assertTrue(all(c in rig.board.find_player_area(P1, "hand").children
                                    for c in stack))
                self.assertIn(e["target"], rig.board.find_player_area(P1, "discard").children)
                self.assertFalse(ended)
                self.assertFalse(rig.session.turn_state.kos_suffered)

    async def test_player_can_choose_the_second_benched_pokemon(self):
        rig, e = self.rig("BW1.SuperScoopUp_103", "trainer")
        active = rig.board.active_pokemon(P1)
        bench = list(rig.board.find_player_area(P1, "bench").children)
        chosen = bench[-1]
        original_promote = rig.session._promote_new_active

        async def human_promote(pid):
            # Use the real network offer/parser with a deterministic human reply.
            # Only promotion treats the smoke player as human; other prompts stay AI.
            with patch(SESSION + ".AIPlayer", type("NotTheSmokePlayer", (), {})):
                return await original_promote(pid)

        async def reply(player, message_type, offer, **kwargs):
            self.assertIsNone(rig.board.active_pokemon(P1))
            self.assertEqual(set(offer["targetMap"]), {p.entity_id for p in bench})
            self.assertIn(active, rig.board.find_player_area(P1, "hand").children)
            self.assertIn(e["target"], rig.board.find_player_area(P1, "discard").children)
            return {"selection": {"entityID": chosen.entity_id}}

        with patch.object(EffectContext, "flip_coins", new=AsyncMock(return_value=[True])), \
                patch.object(EffectContext, "choose_pokemon", new=AsyncMock(return_value=active)), \
                patch.object(rig.session, "_promote_new_active", side_effect=human_promote), \
                patch.object(rig.session, "prompt_selection_message", side_effect=reply) as prompt:
            self.assertFalse(await rig.session._execute_play_trainer(P1, e["target"]))
        prompt.assert_awaited_once()
        self.assertIs(rig.board.active_pokemon(P1), chosen)

    async def test_tails_and_returning_bench_do_not_prompt_for_active(self):
        for heads, bench_target in ((False, False), (True, True)):
            with self.subTest(heads=heads, bench=bench_target):
                rig, _, active, _, _, promote, ended = await self.play_return(
                    "BW1.SuperScoopUp_103", heads=heads, bench_target=bench_target)
                promote.assert_not_awaited()
                self.assertIs(rig.board.active_pokemon(P1), active)
                self.assertFalse(ended)

    async def test_one_replacement_is_automatic(self):
        rig, e = self.rig("BW1.SuperScoopUp_103", "trainer")
        bench = list(rig.board.find_player_area(P1, "bench").children)
        for card in bench[1:]:
            rig.to_area(card, P1, "deck")
        active = rig.board.active_pokemon(P1)
        with patch.object(EffectContext, "flip_coins", new=AsyncMock(return_value=[True])), \
                patch.object(EffectContext, "choose_pokemon", new=AsyncMock(return_value=active)), \
                patch.object(rig.session, "prompt_selection_message", new=AsyncMock()) as prompt:
            await rig.session._execute_play_trainer(P1, e["target"])
        self.assertIs(rig.board.active_pokemon(P1), bench[0])
        prompt.assert_not_awaited()

    async def test_returning_last_pokemon_ends_game_without_awarding_prizes(self):
        rig, e = self.rig("BW1.SuperScoopUp_103", "trainer")
        for card in list(rig.board.find_player_area(P1, "bench").children):
            rig.to_area(card, P1, "deck")
        active = rig.board.active_pokemon(P1)
        prizes = list(rig.board.find_player_area(P2, "prizePile").children)
        with patch.object(EffectContext, "flip_coins", new=AsyncMock(return_value=[True])), \
                patch.object(EffectContext, "choose_pokemon", new=AsyncMock(return_value=active)), \
                patch.object(rig.session, "end_game", wraps=rig.session.end_game) as end:
            with self.assertRaises(GameOver):
                await rig.session._execute_play_trainer(P1, e["target"])
        self.assertEqual(end.await_args.args[0], P2)
        self.assertEqual(list(rig.board.find_player_area(P2, "prizePile").children), prizes)
        self.assertFalse(rig.session.turn_state.kos_suffered)

    async def test_other_return_and_shuffle_trainers_also_promote(self):
        for path, zone in (("XY4.AZ_91", "hand"), ("SV1.Penny_183", "hand"),
                           ("XY1.Cassius_115", "deck"), ("SM3.Acerola_112", "hand"),
                           ("SV4.ProfessorTurosScenario_171", "hand")):
            with self.subTest(card=path):
                rig, _, old, bench, stack, promote, ended = await self.play_return(
                    path, damaged=True)
                self.assertIn(old, rig.board.find_player_area(P1, zone).children)
                self.assertIn(rig.board.active_pokemon(P1), bench)
                promote.assert_awaited_once_with(P1)
                self.assertFalse(ended)

    async def test_both_empty_spots_replace_non_turn_player_first(self):
        rig, _ = self.rig("BW1.SuperScoopUp_103", "trainer")
        rig.session.turn_state.active_player_id = P1
        for pid in (P1, P2):
            rig.to_area(rig.board.active_pokemon(pid), pid, "hand")
        with patch.object(rig.session, "_promote_new_active",
                          wraps=rig.session._promote_new_active) as promote:
            await rig.session._settle_empty_active_spots()
            await rig.session._settle_empty_active_spots()
        self.assertEqual([call.args[0] for call in promote.await_args_list], [P2, P1])

    async def test_normal_actions_are_offered_only_after_replacement(self):
        rig, _ = self.rig("BW1.SuperScoopUp_103", "trainer")
        rig.to_area(rig.board.active_pokemon(P1), P1, "hand")

        def legal_actions(*args, **kwargs):
            self.assertIsNotNone(rig.board.active_pokemon(P1))
            return {}

        with patch(SESSION + ".compute_legal_actions", side_effect=legal_actions) as actions, \
                patch(SESSION + ".choose_action", return_value=None), \
                patch.object(rig.session, "_refresh_dynamic_attacks", new=AsyncMock()):
            await rig.session._run_player_turn(P1)
        actions.assert_called_once()

    async def test_existing_deferred_promotions_are_not_duplicated(self):
        for path in ("SWSH2.ScoopUpNet_165", "BW10.ScoopUpCyclone_95"):
            with self.subTest(card=path):
                rig, _, _, bench, _, promote, ended = await self.play_return(path)
                self.assertIn(rig.board.active_pokemon(P1), bench)
                promote.assert_awaited_once_with(P1)
                self.assertFalse(ended)
