"""Printed clauses resolve once, in order, with their own prerequisites."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.tools.effect_smoke import P1, P2


class InterpreterTransactionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    ctx = fixtures.HgssRulesTests.ctx
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_coin_draw_requires_heads(self):
        for heads in (False, True):
            rig, entries, ctx = self.ctx('SM1.Eevee_101', 'Quick Draw')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            before = ctx.hand_size()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.hand_size() - before, int(heads))

    async def test_draw_per_heads_includes_zero_and_multiple(self):
        for heads in (0, 3):
            rig, entries, ctx = self.ctx('SM11.Pikachu_55', 'Meal Time')
            ctx.flip_coins = AsyncMock(side_effect=[[True]] * heads + [[False]])
            before = ctx.hand_size()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.hand_size() - before, heads)

    async def test_named_bench_draw_and_bonus(self):
        cases = (
            ('Promo_XY.Hoopa_90', 'Summoning Draw', 'SM11.Pikachu_55', 0, 3),
            ('Promo_XY.Latias_78', 'Eon Connection', 'Promo_XY.Latios_79', 1, 2),
        )
        for path, title, partner, absent, present in cases:
            for has_partner in (False, True):
                with self.subTest(path=path, has_partner=has_partner):
                    rig, entries, ctx = self.ctx(path, title)
                    if has_partner:
                        self.add(rig, definition(partner), P1, 'bench')
                    before = ctx.hand_size()
                    await ctx.ability.effect(ctx)
                    self.assertEqual(ctx.hand_size() - before, present if has_partner else absent)

    async def test_draw_per_named_pokemon(self):
        rig, entries, ctx = self.ctx('SM8.Houndour_45', 'Team Hunt')
        self.add(rig, definition('SM8.Houndour_45'), P1, 'bench')
        before = ctx.hand_size()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.hand_size() - before, 3)

    async def test_opponents_hand_reset_occurs_once(self):
        rig, entries, ctx = self.ctx('XY1.Talonflame_28', 'Devastating Wind')
        ctx.draw_cards = AsyncMock(wraps=ctx.draw_cards)
        ctx.shuffle_into_deck = AsyncMock(wraps=ctx.shuffle_into_deck)
        await ctx.ability.effect(ctx)
        ctx.draw_cards.assert_awaited_once_with(4, player_id=P2)
        ctx.shuffle_into_deck.assert_awaited_once()
        self.assertEqual(ctx.hand_size(P2), 4)

    async def test_optional_top_cards_keep_or_discard_then_draw(self):
        for path, title, count in (
            ('SV4.Tinkatink_82', 'Mountain Scrounging', 1),
            ('SV3.Greedentex_179', 'Never Ever Enough', 3),
        ):
            for accept in (False, True):
                with self.subTest(path=path, accept=accept):
                    rig, entries, ctx = self.ctx(path, title)
                    top = ctx.deck_top(count)
                    remaining = ctx.deck_top(count * 2)[count:]
                    ctx.ask_yes_no = AsyncMock(return_value=accept)
                    ctx.draw_cards = AsyncMock(wraps=ctx.draw_cards)
                    ctx.reveal_cards = AsyncMock(wraps=ctx.reveal_cards)
                    before = ctx.hand_size()
                    await ctx.ability.effect(ctx)
                    ctx.ask_yes_no.assert_awaited_once()
                    self.assertEqual(ctx.hand_size() - before, count)
                    self.assertTrue(all(card in (ctx.hand() if accept else ctx.discard_pile()) for card in top))
                    if not accept:
                        self.assertTrue(all(card in ctx.hand() for card in remaining))
                    self.assertEqual(ctx.draw_cards.await_count, int(not accept))
                    self.assertEqual(ctx.reveal_cards.call_args.kwargs['to_player'], P1)

    async def test_lost_zone_payment_precedes_single_draw(self):
        for has_hand in (False, True):
            rig, entries, ctx = self.ctx('SM12.Whimsicott_148', 'Sneaky Pocket')
            if not has_hand:
                for card in list(ctx.hand()):
                    rig.to_area(card, P1, 'deck')
            events = []
            original_move, original_draw = ctx.move_to_lost_zone, ctx.draw_cards

            async def move(cards):
                events.append('pay')
                return await original_move(cards)

            async def draw(count, **kwargs):
                events.append(('draw', count))
                return await original_draw(count, **kwargs)

            ctx.move_to_lost_zone, ctx.draw_cards = move, draw
            await ctx.ability.effect(ctx)
            self.assertEqual(events, ['pay', ('draw', 3)] if has_hand else [])

    async def test_bottom_draw_does_not_take_top_cards(self):
        rig, entries, ctx = self.ctx('SV10.Rabscaex_25', 'Upside-Down Draw')
        bottom, top = list(ctx.deck())[:3], ctx.deck_top(3)
        before = ctx.hand_size()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.hand_size() - before, 3)
        self.assertTrue(all(card in ctx.hand() for card in bottom))
        self.assertTrue(all(card in ctx.deck() for card in top))

    async def test_sages_riddle_only_winner_draws(self):
        rig, entries, ctx = self.ctx('SM11.Oranguru_182', "Sage's Riddle")
        chosen = self.add(rig, definition('SM11.Pikachu_55'), P1, 'hand')
        ctx.choose_cards = AsyncMock(return_value=[chosen])
        ctx.choose = AsyncMock(return_value=3)  # Lightning
        ctx.draw_cards = AsyncMock(wraps=ctx.draw_cards)
        await ctx.ability.effect(ctx)
        ctx.draw_cards.assert_awaited_once_with(4, player_id=P2)
        self.assertIn(chosen, ctx.hand())

    async def test_coin_gated_self_energy_discard(self):
        for path, title, kind, loss in (
            ('Promo_SM.Latios_136', 'Luster Purge', PokemonTypes.WATER, 4),
            ('Promo_XY.RayquazaEX_66', 'Aeroscream', PokemonTypes.WATER, 2),
            ('TwentiethAnn.NinetalesEX_13', 'Fire Blast', PokemonTypes.FIRE, 1),
        ):
            for heads in (False, True):
                with self.subTest(path=path, heads=heads):
                    rig, entries, ctx = self.ctx(path, title)
                    for energy in list(ctx.attached_energies(ctx.attacker)):
                        rig.to_area(energy, P1, 'discard')
                    for _ in range(4):
                        energy = self.add(rig, def_for(self.energies[kind.value]), P1, 'hand')
                        rig.attach(energy, ctx.attacker)
                    ctx.flip_coins = AsyncMock(return_value=[heads])
                    ctx.deal_damage = AsyncMock(return_value=0)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(len(ctx.attached_energies(ctx.attacker)), 4 if heads else 4 - loss)

    async def test_false_swipe_requires_heads_and_resolves_once(self):
        for path in ('SM10.Kartana_19', 'XY5.Doublade_99'):
            for heads in (False, True):
                with self.subTest(path=path, heads=heads):
                    rig, entries, ctx = self.ctx(path, 'False Swipe')
                    ctx.flip_coins = AsyncMock(return_value=[heads])
                    ctx.set_damage_counters = AsyncMock(wraps=ctx.set_damage_counters)
                    before = ctx.defender.get_attribute(AttrID.HP)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(ctx.set_damage_counters.await_count, int(heads))
                    self.assertEqual(ctx.defender.get_attribute(AttrID.HP), 10 if heads else before)

    async def test_coin_mill_requires_heads(self):
        for heads in (False, True):
            rig, entries, ctx = self.ctx('SV1.Wiglett_56', 'Dig a Little')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            before = len(ctx.deck(P2))
            await ctx.ability.effect(ctx)
            self.assertEqual(before - len(ctx.deck(P2)), int(heads))

    async def test_mist_ball_discards_one_of_each_type_only_on_tails(self):
        for heads in (False, True):
            rig, entries, ctx = self.ctx('Promo_SM.Latias_135', 'Mist Ball')
            for energy in list(ctx.attached_energies(ctx.attacker)):
                rig.to_area(energy, P1, 'discard')
            energies = []
            for kind in (PokemonTypes.FIRE, PokemonTypes.PSYCHIC):
                for _ in range(2):
                    energy = self.add(rig, def_for(self.energies[kind.value]), P1, 'hand')
                    rig.attach(energy, ctx.attacker)
                    energies.append(energy)
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(len(ctx.attached_energies(ctx.attacker)), 4 if heads else 2)
            for pair in (energies[:2], energies[2:]):
                self.assertEqual(sum(e in ctx.discard_pile() for e in pair), int(not heads))

    async def test_fluorite_heals_each_tera_once(self):
        rig, entries, ctx = self.ctx('SV3.Greedentex_179', 'Never Ever Enough')
        from copy import copy
        ctx.ability = copy(definition('SV08.TechnicalMachineFluorite_188').granted_abilities[0])
        ctx.heal = AsyncMock()
        await ctx.ability.effect(ctx)
        targets = [call.args[1] for call in ctx.heal.call_args_list]
        self.assertEqual(len(targets), 2)  # Active plus fixture's second copy.
        self.assertEqual(len(set(p.entity_id for p in targets)), 2)

    async def test_heart_wink_skips_only_opponents_next_turn_draw(self):
        for heads in (False, True):
            rig, entries, ctx = self.ctx('XY2.Luvdisc_27', 'Heart Wink')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            mine, theirs = ctx.hand_size(), ctx.hand_size(P2)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.hand_size(), mine)
            rig.session.send_game_sequence = AsyncMock()
            await rig.session._begin_turn(P2)
            self.assertEqual(ctx.hand_size(P2), theirs + int(not heads))
            # Other draws remain legal; the next opponent turn draws normally.
            await ctx.draw_cards(1, player_id=P2)
            self.assertEqual(ctx.hand_size(P2), theirs + 1 + int(not heads))
            await rig.session._begin_turn(P1)
            self.assertEqual(ctx.hand_size(), mine + 1)
            await rig.session._begin_turn(P2)
            self.assertEqual(ctx.hand_size(P2), theirs + 2 + int(not heads))

    async def test_discard_one_energy_per_heads(self):
        for heads in (0, 1, 2):
            rig, entries, ctx = self.ctx('BW4.Pinsir_1', 'Power Pinch')
            for energy in list(ctx.attached_energies(ctx.defender)):
                rig.to_area(energy, P2, 'discard')
            for _ in range(4):
                energy = self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]), P2, 'hand')
                rig.attach(energy, ctx.defender)
            ctx.flip_coins = AsyncMock(return_value=[True] * heads + [False] * (2 - heads))
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(len(ctx.attached_energies(ctx.defender)), 4 - heads)

    async def test_head_status_and_tail_discard_are_independent(self):
        for heads in (False, True):
            rig, entries, ctx = self.ctx('BW2.Gothitelle_48', 'Mental Shock')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.deal_damage = AsyncMock(return_value=0)
            before = len(ctx.attached_energies(ctx.defender))
            await ctx.ability.effect(ctx)
            self.assertEqual(len(ctx.attached_energies(ctx.defender)), before - int(not heads))
            self.assertEqual('Confused' in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), heads)

    async def test_search_one_energy_per_heads(self):
        for heads in (0, 1, 3):
            rig, entries, ctx = self.ctx('SM10.Porygon_154', 'Digicharge')
            for _ in range(4):
                self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]), P1, 'deck')
            ctx.flip_coins = AsyncMock(return_value=[True] * heads + [False] * (3 - heads))
            ctx.shuffle_deck = AsyncMock(wraps=ctx.shuffle_deck)
            before = ctx.hand_size()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.hand_size() - before, heads)
            self.assertEqual(ctx.shuffle_deck.await_count, int(heads > 0))

    async def test_attach_one_discard_energy_per_heads(self):
        for heads in (0, 1, 3):
            rig, entries, ctx = self.ctx('BW8.Manaphy_34', 'Seafaring')
            for _ in range(4):
                self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]), P1, 'discard')
            ctx.flip_coins = AsyncMock(return_value=[True] * heads + [False] * (3 - heads))
            ctx.attach_energy = AsyncMock(wraps=ctx.attach_energy)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.attach_energy.await_count, heads)
            self.assertTrue(all(call.args[1] in ctx.my_bench() for call in ctx.attach_energy.call_args_list))

    async def test_hurricane_call_limits_targets_to_original_ex_and_gx(self):
        rig, entries, ctx = self.ctx('HF.Zapdos_24', 'Hurricane Call')
        allowed = self.add(rig, definition('BW6.RayquazaEX_85'), P1, 'bench')
        for _ in range(4):
            self.add(rig, def_for(self.energies[PokemonTypes.LIGHTNING.value]), P1, 'deck')
        ctx.flip_coins = AsyncMock(return_value=[True, True, True, False])
        ctx.attach_energy = AsyncMock(wraps=ctx.attach_energy)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.attach_energy.await_count, 3)
        self.assertTrue(all(call.args[1] is allowed for call in ctx.attach_energy.call_args_list))

    async def test_variable_coin_count_uses_both_active_pokemon(self):
        rig, entries, ctx = self.ctx('SV08.Exeggutor_3', "Barrage O'Clock")
        from spirit.game.card_effects.bw_era import _energy_count
        expected = _energy_count(ctx, ctx.attacker) + _energy_count(ctx, ctx.defender)
        ctx.flip_coins = AsyncMock(side_effect=lambda count, *args: [False] * count)
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.flip_coins.call_args.args[0], expected)

    async def test_dimension_transfer_puts_chosen_item_on_top(self):
        rig, entries, ctx = self.ctx('HGSS4.PorygonZ_7', 'Dimension Transfer')
        item = self.add(rig, self.item, P1, 'discard')
        ctx.choose_cards = AsyncMock(return_value=[item])
        for heads in (False, True):
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.reveal_cards = AsyncMock(wraps=ctx.reveal_cards)
            await ctx.ability.effect(ctx)
            if heads:
                self.assertIs(ctx.deck_top(1)[0], item)
            else:
                self.assertIn(item, ctx.discard_pile())

    async def test_opponent_peek_prompts_and_shuffles_once(self):
        for accept in (False, True):
            rig, entries, ctx = self.ctx('SV065.Inkay_33', 'Mischievous Tentacles')
            ctx.ask_yes_no = AsyncMock(return_value=accept)
            ctx.shuffle_deck = AsyncMock(wraps=ctx.shuffle_deck)
            await ctx.ability.effect(ctx)
            ctx.ask_yes_no.assert_awaited_once()
            self.assertEqual(ctx.shuffle_deck.await_count, int(accept))

    async def test_modern_ex_energy_discard_is_restricted_and_not_duplicated(self):
        for path, expected in (
            ('BW1.Snivy_1', 0), ('BW6.RayquazaEX_85', 0), ('SV3.Greedentex_179', 1),
        ):
            with self.subTest(path=path):
                rig, entries, ctx = self.ctx('SV08.Turtonator_137', 'Fully Singe')
                old = ctx.defender
                rig.to_area(old, P2, 'bench')
                defender = self.add(rig, definition(path), P2, 'activePokemonArea')
                # EffectContext resolves the current defending Active dynamically.
                for _ in range(3):
                    energy = self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]), P2, 'hand')
                    rig.attach(energy, defender)
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertEqual(len(ctx.attached_energies(defender)), 3 - expected)

    async def test_devolution_removes_only_one_stage(self):
        for path, title, zone in (
            ('XY9.EspeonEX_52', 'Miraculous Shine', 'hand'),
            ('SM11.Celebi_4', 'Time Spiral', 'deck'),
            ('SV08.Espathra_95', 'Mystical Eyes', 'hand'),
        ):
            with self.subTest(path=path):
                rig, entries, ctx = self.ctx(path, title)
                basic = self.add(rig, definition('BW1.Tepig_15'), P2, 'hand')
                stage_one = self.add(rig, definition('BW1.Pignite_17'), P2, 'hand')
                stage_two = self.add(rig, definition('BW1.Emboar_19'), P2, 'bench')
                rig.attach(basic, stage_one)
                rig.attach(stage_one, stage_two)
                ctx.deal_damage = AsyncMock(return_value=0)
                ctx.devolve_pokemon = AsyncMock(wraps=ctx.devolve_pokemon)
                await ctx.ability.effect(ctx)
                ctx.devolve_pokemon.assert_awaited_once()
                self.assertIn(stage_one, ctx.opponent_bench())
                self.assertIs(basic.parent, stage_one)
                self.assertIs(stage_two.parent, rig.board.find_player_area(P2, zone))

    async def test_daunting_eyes_shuffles_one_energy_per_heads(self):
        rig, entries, ctx = self.ctx('SV4.Masquerain_2', 'Daunting Eyes')
        for energy in list(ctx.attached_energies(ctx.defender)):
            rig.to_area(energy, P2, 'discard')
        for _ in range(4):
            energy = self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]), P2, 'hand')
            rig.attach(energy, ctx.defender)
        ctx.flip_coins = AsyncMock(side_effect=[[True], [True], [False]])
        before = len(ctx.deck(P2))
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.attached_energies(ctx.defender)), 2)
        self.assertEqual(len(ctx.deck(P2)) - before, 2)

    async def test_own_devolution_selects_number_of_stages_once(self):
        for path, title in (
            ('SM8.Celebi_19', 'Time Distortion'),
            ('XY7.PorygonZ_67', 'Digital Reboot'),
        ):
            for steps in (1, 2):
                with self.subTest(path=path, steps=steps):
                    rig, entries, ctx = self.ctx(path, title)
                    for pokemon in list(ctx.my_bench()):
                        rig.to_area(pokemon, P1, 'discard')
                    basic = self.add(rig, definition('BW1.Tepig_15'), P1, 'hand')
                    middle = self.add(rig, definition('BW1.Pignite_17'), P1, 'hand')
                    top = self.add(rig, definition('BW1.Emboar_19'), P1, 'bench')
                    rig.attach(basic, middle)
                    rig.attach(middle, top)
                    ctx.choose_cards = AsyncMock(return_value=[top])
                    ctx.choose = AsyncMock(return_value=steps - 1)
                    ctx.ask_yes_no = AsyncMock(return_value=True)
                    await ctx.ability.effect(ctx)
                    self.assertIn(top, ctx.hand())
                    self.assertIn(basic if steps == 2 else middle, ctx.my_bench())
                    ctx.choose_cards.assert_awaited_once()
                    ctx.choose.assert_awaited_once()
                    ctx.ask_yes_no.assert_not_awaited()
