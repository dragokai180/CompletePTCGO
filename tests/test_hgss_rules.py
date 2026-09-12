"""HGSS regressions assert rule outcomes, not just that a callback ran."""
import unittest
from importlib import import_module
from unittest.mock import AsyncMock

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.standard_era import normalize_standard_card_definition
from spirit.game.models.board import create_card_entity
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext, is_basic_energy
from spirit.game.session.legal_actions import _ability_entries, trainer_condition_met
from spirit.game.session.passives import effective_max_hp, compute_damage, effective_retreat_cost, effective_bench_capacity, energy_provided_options
from spirit.tools.effect_smoke import (
    P1, P2, Rig, basic_energy_guids, pick_filler_basic, pick_filler_item,
)


def definition(path):
    card = import_module('spirit.game.scripts.cards.' + path).card
    normalize_standard_card_definition(card)
    return card


class HgssRulesTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        loader.load_all()
        cls.filler = pick_filler_basic()
        cls.energies = basic_energy_guids()
        cls.item = pick_filler_item()

    def rig(self, path, kind='pokemon'):
        rig = Rig(definition(path), self.filler, self.energies, self.item)
        entities = rig.setup(kind)
        for pid in (P1, P2):
            for pokemon in rig.board.pokemon_in_play(pid):
                pokemon.set_attribute(AttrID.HP, effective_max_hp(rig.board, pokemon))
        return rig, entities

    def ctx(self, path, title):
        rig, e = self.rig(path)
        ability = next(a for a in definition(path).abilities if a.title == title)
        return rig, e, EffectContext(rig.session, P1, e['target'], ability)

    def add(self, rig, card_def, pid, zone):
        card = create_card_entity(loader.cards_by_guid[card_def.guid.lower()], pid)
        rig.board.add_card_to_area(card, rig.board.find_player_area(pid, zone))
        card.owning_player_id = pid
        return card

    async def test_poke_power_special_condition_restriction(self):
        rig, e, ctx = self.ctx('HGSS2.Kingdra_85', 'Spray Splash')
        for condition in ('Asleep', 'Burned', 'Confused', 'Paralyzed', 'Poisoned'):
            with self.subTest(condition=condition):
                e['target'].set_attribute(AttrID.SPECIAL_CONDITIONS, [condition])
                self.assertFalse(ctx.ability.condition(rig.board, P1, e['target']))
                self.assertFalse(_ability_entries(rig.board, rig.session.turn_state,
                    P1, rig.session.game_id, [e['target']]))
        e['target'].set_attribute(AttrID.SPECIAL_CONDITIONS, [])
        self.assertTrue(ctx.ability.condition(rig.board, P1, e['target']))

    async def test_named_active_restriction(self):
        rig, e, ctx = self.ctx('HGSS4.Celebi_92', 'Forest Breath')
        rig.to_area(e['target'], P1, 'bench')
        self.assertFalse(ctx.ability.condition(rig.board, P1, e['target']))

    async def test_afterburner_places_counter_on_recipient(self):
        rig, e, ctx = self.ctx('Promo_HGSS.Typhlosion_9', 'Afterburner')
        target = rig.board.pokemon_in_play(P1)[-1]
        energy = next(c for c in ctx.discard_pile()
            if c.archetype_id.lower() == self.energies[PokemonTypes.FIRE.value].lower())
        ctx.choose_cards = AsyncMock(return_value=[energy])
        ctx.choose_pokemon = AsyncMock(return_value=target)
        hp = target.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        self.assertIn(energy, rig.board.attached_energies(target))
        self.assertEqual(target.get_attribute(AttrID.HP), hp - 10)

    async def test_afterburner_unavailable_without_fire_in_discard(self):
        rig, e, ctx = self.ctx('Promo_HGSS.Typhlosion_9', 'Afterburner')
        for card in list(ctx.discard_pile()):
            rig.to_area(card, P1, 'deck')
        self.assertFalse(ctx.ability.condition(rig.board, P1, e['target']))

    async def test_rain_dance_only_offers_water_pokemon(self):
        rig, e, ctx = self.ctx('HGSS1.Feraligatr_108', 'Rain Dance')
        other = rig.board.pokemon_in_play(P1)[-1]
        other.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        ctx.choose_pokemon = AsyncMock(side_effect=lambda pool, *a, **kw: pool[0])
        await ctx.ability.effect(ctx)
        for call in ctx.choose_pokemon.call_args_list:
            self.assertNotIn(other, call.args[0])

    async def test_water_acceleration_attaches_only_to_floatzel(self):
        rig, e, ctx = self.ctx('HGSS2.Floatzel_16', 'Water Acceleration')
        before = len(rig.board.attached_energies(e['target']))
        ctx.choose_pokemon = AsyncMock(return_value=rig.board.pokemon_in_play(P1)[-1])
        await ctx.ability.effect(ctx)
        ctx.choose_pokemon.assert_not_awaited()
        self.assertEqual(len(rig.board.attached_energies(e['target'])), before + 1)

    async def test_dragon_steam_checks_opponents_whole_board(self):
        for fire_on_bench in (False, True):
            with self.subTest(fire_on_bench=fire_on_bench):
                rig, e, ctx = self.ctx('HGSS2.Kingdra_85', 'Dragon Steam')
                for pokemon in rig.board.pokemon_in_play(P2):
                    pokemon.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
                if fire_on_bench:
                    rig.board.pokemon_in_play(P2)[-1].set_attribute(
                        AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args_list[0].args[0],
                                 20 if fire_on_bench else 60)

    async def test_flower_shop_lady_recovers_three_of_each(self):
        path = 'HGSS3.FlowerShopLady_74'
        rig, e = self.rig(path, 'trainer')
        for _ in range(3):
            self.add(rig, self.filler, P1, 'discard')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        ctx.shuffle_into_deck = AsyncMock()
        await definition(path).effect(ctx)
        picked = ctx.shuffle_into_deck.call_args.args[0]
        self.assertEqual(len(picked), 6)
        self.assertEqual(sum(is_basic_energy(card) for card in picked), 3)

    async def test_second_sight_can_choose_opponents_deck(self):
        for path in ('HGSS1.Slowking_12', 'COL.Slowking_32'):
            with self.subTest(path=path):
                rig, e, ctx = self.ctx(path, 'Second Sight')
                ctx.choose = AsyncMock(return_value=1)
                ctx.reorder_deck_top = AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.choose.assert_awaited_once()
                ctx.reorder_deck_top.assert_awaited_once_with(3, player_id=P2)

    async def test_poison_moth_wind_targets_correct_side_on_tails(self):
        for heads in (True, False):
            with self.subTest(heads=heads):
                rig, e, ctx = self.ctx('HGSS4.Venomoth_11', 'Poison Moth Wind')
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.apply_special_condition = AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.apply_special_condition.assert_awaited_once_with(
                    e['p2_active'] if heads else e['target'], SpecialConditions.POISONED)

    async def test_sleeping_face_only_protects_while_asleep(self):
        rig, e = self.rig('HGSS1.Tyrogue_33')
        for asleep in (False, True):
            with self.subTest(asleep=asleep):
                e['target'].set_attribute(AttrID.SPECIAL_CONDITIONS,
                    [CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]] if asleep else [])
                damage = compute_damage(rig.board, e['p2_active'], e['target'], 40,
                                        ignore_weakness=True, ignore_resistance=True)
                self.assertEqual(damage.amount, 0 if asleep else 40)

    async def test_shell_barricade_only_protects_shuckle_on_bench(self):
        rig, e = self.rig('HGSS1.Shuckle_11')
        for benched in (False, True):
            with self.subTest(benched=benched):
                rig.to_area(e['target'], P1, 'bench' if benched else 'activePokemonArea')
                damage = compute_damage(rig.board, e['p2_active'], e['target'], 40,
                                        ignore_weakness=True, ignore_resistance=True)
                self.assertEqual(damage.amount, 0 if benched else 40)

    async def test_dodrio_retreat_aid_is_bench_only(self):
        rig, e = self.rig('HGSS3.Dodrio_11')
        # Remove the second copy that the common rig puts on the Bench.
        for pokemon in list(rig.board.pokemon_in_play(P1)):
            if pokemon is not e['target'] and pokemon.archetype_id == e['target'].archetype_id:
                rig.to_area(pokemon, P1, 'deck')
        e['target'].set_attribute(AttrID.RETREAT_COST, 3)
        self.assertEqual(effective_retreat_cost(rig.board, e['target']), 3)
        other = rig.board.pokemon_in_play(P1)[-1]
        rig.to_area(e['target'], P1, 'bench')
        rig.to_area(other, P1, 'activePokemonArea')
        other.set_attribute(AttrID.RETREAT_COST, 3)
        self.assertEqual(effective_retreat_cost(rig.board, other), 1)

    async def test_allergy_flower_does_not_block_supporters_or_stadiums(self):
        rig, e = self.rig('HGSS3.Vileplume_24')
        passive = definition('HGSS3.Vileplume_24').abilities[0].passive
        for path, expected in (('HGSS1.Switch_102', True),
                               ('HGSS1.Bill_89', False),
                               ('HGSS3.RuinsofAlph_76', False)):
            with self.subTest(path=path):
                card = self.add(rig, definition(path), P2, 'hand')
                self.assertEqual(passive.blocks_trainer_play(card, P2, e['target']), expected)

    async def test_flare_destroy_discards_from_both_pokemon(self):
        rig, e, ctx = self.ctx('Promo_HGSS.Typhlosion_9', 'Flare Destroy')
        before = [len(rig.board.attached_energies(p)) for p in (e['target'], e['p2_active'])]
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        after = [len(rig.board.attached_energies(p)) for p in (e['target'], e['p2_active'])]
        self.assertEqual(after, [n - 1 for n in before])


    async def test_blissful_nurse_discards_only_from_previously_damaged_pokemon(self):
        rig, e, ctx = self.ctx('HGSS1.Blissey_106', 'Blissful Nurse')
        damaged, healthy = ctx.my_pokemon_in_play()[:2]
        damaged.set_attribute(AttrID.HP, ctx.max_hp(damaged) - 30)
        damaged_energy = list(ctx.attached_energies(damaged))
        spare = next(c for c in ctx.discard_pile() if is_basic_energy(c))
        rig.attach(spare, healthy)
        ctx.ask_yes_no = AsyncMock(return_value=True)
        await ctx.ability.effect(ctx)
        self.assertEqual(damaged.get_attribute(AttrID.HP), ctx.max_hp(damaged))
        self.assertTrue(damaged_energy)
        self.assertTrue(all(c in ctx.discard_pile() for c in damaged_energy))
        self.assertIn(spare, ctx.attached_energies(healthy))

    async def test_stardust_song_uses_heads_and_attaches_only_to_jirachi(self):
        for heads in (0, 1, 3):
            with self.subTest(heads=heads):
                rig, e, ctx = self.ctx('HGSS2.Jirachi_1', 'Stardust Song')
                psychic = next(c for c in ctx.discard_pile()
                    if c.archetype_id.lower() == self.energies[PokemonTypes.PSYCHIC.value].lower())
                for _ in range(2):
                    clone = create_card_entity(loader.cards_by_guid[psychic.archetype_id.lower()], P1)
                    rig.board.add_card_to_area(clone, rig.board.find_player_area(P1, 'discard'))
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.flip_coins = AsyncMock(return_value=[True] * heads + [False] * (3 - heads))
                ctx.choose_cards = AsyncMock(side_effect=lambda pool, count, **kw: pool[:count])
                ctx.choose_pokemon = AsyncMock()
                before = len(ctx.attached_energies(e['target']))
                await ctx.ability.effect(ctx)
                self.assertEqual(len(ctx.attached_energies(e['target'])), before + heads)
                ctx.flip_coins.assert_awaited_once_with(3, 'Stardust Song')
                ctx.choose_pokemon.assert_not_awaited()

    async def test_energymite_knocks_out_source_before_energy_distribution(self):
        rig, e, ctx = self.ctx('HGSS4.Electrode_93', 'Energymite')
        viewed = ctx.deck_top(7)
        ctx.choose_cards = AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        self.assertEqual(e['target'].get_attribute(AttrID.HP), 0)
        self.assertIn(e['target'], ctx.knockouts)
        self.assertTrue(all(c in ctx.discard_pile() for c in viewed))
        self.assertEqual(ctx.choose_cards.call_args.kwargs['display_cards'], viewed)

    async def test_ocean_grow_attaches_all_energy_to_lugia_only(self):
        rig, e, ctx = self.ctx('HGSS1.LugiaLEGEND_113', 'Ocean Grow')
        self.assertIsNotNone(ctx.ability.trigger)
        viewed = ctx.discard_pile()[:3] + ctx.hand()[:2]
        energies = [c for c in viewed if is_basic_energy(c)]
        ctx.deck_top = lambda count: viewed
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.reveal_cards = AsyncMock()
        ctx.attach_energy = AsyncMock()
        ctx.discard_cards = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual([c.args for c in ctx.attach_energy.call_args_list],
                         [(energy, e['target']) for energy in energies])
        ctx.discard_cards.assert_awaited_once_with([c for c in viewed if c not in energies])

    async def test_hustle_step_heals_one_counter_from_each_own_pokemon(self):
        rig, e, ctx = self.ctx('HGSS3.Bellossom_1', 'Hustle Step')
        self.assertFalse(ctx.ability.condition(rig.board, P1, e['target']))
        for pokemon in ctx.my_pokemon_in_play():
            pokemon.set_attribute(AttrID.HP, ctx.max_hp(pokemon) - 20)
        self.assertTrue(ctx.ability.condition(rig.board, P1, e['target']))
        await ctx.ability.effect(ctx)
        self.assertTrue(all(p.get_attribute(AttrID.HP) == ctx.max_hp(p) - 10
                            for p in ctx.my_pokemon_in_play()))

    async def test_green_shield_protects_only_own_grass_pokemon(self):
        rig, e = self.rig('HGSS1.Metapod_46')
        rig.to_area(e['target'], P1, 'bench')
        target = next(p for p in rig.board.pokemon_in_play(P1)
                      if p.archetype_id != e['target'].archetype_id)
        rig.to_area(target, P1, 'activePokemonArea')
        for pokemon_type, expected in ((PokemonTypes.GRASS, 30), (PokemonTypes.WATER, 60)):
            with self.subTest(pokemon_type=pokemon_type):
                target.set_attribute(AttrID.POKEMON_TYPES, [pokemon_type.value])
                target.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.FIRE.value])
                target.set_attribute(AttrID.WEAKNESS_AMOUNT, 2)
                e['p2_active'].set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
                self.assertEqual(compute_damage(rig.board, e['p2_active'], target, 30,
                    ignore_resistance=True).amount, expected)


    async def test_collector_reminder_does_not_turn_search_into_supporter_search(self):
        path = 'HGSS1.PokmonCollector_97'
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        ctx.search_deck = AsyncMock(return_value=[])
        await definition(path).effect(ctx)
        predicate = ctx.search_deck.call_args.args[0]
        self.assertTrue(predicate(e['p1_active']))
        self.assertFalse(predicate(e['target']))
        self.assertEqual(ctx.search_deck.call_args.kwargs['count'], 3)

    async def test_good_rod_tails_only_offers_items(self):
        path = 'HGSS2.GoodRod_76'
        rig, e = self.rig(path, 'trainer')
        for card in list(rig.board.find_player_area(P1, 'discard').children):
            rig.to_area(card, P1, 'deck')
        item = self.add(rig, definition('HGSS1.Switch_102'), P1, 'discard')
        self.add(rig, definition('HGSS1.Bill_89'), P1, 'discard')
        self.add(rig, definition('HGSS3.RuinsofAlph_76'), P1, 'discard')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        ctx.flip_coins = AsyncMock(return_value=[False])
        ctx.choose_cards = AsyncMock(return_value=[item])
        ctx.put_on_top_of_deck = AsyncMock()
        await definition(path).effect(ctx)
        # A single eligible card may be selected without a prompt.
        for call in ctx.choose_cards.call_args_list:
            self.assertEqual(call.args[0], [item])
        ctx.put_on_top_of_deck.assert_awaited_once_with(item)

    async def test_junk_arm_needs_item_already_in_discard(self):
        path = 'HGSS4.JunkArm_87'
        rig, e = self.rig(path, 'trainer')
        for card in list(rig.board.find_player_area(P1, 'discard').children):
            rig.to_area(card, P1, 'deck')
        self.add(rig, definition(path), P1, 'discard')
        self.add(rig, definition('HGSS1.Bill_89'), P1, 'discard')
        check = lambda: trainer_condition_met(definition(path).condition, rig.board, P1, e['target'])
        self.assertFalse(check())
        self.add(rig, definition('HGSS1.Switch_102'), P1, 'discard')
        self.assertTrue(check())

    async def test_hgss_rare_candy_uses_current_evolution_restrictions(self):
        path = 'HGSS2.RareCandy_82'
        rig, e = self.rig(path, 'trainer')
        basic = self.add(rig, definition('HGSS1.Totodile_86'), P1, 'bench')
        self.add(rig, definition('HGSS1.Croconaw_38'), P1, 'hand')
        turn = rig.session.turn_state
        turn.turn_number = 3
        check = lambda: trainer_condition_met(definition(path).condition, rig.board, P1, e['target'])
        self.assertFalse(check())
        self.add(rig, definition('HGSS1.Feraligatr_108'), P1, 'hand')
        self.assertTrue(check())
        turn.mark_entered_play(basic.entity_id)
        self.assertFalse(check())
        turn.entered_play_turn.clear()
        turn.turn_number = 1
        self.assertFalse(check())

    async def test_hgss_pluspower_does_not_attach_and_adds_ten_per_copy(self):
        path = 'HGSS2.PlusPower_80'
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        ctx.attach_card = AsyncMock()
        for _ in range(2):
            await definition(path).effect(ctx)
        ctx.attach_card.assert_not_awaited()
        for attacker in rig.board.pokemon_in_play(P1):
            self.assertEqual(compute_damage(rig.board, attacker, e['p2_active'], 30,
                ignore_weakness=True, ignore_resistance=True).amount, 50)


    async def test_afterburner_does_not_damage_if_attachment_fails(self):
        rig, e, ctx = self.ctx('Promo_HGSS.Typhlosion_9', 'Afterburner')
        ctx.attach_energy = AsyncMock(return_value=False)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.attach_energy.assert_awaited_once()
        ctx.deal_damage.assert_not_awaited()

    async def test_red_armor_checks_attackers_special_energy(self):
        rig, e = self.rig('HGSS3.Scizor_84')
        damage = lambda: compute_damage(rig.board, e['p2_active'], e['target'], 40,
                                        ignore_weakness=True, ignore_resistance=True).amount
        self.assertEqual(damage(), 40)
        special = self.add(rig, definition('HGSS1.DoubleColorlessEnergy_103'), P2, 'hand')
        rig.attach(special, e['p2_active'])
        self.assertEqual(damage(), 0)
        rig.to_area(special, P2, 'discard')
        self.assertEqual(damage(), 40)

    async def test_defense_sign_protects_only_own_grass_bench(self):
        rig, e = self.rig('HGSS3.Vespiquen_23')
        target = next(p for p in rig.board.pokemon_in_play(P1)
                      if p.archetype_id != e['target'].archetype_id)
        for element, expected in ((PokemonTypes.GRASS, 0), (PokemonTypes.WATER, 40)):
            target.set_attribute(AttrID.POKEMON_TYPES, [element.value])
            self.assertEqual(compute_damage(rig.board, e['p2_active'], target, 40,
                ignore_weakness=True, ignore_resistance=True).amount, expected)
        self.assertEqual(compute_damage(rig.board, e['p2_active'], e['target'], 40,
            ignore_weakness=True, ignore_resistance=True).amount, 40)


    async def test_psychic_float_requires_psychic_energy_on_own_active(self):
        rig, e = self.rig('HGSS2.Metagross_4')
        target = e['target']
        for energy in list(rig.board.attached_energies(target)):
            rig.to_area(energy, P1, 'discard')
        self.assertEqual(effective_retreat_cost(rig.board, target), 4)
        energy = rig.pull_guid(P1, self.energies[PokemonTypes.PSYCHIC.value])
        rig.attach(energy, target)
        self.assertEqual(effective_retreat_cost(rig.board, target), 0)
        bench = next(p for p in rig.board.pokemon_in_play(P1) if p is not target)
        rig.attach(energy, bench)
        self.assertEqual(effective_retreat_cost(rig.board, target), 4)
        bench.set_attribute(AttrID.RETREAT_COST, 3)
        self.assertEqual(effective_retreat_cost(rig.board, bench), 3)

    async def test_retreat_surcharges_do_not_read_colorless_as_less(self):
        for path in ('HGSS4.Victreebel_12', 'Promo_HGSS.Wobbuffet_4'):
            with self.subTest(path=path):
                rig, e = self.rig(path)
                e['p2_active'].set_attribute(AttrID.RETREAT_COST, 3)
                self.assertEqual(effective_retreat_cost(rig.board, e['p2_active']), 5)
                rig.to_area(e['target'], P1, 'bench')
                self.assertEqual(effective_retreat_cost(rig.board, e['p2_active']), 3)

    async def test_ultra_thick_skin_needs_energy_and_reduces_own_attack_damage(self):
        rig, e = self.rig('COL.Phanpy_66')
        target = e['target']
        for energy in list(rig.board.attached_energies(target)):
            rig.to_area(energy, P1, 'discard')
        damage = lambda attacker: compute_damage(rig.board, attacker, target, 30,
            ignore_weakness=True, ignore_resistance=True).amount
        self.assertEqual(damage(e['p2_active']), 30)
        energy = rig.pull_guid(P1, self.energies[PokemonTypes.WATER.value])
        rig.attach(energy, target)
        self.assertEqual(damage(e['p2_active']), 20)
        self.assertEqual(damage(target), 20)

    async def test_exoskeleton_reduces_friendly_attack_damage_too(self):
        rig, e = self.rig('HGSS1.Donphan_107')
        self.assertEqual(compute_damage(rig.board, e['target'], e['target'], 30,
            ignore_weakness=True, ignore_resistance=True).amount, 10)

    async def test_energy_healer_only_heals_onix_receiving_energy_from_hand(self):
        rig, e = self.rig('HGSS2.Onix_56')
        target = e['target']
        target.set_attribute(AttrID.HP, 60)
        energy = rig.pull_guid(P1, self.energies[PokemonTypes.FIRE.value])
        other = next(p for p in rig.board.pokemon_in_play(P1) if p is not target)
        rig.attach(energy, other)
        await rig.session.fire_energy_attached_triggers(P1, energy, other)
        self.assertEqual(target.get_attribute(AttrID.HP), 60)
        ctx = EffectContext(rig.session, P1, target, None)
        await ctx.attach_energy(energy, target)  # Non-hand attachment: no observer event.
        self.assertEqual(target.get_attribute(AttrID.HP), 60)
        await rig.session.fire_energy_attached_triggers(P1, energy, target)
        self.assertEqual(target.get_attribute(AttrID.HP), 70)

    async def test_dittobolic_discards_chosen_stack_without_awarding_prizes(self):
        rig, e = self.rig('HGSS4.Ditto_17')
        self.assertEqual(effective_bench_capacity(rig.board, P1), 5)
        self.assertEqual(effective_bench_capacity(rig.board, P2), 4)
        for _ in range(3):
            victim = self.add(rig, self.filler, P2, 'bench')
        energy = rig.pull_guid(P2, self.energies[PokemonTypes.WATER.value])
        rig.attach(energy, victim)
        prizes = len(rig.board.find_player_area(P1, 'prizePile').children)
        rig.session.prompt_entity_picker = AsyncMock(return_value=[victim.entity_id])
        await rig.session.enforce_bench_capacity()
        self.assertEqual(len(rig.board.find_player_area(P2, 'bench').children), 4)
        self.assertIs(victim.parent, rig.board.find_player_area(P2, 'discard'))
        self.assertIs(energy.parent, victim.parent)
        self.assertEqual(len(rig.board.find_player_area(P1, 'prizePile').children), prizes)
        self.assertEqual(rig.session.prompt_entity_picker.call_args.args[0], P2)

    async def test_catastrophe_redirects_pokemon_stack_but_not_energy(self):
        for active in (False, True):
            with self.subTest(active=active):
                rig, e = self.rig('HGSS4.Gengar_94')
                if not active:
                    rig.to_area(e['target'], P1, 'bench')
                victim = self.add(rig, definition('HGSS1.Feraligatr_108'), P2, 'bench')
                basic = self.add(rig, definition('HGSS1.Totodile_86'), P2, 'hand')
                middle = self.add(rig, definition('HGSS1.Croconaw_38'), P2, 'hand')
                energy = rig.pull_guid(P2, self.energies[PokemonTypes.WATER.value])
                for card in (basic, middle, energy):
                    rig.attach(card, victim)
                ctx = EffectContext(rig.session, P1, e['target'], None)
                await ctx.knock_out(victim)  # No attack-damage restriction on Catastrophe.
                await rig.session.resolve_knockouts(ctx)
                destination = rig.board.find_player_area(P2, 'lostZone' if active else 'discard')
                self.assertTrue(all(c.parent is destination for c in (victim, basic, middle)))
                self.assertIs(energy.parent, rig.board.find_player_area(P2, 'discard'))

    async def test_energy_signal_applies_matching_conditions_and_can_be_declined(self):
        for kind in ('grass', 'psychic', 'rainbow', 'decline'):
            with self.subTest(kind=kind):
                rig, e, ctx = self.ctx('HGSS2.Roserade_23', 'Energy Signal')
                if kind == 'rainbow':
                    energy = self.add(rig, definition('HGSS1.RainbowEnergy_104'), P1, 'hand')
                else:
                    ptype = PokemonTypes.PSYCHIC if kind == 'psychic' else PokemonTypes.GRASS
                    energy = rig.pull_guid(P1, self.energies[ptype.value])
                rig.attach(energy, e['target'])
                ctx.energy_receiver = e['target']
                ctx.attached_energy = energy
                ctx.attaching_player_id = P1
                rig.session.turn_state.active_player_id = P1
                ctx.ask_yes_no = AsyncMock(return_value=kind != 'decline')
                ctx.apply_special_condition = AsyncMock()
                await ctx.ability.passive.on_energy_attached(ctx, e['target'])
                expected = [] if kind == 'decline' else ([SpecialConditions.CONFUSED] if kind == 'grass'
                    else [SpecialConditions.POISONED] if kind == 'psychic'
                    else [SpecialConditions.CONFUSED, SpecialConditions.POISONED])
                self.assertEqual([call.args[1] for call in ctx.apply_special_condition.call_args_list], expected)


    async def test_eye_of_disaster_only_watches_opponents_hand_while_active(self):
        for active, opponent, from_hand in ((True, True, True), (False, True, True),
                                            (True, False, True), (True, True, False)):
            with self.subTest(active=active, opponent=opponent, from_hand=from_hand):
                rig, e = self.rig('HGSS4.Absol_91')
                if not active:
                    rig.to_area(e['target'], P1, 'bench')
                pid = P2 if opponent else P1
                victim = self.add(rig, self.filler, pid, 'hand' if from_hand else 'deck')
                hp = victim.get_attribute(AttrID.HP)
                if from_hand:
                    rig.to_area(victim, pid, 'bench')
                    await rig.session.fire_pokemon_benched_triggers(pid, victim)
                else:
                    ctx = EffectContext(rig.session, pid, victim, None)
                    await ctx.bench_pokemon(victim)
                self.assertEqual(victim.get_attribute(AttrID.HP),
                                 hp - (20 if active and opponent and from_hand else 0))

    async def test_energy_signal_respects_status_turn_and_receiver(self):
        for invalid in ('status', 'turn', 'receiver', 'type'):
            with self.subTest(invalid=invalid):
                rig, e, ctx = self.ctx('HGSS2.Roserade_23', 'Energy Signal')
                ptype = PokemonTypes.FIRE if invalid == 'type' else PokemonTypes.GRASS
                energy = rig.pull_guid(P1, self.energies[ptype.value])
                receiver = next(p for p in ctx.my_pokemon_in_play() if p is not e['target']) \
                    if invalid == 'receiver' else e['target']
                rig.attach(energy, receiver)
                ctx.energy_receiver, ctx.attached_energy, ctx.attaching_player_id = receiver, energy, P1
                rig.session.turn_state.active_player_id = P2 if invalid == 'turn' else P1
                if invalid == 'status':
                    e['target'].set_attribute(AttrID.SPECIAL_CONDITIONS,
                        [CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]])
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.apply_special_condition = AsyncMock()
                await ctx.ability.passive.on_energy_attached(ctx, e['target'])
                ctx.ask_yes_no.assert_not_awaited()
                ctx.apply_special_condition.assert_not_awaited()

    async def test_heal_block_blocks_healing_but_not_counter_movement(self):
        rig, e = self.rig('HGSS4.Solrock_9')
        target = e['target']
        target.set_attribute(AttrID.HP, effective_max_hp(rig.board, target) - 30)
        ctx = EffectContext(rig.session, P1, target, None)
        self.assertEqual(await ctx.heal(10, target), 10)
        lunatone = self.add(rig, definition('HGSS4.Lunatone_25'), P1, 'bench')
        self.assertEqual(await ctx.heal(10, target), 0)
        other = next(p for p in ctx.my_pokemon_in_play() if p is not target)
        rig.session.turn_state.healed_entities.clear()
        self.assertEqual(await ctx.move_damage_counters(target, other, 1), 1)
        self.assertNotIn(target.entity_id, rig.session.turn_state.healed_entities)
        rig.to_area(lunatone, P1, 'discard')
        self.assertEqual(await ctx.heal(10, target), 10)

    async def test_sacred_rainbow_keeps_double_energy_value_and_holder_scope(self):
        rig, e = self.rig('HGSS1.HoOhLEGEND_111')
        energy = self.add(rig, definition('HGSS1.DoubleColorlessEnergy_103'), P1, 'hand')
        rig.attach(energy, e['target'])
        self.assertEqual(energy_provided_options(rig.board, energy),
                         [[PokemonTypes.FIRE.value, PokemonTypes.FIRE.value]])
        other = next(p for p in rig.board.pokemon_in_play(P1)
                     if p.archetype_id != e['target'].archetype_id)
        rig.attach(energy, other)
        self.assertEqual(energy_provided_options(rig.board, energy),
                         [[PokemonTypes.COLORLESS.value, PokemonTypes.COLORLESS.value]])

    async def test_pheromone_stamina_counts_only_allied_nidoqueen(self):
        rig, e = self.rig('HGSS4.Nidoking_6')
        base = effective_max_hp(rig.board, e['target'])
        self.add(rig, definition('HGSS4.Nidoqueen_28'), P2, 'bench')
        self.assertEqual(effective_max_hp(rig.board, e['target']), base)
        queen = self.add(rig, definition('HGSS4.Nidoqueen_28'), P1, 'bench')
        self.assertEqual(effective_max_hp(rig.board, e['target']), base + 20)
        rig.to_area(queen, P1, 'discard')
        self.assertEqual(effective_max_hp(rig.board, e['target']), base)


    async def test_earthquake_respects_exoskeleton_on_own_bench(self):
        rig, e, ctx = self.ctx('HGSS1.Donphan_107', 'Earthquake')
        protected = next(p for p in ctx.my_bench()
                         if p.archetype_id == e['target'].archetype_id)
        unprotected = next(p for p in ctx.my_bench()
                           if p.archetype_id != e['target'].archetype_id)
        hp_protected = protected.get_attribute(AttrID.HP)
        hp_unprotected = unprotected.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        self.assertEqual(protected.get_attribute(AttrID.HP), hp_protected)
        self.assertEqual(unprotected.get_attribute(AttrID.HP), hp_unprotected - 10)


    async def test_blizzard_damages_only_the_bench_selected_by_the_coin(self):
        for heads in (False, True):
            with self.subTest(heads=heads):
                rig, e, ctx = self.ctx('HGSS4.Piloswine_48', 'Blizzard')
                ctx.flip_coins = AsyncMock(return_value=[heads])
                own, opposing = list(ctx.my_bench()), list(ctx.opponent_bench())
                before = {p.entity_id: p.get_attribute(AttrID.HP) for p in own + opposing}
                active_hp = e['p2_active'].get_attribute(AttrID.HP)
                e['p2_active'].set_attribute(AttrID.WEAKNESS_TYPES, [])
                e['p2_active'].set_attribute(AttrID.RESISTANCE_TYPES, None)
                await ctx.ability.effect(ctx)
                self.assertEqual(e['p2_active'].get_attribute(AttrID.HP), active_hp - 40)
                for pokemon in own + opposing:
                    damaged = pokemon in opposing if heads else pokemon in own
                    self.assertEqual(pokemon.get_attribute(AttrID.HP),
                                     before[pokemon.entity_id] - (10 if damaged else 0))

    async def test_mini_earthquake_hits_own_bench_only(self):
        rig, e, ctx = self.ctx('HGSS4.Diglett_61', 'Mini Earthquake')
        own, opposing = list(ctx.my_bench()), list(ctx.opponent_bench())
        before = {p.entity_id: p.get_attribute(AttrID.HP) for p in own + opposing}
        await ctx.ability.effect(ctx)
        for pokemon in own + opposing:
            self.assertEqual(pokemon.get_attribute(AttrID.HP),
                             before[pokemon.entity_id] - (10 if pokemon in own else 0))


if __name__ == '__main__':
    unittest.main()
