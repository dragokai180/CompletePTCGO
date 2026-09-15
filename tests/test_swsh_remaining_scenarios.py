"""Scenario coverage for conditional SWSH Trainers and SM/SWSH powers."""
import unittest
from unittest.mock import AsyncMock
from importlib import import_module
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1, P2


class SwshRemainingScenarios(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def energy(self, rig, kind=PokemonTypes.LIGHTNING, zone='discard'):
        return self.add(rig, CARD_DEFS_BY_GUID[self.energies[kind.value].lower()], P1, zone)

    async def test_raihan_all_printings_require_ko_and_basic_energy_then_private_search(self):
        for path in ('SWSH7.Raihan_152','SWSH7.Raihan_202','SWSH7.Raihan_224','CZ.Raihan_140'):
            rig,e=self.rig(path,'trainer')
            definition=fixtures.definition(path)
            ctx=EffectContext(rig.session,P1,e['target'],None)
            for c in list(ctx.discard_pile()):rig.to_area(c,P1,'deck')
            rig.session.turn_state.kos_suffered_last_turn={P1:[{'archetype_id':ctx.my_active().archetype_id}]}
            self.assertFalse(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
            wrong=self.add(rig,fixtures.definition('SM11.RecycleEnergy_212'),P1,'discard')
            self.assertFalse(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
            energy=self.energy(rig)
            self.assertTrue(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
            ctx.search_deck=AsyncMock(return_value=[])
            await definition.effect(ctx)
            self.assertIn(energy.parent,ctx.my_pokemon_in_play())
            self.assertIn(wrong,ctx.discard_pile())
            self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'],1)

    async def test_rose_all_printings_require_basic_energy_and_one_vmax_destination(self):
        for path in ('SWSH3.Rose_168','SWSH3.Rose_189','SWSH3.Rose_196','SWSH45.Rose_71'):
            rig,e=self.rig(path,'trainer')
            definition=fixtures.definition(path)
            ctx=EffectContext(rig.session,P1,e['target'],None)
            target=self.add(rig,fixtures.definition('SWSH3.SalamenceVMAX_144'),P1,'bench')
            for c in list(ctx.discard_pile()):rig.to_area(c,P1,'deck')
            self.assertFalse(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
            energies=[self.energy(rig) for _ in range(2)]
            self.assertTrue(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
            hand=list(ctx.hand())
            ctx.choose_cards=AsyncMock(return_value=energies)
            ctx.choose_pokemon=AsyncMock(return_value=target)
            await definition.effect(ctx)
            self.assertTrue(all(c.parent is target for c in energies))
            self.assertTrue(all(c in ctx.discard_pile() for c in hand))

    async def test_rescue_carrier_uses_printed_hp_not_previous_damage(self):
        for path in ('SWSH7.RescueCarrier_154','CZ.RescueCarrier_142'):
            rig,e=self.rig(path,'trainer')
            ctx=EffectContext(rig.session,P1,e['target'],None)
            definition=fixtures.definition(path)
            for c in list(ctx.discard_pile()):rig.to_area(c,P1,'deck')
            wrong=self.add(rig,fixtures.definition('SWSH12.HisuianArcanineV_90'),P1,'discard')
            wrong.set_attribute(AttrID.HP,0)
            self.assertFalse(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
            valid=self.add(rig,fixtures.definition('SWSH11.Spiritomb_117'),P1,'discard')
            self.assertTrue(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))
            await definition.effect(ctx)
            self.assertIn(valid,ctx.hand())
            self.assertIn(wrong,ctx.discard_pile())

    async def test_camping_gear_cannot_play_empty_deck_and_search_ends_turn(self):
        path='SWSH5.CampingGear_122'
        rig,e=self.rig(path,'trainer')
        ctx=EffectContext(rig.session,P1,e['target'],None)
        definition=fixtures.definition(path)
        ctx.search_deck=AsyncMock(return_value=[])
        await definition.effect(ctx)
        self.assertTrue(ctx.ends_turn)
        self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'],1)
        for c in list(ctx.deck()):rig.to_area(c,P1,'discard')
        self.assertFalse(trainer_condition_met(definition.condition,rig.board,P1,ctx.source))

    async def test_dance_of_ancients_one_energy_and_two_distinct_destinations(self):
        for energy_count,bench_count in ((1,1),(1,3),(2,3)):
            rig,e=self.rig('SM9.TapuKoko_51')
            ctx=EffectContext(rig.session,P1,e['target'],fixtures.definition('SM9.TapuKoko_51').abilities[0])
            ability=ctx.ability
            self.assertFalse(ability.condition(rig.board,P1,ctx.source))
            rig.to_area(ctx.source,P1,'bench')
            for c in list(ctx.my_bench()):
                if c is not ctx.source:rig.to_area(c,P1,'deck')
            while len(ctx.my_bench())<bench_count:self.add(rig,self.filler,P1,'bench')
            for c in list(ctx.discard_pile()):rig.to_area(c,P1,'deck')
            self.assertFalse(ability.condition(rig.board,P1,ctx.source))
            energies=[self.energy(rig) for _ in range(energy_count)]
            self.assertTrue(ability.condition(rig.board,P1,ctx.source))
            targets=([ctx.source] if bench_count==1 else ctx.my_bench()[1:])
            ctx.choose_cards=AsyncMock(side_effect=[targets,energies])
            ctx.choose_pokemon=AsyncMock(return_value=targets[-1])
            await ability.effect(ctx)
            self.assertIn(ctx.source,rig.board.find_player_area(P1,'lostZone').children)
            if bench_count==1:
                self.assertIn(energies[0],ctx.discard_pile())
            else:
                self.assertIs(energies[0].parent,targets[-1])
                if energy_count==2:self.assertIs(energies[1].parent,targets[0])
            self.assertFalse(ctx.knockouts)

    async def test_star_guardian_discards_full_stack_without_awarding_prizes(self):
        rig,e=self.rig('CZ.RegigigasVSTAR_114')
        ability=fixtures.definition('CZ.RegigigasVSTAR_114').abilities[0]
        ctx=EffectContext(rig.session,P1,e['target'],ability)
        self.assertFalse(ability.condition(rig.board,P1,ctx.source))
        prizes=rig.board.find_player_area(P2,'prizePile')
        for c in list(prizes.children)[1:]:rig.to_area(c,P2,'deck')
        self.assertTrue(ability.condition(rig.board,P1,ctx.source))
        target=ctx.opponent_bench()[0]
        energy=self.energy(rig)
        energy.owning_player_id=P2
        rig.attach(energy,target)
        before=len(rig.board.find_player_area(P1,'prizePile').children)
        ctx.ask_yes_no=AsyncMock(return_value=True)
        ctx.choose_pokemon=AsyncMock(return_value=target)
        await ability.effect(ctx)
        self.assertIn(target,ctx.discard_pile(P2))
        self.assertIn(energy,ctx.discard_pile(P2))
        self.assertFalse(ctx.knockouts)
        self.assertEqual(len(rig.board.find_player_area(P1,'prizePile').children),before)

    async def test_star_gravity_only_reduces_v_above_one_hundred_hp(self):
        rig,e=self.rig('SWSH12.HisuianArcanineV_90')
        attack=fixtures.definition('SWSH12.EarthenSealStone_154').granted_abilities[0]
        ctx=EffectContext(rig.session,P1,e['target'],attack)
        high=self.add(rig,fixtures.definition('SWSH12.HisuianArcanineV_90'),P2,'bench')
        low=self.add(rig,fixtures.definition('SWSH12.HisuianArcanineV_90'),P2,'bench')
        low.set_attribute(AttrID.HP,60)
        normal=ctx.opponent_active()
        hp=normal.get_attribute(AttrID.HP)
        await attack.effect(ctx)
        self.assertEqual(high.get_attribute(AttrID.HP),100)
        self.assertEqual(low.get_attribute(AttrID.HP),60)
        self.assertEqual(normal.get_attribute(AttrID.HP),hp)

    async def test_elusive_master_only_last_hand_card_and_bench_then_draw(self):
        rig,e=self.rig('SWSH4.Beedrill_3')
        source=e['target']
        ability=fixtures.definition('SWSH4.Beedrill_3').abilities[0]
        ctx=EffectContext(rig.session,P1,source,ability)
        rig.to_area(source,P1,'hand')
        self.assertFalse(ability.condition(rig.board,P1,source))
        for c in list(ctx.hand()):
            if c is not source:rig.to_area(c,P1,'deck')
        self.assertTrue(ability.condition(rig.board,P1,source))
        ctx.ask_yes_no=AsyncMock(return_value=True)
        async def draw(count):
            self.assertIn(source,ctx.my_bench())
            self.assertEqual(count,3)
        ctx.draw_cards=draw
        await ability.effect(ctx)

    async def test_irresistible_force_moves_fighting_special_energy_not_basic_only(self):
        rig,e=self.rig('SWSH12.HisuianArcanineV_90')
        ability=fixtures.definition('SWSH12.HisuianArcanineV_90').abilities[0]
        ctx=EffectContext(rig.session,P1,e['target'],ability)
        for pokemon in ctx.my_pokemon_in_play():
            for energy in list(ctx.attached_energies(pokemon)):rig.to_area(energy,P1,'discard')
        self.assertFalse(ability.condition(rig.board,P1,ctx.source))
        target=ctx.my_bench()[0]
        energy=self.add(rig,fixtures.definition('SM1.RainbowEnergy_137'),P1,'hand')
        rig.attach(energy,target)
        self.assertTrue(ability.condition(rig.board,P1,ctx.source))
        await ability.effect(ctx)
        self.assertIs(energy.parent,ctx.source)
        self.assertFalse(ability.condition(rig.board,P1,ctx.source))
