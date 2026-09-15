"""Conditional SM audit scenarios with rule-outcome assertions."""
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.game.session.passives import (
    effective_attack_cost, effective_max_hp, extra_manual_energy_attachments,
    energy_provided_options, compute_damage,
)
from spirit.tools.effect_smoke import P1, P2


class SmConditionalCoverageTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def energy(self, rig, owner=P1, kind=PokemonTypes.GRASS):
        return self.add(rig, CARD_DEFS_BY_GUID[self.energies[kind.value].lower()], owner, 'hand')

    def playable(self, rig, source, definition):
        return trainer_condition_met(definition.condition, rig.board, P1, source)

    async def test_energy_evolution_optional_and_matches_energy_type(self):
        for accept in (False, True):
            rig, e = self.rig('SM1.Eevee_101')
            rig.session.turn_state.active_player_id = P1
            source = e['target']
            rig.session.turn_state.bonus_energy_target_id = source.entity_id
            psychic = self.energy(rig, kind=PokemonTypes.PSYCHIC)
            evolution = self.add(rig, fixtures.definition('SM1.EspeonGX_61'), P1, 'deck')
            wrong = self.add(rig, fixtures.definition('SM12.Flareon_25'), P1, 'deck')
            rig.attach(psychic, source)
            with patch.object(EffectContext, 'ask_yes_no', AsyncMock(return_value=accept)), \
                 patch.object(EffectContext, 'search_deck', AsyncMock(return_value=[evolution])) as search, \
                 patch.object(EffectContext, 'shuffle_deck', AsyncMock()) as shuffle:
                await rig.session.fire_energy_attached_triggers(P1, psychic, source)
            self.assertEqual(search.await_count, int(accept))
            self.assertEqual(shuffle.await_count, int(accept))
            if accept:
                predicate = search.call_args.args[0]
                self.assertTrue(predicate(evolution))
                self.assertFalse(predicate(wrong))
                self.assertIn(evolution, rig.board.pokemon_in_play(P1))
                self.assertIs(source.parent, evolution)
                self.assertEqual(rig.session.turn_state.bonus_energy_target_id, evolution.entity_id)

    async def test_energy_evolution_does_not_trigger_for_special_or_deck_attachment(self):
        for special in (False, True):
            rig, e = self.rig('SM1.Eevee_101')
            energy = self.add(rig, fixtures.definition('SM11.RecycleEnergy_212'), P1, 'hand') if special else self.energy(rig)
            ctx = EffectContext(rig.session, P1, e['target'], None)
            with patch.object(EffectContext, 'search_deck', AsyncMock()) as search:
                await ctx.attach_energy(energy, e['target'])
                if special: await rig.session.fire_energy_attached_triggers(P1, energy, e['target'])
            search.assert_not_awaited()

    async def test_harmonics_friendly_only_and_not_stacking(self):
        rig, e = self.rig('SM8.Primarina_67')
        self.add(rig, fixtures.definition('SM8.Primarina_67'), P1, 'bench')
        for pokemon in rig.board.pokemon_in_play(P1):
            self.assertEqual(extra_manual_energy_attachments(rig.board, pokemon), 1)
        for pokemon in rig.board.pokemon_in_play(P2):
            self.assertEqual(extra_manual_energy_attachments(rig.board, pokemon), 0)
        ctx = EffectContext(rig.session, P1, e['target'], None)
        state = rig.session.turn_state
        before = state.energy_attachments_this_turn
        await ctx.attach_energy(self.energy(rig), e['target'])
        self.assertEqual(state.energy_attachments_this_turn, before)
        self.assertIsNone(state.bonus_energy_target_id)

    async def test_speed_cheer_does_not_stack_or_apply_to_non_gx(self):
        rig, e = self.rig('SM12.Jolteon_70')
        self.add(rig, fixtures.definition('SM12.Jolteon_70'), P1, 'bench')
        gx = self.add(rig, fixtures.definition('SM1.EspeonGX_61'), P1, 'bench')
        cost = {'Colorless': 3, 'Psychic': 1}
        self.assertEqual(effective_attack_cost(rig.board, gx, cost), {'Colorless': 2, 'Psychic': 1})
        self.assertEqual(effective_attack_cost(rig.board, e['target'], cost), cost)
        opposing = self.add(rig, fixtures.definition('SM1.EspeonGX_61'), P2, 'bench')
        self.assertEqual(effective_attack_cost(rig.board, opposing, cost), cost)

    async def test_jungle_totem_doubles_only_own_basic_grass_not_repeatedly(self):
        rig, e = self.rig('SL.Venusaur_3')
        self.add(rig, fixtures.definition('SL.Venusaur_3'), P1, 'bench')
        for owner, kind, count in ((P1,PokemonTypes.GRASS,2), (P2,PokemonTypes.GRASS,1), (P1,PokemonTypes.WATER,1)):
            energy = self.energy(rig, owner, kind)
            rig.attach(energy, rig.board.active_pokemon(owner))
            self.assertEqual(energy_provided_options(rig.board, energy), [[kind.value] * count])

    async def test_electrocharger_and_lure_ball_flip_and_recover_exact_heads(self):
        for path, recovered, zone, flips in (
            ('SM9.Electrocharger_139', 'SM8.Electropower_172', 'deck', [True, False]),
            ('SM7.LureBall_138', 'SM1.EspeonGX_61', 'hand', [True, False, True]),
        ):
            rig, e = self.rig(path, 'trainer')
            definition = fixtures.definition(path)
            ctx = EffectContext(rig.session, P1, e['target'], None)
            for c in list(ctx.discard_pile()): rig.to_area(c, P1, 'deck')
            self.assertFalse(self.playable(rig, e['target'], definition))
            cards = [self.add(rig, fixtures.definition(recovered), P1, 'discard') for _ in range(3)]
            self.assertTrue(self.playable(rig, e['target'], definition))
            ctx.flip_coins = AsyncMock(return_value=flips)
            ctx.choose_cards = AsyncMock(side_effect=lambda pool, n, **kw: pool[:n])
            await definition.effect(ctx)
            ctx.flip_coins.assert_awaited_once()
            self.assertEqual(ctx.flip_coins.call_args.args[0], len(flips))
            self.assertEqual(sum(c.parent is rig.board.find_player_area(P1, zone) for c in cards), sum(flips))
            self.assertEqual(ctx.choose_cards.call_args.kwargs['minimum'], sum(flips))
            ctx.flip_coins = AsyncMock(return_value=[False] * len(flips))
            ctx.choose_cards.reset_mock()
            await definition.effect(ctx)
            ctx.choose_cards.assert_not_awaited()

    async def test_dana_and_evelyn_opposing_stage_and_outcome(self):
        for path, required in (('SM9.Dana_137', PokemonStage.STAGE2), ('SM9.Evelyn_141', PokemonStage.STAGE1)):
            rig, e = self.rig(path, 'trainer')
            definition = fixtures.definition(path)
            ctx = EffectContext(rig.session, P1, e['target'], None)
            opponent = ctx.opponent_active()
            opponent.set_attribute(AttrID.STAGE, PokemonStage.BASIC.value)
            self.assertFalse(self.playable(rig, e['target'], definition))
            opponent.set_attribute(AttrID.STAGE, required.value)
            self.assertTrue(self.playable(rig, e['target'], definition))
            before = len(ctx.hand())
            await definition.effect(ctx)
            self.assertEqual(len(ctx.hand()) - before, 2 if required == PokemonStage.STAGE2 else 4)

    async def test_bursting_spores_observes_basic_and_evolution_plays_only_own_side(self):
        from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions
        for path, evolved, owner in (
            ('SM11.Foongus_13', False, P1), ('SM11.Breloom_108', True, P1),
            ('SM11.Foongus_13', False, P2),
        ):
            rig, e = self.rig('Promo_SM.Amoonguss_202')
            # Smoke fixtures contain more than one copy of the target.
            for pokemon in list(rig.board.pokemon_in_play(P1)):
                if pokemon is not e['target'] and pokemon.archetype_id == e['target'].archetype_id:
                    rig.to_area(pokemon, P1, 'discard')
            pokemon = self.add(rig, fixtures.definition(path), owner, 'bench')
            with patch.object(EffectContext, 'ask_yes_no', AsyncMock(return_value=True)) as ask:
                if evolved: await rig.session._fire_ally_evolved_triggers(owner, pokemon, None)
                else: await rig.session.fire_pokemon_benched_triggers(owner, pokemon)
            self.assertEqual(ask.await_count, int(owner == P1))
            if owner == P1:
                conditions = rig.board.active_pokemon(P2).get_attribute(AttrID.SPECIAL_CONDITIONS)
                self.assertIn(CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP], conditions)
                self.assertIn(CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED], conditions)

    async def test_hazardous_evolution_is_on_entry_and_sets_three_poison_counters(self):
        from spirit.game.data_utils import Triggers
        from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions
        rig, e = self.rig('SM8.Dustox_28')
        ability = fixtures.definition('SM8.Dustox_28').abilities[0]
        self.assertEqual(ability.trigger, Triggers.ON_EVOLVE)
        self.assertIsNone(ability.passive)
        ctx = EffectContext(rig.session, P1, e['target'], ability)
        await ability.effect(ctx)
        target = ctx.opponent_active()
        self.assertEqual(rig.session.poison_counters.get(target.entity_id), 3)
        conditions = target.get_attribute(AttrID.SPECIAL_CONDITIONS)
        for status in (SpecialConditions.PARALYZED, SpecialConditions.POISONED):
            self.assertIn(CLIENT_SPECIAL_CONDITION_NAMES[status], conditions)

    async def test_power_strong_and_vitality_cheer_do_not_stack(self):
        for path, kind in (('SM12.Flareon_25','damage'), ('SM10.Incineroar_29','damage'), ('SM12.Vaporeon_42','hp')):
            rig, e = self.rig(path)
            self.add(rig, fixtures.definition(path), P1, 'bench')
            attacker = self.add(rig, fixtures.definition('SM1.EspeonGX_61'), P1, 'bench')
            target = rig.board.active_pokemon(P2)
            if kind == 'hp':
                self.assertEqual(effective_max_hp(rig.board, attacker), 260)
                self.assertEqual(effective_max_hp(rig.board, target), target.attribute_originals[AttrID.HP.value])
            else:
                calc = compute_damage(rig.board, attacker, target, 10, ignore_weakness=True, ignore_resistance=True)
                self.assertEqual(calc.amount, 40)
                target = rig.board.pokemon_in_play(P2)[-1]
                self.assertEqual(compute_damage(rig.board, attacker, target, 10).amount, 10)

    async def test_blanket_weaver_and_armor_require_types_names_and_do_not_stack(self):
        for path in ('SM11.Leavanny_9', 'SM12.Solgaleo_142'):
            rig, e = self.rig(path)
            self.add(rig, fixtures.definition(path), P1, 'bench')
            target = e['target']
            attacker = rig.board.active_pokemon(P2)
            def damage():
                return compute_damage(rig.board, attacker, target, 100, ignore_weakness=True, ignore_resistance=True).amount
            if 'Solgaleo' in path:
                self.assertEqual(damage(), 100)
                self.add(rig, fixtures.definition('SM12.Lunala_102'), P1, 'bench')
                self.assertEqual(damage(), 50)
            else:
                self.assertEqual(damage(), 60)
                target.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
                self.assertEqual(damage(), 100)

    async def test_tag_switch_moves_up_to_two_special_or_basic_to_one_other_target(self):
        rig, e = self.rig('SM11.TagSwitch_209', 'trainer')
        definition = fixtures.definition('SM11.TagSwitch_209')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        self.assertFalse(self.playable(rig, e['target'], definition))
        source = self.add(rig, fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'), P1, 'bench')
        energies = [self.energy(rig), self.add(rig, fixtures.definition('SM11.RecycleEnergy_212'), P1, 'hand')]
        for energy in energies:rig.attach(energy, source)
        self.assertTrue(self.playable(rig, e['target'], definition))
        ctx.move_energy_freely = AsyncMock()
        await definition.effect(ctx)
        call = ctx.move_energy_freely.call_args
        self.assertEqual(call.args[0], [source])
        self.assertTrue(call.kwargs['single_source'])
        self.assertTrue(call.kwargs['single_destination'])
        self.assertEqual(call.kwargs['max_count'], 2)
        self.assertNotIn('predicate', call.kwargs)

    async def test_great_catcher_requires_cost_and_only_gx_or_ex_on_bench(self):
        rig, e = self.rig('SM12.GreatCatcher_192', 'trainer')
        definition = fixtures.definition('SM12.GreatCatcher_192')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        self.assertFalse(self.playable(rig, e['target'], definition))
        target = self.add(rig, fixtures.definition('SM1.EspeonGX_61'), P2, 'bench')
        self.assertTrue(self.playable(rig, e['target'], definition))
        for card in list(ctx.hand()):
            if card is not e['target']:rig.to_area(card, P1, 'deck')
        self.assertFalse(self.playable(rig, e['target'], definition))
        for _ in range(2):self.energy(rig)
        self.assertTrue(self.playable(rig, e['target'], definition))
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await definition.effect(ctx)
        self.assertIs(ctx.opponent_active(), target)
        self.assertEqual(ctx.choose_pokemon.call_args.args[0], [target])
        self.assertEqual(len(ctx.hand()), 1)

    async def test_slumbering_forest_requires_two_heads_for_either_player(self):
        from spirit.game.attributes import SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
        for owner in (P1,P2):
            for flips in ([0,0],[0,1],[1,0]):
                rig, e = self.rig('SM11.SlumberingForest_207','trainer')
                rig.board.move_card(e['target'].entity_id,rig.board.find_global_area('activeStadium').entity_id)
                target = rig.board.active_pokemon(owner)
                asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
                target.set_attribute(AttrID.SPECIAL_CONDITIONS,[asleep])
                with patch('spirit.game.session.game_session.random.choice', side_effect=flips) as coin:
                    await rig.session._checkup_sleep(owner,target)
                self.assertEqual(coin.call_count,2)
                self.assertEqual(asleep in (target.get_attribute(AttrID.SPECIAL_CONDITIONS) or []),any(flips))

    async def test_flaming_fighter_changes_opposing_burn_not_own_or_poison(self):
        from spirit.game.session.passives import active_passives
        rig, e = self.rig('SM5.Infernape_23')
        own, opposing = rig.board.active_pokemon(P1),rig.board.active_pokemon(P2)
        for target, expected in ((own,2),(opposing,6)):
            burn, poison = 2,1
            for passive,carrier in active_passives(rig.board):
                burn=passive.modify_burn_counters(burn,target,carrier)
                poison=passive.modify_poison_counters(poison,target,carrier)
            self.assertEqual(burn,expected)
            self.assertEqual(poison,1)

    async def test_damage_reactions_require_active_and_real_opposing_attack_damage(self):
        from spirit.game.data_utils import Attack
        from spirit.game.attributes import SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
        for path, status in (
            ('SM7.Cacnea_19',SpecialConditions.POISONED),
            ('SM6.Dragalge_53',SpecialConditions.POISONED),
            ('SM8.Shiinotic_148',SpecialConditions.ASLEEP),
            ('SM5.Magmortar_19',SpecialConditions.BURNED),
            ('Promo_SM.AlolanMarowakGX_187',SpecialConditions.CONFUSED),
        ):
            for bench, counters in ((False,False),(True,False),(False,True)):
                rig, e = self.rig(path)
                target=e['target']
                if bench:rig.to_area(target,P1,'bench')
                attacker=rig.board.active_pokemon(P2)
                ctx=EffectContext(rig.session,P2,attacker,Attack(title='Hit',cost={},damage=10))
                await ctx.deal_damage(10,target=target,as_counters=counters,apply_modifiers=not counters)
                for action in list(ctx.deferred_actions):await action()
                condition=CLIENT_SPECIAL_CONDITION_NAMES[status]
                self.assertEqual(condition in (attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []),not bench and not counters)

    async def test_fluffy_cotton_and_evasion_jutsu_prevent_damage_only_on_heads(self):
        from spirit.game.data_utils import Attack
        for path in ('SM10.WhimsicottGX_140','GUM.Greninja_9'):
            for heads in (False,True):
                rig,e=self.rig(path)
                target=e['target']
                ctx=EffectContext(rig.session,P2,rig.board.active_pokemon(P2),Attack(title='Hit',cost={},damage=20))
                before=target.get_attribute(AttrID.HP)
                ctx.flip_coins=AsyncMock(return_value=[heads])
                dealt=await ctx.deal_damage(20,target=target)
                self.assertEqual(dealt,0 if heads else 20)
                self.assertEqual(target.get_attribute(AttrID.HP),before-dealt)
                ctx.flip_coins.assert_awaited_once()
                await ctx.deal_damage(10,target=target,as_counters=True,apply_modifiers=False)
                self.assertEqual(target.get_attribute(AttrID.HP),before-dealt-10)
                ctx.flip_coins.assert_awaited_once()

    async def test_guts_and_sturdy_preserve_ten_hp_with_their_distinct_requirements(self):
        from spirit.game.data_utils import Attack
        for path, damaged, heads, survives in (
            ('SM3.Heracross_11',True,True,True),
            ('SM3.Heracross_11',False,False,False),
            ('SM8.Donphan_112',False,False,True),
            ('SM8.Donphan_112',True,False,False),
        ):
            rig,e=self.rig(path)
            target=e['target']
            if damaged:target.set_attribute(AttrID.HP,40)
            ctx=EffectContext(rig.session,P2,rig.board.active_pokemon(P2),Attack(title='Hit',cost={},damage=1000))
            ctx.flip_coins=AsyncMock(return_value=[heads])
            await ctx.deal_damage(1000,target=target)
            self.assertEqual(target.get_attribute(AttrID.HP),10 if survives else 0)

    async def test_evolution_from_deck_does_not_trigger_hand_only_ability(self):
        for zone in ('deck','discard','hand'):
            rig,e=self.rig('SM8.Dustox_28')
            dustox=e['target']
            rig.to_area(dustox,P1,zone)
            target=self.add(rig,fixtures.definition('SM8.Cascoon_27'),P1,'bench')
            with patch.object(EffectContext,'ask_yes_no',AsyncMock(return_value=True)) as ask:
                self.assertTrue(await rig.session.perform_evolution(P1,dustox,target,from_zone_intro=zone=='deck'))
            opponent=rig.board.active_pokemon(P2)
            self.assertEqual(rig.session.poison_counters.get(opponent.entity_id),3 if zone=='hand' else None)
            self.assertEqual(ask.await_count,int(zone=='hand'))
