"""Bonnie's scoped GX exception and selectable devolution depth."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _attack_entries
from spirit.game.session.passives import evolution_blocked
from spirit.tools.effect_smoke import P1,P2


class SmTurnExceptionsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass=classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig=fixtures.HgssRulesTests.rig
    add=fixtures.HgssRulesTests.add

    async def test_bonnie_only_reopens_zygarde_gx_this_turn_and_keeps_used_token(self):
        rig,e=self.rig('SM6.ZygardeGX_73')
        source=e['target']
        state=rig.session.turn_state
        state.turn_number=4
        state.gx_used.add(P1)
        attack=next(a for a in fixtures.definition('SM6.ZygardeGX_73').abilities if a.gx)
        for _ in range(4):
            energy=self.add(rig,CARD_DEFS_BY_GUID[self.energies[PokemonTypes.FIGHTING.value].lower()],P1,'hand')
            rig.attach(energy,source)
        def offered():
            return {x['selectableAction']['actionID'] for x in _attack_entries(rig.board,state,P1,rig.session.game_id)}
        self.assertNotIn(attack.ability_id,offered())
        bonnie=self.add(rig,fixtures.definition('SM6.Bonnie_103'),P1,'hand')
        stadium=self.add(rig,fixtures.definition('SM11.GiantHearth_197'),P1,'hand')
        rig.board.move_card(stadium.entity_id,rig.board.find_global_area('activeStadium').entity_id)
        ctx=EffectContext(rig.session,P1,bonnie,None)
        await fixtures.definition('SM6.Bonnie_103').effect(ctx)
        self.assertIn(stadium,ctx.discard_pile())
        self.assertIn(P1,state.gx_used)
        self.assertIn(attack.ability_id,offered())
        other=self.add(rig,fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'),P1,'bench')
        self.assertFalse(state.can_repeat_gx(P1,other))
        state.gx_locked_players.add(P1)
        self.assertNotIn(attack.ability_id,offered())
        state.gx_locked_players.clear()
        state.begin_turn(P2,rig.board)
        state.begin_turn(P1,rig.board)
        self.assertNotIn(attack.ability_id,offered())
        self.assertIn(P1,state.gx_used)

    async def test_gx_exception_applies_to_copy_but_not_a_different_attacker(self):
        rig,e=self.rig('SM6.ZygardeGX_73')
        state=rig.session.turn_state
        state.gx_used.add(P1)
        state.gx_repeat_names_this_turn[P1]={'zygarde-gx'}
        attack=next(a for a in fixtures.definition('SM6.ZygardeGX_73').abilities if a.gx)
        ctx=EffectContext(rig.session,P1,e['target'],None)
        ctx.deal_damage=AsyncMock(return_value=150)
        self.assertTrue(await ctx.use_attack(attack))
        other=self.add(rig,fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'),P1,'bench')
        otherctx=EffectContext(rig.session,P1,other,None)
        self.assertFalse(await otherctx.use_attack(attack))

    async def test_devolution_spray_z_selects_depth_keeps_stack_and_blocks_evolution(self):
        for depth in (1,2):
            rig,e=self.rig('SM10.DevolutionSprayZ_166','trainer')
            definition=fixtures.definition('SM10.DevolutionSprayZ_166')
            ctx=EffectContext(rig.session,P1,e['target'],None)
            top=self.add(rig,fixtures.definition('SM12.Empoleon_56'),P1,'bench')
            stage=self.add(rig,fixtures.definition('SM12.Prinplup_55'),P1,'hand')
            basic=self.add(rig,fixtures.definition('SM12.Piplup_54'),P1,'hand')
            rig.attach(stage,top)
            rig.attach(basic,top)
            tool=self.add(rig,fixtures.definition('SM3.WishfulBaton_128'),P1,'hand')
            rig.attach(tool,top)
            top.set_attribute(AttrID.HP,ctx.max_hp(top)-20)
            rig.session.turn_state.turn_number=4
            ctx.choose_pokemon=AsyncMock(return_value=top)
            ctx.choose=AsyncMock(return_value=depth-1)
            await definition.effect(ctx)
            remaining=stage if depth==1 else basic
            self.assertIn(remaining,ctx.my_bench())
            self.assertIn(top,ctx.deck())
            self.assertEqual(stage in ctx.deck(),depth==2)
            self.assertIs(tool.parent,remaining)
            self.assertEqual(remaining.get_attribute(AttrID.HP),ctx.max_hp(remaining)-20)
            self.assertTrue(evolution_blocked(rig.board,P1,remaining))
            self.assertFalse(evolution_blocked(rig.board,P1,ctx.my_active()))
            rig.session.turn_state.begin_turn(P2,rig.board)
            self.assertFalse(evolution_blocked(rig.board,P1,remaining))

    def test_protection_and_opponent_attack_locks_do_not_lock_the_users_attack(self):
        for path,title in (
            ('SM6.ZygardeGX_73','Verdict-GX'),
            ('SM6.Uxie_41','Memory Skip'),
            ('SM11.Bibarel_172','Amnesia'),
            ('SM12.Dusclops_84','Disable'),
            ('Promo_SM.JolteonGX_173','Swift Run-GX'),
        ):
            attack=next(a for a in fixtures.definition(path).abilities if a.title==title)
            self.assertFalse(attack.locks_next_turn)
        attack=next(a for a in fixtures.definition('SM12.SolgaleoLunalaGX_75').abilities if a.title=='Cosmic Burn')
        self.assertTrue(attack.locks_next_turn)
