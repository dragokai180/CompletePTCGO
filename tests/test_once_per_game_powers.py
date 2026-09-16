"""Once-per-game powers survive reprints, turn changes and replayed actions."""
import re
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PlayerAttrID
from spirit.game.data_utils import Ability, Attack, CARD_DEFS_BY_GUID, _clone_ability
from spirit.game.session.effects import EffectContext, _send_ability_brackets, _send_attack_bracket
from spirit.game.session.constants import GAME_OPTION_TOKENS_KEY
from spirit.game.session.legal_actions import _attack_entries, _ability_entries
from spirit.tools.effect_smoke import P1, P2


def entry(ability):
    return {"selectableAction": {"actionID": ability.ability_id}}


class OncePerGamePowerTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_cloning_preserves_both_power_flags(self):
        for cls in (Ability, Attack):
            for gx, vstar in ((True, False), (False, True), (False, False)):
                original = cls("Power", gx=gx, vstar=vstar)
                original.ability_id = "original"
                clone = _clone_ability(original)
                self.assertEqual((clone.gx, clone.vstar), (gx, vstar))
                self.assertIsNone(clone.ability_id)

    def test_all_registered_gx_and_vstar_reminders_have_flags(self):
        missing = []
        for card in CARD_DEFS_BY_GUID.values():
            powers = list(getattr(card, "abilities", ()) or ())
            powers += list(getattr(card, "granted_abilities", ()) or ())
            for power in powers:
                text = power.game_text.casefold()
                gx = isinstance(power, Attack) and (
                    re.search(r"(?:-|\s)GX$", power.title, re.I)
                    or "1 gx attack in a game" in text)
                vstar = "1 vstar power in a game" in text
                if (gx and not power.gx) or (vstar and not power.vstar):
                    missing.append((card.set_code, card.collector_number, power.title))
        self.assertEqual(missing, [])

    async def test_reprinted_gx_spends_marker_and_rejects_second_execution(self):
        rig, e = self.rig("HF.CharizardGX_9")
        session, source = rig.session, e["target"]
        attack = next(a for a in fixtures.definition("HF.CharizardGX_9").abilities if a.gx)
        state = session.turn_state
        state.turn_number = 4
        with patch("spirit.game.session.game_session.resolve_attack",
                   new=AsyncMock(return_value=SimpleNamespace(attack_keeps_turn=False))) as resolve:
            self.assertTrue(await session._execute_attack(P1, source, entry(attack)))
            self.assertIn(P1, state.gx_used)
            self.assertNotIn(P2, state.gx_used)
            self.assertTrue(rig.board.find_player_entity(P1).get_attribute(PlayerAttrID.HAS_GX_TOKEN))
            state.begin_turn(P2, rig.board)
            state.begin_turn(P1, rig.board)
            self.assertFalse(await session._execute_attack(P1, source, entry(attack)))
            self.assertEqual(resolve.await_count, 1)
            self.assertNotIn(attack.ability_id, {
                x["selectableAction"]["actionID"]
                for x in _attack_entries(rig.board, state, P1, session.game_id)
            })
        # Changing the card/printing cannot recover the shared match budget.
        other = self.add(rig, fixtures.definition("SM6.ZygardeGX_73"), P1, "bench")
        other_attack = next(a for a in fixtures.definition("SM6.ZygardeGX_73").abilities if a.gx)
        self.assertFalse(await session._execute_attack(P1, other, entry(other_attack)))
        self.assertFalse(await EffectContext(session, P1, source, None).use_attack(attack))

    async def test_vstar_ability_and_attack_share_budget_and_reject_replay(self):
        rig, e = self.rig("SWSH9.ArceusVSTAR_123")
        session, source = rig.session, e["target"]
        ability = next(a for a in fixtures.definition("SWSH9.ArceusVSTAR_123").abilities if a.vstar)
        with patch("spirit.game.session.game_session.resolve_activated_ability",
                   new=AsyncMock(return_value=SimpleNamespace(ends_turn=False))) as resolve:
            await session._execute_use_ability(P1, source, entry(ability))
            session.turn_state.begin_turn(P2, rig.board)
            session.turn_state.begin_turn(P1, rig.board)
            await session._execute_use_ability(P1, source, entry(ability))
            self.assertEqual(resolve.await_count, 1)
        self.assertTrue(rig.board.find_player_entity(P1).get_attribute(PlayerAttrID.HAS_VSTAR_TOKEN))
        self.assertNotIn(P1, session.turn_state.gx_used)
        self.assertEqual(_ability_entries(rig.board, session.turn_state, P1, session.game_id, [source]), [])
        attack = next(a for c in CARD_DEFS_BY_GUID.values()
                      for a in getattr(c, "abilities", ()) or ()
                      if isinstance(a, Attack) and a.vstar)
        self.assertFalse(await session._execute_attack(P1, source, entry(attack)))
        self.assertFalse(await EffectContext(session, P1, source, None).use_attack(attack))

    async def test_bonnie_exception_survives_execution_guard_but_clear_vision_wins(self):
        rig, e = self.rig("SM6.ZygardeGX_73")
        session, source = rig.session, e["target"]
        attack = next(a for a in fixtures.definition("SM6.ZygardeGX_73").abilities if a.gx)
        session.turn_state.gx_used.add(P1)
        session.turn_state.gx_repeat_names_this_turn[P1] = {"zygarde-gx"}
        with patch("spirit.game.session.game_session.resolve_attack",
                   new=AsyncMock(return_value=SimpleNamespace(attack_keeps_turn=False))) as resolve:
            self.assertTrue(await session._execute_attack(P1, source, entry(attack)))
            session.turn_state.gx_locked_players.add(P1)
            self.assertFalse(await session._execute_attack(P1, source, entry(attack)))
            self.assertEqual(resolve.await_count, 1)
        self.assertIn(P1, session.turn_state.gx_used)

    def test_tool_granted_power_creates_marker_without_vstar_pokemon(self):
        for path in ("SWSH12.ForestSealStone_156", "SWSH12.EarthenSealStone_154", "CZ.SkySealStone_143"):
            with self.subTest(path=path):
                rig, _ = self.rig("SWSH9.ArceusVSTAR_123")
                rig.board.populate_deck(P1, {"cards": [{"guid": fixtures.definition(path).guid, "count": 1}]})
                self.assertTrue(rig.board.token_kinds[P1]["VSTAR"])
                self.assertIn("VSTARToken", rig.session._build_game_options()[GAME_OPTION_TOKENS_KEY])
                self.assertFalse(rig.board.find_player_entity(P1).get_attribute(PlayerAttrID.HAS_VSTAR_TOKEN))

    async def test_vstar_marker_flip_is_sent_to_both_players(self):
        rig, e = self.rig("SWSH9.ArceusVSTAR_123")
        ability = next(a for a in fixtures.definition("SWSH9.ArceusVSTAR_123").abilities if a.vstar)
        ctx = EffectContext(rig.session, P1, e["target"], ability)
        rig.session.send_game_sequence = AsyncMock()
        await _send_ability_brackets(rig.session, ctx, e["target"], ability)
        from spirit.network.message_names import OutboundMsg
        marker = OutboundMsg.VSTAR_POWER_USED_EFFECT.value
        matching = [call for call in rig.session.send_game_sequence.await_args_list if marker in str(call.args)]
        self.assertEqual(len(matching), 2)
        self.assertEqual({id(call.args[0][0]) for call in matching},
                         {id(player) for player in rig.session.players.values()})

    async def test_gx_marker_flip_is_sent_to_both_players(self):
        rig, e = self.rig("HF.CharizardGX_9")
        ability = next(a for a in fixtures.definition("HF.CharizardGX_9").abilities if a.gx)
        ctx = EffectContext(rig.session, P1, e["target"], ability)
        rig.session.send_game_sequence = AsyncMock()
        rig.session._broadcast_attack_sources = AsyncMock()
        await _send_attack_bracket(rig.session, ctx, ability.ability_id, ability.title)
        from spirit.network.message_names import OutboundMsg
        marker = OutboundMsg.GX_ATTACK_USED_EFFECT.value
        matching = [call for call in rig.session.send_game_sequence.await_args_list if marker in str(call.args)]
        self.assertEqual(len(matching), 2)
        self.assertEqual({id(call.args[0][0]) for call in matching},
                         {id(player) for player in rig.session.players.values()})
