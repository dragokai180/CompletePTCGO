"""Prerequisites, self-status branches, and imported attack restrictions."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, SpecialConditions, PokemonTypes
from spirit.game.card_effects.attack_requirements import requirements, printed_attack_allowed
from spirit.game.card_effects.bw_era import bw_legacy_attack
from spirit.game.data_utils import Attack, def_for
from spirit.game.scripts.cards import loader
from spirit.tools.effect_smoke import P1, P2


class GenericAttackClauses(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_staggering_steps_only_confuses_the_printed_coin_target(self):
        for heads in (True, False):
            rig, e, ctx = self.ctx('XY5.Spinda_115', 'Staggering Steps')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            await ctx.ability.effect(ctx)
            self.assertEqual('Confused' in (ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), not heads)
            self.assertEqual('Confused' in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), heads)

    async def test_untamed_punch_requires_existing_damage_for_both_statuses(self):
        for damaged in (False, True):
            rig, e, ctx = self.ctx('SM6.Pangoro_78', 'Untamed Punch')
            if damaged:
                ctx.source.set_attribute(AttrID.HP, ctx.max_hp(ctx.source) - 10)
            ctx.deal_damage = AsyncMock(return_value=50)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], 100 if damaged else 50)
            for pokemon in (ctx.source, ctx.defender):
                self.assertEqual('Confused' in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), damaged)

    async def test_caturday_requires_at_least_one_actual_draw(self):
        for remaining in (0, 1, 3):
            rig, e, ctx = self.ctx('SM10.Meowstic_80', 'Caturday')
            for card in list(ctx.deck())[remaining:]:
                rig.to_area(card, P1, 'discard')
            hand = len(ctx.hand())
            await ctx.ability.effect(ctx)
            self.assertEqual(len(ctx.hand()) - hand, remaining)
            self.assertEqual('Asleep' in (ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), remaining > 0)

    async def test_hypno_headbutt_choice_controls_bonus_and_sleep(self):
        for accept in (False, True):
            rig, e, ctx = self.ctx('XY1.Bibarel_107', 'Hypno Headbutt')
            ctx.ask_yes_no = AsyncMock(return_value=accept)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            ctx.ask_yes_no.assert_awaited_once()
            ctx.deal_damage.assert_awaited_once_with(90 if accept else 60)
            self.assertEqual('Asleep' in (ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), accept)

    async def test_poisonous_musculature_checks_actual_attachment_and_order(self):
        for selected, attached in ((False, False), (True, False), (True, True)):
            rig, e, ctx = self.ctx('SV065.Okidogiex_36', 'Poisonous Musculature')
            energy = self.add(rig, def_for(self.energies[PokemonTypes.DARKNESS.value]), P1, 'deck')
            calls = []
            async def attach(*args):
                calls.append('attach')
                return attached
            async def shuffle(): calls.append('shuffle')
            async def status(*args): calls.append('status')
            ctx.search_deck = AsyncMock(return_value=[energy] if selected else [])
            ctx.attach_energy = AsyncMock(side_effect=attach)
            ctx.shuffle_deck = AsyncMock(side_effect=shuffle)
            ctx.apply_special_condition = AsyncMock(side_effect=status)
            await ctx.ability.effect(ctx)
            self.assertEqual(calls, (['attach'] if selected else []) + ['shuffle'] + (['status'] if attached else []))
            self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)

    def test_every_generic_explicit_attack_restriction_is_parsed(self):
        seen = set()
        for model in loader.cards:
            for attack in getattr(def_for(model.guid), 'abilities', ()):
                if not isinstance(attack, Attack) or attack.effect is not bw_legacy_attack:
                    continue
                rules, unknown = requirements(attack.game_text)
                self.assertFalse(unknown, (model.guid, attack.title, unknown))
                if rules:
                    self.assertIsNotNone(attack.condition, attack.title)
                    seen.add(attack.title)
        self.assertGreaterEqual(len(seen), 22)

    async def test_history_ban_is_owner_scoped_and_survives_source_leaving(self):
        for path, title in (('SV08.Sylveonex_86', 'Angelite'),
                            ('SV085.Sylveonex_41', 'Angelite'),
                            ('SM12.Walrein_52', 'Cold Snap'), ('XY12.Mewtwo_51', 'Barrier')):
            rig, e, ctx = self.ctx(path, title)
            state = rig.session.turn_state
            self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
            state.attack_titles_prev_turn_by_player[P2] = [title]
            self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
            state.attack_titles_prev_turn_by_player[P1] = [title]
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
            ctx.deal_damage = AsyncMock()
            ctx.shuffle_into_deck = AsyncMock()
            await ctx.ability.effect(ctx)
            ctx.deal_damage.assert_not_awaited()
            ctx.shuffle_into_deck.assert_not_awaited()

    async def test_first_turn_only_and_damaged_requirements(self):
        rig, e, ctx = self.ctx('SV06.Illumise_10', 'Slowing Perfume')
        for turn in (1, 2, 3, 4):
            rig.session.turn_state.turn_number = turn
            self.assertEqual(ctx.ability.condition(rig.board, P1, ctx.source), turn == 2)
        rig, e, ctx = self.ctx('SM9.Beedrill_5', 'Destiny Stinger')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.source.set_attribute(AttrID.HP, ctx.max_hp(ctx.source) - 10)
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_combo_uses_the_players_previous_turn_not_the_opponents(self):
        rig, e, ctx = self.ctx('SV085.Miltank_81', 'Moomoo Rolling')
        state = rig.session.turn_state
        record = (ctx.source.entity_id, ctx.source.archetype_id, 'Rollout')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        state.attacks_used_last_turn = [record]
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        state.attacks_prev_turn_by_player[P1] = [record]
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        state.attacks_prev_turn_by_player[P1] = [('another-pokemon', ctx.source.archetype_id, 'Rollout')]
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_copied_restricted_attack_does_not_execute(self):
        rig, e, ctx = self.ctx('SM9.Beedrill_5', 'Destiny Stinger')
        attack = ctx.ability
        ctx._copy_chain = ['Metronome']
        ctx.knock_out = AsyncMock()
        self.assertFalse(await ctx.use_attack(attack))
        ctx.knock_out.assert_not_awaited()
        self.assertEqual(ctx._copy_chain, ['Metronome'])

    async def test_angelite_handles_one_target_and_respects_protection(self):
        for path in ('SV08.Sylveonex_86', 'SV085.Sylveonex_41'):
            for protected in (False, True):
                rig, e, ctx = self.ctx(path, 'Angelite')
                target = ctx.opponent_bench()[0]
                for extra in ctx.opponent_bench()[1:]:
                    rig.to_area(extra, P2, 'discard')
                ctx.choose_cards = AsyncMock(return_value=[target])
                ctx.effects_blocked = lambda pokemon: protected
                ctx.shuffle_into_deck = AsyncMock()
                self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.choose_cards.call_args.args[1], 1)
                self.assertEqual(ctx.choose_cards.call_args.kwargs['minimum'], 1)
                moved = [c for call in ctx.shuffle_into_deck.call_args_list for c in call.args[0]]
                self.assertEqual(target in moved, not protected)
