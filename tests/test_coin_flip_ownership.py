"""Coin flips resolve for the player named by the card, even on defense."""

import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.data_utils import Attack
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class CoinFlipOwnershipTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig

    def opposing_attack(self, rig, damage=20):
        return EffectContext(
            rig.session, P2, rig.board.active_pokemon(P2),
            Attack(title='Hit', cost={}, damage=damage),
        )

    async def test_defending_player_flips_damage_prevention_and_reduction(self):
        paths = (
            'SM10.WhimsicottGX_140',  # Fluffy Cotton
            'GUM.Greninja_9',         # Evasion Jutsu
            'BW3.Carracosta_26',     # Solid Rock
            'BW4.Cinccino_85',       # Smooth Coat
        )
        for path in paths:
            with self.subTest(path=path):
                rig, entities = self.rig(path)
                target = entities['target']
                ctx = self.opposing_attack(rig)
                with patch('spirit.game.session.effects.forced_coin_result',
                           side_effect=lambda board, pid: pid == P1), \
                        patch.object(rig.session, 'stat_add',
                                     wraps=rig.session.stat_add) as stats:
                    dealt = await ctx.deal_damage(20, target=target)

                self.assertEqual(dealt, 0)
                stats.assert_any_call(P1, 'headsflipped', 1)
                self.assertEqual(ctx.coin_results, [])
                flips = [msg for _, msg, _ in ctx._messages
                         if msg.get('name', '').endswith(
                             'MultipleCoinFlipWithContextEffect')]
                self.assertEqual(len(flips), 1)
                self.assertEqual(flips[0]['value']['source'], target.entity_id)

    async def test_defending_player_flips_guts_and_evanescent(self):
        rig, entities = self.rig('BW3.Cofagrigus_47')
        target = entities['target']
        ctx = self.opposing_attack(rig, 1000)
        with patch('spirit.game.session.effects.forced_coin_result',
                   side_effect=lambda board, pid: pid == P1):
            await ctx.deal_damage(1000, target=target)
        self.assertEqual(target.get_attribute(fixtures.AttrID.HP), 10)
        self.assertEqual(ctx.coin_results, [])

        rig, entities = self.rig('SV4.Froslassex_3')
        target = entities['target']
        ctx = self.opposing_attack(rig)
        ctx.attack_damage[target.entity_id] = (20, 250)
        ability = next(a for a in fixtures.definition('SV4.Froslassex_3').abilities
                       if a.title == 'Evanescent')
        with patch('spirit.game.session.effects.forced_coin_result',
                   side_effect=lambda board, pid: pid == P1):
            bonus = await ability.passive.extra_prizes_for_knockout(
                target, ctx, 2, target)
        self.assertEqual(bonus, -1)

    async def test_mental_trash_has_one_opponent_owned_flip(self):
        rig, entities = self.rig('XY1.Malamar_76')
        ability = next(a for a in fixtures.definition('XY1.Malamar_76').abilities
                       if a.title == 'Mental Trash')
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        ctx.flip_coins = AsyncMock(return_value=[True, False, False, True])
        ctx.discard_from_hand = AsyncMock(return_value=[])

        await ability.effect(ctx)

        ctx.flip_coins.assert_awaited_once_with(
            4, 'Mental Trash', source=ctx.defender, player_id=P2)
        ctx.discard_from_hand.assert_awaited_once_with(
            2, player_id=P2, prompt='Choose cards to discard')

    async def test_wonder_kiss_uses_the_togekiss_controllers_coin(self):
        rig, entities = self.rig('SV08.Togekiss_72')
        carrier = entities['target']
        victim = rig.board.active_pokemon(P2)
        ability = next(a for a in fixtures.definition('SV08.Togekiss_72').abilities
                       if a.title == 'Wonder Kiss')
        ctx = self.opposing_attack(rig)
        with patch('spirit.game.session.effects.forced_coin_result',
                   side_effect=lambda board, pid: pid == P1):
            bonus = await ability.passive.extra_prizes_for_knockout(
                victim, ctx, 1, carrier)

        self.assertEqual(bonus, 1)

    async def test_bench_manipulation_uses_opponents_coins(self):
        for path, damage in (
            ('HGSS4.Grumpig_23', 40),
            ('SV10.TeamRocketsHypno_80', 80),
        ):
            with self.subTest(path=path):
                rig, entities = self.rig(path)
                ability = next(a for a in fixtures.definition(path).abilities
                               if a.title == 'Bench Manipulation')
                ctx = EffectContext(rig.session, P1, entities['target'], ability)
                count = len(ctx.opponent_bench())
                ctx.flip_coins = AsyncMock(return_value=[False] * count)
                ctx.deal_damage = AsyncMock()

                await ability.effect(ctx)

                ctx.flip_coins.assert_awaited_once_with(
                    count, 'Bench Manipulation', source=ctx.defender,
                    player_id=P2)
                self.assertEqual(ctx.deal_damage.await_args.args[0],
                                 damage * count)


if __name__ == '__main__':
    unittest.main()
