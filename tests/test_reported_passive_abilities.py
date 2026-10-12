"""Regressions for Prize attack gates, Bench shields, auras and evolution hooks."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Ability, Attack
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import attacks_blocked, compute_damage
from spirit.tools.effect_smoke import P1, P2


class ReportedPassiveAbilityTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def damage(self, rig, source, target, amount=40):
        return compute_damage(rig.board, source, target, amount,
                              ignore_weakness=True, ignore_resistance=True).amount

    def test_ultra_burst_unlocks_only_at_two_opponent_prizes(self):
        rig, entities = self.rig('SM12.UltraNecrozma_164')
        ultra = entities['target']
        prizes = rig.board.find_player_area(P2, 'prizePile')
        self.assertTrue(attacks_blocked(rig.board, ultra))
        for prize in list(prizes.children)[:3]:
            rig.to_area(prize, P2, 'hand')
        self.assertTrue(attacks_blocked(rig.board, ultra))
        rig.to_area(prizes.children[0], P2, 'hand')
        self.assertFalse(attacks_blocked(rig.board, ultra))

    async def test_daunting_pose_prevents_opposing_damage_and_counters_on_bench(self):
        rig, entities = self.rig('SM2.Machoke_64')
        own_bench = list(rig.board.find_player_area(P1, 'bench').children)
        protected = own_bench[0]
        attacker = entities['p2_active']
        self.assertEqual(self.damage(rig, attacker, protected), 0)
        before = protected.get_attribute(AttrID.HP)
        for ability, is_attack in ((Attack('Counter attack'), True),
                                   (Ability('Counter ability'), False)):
            ctx = EffectContext(rig.session, P2, attacker, ability)
            await ctx.deal_damage(30, target=protected, apply_modifiers=False,
                                  as_counters=True, is_attack=is_attack)
            self.assertEqual(protected.get_attribute(AttrID.HP), before)
        self.assertEqual(self.damage(rig, attacker, entities['target']), 40)

        own_ctx = EffectContext(rig.session, P1, entities['target'], Ability('Own counter'))
        await own_ctx.deal_damage(10, target=protected, apply_modifiers=False,
                                  as_counters=True, is_attack=False)
        self.assertEqual(protected.get_attribute(AttrID.HP), before - 10)

    async def test_princess_curtain_leaves_own_guzma_free_to_switch(self):
        rig, entities = self.rig('SWSH10.Diancie_68')
        guzma = self.add(rig, fixtures.definition('SM3.Guzma_115'), P1, 'hand')
        ctx = EffectContext(rig.session, P1, guzma, None)
        ctx.is_trainer_effect = True
        target = list(ctx.opponent_bench())[0]
        mine = list(ctx.my_bench())[0]
        ctx.choose_pokemon = AsyncMock(side_effect=[target, mine])
        rig.session._wait_for_client_catchup = AsyncMock()
        rig.session.send_game_sequence = AsyncMock()

        await fixtures.definition('SM3.Guzma_115').effect(ctx)

        self.assertIs(rig.board.active_pokemon(P2), target)
        self.assertIs(rig.board.active_pokemon(P1), mine)
        self.assertIn(entities['target'], ctx.my_bench())

    def test_princess_curtain_still_protects_benched_basics_from_opponent_supporters(self):
        rig, entities = self.rig('SWSH10.Diancie_68')
        guzma = self.add(rig, fixtures.definition('SM3.Guzma_115'), P2, 'hand')
        ctx = EffectContext(rig.session, P2, guzma, None)
        ctx.is_trainer_effect = True
        basic = list(ctx.opponent_bench())[0]
        self.assertTrue(ctx._trainer_blocked(basic))
        self.assertFalse(ctx._trainer_blocked(entities['target']))
        rig.to_area(entities['target'], P1, 'bench')
        self.assertFalse(ctx._trainer_blocked(basic))

    def test_princess_cheers_boosts_fighting_team_only_while_benched(self):
        rig, entities = self.rig('SM6.Diancie_74')
        diancie = entities['target']
        for copy in list(rig.board.find_player_area(P1, 'bench').children):
            if copy.archetype_id == diancie.archetype_id:
                rig.to_area(copy, P1, 'discard')
        attacker = rig.board.find_player_area(P1, 'bench').children[0]
        rig.to_area(attacker, P1, 'activePokemonArea')
        rig.to_area(diancie, P1, 'bench')
        attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIGHTING.value])
        defender = entities['p2_active']
        self.assertEqual(self.damage(rig, attacker, defender), 60)
        attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        self.assertEqual(self.damage(rig, attacker, defender), 40)
        rig.to_area(attacker, P1, 'bench')
        rig.to_area(diancie, P1, 'activePokemonArea')
        self.assertEqual(self.damage(rig, diancie, defender), 40)

    def test_other_typed_team_auras_use_the_same_damage_path(self):
        for path, ptype, bonus in (
                ('BW6.Altaria_84', PokemonTypes.DRAGON, 20),
                ('Promo_SM.Dhelmise_53', PokemonTypes.METAL, 10),
                ('XY3.Machamp_46', PokemonTypes.FIGHTING, 20)):
            with self.subTest(path=path):
                rig, entities = self.rig(path)
                aura = entities['target']
                for copy in list(rig.board.find_player_area(P1, 'bench').children):
                    if copy.archetype_id == aura.archetype_id:
                        rig.to_area(copy, P1, 'discard')
                attacker = rig.board.find_player_area(P1, 'bench').children[0]
                rig.to_area(attacker, P1, 'activePokemonArea')
                rig.to_area(aura, P1, 'bench')
                attacker.set_attribute(AttrID.POKEMON_TYPES, [ptype.value])
                self.assertEqual(self.damage(rig, attacker, entities['p2_active']),
                                 40 + bonus)

    async def test_metal_goggles_counter_shield_requires_metal_holder(self):
        rig, entities = self.rig('SM9.MetalGoggles_148', 'trainer')
        holder = entities['p1_active']
        rig.attach(entities['target'], holder)
        opponent = entities['p2_active']
        ctx = EffectContext(rig.session, P2, opponent, Ability('Counter ability'))
        before = holder.get_attribute(AttrID.HP)
        holder.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        await ctx.deal_damage(10, target=holder, apply_modifiers=False,
                              as_counters=True, is_attack=False)
        self.assertEqual(holder.get_attribute(AttrID.HP), before - 10)
        holder.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.METAL.value])
        await ctx.deal_damage(10, target=holder, apply_modifiers=False,
                              as_counters=True, is_attack=False)
        self.assertEqual(holder.get_attribute(AttrID.HP), before - 10)

    async def test_kinesis_places_counters_before_hand_evolution(self):
        rig, entities = self.rig('XY10.AlakazamEX_25')
        lower = entities['target']
        mega = self.add(rig, fixtures.definition('XY10.MAlakazamEX_26'), P1, 'hand')
        opposing_active = entities['p2_active']
        opposing_bench = list(rig.board.find_player_area(P2, 'bench').children)[0]
        active_hp = opposing_active.get_attribute(AttrID.HP)
        bench_hp = opposing_bench.get_attribute(AttrID.HP)
        rig.session.send_game_sequence = AsyncMock()
        rig.session.broadcast_packet = AsyncMock()

        async def confirm(_prompt, **_kwargs):
            self.assertIs(rig.board.active_pokemon(P1), lower)
            self.assertEqual(mega._containing_area_name(), 'hand')
            return True

        with patch.object(EffectContext, 'ask_yes_no', side_effect=confirm), \
             patch.object(EffectContext, 'choose_pokemon', new_callable=AsyncMock,
                          return_value=opposing_bench):
            self.assertTrue(await rig.session.perform_evolution(P1, mega, lower))
        self.assertEqual(opposing_active.get_attribute(AttrID.HP), active_hp - 20)
        self.assertEqual(opposing_bench.get_attribute(AttrID.HP), bench_hp - 30)
        self.assertIs(rig.board.active_pokemon(P1), mega)

    async def test_kinesis_does_not_trigger_for_deck_evolution(self):
        rig, entities = self.rig('XY10.AlakazamEX_25')
        lower = entities['target']
        mega = self.add(rig, fixtures.definition('XY10.MAlakazamEX_26'), P1, 'deck')
        opposing_active = entities['p2_active']
        before = opposing_active.get_attribute(AttrID.HP)
        rig.session.send_game_sequence = AsyncMock()
        rig.session.broadcast_packet = AsyncMock()
        with patch.object(EffectContext, 'ask_yes_no', new_callable=AsyncMock) as ask:
            self.assertTrue(await rig.session.perform_evolution(
                P1, mega, lower, from_zone_intro=True))
        ask.assert_not_awaited()
        self.assertEqual(opposing_active.get_attribute(AttrID.HP), before)

    async def test_daunting_pose_blocks_kinesis_bench_counters_only(self):
        rig, entities = self.rig('XY10.AlakazamEX_25')
        lower = entities['target']
        mega = self.add(rig, fixtures.definition('XY10.MAlakazamEX_26'), P1, 'hand')
        self.add(rig, fixtures.definition('SM2.Machoke_64'), P2, 'bench')
        opposing_active = entities['p2_active']
        opposing_bench = rig.board.find_player_area(P2, 'bench').children[0]
        active_hp = opposing_active.get_attribute(AttrID.HP)
        bench_hp = opposing_bench.get_attribute(AttrID.HP)
        rig.session.send_game_sequence = AsyncMock()
        rig.session.broadcast_packet = AsyncMock()
        with patch.object(EffectContext, 'ask_yes_no', new_callable=AsyncMock,
                          return_value=True), \
             patch.object(EffectContext, 'choose_pokemon', new_callable=AsyncMock,
                          return_value=opposing_bench):
            self.assertTrue(await rig.session.perform_evolution(P1, mega, lower))
        self.assertEqual(opposing_active.get_attribute(AttrID.HP), active_hp - 20)
        self.assertEqual(opposing_bench.get_attribute(AttrID.HP), bench_hp)


if __name__ == '__main__':
    unittest.main()
