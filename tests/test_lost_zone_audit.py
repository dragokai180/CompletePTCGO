"""Lost Zone destinations, payments, coin branches, and counted resources."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.tools.effect_smoke import P1, P2


class LostZoneAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def energy(self, rig, pid=P1, zone='hand', kind=PokemonTypes.LIGHTNING):
        return self.add(rig, definition('BW1.' + kind.name.title() + 'Energy_' + {
            PokemonTypes.LIGHTNING: '108', PokemonTypes.FIRE: '106',
            PokemonTypes.WATER: '107'}[kind]), pid, zone)

    async def test_see_off_lost_zone_not_hand_and_allows_failed_search(self):
        for fail in (False, True):
            rig, e, ctx = self.ctx('HGSS4.Mew_97', 'See Off')
            chosen = self.add(rig, self.filler, P1, 'deck')
            ctx.search_deck = AsyncMock(return_value=[] if fail else [chosen])
            ctx.shuffle_deck = AsyncMock()
            await ctx.ability.effect(ctx)
            ctx.search_deck.assert_awaited_once()
            self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)
            self.assertTrue(ctx.search_deck.call_args.args[0](chosen))
            self.assertFalse(ctx.search_deck.call_args.args[0](self.energy(rig)))
            self.assertNotIn(chosen, ctx.hand())
            self.assertEqual(chosen in ctx.lost_zone(), not fail)
            ctx.shuffle_deck.assert_awaited_once()

    async def test_lost_crush_flips_and_can_select_benched_energy(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx('HGSS4.Banette_14', 'Lost Crush')
            target = ctx.opponent_bench()[0]
            chosen = self.energy(rig, P2)
            rig.attach(chosen, target)
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.choose_cards = AsyncMock(return_value=[chosen])
            await ctx.ability.effect(ctx)
            ctx.flip_coins.assert_awaited_once()
            self.assertEqual(chosen in ctx.lost_zone(P2), heads)
            if heads:
                self.assertIn(chosen, ctx.choose_cards.call_args.args[0])
            else:
                ctx.choose_cards.assert_not_awaited()

    async def test_tangrowth_heads_paralyzes_tails_removes_only_defenders_energy(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx('COL.Tangrowth_34', 'Plow Over')
            own = self.energy(rig)
            other = self.energy(rig, P2)
            rig.attach(own, ctx.attacker)
            rig.attach(other, ctx.defender)
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.choose_cards = AsyncMock(side_effect=lambda pool, n, **kw: pool[:n])
            ctx.apply_special_condition = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertIn(own, ctx.attached_energies(ctx.attacker))
            self.assertEqual(other in ctx.lost_zone(P2), not heads)
            if heads:
                ctx.apply_special_condition.assert_awaited_once_with(ctx.defender, SpecialConditions.PARALYZED)
            else:
                ctx.apply_special_condition.assert_not_awaited()

    async def test_lost_claw_random_hand_card_not_whole_hand(self):
        rig, e, ctx = self.ctx('COL.Zangoose_39', 'Lost Claw')
        hand = list(ctx.hand(P2))
        ctx.reveal_hand = AsyncMock()
        ctx.choose_cards = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.hand(P2)), len(hand) - 1)
        self.assertEqual(len(set(hand).intersection(ctx.lost_zone(P2))), 1)
        ctx.reveal_hand.assert_not_awaited()
        ctx.choose_cards.assert_not_awaited()

    async def test_vicious_claw_requires_pokemon_payment_before_damage(self):
        for has_pokemon in (False, True):
            rig, e, ctx = self.ctx('HGSS4.Absol_91', 'Vicious Claw')
            for c in list(ctx.hand()): rig.to_area(c, P1, 'deck')
            chosen = self.add(rig, self.filler, P1, 'hand') if has_pokemon else None
            self.energy(rig)
            ctx.choose_cards = AsyncMock(return_value=[chosen] if chosen else [])
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.await_count, int(has_pokemon))
            if has_pokemon: self.assertIn(chosen, ctx.lost_zone())

    async def test_lost_march_and_dimension_sphere_count_only_own_eligible_pokemon(self):
        for path, title, expected in [('COL.Lucario_14', 'Dimension Sphere', 90),
                ('SM8.Jumpluff_14', 'Lost March', 40),
                ('SM12.Cottonee_147', 'Lost March', 40)]:
            rig, e, ctx = self.ctx(path, title)
            for _ in range(2): self.add(rig, self.filler, P1, 'lostZone')
            self.add(rig, definition('SM9.TapuKoko_51'), P1, 'lostZone')
            self.add(rig, self.filler, P2, 'lostZone')
            self.energy(rig, zone='lostZone')
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            ctx.deal_damage.assert_awaited_once_with(expected)

    async def test_unseen_flash_payment_and_permission(self):
        for count in (0, 1, 2):
            rig, e, ctx = self.ctx('SM8.Ampharos_78', 'Unseen Flash')
            for c in list(ctx.hand()): rig.to_area(c, P1, 'deck')
            cards = [self.energy(rig) for _ in range(count)]
            self.energy(rig, kind=PokemonTypes.FIRE)
            self.assertEqual(ctx.ability.condition(rig.board, P1, ctx.source), count == 2)
            ctx.choose_cards = AsyncMock(return_value=cards)
            ctx.ask_yes_no = AsyncMock(return_value=True)
            ctx.apply_special_condition = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.apply_special_condition.await_count, int(count == 2))
            self.assertEqual(len(ctx.lost_zone()), count if count == 2 else 0)

    async def test_lost_boomerang_redirects_only_knocked_out_targets_and_attachments(self):
        rig, e, ctx = self.ctx('Promo_SM.AlolanMarowakGX_187', 'Lost Boomerang-GX')
        victim = ctx.defender
        survivor = ctx.opponent_bench()[0]
        victim.set_attribute(AttrID.HP, 40)
        survivor.set_attribute(AttrID.HP, 200)
        energy = self.energy(rig, P2)
        rig.attach(energy, victim)
        ctx.choose_cards = AsyncMock(return_value=[victim, survivor])
        await ctx.ability.effect(ctx)
        await rig.session.resolve_knockouts(ctx)
        self.assertIn(victim, ctx.lost_zone(P2))
        self.assertIn(energy, ctx.lost_zone(P2))
        self.assertIn(survivor, ctx.opponent_pokemon_in_play())
        self.assertEqual(survivor.get_attribute(AttrID.HP), 150)

    async def test_energy_value_payments_accept_one_double_energy(self):
        cases = [('SWSH11.GiratinaVSTAR_131', 'Lost Impact', P1),
                 ('SWSH11.GiratinaVSTAR_201', 'Lost Impact', P1),
                 ('SWSH11.GiratinaVSTAR_212', 'Lost Impact', P1),
                 ('SWSH11.DelphoxV_27', 'Magical Fire', P1),
                 ('SWSH11.DelphoxV_173', 'Magical Fire', P1),
                 ('SM8.Typhlosion_42', 'Lost Flame', P2)]
        for path, title, owner in cases:
            with self.subTest(path=path):
                rig, e, ctx = self.ctx(path, title)
                holder = ctx.attacker if owner == P1 else ctx.defender
                for p in rig.board.pokemon_in_play(owner):
                    for c in list(ctx.attached_energies(p)): rig.to_area(c, owner, 'discard')
                double = self.add(rig, definition('HGSS1.DoubleColorlessEnergy_103'), owner, 'hand')
                basic = self.energy(rig, owner)
                rig.attach(double, holder)
                rig.attach(basic, holder)
                rig.session.prompt_energy_unit_picker = AsyncMock(return_value=[double.entity_id])
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertIn(double, ctx.lost_zone(owner))
                self.assertIn(basic, ctx.attached_energies(holder))
                rig.session.prompt_energy_unit_picker.assert_awaited_once()

    async def test_lost_burn_counts_cards_not_double_energy_value(self):
        rig, e, ctx = self.ctx('HGSS4.Magnezone_96', 'Lost Burn')
        double = self.add(rig, definition('HGSS1.DoubleColorlessEnergy_103'), P1, 'hand')
        rig.attach(double, ctx.attacker)
        ctx.choose_cards = AsyncMock(return_value=[double])
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(50)
        self.assertIn(double, ctx.lost_zone())

    async def test_energy_removal_respects_protection(self):
        rig, e, ctx = self.ctx('HGSS4.Banette_14', 'Lost Crush')
        protected = self.add(rig, definition('ME2.Empoleonex_70'), P2, 'bench')
        energy = self.energy(rig, P2)
        rig.attach(energy, protected)
        ctx.flip_coins = AsyncMock(return_value=[True])
        ctx.choose_cards = AsyncMock(return_value=[energy])
        await ctx.ability.effect(ctx)
        self.assertIn(energy, ctx.attached_energies(protected))
        self.assertNotIn(energy, ctx.lost_zone(P2))

    async def test_lost_boomerang_protection_and_no_later_attack_leak(self):
        from spirit.game.card_effects.lost_zone import _LostAttackKnockouts
        from spirit.game.session.effects import EffectContext
        from spirit.game.data_utils import Attack
        rig, e, ctx = self.ctx('Promo_SM.AlolanMarowakGX_187', 'Lost Boomerang-GX')
        protected = self.add(rig, definition('ME2.Empoleonex_70'), P2, 'bench')
        other = ctx.defender
        for p in (protected, other): p.set_attribute(AttrID.HP, 40)
        ctx.choose_cards = AsyncMock(return_value=[protected, other])
        await ctx.ability.effect(ctx)
        replacement = _LostAttackKnockouts(ctx)
        later = EffectContext(rig.session, P1, ctx.attacker, Attack(title='Later', damage=100))
        later.attack_damage[other.entity_id] = 100
        self.assertIsNone(replacement.knockout_destination_for(other, later, ctx.attacker))
        await rig.session.resolve_knockouts(ctx)
        self.assertIn(protected, ctx.discard_pile(P2))
        self.assertIn(other, ctx.lost_zone(P2))

    async def test_unseen_flash_can_be_declined(self):
        rig, e, ctx = self.ctx('SM8.Ampharos_78', 'Unseen Flash')
        for _ in range(2): self.energy(rig)
        ctx.ask_yes_no = AsyncMock(return_value=False)
        ctx.choose_cards = AsyncMock()
        ctx.apply_special_condition = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.choose_cards.assert_not_awaited()
        ctx.apply_special_condition.assert_not_awaited()
        self.assertFalse(ctx.lost_zone())

    async def test_self_energy_card_moves_do_not_touch_opponent(self):
        for path, title, count in [('COL.Snorlax_33', 'Clomp Clomp Clobber', 1),
                                   ('COL.Pachirisu_18', 'Shocking Bolt', None)]:
            rig, e, ctx = self.ctx(path, title)
            own = list(ctx.attached_energies(ctx.attacker))
            opposing = list(ctx.attached_energies(ctx.defender))
            ctx.choose_cards = AsyncMock(side_effect=lambda pool, n, **kw: pool[:n])
            await ctx.ability.effect(ctx)
            self.assertEqual(len(ctx.lost_zone()), count or len(own))
            self.assertTrue(all(c in ctx.attached_energies(ctx.defender) for c in opposing))

    async def test_comfey_and_abyss_seeking_split_top_cards_without_revealing_hand(self):
        for path, title, viewed, keep in [('SWSH11.Comfey_79', 'Flower Selecting', 2, 1),
                ('SWSH11.GiratinaV_130', 'Abyss Seeking', 4, 2)]:
            rig, e, ctx = self.ctx(path, title)
            top = ctx.deck_top(viewed)
            ctx.choose_cards = AsyncMock(return_value=top[:keep])
            await ctx.ability.effect(ctx)
            self.assertTrue(all(c in ctx.hand() for c in top[:keep]))
            self.assertTrue(all(c in ctx.lost_zone() for c in top[keep:]))

    async def test_lost_impact_still_damages_when_copied_without_energy(self):
        rig, e, ctx = self.ctx('SWSH11.GiratinaVSTAR_131', 'Lost Impact')
        for p in ctx.my_pokemon_in_play():
            for c in list(ctx.attached_energies(p)): rig.to_area(c, P1, 'discard')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once()
        self.assertFalse(ctx.lost_zone())

    async def test_hurl_into_darkness_reveals_hand_only_once(self):
        rig, e, ctx = self.ctx('HGSS4.Gengar_94', 'Hurl into Darkness')
        chosen = self.add(rig, self.filler, P2, 'hand')
        ctx.reveal_hand = AsyncMock(return_value=list(ctx.hand(P2)))
        ctx.choose_cards = AsyncMock(return_value=[chosen])
        await ctx.ability.effect(ctx)
        ctx.reveal_hand.assert_awaited_once_with(P2, P1)
        self.assertIn(chosen, ctx.lost_zone(P2))
