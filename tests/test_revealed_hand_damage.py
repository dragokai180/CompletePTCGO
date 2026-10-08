"""Hand-reveal attacks count the printed category before dealing damage."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import def_for
from spirit.tools.effect_smoke import P2


class RevealedHandDamageTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def fill_opponent_hand(self, rig, ctx):
        for card in list(ctx.hand(P2)):
            rig.to_area(card, P2, 'deck')
        paths = (
            'SV1.NestBall_181', 'SM5.Volkner_135',
            'SV1.Mesagoza_178', 'BW9.FloatStone_99', 'BW1.Snivy_1',
        )
        cards = [self.add(rig, fixtures.definition(path), P2, 'hand')
                 for path in paths]
        cards.extend(self.add(
            rig, def_for(self.energies[energy_type.value]), P2, 'hand')
            for energy_type in (PokemonTypes.FIRE, PokemonTypes.WATER))
        return cards

    async def test_shared_attacks_count_revealed_trainers_and_energies(self):
        cases = (
            ('SV1.Banetteex_88', 'Poltergeist', 240),
            ('SM2.Trevenant_7', 'Poltergeist', 120),
            ('SM9.GengarMimikyuGX_53', 'Poltergeist', 200),
            ('SV035.Gengar_94', 'Poltergeist', 200),
            ('RSV10PT5.Whimsicottex_5', 'Wondrous Cotton', 200),
            ('BW8.Rotom_49', 'Poltergeist', 80),
            ('Promo_XY.NoctowlBREAK_136', 'Night Scan', 180),
            ('ME2PT5.Beautifly_13', 'Energy Straw', 160),
            ('Promo_XY.DelphoxEX_19', 'Wonder Flare', 160),
            ('Promo_SM.ZygardeGX_122', 'Liberation-GX', 240),
            ('SM8.Xatu_88', 'Energy Gaze', 90),
            ('Promo_SM.Gumshoos_97', 'Identify', 100),
            ('SWSH1.Polteageist_90', 'Poltergeist', 200),
            ('SWSH8.ChandelureV_39', 'Poltergeist', 160),
            ('SWSH8.ChandelureVMAX_40', 'Max Poltergeist', 280),
            ('SWSH8.Simipour_69', 'Circus Soaking', 60),
        )
        for path, title, expected in cases:
            with self.subTest(attack=path):
                rig, _, ctx = self.ctx(path, title)
                self.fill_opponent_hand(rig, ctx)
                rig.session.prompt_view_cards = AsyncMock()
                ctx.deal_damage = AsyncMock(return_value=0)

                await ctx.ability.effect(ctx)

                self.assertEqual(ctx.deal_damage.await_args.args[0], expected)
                rig.session.prompt_view_cards.assert_awaited_once()

    async def test_poltergeist_does_zero_with_no_trainers(self):
        rig, _, ctx = self.ctx('SV1.Banetteex_88', 'Poltergeist')
        for card in list(ctx.hand(P2)):
            rig.to_area(card, P2, 'deck')
        self.add(rig, fixtures.definition('BW1.Snivy_1'), P2, 'hand')
        rig.session.prompt_view_cards = AsyncMock()
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        self.assertEqual(ctx.deal_damage.await_args.args[0], 0)

    async def test_reveal_happens_before_damage(self):
        rig, _, ctx = self.ctx('SV1.Banetteex_88', 'Poltergeist')
        self.fill_opponent_hand(rig, ctx)
        events = []
        rig.session.prompt_view_cards = AsyncMock(
            side_effect=lambda *args, **kwargs: events.append('reveal'))
        ctx.deal_damage = AsyncMock(
            side_effect=lambda *args, **kwargs: events.append('damage'))

        await ctx.ability.effect(ctx)

        self.assertEqual(events, ['reveal', 'damage'])

    async def test_high_flight_counts_items_in_both_revealed_hands(self):
        rig, _, ctx = self.ctx('XY8.Noctowl_120', 'High Flight')
        for player_id in (ctx.player_id, P2):
            for card in list(ctx.hand(player_id)):
                rig.to_area(card, player_id, 'deck')
            self.add(rig, fixtures.definition('SV1.NestBall_181'),
                     player_id, 'hand')
        rig.session.prompt_view_cards = AsyncMock()
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        self.assertEqual(ctx.deal_damage.await_args.args[0], 40)
        self.assertEqual(rig.session.prompt_view_cards.await_count, 2)

    async def test_milk_cannon_counts_only_chosen_cards(self):
        rig, _, ctx = self.ctx('SM8.Miltank_158', 'Milk Cannon')
        milks = [self.add(rig, fixtures.definition('SM8.MoomooMilk_185'),
                          ctx.player_id, 'hand') for _ in range(2)]
        ctx.choose_cards = AsyncMock(return_value=milks)
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        self.assertEqual(ctx.deal_damage.await_args.args[0], 120)


if __name__ == '__main__':
    unittest.main()
