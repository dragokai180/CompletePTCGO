"""Printed search quantities/privacy and Pokemon-only Ability suppression."""
import re
import unittest
from pathlib import Path
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Attack, PokemonCardDef, def_for
from spirit.game.scripts.cards import loader
from spirit.game.models.board import PokemonEntity
from spirit.game.card_effects.bw_era import bw_legacy_attack, _norm
from spirit.game.session.effects import EffectContext, resolve_triggered_ability
from spirit.game.session.passives import ability_locked, out_of_play_ability_locked, active_passives, tool_suppressed
from spirit.tools.effect_smoke import P1, P2


class SearchAndSuppressionAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def path_for(self, code, number):
        model = next(m for m in loader.cards if def_for(m.guid).set_code == code
                     and str(def_for(m.guid).collector_number) == str(number))
        path = Path(loader.script_by_guid[model.guid]).relative_to(loader.scripts_dir).with_suffix('')
        return '.'.join(path.parts)

    async def test_named_searches_keep_names_instead_of_accepting_any_card(self):
        for code, number, title, target_code, target_number, count in (
                ('TwentiethAnn', 125, 'Warble', 'TwentiethAnn', 125, 2),
                ('DV', 12, 'Signs of Evolution', 'DV', 14, 1)):
            rig, e, ctx = self.ctx(self.path_for(code, number), title)
            good = self.add(rig, fixtures.definition(self.path_for(target_code, target_number)), P1, 'deck')
            bad = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'deck')
            ctx.flip_coins = AsyncMock(return_value=[True])
            ctx.shuffle_deck = AsyncMock()
            async def search(predicate, count, **kwargs):
                self.assertTrue(predicate(good))
                self.assertFalse(predicate(bad))
                return []
            ctx.search_deck = AsyncMock(side_effect=search)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.search_deck.await_args.args[1], count)

    async def test_bench_search_quantities_names_stages_and_capacity(self):
        cases = (
            ('BW10', 71, 'Call for Family', 'BW1', 1, 2),
            ('BW10', 10, 'Call for Family', 'BW1', 1, 2),
            ('SWSH6', 60, 'Mirage Step', 'SWSH6', 60, 3),
            ('SWSH12', 61, 'Psy Call', 'BW1', 3, 2),
            ('ME5', 37, 'Spreading Light', 'ME5', 37, 3),
            ('XY6', 10, 'Afterimage Assault', 'XY6', 10, 2),
            ('SM2', 95, 'Division', 'SM2', 95, 2),
            ('SM8', 31, 'Bee March', 'BW8', 4, 3),
            ('SM4', 2, 'Multiply', 'SM4', 2, 3),
            ('XY11', 43, 'Come Along', 'HGSS4', 69, 1),
            ('SV05', 18, 'Flock', 'SV05', 18, 2),
        )
        for code, number, title, target_code, target_number, maximum in cases:
            for free in (1, 5):
                with self.subTest(card=(code, number), free=free):
                    rig, e, ctx = self.ctx(self.path_for(code, number), title)
                    for card in list(ctx.my_bench()):
                        rig.to_area(card, P1, 'discard')
                    for _ in range(5-free):
                        self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
                    for card in list(ctx.deck()):
                        rig.to_area(card, P1, 'discard')
                    good = [self.add(rig, fixtures.definition(self.path_for(target_code, target_number)),
                                     P1, 'deck') for _ in range(maximum)]
                    bad = self.add(rig, fixtures.definition('BW1.ProfessorJuniper_101'), P1, 'deck')
                    async def choose(cards, count, **kwargs):
                        self.assertNotIn(bad, cards)
                        self.assertEqual(kwargs['minimum'], 0)
                        return list(cards)[:count]
                    ctx.choose_cards = AsyncMock(side_effect=choose)
                    ctx.shuffle_deck = AsyncMock()
                    ctx.deal_damage = AsyncMock()
                    await ctx.ability.effect(ctx)
                    self.assertEqual(sum(c in ctx.my_bench() for c in good), min(free, maximum))
                    self.assertIn(bad, ctx.deck())
                    ctx.shuffle_deck.assert_awaited_once()

    async def test_energy_salon_requires_different_types_not_different_art(self):
        rig, e, ctx = self.ctx('XY1.Delcatty_105', 'Energy Salon')
        for card in list(ctx.deck()):
            rig.to_area(card, P1, 'discard')
        cards = [self.add(rig, fixtures.definition(path), P1, 'deck') for path in (
            'BW1.FireEnergy_106', 'BW1.FireEnergy_106', 'BW1.GrassEnergy_105', 'BW1.WaterEnergy_107')]
        selected = []
        async def choose(candidates, count, **kwargs):
            self.assertEqual(count, 1)
            if selected:
                self.assertNotIn(cards[1], candidates)
            pick = list(candidates)[:1]
            selected.extend(pick)
            return pick
        ctx.choose_cards = AsyncMock(side_effect=choose)
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(selected, [cards[0], cards[2], cards[3]])
        self.assertTrue(all(card in ctx.hand() for card in selected))
        self.assertIn(cards[1], ctx.deck())

    async def test_coin_gated_search_requires_both_heads_and_does_not_shuffle_on_failure(self):
        for coins in ([False, False], [True, False], [True, True]):
            rig, e, ctx = self.ctx(self.path_for('ME5', 71), 'Challenging Delivery')
            ctx.flip_coins = AsyncMock(return_value=coins)
            ctx.search_deck = AsyncMock(return_value=[])
            ctx.shuffle_deck = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.search_deck.await_count, int(all(coins)))
            self.assertEqual(ctx.shuffle_deck.await_count, int(all(coins)))

    async def test_tool_suppressing_ability_stops_but_tool_effects_remain(self):
        rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        self.add(rig, fixtures.definition('XY6.Banette_31'), P2, 'bench')
        tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P1, 'hand')
        rig.attach(tool, ctx.attacker)
        self.assertTrue(tool_suppressed(rig.board, tool))
        await ctx.ability.effect(ctx)
        self.assertFalse(tool_suppressed(rig.board, tool))
        jammer = self.add(rig, fixtures.definition('SWSH5.ToolJammer_136'), P2, 'hand')
        rig.attach(jammer, ctx.defender)
        self.assertTrue(tool_suppressed(rig.board, tool))

    async def test_stadium_is_not_an_opposing_pokemon_ability(self):
        rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        target = self.add(rig, fixtures.definition('SWSH5.CorviknightVMAX_110'), P2, 'bench')
        target.set_attribute(AttrID.HP, 320)
        stadium = self.stadium(rig, 'SWSH6.OldCemetery_147', P1)
        ability = fixtures.definition('SWSH6.OldCemetery_147').abilities[0]
        stadium_ctx = EffectContext(rig.session, P1, stadium, ability)
        stadium_ctx.energy_receiver = target
        self.assertFalse(stadium_ctx.is_ability_effect())
        self.assertFalse(stadium_ctx.effects_blocked(target))
        await ability.effect(stadium_ctx)
        self.assertEqual(target.get_attribute(AttrID.HP), 300)

    def stadium(self, rig, path, owner=P2):
        card = self.add(rig, fixtures.definition(path), owner, 'hand')
        area = rig.board.find_global_area('activeStadium')
        for old in list(area.children):
            rig.to_area(old, old.owning_player_id, 'discard')
        rig.board.move_card(card.entity_id, area.entity_id)
        return card

    async def test_aero_blitz_requires_one_or_two_without_revealing(self):
        for deck_size, amount in ((3, 1), (3, 2), (1, 1), (0, 0)):
            rig, e, ctx = self.ctx('XY11.Talonflame_96', 'Aero Blitz')
            for card in list(ctx.deck())[deck_size:]:
                rig.to_area(card, P1, 'discard')
            picks = ctx.deck()[:amount]
            hand_before = len(ctx.hand())
            ctx.deal_damage = AsyncMock()
            ctx.shuffle_deck = AsyncMock()
            ctx.reveal_cards = AsyncMock()

            async def select(cards, count, **kwargs):
                self.assertEqual(count, 2)
                self.assertEqual(kwargs['minimum'], min(1, deck_size))
                self.assertEqual(list(cards), list(kwargs['display_cards']))
                return picks

            ctx.choose_cards = AsyncMock(side_effect=select)
            await ctx.ability.effect(ctx)
            self.assertEqual(len(ctx.hand()), hand_before + amount)
            self.assertTrue(all(c in ctx.hand() for c in picks))
            ctx.shuffle_deck.assert_awaited_once()
            ctx.reveal_cards.assert_not_awaited()
            ctx.deal_damage.assert_awaited()

    async def test_all_plain_shared_search_to_hand_families_keep_printed_count(self):
        seen = set()
        checked = 0
        for model in loader.cards:
            definition = def_for(model.guid)
            for attack in getattr(definition, 'abilities', []):
                text = _norm(attack.game_text or '')
                match = re.fullmatch(
                    r"search your deck for (up to |any )?(\d+|an?|1) "
                    r"(.+?)(?:, (?:reveal (?:it|them)|show (?:it|them) to your opponent),)? "
                    r"and put (?:it|them) into your hand\. "
                    r"(?:then, shuffle your deck|shuffle your deck afterward)\.", text)
                if not match or text in seen or not isinstance(attack, Attack) \
                        or attack.effect is not bw_legacy_attack or 'different types' in text \
                        or 'different names' in text or ', and a ' in text or ' and a ' in text:
                    continue
                seen.add(text)
                path = Path(loader.script_by_guid[model.guid]).relative_to(loader.scripts_dir).with_suffix('')
                path = '.'.join(path.parts)
                with self.subTest(card=path, attack=attack.title):
                    rig, e, ctx = self.ctx(path, attack.title)
                    ctx.search_deck = AsyncMock(return_value=[])
                    ctx.shuffle_deck = AsyncMock()
                    ctx.deal_damage = AsyncMock()
                    await attack.effect(ctx)
                    ctx.search_deck.assert_awaited_once()
                    args, kwargs = ctx.search_deck.await_args
                    expected = int(match.group(2)) if match.group(2).isdigit() else 1
                    self.assertEqual(kwargs.get('count', args[1] if len(args) > 1 else 1), expected)
                    if match.group(1) == 'up to ':
                        self.assertEqual(kwargs.get('minimum', 0),
                                         1 if args[0] is None else 0)
                    ctx.shuffle_deck.assert_awaited_once()
                    checked += 1
        self.assertGreater(checked, 35)

    async def test_search_filters_do_not_accept_unrelated_card_classes(self):
        cases = (
            ('XY1.Gogoat_19', 'Lead', 'BW1.ProfessorJuniper_101', 'BW1.Snivy_1', 2),
            ('XY5.Solrock_83', 'Solar Generator', 'HGSS1.DoubleColorlessEnergy_103', 'BW1.FireEnergy_106', 2),
            ('XY7.Relicanth_23', 'Deep Sea Search', 'BW5.DarkClaw_92', 'BW1.ProfessorJuniper_101', 2),
            ('XY9.Kricketot_5', 'Bug Hunch', 'BW1.Snivy_1', 'BW1.Tepig_15', 3),
        )
        for path, title, valid_path, invalid_path, count in cases:
            with self.subTest(card=path):
                rig, e, ctx = self.ctx(path, title)
                good = self.add(rig, fixtures.definition(valid_path), P1, 'deck')
                bad = self.add(rig, fixtures.definition(invalid_path), P1, 'deck')

                async def search(predicate, requested, **kwargs):
                    self.assertEqual(requested, count)
                    self.assertTrue(predicate(good))
                    self.assertFalse(predicate(bad))
                    self.assertEqual(kwargs['minimum'], 0)
                    return []
                ctx.search_deck = AsyncMock(side_effect=search)
                ctx.shuffle_deck = AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.search_deck.assert_awaited_once()

    async def test_stadium_attachment_triggers_survive_shadow_stitching_and_hex(self):
        for mode in ('shadow', 'hex', 'garbotoxin', 'bide'):
            for owner in (P1, P2):
                with self.subTest(lock=mode, stadium_owner=owner):
                    rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
                    if mode == 'shadow':
                        await ctx.ability.effect(ctx)
                    elif mode == 'hex':
                        rig.session.turn_state.abilities_disabled_through_turn = rig.session.turn_state.turn_number + 1
                    elif mode == 'garbotoxin':
                        garbo = self.add(rig, fixtures.definition('XY9.Garbodor_57'), P1, 'bench')
                        tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P1, 'hand')
                        rig.attach(tool, garbo)
                    else:
                        rig.to_area(ctx.attacker, P1, 'bench')
                        self.add(rig, fixtures.definition('XY4.Wobbuffet_36'), P1, 'activePokemonArea')
                    stadium = self.stadium(rig, 'SWSH6.OldCemetery_147', owner)
                    receiver = ctx.opponent_bench()[0]
                    receiver.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
                    receiver.set_attribute(AttrID.HP, 100)
                    energy = self.add(rig, fixtures.definition('BW1.FireEnergy_106'), P2, 'hand')
                    rig.attach(energy, receiver)
                    self.assertFalse(ability_locked(rig.board, stadium))
                    await rig.session.fire_energy_attached_triggers(P2, energy, receiver)
                    self.assertEqual(receiver.get_attribute(AttrID.HP), 80)

    async def test_every_non_pokemon_callback_is_exempt_from_pokemon_ability_locks(self):
        rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        await ctx.ability.effect(ctx)
        rig.session.turn_state.abilities_disabled_through_turn = rig.session.turn_state.turn_number + 1
        checked = 0
        for model in loader.cards:
            definition = def_for(model.guid)
            if isinstance(definition, PokemonCardDef) or not getattr(definition, 'abilities', []):
                continue
            card = self.add(rig, definition, P2, 'hand')
            # Fossils played as Pokemon can have genuine Pokemon Abilities.
            if isinstance(card, PokemonEntity):
                continue
            for ability in definition.abilities:
                self.assertFalse(ability_locked(rig.board, card, ability), definition.display_name)
            self.assertFalse(out_of_play_ability_locked(rig.board, card))
            checked += 1
        self.assertGreaterEqual(checked, 7)

    async def test_shadow_stitching_disables_garbotoxin_without_disabling_own_abilities(self):
        rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        garbo = self.add(rig, fixtures.definition('XY9.Garbodor_57'), P2, 'bench')
        tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P2, 'hand')
        rig.attach(tool, garbo)
        self.assertTrue(ability_locked(rig.board, ctx.attacker))
        await ctx.ability.effect(ctx)
        self.assertFalse(ability_locked(rig.board, ctx.attacker))
        self.assertTrue(ability_locked(rig.board, garbo))
        self.assertFalse(any(carrier is garbo for _, carrier in active_passives(rig.board)))
        await fixtures.definition('XY11.PokmonRanger_104').effect(
            EffectContext(rig.session, P1, ctx.attacker, None))
        self.assertTrue(ability_locked(rig.board, ctx.attacker))

    async def test_garbotoxin_disables_tool_concealment(self):
        rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        self.add(rig, fixtures.definition('XY6.Banette_31'), P2, 'bench')
        tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P1, 'hand')
        rig.attach(tool, ctx.attacker)
        self.assertTrue(tool_suppressed(rig.board, tool))
        garbo = self.add(rig, fixtures.definition('XY9.Garbodor_57'), P1, 'bench')
        garbo_tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P1, 'hand')
        rig.attach(garbo_tool, garbo)
        self.assertFalse(tool_suppressed(rig.board, tool))

    def definition_named(self, name):
        return next(def_for(m.guid) for m in loader.cards if def_for(m.guid).display_name == name)

    async def test_compound_searches_choose_one_from_each_requested_group(self):
        for path, title, names, bench in (
                ('SM8.Carbink_117', 'Diamond Gate', ('Professor Juniper', 'Old Cemetery'), False),
                ('SM1.Dratini_94', 'Signs of Evolution', ('Dratini', 'Dragonair', 'Dragonite'), False),
                ('SM2.Politoed_25', 'Roll Call', ('Poliwag', 'Poliwhirl', 'Poliwrath'), True)):
            with self.subTest(card=path):
                rig, e, ctx = self.ctx(path, title)
                for card in list(ctx.deck()):
                    rig.to_area(card, P1, 'discard')
                for card in list(ctx.my_bench()):
                    rig.to_area(card, P1, 'discard')
                wanted = [self.add(rig, self.definition_named(name), P1, 'deck') for name in names]
                duplicate = self.add(rig, self.definition_named(names[0]), P1, 'deck')
                async def groups(specs, **kwargs):
                    self.assertEqual(len(specs), len(wanted))
                    self.assertEqual(kwargs['total'], len(wanted))
                    for i, (predicate, count, _) in enumerate(specs):
                        self.assertEqual(count, 1)
                        self.assertTrue(predicate(wanted[i]))
                        self.assertTrue(all(not predicate(card) for j, card in enumerate(wanted) if j != i))
                    return [[card] for card in wanted]
                ctx.search_deck_groups = AsyncMock(side_effect=groups)
                ctx.shuffle_deck = AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.search_deck_groups.assert_awaited_once()
                self.assertTrue(all(c in (ctx.my_bench() if bench else ctx.hand()) for c in wanted))
                self.assertIn(duplicate, ctx.deck())

    async def test_variable_coin_search_count_is_not_one(self):
        for heads in (0, 3):
            rig, e, ctx = self.ctx(self.path_for('ME1', 99), 'All-You-Can-Grab')
            ctx.flip_coins = AsyncMock(side_effect=[[True]] * heads + [[False]])
            ctx.search_deck = AsyncMock(return_value=[])
            ctx.shuffle_deck = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.search_deck.await_count, int(heads > 0))
            if heads:
                self.assertIsNone(ctx.search_deck.await_args.args[0])
                self.assertEqual(ctx.search_deck.await_args.args[1], heads)
                self.assertEqual(ctx.search_deck.await_args.kwargs['minimum'], 1)

    async def test_fan_call_checks_both_type_and_printed_hp(self):
        from spirit.game.card_effects.bw_era import _ability_search_predicate
        rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        predicate = _ability_search_predicate('search your deck for up to 3 [c] pokémon with 100 hp or less, reveal them, and put them into your hand.')
        small = self.add(rig, self.definition_named('Patrat'), P1, 'deck')
        big = self.add(rig, fixtures.definition('PGO.Snorlax_55'), P1, 'deck')
        boundary = self.add(rig, fixtures.definition('BW7.Snorlax_109'), P1, 'deck')
        colored = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'deck')
        self.assertTrue(predicate(small))
        self.assertTrue(predicate(boundary))
        self.assertFalse(predicate(big))
        self.assertFalse(predicate(colored))

    async def test_different_names_search_rejects_another_copy(self):
        rig, e, ctx = self.ctx('Promo_SM.Celebi_224', 'Call for Greatness')
        for card in list(ctx.deck()):
            rig.to_area(card, P1, 'discard')
        names = ('Tapu Lele-GX', 'Tapu Lele-GX', 'Darkrai-GX', 'Decidueye-GX')
        cards = [self.add(rig, self.definition_named(name), P1, 'deck') for name in names]
        selected = []
        async def choose(candidates, count, **kwargs):
            if selected:
                self.assertNotIn(cards[1], candidates)
            picked = list(candidates)[:count]
            selected.extend(picked)
            return picked
        ctx.choose_cards = AsyncMock(side_effect=choose)
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(selected, [cards[0], cards[2], cards[3]])
        self.assertIn(cards[1], ctx.deck())

    async def test_super_growth_evolves_chosen_grass_pokemon_twice(self):
        rig, e, ctx = self.ctx(self.path_for('SM11', 1), 'Super Growth')
        basic = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
        first = self.add(rig, fixtures.definition('BW1.Servine_3'), P1, 'deck')
        second = self.add(rig, fixtures.definition('BW1.Serperior_5'), P1, 'deck')
        for card in list(ctx.deck()):
            if card not in (first, second):
                rig.to_area(card, P1, 'discard')
        ctx.choose_pokemon = AsyncMock(return_value=basic)
        ctx.choose_cards = AsyncMock(side_effect=lambda cards, count, **kw: list(cards)[:count])
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertIn(second, ctx.my_bench())
        self.assertIn(first, second.children)
        self.assertIn(basic, second.children)
        self.assertIs(ctx.my_active(), ctx.attacker)
        ctx.shuffle_deck.assert_awaited_once()

    async def test_ultra_evolution_uses_the_named_stage_two_not_the_hand(self):
        rig, e, ctx = self.ctx(self.path_for('SM6', 6), 'Ultra Evolution')
        evolution = self.add(rig, self.definition_named('Vivillon'), P1, 'deck')
        ctx.flip_coins = AsyncMock(return_value=[True])
        ctx.choose_cards = AsyncMock(side_effect=lambda cards, count, **kw: [evolution] if evolution in cards else [])
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertIs(ctx.my_active(), evolution)
        self.assertIn(ctx.attacker, evolution.children)
        self.assertNotIn(evolution, ctx.hand())
        ctx.shuffle_deck.assert_awaited_once()

    async def test_search_predicates_include_v_subclasses_and_both_evolution_stages(self):
        from spirit.game.card_effects.bw_era import _ability_search_predicate
        rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        v = self.add(rig, self.definition_named('Corviknight V'), P1, 'deck')
        vmax = self.add(rig, fixtures.definition('SWSH5.CorviknightVMAX_110'), P1, 'deck')
        basic = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'deck')
        predicate = _ability_search_predicate('search your deck for a pokémon v')
        self.assertTrue(predicate(v))
        self.assertTrue(predicate(vmax))
        self.assertFalse(predicate(basic))
        predicate = _ability_search_predicate('stage 1 or stage 2 pokémon')
        self.assertTrue(predicate(self.add(rig, fixtures.definition('BW1.Servine_3'), P1, 'deck')))
        self.assertTrue(predicate(self.add(rig, fixtures.definition('BW1.Serperior_5'), P1, 'deck')))
        self.assertFalse(predicate(basic))
