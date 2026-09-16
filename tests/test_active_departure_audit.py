"""Audit Active departures, delayed damage and native message ordering."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, GameSequence, PokemonTypes, SpecialConditions
from spirit.game.data_utils import Attack, ABILITIES_BY_ID
from spirit.game.game_sequence_packets import NestedSequence
from spirit.game.session.effects import EffectContext, full_stack, resolve_attack
from spirit.tools.effect_smoke import P1, P2, GameOver

SESSION = 'spirit.game.session.game_session'


class ActiveDepartureAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def setup_case(self, reaction=None, owner=P1):
        rig, e = self.rig('BW5.Accelgor_11')
        attacker = e['target']
        if owner != P1:
            rig.to_area(rig.board.active_pokemon(owner), owner, 'hand')
            rig.to_area(attacker, owner, 'activePokemonArea')
            attacker.owning_player_id = owner
            self.add(rig, self.filler, P1, 'activePokemonArea')
        rig.session.turn_state.active_player_id = owner
        opponent = P2 if owner == P1 else P1
        rig.to_area(rig.board.active_pokemon(opponent), opponent, 'hand')
        defender = self.add(rig, fixtures.definition('BW3.Druddigon_89'),
                            opponent, 'activePokemonArea')
        # Only the selected reaction is enabled.
        if reaction != 'skin':
            defender.set_attribute(AttrID.PIE_ABILITIES, [])
            # Rough Skin is a passive on the definition; use an ordinary Basic.
            rig.to_area(defender, opponent, 'hand')
            defender = self.add(rig, self.filler, opponent, 'activePokemonArea')
            defender.set_attribute(AttrID.HP, 200)
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
        if reaction in ('horror', 'helmet'):
            path = ('SWSH2.HorrorPsychicEnergy_172' if reaction == 'horror'
                    else 'SWSH4.RockyHelmet_159')
            attached = self.add(rig, fixtures.definition(path), opponent, 'hand')
            rig.attach(attached, defender)
            if reaction == 'horror':
                defender.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.PSYCHIC.value])
            await rig.session.refresh_granted_abilities(defender)
        attack = fixtures.definition('BW5.Accelgor_11').abilities[1]
        return rig, attacker, defender, attack

    def record_native_moves(self, rig, viewer_id=P1):
        locations = {}
        for pid in (P1, P2):
            for area_name in ('activePokemonArea', 'bench', 'hand', 'deck', 'discard', 'lostZone'):
                area = rig.board.find_player_area(pid, area_name)
                if area:
                    for card in area.children:
                        locations[card.entity_id] = area.entity_id
        fields = {rig.board.find_player_area(pid, name).entity_id
                  for pid in (P1, P2) for name in ('activePokemonArea', 'bench')}
        events = []

        def consume(msg):
            if isinstance(msg, NestedSequence):
                for child in msg.messages:
                    consume(child)
                return
            name, value = msg.get('name', ''), msg.get('value', {})
            if name.endswith('EntityMoved'):
                locations[value['entityID']] = value['destinationID']
                events.append(('move', value['entityID']))
            if name.endswith('PlaceDamageEffect'):
                entity_id = value['destinationID']
                self.assertIn(locations.get(entity_id), fields,
                              'The native damage animator cannot hit an out-of-play pile')
                events.append(('damage', entity_id))

        async def send(players, name, messages):
            if rig.session.players[viewer_id] in players:
                for msg in messages:
                    consume(msg)
        return AsyncMock(side_effect=send), events

    async def test_deck_and_cover_reactions_do_not_damage_shuffled_attacker(self):
        for reaction in (None, 'skin', 'horror', 'helmet'):
            for owner in (P1, P2):
                with self.subTest(reaction=reaction, owner=owner):
                    rig, attacker, defender, attack = await self.setup_case(reaction, owner)
                    stack = list(full_stack(attacker))
                    sender, events = self.record_native_moves(rig, owner)
                    rig.session.send_game_sequence = sender
                    ended = await rig.session._execute_attack(
                        owner, attacker, {'selectableAction': {'actionID': attack.ability_id}})
                    self.assertTrue(ended)
                    self.assertIsNotNone(rig.board.active_pokemon(owner))
                    self.assertIsNot(rig.board.active_pokemon(owner), attacker)
                    self.assertTrue(all(c in rig.board.find_player_area(owner, 'deck').children
                                        for c in stack))
                    self.assertEqual(attacker.get_attribute(AttrID.HP),
                                     attacker.attribute_originals[AttrID.HP.value])
                    self.assertNotIn(('damage', attacker.entity_id), events)

    async def test_human_selects_second_replacement_after_deck_and_cover(self):
        rig, attacker, _, attack = await self.setup_case('horror')
        bench = list(rig.board.find_player_area(P1, 'bench').children)
        chosen = bench[-1]
        original = rig.session._promote_new_active

        async def promote(pid):
            with patch(SESSION + '.AIPlayer', type('NotAI', (), {})):
                return await original(pid)

        async def reply(player, message, offer, **kwargs):
            self.assertIsNone(rig.board.active_pokemon(P1))
            self.assertEqual(set(offer['targetMap']), {p.entity_id for p in bench})
            self.assertIn(attacker, rig.board.find_player_area(P1, 'deck').children)
            return {'selection': {'entityID': chosen.entity_id}}

        with patch.object(rig.session, '_promote_new_active', side_effect=promote), \
                patch.object(rig.session, 'prompt_selection_message', side_effect=reply) as prompt:
            await rig.session._execute_attack(P1, attacker,
                {'selectableAction': {'actionID': attack.ability_id}})
        prompt.assert_awaited_once()
        self.assertIs(rig.board.active_pokemon(P1), chosen)

    async def test_last_attacker_leaving_field_loses_without_prizes(self):
        rig, attacker, _, attack = await self.setup_case()
        for card in list(rig.board.find_player_area(P1, 'bench').children):
            rig.to_area(card, P1, 'hand')
        with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
            with self.assertRaises(GameOver):
                await rig.session._execute_attack(P1, attacker,
                    {'selectableAction': {'actionID': attack.ability_id}})
        prizes.assert_not_awaited()

    async def test_single_replacement_is_automatic_after_attack(self):
        rig, attacker, _, attack = await self.setup_case()
        bench = list(rig.board.find_player_area(P1, 'bench').children)
        for card in bench[1:]:
            rig.to_area(card, P1, 'hand')
        with patch.object(rig.session, 'prompt_selection_message', AsyncMock()) as prompt:
            await rig.session._execute_attack(P1, attacker,
                {'selectableAction': {'actionID': attack.ability_id}})
        prompt.assert_not_awaited()
        self.assertIs(rig.board.active_pokemon(P1), bench[0])

    async def test_simultaneous_departures_promote_non_turn_player_first(self):
        for owner in (P1, P2):
            rig, attacker, _, _ = await self.setup_case(owner=owner)

            async def remove_actives(ctx):
                for pid in (P1, P2):
                    await ctx.shuffle_into_deck(full_stack(ctx.board.active_pokemon(pid)), pid)

            attack = Attack('Both depart audit', effect=remove_actives)
            key = 'audit-both-depart'
            with patch.dict(ABILITIES_BY_ID, {key: attack}), \
                    patch.object(rig.session, '_promote_new_active',
                                 wraps=rig.session._promote_new_active) as promote:
                await rig.session._execute_attack(owner, attacker,
                    {'selectableAction': {'actionID': key}})
            other = P2 if owner == P1 else P1
            self.assertEqual([call.args[0] for call in promote.await_args_list], [other, owner])

    async def test_recoil_on_benched_attacker_remains_valid(self):
        rig, attacker, _, _ = await self.setup_case('horror')
        replacement = rig.board.find_player_area(P1, 'bench').children[-1]

        async def attack_then_switch(ctx):
            await ctx.deal_damage(10)
            await ctx.switch_active(P1, replacement)

        attack = Attack('Hit and switch audit', damage=10, effect=attack_then_switch)
        before = attacker.get_attribute(AttrID.HP)
        sender, events = self.record_native_moves(rig)
        rig.session.send_game_sequence = sender
        await resolve_attack(rig.session, P1, attacker, attack, 'audit-hit-switch')
        self.assertEqual(attacker.get_attribute(AttrID.HP), before - 20)
        self.assertIs(rig.board.active_pokemon(P1), replacement)
        self.assertIn(('damage', attacker.entity_id), events)

    async def test_lethal_reaction_animates_before_discard_and_promotion(self):
        for reaction in ('skin', 'horror', 'helmet'):
            with self.subTest(reaction=reaction):
                rig, attacker, _, _ = await self.setup_case(reaction)
                attacker.set_attribute(AttrID.HP, 10)
                attack = Attack('Stay in play', damage=10)
                sender, events = self.record_native_moves(rig)
                rig.session.send_game_sequence = sender
                with patch.object(rig.session, '_take_prizes', AsyncMock()):
                    await resolve_attack(rig.session, P1, attacker, attack, 'audit-hit')
                self.assertIn(attacker, rig.board.find_player_area(P1, 'discard').children)
                self.assertIsNotNone(rig.board.active_pokemon(P1))
                self.assertLess(events.index(('damage', attacker.entity_id)),
                                events.index(('move', attacker.entity_id)))

    async def test_departure_primitives_do_not_allow_stale_damage_or_status(self):
        for zone in ('hand', 'deck', 'discard', 'lostZone'):
            rig, attacker, _, _ = await self.setup_case()
            ctx = EffectContext(rig.session, P2, rig.board.active_pokemon(P2), None)
            rig.to_area(attacker, P1, zone)
            before = attacker.get_attribute(AttrID.HP)
            self.assertEqual(await ctx.deal_damage(20, attacker, as_counters=True), 0)
            self.assertFalse(await ctx.knock_out(attacker))
            self.assertFalse(await ctx.apply_special_condition(attacker, SpecialConditions.POISONED))
            self.assertEqual(attacker.get_attribute(AttrID.HP), before)
            self.assertFalse(ctx._messages)
            ctx.knockouts.append(attacker)
            with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
                await rig.session.resolve_knockouts(ctx)
            prizes.assert_not_awaited()
            self.assertEqual(attacker.parent.get_attribute(AttrID.NAME), zone)

    async def test_return_to_hand_moves_entire_stack_after_attack_bracket(self):
        rig, attacker, _, _ = await self.setup_case('horror')
        stack = list(full_stack(attacker))

        async def leave(ctx):
            await ctx.deal_damage(10)
            await ctx.put_in_hand(full_stack(ctx.attacker), reveal=False)

        attack = Attack('Return audit', damage=10, effect=leave)
        sender, events = self.record_native_moves(rig)
        rig.session.send_game_sequence = sender
        await resolve_attack(rig.session, P1, attacker, attack, 'return-audit')
        await rig.session._settle_empty_active_spots()
        for call in sender.await_args_list:
            if call.args[1] == GameSequence.ATTACK:
                for msg in call.args[2]:
                    if isinstance(msg, dict):
                        self.assertFalse(msg.get('name', '').endswith('EntityMoved'))
        self.assertTrue(all(c in rig.board.find_player_area(P1, 'hand').children for c in stack))
        self.assertIsNotNone(rig.board.active_pokemon(P1))
        self.assertNotIn(('damage', attacker.entity_id), events)
