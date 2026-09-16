"""Repeat hand attachment Abilities without replaying their source animation."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, GameSequence, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import resolve_activated_ability, is_energy_card
from spirit.tools.effect_smoke import P1, P2


class RepeatableEnergyAttachmentTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_case(self, path, title, kind, owner=P1):
        rig, e = self.rig(path)
        source = e['target']
        if owner == P2:
            rig.to_area(rig.board.active_pokemon(P2), P2, 'deck')
            rig.to_area(source, P2, 'activePokemonArea')
            source.owning_player_id = P2
        rig.session.turn_state.active_player_id = owner
        hand = rig.board.find_player_area(owner, 'hand')
        for card in list(hand.children):
            rig.to_area(card, owner, 'deck')
        energies = [self.add(rig, def_for(self.energies[kind.value]), owner, 'hand')
                    for _ in range(2)]
        ability = next(a for a in fixtures.definition(path).abilities if a.title == title)
        return rig, source, ability, energies

    def record(self, rig):
        events = {P1: [], P2: []}

        async def send(players, bracket, messages):
            for pid, viewer in rig.session.players.items():
                if viewer not in players:
                    continue
                for msg in messages:
                    name, value = msg.get('name', ''), msg.get('value', {})
                    if name.endswith('EntityMoved'):
                        events[pid].append(('move', value['entityID'], bracket))
                    if name.endswith('AbilityPlayedEffect'):
                        events[pid].append(('ability', value['eID'], bracket))
        rig.session.send_game_sequence = AsyncMock(side_effect=send)
        return events

    async def test_loop_flushes_each_attachment_then_announces_once_for_both_players(self):
        for owner in (P1, P2):
            with self.subTest(owner=owner):
                rig, source, ability, energies = self.setup_case(
                    'BW1.Emboar_20', 'Inferno Fandango', PokemonTypes.FIRE, owner)
                events = self.record(rig)
                seen = []

                async def pick(pid, source_id, cards, count, minimum, prompt):
                    if is_energy_card(cards[0]):
                        self.assertEqual(minimum, 0)
                        for previous in seen:
                            for viewer in (P1, P2):
                                self.assertIn(('move', previous, GameSequence.GROUPED_MOVE.value),
                                              events[viewer])
                        self.assertFalse(any(x[0] == 'ability' for x in events[owner]))
                        seen.append(cards[0].entity_id)
                    return [cards[0].entity_id]

                rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
                rig.session.fire_energy_attached_triggers = AsyncMock()
                rig.session.turn_state.energy_attached = True
                ctx = await resolve_activated_ability(rig.session, owner, source, ability)
                self.assertEqual(seen, [e.entity_id for e in energies])
                self.assertTrue(all(e not in ctx.hand() for e in energies))
                self.assertEqual(rig.session.fire_energy_attached_triggers.await_count, 2)
                self.assertFalse(ctx._messages)
                self.assertFalse(ctx.deferred_actions)
                for viewer in (P1, P2):
                    self.assertEqual([x[0] for x in events[viewer]],
                                     ['move', 'move', 'ability'])

    async def test_done_stops_before_or_after_first_attachment(self):
        for limit in (0, 1):
            rig, source, ability, energies = self.setup_case(
                'BW7.Blastoise_31', 'Deluge', PokemonTypes.WATER)
            events = self.record(rig)
            selected = 0

            async def pick(pid, source_id, cards, count, minimum, prompt):
                nonlocal selected
                if is_energy_card(cards[0]):
                    self.assertEqual(minimum, 0)
                    if selected >= limit:
                        return []
                    selected += 1
                return [cards[0].entity_id]

            rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
            ctx = await resolve_activated_ability(rig.session, P1, source, ability)
            self.assertEqual(sum(e in ctx.hand() for e in energies), 2 - limit)
            self.assertEqual(sum(x[0] == 'ability' for x in events[P1]), limit)

    async def test_variants_loop_and_preserve_their_target_restrictions(self):
        cases = (
            ('BW4.Emboar_100', 'Inferno Fandango', PokemonTypes.FIRE),
            ('BW10.Blastoise_16', 'Deluge', PokemonTypes.WATER),
            ('HGSS1.Feraligatr_108', 'Rain Dance', PokemonTypes.WATER),
            ('XY8.Magnezone_54', 'Magnetic Circuit', PokemonTypes.LIGHTNING),
            ('SWSH1.Frosmoth_64', 'Ice Dance', PokemonTypes.WATER),
            ('SWSH2.Frosmoth_204', 'Ice Dance', PokemonTypes.WATER),
            ('SWSH45.Frosmoth_30', 'Ice Dance', PokemonTypes.WATER),
            ('SWSH5.Cherrim_8', 'Spring Bloom', PokemonTypes.GRASS),
            ('ME2.Oricorioex_18', 'Excited Turbo', PokemonTypes.FIRE),
            ('MEP.Oricorioex_24', 'Excited Turbo', PokemonTypes.FIRE),
            ('RSV10PT5.Emboar_13', 'Inferno Fandango', PokemonTypes.FIRE),
            ('SV2.Baxcalibur_60', 'Super Cold', PokemonTypes.WATER),
            ('SV09.IonosBelliboltex_53', 'Electric Streamer', PokemonTypes.LIGHTNING),
            ('SWSH3.Hydreigon_110', 'Dark Squall', PokemonTypes.DARKNESS),
        )
        for path, title, kind in cases:
            with self.subTest(path=path):
                rig, source, ability, energies = self.setup_case(path, title, kind)
                bench = rig.board.find_player_area(P1, 'bench').children
                if title in ('Ice Dance', 'Excited Turbo'):
                    for p in bench:
                        p.set_attribute(AttrID.POKEMON_TYPES, [kind.value])
                    if title == 'Excited Turbo':
                        self.add(rig, fixtures.definition('ME2.MegaCharizardXex_13'),
                                 P1, 'bench')

                async def pick(pid, source_id, cards, count, minimum, prompt):
                    if not is_energy_card(cards[0]):
                        if title in ('Ice Dance', 'Excited Turbo'):
                            self.assertTrue(all(p in bench for p in cards))
                        if title == 'Rain Dance':
                            self.assertTrue(all(kind.value in p.get_attribute(AttrID.POKEMON_TYPES)
                                                for p in cards))
                    return [cards[0].entity_id]

                rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
                ctx = await resolve_activated_ability(rig.session, P1, source, ability)
                self.assertTrue(all(e not in ctx.hand() for e in energies))

    async def test_crazy_code_repeats_only_special_energy(self):
        rig, source, ability, basic = self.setup_case(
            'SM10.PorygonZ_157', 'Crazy Code', PokemonTypes.WATER)
        special = [self.add(rig, fixtures.definition('HGSS1.DoubleColorlessEnergy_103'),
                            P1, 'hand') for _ in range(2)]
        rig.session.prompt_entity_picker = AsyncMock(
            side_effect=lambda pid, sid, cards, *args: [cards[0].entity_id])
        ctx = await resolve_activated_ability(rig.session, P1, source, ability)
        self.assertTrue(all(e in ctx.hand() for e in basic))
        self.assertTrue(all(e not in ctx.hand() for e in special))

    async def test_one_use_attachment_does_not_enter_the_loop(self):
        rig, source, ability, energies = self.setup_case(
            'HGSS2.Floatzel_16', 'Water Acceleration', PokemonTypes.WATER)
        rig.session.prompt_entity_picker = AsyncMock(
            side_effect=lambda pid, sid, cards, *args: [cards[0].entity_id])
        ctx = await resolve_activated_ability(rig.session, P1, source, ability)
        self.assertEqual(sum(e in ctx.hand() for e in energies), 1)
        self.assertFalse(ctx.completed_attachment_loop)

    async def test_attachment_observer_resolves_before_next_pick(self):
        rig, source, ability, energies = self.setup_case(
            'BW7.Blastoise_31', 'Deluge', PokemonTypes.WATER)
        events = []
        async def pick(pid, sid, cards, *args):
            if is_energy_card(cards[0]):
                events.append('pick')
            return [cards[0].entity_id]
        async def trigger(*args):
            events.append('trigger')
        rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
        rig.session.fire_energy_attached_triggers = AsyncMock(side_effect=trigger)
        ctx = await resolve_activated_ability(rig.session, P1, source, ability)
        self.assertEqual(events, ['pick', 'trigger', 'pick', 'trigger'])
        self.assertFalse(ctx.deferred_actions)

    async def test_no_matching_energy_exits_without_another_prompt(self):
        rig, source, ability, energies = self.setup_case(
            'BW7.Blastoise_31', 'Deluge', PokemonTypes.WATER)
        fire = self.add(rig, def_for(self.energies[PokemonTypes.FIRE.value]), P1, 'hand')
        rig.session.prompt_entity_picker = AsyncMock(
            side_effect=lambda pid, sid, cards, *args: [cards[0].entity_id])
        ctx = await resolve_activated_ability(rig.session, P1, source, ability)
        self.assertEqual(ctx.hand(), [fire])
        self.assertTrue(all(e not in ctx.hand() for e in energies))


if __name__ == '__main__':
    unittest.main()
