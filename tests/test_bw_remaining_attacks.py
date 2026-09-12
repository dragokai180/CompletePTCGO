"""BW3 through BW11, Dragon Vault and promo semantic regression matrix."""
import unittest
from unittest.mock import AsyncMock, Mock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.tools.effect_smoke import P1, P2


class RemainingAttackTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_fortunate_draw_both_results_and_tie(self):
        for choices,winner,loser in [([0,0,0,2],P1,P2),([0,1],P2,P1)]:
            rig,e,ctx=self.ctx('BW11.Xatu_56','Fortunate Draw')
            ctx.choose=AsyncMock(side_effect=choices)
            ctx.draw_cards=AsyncMock();ctx.discard_cards=AsyncMock()
            expected=ctx.deck_top(3,loser)
            await ctx.ability.effect(ctx)
            ctx.draw_cards.assert_awaited_once_with(3,player_id=winner)
            ctx.discard_cards.assert_awaited_once_with(expected)
            self.assertEqual(ctx.choose.await_count,len(choices))

    async def test_signs_of_evolution_filters_family_and_types(self):
        rig,e,ctx=self.ctx('BW9.Eevee_90','Signs of Evolution')
        vap=self.add(rig,definition('BW9.Vaporeon_20'),P1,'deck')
        vap2=self.add(rig,definition('BW9.Vaporeon_20'),P1,'deck')
        selected=[]
        async def choose(pool,*args,**kwargs):
            if not selected:
                self.assertIn(vap,pool)
                self.assertTrue(all('Eevee' in str(p.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)) for p in pool))
                selected.append(vap);return [vap]
            self.assertNotIn(vap2,pool)
            return []
        ctx.choose_cards=AsyncMock(side_effect=choose)
        ctx.put_in_hand=AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.put_in_hand.assert_awaited_once_with([vap],reveal=True)

    async def test_optional_discards_do_not_apply_status_when_declined(self):
        for path,title in [('BW5.Volcarona_22','Burning Wind'),
                ('BW7.Flygon_99','Flying Beatdown'),('BW8.Ludicolo_31','Groovy Dance')]:
            with self.subTest(title=title):
                rig,e,ctx=self.ctx(path,title)
                ctx.ask_yes_no=AsyncMock(return_value=False)
                ctx.apply_special_condition=AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.apply_special_condition.assert_not_awaited()

    async def test_optional_discards_apply_status_when_paid(self):
        for path,title,expected in [('BW5.Volcarona_22','Burning Wind',1),
                ('BW7.Flygon_99','Flying Beatdown',2),('BW8.Ludicolo_31','Groovy Dance',1)]:
            with self.subTest(title=title):
                rig,e,ctx=self.ctx(path,title)
                before=len(ctx.attached_energies(ctx.attacker))
                ctx.ask_yes_no=AsyncMock(return_value=True)
                ctx.apply_special_condition=AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.apply_special_condition.assert_awaited_once()
                self.assertEqual(before-len(ctx.attached_energies(ctx.attacker)),expected)

    async def test_payback_discards_when_opponent_has_one_prize(self):
        rig,e,ctx=self.ctx('BW9.Cacturne_10','Payback')
        prizes=rig.board.find_player_area(P2,'prizePile')
        for card in list(prizes.children)[1:]:rig.to_area(card,P2,'hand')
        ctx.discard_energy_from=AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.discard_energy_from.assert_awaited_once()

    async def test_thunderous_noise_discards_with_plasma_energy(self):
        rig,e,ctx=self.ctx('BW9.ThundurusEX_38','Thunderous Noise')
        plasma=self.add(rig,definition('BW8.PlasmaEnergy_127'),P1,'hand')
        rig.attach(plasma,ctx.attacker)
        ctx.discard_energy_from=AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.discard_energy_from.assert_awaited_once()

    async def test_conditional_defender_discard(self):
        for path,title in [('BW9.Cacturne_10','Payback'),('BW9.ThundurusEX_38','Thunderous Noise')]:
            with self.subTest(title=title):
                rig,e,ctx=self.ctx(path,title)
                ctx.discard_energy_from=AsyncMock();ctx.discard_cards=AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.discard_energy_from.assert_not_awaited()
                ctx.discard_cards.assert_not_awaited()

    async def test_optional_energy_transfer_can_be_declined(self):
        rig,e,ctx=self.ctx('BW4.Hippowdon_66','Sand Bazooka')
        ctx.ask_yes_no=AsyncMock(return_value=False)
        ctx.choose_cards=AsyncMock(return_value=[])
        ctx.move_energy=AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.move_energy.assert_not_awaited()
        self.assertTrue(ctx.ask_yes_no.await_count or
                        ctx.choose_cards.call_args.kwargs.get('minimum') == 0)

    async def test_clear_search_requires_three_cards(self):
        rig,e,ctx=self.ctx('BW6.Milotic_28','Clear Search')
        ctx.search_deck=AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.search_deck.call_args.kwargs.get('minimum'),3)

    async def test_secondary_clauses_require_stadium(self):
        for path,title,method in [('BW4.Simisage_7','Stadium Drain','heal'),
                ('BW4.Simisear_16','Stadium Burn','apply_special_condition'),
                ('BW4.Simipour_29','Stadium Wave','apply_special_condition')]:
            with self.subTest(title=title):
                rig,e,ctx=self.ctx(path,title)
                callback=AsyncMock(); setattr(ctx,method,callback)
                await ctx.ability.effect(ctx)
                callback.assert_not_awaited()

    async def test_two_coin_status_requirements(self):
        for path,title,minimum in [('BW3.Vanilluxe_29','Double Freeze',1),
                                   ('BW5.Haxorus_89','Stunning Uppercut',2)]:
            for coins in ([False,False],[True,False],[True,True]):
                with self.subTest(title=title,coins=coins):
                    rig,e,ctx=self.ctx(path,title)
                    ctx.flip_coins=AsyncMock(return_value=coins)
                    ctx.apply_special_condition=AsyncMock()
                    await ctx.ability.effect(ctx)
                    self.assertEqual(ctx.apply_special_condition.await_count,int(sum(coins)>=minimum))

    async def test_both_active_condition_wording(self):
        for path,title in [('BW5.Slowpoke_23','Big Yawn'),('BW6.Bidoof_106','Bang Heads')]:
            with self.subTest(title=title):
                rig,e,ctx=self.ctx(path,title)
                ctx.apply_special_condition=AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual({c.args[0].entity_id for c in ctx.apply_special_condition.call_args_list},
                                 {ctx.attacker.entity_id,ctx.defender.entity_id})

    async def test_healing_conditions_and_multipliers(self):
        for path,title,coins,expected in [
            ('BW7.Azumarill_37','Deep Dive',[False,False],0),
            ('BW7.Azumarill_37','Deep Dive',[True,True],80),
            ('BW7.Lopunny_117','Healing Melody',[False],0),
            ('DV.Latias_9','Sky Heal',[],0),
            ('BW9.Muk_46','Poison Suction',[],0),
        ]:
            with self.subTest(title=title,coins=coins):
                rig,e,ctx=self.ctx(path,title)
                ctx.flip_coins=AsyncMock(return_value=coins)
                ctx.heal=AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual(sum(c.args[0] for c in ctx.heal.call_args_list),expected)

    async def test_energy_bloom_only_heals_energy_holders(self):
        rig,e,ctx=self.ctx('BW9.Sceptile_8','Energy Bloom')
        ctx.heal=AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual({c.args[1].entity_id for c in ctx.heal.call_args_list},
                         {p.entity_id for p in ctx.my_pokemon_in_play() if ctx.attached_energies(p)})

    async def test_swift_sting_needs_full_hp_for_conditions(self):
        rig,e,ctx=self.ctx('BW9.Beedrill_3','Swift Sting')
        ctx.attacker.set_attribute(AttrID.HP,ctx.max_hp(ctx.attacker)-10)
        ctx.apply_special_condition=AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.apply_special_condition.assert_not_awaited()

    async def test_switch_coin_gate_and_new_defending_wording(self):
        rig,e,ctx=self.ctx('BW7.Purrloin_90','Captivate')
        ctx.flip_coins=AsyncMock(return_value=[False])
        ctx.switch_active=AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.switch_active.assert_not_awaited()
        for path,title in [('BW5.Eelektross_47','Slurp Shakedown'),('BW9.Hydreigon_78','Tractorbeam')]:
            with self.subTest(title=title):
                rig,e,ctx=self.ctx(path,title)
                target=ctx.opponent_bench()[0]
                ctx.choose_pokemon=AsyncMock(return_value=target)
                ctx.deal_damage=AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                hits=[c for c in ctx.deal_damage.call_args_list if c.kwargs.get('target') is target]
                self.assertEqual(len(hits),1)

    async def test_optional_switch_can_be_declined(self):
        rig,e,ctx=self.ctx('BW5.KyogreEX_26','Smash Turn')
        ctx.ask_yes_no=AsyncMock(return_value=False)
        ctx.choose_pokemon=AsyncMock(return_value=None)
        await ctx.ability.effect(ctx)
        ctx.ask_yes_no.assert_awaited_once()
        ctx.choose_pokemon.assert_not_awaited()

    async def test_promo_condition_without_now(self):
        rig,e,ctx=self.ctx('PROMO_BW.Electrode_BW76','Electribeam')
        ctx.flip_coins=AsyncMock(return_value=[True])
        ctx.apply_special_condition=AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.apply_special_condition.assert_awaited_once()

    async def test_declared_coin_damage_variants(self):
        for path,title,coins,expected in [('BW4.Mienfoo_67','Triple Smash',[True,True,False],20),
                ('BW9.Vanilluxe_29','ChillMAX',[True,True,False],120),
                ('BW11.Audino_RC17','Relaxed Roll',None,60)]:
            with self.subTest(title=title):
                rig,e,ctx=self.ctx(path,title)
                ctx.flip_coins=AsyncMock(return_value=coins) if coins is not None else AsyncMock(side_effect=[[True],[True],[False]])
                if coins is None:
                    ctx.flip_until_tails=AsyncMock(return_value=2)
                ctx.deal_damage=AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args_list[0].args[0],expected)
