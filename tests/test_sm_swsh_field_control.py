"""Control/attachment scenarios for the remaining conditional SM/SWSH families."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID,PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1,P2


class SmSwshFieldControlTests(unittest.IsolatedAsyncioTestCase):
    setUpClass=classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig=fixtures.HgssRulesTests.rig
    add=fixtures.HgssRulesTests.add

    def setup_card(self,path):
        rig,e=self.rig(path,'trainer')
        return rig,EffectContext(rig.session,P1,e['target'],None),fixtures.definition(path)

    def legal(self,rig,ctx,definition):
        return trainer_condition_met(definition.condition,rig.board,P1,ctx.source)

    def energy(self,rig,kind=PokemonTypes.METAL,zone='hand',pid=P1):
        return self.add(rig,CARD_DEFS_BY_GUID[self.energies[kind.value].lower()],pid,zone)

    async def test_counter_catcher_and_surges_strategy_prize_gate(self):
        for path in ('SM4.CounterCatcher_91','SM10.LtSurgesStrategy_178'):
            rig,ctx,definition=self.setup_card(path)
            self.assertFalse(self.legal(rig,ctx,definition))
            prize=rig.board.find_player_area(P2,'prizePile').children[0]
            rig.to_area(prize,P2,'hand')
            self.assertTrue(self.legal(rig,ctx,definition))
            target=ctx.opponent_bench()[0]
            ctx.choose_pokemon=AsyncMock(return_value=target)
            await definition.effect(ctx)
            if 'Catcher' in path:self.assertIs(ctx.opponent_active(),target)
            else:
                self.assertEqual(rig.session.turn_state.supporter_limit_this_turn,3)
                rig.session.turn_state.begin_turn(P2,rig.board)
                self.assertEqual(rig.session.turn_state.supporter_limit_this_turn,1)

    async def test_rescue_stretcher_both_modes_and_partial_discard(self):
        for count,mode in ((1,0),(2,1),(4,1)):
            rig,ctx,definition=self.setup_card('SM2.RescueStretcher_130')
            for c in list(ctx.discard_pile()):rig.to_area(c,P1,'deck')
            cards=[self.add(rig,self.filler,P1,'discard') for _ in range(count)]
            wrong=self.energy(rig,zone='discard')
            ctx.choose=AsyncMock(return_value=mode)
            await definition.effect(ctx)
            destination=ctx.hand() if mode==0 else ctx.deck()
            self.assertEqual(sum(c in destination for c in cards),1 if mode==0 else min(3,count))
            self.assertIn(wrong,ctx.discard_pile())

    async def test_switch_raft_heals_only_outgoing_water(self):
        rig,ctx,definition=self.setup_card('DM.SwitchRaft_62')
        outgoing=ctx.my_active()
        incoming=ctx.my_bench()[0]
        outgoing.set_attribute(AttrID.POKEMON_TYPES,[PokemonTypes.FIRE.value])
        self.assertFalse(self.legal(rig,ctx,definition))
        outgoing.set_attribute(AttrID.POKEMON_TYPES,[PokemonTypes.WATER.value])
        outgoing.set_attribute(AttrID.HP,ctx.max_hp(outgoing)-40)
        incoming.set_attribute(AttrID.HP,ctx.max_hp(incoming)-20)
        self.assertTrue(self.legal(rig,ctx,definition))
        ctx.choose_pokemon=AsyncMock(return_value=incoming)
        await definition.effect(ctx)
        self.assertIs(ctx.my_active(),incoming)
        self.assertEqual(outgoing.get_attribute(AttrID.HP),ctx.max_hp(outgoing)-10)
        self.assertEqual(incoming.get_attribute(AttrID.HP),ctx.max_hp(incoming)-20)

    async def test_melony_and_metal_saucer_attach_exactly_one_to_allowed_target(self):
        for path,kind,target_path in (
            ('SWSH6.Melony_146',PokemonTypes.WATER,'SWSH12.HisuianArcanineV_90'),
            ('SWSH1.MetalSaucer_170',PokemonTypes.METAL,'CZ.ZamazentaVSTAR_99')):
            rig,ctx,definition=self.setup_card(path)
            for c in list(ctx.discard_pile()):rig.to_area(c,P1,'deck')
            target=self.add(rig,fixtures.definition(target_path),P1,'bench')
            energies=[self.energy(rig,kind,'discard') for _ in range(2)]
            wrong=self.energy(rig,PokemonTypes.FIRE,'discard')
            ctx.choose_cards=AsyncMock(return_value=[energies[1]])
            ctx.choose_pokemon=AsyncMock(return_value=target)
            ctx.draw_cards=AsyncMock()
            self.assertTrue(self.legal(rig,ctx,definition))
            await definition.effect(ctx)
            self.assertIs(energies[1].parent,target)
            self.assertIn(energies[0],ctx.discard_pile())
            self.assertIn(wrong,ctx.discard_pile())
            self.assertEqual(ctx.choose_cards.call_args.args[1],1)
            self.assertNotIn(wrong,ctx.choose_cards.call_args.args[0])
            if 'Melony' in path:ctx.draw_cards.assert_awaited_once_with(3)

    async def test_faba_can_remove_opposing_tool_or_special_energy_or_stadium(self):
        for kind in ('tool','energy','stadium'):
            rig,ctx,definition=self.setup_card('SM8.Faba_173')
            if kind=='tool':
                target=self.add(rig,fixtures.definition('SM3.WishfulBaton_128'),P2,'hand')
                rig.attach(target,ctx.opponent_active())
            elif kind=='energy':
                target=self.add(rig,fixtures.definition('SM1.RainbowEnergy_137'),P2,'hand')
                rig.attach(target,ctx.opponent_active())
            else:
                target=self.add(rig,fixtures.definition('SM11.GiantHearth_197'),P2,'hand')
                rig.board.move_card(target.entity_id,rig.board.find_global_area('activeStadium').entity_id)
                target.owning_player_id=P2  # Real Stadium placement preserves its owner.
            self.assertTrue(self.legal(rig,ctx,definition))
            ctx.choose_cards=AsyncMock(return_value=[target])
            await definition.effect(ctx)
            self.assertIn(target,rig.board.find_player_area(P2,'lostZone').children)

    async def test_tool_scrapper_and_field_blower_limit_two_from_either_side(self):
        # Both effects are explicitly allowed to target either player's Tools.
        for path in ('SWSH2.ToolScrapper_168','SM2.FieldBlower_125'):
            rig,ctx,definition=self.setup_card(path)
            tools=[]
            for pid in (P1,P2):
                tool=self.add(rig,fixtures.definition('SM3.WishfulBaton_128'),pid,'hand')
                rig.attach(tool,rig.board.active_pokemon(pid))
                tools.append(tool)
            ctx.choose_cards=AsyncMock(return_value=tools)
            self.assertTrue(self.legal(rig,ctx,definition))
            await definition.effect(ctx)
            self.assertEqual(ctx.choose_cards.call_args.args[1],2)
            for tool,pid in zip(tools,(P1,P2)):self.assertIn(tool,ctx.discard_pile(pid))

    async def test_magma_basin_attaches_before_damage_and_only_to_benched_fire(self):
        rig,ctx,definition=self.setup_card('SWSH9.MagmaBasin_144')
        ability=definition.ability
        target=self.add(rig,fixtures.definition('SM12.Flareon_25'),P1,'bench')
        energy=self.energy(rig,PokemonTypes.FIRE,'discard')
        ctx.choose_cards=AsyncMock(return_value=[energy])
        ctx.choose_pokemon=AsyncMock(return_value=target)
        self.assertTrue(ability.condition(rig.board,P1,ctx.source))
        before=target.get_attribute(AttrID.HP)
        await ability.effect(ctx)
        self.assertIs(energy.parent,target)
        self.assertEqual(target.get_attribute(AttrID.HP),before-20)
        self.assertNotIn(ctx.my_active(),ctx.choose_pokemon.call_args.args[0])

    async def test_crystal_cave_heals_only_friendly_metal_dragon(self):
        rig,ctx,definition=self.setup_card('SWSH7.CrystalCave_144')
        ability=definition.ability
        targets=[self.add(rig,fixtures.definition(path),pid,'bench') for path,pid in (
            ('CZ.ZamazentaVSTAR_99',P1),('SM12.ArceusDialgaPalkiaGX_156',P1),
            ('SM12.ArceusDialgaPalkiaGX_156',P2))]
        for p in targets:p.set_attribute(AttrID.HP,ctx.max_hp(p)-50)
        self.assertTrue(ability.condition(rig.board,P1,ctx.source))
        await ability.effect(ctx)
        for p in targets:self.assertEqual(p.get_attribute(AttrID.HP),ctx.max_hp(p)-(20 if p.owning_player_id==P1 else 50))

    async def test_rogue_fangs_counts_only_single_strike_pokemon(self):
        rig,e=self.rig('SWSH6.Lycanroc_87')
        attack=fixtures.definition('SWSH6.Lycanroc_87').abilities[0]
        ctx=EffectContext(rig.session,P1,e['target'],attack)
        for c in list(ctx.discard_pile()):rig.to_area(c,P1,'deck')
        self.add(rig,fixtures.definition('SWSH5.Houndoom_96'),P1,'discard')
        self.add(rig,fixtures.definition('SWSH5.SingleStrikeEnergy_141'),P1,'discard')
        self.add(rig,fixtures.definition('SWSH5.UrnofVitality_139'),P1,'discard')
        ctx.deal_damage=AsyncMock(return_value=90)
        await attack.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0],90)
