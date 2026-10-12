"""A public switch must reach the next chooser before their prompt opens."""

import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.card_effects.trainers import catcher_switch_both, escape_rope
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class SwitchSequenceVisibilityTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    ctx = fixtures.HgssRulesTests.ctx
    rig = fixtures.HgssRulesTests.rig

    async def test_single_bench_switches_without_picker(self):
        for path, own, opposing in (
                ('BW1.Switch_104', True, False),
                ('SWSH2.BosssOrders_154', False, True),
                ('SM3.Guzma_115', True, True)):
            with self.subTest(card=path):
                rig, entities = self.rig(path, 'trainer')
                ctx = EffectContext(rig.session, P1, entities['target'], None)
                for player_id, reduce in ((P1, own), (P2, opposing)):
                    if reduce:
                        rig.to_area(
                            rig.board.find_player_area(player_id, 'bench').children[-1],
                            player_id, 'discard',
                        )
                new_own = ctx.my_bench()[0] if own else None
                new_opposing = ctx.opponent_bench()[0] if opposing else None
                ctx.choose_cards = AsyncMock(
                    side_effect=AssertionError('one target must not open a picker'))
                ctx.session._wait_for_client_catchup = AsyncMock(
                    side_effect=AssertionError('no choice needs client catch-up'))

                await fixtures.definition(path).effect(ctx)

                ctx.choose_cards.assert_not_awaited()
                if own:
                    self.assertIs(rig.board.active_pokemon(P1), new_own)
                if opposing:
                    self.assertIs(rig.board.active_pokemon(P2), new_opposing)

    async def test_multiple_switch_targets_still_prompt(self):
        rig, entities = self.rig('BW1.Switch_104', 'trainer')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        chosen = ctx.my_bench()[-1]
        ctx.choose_cards = AsyncMock(return_value=[chosen])

        await fixtures.definition('BW1.Switch_104').effect(ctx)

        ctx.choose_cards.assert_awaited_once()
        self.assertIs(rig.board.active_pokemon(P1), chosen)

    async def test_optional_single_pokemon_choice_can_be_declined(self):
        _, _, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        ctx.choose_cards = AsyncMock(return_value=[])

        picked = await ctx.choose_pokemon(
            [ctx.my_bench()[0]], 'Choose a Pokémon', optional=True)

        self.assertIsNone(picked)
        ctx.choose_cards.assert_awaited_once()

    def record(self, ctx):
        events = []

        async def choose(pool, *args, **kwargs):
            events.append(('choose', kwargs.get('player_id', P1)))
            return pool[0]

        async def switch(player_id, target, **kwargs):
            events.append(('switch', player_id))
            return True

        async def flush():
            events.append(('flush', None))

        async def wait(player_id):
            events.append(('wait', player_id))

        ctx.choose_pokemon = AsyncMock(side_effect=choose)
        ctx.switch_active = AsyncMock(side_effect=switch)
        ctx.flush_choreography = AsyncMock(side_effect=flush)
        ctx.session._wait_for_client_catchup = AsyncMock(side_effect=wait)
        return events

    async def test_catcher_shows_opponent_switch_before_own_choice(self):
        _, _, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        events = self.record(ctx)
        await catcher_switch_both(ctx)
        self.assertEqual(events, [
            ('choose', P1), ('switch', P2), ('flush', None),
            ('wait', P1), ('choose', P1), ('switch', P1),
        ])

    async def test_escape_rope_shows_opponent_switch_before_own_choice(self):
        _, _, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        events = self.record(ctx)
        ctx._trainer_blocked = lambda _pokemon: False
        await escape_rope(ctx)
        self.assertEqual(events, [
            ('choose', P2), ('switch', P2), ('flush', None),
            ('wait', P1), ('choose', P1), ('switch', P1),
        ])

    async def test_bronzong_gyro_ball_shows_first_switch_before_second_choice(self):
        _, _, ctx = self.ctx('SWSH2.Bronzong_130', 'Gyro Ball')
        events = self.record(ctx)
        ctx.deal_damage = AsyncMock(return_value=70)
        await ctx.ability.effect(ctx)
        self.assertEqual(events, [
            ('choose', P1), ('switch', P1), ('flush', None),
            ('wait', P2), ('choose', P2), ('switch', P2),
        ])

    async def test_text_interpreter_shows_own_switch_before_opponent_choice(self):
        for path, title in (
            ('BW2.Ferrothorn_72', 'Gyro Ball'),
            ('BW8.Magnezone_46', 'Gyro Ball'),
            ('HGSS3.Forretress_13', 'Gyro Ball'),
            ('SM8.Hitmontop_113', 'Rapid Spin'),
        ):
            with self.subTest(path=path):
                _, _, ctx = self.ctx(path, title)
                events = self.record(ctx)
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertEqual(events, [
                    ('choose', P1), ('switch', P1), ('flush', None),
                    ('wait', P2), ('choose', P2), ('switch', P2),
                ])

    async def test_if_you_do_never_switches_opponent_when_own_switch_fails(self):
        for path, title in (
            ('SM8.Hitmontop_113', 'Rapid Spin'),
            ('SWSH2.Bronzong_130', 'Gyro Ball'),
        ):
            with self.subTest(path=path):
                _, _, ctx = self.ctx(path, title)
                ctx.choose_pokemon = AsyncMock(side_effect=lambda pool, *a, **k: pool[0])
                ctx.switch_active = AsyncMock(return_value=False)
                ctx.flush_choreography = AsyncMock()
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                ctx.choose_pokemon.assert_awaited_once()
                ctx.switch_active.assert_awaited_once()
                ctx.flush_choreography.assert_not_awaited()

    async def test_forretress_optional_switch_can_be_declined(self):
        _, _, ctx = self.ctx('HGSS3.Forretress_13', 'Gyro Ball')
        ctx.choose_pokemon = AsyncMock(return_value=None)
        ctx.switch_active = AsyncMock()
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.choose_pokemon.assert_awaited_once()
        self.assertTrue(ctx.choose_pokemon.call_args.kwargs['optional'])
        ctx.switch_active.assert_not_awaited()

    async def test_slippery_soles_shows_first_switch_before_second_choice(self):
        _, _, ctx = self.ctx('BW4.Vanilluxe_33', 'Slippery Soles')
        events = self.record(ctx)
        await ctx.ability.effect(ctx)
        self.assertEqual(events, [
            ('choose', P1), ('switch', P1), ('flush', None),
            ('wait', P2), ('choose', P2), ('switch', P2),
        ])

    async def test_witch_rondo_shows_first_switch_before_opponent_choice(self):
        _, _, ctx = self.ctx('SWSH6.Hatterene_73', 'Witch Rondo')
        events = self.record(ctx)
        await ctx.ability.effect(ctx)
        self.assertEqual(events, [
            ('choose', P1), ('switch', P1), ('flush', None),
            ('wait', P2), ('choose', P2), ('switch', P2),
        ])

    async def test_cross_switcher_shows_gust_before_own_choice(self):
        from spirit.game.scripts.cards.SWSH8.CrossSwitcher_230 import cross_switcher

        _, _, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        events = self.record(ctx)
        ctx.discard_cards = AsyncMock()
        with patch('spirit.game.scripts.cards.SWSH8.CrossSwitcher_230._second_copy',
                   return_value=object()):
            await cross_switcher(ctx)
        self.assertEqual(events, [
            ('choose', P1), ('switch', P2), ('flush', None),
            ('wait', P1), ('choose', P1), ('switch', P1),
        ])

    async def test_giovanni_shows_own_switch_before_gust_choice(self):
        from spirit.game.scripts.cards.SV10.TeamRocketsGiovanni_174 import team_rockets_giovanni

        _, _, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        events = self.record(ctx)
        with patch('spirit.game.scripts.cards.SV10.TeamRocketsGiovanni_174._is_team_rockets',
                   return_value=True):
            await team_rockets_giovanni(ctx)
        self.assertEqual(events, [
            ('choose', P1), ('switch', P1), ('flush', None),
            ('wait', P1), ('choose', P1), ('switch', P2),
        ])

    async def test_star_rondo_shows_own_switch_before_gust_choice(self):
        _, _, ctx = self.ctx('SWSH12.MawileVSTAR_71', 'Star Rondo')
        events = self.record(ctx)
        ctx.ask_yes_no = AsyncMock(return_value=True)
        await ctx.ability.effect(ctx)
        self.assertEqual(events, [
            ('switch', P1), ('flush', None), ('wait', P1),
            ('choose', P1), ('switch', P2),
        ])


if __name__ == '__main__':
    unittest.main()
