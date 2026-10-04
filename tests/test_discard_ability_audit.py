"""Out-of-play Pokémon Abilities honor Bench space and resolve their effects."""

import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _out_of_zone_ability_entries
from spirit.game.session.passives import effective_bench_capacity, effective_max_hp
from spirit.tools.effect_smoke import P1


class DiscardAbilityAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_source(self, path):
        rig, _ = self.rig('BW1.Snivy_1')
        definition = fixtures.definition(path)
        source = self.add(rig, definition, P1, 'discard')
        return rig, source, definition.abilities[0]

    @staticmethod
    def offered(rig, source, ability):
        return any(entry['entityID'] == source.entity_id
                   and entry['selectableAction']['actionID'] == ability.ability_id
                   for entry in _out_of_zone_ability_entries(
                       rig.board, rig.session.turn_state, P1,
                       rig.session.game_id))

    def expand_bench(self, rig, occupied):
        stadium = self.add(rig, fixtures.definition('XY6.SkyField_89'),
                           P1, 'hand')
        rig.board.move_card(stadium.entity_id,
                            rig.board.find_global_area('activeStadium').entity_id)
        bench = rig.board.find_player_area(P1, 'bench')
        while len(bench.children) < occupied:
            rig.to_area(rig.pull_guid(P1, self.filler.guid), P1, 'bench')
        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)

    def test_rebirth_is_hidden_when_bench_is_full(self):
        for path in ('BW6.HoOhEX_22', 'BW6.HoOhEX_119'):
            with self.subTest(path=path):
                rig, source, ability = self.setup_source(path)
                self.assertTrue(self.offered(rig, source, ability))
                bench = rig.board.find_player_area(P1, 'bench')
                while len(bench.children) < 5:
                    rig.to_area(rig.pull_guid(P1, self.filler.guid), P1, 'bench')
                self.assertFalse(self.offered(rig, source, ability))
                self.expand_bench(rig, 7)
                self.assertTrue(self.offered(rig, source, ability))
                self.expand_bench(rig, 8)
                self.assertFalse(self.offered(rig, source, ability))

    def test_emergency_surfacing_uses_expanded_bench_space(self):
        rig, source, ability = self.setup_source('SWSH9.Empoleon_37')
        for card in list(rig.board.find_player_area(P1, 'hand').children):
            rig.to_area(card, P1, 'deck')
        self.expand_bench(rig, 7)
        self.assertTrue(self.offered(rig, source, ability))
        self.expand_bench(rig, 8)
        self.assertFalse(self.offered(rig, source, ability))

    async def test_emergency_surfacing_enters_eighth_slot_and_draws(self):
        rig, source, ability = self.setup_source('SWSH9.Empoleon_37')
        for card in list(rig.board.find_player_area(P1, 'hand').children):
            rig.to_area(card, P1, 'deck')
        self.expand_bench(rig, 7)
        entry = next(entry for entry in _out_of_zone_ability_entries(
            rig.board, rig.session.turn_state, P1, rig.session.game_id)
            if entry['entityID'] == source.entity_id
            and entry['selectableAction']['actionID'] == ability.ability_id)

        await rig.session._execute_use_ability(P1, source, entry)

        self.assertIn(source, rig.board.find_player_area(P1, 'bench').children)
        self.assertEqual(len(rig.board.find_player_area(P1, 'bench').children), 8)
        self.assertEqual(len(rig.board.find_player_area(P1, 'hand').children), 3)

    async def test_prehistoric_call_moves_all_prints_to_deck_bottom(self):
        for path in ('BW10.Lileep_3', 'BW10.Tirtouga_27', 'BW10.Archen_53'):
            with self.subTest(path=path):
                rig, source, ability = self.setup_source(path)
                self.assertTrue(self.offered(rig, source, ability))
                ctx = EffectContext(rig.session, P1, source, ability)

                await ability.effect(ctx)

                self.assertIs(ctx.deck()[0], source)
                self.assertNotIn(source, ctx.discard_pile())

    async def test_rebirth_tails_leaves_card_in_discard_and_uses_ability(self):
        rig, source, ability = self.setup_source('BW6.HoOhEX_22')
        entry = next(entry for entry in _out_of_zone_ability_entries(
            rig.board, rig.session.turn_state, P1, rig.session.game_id)
            if entry['entityID'] == source.entity_id
            and entry['selectableAction']['actionID'] == ability.ability_id)
        with patch.object(EffectContext, 'flip_coins',
                          AsyncMock(return_value=[False])) as flip:
            await rig.session._execute_use_ability(P1, source, entry)

        flip.assert_awaited_once()
        self.assertIn(source, rig.board.find_player_area(P1, 'discard').children)
        self.assertFalse(self.offered(rig, source, ability))

    async def test_rebirth_heads_benches_and_attaches_distinct_basic_types(self):
        rig, source, ability = self.setup_source('BW6.HoOhEX_22')
        ctx = EffectContext(rig.session, P1, source, ability)
        ctx.flip_coins = AsyncMock(return_value=[True])
        ctx.choose_cards = AsyncMock(side_effect=lambda pool, *a, **kw: [pool[0]])

        await ability.effect(ctx)

        self.assertIn(source, ctx.my_bench())
        attached = ctx.attached_energies(source)
        self.assertEqual(len(attached), 3)
        types = [tuple(energy.get_attribute(AttrID.POKEMON_TYPES) or [])
                 for energy in attached]
        self.assertEqual(len(set(types)), 3)

    async def test_netherworld_gate_benches_and_marks_its_holder(self):
        rig, source, ability = self.setup_source('SWSH11.Gengar_66')
        ctx = EffectContext(rig.session, P1, source, ability)

        await ability.effect(ctx)

        self.assertIn(source, ctx.my_bench())
        self.assertEqual(source.get_attribute(AttrID.HP),
                         effective_max_hp(rig.board, source) - 30)

    async def test_reviving_flame_benches_attaches_and_ends_turn(self):
        rig, source, ability = self.setup_source('SWSH12.HoOhV_140')
        ctx = EffectContext(rig.session, P1, source, ability)
        # Select four of the Basic Energy already stocked in the discard pile.
        energies = [card for card in ctx.discard_pile()
                    if card.archetype_id in self.energies.values()][:4]
        ctx.choose_cards = AsyncMock(return_value=energies)

        await ability.effect(ctx)

        self.assertIn(source, ctx.my_bench())
        self.assertTrue(ctx.ends_turn)
        self.assertTrue(all(energy.parent is source for energy in energies))


if __name__ == '__main__':
    unittest.main()
