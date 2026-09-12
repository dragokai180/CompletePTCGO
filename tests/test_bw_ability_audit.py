"""BW abilities: private searches, ownership, costs and ordering."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.tools.effect_smoke import P1,P2


class BwAbilityAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass=classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig=fixtures.HgssRulesTests.rig
    ctx=fixtures.HgssRulesTests.ctx
    add=fixtures.HgssRulesTests.add

    async def test_slippery_soles_switches_self_then_opponent_chooses(self):
        rig,e,ctx=self.ctx('BW4.Vanilluxe_33','Slippery Soles')
        calls=[]
        async def choose(pool,*a,**kw):
            calls.append(('choose',kw.get('player_id',P1)));return pool[0]
        async def switch(pid,target):
            calls.append(('switch',pid));return True
        ctx.choose_pokemon=AsyncMock(side_effect=choose);ctx.switch_active=AsyncMock(side_effect=switch)
        await ctx.ability.effect(ctx)
        self.assertEqual(calls,[('choose',P1),('switch',P1),('choose',P2),('switch',P2)])

    async def test_unrestricted_ability_search_must_find_without_reveal(self):
        for path,title in [('BW6.Roserade_15','Le Parfum'),('BW8.Manaphy_34','Final Wish')]:
            with self.subTest(title=title):
                rig,e,ctx=self.ctx(path,title)
                ctx.ask_yes_no=AsyncMock(return_value=True)
                ctx.ko_from_attack=True
                ctx.search_deck=AsyncMock(return_value=[ctx.deck()[0]])
                ctx.put_in_hand=AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'],1)
                self.assertFalse(ctx.put_in_hand.call_args.kwargs['reveal'])

    async def test_stellar_guidance_can_search_even_without_supporters(self):
        rig,e,ctx=self.ctx('BW10.JirachiEX_60','Stellar Guidance')
        from spirit.game.session.effects import is_supporter_card
        for card in list(ctx.deck()):
            if is_supporter_card(card):rig.to_area(card,P1,'discard')
        ctx.ask_yes_no=AsyncMock(return_value=True)
        ctx.search_deck=AsyncMock(return_value=[]);ctx.shuffle_deck=AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.search_deck.assert_awaited_once();ctx.shuffle_deck.assert_awaited_once()

    async def test_flare_navigate_places_counter_only_after_attachment(self):
        for found in (False,True):
            rig,e,ctx=self.ctx('BW9.Chandelure_16','Flare Navigate')
            energy=rig.pull_guid(P1,self.energies[PokemonTypes.FIRE.value]);target=ctx.my_bench()[-1]
            ctx.search_deck=AsyncMock(return_value=[energy] if found else [])
            ctx.choose_pokemon=AsyncMock(return_value=target)
            ctx.attach_energy=AsyncMock(return_value=True);ctx.deal_damage=AsyncMock(return_value=10)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.attach_energy.await_count,int(found))
            self.assertEqual(ctx.deal_damage.await_count,int(found))
            if found:
                self.assertEqual(ctx.deal_damage.call_args.args[0],10)
                self.assertIs(ctx.deal_damage.call_args.kwargs['target'],target)
                self.assertTrue(ctx.deal_damage.call_args.kwargs['as_counters'])

    async def test_scornful_storm_opponent_selects_discard(self):
        rig,e,ctx=self.ctx('DV.Salamence_8','Scornful Storm')
        excess=len(ctx.hand(P2))-4
        ctx.discard_from_hand=AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.discard_from_hand.call_args.args[0],excess)
        self.assertEqual(ctx.discard_from_hand.call_args.kwargs['player_id'],P2)

    async def test_forewarn_keeps_other_card_without_shuffle(self):
        rig,e,ctx=self.ctx('BW4.Musharna_59','Forewarn')
        top=ctx.deck_top(2)
        ctx.choose_cards=AsyncMock(return_value=[top[1]])
        ctx.shuffle_deck=AsyncMock();ctx.put_in_hand=AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_cards.call_args.args[0],top)
        ctx.put_in_hand.assert_awaited_once_with([top[1]],reveal=False)
        ctx.shuffle_deck.assert_not_awaited()
