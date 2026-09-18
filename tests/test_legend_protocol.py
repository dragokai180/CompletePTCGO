"""Native LEGEND rendering contract and physical-card lifecycle regressions."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, CardType, GameSequence, PokemonStage, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.models.board import LegendPokemonEntity
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext, full_stack, split_pokemon_stack
from spirit.game.session.constants import SelectionKind
from spirit.game.session.passives import effective_retreat_cost
from spirit.game.legend import legend_pairs
from spirit.tools.effect_smoke import Rig, P1, P2


def attributes(entity):
    return {a['name']: a['value'] for a in entity.serialize_attributes()}


class LegendProtocolTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    add = fixtures.HgssRulesTests.add

    def rig(self):
        rig = Rig(self.filler, self.filler, self.energies, self.item)
        rig.setup('pokemon')
        return rig

    async def assembled(self, owner=P1):
        rig = self.rig()
        top, bottom = [self.add(rig, definition('HGSS1.LugiaLEGEND_' + str(n)),
                                owner, 'hand') for n in (113, 114)]
        ctx = EffectContext(rig.session, owner, top, None)
        legend = await ctx.put_legend(top, bottom)
        self.assertIsInstance(legend, LegendPokemonEntity)
        return rig, ctx, legend, top, bottom

    def assert_composite(self, legend, top, bottom):
        values = attributes(legend)
        self.assertEqual(values[AttrID.CARD_TYPE], CardType.POKEMON)
        self.assertTrue(values[AttrID.IS_LEGEND])
        self.assertEqual(values[AttrID.STAGE], PokemonStage.LEGEND)
        self.assertEqual(values[AttrID.LEGEND_TOP_HALF], top.entity_id)
        self.assertEqual(values[AttrID.LEGEND_BOTTOM_HALF], bottom.entity_id)
        self.assertTrue(legend.get_entity_name().endswith('.LegendPokemon'))
        self.assertEqual(len({legend.entity_id, top.entity_id, bottom.entity_id}), 3)
        for half in (top, bottom):
            self.assertIs(half.parent, legend)
            self.assertEqual(attributes(half)[AttrID.CARD_TYPE], CardType.LEGEND_HALF)
        self.assertCountEqual(split_pokemon_stack(legend)[0], [top, bottom])
        self.assertNotIn(legend, full_stack(legend))

    async def test_native_zoom_has_one_complete_pair_and_reaches_attachments_both_ways(self):
        # N.V reserves two slots for the combined image (composite + top).
        # Its Children must contain only attachments, not duplicate halves.
        # Both image sources stay in the native entity registry for rendering.
        for owner in (P1, P2):
            with self.subTest(owner=owner):
                rig, ctx, legend, top, bottom = await self.assembled(owner)
                energy = self.add(rig, def_for(next(iter(self.energies.values()))), owner, 'hand')
                rig.attach(energy, legend)
                for viewer in (P1, P2):
                    snapshot = rig.board.serialize(viewer)['entities']
                    registry = {}

                    def collect(entity):
                        self.assertNotIn(entity['entityID'], registry)
                        registry[entity['entityID']] = entity
                        for child in entity['children']:
                            collect(child)

                    collect(snapshot)
                    tree = registry[legend.entity_id]
                    self.assertEqual([c['entityID'] for c in tree['children']], [energy.entity_id])
                    flags = {a['name']: a['value'] for a in tree['attributes']}
                    for attribute, half in ((AttrID.LEGEND_TOP_HALF, top),
                                            (AttrID.LEGEND_BOTTOM_HALF, bottom)):
                        image = registry[flags[attribute]]
                        self.assertEqual(image['archetypeID'], half.archetype_id)
                        self.assertTrue(image['attributes'])
                    zoom = [tree, registry[top.entity_id], registry[energy.entity_id]]

                    def shift(index, direction):
                        # Mirror the native navigation contract, not a server
                        # implementation: test the actual serialized flags.
                        probe = index if direction > 0 or index == 0 else index - 1
                        flags = {a['name']: a['value'] for a in zoom[probe]['attributes']}
                        delta = direction * (2 if flags.get(AttrID.IS_LEGEND) else 1)
                        target = index + delta
                        return target if 0 <= target < len(zoom) else index

                    self.assertEqual(shift(0, 1), 2)
                    self.assertEqual(shift(2, -1), 0)
                    self.assertEqual(shift(2, 1), 2)
                    self.assertEqual(shift(0, -1), 0)

                # Recovery/replay keeps both physical cards and collection tags.
                await ctx.put_in_hand([legend])
                for half in (top, bottom):
                    facet = half.card_obj.to_archetype_attributes(half.card_obj.key)
                    self.assertTrue(facet[str(AttrID.IS_LEGEND.value)]['value'])
                replacement = await ctx.put_legend(bottom, top)
                self.assert_composite(replacement, top, bottom)

    async def test_all_pairs_have_native_render_ids_and_reconnect_tree(self):
        rig = self.rig()
        halves = [self.add(rig, def_for(c.guid), P1, 'hand')
                  for c in loader.cards_by_guid.values()
                  if c.get_attribute_value(AttrID.STAGE) == PokemonStage.LEGEND.value]
        pairs = legend_pairs(halves)
        self.assertGreaterEqual(len(pairs), 9)
        for top, bottom in pairs:
            with self.subTest(card=top.card_obj.key):
                ctx = EffectContext(rig.session, P1, top, None)
                legend = await ctx.put_legend(top, bottom)
                self.assert_composite(legend, top, bottom)
                for viewer in (P1, P2):
                    tree = legend.serialize(viewer)
                    self.assertEqual(tree['children'], [])
                    snapshot = rig.board.serialize(viewer)['entities']
                    out = rig.board.find_global_area('outOfPlay')
                    parked = next(c for c in snapshot['children'] if c['entityID'] == out.entity_id)
                    by_id = {c['entityID']: c for c in parked['children']}
                    for half in (top, bottom):
                        self.assertTrue(by_id[half.entity_id]['attributes'])
                        self.assertEqual(by_id[half.entity_id]['parentID'], out.entity_id)
                    self.assertEqual(tree['parentID'], rig.board.find_player_area(P1, 'bench').entity_id)
                await ctx.put_in_hand([legend])
                self.assertIsNone(rig.board.get_entity(legend.entity_id))

    async def test_creation_introduces_halves_before_composite_for_both_viewers(self):
        rig, ctx, legend, top, bottom = await self.assembled()
        senders = {pid: AsyncMock() for pid in (P1, P2)}
        with patch.object(rig.session.players[P1], 'send_packet', senders[P1]), \
                patch.object(rig.session.players[P2], 'send_packet', senders[P2]):
            await ctx.flush_choreography()
        for sender in senders.values():
            messages = [call.args[1]['msg'] for call in sender.await_args_list]
            names = [m['name'] for m in messages]
            self.assertIn('EntityAdded', names)
            self.assertTrue(any(m['name'] == 'StartSequence' and
                                m['value']['name'] == GameSequence.CREATE_LEGEND.value for m in messages))
            index = next(i for i, m in enumerate(messages) if m['name'] == 'EntityIntroduced'
                         and m['value']['entityID'] == legend.entity_id)
            earlier = messages[:index]
            self.assertEqual({m['value']['entityID'] for m in earlier if m['name'] == 'EntityIntroduced'},
                             {top.entity_id, bottom.entity_id})
            self.assertTrue(any(m['name'] == 'EntityAdded' and m['value']['entityID'] == legend.entity_id
                                for m in earlier))
            moves = [m for m in messages if m['name'] == 'EntityMoved']
            self.assertEqual([m['value']['entityID'] for m in moves],
                             [top.entity_id, bottom.entity_id, legend.entity_id])
            out_id = rig.board.find_global_area('outOfPlay').entity_id
            self.assertEqual([m['value']['destinationID'] for m in moves[:2]], [out_id, out_id])

    async def test_leaving_play_moves_only_physical_cards_then_destroys_wrapper(self):
        for owner in (P1, P2):
            for destination in ('hand', 'deck', 'discard', 'lostZone'):
                with self.subTest(owner=owner, destination=destination):
                    rig, ctx, legend, top, bottom = await self.assembled(owner)
                    energy = self.add(rig, def_for(next(iter(self.energies.values()))), owner, 'hand')
                    rig.attach(energy, legend)
                    await ctx.flush_choreography()
                    if destination == 'hand':
                        await ctx.put_in_hand([legend])
                    elif destination == 'deck':
                        await ctx.shuffle_into_deck([legend], player_id=owner)
                    elif destination == 'discard':
                        await ctx.discard_cards([legend])
                    else:
                        await ctx.move_to_lost_zone([legend])
                    pile = rig.board.find_player_area(owner, destination)
                    for physical in (top, bottom, energy):
                        self.assertIs(physical.parent, pile)
                    self.assertNotIn(legend, pile.children)
                    self.assertIsNone(rig.board.get_entity(legend.entity_id))
                    senders = {pid: AsyncMock() for pid in (P1, P2)}
                    with patch.object(rig.session.players[P1], 'send_packet', senders[P1]), \
                            patch.object(rig.session.players[P2], 'send_packet', senders[P2]):
                        await ctx.flush_choreography()
                    for sender in senders.values():
                        messages = [call.args[1]['msg'] for call in sender.await_args_list]
                        destroys = [i for i, m in enumerate(messages) if m['name'] == 'EntityDestroyed'
                                    and m['value']['entityID'] == legend.entity_id]
                        self.assertEqual(len(destroys), 1)
                        for physical in (top, bottom, energy):
                            moved = [i for i, m in enumerate(messages) if m['name'] == 'EntityMoved'
                                     and m['value']['entityID'] == physical.entity_id]
                            self.assertTrue(moved)
                            self.assertLess(max(moved), destroys[0])
                    self.assertNotIn(legend.entity_id, rig.board.retired_legends)

    async def test_switching_preserves_composite_and_half_identity(self):
        rig, ctx, legend, top, bottom = await self.assembled()
        old_active = rig.board.active_pokemon(P1)
        self.assertTrue(await ctx.switch_active(P1, legend))
        self.assertIs(rig.board.active_pokemon(P1), legend)
        self.assert_composite(legend, top, bottom)
        self.assertTrue(await ctx.switch_active(P1, old_active))
        self.assertIs(legend.parent, rig.board.find_player_area(P1, 'bench'))
        self.assert_composite(legend, top, bottom)
        self.assertEqual(rig.board.retired_legends, {})

    async def test_replaying_uses_new_composite_but_same_two_physical_cards(self):
        rig, ctx, legend, top, bottom = await self.assembled()
        await ctx.flush_choreography()
        await ctx.put_in_hand([legend])
        await ctx.flush_choreography()
        replacement = await ctx.put_legend(bottom, top)
        self.assertNotEqual(legend.entity_id, replacement.entity_id)
        self.assert_composite(replacement, top, bottom)
        self.assertIsNone(rig.board.get_entity(legend.entity_id))

    async def test_paid_retreat_moves_composite_but_not_its_halves(self):
        rig, ctx, legend, top, bottom = await self.assembled()
        replacement = rig.board.active_pokemon(P1)
        await ctx.switch_active(P1, legend)
        await ctx.flush_choreography()
        cost = effective_retreat_cost(rig.board, legend)
        self.assertGreater(cost, 0)
        energies = [self.add(rig, def_for(self.energies[PokemonTypes.WATER]), P1, 'hand')
                    for _ in range(cost)]
        for energy in energies:
            rig.attach(energy, legend)
        entry = {'_autoRetreatEnergyIDs': [e.entity_id for e in energies],
                 'targetInfoLst': [{'name': SelectionKind.RETREAT_NEW_ACTIVE.value,
                                    'validTargets': [replacement.entity_id]}]}
        await rig.session._execute_retreat(P1, legend, entry, [replacement.entity_id])
        self.assertIs(rig.board.active_pokemon(P1), replacement)
        self.assertTrue(rig.session.turn_state.retreated)
        self.assertIs(legend.parent, rig.board.find_player_area(P1, 'bench'))
        self.assert_composite(legend, top, bottom)
        self.assertTrue(all(e.parent is rig.board.find_player_area(P1, 'discard') for e in energies))
        self.assertEqual(rig.board.retired_legends, {})

    async def test_composite_attacks_and_discards_energy_without_detaching_halves(self):
        rig, ctx, legend, top, bottom = await self.assembled()
        await ctx.switch_active(P1, legend)
        await ctx.flush_choreography()
        energies = []
        for kind in (PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING):
            energy = self.add(rig, def_for(self.energies[kind]), P1, 'hand')
            rig.attach(energy, legend)
            energies.append(energy)
        ability = next(a for a in def_for(legend.archetype_id).abilities if a.title == 'Elemental Blast')
        attack = EffectContext(rig.session, P1, legend, ability)
        defender = rig.board.active_pokemon(P2)
        before = defender.get_attribute(AttrID.HP)
        await ability.effect(attack)
        await attack.flush_choreography()
        self.assertLess(defender.get_attribute(AttrID.HP), before)
        self.assertTrue(all(e.parent is rig.board.find_player_area(P1, 'discard') for e in energies))
        self.assert_composite(legend, top, bottom)
        self.assertEqual(rig.board.retired_legends, {})

    async def test_knockout_awards_prizes_once_and_retires_render_entity(self):
        for set_code, name, numbers, prizes in (
                ('HGSS1', 'LugiaLEGEND', (113, 114), 1),
                ('HGSS2', 'SuicuneEnteiLEGEND', (94, 95), 2)):
            with self.subTest(legend=name):
                rig = self.rig()
                halves = [self.add(rig, definition(f'{set_code}.{name}_{n}'), P1, 'hand')
                          for n in numbers]
                ctx = EffectContext(rig.session, P1, halves[0], None)
                legend = await ctx.put_legend(*halves)
                await ctx.switch_active(P1, legend)
                await ctx.flush_choreography()
                damage = EffectContext(rig.session, P2, rig.board.active_pokemon(P2), None)
                with patch.object(rig.session, '_take_prizes', AsyncMock()) as take_prizes:
                    await damage.deal_damage(1000, target=legend)
                    await rig.session.resolve_knockouts(damage)
                self.assertEqual(take_prizes.await_count, 1)
                self.assertEqual(take_prizes.await_args.args[:2], (P2, prizes))
                self.assertIsNotNone(rig.board.active_pokemon(P1))
                self.assertIsNone(rig.board.get_entity(legend.entity_id))
                self.assertTrue(all(c.parent is rig.board.find_player_area(P1, 'discard') for c in halves))
                self.assertEqual(rig.board.retired_legends, {})
