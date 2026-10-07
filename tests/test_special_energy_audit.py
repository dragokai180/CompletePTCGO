"""Special Energy payment, provision, and end-of-turn regressions."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Attack
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _retreat_entry, energy_provided_count
from spirit.game.session.passives import energy_provided_options
from spirit.tools.effect_smoke import P1, P2


class SpecialEnergyAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_recycle_energy_returns_to_hand_when_paid_for_retreat(self):
        for path in ('SM11.RecycleEnergy_212', 'SM11.RecycleEnergy_257'):
            with self.subTest(path=path):
                rig, entries = self.rig('BW1.Snivy_1')
                active = entries['p1_active']
                for other in list(rig.board.attached_energies(active)):
                    rig.to_area(other, P1, 'discard')
                energy = self.add(rig, fixtures.definition(path), P1, 'hand')
                rig.attach(energy, active)
                replacement = rig.board.find_player_area(P1, 'bench').children[0]
                entry = _retreat_entry(
                    rig.board, rig.session.turn_state, P1,
                    rig.session.game_id,
                )[0]
                rig.session.send_game_sequence = AsyncMock()

                await rig.session._execute_retreat(
                    P1, active, entry, [replacement.entity_id],
                )

                self.assertIn(energy, rig.board.find_player_area(P1, 'hand').children)
                self.assertNotIn(energy, rig.board.find_player_area(P1, 'discard').children)
                self.assertIs(rig.board.active_pokemon(P1), replacement)
                reset_calls = [call for call in rig.session.send_game_sequence.await_args_list
                               if any(m['name'].endswith('AttributesReset')
                                      for m in call.args[2])]
                self.assertEqual(len(reset_calls), 1)
                self.assertEqual(reset_calls[0].args[0], [rig.session.players[P2]])
                self.assertEqual(reset_calls[0].args[2][0]['value']['entityID'],
                                 energy.entity_id)

    async def test_recycle_energy_replaces_effect_discard_but_not_hand_discard(self):
        rig, entries = self.rig('BW1.Snivy_1')
        active = entries['p1_active']
        energy = self.add(rig, fixtures.definition('SM11.RecycleEnergy_212'),
                          P1, 'hand')
        rig.attach(energy, active)
        ctx = EffectContext(rig.session, P1, active, None)

        await ctx.discard_cards([energy])

        self.assertIn(energy, rig.board.find_player_area(P1, 'hand').children)
        opponent_messages = ctx.messages_for(P2)
        self.assertFalse(any(m['name'].endswith('EntityIntroduced')
                             and m['value']['entityID'] == energy.entity_id
                             for m in opponent_messages))
        self.assertTrue(any(m['name'].endswith('AttributesReset')
                            and m['value']['entityID'] == energy.entity_id
                            for m in opponent_messages))

        await EffectContext(rig.session, P1, active, None).discard_cards([energy])
        self.assertIn(energy, rig.board.find_player_area(P1, 'discard').children)

    async def test_recycle_energy_returns_from_knockout(self):
        rig, entries = self.rig('BW1.Snivy_1')
        victim = entries['p1_active']
        attacker = rig.board.active_pokemon(P2)
        energy = self.add(rig, fixtures.definition('SM11.RecycleEnergy_212'),
                          P1, 'hand')
        rig.attach(energy, victim)
        ctx = EffectContext(rig.session, P2, attacker, Attack('Knock Out'))
        hp = victim.get_attribute(AttrID.HP)
        ctx.attack_damage[victim.entity_id] = (hp, hp)
        ctx.knockouts.append(victim)
        rig.session.send_game_sequence = AsyncMock()
        rig.session._take_prizes = AsyncMock(return_value=[])

        await rig.session.resolve_knockouts(ctx)

        self.assertIn(energy, rig.board.find_player_area(P1, 'hand').children)
        self.assertNotIn(energy, rig.board.find_player_area(P1, 'discard').children)
        self.assertTrue(any(call.args[0] == [rig.session.players[P2]]
                            and any(m['name'].endswith('AttributesReset')
                                    and m['value']['entityID'] == energy.entity_id
                                    for m in call.args[2])
                            for call in rig.session.send_game_sequence.await_args_list))

    async def test_triple_acceleration_provides_three_only_to_evolution(self):
        for path in ('SM10.TripleAccelerationEnergy_190',
                     'SM10.TripleAccelerationEnergy_234'):
            with self.subTest(path=path):
                rig, entries = self.rig('BW1.Snivy_1')
                basic = rig.board.find_player_area(P1, 'bench').children[0]
                evolution = self.add(rig, fixtures.definition('BW1.Servine_3'),
                                     P1, 'hand')
                await rig.session.perform_evolution(P1, evolution, basic)
                definition = fixtures.definition(path)
                energy = self.add(rig, definition, P1, 'hand')

                self.assertFalse(definition.attach_to(entries['p1_active']))
                self.assertTrue(definition.attach_to(evolution))
                rig.attach(energy, evolution)
                expected = [PokemonTypes.COLORLESS.value] * 3
                self.assertEqual(energy_provided_options(rig.board, energy),
                                 [expected])
                self.assertEqual(energy_provided_count(energy, rig.board), 3)

                await rig.session._fire_end_of_turn_triggers(P1)
                self.assertIn(energy, rig.board.find_player_area(P1, 'discard').children)

    async def test_temple_suppresses_triple_acceleration(self):
        rig, _ = self.rig('BW1.Snivy_1')
        basic = rig.board.find_player_area(P1, 'bench').children[0]
        evolution = self.add(rig, fixtures.definition('BW1.Servine_3'), P1,
                             'hand')
        await rig.session.perform_evolution(P1, evolution, basic)
        energy = self.add(rig, fixtures.definition(
            'SM10.TripleAccelerationEnergy_190'), P1, 'hand')
        rig.attach(energy, evolution)
        stadium = self.add(rig, fixtures.definition(
            'SWSH10.TempleofSinnoh_155'), P1, 'hand')
        rig.board.move_card(stadium.entity_id,
                            rig.board.find_global_area('activeStadium').entity_id)

        self.assertEqual(energy_provided_options(rig.board, energy),
                         [[PokemonTypes.COLORLESS.value]])
        await rig.session._fire_end_of_turn_triggers(P1)
        self.assertIn(energy, rig.board.attached_energies(evolution))

    async def test_devolution_discards_triple_acceleration_from_basic(self):
        rig, _ = self.rig('BW1.Snivy_1')
        basic = rig.board.find_player_area(P1, 'bench').children[0]
        evolution = self.add(rig, fixtures.definition('BW1.Servine_3'),
                             P1, 'hand')
        await rig.session.perform_evolution(P1, evolution, basic)
        energy = self.add(rig, fixtures.definition(
            'SM10.TripleAccelerationEnergy_190'), P1, 'hand')
        rig.attach(energy, evolution)

        await rig.session.perform_devolution(evolution)

        self.assertIn(energy, rig.board.find_player_area(P1, 'discard').children)
        self.assertNotIn(energy, rig.board.attached_energies(basic))

    async def test_nitro_fire_returns_only_after_fire_carrier_attack(self):
        for path, returns in (('BW1.Tepig_15', True),
                              ('BW1.Snivy_1', False)):
            with self.subTest(path=path):
                rig, entries = self.rig(path)
                attacker = entries['p1_active']
                energy = self.add(rig, fixtures.definition(
                    'ME4.NitroFireEnergy_86'), P1, 'hand')
                rig.attach(energy, attacker)
                ctx = EffectContext(rig.session, P1, attacker,
                                    Attack('Discard Energy'))

                await ctx.discard_cards([energy])
                self.assertIn(energy, rig.board.find_player_area(P1, 'discard').children)
                self.assertEqual(len(ctx.deferred_actions), 1)
                await ctx.deferred_actions.pop()()

                destination = 'hand' if returns else 'discard'
                self.assertIn(energy, rig.board.find_player_area(
                    P1, destination).children)
                self.assertEqual(
                    any(m['name'].endswith('AttributesReset')
                        and m['value']['entityID'] == energy.entity_id
                        for m in ctx.messages_for(P2)),
                    returns,
                )


if __name__ == '__main__':
    unittest.main()
