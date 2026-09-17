"""Printed removal rules are not Abilities; Despair Ray counts discards."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Ability
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _ability_entries
from spirit.game.session.passives import ability_locked
from spirit.tools.effect_smoke import P1, P2


class RoboSubstituteDespairRayTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def install_lock(self, rig, lock):
        if lock == 'turn_effect':
            state = rig.session.turn_state
            state.abilities_disabled_through_turn = state.turn_number + 1
        elif lock == 'silent_lab':
            stadium = self.add(rig, definition('XY5.SilentLab_140'), P2, 'hand')
            rig.board.move_card(stadium.entity_id,
                                rig.board.find_global_area('activeStadium').entity_id)
        else:
            garbodor = self.add(rig, definition('BW6.Garbodor_54'), P2, 'bench')
            tool = self.add(rig, definition('BW9.FloatStone_99'), P2, 'hand')
            rig.attach(tool, garbodor)

    async def test_robo_removal_works_under_ability_locks_active_and_bench(self):
        path = 'XY4.RoboSubstituteTeamFlareGear_102'
        for lock in ('turn_effect', 'silent_lab', 'garbotoxin'):
            for active in (True, False):
                with self.subTest(lock=lock, active=active):
                    rig, e = self.rig(path, 'trainer')
                    robo = e['target']
                    if active:
                        rig.to_area(rig.board.active_pokemon(P1), P1, 'hand')
                    rig.to_area(robo, P1, 'activePokemonArea' if active else 'bench')
                    self.install_lock(rig, lock)
                    ability = definition(path).abilities[0]
                    self.assertFalse(ability_locked(rig.board, robo, ability))
                    basic = self.add(rig, definition('BW1.Snivy_1'), P1, 'bench')
                    self.assertTrue(ability_locked(rig.board, basic, Ability('Real Ability')))
                    ctx = EffectContext(rig.session, P1, robo, ability)
                    self.assertFalse(ctx.is_ability_effect())
                    rig.attach_energy_type(P1, robo, PokemonTypes.WATER.value)
                    attachments = list(robo.children)
                    entries = _ability_entries(rig.board, rig.session.turn_state,
                                               P1, rig.session.game_id, [robo])
                    self.assertEqual(len(entries), 1)
                    with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes, \
                            patch.object(rig.session, '_broadcast_attack_sources', AsyncMock()) as banner:
                        await rig.session._execute_use_ability(P1, robo, entries[0])
                    self.assertIn(robo, ctx.discard_pile())
                    for card in attachments:
                        self.assertIn(card, ctx.discard_pile())
                    self.assertIsNotNone(rig.board.active_pokemon(P1))
                    prizes.assert_not_awaited()
                    banner.assert_not_awaited()

    async def test_other_doll_and_fossil_removal_rules_not_suppressed(self):
        for path in ('SM12.LilliesPokDoll_197', 'SV4.SnorlaxDoll_175',
                     'SWSH12.UnidentifiedFossil_165', 'ME5.AntiqueArmorFossil_72'):
            with self.subTest(path=path):
                rig, e = self.rig(path, 'trainer')
                rig.to_area(rig.board.active_pokemon(P1), P1, 'hand')
                rig.to_area(e['target'], P1, 'activePokemonArea')
                self.install_lock(rig, 'turn_effect')
                ability = definition(path).abilities[0]
                self.assertTrue(ability.is_rule_action)
                self.assertFalse(ability_locked(rig.board, e['target'], ability))
                self.assertEqual(len(_ability_entries(rig.board, rig.session.turn_state,
                    P1, rig.session.game_id, [e['target']])), 1)
                for real_ability in definition(path).abilities[1:]:
                    self.assertFalse(real_ability.is_rule_action)
                    self.assertTrue(ability_locked(rig.board, e['target'], real_ability))

    async def test_despair_ray_counts_only_selected_discards_both_printings(self):
        for path in ('XY11.MGardevoirEX_79', 'XY11.MGardevoirEX_112'):
            for count in (0, 1, 3):
                with self.subTest(path=path, count=count):
                    rig, e = self.rig(path)
                    attack = next(a for a in definition(path).abilities if a.title == 'Despair Ray')
                    ctx = EffectContext(rig.session, P1, e['target'], attack)
                    bench = list(ctx.my_bench())
                    self.assertEqual(len(bench), 3)
                    rig.attach_energy_type(P1, bench[0], PokemonTypes.WATER.value)
                    attachments = list(bench[0].children)
                    picks = bench[:count]
                    ctx.choose_cards = AsyncMock(return_value=picks)
                    ctx.deal_damage = AsyncMock()
                    await attack.effect(ctx)
                    ctx.deal_damage.assert_awaited_once()
                    self.assertEqual(ctx.deal_damage.await_args.args[0], 110 + 10 * count)
                    self.assertEqual(ctx.my_bench(), bench[count:])
                    for pokemon in picks:
                        self.assertIn(pokemon, ctx.discard_pile())
                    if count:
                        for card in attachments:
                            self.assertIn(card, ctx.discard_pile())
                    self.assertFalse(ctx.knockouts)
