"""TAG TEAM Supporter bonuses must pay before their printed main effect."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1, P2


class SmTagTeamSupportersTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_card(self,path):
        rig,e=self.rig(path,'trainer')
        ctx=EffectContext(rig.session,P1,e['target'],None)
        for c in list(ctx.hand()):
            if c is not ctx.source:rig.to_area(c,P1,'deck')
        return rig,ctx,fixtures.definition(path)

    async def test_mallow_lana_paid_bonus_heals_outgoing_not_incoming(self):
        for pays in (False,True):
            rig,ctx,definition=self.setup_card('SM12.MallowLana_198')
            outgoing=ctx.my_active()
            incoming=ctx.my_bench()[0]
            outgoing.set_attribute(AttrID.HP,ctx.max_hp(outgoing)-30)
            incoming.set_attribute(AttrID.HP,ctx.max_hp(incoming)-20)
            costs=[self.add(rig,self.filler,P1,'hand') for _ in range(2)]
            ctx.ask_yes_no=AsyncMock(return_value=pays)
            ctx.choose_cards=AsyncMock(return_value=costs)
            ctx.choose_pokemon=AsyncMock(return_value=incoming)
            self.assertTrue(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
            await definition.effect(ctx)
            self.assertIs(ctx.my_active(),incoming)
            self.assertEqual(outgoing.get_attribute(AttrID.HP),ctx.max_hp(outgoing)-(0 if pays else 30))
            self.assertEqual(incoming.get_attribute(AttrID.HP),ctx.max_hp(incoming)-20)
            for c in costs:self.assertIn(c,ctx.discard_pile() if pays else ctx.hand())

    async def test_mallow_lana_healthy_switch_is_legal_without_heal_cost(self):
        rig,ctx,definition=self.setup_card('SM12.MallowLana_198')
        for p in ctx.my_pokemon_in_play():p.set_attribute(AttrID.HP,ctx.max_hp(p))
        self.assertTrue(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
        ctx.ask_yes_no=AsyncMock()
        outgoing=ctx.my_active()
        await definition.effect(ctx)
        self.assertIn(outgoing,ctx.my_bench())
        ctx.ask_yes_no.assert_not_awaited()
        for p in list(ctx.my_bench()):rig.to_area(p,P1,'deck')
        self.assertFalse(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))

    async def test_guzma_hala_bonus_gives_one_separate_search_slot_per_category(self):
        for pays in (False,True):
            rig,ctx,definition=self.setup_card('SM12.GuzmaHala_193')
            costs=[self.add(rig,self.filler,P1,'hand') for _ in range(2)]
            stadium=self.add(rig,fixtures.definition('SM11.GiantHearth_197'),P1,'deck')
            tool=self.add(rig,fixtures.definition('SM3.WishfulBaton_128'),P1,'deck')
            energy=self.add(rig,fixtures.definition('SM1.RainbowEnergy_137'),P1,'deck')
            ctx.ask_yes_no=AsyncMock(return_value=pays)
            ctx.choose_cards=AsyncMock(return_value=costs)
            async def search(groups,**kwargs):
                for c in costs:self.assertIn(c,ctx.discard_pile() if pays else ctx.hand())
                self.assertEqual(len(groups),3 if pays else 1)
                self.assertTrue(groups[0][0](stadium))
                self.assertFalse(groups[0][0](tool))
                if pays:
                    self.assertTrue(groups[1][0](tool))
                    self.assertFalse(groups[1][0](energy))
                    self.assertTrue(groups[2][0](energy))
                return [[stadium],[tool],[energy]] if pays else [[stadium]]
            ctx.search_deck_groups=search
            ctx.reveal_cards=AsyncMock()
            ctx.put_in_hand=AsyncMock(wraps=ctx.put_in_hand)
            await definition.effect(ctx)
            self.assertIn(stadium,ctx.hand())
            self.assertEqual(tool in ctx.hand(),pays)
            self.assertEqual(energy in ctx.hand(),pays)
            self.assertEqual(ctx.put_in_hand.call_args.args[0],[stadium,tool,energy] if pays else [stadium])
            self.assertTrue(ctx.put_in_hand.call_args.kwargs['reveal'])

    async def test_guzma_hala_can_fail_private_search_without_changing_categories(self):
        rig,ctx,definition=self.setup_card('SM12.GuzmaHala_193')
        ctx.search_deck_groups=AsyncMock(return_value=[[]])
        ctx.shuffle_deck=AsyncMock()
        self.assertTrue(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
        await definition.effect(ctx)
        ctx.shuffle_deck.assert_awaited_once()

    async def test_bellelba_cost_precedes_mill_and_opponent_discards_bench_first(self):
        rig,ctx,definition=self.setup_card('SM12.BellelbaBrycenMan_186')
        costs=[self.add(rig,self.filler,P1,'hand') for _ in range(3)]
        for pid in (P1,P2):
            while len(rig.board.pokemon_in_play(pid))<5:self.add(rig,self.filler,pid,'bench')
        tops={pid:ctx.deck_top(3,pid) for pid in (P1,P2)}
        events=[]
        async def choose(pool,count,**kwargs):
            if costs[0] in pool:
                self.assertTrue(all(c in ctx.deck(pid) for pid in (P1,P2) for c in tops[pid]))
                events.append('cost')
                return costs
            self.assertTrue(all(c in ctx.discard_pile(pid) for pid in (P1,P2) for c in tops[pid]))
            events.append(kwargs['player_id'])
            return pool[:count]
        ctx.ask_yes_no=AsyncMock(return_value=True)
        ctx.choose_cards=choose
        await definition.effect(ctx)
        self.assertEqual(events,['cost',P2,P1])
        self.assertEqual(len(ctx.my_bench()),3)
        self.assertEqual(len(ctx.opponent_bench()),3)
        self.assertFalse(ctx.knockouts)

    async def test_bellelba_without_bonus_leaves_bench_and_empty_decks_allow_only_bonus(self):
        rig,ctx,definition=self.setup_card('SM12.BellelbaBrycenMan_186')
        for pid in (P1,P2):
            while len(rig.board.pokemon_in_play(pid))<5:self.add(rig,self.filler,pid,'bench')
        ctx.ask_yes_no=AsyncMock(return_value=False)
        await definition.effect(ctx)
        self.assertEqual(len(ctx.my_bench()),4)
        for pid in (P1,P2):
            for c in list(ctx.deck(pid)):rig.to_area(c,pid,'lostZone')
        self.assertFalse(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
        for _ in range(3):self.add(rig,self.filler,P1,'hand')
        self.assertTrue(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
