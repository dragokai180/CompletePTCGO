"""Two physical cards, one LEGEND Pokemon: legal play and zone transitions."""
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, CardType, GameSequence, PokemonStage, PokemonTypes
from spirit.game.scripts.cards import loader
from spirit.game.models.board import LegendPokemonEntity
from spirit.game.game_sequence_packets import NestedSequence
from spirit.game.data_utils import def_for, prize_value
from spirit.game.legend import complementary_halves
from spirit.game.session.effects import EffectContext, full_stack, is_evolution_pokemon, split_pokemon_stack
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.game.session.passives import compute_damage
from spirit.tools.effect_smoke import P1, P2


# Reuse fixtures without inheriting (and duplicating) the older test methods.
class LegendTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def pair(self, rig, zone='hand'):
        return [self.add(rig, definition('HGSS1.LugiaLEGEND_' + str(n)), P1, zone)
                for n in (113, 114)]

    def assert_client_half(self, attributes):
        values = {a['name']: a['value'] for a in attributes}
        self.assertEqual(values[AttrID.STAGE.value], PokemonStage.LEGEND.value)
        self.assertEqual(values[AttrID.CARD_TYPE.value], CardType.LEGEND_HALF.value)
        # Native k.P.ConfigureLegendary skips this branch ONLY for LegendHalf.
        # Otherwise its missing 201670/201680 IDs crash the initial deal.
        self.assertFalse(values.get(201030, False) and
                         values[AttrID.CARD_TYPE.value] != CardType.LEGEND_HALF.value)

    def test_every_legend_print_has_safe_archetype_and_entity_attributes(self):
        cards = [c for c in loader.cards_by_guid.values()
                 if c.get_attribute_value(AttrID.STAGE) == PokemonStage.LEGEND.value]
        self.assertGreaterEqual(len(cards), 18)
        from spirit.game.models.board import create_card_entity
        for card in cards:
            with self.subTest(card=card.key):
                archetype = card.to_archetype_attributes(card.key)
                self.assertEqual(archetype[str(AttrID.CARD_TYPE.value)]['value'],
                                 CardType.LEGEND_HALF.value)
                entity = create_card_entity(card, P1)
                self.assert_client_half(entity.serialize_attributes())
                self.assertTrue(entity.get_entity_name().endswith('.HalfLegend'))
                # Do not change rules-side Pokemon classification or state.
                self.assertEqual(entity.get_attribute(AttrID.CARD_TYPE), CardType.POKEMON.value)
                self.assertEqual(card.get_attribute_value(AttrID.CARD_TYPE), CardType.POKEMON.value)

    async def test_opening_deal_with_half_uses_safe_introduction_before_animation(self):
        for number in (113, 114):
            with self.subTest(half=number):
                rig, e = self.rig('HGSS1.LugiaLEGEND_113')
                for pid in (P1, P2):
                    for zone in ('hand', 'deck'):
                        for card in list(rig.board.find_player_area(pid, zone).children):
                            rig.to_area(card, pid, 'discard')
                    # Reproduce the report: a LEGEND half and six Energy
                    # cards form a mulligan, while the other hand is valid.
                    filler = def_for(next(iter(self.energies.values()))) if pid == P1 else self.filler
                    for _ in range(6):
                        self.add(rig, filler, pid, 'deck')
                half = self.add(rig, definition('HGSS1.LugiaLEGEND_' + str(number)), P1, 'deck')
                self.add(rig, self.filler, P2, 'deck')
                sender = AsyncMock()
                with patch.object(rig.session.players[P1], 'send_packet', sender), \
                        patch.object(rig.session, '_broadcast_shuffle_deck', AsyncMock()), \
                        patch.object(rig.session, 'send_game_sequence', AsyncMock()), \
                        patch('spirit.game.session.game_session.asyncio.sleep', AsyncMock()):
                    await rig.session.run_setup_phase()
                self.assertIs(half.parent, rig.board.find_player_area(P1, 'hand'))
                introductions = []
                def visit(value):
                    if isinstance(value, dict):
                        if value.get('entityID') == half.entity_id and 'attributeMap' in value:
                            introductions.append(value)
                        for item in value.values():
                            visit(item)
                    elif isinstance(value, (list, tuple)):
                        for item in value:
                            visit(item)
                for call in sender.await_args_list:
                    visit(call.args)
                self.assertEqual(len(introductions), 1)
                self.assert_client_half(introductions[0]['attributeMap'])
                # Same snapshot is used by the mulligan carousel. Opponents
                # still cannot see the owner's hand outside that reveal.
                self.assert_client_half(half.serialize(P1)['attributes'])
                self.assertIsNone(half.serialize(P2)['attributes'])
                self.assertFalse(rig.board.setup_active_candidates(P1))
                snapshot = {c.entity_id: c.serialize_attributes()
                            for c in rig.board.find_player_area(P1, 'hand').children}
                with patch.object(rig.session, 'send_game_sequence', AsyncMock()) as reveal:
                    await rig.session._reveal_mulligans({P1: [snapshot]})
                effect = reveal.await_args.args[2][0]
                # The snapshot passed to both viewers uses the same safe type.
                def find_piles(value):
                    if isinstance(value, dict):
                        if 'entityIDPiles' in value:
                            return value['entityIDPiles']
                        for child in value.values():
                            found = find_piles(child)
                            if found is not None:
                                return found
                    return None
                self.assert_client_half(find_piles(effect)[0][half.entity_id])

    async def test_legend_knockout_uses_safe_movement_and_promotes(self):
        rig, e = self.rig('HGSS1.LugiaLEGEND_113')
        first, second = self.pair(rig)
        ctx = EffectContext(rig.session, P1, first, None)
        legend = await ctx.put_legend(first, second)
        self.assertIsInstance(legend, LegendPokemonEntity)
        rig.to_area(rig.board.active_pokemon(P1), P1, 'discard')
        rig.to_area(legend, P1, 'activePokemonArea')
        attacker = rig.board.active_pokemon(P2)
        damage = EffectContext(rig.session, P2, attacker, None)
        with patch.object(rig.session, 'send_game_sequence', AsyncMock()) as sequences, \
                patch.object(rig.session, '_take_prizes', AsyncMock()):
            await damage.deal_damage(1000, target=legend)
            await rig.session.resolve_knockouts(damage)
        self.assertEqual(sequences.await_args_list[0].args[1], GameSequence.GROUPED_MOVE)
        self.assertIsNotNone(rig.board.active_pokemon(P1))
        for half in (first, second):
            self.assertIs(half.parent, rig.board.find_player_area(P1, 'discard'))
            self.assert_client_half(half.serialize_attributes())

    async def test_only_complementary_halves_are_playable(self):
        rig, e = self.rig('HGSS1.LugiaLEGEND_113')
        first = self.add(rig, definition('HGSS1.LugiaLEGEND_113'), P1, 'hand')
        duplicate = self.add(rig, definition('HGSS1.LugiaLEGEND_113'), P1, 'hand')
        def offered():
            return {entry['entityID'] for entry in compute_legal_actions(
                rig.board, rig.session.turn_state, P1, rig.session.game_id)}
        self.assertFalse(complementary_halves(first, duplicate))
        self.assertNotIn(first.entity_id, offered())
        second = self.add(rig, definition('HGSS1.LugiaLEGEND_114'), P1, 'hand')
        self.assertIn(first.entity_id, offered())
        self.assertIn(second.entity_id, offered())
        for _ in range(2):
            self.add(rig, self.filler, P1, 'bench')
        self.assertNotIn(first.entity_id, offered())

    async def test_manual_pair_play_from_either_half(self):
        for clicked in (0, 1):
            with self.subTest(clicked=clicked):
                rig, e = self.rig('HGSS1.LugiaLEGEND_113')
                first, second = self.pair(rig)
                rig.session._fire_triggered_abilities = AsyncMock(return_value=False)
                rig.session.fire_pokemon_benched_triggers = AsyncMock()
                await rig.session._execute_play_basic(P1, (first, second)[clicked])
                legend = first.parent
                self.assertIsInstance(legend, LegendPokemonEntity)
                self.assertIs(legend.parent, rig.board.find_player_area(P1, 'bench'))
                self.assertIs(second.parent, legend)
                self.assertEqual(len(rig.board.pokemon_in_play(P1)), 5)
                self.assertIn(legend.entity_id, rig.session.turn_state.entered_play_turn)
                rig.session._fire_triggered_abilities.assert_awaited_once()
                self.assertIs(rig.session._fire_triggered_abilities.await_args.args[1], legend)
                rig.session.fire_pokemon_benched_triggers.assert_not_awaited()

    async def test_pair_validation_is_atomic(self):
        rig, e = self.rig('HGSS1.LugiaLEGEND_113')
        first, second = self.pair(rig)
        ctx = EffectContext(rig.session, P1, first, None)
        rig.to_area(second, P1, 'deck')
        self.assertFalse(await ctx.put_legend(first, second))
        self.assertIs(first.parent, rig.board.find_player_area(P1, 'hand'))
        rig.to_area(second, P1, 'hand')
        for _ in range(2):
            self.add(rig, self.filler, P1, 'bench')
        self.assertFalse(await ctx.put_legend(first, second))
        self.assertIs(second.parent, first.parent)

    async def test_legend_is_not_evolution_but_both_halves_return(self):
        rig, e = self.rig('HGSS1.LugiaLEGEND_113')
        first, second = self.pair(rig)
        ctx = EffectContext(rig.session, P1, first, None)
        legend = await ctx.put_legend(first, second)
        self.assertIsInstance(legend, LegendPokemonEntity)
        self.assertFalse(is_evolution_pokemon(legend))
        self.assertIsNone(await rig.session.perform_devolution(legend))
        line, attachments = split_pokemon_stack(legend)
        self.assertCountEqual(line, [first, second])
        self.assertEqual(attachments, [])
        await ctx.put_in_hand(line)
        self.assertIsNone(rig.board.get_entity(legend.entity_id))
        self.assertTrue(all(c.parent is rig.board.find_player_area(P1, 'hand') for c in line))
        for half in line:
            self.assert_client_half(half.serialize_attributes())

    async def test_prizes_and_dual_weakness(self):
        for path, count in [('HGSS1.LugiaLEGEND_113', 1), ('HGSS1.HoOhLEGEND_111', 1),
                            ('HGSS2.SuicuneEnteiLEGEND_94', 2)]:
            self.assertEqual(prize_value(definition(path).guid), count)
        rig, e = self.rig('HGSS2.RaikouSuicuneLEGEND_92')
        defender = self.add(rig, definition('HGSS2.SuicuneEnteiLEGEND_94'), P2, 'bench')
        rig.to_area(e['p2_active'], P2, 'discard')
        rig.to_area(defender, P2, 'activePokemonArea')
        self.assertEqual(compute_damage(rig.board, e['target'], defender, 30).amount, 120)
        e['target'].set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        self.assertEqual(compute_damage(rig.board, e['target'], defender, 30).amount, 60)

    async def test_legend_box_rejects_duplicate_half_and_uses_real_capacity(self):
        for mode in ('duplicate', 'full', 'valid'):
            with self.subTest(mode=mode):
                rig, e = self.rig('HGSS3.LegendBox_75', 'trainer')
                deck = rig.board.find_player_area(P1, 'deck')
                for card in list(deck.children):
                    rig.to_area(card, P1, 'discard')
                first, second = self.pair(rig, 'deck')
                if mode == 'duplicate':
                    rig.to_area(second, P1, 'discard')
                    second = self.add(rig, definition('HGSS1.LugiaLEGEND_113'), P1, 'deck')
                if mode == 'full':
                    while len(rig.board.find_player_area(P1, 'bench').children) < 5:
                        self.add(rig, self.filler, P1, 'bench')
                rig.session._fire_triggered_abilities = AsyncMock(return_value=False)
                ctx = EffectContext(rig.session, P1, e['target'], None)
                await definition('HGSS3.LegendBox_75').effect(ctx)
                if mode == 'valid':
                    self.assertIsInstance(first.parent, LegendPokemonEntity)
                    self.assertIs(second.parent, first.parent)
                    rig.session._fire_triggered_abilities.assert_awaited_once()
                else:
                    self.assertIs(first.parent, deck)
                    self.assertIs(second.parent, deck)
                    rig.session._fire_triggered_abilities.assert_not_awaited()
