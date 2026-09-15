"""Remaining subtype, recovery and side-wide temporary Trainer rules."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.game.session.passives import compute_damage
from spirit.tools.effect_smoke import P1,P2


class SmSwshTrainerScopeTests(unittest.IsolatedAsyncioTestCase):
    setUpClass=classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig=fixtures.HgssRulesTests.rig
    add=fixtures.HgssRulesTests.add

    def setup_card(self,path):
        rig,e=self.rig(path,'trainer')
        ctx=EffectContext(rig.session,P1,e['target'],None)
        for c in list(ctx.discard_pile()):rig.to_area(c,P1,'deck')
        return rig,ctx,fixtures.definition(path)

    def energy(self,rig,kind=PokemonTypes.METAL,zone='hand'):
        return self.add(rig,CARD_DEFS_BY_GUID[self.energies[kind.value].lower()],P1,zone)

    def legal(self,rig,ctx,definition):
        return trainer_condition_met(definition.condition,rig.board,P1,ctx.source)

    async def test_fantina_and_shield_star_reduce_once_survive_departures_and_expire(self):
        for path,amount in (('SWSH11.Fantina_157',120),('SWSH11.Fantina_191',120),
                            ('SWSH11.Fantina_206',120),('CZ.ZamazentaVSTAR_99',100)):
            rig,e=self.rig(path,'trainer' if 'Fantina' in path else 'ability')
            definition=fixtures.definition(path)
            ability=None if 'Fantina' in path else definition.abilities[0]
            ctx=EffectContext(rig.session,P1,e['target'],ability)
            enemy=self.add(rig,fixtures.definition('SWSH12.HisuianArcanineV_90'),P2,'bench')
            rig.session.turn_state.turn_number=4
            await (definition.effect(ctx) if ability is None else ability.effect(ctx))
            # Leave all old carriers, then introduce a new Pokemon.
            for p in list(ctx.my_pokemon_in_play()):rig.to_area(p,P1,'discard')
            fresh=self.add(rig,self.filler,P1,'bench')
            rig.session.turn_state.begin_turn(P2,rig.board)
            def damage():
                return compute_damage(rig.board,enemy,fresh,300,
                    ignore_weakness=True,ignore_resistance=True).amount
            self.assertEqual(damage(),300-amount)
            if 'Fantina' in path:
                normal=ctx.opponent_active()
                self.assertEqual(compute_damage(rig.board,normal,fresh,300,
                    ignore_weakness=True,ignore_resistance=True).amount,300)
            rig.session.turn_state.begin_turn(P1,rig.board)
            self.assertEqual(damage(),300)

    async def test_urn_only_single_strike_energy_not_pokemon_or_trainers(self):
        for path in ('SWSH5.UrnofVitality_139','SWSH6.UrnofVitality_229'):
            rig,ctx,definition=self.setup_card(path)
            pokemon=self.add(rig,fixtures.definition('SWSH5.Houndoom_96'),P1,'discard')
            trainer=self.add(rig,definition,P1,'discard')
            self.assertFalse(self.legal(rig,ctx,definition))
            valid=self.add(rig,fixtures.definition('SWSH5.SingleStrikeEnergy_141'),P1,'discard')
            self.assertTrue(self.legal(rig,ctx,definition))
            await definition.effect(ctx)
            self.assertIn(valid,ctx.deck())
            self.assertIn(pokemon,ctx.discard_pile())
            self.assertIn(trainer,ctx.discard_pile())

    async def test_siebold_requires_damaged_rapid_strike_and_heals_at_most_two(self):
        for path in ('SWSH6.Siebold_153','SWSH6.Siebold_198','SWSH6.Siebold_221'):
            rig,ctx,definition=self.setup_card(path)
            rapid=[self.add(rig,fixtures.definition('SWSH6.ZeraoraV_53'),P1,'bench') for _ in range(3)]
            self.assertFalse(self.legal(rig,ctx,definition))
            for p in rapid[:2]:p.set_attribute(AttrID.HP,ctx.max_hp(p)-100)
            self.assertTrue(self.legal(rig,ctx,definition))
            ctx.choose_cards=AsyncMock(return_value=rapid[:2])
            await definition.effect(ctx)
            self.assertEqual(ctx.choose_cards.call_args.args[0],rapid[:2])
            self.assertEqual(ctx.choose_cards.call_args.args[1],2)
            for p in rapid[:2]:self.assertEqual(p.get_attribute(AttrID.HP),ctx.max_hp(p)-40)

    async def test_molayne_discards_metal_but_recovers_exactly_one_trainer(self):
        rig,ctx,definition=self.setup_card('SM10.Molayne_181')
        for c in list(ctx.hand()):
            if c is not ctx.source:rig.to_area(c,P1,'deck')
        costs=[self.energy(rig) for _ in range(2)]
        self.assertFalse(self.legal(rig,ctx,definition))
        trainer=self.add(rig,self.item,P1,'discard')
        self.assertTrue(self.legal(rig,ctx,definition))
        await definition.effect(ctx)
        self.assertIn(trainer,ctx.deck())
        self.assertTrue(all(c in ctx.discard_pile() for c in costs))

    async def test_sky_seal_stone_awards_extra_only_for_basic_v_attack_on_active(self):
        rig,e=self.rig('SWSH12.HisuianArcanineV_90')
        ability=fixtures.definition('CZ.SkySealStone_143').granted_abilities[0]
        ctx=EffectContext(rig.session,P1,e['target'],ability)
        await ability.effect(ctx)
        old=ctx.opponent_active()
        rig.to_area(old,P2,'discard')
        target=self.add(rig,fixtures.definition('CZ.RegigigasVSTAR_114'),P2,'activePokemonArea')
        target.set_attribute(AttrID.HP,10)
        from spirit.game.data_utils import Attack
        attack=Attack('Test',cost={},damage=20)
        attack_ctx=EffectContext(rig.session,P1,e['target'],attack)
        before=len(rig.board.find_player_area(P1,'prizePile').children)
        await attack_ctx.deal_damage(20,target=target,apply_modifiers=False)
        await rig.session.resolve_knockouts(attack_ctx)
        self.assertEqual(len(rig.board.find_player_area(P1,'prizePile').children),before-3)
