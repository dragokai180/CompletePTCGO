"""Prize bonuses require the KO and victim described by the card."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class PrizeBonusAttackConditionsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_attack(self, path, title, victim=None, hp=100):
        rig, entities = self.rig(path)
        defender = rig.board.active_pokemon(P2)
        if victim is not None:
            rig.to_area(defender, P2, "hand")
            defender = self.add(rig, fixtures.definition(victim),
                                P2, "activePokemonArea")
        defender.set_attribute(AttrID.HP, hp)
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
        defender.set_attribute(AttrID.RESISTANCE_TYPES, [])
        attack = next(ability for ability in fixtures.definition(path).abilities
                      if ability.title == title)
        return rig, EffectContext(rig.session, P1, entities["target"], attack)

    async def test_conditional_attack_bonus_uses_only_eligible_knockouts(self):
        cases = (
            ("SM11.MegaSableyeTyranitarGX_126", "Greedy Crush",
             "SM10.HonchkrowGX_109", 3),
            ("SM11.MegaSableyeTyranitarGX_126", "Greedy Crush",
             "XY10.UmbreonEX_55", 3),
            ("SM11.MegaSableyeTyranitarGX_126", "Greedy Crush",
             "SV10.Arbolivaex_23", 2),
            ("SM11.MegaSableyeTyranitarGX_126", "Greedy Crush", None, 1),
            ("XY10.UmbreonEX_55", "Endgame", "XY5.PrimalKyogreEX_55", 4),
            ("XY10.UmbreonEX_55", "Endgame", "SM10.HonchkrowGX_109", 2),
            ("SM4.GuzzlordGX_63", "Glutton-GX", None, 3),
        )
        for path, title, victim, expected in cases:
            with self.subTest(attack=title, victim=victim):
                rig, ctx = self.setup_attack(
                    path, title, victim, hp=50 if title == "Endgame" else 100)
                with patch.object(rig.session, "_take_prizes", AsyncMock()) as prizes:
                    await ctx.ability.effect(ctx)
                    await rig.session.resolve_knockouts(ctx)
                prizes.assert_awaited_once_with(P1, expected,
                                                destination="hand")

    async def test_greedy_crush_nonlethal_hit_gets_no_bonus(self):
        rig, ctx = self.setup_attack("SM11.MegaSableyeTyranitarGX_126",
                                     "Greedy Crush", "SM10.HonchkrowGX_109",
                                     hp=250)
        with patch.object(rig.session, "_take_prizes", AsyncMock()) as prizes:
            await ctx.ability.effect(ctx)
            await rig.session.resolve_knockouts(ctx)
        prizes.assert_not_awaited()
        self.assertEqual(ctx.extra_prizes, 0)

    async def test_greedy_eater_requires_a_basic_victim(self):
        for victim, expected in ((None, 2), ("SM10.HonchkrowGX_109", 2)):
            with self.subTest(victim=victim):
                rig, ctx = self.setup_attack("RSV10PT5.Hydreigonex_67",
                                             "Dark Bite", victim)
                with patch.object(rig.session, "_take_prizes", AsyncMock()) as prizes:
                    await ctx.ability.effect(ctx)
                    await rig.session.resolve_knockouts(ctx)
                prizes.assert_awaited_once_with(P1, expected,
                                                destination="hand")

    async def test_next_turn_prize_mark_accepts_both_word_orders(self):
        for path, title in (("SM2.Whimsicott_91", "The Wages of Fluff"),
                            ("SV05.Ribombee_76", "Plentiful Pollen")):
            with self.subTest(attack=title):
                rig, ctx = self.setup_attack(path, title, hp=300)
                await ctx.ability.effect(ctx)
                marks = [entry for entry in rig.board.temporary_passives
                         if getattr(entry.passive, "bonus", None) == 2]
                self.assertEqual(len(marks), 1)
                self.assertEqual(marks[0].carrier_entity_id,
                                 ctx.defender.entity_id)

    def test_beast_bringer_only_rewards_an_active_gx_or_ex(self):
        rig, entities = self.rig("SM6.Buzzwole_77")
        attacker = entities["target"]
        tool_def = fixtures.definition("SM10.BeastBringer_164")
        tool = self.add(rig, tool_def, P1, "hand")
        rig.attach(tool, attacker)
        old_active = rig.board.active_pokemon(P2)
        rig.to_area(old_active, P2, "hand")
        gx = fixtures.definition("SM10.HonchkrowGX_109")
        active = self.add(rig, gx, P2, "activePokemonArea")
        benched = self.add(rig, gx, P2, "bench")
        attack = next(ability for ability in fixtures.definition(
            "SM6.Buzzwole_77").abilities if ability.title == "Sledgehammer")
        ctx = EffectContext(rig.session, P1, attacker, attack)
        ctx.attack_damage[active.entity_id] = (100, 100)
        ctx.attack_damage[benched.entity_id] = (100, 100)
        passive = tool_def.passive
        self.assertEqual(passive.modify_prizes_for_knockout(
            active, ctx, 2, tool), 3)
        self.assertEqual(passive.modify_prizes_for_knockout(
            benched, ctx, 2, tool), 2)
