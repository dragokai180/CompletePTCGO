"""Original PTCGO V-UNION prints, rule actions, effects and wire lifecycle."""
import json
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, CardType, PokemonStage, PokemonTypes as T, SpecialConditions, TrainerType, FoilEffects
from spirit.game.data_utils import ABILITIES_BY_ID, CARD_DEFS_BY_GUID, def_for, Attack, prize_value
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext, full_stack, split_pokemon_stack
from spirit.game.session.legal_actions import _out_of_zone_ability_entries, _ability_entries, ability_condition_met
from spirit.game.session.passives import effective_max_hp, attack_effects_blocked, trainer_effects_blocked
from spirit.game.vunion import SPECS, VUnionPokemonEntity, assemble, can_assemble, assembled_definition
from spirit.tools.effect_smoke import Rig, P1, P2


class VUnionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    add = fixtures.HgssRulesTests.add

    def rig(self):
        rig = Rig(self.filler, self.filler, self.energies, self.item)
        rig.setup('pokemon')
        return rig

    def parts(self, rig, name='Mewtwo', pid=P1, zone='discard'):
        start = SPECS[name][0]
        return [self.add(rig, definition(f'Promo_SWSH.{name}VUNION_{n}'), pid, zone)
                for n in range(start, start + 4)]

    async def assembled(self, name='Mewtwo', pid=P1):
        rig = self.rig()
        parts = self.parts(rig, name, pid)
        ability = def_for(parts[0].archetype_id).abilities[0]
        ctx = EffectContext(rig.session, pid, parts[0], ability)
        pokemon = await assemble(ctx)
        self.assertIsInstance(pokemon, VUnionPokemonEntity)
        return rig, ctx, pokemon, parts

    def attack_context(self, rig, pokemon, title):
        ability = next(a for a in def_for(pokemon.archetype_id).abilities if a.title == title)
        return EffectContext(rig.session, pokemon.owning_player_id, pokemon, ability)

    def energy(self, rig, kind, zone='discard', pid=P1):
        return self.add(rig, def_for(self.energies[kind]), pid, zone)

    def durable(self, target, hp=2000):
        target.set_attribute(AttrID.HP, hp)
        target.attribute_originals[AttrID.HP.value] = hp
        target.set_attribute(AttrID.WEAKNESS_TYPES, [])
        target.set_attribute(AttrID.RESISTANCE_TYPES, 0)

    def test_twenty_physical_prints_no_phantom_collectible_or_fragment_attacks(self):
        models = [c for c in loader.cards if c.get_attribute_value(AttrID.STAGE) == PokemonStage.VUNION]
        self.assertEqual(len(models), 20)
        for model in models:
            d = def_for(model.guid)
            self.assertTrue(d.vunion_part)
            self.assertIsNone(model.get_attribute_value(AttrID.HP))
            self.assertEqual(len(d.abilities), 1)
            self.assertTrue(d.abilities[0].is_rule_action)
            self.assertFalse(isinstance(d.abilities[0], Attack))
        for name in SPECS:
            assembled = assembled_definition(name)
            self.assertNotIn(assembled.guid, CARD_DEFS_BY_GUID)
            self.assertNotIn(assembled.guid, loader.cards_by_guid)
            self.assertEqual(prize_value(assembled.guid), 3)

    @unittest.skipUnless(Path('tools/card-builder/data/pokemon-tcg-data/cards/en/swshp.json').is_file(),
                         'Optional printed metadata snapshot not installed')
    def test_all_twenty_attacks_match_printed_cost_and_damage(self):
        data = json.loads(Path('tools/card-builder/data/pokemon-tcg-data/cards/en/swshp.json').read_text(encoding='utf-8'))
        for name, spec in SPECS.items():
            printed = next(c for c in data if c['number'] == f'SWSH{spec[0]}')
            attacks = [a for a in assembled_definition(name).abilities if isinstance(a, Attack)]
            self.assertEqual(len(attacks), 4)
            for attack, original in zip(attacks, printed['attacks']):
                with self.subTest(name=name, attack=attack.title):
                    self.assertEqual(attack.title, original['name'])
                    self.assertEqual(sum(attack.cost.values()), original['convertedEnergyCost'])
                    self.assertEqual(attack.damage, int(original['damage'].replace('×', '') or 0))
                    self.assertEqual(attack.effect is None, not bool(original['text']))

    async def test_requires_four_different_owned_parts_in_discard(self):
        rig = self.rig()
        parts = self.parts(rig)
        ctx = EffectContext(rig.session, P1, parts[0], def_for(parts[0].archetype_id).abilities[0])
        rig.to_area(parts[-1], P1, 'hand')
        duplicate = self.add(rig, def_for(parts[0].archetype_id), P1, 'discard')
        self.assertFalse(can_assemble(rig.board, P1, parts[0]))
        self.assertIsNone(await assemble(ctx))
        rig.to_area(parts[-1], P2, 'discard')
        self.assertFalse(can_assemble(rig.board, P1, parts[0]))
        rig.to_area(parts[-1], P1, 'discard')
        self.assertTrue(can_assemble(rig.board, P1, parts[0]))
        pokemon = await assemble(ctx)
        self.assertCountEqual(pokemon.physical_parts, parts)
        self.assertEqual(duplicate._containing_area_name(), 'discard')

    async def test_not_basic_not_evolution_not_benchable_as_individual_fragment(self):
        rig = self.rig()
        part = self.parts(rig, zone='hand')[0]
        ctx = EffectContext(rig.session, P1, part, None)
        self.assertFalse(ctx.can_bench_pokemon(part))
        self.assertFalse(await ctx.bench_pokemon(part))
        self.assertFalse(can_assemble(rig.board, P1, part))

    async def test_full_bench_and_ability_suppression(self):
        rig = self.rig()
        parts = self.parts(rig)
        rig.session.turn_state.abilities_disabled_through_turn = 100
        entries = _out_of_zone_ability_entries(rig.board, rig.session.turn_state, P1, rig.session.game_id)
        ids = {e['selectableAction']['actionID'] for e in entries}
        self.assertIn(def_for(parts[0].archetype_id).abilities[0].ability_id, ids)
        bench = rig.board.find_player_area(P1, 'bench')
        while len(bench.children) < 5:
            self.add(rig, self.filler, P1, 'bench')
        self.assertFalse(can_assemble(rig.board, P1, parts[0]))

    async def test_once_per_name_per_player_survives_turn_changes(self):
        rig, ctx, pokemon, parts = await self.assembled()
        await ctx.discard_cards([pokemon])
        rig.session.turn_state.begin_turn(P2)
        rig.session.turn_state.begin_turn(P1)
        self.assertFalse(can_assemble(rig.board, P1, parts[0]))
        other_name = self.parts(rig, 'Pikachu')
        self.assertTrue(can_assemble(rig.board, P1, other_name[0]))
        other_owner = self.parts(rig, 'Mewtwo', P2)
        self.assertTrue(can_assemble(rig.board, P2, other_owner[0]))

    async def test_all_five_wire_faces_stats_and_physical_lifecycle(self):
        for name, spec in SPECS.items():
            for owner in (P1, P2):
                with self.subTest(name=name, owner=owner):
                    rig, ctx, pokemon, parts = await self.assembled(name, owner)
                    self.assertEqual(effective_max_hp(rig.board, pokemon), spec[2])
                    self.assertEqual(pokemon.get_attribute(AttrID.IMAGE_URL), f'{spec[0]}to{spec[0]+3}')
                    self.assertFalse(pokemon.get_attribute(AttrID.IS_LEGEND))
                    self.assertCountEqual(split_pokemon_stack(pokemon)[0], parts)
                    self.assertCountEqual(full_stack(pokemon), parts)
                    self.assertEqual(pokemon.serialize(owner)['children'], [])
                    for viewer in (P1, P2):
                        tree = rig.board.serialize(viewer)['entities']
                        def all_ids(entity):
                            return [entity['entityID']] + [i for c in entity['children'] for i in all_ids(c)]
                        ids = all_ids(tree)
                        for part in parts:
                            self.assertEqual(ids.count(part.entity_id), 1)
                    await ctx.put_in_hand([pokemon])
                    self.assertIsNone(rig.board.get_entity(pokemon.entity_id))
                    self.assertTrue(all(p._containing_area_name() == 'hand' for p in parts))

    async def test_native_creation_has_four_parts_and_playcard_final_move(self):
        rig, ctx, pokemon, parts = await self.assembled()
        senders = {pid: AsyncMock() for pid in (P1, P2)}
        with patch.object(rig.session.players[P1], 'send_packet', senders[P1]), \
                patch.object(rig.session.players[P2], 'send_packet', senders[P2]):
            await ctx.flush_choreography()
        for sender in senders.values():
            messages = [call.args[1]['msg'] for call in sender.await_args_list]
            sequences = [m['value']['name'] for m in messages if m['name'] == 'StartSequence']
            self.assertIn('CreateVUnion', sequences)
            self.assertIn('AttachToVUnion', sequences)
            self.assertIn('PlayCard', sequences)
            moves = [m['value']['entityID'] for m in messages if m['name'] == 'EntityMoved']
            self.assertEqual(moves, [p.entity_id for p in parts] + [pokemon.entity_id])

    async def test_union_gain_all_types_up_to_two_and_preserves_energy_identity(self):
        for name, spec in SPECS.items():
            rig, _, pokemon, _ = await self.assembled(name)
            ctx = self.attack_context(rig, pokemon, 'Union Gain')
            energies = [self.energy(rig, spec[1]) for _ in range(3)]
            wrong = self.energy(rig, T.FIRE)
            ctx.choose_cards = AsyncMock(return_value=energies[:2])
            await ctx.ability.effect(ctx)
            offered = ctx.choose_cards.await_args.args[0]
            self.assertNotIn(wrong, offered)
            self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 0)
            self.assertTrue(all(e.parent is pokemon for e in energies[:2]))
            self.assertEqual(energies[-1]._containing_area_name(), 'discard')

    async def test_shocking_shock_coin_and_disconnect_item_lock(self):
        rig, _, pokemon, _ = await self.assembled('Pikachu')
        self.durable(rig.board.active_pokemon(P2))
        ctx = self.attack_context(rig, pokemon, 'Shocking Shock')
        ctx.flip_coins = AsyncMock(return_value=[False])
        await ctx.ability.effect(ctx)
        self.assertFalse(ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS))
        ctx.flip_coins = AsyncMock(return_value=[True])
        await ctx.ability.effect(ctx)
        self.assertIn('Paralyzed', ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS))
        ctx = self.attack_context(rig, pokemon, 'Disconnect')
        await ctx.ability.effect(ctx)
        item = self.add(rig, self.item, P2, 'hand')
        self.assertTrue(rig.session.turn_state.play_locked(P2, item))

    async def test_greninja_bench_damage_and_retreat_lock(self):
        rig, _, pokemon, _ = await self.assembled('Greninja')
        targets = rig.board.pokemon_in_play(P2)
        for target in targets:
            self.durable(target)
        ctx = self.attack_context(rig, pokemon, 'Twister Shuriken')
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.defender.get_attribute(AttrID.HP), 2000)
        self.assertTrue(all(t.get_attribute(AttrID.HP) == 1900 for t in ctx.opponent_bench()))
        ctx = self.attack_context(rig, pokemon, 'Waterfall Blind')
        await ctx.ability.effect(ctx)
        self.assertTrue(rig.session.turn_state.retreat_locked(ctx.defender.entity_id))

    async def test_greninja_abilities_and_item_only_shield(self):
        rig, _, pokemon, _ = await self.assembled('Greninja')
        ctx = self.attack_context(rig, pokemon, 'Feel the Way')
        ctx.reveal_hand = AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        ctx.reveal_hand.assert_awaited_once_with(P2, P1)
        item = self.add(rig, self.item, P2, 'hand')
        self.assertTrue(trainer_effects_blocked(rig.board, P1, item, pokemon))
        item.set_attribute(AttrID.TRAINER_TYPE, TrainerType.SUPPORTER)
        self.assertFalse(trainer_effects_blocked(rig.board, P1, item, pokemon))
        attack = EffectContext(rig.session, P2, rig.board.active_pokemon(P2), Attack(title='Test', damage=0))
        self.assertFalse(await attack.apply_special_condition(pokemon, SpecialConditions.POISONED))

    async def test_mewtwo_heal_and_sixteen_counters_and_effect_not_damage_shield(self):
        rig, _, pokemon, _ = await self.assembled('Mewtwo')
        pokemon.set_attribute(AttrID.HP, 50)
        ctx = self.attack_context(rig, pokemon, 'Super Regeneration')
        await ctx.ability.effect(ctx)
        self.assertEqual(pokemon.get_attribute(AttrID.HP), 250)
        for target in rig.board.pokemon_in_play(P2):
            self.durable(target)
        ctx = self.attack_context(rig, pokemon, 'Psysplosion')
        targets = ctx.opponent_pokemon_in_play()
        rig.session.prompt_damage_counter_placement = AsyncMock(return_value={targets[0].entity_id: 5, targets[1].entity_id: 11})
        await ctx.ability.effect(ctx)
        self.assertEqual(targets[0].get_attribute(AttrID.HP), 1950)
        self.assertEqual(targets[1].get_attribute(AttrID.HP), 1890)
        rig.session.prompt_damage_counter_placement.assert_awaited_once()
        self.assertTrue(attack_effects_blocked(rig.board, pokemon))
        hostile = EffectContext(rig.session, P2, targets[0], Attack(title='Test', damage=20))
        await hostile.deal_damage(20, pokemon)
        self.assertEqual(pokemon.get_attribute(AttrID.HP), 230)
        self.assertFalse(await hostile.apply_special_condition(pokemon, SpecialConditions.PARALYZED))

    async def test_zacian_reduction_and_master_blade_preserve_parts(self):
        rig, _, pokemon, parts = await self.assembled('Zacian')
        self.durable(rig.board.active_pokemon(P2))
        ctx = self.attack_context(rig, pokemon, 'Dance of the Crowned Sword')
        await ctx.ability.effect(ctx)
        target = rig.board.active_pokemon(P1)
        self.durable(target)
        reply = EffectContext(rig.session, P2, ctx.defender, Attack(title='Test', damage=200))
        await reply.deal_damage(200, target)
        self.assertEqual(target.get_attribute(AttrID.HP), 1950)
        energy = [self.energy(rig, T.METAL) for _ in range(3)]
        for e in energy:
            rig.attach(e, pokemon)
        ctx = self.attack_context(rig, pokemon, 'Master Blade')
        await ctx.ability.effect(ctx)
        self.assertTrue(all(e._containing_area_name() == 'discard' for e in energy))
        self.assertTrue(all(p.parent is pokemon for p in parts))

    async def test_morpeko_draw_until_ten_and_burst_counts_cards_not_units(self):
        rig, _, pokemon, _ = await self.assembled('Morpeko')
        ctx = self.attack_context(rig, pokemon, 'All You Can Eat')
        for card in list(ctx.hand()):
            rig.to_area(card, P1, 'deck')
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.hand()), 10)
        self.durable(ctx.defender)
        first = self.energy(rig, T.LIGHTNING)
        second = self.add(rig, definition('HGSS1.DoubleColorlessEnergy_103'), P1, 'discard')
        rig.attach(first, pokemon)
        rig.attach(second, pokemon)
        ctx = self.attack_context(rig, pokemon, 'Burst Wheel')
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.defender.get_attribute(AttrID.HP), 1800)
        self.assertEqual(ctx.attached_energies(pokemon), [])

    async def test_native_half_type_foil_and_missing_hp_searches(self):
        rig = self.rig()
        parts = self.parts(rig)
        from spirit.game.card_effects.bw_era import _ability_search_predicate
        from importlib import import_module
        level = import_module('spirit.game.scripts.cards.SWSH5.LevelBall_129')
        for part in parts:
            self.assertEqual(part.client_card_type(), CardType.LEGEND_HALF)
            self.assertTrue(part.get_entity_name().endswith('.HalfLegend'))
            self.assertFalse(part.get_attribute(AttrID.IS_LEGEND))
            self.assertEqual(part.get_attribute(AttrID.HP), 0)
            self.assertFalse(level._hp_90_or_less(part))
            self.assertFalse(_ability_search_predicate('search your deck for a pokémon with 90 hp or less')(part))
            self.assertEqual(part.get_attribute(AttrID.FOIL_EFFECT), FoilEffects.SUNPILLAR)

    async def test_all_vanilla_attacks_and_dynamic_panel_keep_complete_attacks(self):
        for name in SPECS:
            rig, _, pokemon, _ = await self.assembled(name)
            entries = rig.session._pie_ability_entries(pokemon)
            attacks = [ABILITIES_BY_ID[e['abilityID']] for e in entries if isinstance(ABILITIES_BY_ID[e['abilityID']], Attack)]
            self.assertEqual(len(attacks), 4)
            for attack in attacks:
                if attack.effect is not None:
                    continue
                target = rig.board.active_pokemon(P2)
                self.durable(target)
                ctx = EffectContext(rig.session, P1, pokemon, attack)
                await ctx.deal_damage()
                self.assertEqual(target.get_attribute(AttrID.HP), 2000 - attack.damage)
            rig.session.credit_card_damage(P1, pokemon, 10)
            self.assertIn(rig.session._mvp_for(P1)[0], loader.cards_by_guid)

    async def test_ko_all_five_give_three_prizes_and_choose_replacement(self):
        for name in SPECS:
            rig, ctx, pokemon, parts = await self.assembled(name)
            await ctx.switch_active(P1, pokemon)
            await ctx.flush_choreography()
            damage = EffectContext(rig.session, P2, rig.board.active_pokemon(P2), None)
            with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
                await damage.deal_damage(2000, pokemon)
                await rig.session.resolve_knockouts(damage)
            self.assertEqual(prizes.await_args.args[:2], (P2, 3))
            self.assertIsNotNone(rig.board.active_pokemon(P1))
            self.assertIsNone(rig.board.get_entity(pokemon.entity_id))
            self.assertTrue(all(p._containing_area_name() == 'discard' for p in parts))
            self.assertFalse(can_assemble(rig.board, P1, parts[0]))

    async def test_returning_to_deck_lostzone_and_discard_moves_all_four_not_wrapper(self):
        for destination in ('deck', 'lostZone', 'discard'):
            rig, ctx, pokemon, parts = await self.assembled()
            if destination == 'deck':
                await ctx.shuffle_into_deck([pokemon])
            elif destination == 'lostZone':
                await ctx.move_to_lost_zone([pokemon])
            else:
                await ctx.discard_cards([pokemon])
            self.assertTrue(all(p._containing_area_name() == destination for p in parts))
            self.assertIsNone(rig.board.get_entity(pokemon.entity_id))

    async def test_union_gain_does_not_take_special_energy_with_no_type_in_discard(self):
        rig, _, pokemon, _ = await self.assembled('Greninja')
        ctx = self.attack_context(rig, pokemon, 'Union Gain')
        splash = self.add(rig, definition('XY9.SplashEnergy_113'), P1, 'discard')
        ctx.choose_cards = AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        self.assertNotIn(splash, ctx.choose_cards.await_args.args[0])
        self.assertEqual(splash._containing_area_name(), 'discard')

    async def test_antidote_recovers_after_ability_lock_ends_without_curing_other_conditions(self):
        rig, ctx, pokemon, _ = await self.assembled('Greninja')
        await ctx.switch_active(P1, pokemon)
        pokemon.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned', 'Burned'])
        rig.session.turn_state.abilities_disabled_through_turn = 100
        await rig.session.sync_player_visualizations()
        self.assertIn('Poisoned', pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS))
        rig.session.turn_state.abilities_disabled_through_turn = 0
        await rig.session.sync_player_visualizations()
        self.assertEqual(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS), ['Burned'])

    async def test_master_blade_can_pay_three_units_with_two_cards(self):
        rig, _, pokemon, _ = await self.assembled('Zacian')
        self.durable(rig.board.active_pokemon(P2))
        double = self.add(rig, definition('HGSS1.DoubleColorlessEnergy_103'), P1, 'hand')
        single = self.energy(rig, T.METAL)
        rig.attach(double, pokemon)
        rig.attach(single, pokemon)
        ctx = self.attack_context(rig, pokemon, 'Master Blade')
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.attached_energies(pokemon), [])

    async def test_assembly_rule_is_executable_while_abilities_disabled(self):
        rig = self.rig()
        parts = self.parts(rig)
        rig.session.turn_state.abilities_disabled_through_turn = 100
        ability = def_for(parts[0].archetype_id).abilities[0]
        self.assertTrue(ability_condition_met(ability, rig.board, P1, parts[0]))
        await rig.session._execute_use_ability(P1, parts[0], {'selectableAction': {'actionID': ability.ability_id}})
        self.assertTrue(any(isinstance(p, VUnionPokemonEntity) for p in rig.board.pokemon_in_play(P1)))


if __name__ == '__main__':
    unittest.main()
