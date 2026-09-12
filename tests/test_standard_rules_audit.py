"""Standard-era semantic regressions; exercise real board entities."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage
from spirit.game.session.passives import energy_provided_options
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class StandardRulesAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass=classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig=fixtures.HgssRulesTests.rig
    ctx=fixtures.HgssRulesTests.ctx
    add=fixtures.HgssRulesTests.add

    async def test_ignition_and_prism_do_not_change_other_energy(self):
        for path,stage,units in [
                ('RSV10PT5.IgnitionEnergy_86',PokemonStage.STAGE1,3),
                ('ME2.IgnitionEnergy_124',PokemonStage.STAGE1,3),
                ('ZSV10PT5.PrismEnergy_86',PokemonStage.BASIC,1),
                ('ME2PT5.PrismEnergy_216',PokemonStage.BASIC,1)]:
            with self.subTest(path=path):
                rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
                ctx.attacker.set_attribute(AttrID.STAGE,stage.value)
                energy=self.add(rig,definition(path),P1,'hand')
                rig.attach(energy,ctx.attacker)
                basic=rig.pull_guid(P1,self.energies[PokemonTypes.GRASS.value])
                rig.attach(basic,ctx.attacker)
                self.assertEqual(energy_provided_options(rig.board,basic),[[PokemonTypes.GRASS.value]])
                self.assertTrue(all(len(opt)==units for opt in energy_provided_options(rig.board,energy)))

    async def test_neo_upper_provides_two_different_types_on_stage_two(self):
        rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
        ctx.attacker.set_attribute(AttrID.STAGE,PokemonStage.STAGE2.value)
        energy=self.add(rig,definition('SV05.NeoUpperEnergy_162'),P1,'hand')
        rig.attach(energy,ctx.attacker)
        options=energy_provided_options(rig.board,energy)
        self.assertTrue(any(sorted(opt)==sorted([PokemonTypes.GRASS.value,PokemonTypes.FIRE.value]) for opt in options))

    async def test_neo_upper_does_not_modify_other_energy_cards(self):
        rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
        ctx.attacker.set_attribute(AttrID.STAGE,PokemonStage.STAGE2.value)
        energy=self.add(rig,definition('SV05.NeoUpperEnergy_162'),P1,'hand')
        rig.attach(energy,ctx.attacker)
        basic=rig.pull_guid(P1,self.energies[PokemonTypes.GRASS.value])
        rig.attach(basic,ctx.attacker)
        self.assertEqual(energy_provided_options(rig.board,basic),[[PokemonTypes.GRASS.value]])

    async def test_prime_catcher_does_not_switch_self_if_gust_fails(self):
        from spirit.game.card_effects.trainers import catcher_switch_both
        rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
        ctx.choose_pokemon=AsyncMock(side_effect=[ctx.opponent_bench()[0],ctx.my_bench()[0]])
        ctx.switch_active=AsyncMock(return_value=False)
        await catcher_switch_both(ctx)
        ctx.switch_active.assert_awaited_once()

    async def test_spikemuth_ability_condition_accepts_source(self):
        path='SV10.SpikemuthGym_169'
        rig,e=self.rig(path,'trainer')
        ability=definition(path).ability
        self.assertTrue(ability.condition(rig.board,P1,e['target']))
        for card in list(rig.board.find_player_area(P1,'deck').children):
            rig.to_area(card,P1,'hand')
        self.assertFalse(ability.condition(rig.board,P1,e['target']))

    async def test_maximum_belt_distinguishes_ex_from_EX(self):
        rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
        tool=self.add(rig,definition('SV05.MaximumBelt_154'),P1,'hand')
        rig.attach(tool,ctx.attacker)
        passive=definition('SV05.MaximumBelt_154').passive
        for path,bonus in [('BW7.KeldeoEX_49',0),('SV05.IronCrownex_81',50)]:
            target=self.add(rig,definition(path),P2,'bench')
            calc=SimpleNamespace(is_attack=True,is_opposing=True,to_active=True,
                attacker=ctx.attacker,target=target,amount=20)
            passive.modify_damage_dealt(calc,tool)
            self.assertEqual(calc.amount,20+bonus)

    async def test_cyrano_does_not_search_uppercase_EX(self):
        from spirit.game.scripts.cards.SV08.Cyrano_170 import _is_pokemon_ex
        rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
        old=self.add(rig,definition('BW7.KeldeoEX_49'),P1,'deck')
        new=self.add(rig,definition('SV05.IronCrownex_81'),P1,'deck')
        self.assertFalse(_is_pokemon_ex(old))
        self.assertTrue(_is_pokemon_ex(new))

    async def test_secret_box_requires_nonempty_deck(self):
        path='SV06.SecretBox_163'
        rig,e=self.rig(path,'trainer')
        for card in list(rig.board.find_player_area(P1,'deck').children):
            rig.to_area(card,P1,'hand')
        self.assertFalse(definition(path).condition(rig.board,P1,e['target']))

    async def test_reboot_pod_allows_choosing_recipient_when_energy_is_short(self):
        path='SV05.RebootPod_158'
        rig,e=self.rig(path,'trainer')
        ctx=EffectContext(rig.session,P1,e['target'],None)
        one=self.add(rig,definition('SV05.IronCrownex_81'),P1,'bench')
        two=self.add(rig,definition('SV05.IronLeavesex_25'),P1,'bench')
        energy=rig.pull_guid(P1,self.energies[PokemonTypes.GRASS.value])
        ctx.discard_pile=lambda *args:[energy]
        ctx.choose_cards=AsyncMock(return_value=[energy])
        ctx.choose_pokemon=AsyncMock(return_value=two)
        ctx.attach_energy=AsyncMock(return_value=True)
        await definition(path).effect(ctx)
        ctx.attach_energy.assert_awaited_once_with(energy,two)
        self.assertIn(one,ctx.choose_pokemon.call_args.args[0])

    async def test_legacy_energy_is_once_for_each_player(self):
        rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
        passive=definition('SV06.LegacyEnergy_167').passive
        holders=[ctx.attacker,ctx.defender]
        for holder in holders:
            energy=self.add(rig,definition('SV06.LegacyEnergy_167'),holder.owning_player_id,'hand')
            rig.attach(energy,holder)
            event=SimpleNamespace(session=rig.session,player_id=P2 if holder is ctx.attacker else P1,
                is_attack_effect=lambda:True,attack_damage={holder.entity_id:(100,60)})
            self.assertEqual(passive.modify_prizes_for_knockout(holder,event,2,energy),1)
            self.assertEqual(passive.modify_prizes_for_knockout(holder,event,2,energy),2)

    async def test_legacy_energy_does_not_reduce_counter_knockouts(self):
        rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
        holder=ctx.defender
        energy=self.add(rig,definition('SV06.LegacyEnergy_167'),P2,'hand')
        rig.attach(energy,holder)
        event=SimpleNamespace(session=rig.session,player_id=P1,
            is_attack_effect=lambda:True,attack_damage={})
        passive=definition('SV06.LegacyEnergy_167').passive
        self.assertEqual(passive.modify_prizes_for_knockout(holder,event,2,energy),2)
