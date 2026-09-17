"""In-place batched counter transfer and remaining-HP receiver limits."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class DamageTransferSelectionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_transfer(self, path, owner=P1):
        definition = fixtures.definition(path)
        rig, _ = self.rig(path)
        for pid in (P1, P2):
            for card in list(rig.board.pokemon_in_play(pid)):
                rig.to_area(card, pid, 'hand')
            self.add(rig, definition if pid == owner else self.filler,
                     pid, 'activePokemonArea')
            self.add(rig, self.filler, pid, 'bench')
            self.add(rig, self.filler, pid, 'bench')
        ability = definition.abilities[0]
        carrier = rig.board.active_pokemon(owner)
        ctx = EffectContext(rig.session, owner, carrier, ability)
        field_owner = owner if ability.title == 'Damage Swap' else ctx.opponent_id
        field = rig.board.pokemon_in_play(field_owner)
        source, target, too_small = field[1], field[2], field[0]
        source.set_attribute(AttrID.HP, ctx.max_hp(source) - 50)
        target.set_attribute(AttrID.HP, 30)
        too_small.set_attribute(AttrID.HP, 20)
        return rig, ctx, source, target, too_small

    async def test_all_prints_both_owners_select_amount_before_destination(self):
        for path in ('BW1.Reuniclus_57', 'BW6.Reuniclus_126',
                     'BW7.Dusknoir_63', 'BW10.Dusknoir_104'):
            for owner in (P1, P2):
                with self.subTest(card=path, owner=owner):
                    rig, ctx, source, target, small = self.setup_transfer(path, owner)
                    hp_before = source.get_attribute(AttrID.HP)
                    order = []

                    async def choose(candidates, prompt, **kwargs):
                        if not order:
                            order.append('source')
                            self.assertIn(source, candidates)
                            self.assertTrue(all(p.owning_player_id == source.owning_player_id
                                                for p in candidates))
                            return source
                        order.append('destination')
                        self.assertEqual(order, ['source', 'amount', 'destination'])
                        self.assertNotIn(source, candidates)
                        self.assertNotIn(small, candidates)
                        self.assertIn(target, candidates)
                        return target

                    async def amount(pid, source_id, candidates, count, **kwargs):
                        order.append('amount')
                        self.assertEqual(candidates, [source])
                        self.assertEqual(count, 3)
                        self.assertEqual(kwargs['minimum'], 1)
                        self.assertEqual(kwargs['amount_per_click'], 10)
                        # Selection is only a preview until the receiver is chosen.
                        self.assertEqual(source.get_attribute(AttrID.HP), hp_before)
                        return {source.entity_id: 3}

                    ctx.choose_pokemon = AsyncMock(side_effect=choose)
                    rig.session.prompt_damage_counter_placement = AsyncMock(side_effect=amount)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(source.get_attribute(AttrID.HP), hp_before + 30)
                    self.assertEqual(target.get_attribute(AttrID.HP), 0)
                    self.assertIn(target, ctx.knockouts)
                    self.assertEqual(small.get_attribute(AttrID.HP), 20)

    async def test_invalid_or_empty_quantity_does_not_move_damage(self):
        for quantity in (0, 4, -1, '2', True):
            with self.subTest(quantity=quantity):
                rig, ctx, source, target, _ = self.setup_transfer('BW1.Reuniclus_57')
                before = source.get_attribute(AttrID.HP)
                ctx.choose_pokemon = AsyncMock(side_effect=[source, target])
                rig.session.prompt_damage_counter_placement = AsyncMock(
                    return_value={source.entity_id: quantity})
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.choose_pokemon.await_count, 1)
                self.assertEqual(source.get_attribute(AttrID.HP), before)

    async def test_stale_destination_below_selected_damage_is_rejected(self):
        rig, ctx, source, target, small = self.setup_transfer('BW7.Dusknoir_63')
        before = source.get_attribute(AttrID.HP)
        ctx.choose_pokemon = AsyncMock(side_effect=[source, small])
        rig.session.prompt_damage_counter_placement = AsyncMock(
            return_value={source.entity_id: 3})
        await ctx.ability.effect(ctx)
        self.assertEqual(source.get_attribute(AttrID.HP), before)
        self.assertEqual(small.get_attribute(AttrID.HP), 20)

    async def test_permissions_use_the_correct_side_and_no_dead_end(self):
        for path in ('BW1.Reuniclus_57', 'BW7.Dusknoir_63'):
            rig, ctx, source, target, small = self.setup_transfer(path)
            self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
            for p in rig.board.pokemon_in_play(source.owning_player_id):
                p.set_attribute(AttrID.HP, ctx.max_hp(p))
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
            source.set_attribute(AttrID.HP, ctx.max_hp(source) - 50)
            target.set_attribute(AttrID.HP, 5)
            small.set_attribute(AttrID.HP, ctx.max_hp(small))
            rig.to_area(target, target.owning_player_id, 'hand')
            rig.to_area(small, small.owning_player_id, 'hand')
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_native_picker_allows_done_after_partial_count(self):
        rig, ctx, source, _, _ = self.setup_transfer('BW1.Reuniclus_57')

        async def reply(player, message, offer, **kwargs):
            node = offer['targetMap'][ctx.source.entity_id][0]
            self.assertEqual(node['minimumToSelect'], 1)
            self.assertEqual(node['numberToSelect'], 5)
            self.assertEqual(node['validTargets'], [source.entity_id])
            self.assertEqual(node['amountPerClick'], 10)
            return {'selection': {'targetResponses': [
                {'entities': [{'target': source.entity_id, 'selections': 3}]}]}}

        with patch('spirit.game.session.game_session.AIPlayer', type('NotAI', (), {})), \
                patch.object(rig.session, 'prompt_selection_message', side_effect=reply):
            result = await rig.session.prompt_damage_counter_placement(
                P1, ctx.source.entity_id, [source], 5, 10, minimum=1)
        self.assertEqual(result, {source.entity_id: 3})

    async def test_native_picker_rejects_overflow_and_foreign_targets(self):
        rig, ctx, source, target, _ = self.setup_transfer('BW1.Reuniclus_57')
        for entries in (
            [{'target': source.entity_id, 'selections': 6}],
            [{'target': source.entity_id, 'selections': 5},
             {'target': source.entity_id, 'selections': 1}],
            [{'target': target.entity_id, 'selections': 1}],
            [{'target': source.entity_id, 'selections': -1}],
        ):
            with self.subTest(entries=entries):
                reply = {'selection': {'targetResponses': [{'entities': entries}]}}
                with patch('spirit.game.session.game_session.AIPlayer', type('NotAI', (), {})), \
                        patch.object(rig.session, 'prompt_selection_message', AsyncMock(return_value=reply)):
                    result = await rig.session.prompt_damage_counter_placement(
                        P1, ctx.source.entity_id, [source], 5, minimum=1)
                self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
