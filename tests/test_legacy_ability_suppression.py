"""Modern Ability locks must not erase printed Poke-Powers or Poke-Bodies."""

import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.session.passives import TempPassive, ability_locked, active_passives
from spirit.tools.effect_smoke import P1, P2


class LegacyAbilitySuppressionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def targets(self, rig, owner=P1):
        power_def = fixtures.definition('HGSS2.Kingdra_85')
        body_def = fixtures.definition('HGSS1.Donphan_107')
        modern_def = fixtures.definition('XY6.Banette_31')
        power = self.add(rig, power_def, owner, 'bench')
        body = self.add(rig, body_def, owner, 'bench')
        modern = self.add(rig, modern_def, owner, 'bench')
        return (power, power_def.abilities[0],
                body, body_def.abilities[0],
                modern, modern_def.abilities[0])

    def assert_legacy_unlocked(self, rig, targets, modern_locked=True):
        power, power_ability, body, body_ability, modern, modern_ability = targets
        self.assertFalse(ability_locked(rig.board, power, power_ability))
        self.assertFalse(ability_locked(rig.board, body, body_ability))
        self.assertEqual(ability_locked(rig.board, modern, modern_ability),
                         modern_locked)
        self.assertIn((body_ability.passive, body), active_passives(rig.board))
        if modern_locked:
            self.assertNotIn((modern_ability.passive, modern),
                             active_passives(rig.board))

    async def test_every_garbotoxin_printing_preserves_legacy_powers_and_bodies(self):
        for printing in ('BW6.Garbodor_54', 'BW9.Garbodor_119',
                         'BW11.Garbodor_68', 'XY9.Garbodor_57'):
            with self.subTest(printing=printing):
                rig, _ = self.rig('HGSS1.Pikachu_78')
                targets = self.targets(rig)
                garbodor = self.add(rig, fixtures.definition(printing), P2, 'bench')
                tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P2, 'hand')
                rig.attach(tool, garbodor)
                self.assert_legacy_unlocked(rig, targets)

    async def test_hex_maniac_and_bide_barricade_preserve_legacy_types(self):
        rig, _ = self.rig('HGSS1.Pikachu_78')
        targets = self.targets(rig)
        rig.session.turn_state.abilities_disabled_through_turn = 99
        self.assert_legacy_unlocked(rig, targets)

        rig, _ = self.rig('HGSS1.Pikachu_78')
        targets = self.targets(rig)
        rig.to_area(rig.board.active_pokemon(P2), P2, 'bench')
        self.add(rig, fixtures.definition('XY4.Wobbuffet_36'), P2,
                 'activePokemonArea')
        self.assert_legacy_unlocked(rig, targets, modern_locked=False)
        eternatus_def = fixtures.definition('SWSH3.EternatusVMAX_117')
        eternatus = self.add(rig, eternatus_def, P1, 'bench')
        self.assertTrue(ability_locked(rig.board, eternatus,
                                       eternatus_def.abilities[0]))

    async def test_shadow_stitching_preserves_opponents_legacy_types(self):
        rig, _, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        targets = self.targets(rig, owner=P2)
        await ctx.ability.effect(ctx)
        self.assert_legacy_unlocked(rig, targets)

    async def test_psychic_lock_still_blocks_only_poke_powers(self):
        from spirit.game.card_effects.hgss_era import PsychicLock

        rig, _ = self.rig('HGSS1.Pikachu_78')
        power, power_ability, body, body_ability, _, _ = self.targets(rig)
        roserade_def = fixtures.definition('HGSS2.Roserade_23')
        roserade = self.add(rig, roserade_def, P1, 'bench')
        roserade_passive = roserade_def.abilities[0].passive
        self.assertIn((roserade_passive, roserade), active_passives(rig.board))
        player = rig.board.find_player_entity(P1)
        rig.board.temporary_passives.append(
            TempPassive(PsychicLock(P1), player.entity_id, 99, P1))
        self.assertTrue(ability_locked(rig.board, power, power_ability))
        self.assertFalse(ability_locked(rig.board, body, body_ability))
        self.assertNotIn((roserade_passive, roserade), active_passives(rig.board))

    async def test_basic_ability_locks_preserve_legacy_basic_powers_and_bodies(self):
        for blocker in ('silent_lab', 'klefki'):
            with self.subTest(blocker=blocker):
                rig, _ = self.rig('HGSS1.Pikachu_78')
                power_def = fixtures.definition('HGSS4.Unown_51')
                body_def = fixtures.definition('HGSS4.Yanma_84')
                modern_def = fixtures.definition('SV1.Miraidonex_81')
                power = self.add(rig, power_def, P1, 'bench')
                body = self.add(rig, body_def, P1, 'bench')
                modern = self.add(rig, modern_def, P1, 'bench')
                if blocker == 'silent_lab':
                    stadium = self.add(rig, fixtures.definition('XY5.SilentLab_140'),
                                       P2, 'hand')
                    stadium_area = rig.board.find_global_area('activeStadium')
                    rig.board.move_card(stadium.entity_id, stadium_area.entity_id)
                else:
                    rig.to_area(rig.board.active_pokemon(P2), P2, 'bench')
                    self.add(rig, fixtures.definition('SV1.Klefki_96'), P2,
                             'activePokemonArea')
                self.assertFalse(ability_locked(rig.board, power,
                                                power_def.abilities[0]))
                self.assertFalse(ability_locked(rig.board, body,
                                                body_def.abilities[0]))
                self.assertTrue(ability_locked(rig.board, modern,
                                               modern_def.abilities[0]))
                self.assertIn((body_def.abilities[0].passive, body),
                              active_passives(rig.board))
