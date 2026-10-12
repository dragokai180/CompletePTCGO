"""Ability-blocking text must respect target class, zone, and position."""

import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Ability
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import (
    ability_locked, attacks_blocked, out_of_play_ability_locked,
)
from spirit.tools.effect_smoke import P1, P2


class TextAbilityBlockerTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_board(self):
        rig, _ = self.rig('HGSS1.Pikachu_78')
        return rig

    def put(self, rig, path, owner=P1, zone='bench'):
        return self.add(rig, fixtures.definition(path), owner, zone)

    def make_active(self, rig, pokemon, owner=P1):
        rig.to_area(rig.board.active_pokemon(owner), owner, 'bench')
        rig.to_area(pokemon, owner, 'activePokemonArea')

    def test_power_of_alchemy_all_players_and_zones(self):
        rig = self.setup_board()
        muk = self.put(rig, 'SM1.AlolanMuk_58')
        for owner in (P1, P2):
            for zone in ('bench', 'hand', 'discard'):
                with self.subTest(owner=owner, zone=zone):
                    basic = self.put(rig, 'SV1.Klefki_96', owner, zone)
                    check = ability_locked if zone == 'bench' else out_of_play_ability_locked
                    self.assertTrue(check(rig.board, basic, Ability('Probe')))
                    stage_one = self.put(rig, 'SM1.AlolanMuk_58', owner, zone)
                    self.assertFalse(check(rig.board, stage_one, Ability('Probe')))
        self.assertFalse(ability_locked(rig.board, muk, Ability('Power of Alchemy')))

    def test_basic_v_and_break_blockers(self):
        cases = (
            ('SV2.Spiritomb_89', 'SWSH1.ZacianV_138', True),
            ('SV045.Spiritomb_158', 'SWSH1.ZacianV_138', True),
            ('SV2.Spiritomb_89', 'SV1.Miraidonex_81', False),
            ('Promo_XY.Giratina_184', 'XY9.GreninjaBREAK_41', True),
            ('Promo_XY.Giratina_184', 'SV1.Klefki_96', False),
        )
        for blocker, target, expected in cases:
            with self.subTest(blocker=blocker, target=target):
                rig = self.setup_board()
                self.put(rig, blocker)
                card = self.put(rig, target, P2)
                self.assertEqual(ability_locked(rig.board, card, Ability('Probe')),
                                 expected)

    def test_damage_and_bench_stage_restrictions(self):
        rig = self.setup_board()
        self.put(rig, 'SM12.Mimikyu_97')
        gx = self.put(rig, 'Promo_SM.GlaceonGX_147', P2)
        self.assertFalse(ability_locked(rig.board, gx, Ability('Probe')))
        gx.set_attribute(AttrID.HP, gx.get_attribute(AttrID.HP) - 10)
        self.assertTrue(ability_locked(rig.board, gx, Ability('Probe')))

        rig = self.setup_board()
        gastrodon = self.put(rig, 'SV08.Gastrodon_107')
        stage_two = self.put(rig, 'SM7.Slaking_115', P2)
        self.assertTrue(ability_locked(rig.board, stage_two, Ability('Probe')))
        self.make_active(rig, gastrodon)
        self.assertFalse(ability_locked(rig.board, stage_two, Ability('Probe')))

        rig = self.setup_board()
        self.put(rig, 'SM8.Wobbuffet_93')
        prism = self.put(rig, 'SM8.Ditto_154', P2)
        self.assertTrue(ability_locked(rig.board, prism, Ability('Probe')))
        self.assertTrue(attacks_blocked(rig.board, prism))
        self.assertFalse(ability_locked(rig.board,
                                        self.put(rig, 'SV1.Klefki_96', P2),
                                        Ability('Probe')))

    def test_sun_shade_needs_solrock_and_excludes_gx_ex(self):
        rig = self.setup_board()
        self.put(rig, 'SM7.Lunatone_61')
        target = self.put(rig, 'SV1.Klefki_96', P2)
        target.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        self.assertFalse(ability_locked(rig.board, target, Ability('Probe')))
        self.put(rig, 'SM7.Solrock_62')
        self.assertTrue(ability_locked(rig.board, target, Ability('Probe')))
        gx = self.put(rig, 'Promo_SM.GlaceonGX_147', P2)
        gx.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        self.assertFalse(ability_locked(rig.board, gx, Ability('Probe')))

    def test_active_opponent_locks_and_exceptions(self):
        rig = self.setup_board()
        ting = self.put(rig, 'SV2.TingLuex_127')
        target = self.put(rig, 'SV1.Klefki_96', P2)
        target.set_attribute(AttrID.HP, target.get_attribute(AttrID.HP) - 10)
        self.assertFalse(ability_locked(rig.board, target, Ability('Probe')))
        self.make_active(rig, ting)
        self.assertTrue(ability_locked(rig.board, target, Ability('Probe')))
        modern_ex = self.put(rig, 'SV1.Miraidonex_81', P2)
        modern_ex.set_attribute(AttrID.HP, modern_ex.get_attribute(AttrID.HP) - 10)
        self.assertFalse(ability_locked(rig.board, modern_ex, Ability('Probe')))

        rig = self.setup_board()
        slaking = self.put(rig, 'SM7.Slaking_115')
        target = self.put(rig, 'SV1.Klefki_96', P2)
        self.assertFalse(ability_locked(rig.board, target, Ability('Probe')))
        self.make_active(rig, slaking)
        self.assertTrue(ability_locked(rig.board, target, Ability('Probe')))
        opposing_slaking = self.put(rig, 'SM7.Slaking_115', P2)
        self.assertFalse(ability_locked(rig.board, opposing_slaking,
                                        fixtures.definition('SM7.Slaking_115').abilities[0]))
        self.assertFalse(ability_locked(rig.board,
                                        self.put(rig, 'SV1.Klefki_96', P1),
                                        Ability('Probe')))

        rig = self.setup_board()
        glaceon = self.put(rig, 'Promo_SM.GlaceonGX_147')
        gx = self.put(rig, 'Promo_SM.GlaceonGX_147', P2)
        basic = self.put(rig, 'SV1.Klefki_96', P2)
        self.assertFalse(ability_locked(rig.board, gx, Ability('Probe')))
        self.make_active(rig, glaceon)
        self.assertTrue(ability_locked(rig.board, gx, Ability('Probe')))
        self.assertFalse(ability_locked(rig.board, gx, Ability('Freezing Gaze')))
        self.assertFalse(ability_locked(rig.board, basic, Ability('Probe')))
        hand_gx = self.put(rig, 'Promo_SM.GlaceonGX_147', P2, 'hand')
        self.assertFalse(out_of_play_ability_locked(rig.board, hand_gx,
                                                     Ability('Freezing Gaze')))
        other_gx = self.put(rig, 'SM12.ArceusDialgaPalkiaGX_156', P2, 'hand')
        self.assertTrue(out_of_play_ability_locked(rig.board, other_gx,
                                                    Ability('Probe')))

    def test_midnight_fluttering_keeps_its_named_exception(self):
        rig = self.setup_board()
        mine = self.put(rig, 'SV05.FlutterMane_78')
        opposing = self.put(rig, 'SV05.FlutterMane_78', P2)
        self.make_active(rig, mine)
        self.make_active(rig, opposing, P2)
        self.assertFalse(ability_locked(rig.board, opposing,
                                        Ability('Midnight Fluttering')))
        self.assertTrue(ability_locked(rig.board, opposing,
                                       Ability('Probe')))

    async def test_gastro_acid_locks_defender_until_next_own_turn(self):
        for attacker in ('XY1.Arbok_48', 'SM10.Victreebel_15'):
            with self.subTest(attacker=attacker):
                rig = self.setup_board()
                source = self.put(rig, attacker)
                self.make_active(rig, source)
                attack = next(ability for ability in fixtures.definition(attacker).abilities
                              if ability.title == 'Gastro Acid')
                ctx = EffectContext(rig.session, P1, source, attack)
                defender = rig.board.active_pokemon(P2)
                ctx.deal_damage = AsyncMock()
                self.assertFalse(ability_locked(rig.board, defender,
                                                Ability('Probe')))
                await ctx.ability.effect(ctx)
                ctx.deal_damage.assert_awaited_once()
                self.assertTrue(ability_locked(rig.board, defender,
                                               Ability('Probe')))
                rig.to_area(defender, P2, 'bench')
                self.assertFalse(ability_locked(rig.board, defender,
                                                Ability('Probe')))


if __name__ == '__main__':
    unittest.main()
