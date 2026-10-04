"""Technical Machine attacks must be granted and execute their printed effects."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.tools.effect_smoke import P1


TM_PATHS = (
    'SV4.TechnicalMachineBlindside_176',
    'SV4.TechnicalMachineDevolution_177',
    'SV4.TechnicalMachineEvolution_178',
    'SV4.TechnicalMachineTurboEnergize_179',
    'SV045.TechnicalMachineCrisisPunch_90',
    'SV08.TechnicalMachineFluorite_188',
)


class TechnicalMachineAttackTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    @staticmethod
    def legal_entry(rig, entity_id, action_id):
        return next((entry for entry in compute_legal_actions(
            rig.board, rig.session.turn_state, P1, rig.session.game_id)
            if entry['entityID'] == entity_id
            and entry['selectableAction']['actionID'] == action_id), None)

    async def test_evolution_attack_is_offered_after_attaching_tool(self):
        rig, entities = self.rig('BW1.Snivy_1')
        active = entities['target']
        tool_def = definition('SV4.TechnicalMachineEvolution_178')
        tool = self.add(rig, tool_def, P1, 'hand')
        attack = tool_def.granted_abilities[0]
        self.assertIsNone(self.legal_entry(
            rig, active.entity_id, attack.ability_id))

        attach_entry = next(entry for entry in compute_legal_actions(
            rig.board, rig.session.turn_state, P1, rig.session.game_id)
            if entry['entityID'] == tool.entity_id)
        await rig.session._execute_attach_tool(
            P1, tool, attach_entry, [active.entity_id])

        self.assertIs(tool.parent, active)
        self.assertTrue(any(row.get('abilityID') == attack.ability_id
                            for row in active.get_attribute(AttrID.PIE_ABILITIES)))
        self.assertIsNotNone(self.legal_entry(
            rig, active.entity_id, attack.ability_id))

    async def test_all_technical_machines_grant_their_attack(self):
        for path in TM_PATHS:
            with self.subTest(tool=path):
                rig, entities = self.rig('BW1.Snivy_1')
                active = entities['target']
                tool_def = definition(path)
                tool = self.add(rig, tool_def, P1, 'hand')
                rig.attach(tool, active)
                granted_id = tool_def.granted_abilities[0].ability_id
                self.assertTrue(any(row.get('abilityID') == granted_id
                                    for row in rig.session._pie_ability_entries(active)))

        rig, entities = self.rig('BW1.Snivy_1')
        active = entities['target']
        core_memory = self.add(rig, definition('ME3.CoreMemory_70'), P1,
                               'hand')
        rig.attach(core_memory, active)
        core_id = definition('ME3.CoreMemory_70').granted_abilities[0].ability_id
        self.assertFalse(any(row.get('abilityID') == core_id
                             for row in rig.session._pie_ability_entries(active)))

    async def test_technical_machine_is_discarded_at_end_of_turn(self):
        rig, entities = self.rig('BW1.Snivy_1')
        active = entities['target']
        tool_def = definition('SV4.TechnicalMachineEvolution_178')
        tool = self.add(rig, tool_def, P1, 'hand')
        rig.attach(tool, active)

        await rig.session._fire_end_of_turn_triggers(P1)

        discard = rig.board.find_player_area(P1, 'discard')
        self.assertIn(tool, discard.children)
        self.assertFalse(any(
            row.get('abilityID') == tool_def.granted_abilities[0].ability_id
            for row in rig.session._pie_ability_entries(active)
        ))

    async def test_evolution_evolves_two_distinct_benched_pokemon(self):
        rig, entities = self.rig('BW1.Snivy_1')
        attack = definition('SV4.TechnicalMachineEvolution_178').granted_abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], attack)
        snivy = ctx.my_bench()[0]
        tepig = self.add(rig, definition('BW1.Tepig_15'), P1, 'bench')
        servine = self.add(rig, definition('BW1.Servine_3'), P1, 'deck')
        pignite = self.add(rig, definition('BW1.Pignite_17'), P1, 'deck')
        ctx.choose_cards = AsyncMock(return_value=[snivy, tepig])
        ctx.search_deck = AsyncMock(side_effect=[[servine], [pignite]])
        ctx.shuffle_deck = AsyncMock()

        await attack.effect(ctx)

        self.assertIn(servine, ctx.my_bench())
        self.assertIn(pignite, ctx.my_bench())
        self.assertIs(snivy.parent, servine)
        self.assertIs(tepig.parent, pignite)
        self.assertEqual(ctx.search_deck.await_count, 2)
        first, second = ctx.search_deck.call_args_list
        self.assertTrue(first.args[0](servine))
        self.assertFalse(first.args[0](pignite))
        self.assertTrue(second.args[0](pignite))
        self.assertFalse(second.args[0](servine))
        ctx.shuffle_deck.assert_awaited_once()

    async def test_turbo_energize_attaches_two_basic_energy_from_deck(self):
        rig, entities = self.rig('BW1.Snivy_1')
        attack = definition('SV4.TechnicalMachineTurboEnergize_179').granted_abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], attack)
        energies = [rig.pull_guid(P1, self.energies[PokemonTypes.GRASS.value])
                    for _ in range(2)]
        target = ctx.my_bench()[0]
        ctx.search_deck = AsyncMock(return_value=energies)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.shuffle_deck = AsyncMock()

        await attack.effect(ctx)

        self.assertTrue(all(energy.parent is target for energy in energies))
        self.assertEqual(ctx.choose_pokemon.await_count, 2)
        ctx.shuffle_deck.assert_awaited_once()

    async def test_blindside_targets_only_damaged_opposing_pokemon(self):
        rig, entities = self.rig('BW1.Snivy_1')
        attack = definition('SV4.TechnicalMachineBlindside_176').granted_abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], attack)
        damaged = ctx.opponent_bench()[0]
        undamaged = ctx.opponent_bench()[1]
        damaged.set_attribute(AttrID.HP, ctx.max_hp(damaged) - 20)
        undamaged.set_attribute(AttrID.HP, ctx.max_hp(undamaged))
        ctx.choose_cards = AsyncMock(return_value=[damaged])
        ctx.deal_damage = AsyncMock()

        await attack.effect(ctx)

        candidates = ctx.choose_cards.call_args.args[0]
        self.assertIn(damaged, candidates)
        self.assertNotIn(undamaged, candidates)
        ctx.deal_damage.assert_awaited_once()
        self.assertEqual(ctx.deal_damage.call_args.args[0], 100)
        self.assertIs(ctx.deal_damage.call_args.kwargs['target'], damaged)

    async def test_devolution_returns_each_opposing_evolution_to_hand(self):
        rig, entities = self.rig('BW1.Snivy_1')
        attack = definition('SV4.TechnicalMachineDevolution_177').granted_abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], attack)
        snivy = self.add(rig, definition('BW1.Snivy_1'), ctx.opponent_id,
                         'bench')
        servine = self.add(rig, definition('BW1.Servine_3'), ctx.opponent_id,
                           'hand')
        await rig.session.perform_evolution(ctx.opponent_id, servine, snivy)

        await attack.effect(ctx)

        self.assertIn(snivy, ctx.opponent_bench())
        self.assertIn(servine, ctx.hand(ctx.opponent_id))

    async def test_crisis_punch_requires_one_opponent_prize(self):
        rig, entities = self.rig('BW1.Snivy_1')
        active = entities['target']
        tool_def = definition('SV045.TechnicalMachineCrisisPunch_90')
        attack = tool_def.granted_abilities[0]
        tool = self.add(rig, tool_def, P1, 'hand')
        rig.attach(tool, active)
        while len(rig.board.attached_energies(active)) < 3:
            energy = rig.pull_guid(P1, self.energies[PokemonTypes.GRASS.value])
            rig.attach(energy, active)
        active.set_attribute(AttrID.PIE_ABILITIES,
                             rig.session._pie_ability_entries(active))
        self.assertIsNone(self.legal_entry(
            rig, active.entity_id, attack.ability_id))

        prizes = rig.board.find_player_area(rig.session._opponent_id(P1),
                                            'prizePile')
        for card in list(prizes.children)[:-1]:
            rig.to_area(card, rig.session._opponent_id(P1), 'discard')
        self.assertIsNotNone(self.legal_entry(
            rig, active.entity_id, attack.ability_id))


if __name__ == '__main__':
    unittest.main()
