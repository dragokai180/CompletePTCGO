"""Outcome-based regressions for 30C, including negative and copied cases."""
import json
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Attack, def_for
from spirit.game.card_effects.thirtieth_celebration import (
    CUSTOM_ATTACKS, COMMON_ATTACKS, PASSIVES, ACTIVATED, attack_effect, basic_of, area,
)
from spirit.game.session.effects import EffectContext, is_basic_energy, is_pokemon_card, _fire_damaged_by_attack_triggers
from spirit.game.session.passives import (
    effective_max_hp, effective_retreat_cost, compute_damage, active_passives,
    attacks_blocked, attack_effects_blocked, retreat_blocked,
)
from spirit.game.scripts.cards import loader
from spirit.tools.effect_smoke import P1, P2
from spirit.tools.import_thirtieth_celebration import normalized_card
from spirit.tools.install_recent_card_art import RecentSet, load_image_urls
import test_hgss_rules as fixtures


class CelebrationTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def energy(self, rig, kind, zone='hand'):
        return self.add(rig, def_for(self.energies[kind.value]), P1, zone)

    async def test_catalog_identity_and_printed_metadata(self):
        definitions = [def_for(c.guid) for c in loader.cards if c.key == 'ME55']
        self.assertEqual(len(definitions), 161)
        self.assertEqual(len({c.guid for c in definitions}), 161)
        self.assertFalse(any(c.key == 'ME55C' for c in loader.cards))
        attacks = {a.title for c in definitions for a in c.abilities if isinstance(a, Attack)}
        abilities = {a.title for c in definitions for a in c.abilities if not isinstance(a, Attack)}
        self.assertFalse((CUSTOM_ATTACKS | COMMON_ATTACKS) - attacks)
        self.assertFalse((PASSIVES | ACTIVATED) - abilities)
        for c in definitions:
            for a in c.abilities:
                if isinstance(a, Attack) and a.game_text:
                    self.assertIs(a.effect, attack_effect)
        self.assertEqual({c.collector_number for c in definitions}, set(range(1, 162)))
        self.assertEqual(fixtures.definition('ME55.Murkrow_93').extra_attributes[str(AttrID.RESISTANCE_AMOUNT.value)]['value'], 30)
        for n, text in ((159, 'R'), (160, 'G'), (161, 'B')):
            self.assertEqual(fixtures.definition(f'ME55.Mew_{n}').extra_attributes['200790']['value'], text)

    async def test_all_art_urls_are_main_set_and_rgb_are_mapped(self):
        numbers = [str(n) for n in range(1, 159)] + ['R', 'G', 'B']
        catalog = [dict(id=f'me55-{n}', number=n, images={'large': f'https://images.scrydex.com/pokemon/me55-{n}/large'}) for n in numbers]
        with patch('spirit.tools.install_recent_card_art.load_catalog', return_value=catalog):
            urls = load_image_urls(RecentSet('mega', 'me55', 'ME55'))
        self.assertEqual(len(urls), 161)
        for number, url in urls.items():
            self.assertIn('/me55-', url)
            self.assertNotIn('me55c', url)
        self.assertTrue(urls['159'].endswith('/me55-R/large'))

    async def test_scale_up_requires_six_energy_and_turns_off(self):
        rig, e = self.rig('ME55.AlolanExeggutor_2')
        p = e['target']
        for c in list(rig.board.attached_energies(p)):
            rig.to_area(c, P1, 'discard')
        for _ in range(5):
            rig.attach(self.energy(rig, PokemonTypes.GRASS), p)
        self.assertEqual(effective_max_hp(rig.board, p), 150)
        sixth = self.energy(rig, PokemonTypes.GRASS)
        rig.attach(sixth, p)
        self.assertEqual(effective_max_hp(rig.board, p), 400)
        rig.to_area(sixth, P1, 'discard')
        self.assertEqual(effective_max_hp(rig.board, p), 150)

    async def test_pheromones_both_sides_and_volbeat_gate(self):
        rig, e = self.rig('ME55.Illumise_4')
        a, b = e['target'], e['p2_active']
        for p in (a, b):
            p.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.GRASS.value])
            p.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
            p.set_attribute(AttrID.RESISTANCE_TYPES, 0)
        self.assertEqual(compute_damage(rig.board, a, b, 10).amount, 20)
        volbeat = self.add(rig, fixtures.definition('ME55.Volbeat_3'), P1, 'bench')
        self.assertEqual(compute_damage(rig.board, a, b, 10).amount, 30)
        self.assertEqual(compute_damage(rig.board, b, a, 10).amount, 30)
        rig.to_area(volbeat, P1, 'discard')
        self.assertEqual(compute_damage(rig.board, a, b, 10).amount, 20)

    async def test_birds_require_both_allies_and_typed_basic_energy(self):
        for path, title, kind in (
            ('Moltres_11', 'Fiery Flapping', PokemonTypes.FIRE),
            ('Articuno_18', 'Frosty Flapping', PokemonTypes.WATER),
            ('Zapdos_55', 'Flash-Pop Flapping', PokemonTypes.LIGHTNING),
        ):
            rig, e, ctx = self.ctx('ME55.' + path, title)
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
            for bird in ('Moltres_11', 'Articuno_18', 'Zapdos_55'):
                if bird != path:
                    self.add(rig, fixtures.definition('ME55.' + bird), P1, 'bench')
            for c in list(ctx.hand()):
                rig.to_area(c, P1, 'discard')
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
            energy = self.energy(rig, kind)
            self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
            await ctx.ability.effect(ctx)
            self.assertIn(energy, ctx.attached_energies(ctx.source))

    async def test_sunrise_only_benched_and_attaches_two_metal(self):
        rig, e, ctx = self.ctx('ME55.Solgaleo_105', 'Sunrise')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        rig.to_area(ctx.source, P1, 'bench')
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        energies = [self.energy(rig, PokemonTypes.METAL, 'deck') for _ in range(2)]
        ctx.search_deck = AsyncMock(return_value=energies)
        await ctx.ability.effect(ctx)
        self.assertTrue(all(c in ctx.attached_energies(ctx.source) for c in energies))
        predicate = ctx.search_deck.call_args.args[0]
        self.assertFalse(predicate(self.energy(rig, PokemonTypes.FIRE)))

    async def test_memory_helix_only_own_bench(self):
        rig, e = self.rig('ME55.Mewex_66')
        p = self.add(rig, fixtures.definition('ME55.Pikachuex_53'), P1, 'bench')
        self.add(rig, fixtures.definition('ME55.Gengarex_90'), P2, 'bench')
        granted = [a.title for passive, carrier in active_passives(rig.board)
                   for a in passive.granted_attacks(rig.board, e['target'], carrier)]
        self.assertIn('Pika-Pika Parade', granted)
        self.assertNotIn('Chaotic Pain', granted)
        rig.to_area(p, P1, 'hand')
        granted = [a.title for passive, carrier in active_passives(rig.board)
                   for a in passive.granted_attacks(rig.board, e['target'], carrier)]
        self.assertNotIn('Pika-Pika Parade', granted)

    async def test_counterattack_grouping_observes_bench_and_lethal_hit(self):
        rig, e, _ = self.ctx('ME55.Wishiwashi_22', 'Counterattack Grouping')
        active = e['target']
        attacker = e['p2_active']
        attacker.set_attribute(AttrID.HP, 500)
        ctx = EffectContext(rig.session, P2, attacker, Attack(title='Test', damage=50))
        await ctx.deal_damage(50, active)
        self.assertIn(active, ctx.knockouts)
        await _fire_damaged_by_attack_triggers(rig.session, ctx)
        self.assertEqual(attacker.get_attribute(AttrID.HP), 440)  # active + benched copy

    async def test_chaotic_pain_one_target_and_no_weakness(self):
        rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
        p = ctx.opponent_bench()[0]
        p.set_attribute(AttrID.HP, 300)
        ctx.choose_pokemon = AsyncMock(return_value=p)
        await ctx.ability.effect(ctx)
        self.assertEqual(p.get_attribute(AttrID.HP), 170)
        ctx.choose_pokemon.assert_awaited_once()

    async def test_stealthy_slash_uses_chosen_targets_damage(self):
        rig, e, ctx = self.ctx('ME55.Greninjaex_21', 'Stealthy Slash')
        p = ctx.opponent_bench()[0]
        p.set_attribute(AttrID.HP, ctx.max_hp(p) - 20)
        ctx.choose_pokemon = AsyncMock(return_value=p)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(60, p)

    async def test_colorful_harmony_counts_types_not_cards(self):
        rig, e, ctx = self.ctx('ME55.Sylveonex_71', 'Colorful Harmony')
        for p in ctx.my_pokemon_in_play():
            for c in list(ctx.attached_energies(p)):
                rig.to_area(c, P1, 'discard')
        for kind in (PokemonTypes.FIRE, PokemonTypes.FIRE, PokemonTypes.WATER):
            rig.attach(self.energy(rig, kind), ctx.attacker)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(100)

    async def test_empower_both_energy_to_one_pokemon(self):
        rig, e, ctx = self.ctx('ME55.Mewtwo_63', 'Empower')
        energies = [self.energy(rig, PokemonTypes.FIRE, 'discard') for _ in range(2)]
        ctx.choose_cards = AsyncMock(return_value=energies)
        target = ctx.my_bench()[0]
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ctx.ability.effect(ctx)
        ctx.choose_pokemon.assert_awaited_once()
        self.assertTrue(all(c in ctx.attached_energies(target) for c in energies))

    async def test_energy_gift_distributes_and_allows_failed_search(self):
        rig, e, ctx = self.ctx('ME55.Cherrim_7', 'Energy Gift')
        energies = [self.energy(rig, PokemonTypes.WATER, 'deck') for _ in range(2)]
        targets = ctx.my_bench()[:2]
        ctx.search_deck = AsyncMock(return_value=energies)
        ctx.choose_pokemon = AsyncMock(side_effect=targets)
        await ctx.ability.effect(ctx)
        for c, target in zip(energies, targets):
            self.assertIn(c, ctx.attached_energies(target))
        ctx.search_deck = AsyncMock(return_value=[])
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.shuffle_deck.assert_awaited_once()

    async def test_booming_call_allows_evolutions_and_caps_bench(self):
        rig, e, ctx = self.ctx('ME55.Salamenceex_109', 'Booming Call')
        dragon = self.add(rig, fixtures.definition('ME55.Kommoo_112'), P1, 'discard')
        wrong = self.add(rig, fixtures.definition('ME55.Gengarex_90'), P1, 'discard')
        ctx.choose_cards = AsyncMock(return_value=[dragon])
        await ctx.ability.effect(ctx)
        self.assertIn(dragon, ctx.my_bench())
        self.assertNotIn(wrong, ctx.choose_cards.call_args.args[0])
        self.assertEqual(ctx.choose_cards.call_args.args[1], 2)

    async def test_pika_parade_uses_available_spaces(self):
        rig, e, ctx = self.ctx('ME55.Pikachuex_53', 'Pika-Pika Parade')
        ctx.search_deck = AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.search_deck.call_args.kwargs['count'], 2)

    async def test_private_unrevealed_search_cannot_fail(self):
        rig, e, ctx = self.ctx('ME55.Gimmighoul_81', 'Strolls So Much')
        ctx.flip_coins = AsyncMock(return_value=[True])
        ctx.search_deck = AsyncMock(return_value=[])
        ctx.put_in_hand = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 1)
        self.assertIsNone(ctx.search_deck.call_args.args[0])
        self.assertFalse(ctx.put_in_hand.call_args.kwargs['reveal'])

    async def test_select_a_snack_only_returns_one_of_three(self):
        rig, e, ctx = self.ctx('ME55.Morpeko_61', 'Select a Snack')
        top = list(ctx.deck_top(3))
        ctx.choose_cards = AsyncMock(return_value=[top[1]])
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_cards.call_args.args[0], top)
        self.assertIn(top[1], ctx.hand())
        self.assertTrue(all(c in ctx.discard_pile() for c in (top[0], top[2])))

    async def test_photon_bullets_modern_ex_only(self):
        rig, e, ctx = self.ctx('ME55.Mewtwoex_64', 'Photon Bullets')
        modern = self.add(rig, fixtures.definition('ME55.Gengarex_90'), P2, 'bench')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(50, modern)

    async def test_wormhole_other_player_chooses_only_after_own_switch(self):
        rig, e, ctx = self.ctx('ME55.Palkia_20', 'Wormhole')
        first, second = ctx.my_bench()[0], ctx.opponent_bench()[0]
        ctx.choose_pokemon = AsyncMock(side_effect=[first, second])
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertIs(ctx.my_active(), first)
        self.assertIs(ctx.opponent_active(), second)
        self.assertEqual(ctx.choose_pokemon.call_args_list[1].kwargs['player_id'], P2)

    async def test_swirl_never_heals_low_hp(self):
        for hp, expected in ((130, 50), (50, 50), (30, 30)):
            rig, e, ctx = self.ctx('ME55.HisuianZoroark_123', 'Swirling Resentment')
            ctx.defender.set_attribute(AttrID.HP, hp)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.defender.get_attribute(AttrID.HP), expected)

    async def test_celebration_exact_hand_size(self):
        rig, e, ctx = self.ctx('ME55.Gholdengo_108', 'Celebration')
        ctx.take_prizes = AsyncMock(return_value=[object(), object()])
        ctx.shuffle_into_deck = AsyncMock()
        ctx.hand_size = lambda: 29
        await ctx.ability.effect(ctx)
        ctx.take_prizes.assert_not_awaited()
        ctx.hand_size = lambda: 30
        await ctx.ability.effect(ctx)
        ctx.take_prizes.assert_awaited_once_with(2)
        ctx.shuffle_into_deck.assert_awaited_once()

    async def test_good_sleep_only_if_still_asleep(self):
        rig, e, ctx = self.ctx('ME55.Snorlax_119', 'Good Sleep')
        p = ctx.source
        p.set_attribute(AttrID.HP, 50)
        await ctx.ability.effect(ctx)
        self.assertEqual(p.get_attribute(AttrID.HP), 50)
        p.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Asleep'])
        await ctx.ability.effect(ctx)
        self.assertEqual(p.get_attribute(AttrID.HP), 160)

    async def test_fainting_spell_not_for_checkup_ko(self):
        rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Fainting Spell')
        ctx.ko_attacker = e['p2_active']
        ctx.flip_coins = AsyncMock(return_value=[True])
        ctx.knock_out = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.flip_coins.assert_not_awaited()
        ctx.ko_from_attack = True
        await ctx.ability.effect(ctx)
        ctx.knock_out.assert_awaited_once_with(ctx.ko_attacker)

    async def test_guiding_dance_tails_does_not_search_or_shuffle(self):
        rig, e, ctx = self.ctx('ME55.Vivillon_8', 'Guiding Dance')
        ctx.flip_coins = AsyncMock(return_value=[False])
        ctx.search_deck = AsyncMock(return_value=[])
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.search_deck.assert_not_awaited()
        ctx.shuffle_deck.assert_not_awaited()
        ctx.flip_coins.return_value = [True]
        await ctx.ability.effect(ctx)
        ctx.search_deck.assert_awaited_once()
        ctx.shuffle_deck.assert_awaited_once()

    async def test_nighttime_byway_only_reduces_own_active_from_bench(self):
        rig, e = self.rig('ME55.Zoroark_96')
        active = e['target']
        active.set_attribute(AttrID.RETREAT_COST, 4)
        self.assertEqual(effective_retreat_cost(rig.board, active), 2)  # one benched copy
        for p in list(rig.board.pokemon_in_play(P1)):
            if p is not active:
                rig.to_area(p, P1, 'discard')
        self.assertEqual(effective_retreat_cost(rig.board, active), 4)
        other = e['p2_active']
        other.set_attribute(AttrID.RETREAT_COST, 4)
        self.add(rig, fixtures.definition('ME55.Zoroark_96'), P1, 'bench')
        self.assertEqual(effective_retreat_cost(rig.board, active), 2)
        self.assertEqual(effective_retreat_cost(rig.board, other), 4)

    async def test_share_happiness_requires_damage(self):
        rig, e, ctx = self.ctx('ME55.Nidorina_88', 'Share Happiness')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        target = ctx.my_bench()[0]
        target.set_attribute(AttrID.HP, ctx.max_hp(target) - 40)
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ctx.ability.effect(ctx)
        self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target) - 10)

    async def test_life_locked_blocks_opponents_active_only(self):
        rig, e, ctx = self.ctx('ME55.Yveltal_100', 'Life-Locked')
        for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
            p.set_attribute(AttrID.HP, ctx.max_hp(p) - 20)
        opponent = ctx.opponent_active()
        hp = opponent.get_attribute(AttrID.HP)
        await ctx.heal(20, opponent)
        self.assertEqual(opponent.get_attribute(AttrID.HP), hp)
        bench = ctx.opponent_bench()[0]
        await ctx.heal(20, bench)
        self.assertEqual(bench.get_attribute(AttrID.HP), ctx.max_hp(bench))

    async def test_keep_hidden_only_on_bench(self):
        rig, e = self.rig('ME55.Pikachu_33')
        bench = rig.board.pokemon_in_play(P1)[1]
        attacker = e['p2_active']
        self.assertTrue(compute_damage(rig.board, attacker, bench, 50).prevented)
        self.assertTrue(attack_effects_blocked(rig.board, bench))
        self.assertFalse(compute_damage(rig.board, attacker, e['target'], 50).prevented)

    async def test_lonely_gaze_reduces_before_weakness(self):
        rig, e = self.rig('ME55.Pikachu_28')
        target, attacker = e['target'], e['p2_active']
        target.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.WATER.value])
        attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        self.assertEqual(compute_damage(rig.board, attacker, target, 50).amount, 60)

    async def test_hail_applies_weakness_to_active_not_bench(self):
        rig, e, ctx = self.ctx('ME55.Articuno_18', 'Hail')
        for p in ctx.opponent_pokemon_in_play():
            p.set_attribute(AttrID.HP, 300)
            p.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.WATER.value])
            p.set_attribute(AttrID.RESISTANCE_TYPES, 0)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.opponent_active().get_attribute(AttrID.HP), 240)
        self.assertTrue(all(p.get_attribute(AttrID.HP) == 270 for p in ctx.opponent_bench()))

    async def test_snipe_discard_and_target(self):
        for path, title, amount in (
            ('Pikachu_51', 'Lightning Crash', 90),
            ('Minior_124', 'Shoot Meteors', 120),
            ('Pikachu_38', 'Targeted Spark', 20),
        ):
            rig, e, ctx = self.ctx('ME55.' + path, title)
            p = ctx.opponent_bench()[0]
            ctx.choose_pokemon = AsyncMock(return_value=p)
            ctx.deal_damage = AsyncMock()
            await ctx.ability.effect(ctx)
            ctx.deal_damage.assert_awaited_once_with(amount, p)
            if title != 'Targeted Spark':
                self.assertFalse(ctx.attached_energies(ctx.attacker))

    async def test_damage_formulas(self):
        for path, title, amount in (
            ('Kyogre_19', 'Hydro Pump', 240),  # 4 C paid with Water plus two spare Water
            ('Mew_65', 'Psychic', 90),
            ('Espeonex_70', 'Solar Beatdown', 120),
            ('Pikachu_34', 'Pika Chain', 80),
        ):
            rig, e, ctx = self.ctx('ME55.' + path, title)
            ctx.deal_damage = AsyncMock()
            await ctx.ability.effect(ctx)
            ctx.deal_damage.assert_awaited_once_with(amount)

    async def test_simple_conditions_and_coin_branches(self):
        cases = (
            ('Exeggcute_1', 'Hypnosis', 'Asleep', False),
            ('Vivillon_8', 'Poison Powder', 'Poisoned', False),
            ('Fuecocoex_15', 'Singe', 'Burned', False),
            ('Pikachu_23', 'Thunder Shock', 'Paralyzed', True),
            ('Lapras_17', 'Ice Beam', 'Paralyzed', True),
            ('Azumarill_68', 'Body Slam', 'Paralyzed', True),
        )
        for path, title, condition, coin in cases:
            for heads in (False, True):
                rig, e, ctx = self.ctx('ME55.' + path, title)
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.deal_damage = AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual(condition in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), heads or not coin)

    async def test_coin_damage_and_protection_branches(self):
        for path, title, base, bonus in (
            ('Vulpix_9', 'Wild Kick', 0, 30),
            ('Wishiwashi_22', 'Surprise Attack', 0, 30),
            ('Pikachu_47', 'Play Rough', 10, 20),
            ('Eevee_117', 'Quick Attack', 20, 20),
        ):
            for heads in (False, True):
                rig, e, ctx = self.ctx('ME55.' + path, title)
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.deal_damage = AsyncMock()
                await ctx.ability.effect(ctx)
                damage = sum(call.args[0] for call in ctx.deal_damage.call_args_list)
                self.assertEqual(damage, base + (bonus if heads else 0))
        for path, title in (('Cherubi_6', 'Hide'), ('Slowpoke_16', 'Well-Hidden'), ('Pikachu_44', 'Agility')):
            for heads in (False, True):
                rig, e, ctx = self.ctx('ME55.' + path, title)
                ctx.flip_coins = AsyncMock(return_value=[heads])
                await ctx.ability.effect(ctx)
                self.assertEqual(attack_effects_blocked(rig.board, ctx.source), heads)

    async def test_attack_locks_and_retreat_coin(self):
        for path, title in (('Toxtricity_60', 'Thunderous Bolt'), ('Mewtwoex_64', 'Psychic Powers')):
            rig, e, ctx = self.ctx('ME55.' + path, title)
            ctx.deal_damage = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertTrue(attacks_blocked(rig.board, ctx.attacker))
            rig.session.turn_state.begin_turn(P2, rig.board)
            rig.session.turn_state.begin_turn(P1, rig.board)
            self.assertTrue(attacks_blocked(rig.board, ctx.attacker))
            rig.session.turn_state.begin_turn(P2, rig.board)
            self.assertFalse(attacks_blocked(rig.board, ctx.attacker))
        for heads in (False, True):
            rig, e, ctx = self.ctx('ME55.Murkrow_93', 'Clumsily Clutch')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.deal_damage = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(rig.session.turn_state.retreat_locked(ctx.defender.entity_id), heads)

    async def test_quaking_fist_trainer_lock_expires(self):
        rig, e, ctx = self.ctx('ME55.Seismitoad_84', 'Quaking Fist')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertIn(P2, rig.session.turn_state.trainer_flip_checks)
        rig.session.turn_state.begin_turn(P2)
        self.assertIn(P2, rig.session.turn_state.trainer_flip_checks)
        rig.session.turn_state.begin_turn(P1)
        self.assertNotIn(P2, rig.session.turn_state.trainer_flip_checks)

    async def test_teleportation_and_float_up_can_be_declined(self):
        rig, e, ctx = self.ctx('ME55.Mewex_66', 'Teleportation Burst')
        ctx.choose_pokemon = AsyncMock(return_value=None)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertTrue(ctx.choose_pokemon.call_args.kwargs['optional'])
        self.assertIs(ctx.my_active(), e['target'])
        rig, e, ctx = self.ctx('ME55.Drifloon_73', 'Float Up')
        ctx.ask_yes_no = AsyncMock(return_value=False)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertIs(ctx.my_active(), e['target'])

    async def test_nitpick_changes_only_opponents_hand(self):
        rig, e, ctx = self.ctx('ME55.Scraggy_94', 'Nitpick')
        own_hand = list(ctx.hand())
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.hand_size(P2), 4)
        self.assertEqual(ctx.hand(), own_hand)

    async def test_zip_zap_repeats_then_done_without_new_energy(self):
        rig, e, ctx = self.ctx('ME55.Pikachuex_54', 'Zip-Zap Frenzy')
        for c in list(ctx.hand()):
            rig.to_area(c, P1, 'discard')
        energies = [self.energy(rig, PokemonTypes.FIRE), self.energy(rig, PokemonTypes.WATER)]
        p, q = ctx.my_bench()[:2]
        ctx.choose_cards = AsyncMock(side_effect=[[energies[0]], [energies[1]]])
        ctx.choose_pokemon = AsyncMock(side_effect=[p, q])
        await ctx.ability.effect(ctx)
        self.assertIn(energies[0], ctx.attached_energies(p))
        self.assertIn(energies[1], ctx.attached_energies(q))
        self.assertEqual(ctx.choose_cards.await_count, 2)

    async def test_gnaw_together_counts_only_own_maushold(self):
        rig, e, ctx = self.ctx('ME55.Maushold_125', 'Gnaw Together')
        ctx.flip_coins = AsyncMock(return_value=[True, False])
        top = list(ctx.deck_top(2, P2))
        await ctx.ability.effect(ctx)
        ctx.flip_coins.assert_awaited_once_with(2)
        self.assertTrue(all(c in ctx.discard_pile(P2) for c in top))

    async def test_transform_transfers_attachments_damage_and_age(self):
        rig, e, ctx = self.ctx('ME55.Ditto_115', 'Surprisingly Transform')
        incoming = self.add(rig, fixtures.definition('ME55.Solgaleo_105'), P1, 'deck')
        old = ctx.attacker
        old.set_attribute(AttrID.HP, ctx.max_hp(old) - 20)
        old.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned'])
        energies = list(ctx.attached_energies(old))
        ctx.flip_coins = AsyncMock(return_value=[True])
        ctx.search_deck = AsyncMock(return_value=[incoming])
        await ctx.ability.effect(ctx)
        self.assertIs(ctx.my_active(), incoming)
        self.assertEqual(incoming.get_attribute(AttrID.HP), ctx.max_hp(incoming) - 20)
        self.assertIn('Poisoned', incoming.get_attribute(AttrID.SPECIAL_CONDITIONS))
        self.assertTrue(all(c in ctx.attached_energies(incoming) for c in energies))
        self.assertIn(old, ctx.deck())

    async def test_import_corrections_leave_raw_input_unchanged(self):
        raw = dict(id='me55-93', number='93', name='Murkrow', resistances=[dict(type='Fighting', value='×2')])
        fixed = normalized_card(raw)
        self.assertEqual(fixed['resistances'][0]['value'], '-30')
        self.assertEqual(raw['resistances'][0]['value'], '×2')

    async def test_counterattack_remembers_active_before_attack_switch(self):
        rig, e, _ = self.ctx('ME55.Wishiwashi_22', 'Counterattack Grouping')
        active, attacker = e['target'], e['p2_active']
        active.set_attribute(AttrID.HP, 500)
        attacker.set_attribute(AttrID.HP, 500)
        ctx = EffectContext(rig.session, P2, attacker, Attack(title='Test', damage=10))
        await ctx.deal_damage(10, active)
        target = rig.board.pokemon_in_play(P1)[-1]
        await ctx.switch_active(P1, target)
        await _fire_damaged_by_attack_triggers(rig.session, ctx)
        self.assertEqual(attacker.get_attribute(AttrID.HP), 440)

    async def test_float_up_settles_new_active_after_whole_stack_leaves(self):
        rig, e, ctx = self.ctx('ME55.Drifloon_73', 'Float Up')
        source = ctx.attacker
        attached = list(ctx.attached_energies(source))
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertIn(source, ctx.deck())
        self.assertTrue(all(c in ctx.deck() for c in attached))
        await rig.session._settle_empty_active_spots()
        self.assertIsNotNone(ctx.my_active())
        self.assertIsNot(ctx.my_active(), source)

    async def test_all_new_prints_are_legal_in_standard(self):
        from spirit.game.format_manager import FormatManager
        manager = FormatManager()
        for c in loader.cards:
            if c.key == 'ME55':
                self.assertTrue(manager.is_card_eventually_legal('6402e830-7fed-4cd1-b172-2a320047c2bb', c), c.guid)


if __name__ == '__main__':
    unittest.main()
