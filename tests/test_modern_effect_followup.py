"""Effect outcomes, legal targets, source visibility and complete follow-ups."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext, resolve_activated_ability
from spirit.game.session.legal_actions import ability_condition_met, compute_legal_actions
from spirit.game.session.passives import effective_max_hp
from spirit.tools.effect_smoke import P1, P2


class ModernEffectFollowupTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def card(self, rig, path, owner=P1, zone='hand'):
        return self.add(rig, fixtures.definition(path), owner, zone)

    def ability(self, card, title):
        return next(a for a in CARD_DEFS_BY_GUID[card.archetype_id].abilities if a.title == title)

    def offered(self, rig, card, ability, owner=P1):
        return any(a['entityID'] == card.entity_id and a['selectableAction']['actionID'] == ability.ability_id
                   for a in compute_legal_actions(rig.board, rig.session.turn_state, owner, rig.session.game_id))

    def empty(self, rig, zone, owner=P1):
        for c in list(rig.board.find_player_area(owner, zone).children):
            rig.to_area(c, owner, 'deck' if zone != 'deck' else 'discard')

    async def test_artazon_all_prints_both_players_filter_rule_boxes_and_evolutions(self):
        for d in [d for d in CARD_DEFS_BY_GUID.values() if d.display_name == 'Artazon']:
            for owner in (P1, P2):
                with self.subTest(print=d.guid, owner=owner):
                    rig, e = self.rig('BW1.Snivy_1')
                    stadium = self.add(rig, d, P1, 'hand')
                    rig.board.move_card(stadium.entity_id, rig.board.find_global_area('activeStadium').entity_id)
                    ctx = EffectContext(rig.session, owner, stadium, d.ability)
                    good = self.card(rig, 'BW1.Snivy_1', owner, 'deck')
                    invalid = [self.card(rig, p, owner, 'deck') for p in
                               ['SV1.Gardevoirex_86', 'XY5.GroudonEX_85', 'BW1.Servine_3']]
                    ctx.choose_cards = AsyncMock(return_value=[good])
                    await d.ability.effect(ctx)
                    self.assertIn(good, ctx.my_bench())
                    pool = ctx.choose_cards.call_args.args[0]
                    self.assertIn(good, pool)
                    self.assertTrue(all(c not in pool for c in invalid))
                    self.assertEqual(ctx.choose_cards.call_args.kwargs['minimum'], 0)
                    self.assertEqual(ctx.choose_cards.call_args.kwargs['player_id'], owner)

    async def test_related_stadium_searches_resolve_and_can_fail(self):
        specs = [('SV3.TownStore_196', 'BW9.FloatStone_99', 'hand'),
                 ('ME3.LumioseCity_77', 'BW1.Snivy_1', 'bench'),
                 ('SV1.Mesagoza_178', 'BW1.Servine_3', 'hand')]
        for path, selected, destination in specs:
            for success in (True, False):
                with self.subTest(path=path, success=success):
                    rig, e = self.rig('BW1.Snivy_1')
                    stadium = self.card(rig, path)
                    ability = fixtures.definition(path).ability
                    ctx = EffectContext(rig.session, P1, stadium, ability)
                    good = self.card(rig, selected, P1, 'deck')
                    ctx.choose_cards = AsyncMock(return_value=[good] if success else [])
                    ctx.flip_coins = AsyncMock(return_value=[True])
                    await ability.effect(ctx)
                    self.assertIn(good, ctx.choose_cards.call_args.args[0])
                    self.assertEqual(good._containing_area_name(), destination if success else 'deck')
                    self.assertEqual(ctx.ends_turn, path.startswith('ME3.'))

    async def test_mesagoza_tails_does_not_search_or_shuffle(self):
        rig, e = self.rig('BW1.Snivy_1')
        source = self.card(rig, 'SV1.Mesagoza_178')
        ability = fixtures.definition('SV1.Mesagoza_178').ability
        ctx = EffectContext(rig.session, P1, source, ability)
        ctx.flip_coins = AsyncMock(return_value=[False])
        ctx.search_deck = AsyncMock()
        ctx.shuffle_deck = AsyncMock()
        await ability.effect(ctx)
        ctx.search_deck.assert_not_awaited()
        ctx.shuffle_deck.assert_not_awaited()

    async def test_swelling_flash_prize_permission_and_actual_hand_entry(self):
        for prizes in (5, 6, 7):
            rig, e = self.rig('BW1.Snivy_1')
            source = self.card(rig, 'SV2.Luxray_71')
            ability = self.ability(source, 'Swelling Flash')
            self.empty(rig, 'prizePile')
            for _ in range(prizes): self.card(rig, 'BW1.Snivy_1', P1, 'prizePile')
            self.assertEqual(self.offered(rig, source, ability), prizes > 6)
            ctx = EffectContext(rig.session, P1, source, ability)
            await ability.effect(ctx)
            self.assertEqual(source._containing_area_name(), 'bench' if prizes > 6 else 'hand')

    async def test_emergency_rotation_needs_opposing_stage_two_and_bench_room(self):
        rig, e = self.rig('BW1.Snivy_1')
        source = self.card(rig, 'SV07.Klinklang_101')
        ability = self.ability(source, 'Emergency Rotation')
        self.assertFalse(self.offered(rig, source, ability))
        self.card(rig, 'BW1.Serperior_5', P2, 'bench')
        self.assertTrue(self.offered(rig, source, ability))
        await ability.effect(EffectContext(rig.session, P1, source, ability))
        self.assertEqual(source._containing_area_name(), 'bench')
        other = self.card(rig, 'SV07.Klinklang_101')
        while len(rig.board.find_player_area(P1, 'bench').children) < 5:
            self.card(rig, 'BW1.Snivy_1', P1, 'bench')
        self.assertFalse(self.offered(rig, other, ability))

    async def test_hand_entry_introduced_and_moved_before_ability_announcement(self):
        rig, e = self.rig('BW1.Snivy_1')
        source = self.card(rig, 'SV2.Luxray_71')
        self.card(rig, 'BW1.Snivy_1', P1, 'prizePile')
        ability = self.ability(source, 'Swelling Flash')
        senders = {pid: AsyncMock() for pid in (P1, P2)}
        with patch.object(rig.session.players[P1], 'send_packet', senders[P1]), \
                patch.object(rig.session.players[P2], 'send_packet', senders[P2]):
            await resolve_activated_ability(rig.session, P1, source, ability)
        for sender in senders.values():
            messages = [call.args[1]['msg'] for call in sender.await_args_list]
            intro = next(i for i, m in enumerate(messages) if m['name'] == 'EntityIntroduced'
                         and m['value']['entityID'] == source.entity_id)
            move = next(i for i, m in enumerate(messages) if m['name'] == 'EntityMoved'
                        and m['value']['entityID'] == source.entity_id)
            announcement = next(i for i, m in enumerate(messages) if m['name'] == 'AbilityPlayedEffect')
            self.assertLess(intro, move)
            self.assertLess(move, announcement)

    async def test_hand_entry_still_respects_garbotoxin(self):
        rig, e = self.rig('BW1.Snivy_1')
        source = self.card(rig, 'SV2.Luxray_71')
        self.card(rig, 'BW1.Snivy_1', P1, 'prizePile')
        ability = self.ability(source, 'Swelling Flash')
        self.assertTrue(self.offered(rig, source, ability))
        garbodor = self.card(rig, 'XY9.Garbodor_57', P2, 'bench')
        rig.attach(self.card(rig, 'BW9.FloatStone_99', P2), garbodor)
        self.assertFalse(self.offered(rig, source, ability))

    async def test_elusive_master_enters_before_drawing_not_just_draw(self):
        rig, e = self.rig('BW1.Snivy_1')
        self.empty(rig, 'hand')
        source = self.card(rig, 'Promo_SM.GreninjaGX_197')
        ability = self.ability(source, 'Elusive Master')
        self.assertTrue(self.offered(rig, source, ability))
        extra = self.card(rig, 'BW1.Snivy_1')
        self.assertFalse(self.offered(rig, source, ability))
        rig.to_area(extra, P1, 'deck')
        await ability.effect(EffectContext(rig.session, P1, source, ability))
        self.assertEqual(source._containing_area_name(), 'bench')
        self.assertEqual(len(rig.board.find_player_area(P1, 'hand').children), 3)

    async def test_electric_swamp_counts_cards_then_enters_before_energy_transfer(self):
        rig, e = self.rig('BW1.Snivy_1')
        source = self.card(rig, 'SM11.Eelektross_66')
        ability = self.ability(source, 'Electric Swamp')
        self.assertFalse(self.offered(rig, source, ability))
        energies = []
        for _ in range(3):
            energy = self.card(rig, 'BW1.LightningEnergy_108')
            rig.attach(energy, e['target'])
            energies.append(energy)
        self.assertFalse(self.offered(rig, source, ability))
        rig.attach(self.card(rig, 'BW1.LightningEnergy_108'), e['target'])
        self.assertTrue(self.offered(rig, source, ability))
        ctx = EffectContext(rig.session, P1, source, ability)
        choices = iter([[energies[0]], []])
        async def pick(pool, *args, **kwargs):
            self.assertEqual(source._containing_area_name(), 'bench')
            chosen = next(choices)
            self.assertTrue(all(c in pool for c in chosen))
            return chosen
        ctx.choose_cards = AsyncMock(side_effect=pick)
        ctx.choose_pokemon = AsyncMock(return_value=source)
        await ability.effect(ctx)
        self.assertIs(energies[0].parent, source)
        self.assertIs(energies[1].parent, e['target'])

    async def test_discard_entry_with_empty_hand_is_not_a_hand_entry(self):
        rig, e = self.rig('BW1.Snivy_1')
        self.empty(rig, 'hand')
        source = self.card(rig, 'SWSH9.Empoleon_37', P1, 'discard')
        ability = self.ability(source, 'Emergency Surfacing')
        self.assertTrue(self.offered(rig, source, ability))
        ctx = EffectContext(rig.session, P1, source, ability)
        ctx.ask_yes_no = AsyncMock(return_value=True)
        await ability.effect(ctx)
        self.assertEqual(source._containing_area_name(), 'bench')
        self.assertEqual(len(ctx.hand()), 3)

    async def test_psychic_embrace_all_prints_damage_and_target_restrictions(self):
        definitions = [(d, a) for d in CARD_DEFS_BY_GUID.values() for a in getattr(d, 'abilities', [])
                       if a.title == 'Psychic Embrace']
        self.assertGreaterEqual(len(definitions), 3)
        for d, ability in definitions:
            with self.subTest(card=d.guid):
                rig, e = self.rig('BW1.Snivy_1')
                source = self.add(rig, d, P1, 'bench')
                source.set_attribute(AttrID.HP, 310)
                target = self.card(rig, 'BW1.Solosis_55', P1, 'bench')
                target.set_attribute(AttrID.HP, 20)
                energy = self.card(rig, 'BW1.PsychicEnergy_109', P1, 'discard')
                ctx = EffectContext(rig.session, P1, source, ability)
                ctx.choose_cards = AsyncMock(return_value=[energy])
                ctx.choose_pokemon = AsyncMock(return_value=source)
                await ability.effect(ctx)
                self.assertIs(energy.parent, source)
                self.assertEqual(source.get_attribute(AttrID.HP), 290)
                # At 20 HP neither the source nor another Psychic may be selected.
                source.set_attribute(AttrID.HP, 20)
                self.card(rig, 'BW1.PsychicEnergy_109', P1, 'discard')
                self.assertFalse(ability_condition_met(ability, rig.board, P1, source))
                target.set_attribute(AttrID.HP, 30)
                self.assertTrue(ability_condition_met(ability, rig.board, P1, source))

    async def test_failed_energy_attachment_does_not_place_counters(self):
        for path, title in [('SV1.Gardevoirex_86', 'Psychic Embrace'),
                            ('SWSH5.Houndoom_96', 'Single Strike Roar')]:
            rig, e = self.rig(path)
            source = e['target']
            ability = self.ability(source, title)
            ctx = EffectContext(rig.session, P1, source, ability)
            energy = self.card(rig, 'BW1.PsychicEnergy_109', P1, 'discard')
            ctx.choose_cards = AsyncMock(return_value=[energy])
            ctx.search_deck = AsyncMock(return_value=[energy])
            ctx.ask_yes_no = AsyncMock(return_value=True)
            ctx.choose_pokemon = AsyncMock(return_value=source)
            ctx.attach_energy = AsyncMock(return_value=False)
            ctx.deal_damage = AsyncMock()
            await ability.effect(ctx)
            ctx.deal_damage.assert_not_awaited()

    async def test_similar_energy_counter_effects_complete_after_success(self):
        specs = [('Promo_HGSS.Typhlosion_9', 'Afterburner', 'BW1.FireEnergy_106', 10),
                 ('SWSH5.Houndoom_96', 'Single Strike Roar', 'SWSH5.SingleStrikeEnergy_141', 20),
                 ('SWSH5.Houndoom_179', 'Single Strike Roar', 'SWSH5.SingleStrikeEnergy_141', 20),
                 ('ME2.Toxtricity_68', 'Sinister Surge', 'BW1.DarknessEnergy_111', 20)]
        for path, title, energy_path, damage in specs:
            with self.subTest(path=path):
                rig, e = self.rig(path)
                source = e['target']
                ability = self.ability(source, title)
                target = source if title != 'Sinister Surge' else self.card(rig, 'BW5.DarkraiEX_63', P1, 'bench')
                hp = target.get_attribute(AttrID.HP)
                zone = 'discard' if title == 'Afterburner' else 'deck'
                energy = self.card(rig, energy_path, P1, zone)
                ctx = EffectContext(rig.session, P1, source, ability)
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.choose_cards = AsyncMock(return_value=[energy])
                ctx.choose_pokemon = AsyncMock(return_value=target)
                await ability.effect(ctx)
                self.assertIs(energy.parent, target)
                self.assertEqual(target.get_attribute(AttrID.HP), hp - damage)

    async def test_psychic_embrace_cannot_target_wrong_type_or_lethal_hp(self):
        rig, e = self.rig('SV1.Gardevoirex_86')
        source = e['target']
        source.set_attribute(AttrID.HP, 20)
        target = self.card(rig, 'BW1.Solosis_55', P1, 'bench')
        target.set_attribute(AttrID.HP, 30)
        energy = self.card(rig, 'BW1.PsychicEnergy_109', P1, 'discard')
        ability = self.ability(source, 'Psychic Embrace')
        ctx = EffectContext(rig.session, P1, source, ability)
        ctx.choose_cards = AsyncMock(return_value=[energy])
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ability.effect(ctx)
        self.assertIs(energy.parent, target)
        self.assertEqual(target.get_attribute(AttrID.HP), 10)
        self.assertEqual(source.get_attribute(AttrID.HP), 20)

    async def test_artazon_no_hidden_match_still_searches_and_full_bench_blocks(self):
        rig, e = self.rig('BW1.Snivy_1')
        source = self.card(rig, 'SV2.Artazon_171')
        ability = fixtures.definition('SV2.Artazon_171').ability
        rig.board.move_card(source.entity_id, rig.board.find_global_area('activeStadium').entity_id)
        self.empty(rig, 'deck')
        self.card(rig, 'HGSS1.Switch_102', P1, 'deck')
        self.assertTrue(self.offered(rig, source, ability))
        ctx = EffectContext(rig.session, P1, source, ability)
        ctx.choose_cards = AsyncMock(return_value=[])
        await ability.effect(ctx)
        self.assertEqual(ctx.choose_cards.call_args.args[0], [])
        self.assertEqual(len(ctx.choose_cards.call_args.kwargs['display_cards']), 1)
        while len(ctx.my_bench()) < 5: self.card(rig, 'BW1.Snivy_1', P1, 'bench')
        self.assertFalse(self.offered(rig, source, ability))


if __name__ == '__main__':
    unittest.main()
