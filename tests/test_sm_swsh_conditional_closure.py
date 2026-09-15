"""Scenario coverage for SM/SWSH prerequisite-dependent effects."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests import test_sm_swsh_final_trainers as helpers
from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class ConditionalClosureTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    setup_card = helpers.RemainingTrainerTests.setup_card
    energy = helpers.RemainingTrainerTests.energy
    legal = helpers.RemainingTrainerTests.legal

    async def test_morgan_pays_named_cost_then_inspects_twelve_and_splits_energy(self):
        rig, ctx, d = self.setup_card('SM9.Morgan_149')
        self.assertFalse(self.legal(rig, ctx, d))
        paid = [self.add(rig, fixtures.definition(p), P1, 'hand') for p in
                ('SM9.Dana_137', 'SM9.Evelyn_141', 'SM9.Nita_151')]
        basic = self.energy(rig, zone='deck')
        special = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), P1, 'deck')
        viewed = ctx.deck_top(12)
        async def choose(pool, count, **kwargs):
            self.assertTrue(all(c in ctx.discard_pile() for c in paid))
            self.assertEqual(kwargs['display_cards'], viewed)
            self.assertEqual(kwargs['minimum'], 0)
            self.assertIn(basic, pool)
            self.assertIn(special, pool)
            self.assertTrue(all(c in viewed for c in pool))
            return [basic, special]
        ctx.choose_cards = AsyncMock(side_effect=choose)
        a, b = ctx.my_active(), ctx.my_bench()[0]
        ctx.choose_pokemon = AsyncMock(side_effect=[a, b])
        self.assertTrue(self.legal(rig, ctx, d))
        await d.effect(ctx)
        self.assertIs(basic.parent, a)
        self.assertIs(special.parent, b)
        self.assertTrue(all(c in ctx.deck() for c in viewed if c not in (basic, special)))

    async def test_wait_and_see_hammer_only_second_players_first_turn_and_one_enemy_energy(self):
        for path in ('SM8.WaitandSeeHammer_192', 'SM8.WaitandSeeHammer_236'):
            rig, ctx, d = self.setup_card(path)
            energy = self.energy(rig, pid=P2)
            rig.attach(energy, ctx.opponent_bench()[0])
            for turn in (1, 3, 4):
                rig.session.turn_state.turn_number = turn
                self.assertFalse(self.legal(rig, ctx, d))
            rig.session.turn_state.turn_number = 2
            self.assertTrue(self.legal(rig, ctx, d))
            ctx.choose_cards = AsyncMock(return_value=[energy])
            await d.effect(ctx)
            self.assertIn(energy, ctx.discard_pile(P2))
            self.assertEqual(ctx.choose_cards.call_args.args[1], 1)
            self.assertTrue(all(c.owning_player_id == P2 for c in ctx.choose_cards.call_args.args[0]))

    async def test_thorton_transfers_damage_conditions_attachments_and_turn_locks(self):
        rig, ctx, d = self.setup_card('SWSH11.Thorton_167')
        outgoing = ctx.my_active()
        incoming = self.add(rig, fixtures.definition('SWSH12.HisuianArcanineV_90'), P1, 'discard')
        energy = self.energy(rig)
        rig.attach(energy, outgoing)
        outgoing.set_attribute(AttrID.HP, ctx.max_hp(outgoing)-30)
        poisoned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
        outgoing.set_attribute(AttrID.SPECIAL_CONDITIONS, [poisoned])
        ts = rig.session.turn_state
        ts.entered_play_turn[outgoing.entity_id] = 2
        ts.retreat_locks[outgoing.entity_id] = 6
        ts.attack_locks[(outgoing.entity_id, 'blocked')] = 6
        ctx.choose_cards = AsyncMock(return_value=[incoming])
        ctx.choose_pokemon = AsyncMock(return_value=outgoing)
        self.assertTrue(self.legal(rig, ctx, d))
        await d.effect(ctx)
        self.assertIs(ctx.my_active(), incoming)
        self.assertIs(energy.parent, incoming)
        self.assertIn(outgoing, ctx.discard_pile())
        self.assertEqual(incoming.get_attribute(AttrID.HP), ctx.max_hp(incoming)-30)
        self.assertEqual(incoming.get_attribute(AttrID.SPECIAL_CONDITIONS), [poisoned])
        self.assertEqual(ts.entered_play_turn[incoming.entity_id], 2)
        self.assertEqual(ts.retreat_locks[incoming.entity_id], 6)
        self.assertEqual(ts.attack_locks[(incoming.entity_id, 'blocked')], 6)

    async def test_lost_vacuum_pays_before_target_and_lost_zones_both_cards(self):
        for path in ('SWSH11.LostVacuum_162', 'CZ.LostVacuum_135'):
            rig, ctx, d = self.setup_card(path)
            cost = self.energy(rig)
            tool = self.add(rig, fixtures.definition('SM3.WishfulBaton_128'), P2, 'hand')
            rig.attach(tool, ctx.opponent_active())
            calls = 0
            async def choose(pool, count, **kwargs):
                nonlocal calls
                calls += 1
                self.assertEqual(count, 1)
                if calls == 1: return [cost]
                self.assertIn(cost, rig.board.find_player_area(P1, 'lostZone').children)
                self.assertIn(tool, pool)
                return [tool]
            ctx.choose_cards = AsyncMock(side_effect=choose)
            self.assertTrue(self.legal(rig, ctx, d))
            await d.effect(ctx)
            self.assertIn(cost, rig.board.find_player_area(P1, 'lostZone').children)
            self.assertIn(tool, rig.board.find_player_area(P2, 'lostZone').children)

    async def test_authored_discards_use_provided_energy_not_physical_card_count(self):
        cases = (
            ('SWSH1.Cinderace_36', 'Bright Flame', 2),
            ('SWSH1.Corviknight_135', 'Iron Wings', 2),
            ('SWSH4.DrapionV_106', 'Hazardous Claws', 2),
            ('SWSH4.DrapionV_175', 'Hazardous Claws', 2),
            ('SWSH6.Walrein_39', 'Hail Prison', 2),
            ('SWSH9.FlygonV_106', 'Draconic Impulse', 3),
            ('SWSH9.FlygonV_164', 'Draconic Impulse', 3),
            ('SWSH10.GarchompV_117', 'Sonic Strike', 3),
            ('SWSH10.GarchompV_178', 'Sonic Strike', 3),
            ('SWSH10.LuxrayV_50', 'Radiating Pulse', 2),
            ('SWSH10.LuxrayV_168', 'Radiating Pulse', 2),
            ('SWSH7.RapidStrikeScrolloftheFlyingDragon_153', 'Meteor', 2))
        for path, title, amount in cases:
            with self.subTest(path=path):
                tool = 'Scroll' in path
                rig, e = self.rig(path, 'trainer' if tool else 'pokemon')
                d = fixtures.definition(path)
                attacker = rig.board.active_pokemon(P1) if tool else e['target']
                attack = next(a for a in (d.granted_abilities if tool else d.abilities) if a.title == title)
                ctx = EffectContext(rig.session, P1, attacker, attack)
                for energy in list(ctx.attached_energies(attacker)): rig.to_area(energy, P1, 'hand')
                double = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), P1, 'hand')
                extra = self.energy(rig)
                rig.attach(double, attacker); rig.attach(extra, attacker)
                selected = [double]
                if amount == 3:
                    single = self.energy(rig); rig.attach(single, attacker)
                    selected.append(single)
                rig.session.prompt_energy_unit_picker = AsyncMock(return_value=[c.entity_id for c in selected])
                ctx.flip_coins = AsyncMock(return_value=[False])
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.deal_damage = AsyncMock(return_value=10)
                ctx.choose_pokemon = AsyncMock(return_value=ctx.opponent_bench()[0])
                if 'Flygon' in path:
                    rig.to_area(ctx.opponent_active(), P2, 'bench')
                    self.add(rig, fixtures.definition('SWSH1.SnorlaxVMAX_142'), P2, 'activePokemonArea')
                await attack.effect(ctx)
                for energy in selected: self.assertIn(energy, ctx.discard_pile(), path)
                self.assertIs(extra.parent, attacker, path)
                self.assertEqual(rig.session.prompt_energy_unit_picker.call_args.args[3], amount)
                ctx.deal_damage.assert_awaited()

    async def test_rosa_searches_three_independent_categories_after_a_ko(self):
        rig, ctx, d = self.setup_card('SM12.Rosa_204')
        self.assertFalse(self.legal(rig, ctx, d))
        rig.session.turn_state.kos_suffered_last_turn[P1] = [{'archetype_id': ctx.my_active().archetype_id}]
        self.assertTrue(self.legal(rig, ctx, d))
        pokemon = self.add(rig, fixtures.definition('SM12.Flareon_25'), P1, 'deck')
        trainer = self.add(rig, fixtures.definition('SM9.Morgan_149'), P1, 'deck')
        basic = self.energy(rig, zone='deck')
        special = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), P1, 'deck')
        async def choose(groups, **kwargs):
            self.assertEqual(len(groups), 3)
            for group, expected in zip(groups, (pokemon, trainer, basic)):
                pred, count, _ = group
                self.assertEqual(count, 1)
                self.assertEqual([c for c in (pokemon, trainer, basic, special) if pred(c)], [expected])
            return [[pokemon], [trainer], [basic]]
        ctx.search_deck_groups = AsyncMock(side_effect=choose)
        ctx.put_in_hand = AsyncMock(wraps=ctx.put_in_hand)
        await d.effect(ctx)
        ctx.search_deck_groups.assert_awaited_once()
        self.assertTrue(all(c in ctx.hand() for c in (pokemon, trainer, basic)))
        self.assertTrue(ctx.put_in_hand.call_args.kwargs['reveal'])
        self.assertIn(special, ctx.deck())

    async def test_lance_can_bench_evolved_dragons_and_limits_search_to_free_slots(self):
        rig, ctx, d = self.setup_card('DM.Lance_61')
        self.assertFalse(self.legal(rig, ctx, d))
        rig.session.turn_state.kos_suffered_last_turn[P1] = [{'archetype_id': ctx.my_active().archetype_id}]
        self.assertTrue(self.legal(rig, ctx, d))
        dragon = self.add(rig, fixtures.definition('DM.DragoniteGX_37'), P1, 'deck')
        while len(ctx.my_bench()) < 4:
            self.add(rig, fixtures.definition('SM12.Flareon_25'), P1, 'bench')
        ctx.search_deck = AsyncMock(return_value=[dragon])
        await d.effect(ctx)
        args, kwargs = ctx.search_deck.call_args
        self.assertTrue(args[0](dragon))
        self.assertFalse(args[0](ctx.my_active()))
        self.assertEqual(kwargs.get('count', args[1] if len(args) > 1 else None), 1)
        self.assertEqual(kwargs['minimum'], 0)
        self.assertIn(dragon, ctx.my_bench())
        self.assertFalse(self.legal(rig, ctx, d))

    async def test_lysandre_prism_counts_own_fire_and_targets_opponent_discard(self):
        rig, ctx, d = self.setup_card('SM6.Lysandre_110')
        for p in ctx.my_pokemon_in_play(): p.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        cards = [self.energy(rig, pid=P2, zone='discard') for _ in range(3)]
        self.assertFalse(self.legal(rig, ctx, d))
        for p in ctx.my_pokemon_in_play()[:2]: p.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        self.assertTrue(self.legal(rig, ctx, d))
        ctx.choose_cards = AsyncMock(return_value=cards[:2])
        await d.effect(ctx)
        self.assertEqual(ctx.choose_cards.call_args.args[1], 2)
        self.assertTrue(all(c.owning_player_id == P2 for c in ctx.choose_cards.call_args.args[0]))
        self.assertTrue(all(c in rig.board.find_player_area(P2, 'lostZone').children for c in cards[:2]))
        self.assertIn(cards[2], ctx.discard_pile(P2))

    async def test_oricorio_dance_of_tribute_requires_prior_ko_and_is_shared_once(self):
        from spirit.game.session.legal_actions import _ability_entries
        rig, e = self.rig('SM12.OricorioGX_95')
        ability = fixtures.definition('SM12.OricorioGX_95').abilities[0]
        ctx = EffectContext(rig.session, P1, e['target'], ability)
        other = self.add(rig, fixtures.definition('SM12.OricorioGX_95'), P1, 'bench')
        ts = rig.session.turn_state
        entries = lambda: _ability_entries(rig.board, ts, P1, 'test', [ctx.attacker, other])
        self.assertFalse(entries())
        ts.kos_suffered_last_turn[P1] = [{'archetype_id': other.archetype_id}]
        self.assertEqual(len(entries()), 2)
        before = ctx.hand_size()
        await ability.effect(ctx)
        self.assertEqual(ctx.hand_size(), before+3)
        ts.used_named_abilities.add('Dance of Tribute')
        self.assertFalse(entries())

    def scroll(self, path, holder='SWSH5.Houndoom_96'):
        rig, e = self.rig(holder)
        d = fixtures.definition(path)
        attack = d.granted_abilities[0]
        tool = self.add(rig, d, P1, 'hand')
        rig.attach(tool, e['target'])
        return rig, EffectContext(rig.session, P1, e['target'], attack)

    async def test_scrolls_require_their_matching_battle_style(self):
        from spirit.game.session.legal_actions import ability_condition_met
        paths = ('SWSH5.RapidStrikeScrollofSwirls_131',
                 'SWSH5.SingleStrikeScrollofScorn_133',
                 'SWSH6.RapidStrikeScrolloftheSkies_151',
                 'SWSH6.SingleStrikeScrollofPiercing_154',
                 'SWSH7.RapidStrikeScrolloftheFlyingDragon_153',
                 'SWSH7.SingleStrikeScrolloftheFangedDragon_158')
        for path in paths:
            rig, ctx = self.scroll(path)
            rapid = self.add(rig, fixtures.definition('SWSH6.ZeraoraV_53'), P1, 'bench')
            plain = self.add(rig, fixtures.definition('SM12.Flareon_25'), P1, 'bench')
            self.assertEqual(ability_condition_met(ctx.ability, rig.board, P1, ctx.attacker), 'SingleStrike' in path)
            self.assertEqual(ability_condition_met(ctx.ability, rig.board, P1, rapid), 'RapidStrike' in path)
            self.assertFalse(ability_condition_met(ctx.ability, rig.board, P1, plain))

    async def test_scorn_counts_damage_counters_and_skies_counts_energy_units(self):
        rig, ctx = self.scroll('SWSH5.SingleStrikeScrollofScorn_133')
        ctx.attacker.set_attribute(AttrID.HP, ctx.max_hp(ctx.attacker)-40)
        ctx.deal_damage = AsyncMock(return_value=50)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 50)
        rig, ctx = self.scroll('SWSH6.RapidStrikeScrolloftheSkies_151', 'SWSH6.ZeraoraV_53')
        for card in list(ctx.attached_energies(ctx.defender)): rig.to_area(card, P2, 'hand')
        double = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), P2, 'hand')
        rig.attach(double, ctx.defender)
        ctx.deal_damage = AsyncMock(return_value=110)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 110)

    async def test_matchless_maelstrom_hits_every_opponent_once(self):
        rig, ctx = self.scroll('SWSH5.RapidStrikeScrollofSwirls_131', 'SWSH6.ZeraoraV_53')
        for pokemon in ctx.opponent_pokemon_in_play():
            pokemon.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.LIGHTNING.value])
            pokemon.set_attribute(AttrID.RESISTANCE_TYPES, PokemonTypes.FIRE.value)
        before = {p: p.get_attribute(AttrID.HP) for p in ctx.opponent_pokemon_in_play()}
        await ctx.ability.effect(ctx)
        for p, hp in before.items():
            self.assertEqual(hp-p.get_attribute(AttrID.HP), 60 if p is ctx.defender else 30)

    async def test_bullet_breakthrough_ignores_defender_protection_and_weakness(self):
        from spirit.game.card_effects.passives_common import apply_protection
        rig, ctx = self.scroll('SWSH6.SingleStrikeScrollofPiercing_154')
        defender = ctx.defender
        defender.set_attribute(AttrID.HP, 400)
        defender.set_attribute(AttrID.WEAKNESS_TYPES, list(ctx.attacker.get_attribute(AttrID.POKEMON_TYPES)))
        guard = EffectContext(rig.session, P2, defender, None)
        await apply_protection(guard, prevent=True)
        before = defender.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        self.assertEqual(before-defender.get_attribute(AttrID.HP), 120)

    async def test_superstrong_slash_discards_every_energy_after_damage(self):
        rig, ctx = self.scroll('SWSH7.SingleStrikeScrolloftheFangedDragon_158')
        energies = list(ctx.attached_energies(ctx.attacker))
        async def damage(amount, **kwargs):
            self.assertIsNone(amount)  # None asks deal_damage to use the printed damage.
            self.assertEqual(ctx.ability.damage, 300)
            self.assertTrue(all(c.parent is ctx.attacker for c in energies))
            return 300
        ctx.deal_damage = AsyncMock(side_effect=damage)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once()
        self.assertFalse(ctx.attached_energies(ctx.attacker))
        self.assertTrue(all(c in ctx.discard_pile() for c in energies))

    async def test_iron_wings_can_pay_with_one_double_energy_card(self):
        from unittest.mock import patch
        rig, e = self.rig('SWSH1.Corviknight_135')
        d = fixtures.definition('SWSH1.Corviknight_135')
        ctx = EffectContext(rig.session, P1, e['target'], d.abilities[1])
        for energy in list(ctx.attached_energies(ctx.attacker)): rig.to_area(energy, P1, 'hand')
        double = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), P1, 'hand')
        rig.attach(double, ctx.attacker)
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.deal_damage = AsyncMock(return_value=130)
        with patch('spirit.game.scripts.cards.SWSH1.Corviknight_135.apply_protection', new_callable=AsyncMock) as protect:
            await ctx.ability.effect(ctx)
            self.assertIn(double, ctx.discard_pile())
            protect.assert_awaited_once()
