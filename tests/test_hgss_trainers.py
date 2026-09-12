"""Outcome checks for the HGSS Trainer families and private selections."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext, is_basic_energy, full_stack
from spirit.tools.effect_smoke import P1, P2


class TrainerTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def trainer(self, path):
        rig, e = self.rig(path, 'trainer')
        # Play executor takes the source out of hand before resolving it.
        rig.to_area(e['target'], P1, 'discard')
        return rig, e, EffectContext(rig.session, P1, e['target'], None), definition(path)

    async def test_coin_draw_and_opponent_optional_draw(self):
        for heads in (False, True):
            rig, e, ctx, card = self.trainer('HGSS2.EmceesChatter_73')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            count = ctx.hand_size()
            await card.effect(ctx)
            self.assertEqual(ctx.hand_size() - count, 3 if heads else 2)
        for accept in (False, True):
            rig, e, ctx, card = self.trainer('HGSS2.CheerleadersCheer_71')
            ctx.ask_yes_no = AsyncMock(return_value=accept)
            mine, theirs = ctx.hand_size(), ctx.hand_size(P2)
            await card.effect(ctx)
            self.assertEqual(ctx.hand_size() - mine, 3)
            self.assertEqual(ctx.hand_size(P2) - theirs, int(accept))
            self.assertEqual(ctx.ask_yes_no.call_args.kwargs['player_id'], P2)

    async def test_hand_resets_have_exact_sizes(self):
        for path, count in [('HGSS1.Copycat_90', None),
                            ('HGSS1.ProfessorOaksNewTheory_101', 6),
                            ('HGSS2.Judge_78', 4)]:
            rig, e, ctx, card = self.trainer(path)
            expected = ctx.hand_size(P2) if count is None else count
            await card.effect(ctx)
            self.assertEqual(ctx.hand_size(), expected, path)
            if 'Judge' in path:
                self.assertEqual(ctx.hand_size(P2), 4)

    async def test_public_energy_recovery_amount_and_destination(self):
        for path, zone in [('HGSS1.Fisherman_92', 'hand'), ('HGSS2.EnergyReturner_74', 'deck')]:
            rig, e, ctx, card = self.trainer(path)
            for entry in list(ctx.discard_pile()):
                rig.to_area(entry, P1, 'deck')
            energies = []
            from spirit.game.data_utils import def_for
            for _ in range(4):
                energies.append(self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]), P1, 'discard'))
            special = self.add(rig, definition('HGSS1.DoubleColorlessEnergy_103'), P1, 'discard')
            await card.effect(ctx)
            for energy in energies:
                self.assertIs(energy.parent, rig.board.find_player_area(P1, zone))
            self.assertIn(special, ctx.discard_pile())

    async def test_life_herb_heals_and_cures_on_heads(self):
        for heads in (False, True):
            rig, e, ctx, card = self.trainer('HGSS2.LifeHerb_79')
            target = ctx.my_active()
            target.set_attribute(AttrID.HP, ctx.max_hp(target) - 70)
            target.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned', 'Confused'])
            ctx.choose_pokemon = AsyncMock(return_value=target)
            ctx.flip_coins = AsyncMock(return_value=[heads])
            await card.effect(ctx)
            self.assertEqual(ctx.max_hp(target) - target.get_attribute(AttrID.HP), 10 if heads else 70)
            self.assertEqual(target.get_attribute(AttrID.SPECIAL_CONDITIONS), [] if heads else ['Poisoned', 'Confused'])

    async def test_moomoo_milk_heals_only_chosen_pokemon(self):
        rig, e, ctx, card = self.trainer('HGSS1.MoomooMilk_94')
        target = ctx.my_bench()[0]
        target.set_attribute(AttrID.HP, ctx.max_hp(target) - 70)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.flip_coins = AsyncMock(return_value=[True, False])
        await card.effect(ctx)
        self.assertEqual(ctx.max_hp(target) - target.get_attribute(AttrID.HP), 40)

    async def test_sages_training_two_private_cards_then_rest_discarded(self):
        rig, e, ctx, card = self.trainer('HGSS3.SagesTraining_77')
        viewed = ctx.deck_top(5)
        ctx.choose_cards = AsyncMock(return_value=viewed[:2])
        await card.effect(ctx)
        for entry in viewed[:2]:
            self.assertIn(entry, ctx.hand())
        for entry in viewed[2:]:
            self.assertIn(entry, ctx.discard_pile())
        self.assertEqual(ctx.choose_cards.call_args.kwargs.get('minimum', 2), 2)

    async def test_energy_exchanger_returns_before_search(self):
        rig, e, ctx, card = self.trainer('HGSS3.EnergyExchanger_73')
        energy = next(c for c in ctx.hand() if is_basic_energy(c))
        ctx.choose_cards = AsyncMock(return_value=[energy])
        async def search(*args, **kwargs):
            self.assertIn(energy, ctx.deck())
            return [energy]
        ctx.search_deck = AsyncMock(side_effect=search)
        await card.effect(ctx)
        ctx.search_deck.assert_awaited_once()
        self.assertIn(energy, ctx.hand())

    async def test_seeker_returns_complete_stacks_in_player_order(self):
        rig, e, ctx, card = self.trainer('HGSS4.Seeker_88')
        mine, theirs = ctx.my_bench()[0], ctx.opponent_bench()[0]
        energy = rig.pull_guid(P1, self.energies[PokemonTypes.WATER.value])
        rig.attach(energy, mine)
        ctx.choose_pokemon = AsyncMock(side_effect=[mine, theirs])
        await card.effect(ctx)
        self.assertIn(mine, ctx.hand())
        self.assertIn(energy, ctx.hand())
        self.assertIn(theirs, ctx.hand(P2))
        self.assertEqual([c.kwargs['player_id'] for c in ctx.choose_pokemon.call_args_list], [P1, P2])

    async def test_twins_and_black_belt_require_prize_disadvantage(self):
        for path in ('HGSS4.Twins_89', 'HGSS4.BlackBelt_85'):
            rig, e, ctx, card = self.trainer(path)
            self.assertFalse(card.condition(rig.board, P1, e['target']))
            prize = rig.board.find_player_area(P2, 'prizePile').children[0]
            rig.to_area(prize, P2, 'hand')
            self.assertTrue(card.condition(rig.board, P1, e['target']))

    async def test_exchanges_require_the_public_hand_cost(self):
        from spirit.game.session.effects import is_energy_card, is_pokemon_card
        for path, predicate in [('HGSS3.EnergyExchanger_73', is_energy_card),
                                ('HGSS1.PokmonCommunication_98', is_pokemon_card)]:
            rig, e, ctx, card = self.trainer(path)
            pool = [c for c in ctx.hand() if predicate(c)]
            for entry in pool:
                rig.to_area(entry, P1, 'deck')
            self.assertFalse(card.condition(rig.board, P1, e['target']), path)
            rig.to_area(pool[0], P1, 'hand')
            self.assertTrue(card.condition(rig.board, P1, e['target']), path)

    async def test_conditional_trainers_positive_effects(self):
        from spirit.game.session.passives import compute_damage
        rig, e, ctx, card = self.trainer('HGSS1.FullHeal_93')
        target = ctx.my_active()
        target.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned', 'Asleep'])
        self.assertTrue(card.condition(rig.board, P1, e['target']))
        await card.effect(ctx)
        self.assertEqual(target.get_attribute(AttrID.SPECIAL_CONDITIONS), [])

        rig, e, ctx, card = self.trainer('HGSS4.Twins_89')
        prize = rig.board.find_player_area(P2, 'prizePile').children[0]
        rig.to_area(prize, P2, 'hand')
        chosen = ctx.deck_top(2)
        ctx.choose_cards = AsyncMock(return_value=chosen)
        before = ctx.hand_size()
        await card.effect(ctx)
        self.assertEqual(ctx.hand_size() - before, 2)
        self.assertTrue(all(c in ctx.hand() for c in chosen))

        rig, e, ctx, card = self.trainer('HGSS4.BlackBelt_85')
        prize = rig.board.find_player_area(P2, 'prizePile').children[0]
        rig.to_area(prize, P2, 'hand')
        defender = ctx.opponent_active()
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
        defender.set_attribute(AttrID.RESISTANCE_TYPES, PokemonTypes.UNSET.value)
        before = compute_damage(rig.board, ctx.my_active(), defender, 40).amount
        await card.effect(ctx)
        self.assertEqual(compute_damage(rig.board, ctx.my_active(), defender, 40).amount, before + 40)
        self.assertEqual(compute_damage(rig.board, ctx.my_active(), ctx.opponent_bench()[0],
                                       40, apply_modifiers=False).amount, 40)
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertEqual(compute_damage(rig.board, ctx.my_active(), defender, 40).amount, before)
