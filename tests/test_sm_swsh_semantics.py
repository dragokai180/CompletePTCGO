"""SM/SWSH target, energy, and persistent-GX semantic regressions."""
import unittest
from importlib import import_module
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.pokemon import energy_card_types
from spirit.game.card_effects.standard_era import _search_predicate
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import compute_damage, active_passives
from spirit.tools.effect_smoke import P1, P2


class SmSwshSemanticTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def clear_energy(self, rig, pokemon):
        for energy in list(rig.board.attached_energies(pokemon)):
            rig.to_area(energy, pokemon.owning_player_id, 'discard')

    async def test_tag_call_accepts_only_tag_teams_including_supporters(self):
        rig, e = self.rig('SM12.TagCall_206', 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        tag_pokemon = self.add(rig, fixtures.definition(
            'SM12.ArceusDialgaPalkiaGX_156'), P1, 'deck')
        tag_supporter = self.add(rig, fixtures.definition(
            'SM12.CynthiaCaitlin_189'), P1, 'deck')
        predicate = _search_predicate("search your deck for up to 2 tag team cards")
        self.assertTrue(predicate(tag_pokemon))
        self.assertTrue(predicate(tag_supporter))
        self.assertFalse(predicate(ctx.my_active()))
        self.assertFalse(predicate(e['target']))
        self.assertFalse(predicate(next(c for c in ctx.hand() if energy_card_types(c))))
        ctx.search_deck = AsyncMock(return_value=[tag_pokemon, tag_supporter])
        ctx.reveal_cards = AsyncMock()
        await fixtures.definition('SM12.TagCall_206').effect(ctx)
        call = ctx.search_deck.call_args
        self.assertEqual(call.kwargs['count'], 2)
        self.assertEqual(call.kwargs['minimum'], 0)
        self.assertTrue(call.args[0](tag_supporter))
        self.assertFalse(call.args[0](ctx.my_active()))
        self.assertIn(tag_pokemon, ctx.hand())
        self.assertIn(tag_supporter, ctx.hand())

    async def test_power_accelerator_deals_damage_and_attaches_darkness_to_bench(self):
        rig, e, ctx = self.ctx('SWSH3.EternatusV_116', 'Power Accelerator')
        dark = rig.pull_guid(P1, self.energies[PokemonTypes.DARKNESS.value])
        rig.to_area(dark, P1, 'hand')
        target = ctx.my_bench()[0]
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.choose_cards = AsyncMock(return_value=[dark])
        ctx.choose_pokemon = AsyncMock(return_value=target)
        hp = ctx.defender.get_attribute(AttrID.HP)
        expected = compute_damage(rig.board, ctx.attacker, ctx.defender, 30).amount
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.defender.get_attribute(AttrID.HP), hp - expected)
        self.assertIn(dark, rig.board.attached_energies(target))
        self.assertNotIn(ctx.my_active(), ctx.choose_pokemon.call_args.args[0])
        self.assertTrue(all(PokemonTypes.DARKNESS.value in energy_card_types(c)
                            for c in ctx.choose_cards.call_args.args[0]))

    async def test_power_accelerator_without_energy_still_deals_damage(self):
        rig, e, ctx = self.ctx('SWSH3.EternatusV_116', 'Power Accelerator')
        for card in list(ctx.hand()):
            rig.to_area(card, P1, 'deck')
        ctx.ask_yes_no = AsyncMock()
        hp = ctx.defender.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        self.assertLess(ctx.defender.get_attribute(AttrID.HP), hp)
        ctx.ask_yes_no.assert_not_awaited()

    async def test_altered_creation_is_permanent_active_only_and_prize_requires_damage(self):
        rig, e, ctx = self.ctx('SM12.ArceusDialgaPalkiaGX_156', 'Altered Creation-GX')
        self.clear_energy(rig, ctx.attacker)
        for kind in (PokemonTypes.METAL, PokemonTypes.WATER):
            rig.attach_energy_type(P1, ctx.attacker, kind.value)
        await ctx.ability.effect(ctx)
        rule = rig.board.temporary_passives[-1].passive
        self.assertEqual(rule.extra_prizes, 1)
        for pid in (P2, P1, P2, P1):
            rig.session.turn_state.begin_turn(pid, rig.board)
        target = ctx.defender
        target.set_attribute(AttrID.WEAKNESS_TYPES, [])
        target.set_attribute(AttrID.RESISTANCE_TYPES, [])
        self.assertEqual(compute_damage(rig.board, ctx.attacker, target, 100).amount, 130)
        self.assertEqual(compute_damage(rig.board, ctx.attacker, ctx.opponent_bench()[0], 100).amount, 100)
        self.assertEqual(compute_damage(rig.board, ctx.attacker, ctx.my_bench()[0], 100).amount, 100)
        self.assertEqual(compute_damage(rig.board, ctx.attacker, target, 100, is_attack=False).amount, 100)
        # The actual KO resolver passes attack_damage, not ko_from_attack.
        ctx.attack_damage[target.entity_id] = (150, 100)
        self.assertEqual(rule.modify_prizes_for_knockout(target, ctx, 1, None), 2)
        bench = ctx.opponent_bench()[0]
        ctx.attack_damage[bench.entity_id] = (150, 100)
        self.assertEqual(rule.modify_prizes_for_knockout(bench, ctx, 1, None), 1)
        ctx.attack_damage.clear()
        self.assertEqual(rule.modify_prizes_for_knockout(target, ctx, 1, None), 1)
        rig.to_area(ctx.attacker, P1, 'discard')
        self.assertIn(rule, [p for p, c in active_passives(rig.board)])
        other = ctx.my_bench()[0]
        self.assertEqual(compute_damage(rig.board, other, target, 100).amount, 130)

    async def test_altered_creation_extra_water_is_in_addition_to_cost(self):
        rainbow_def = next(d for d in CARD_DEFS_BY_GUID.values()
                           if d.display_name == 'Rainbow Energy' and d.set_code == 'SM1')
        for count in (1, 2):
            with self.subTest(rainbows=count):
                rig, e, ctx = self.ctx('SM12.ArceusDialgaPalkiaGX_156', 'Altered Creation-GX')
                self.clear_energy(rig, ctx.attacker)
                for _ in range(count):
                    rig.attach(self.add(rig, rainbow_def, P1, 'hand'), ctx.attacker)
                await ctx.ability.effect(ctx)
                rule = rig.board.temporary_passives[-1].passive
                self.assertEqual(rule.damage_boost, 30)
                self.assertEqual(rule.extra_prizes, count - 1)

    async def test_basic_energy_types_and_representative_typed_filters(self):
        rig, e = self.rig('SWSH3.EternatusV_116')
        filters = [
            ('SWSH3.EternatusV_116', '_is_darkness_energy', PokemonTypes.DARKNESS),
            ('SWSH4.Nessa_157', 'is_water_energy_card', PokemonTypes.WATER),
            ('SWSH10.DarkPatch_139', '_is_basic_darkness_energy', PokemonTypes.DARKNESS),
            ('SWSH1.Frosmoth_64', '_is_water_energy_card', PokemonTypes.WATER),
            ('PGO.Solrock_39', '_is_psychic_energy_card', PokemonTypes.PSYCHIC),
            ('SWSH9.Kindler_143', '_is_fire_energy_card', PokemonTypes.FIRE),
        ]
        for module, name, wanted in filters:
            predicate = getattr(import_module('spirit.game.scripts.cards.' + module), name)
            for kind, guid in self.energies.items():
                energy = rig.pull_guid(P1, guid)
                if energy is None:
                    continue
                rig.to_area(energy, P1, 'hand')
                with self.subTest(module=module, kind=kind):
                    self.assertEqual(energy_card_types(energy), [kind])
                    self.assertEqual(predicate(energy), kind == wanted.value)
            self.assertFalse(predicate(e['target']))

    async def test_frozen_breath_optional_numbered_discard_applies_paralysis(self):
        for accept in (False, True):
            rig, e, ctx = self.ctx('SM2.Vanilluxe_35', 'Frozen Breath')
            self.clear_energy(rig, ctx.attacker)
            for _ in range(2):
                rig.attach_energy_type(P1, ctx.attacker, PokemonTypes.WATER.value)
            ctx.ask_yes_no = AsyncMock(return_value=accept)
            before = set(ctx.attached_energies(ctx.attacker))
            await ctx.ability.effect(ctx)
            self.assertEqual(bool('Paralyzed' in (ctx.defender.get_attribute(
                AttrID.SPECIAL_CONDITIONS) or [])), accept)
            self.assertEqual(len(ctx.attached_energies(ctx.attacker)), 0 if accept else 2)
            if accept:self.assertTrue(before.issubset(set(ctx.discard_pile())))

    async def test_surprise_fist_uses_damage_not_unrelated_draw_and_mill(self):
        for picks, expected in (([1, 0], 120), ([0, 1], 60)):
            rig, e, ctx = self.ctx('SM10.Pyukumuku_53', 'Surprise Fist')
            ctx.choose = AsyncMock(side_effect=picks)
            ctx.deal_damage = AsyncMock()
            ctx.draw_cards = AsyncMock()
            ctx.discard_cards = AsyncMock()
            await ctx.ability.effect(ctx)
            ctx.deal_damage.assert_awaited_once_with(expected)
            ctx.draw_cards.assert_not_awaited()
            ctx.discard_cards.assert_not_awaited()

    async def test_special_energy_types_exist_only_in_play_all_printings(self):
        names = {'Hiding Darkness Energy', 'Wash Water Energy', 'Aurora Energy',
                 'Heat Fire Energy', 'Horror Psychic Energy', 'Speed Lightning Energy',
                 'Aromatic Grass Energy', 'Stone Fighting Energy', 'Coating Metal Energy',
                 'Single Strike Energy', 'Rapid Strike Energy', 'Impact Energy',
                 'Spiral Energy', 'Fusion Strike Energy'}
        rig, e = self.rig('SWSH3.EternatusV_116')
        definitions = [d for d in CARD_DEFS_BY_GUID.values() if d.display_name in names]
        self.assertGreater(len(definitions), len(names))
        for definition in definitions:
            with self.subTest(name=definition.display_name, set=definition.set_code,
                              number=definition.collector_number):
                energy = self.add(rig, definition, P1, 'hand')
                self.assertEqual(energy_card_types(energy), [])
                rig.attach(energy, e['target'])
                self.assertTrue(energy_card_types(energy))
                rig.to_area(energy, P1, 'discard')
                self.assertEqual(energy_card_types(energy), [])

    async def test_conditional_heals_require_regice_or_poison(self):
        from spirit.game.attributes import SpecialConditions
        for path, title, needs_poison, amount in (
            ('SM4.Registeel_68', 'Iron Hand', False, 30),
            ('Promo_SM.Registeel_75', 'Iron Fist', False, 30),
            ('SM10.MukAlolanMukGX_61', 'Poison Absorption', True, 100),
        ):
            for qualified in (False, True):
                rig, e, ctx = self.ctx(path, title)
                maximum = ctx.max_hp(ctx.attacker)
                ctx.attacker.set_attribute(AttrID.HP, maximum - 100)
                if qualified:
                    if needs_poison:
                        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
                    else:
                        self.add(rig, fixtures.definition('SM4.Regice_28'), P1, 'bench')
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.attacker.get_attribute(AttrID.HP),
                                 maximum - 100 + (amount if qualified else 0))
