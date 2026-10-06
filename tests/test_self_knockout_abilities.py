"""Activated Abilities must complete their benefit and printed self-KO."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import is_energy_card
from spirit.game.session.legal_actions import ability_condition_met
from spirit.tools.effect_smoke import P1, P2


class SelfKnockoutAbilityTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_extra_energy_bomb_attaches_only_to_eligible_pokemon_and_awards_prizes(self):
        rig, e, ctx = self.ctx('SM7.ElectrodeGX_48', 'Extra Energy Bomb')
        gx = self.add(rig, fixtures.definition('SM7.RayquazaGX_109'), P1, 'bench')
        ex = self.add(rig, fixtures.definition('XY5.GroudonEX_85'), P1, 'bench')
        receiver = next(p for p in ctx.my_bench() if p is not gx and p is not ex
                        and p.archetype_id != ctx.source.archetype_id)
        energies = [card for card in ctx.discard_pile() if is_energy_card(card)][:5]
        self.assertEqual(len(energies), 5)
        self.assertTrue(ability_condition_met(ctx.ability, rig.board, P1, ctx.source))
        ctx.choose_cards = AsyncMock(return_value=energies)
        ctx.choose_pokemon = AsyncMock(return_value=receiver)
        prizes_before = len(rig.board.find_player_area(P2, 'prizePile').children)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_cards.call_args.kwargs['minimum'], 5)
        for call in ctx.choose_pokemon.call_args_list:
            self.assertNotIn(ctx.source, call.args[0])
            self.assertNotIn(gx, call.args[0])
            self.assertNotIn(ex, call.args[0])
        self.assertTrue(all(energy in ctx.attached_energies(receiver) for energy in energies))
        self.assertIn(ctx.source, ctx.knockouts)
        await rig.session.resolve_knockouts(ctx)
        self.assertEqual(len(rig.board.find_player_area(P2, 'prizePile').children), prizes_before - 2)

    async def test_extra_energy_bomb_needs_eligible_target(self):
        rig, e, ctx = self.ctx('SM7.ElectrodeGX_48', 'Extra Energy Bomb')
        for pokemon in list(ctx.my_bench()):
            if pokemon.archetype_id != ctx.source.archetype_id:
                rig.to_area(pokemon, P1, 'discard')
        self.assertFalse(ability_condition_met(ctx.ability, rig.board, P1, ctx.source))
        self.add(rig, self.filler, P1, 'bench')
        self.assertTrue(ability_condition_met(ctx.ability, rig.board, P1, ctx.source))

    async def test_extra_energy_bomb_uses_available_energy_when_fewer_than_five(self):
        rig, e, ctx = self.ctx('SM7.ElectrodeGX_48', 'Extra Energy Bomb')
        energies = [card for card in ctx.discard_pile() if is_energy_card(card)]
        for card in energies[2:]:
            rig.to_area(card, P1, 'hand')
        receiver = next(p for p in ctx.my_bench()
                        if p.archetype_id != ctx.source.archetype_id)
        ctx.choose_cards = AsyncMock(return_value=energies[:2])
        ctx.choose_pokemon = AsyncMock(return_value=receiver)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_cards.call_args.args[1], 2)
        self.assertEqual(ctx.choose_cards.call_args.kwargs['minimum'], 2)
        self.assertTrue(all(card in ctx.attached_energies(receiver) for card in energies[:2]))
        self.assertIn(ctx.source, ctx.knockouts)

    async def test_mysterious_message_knocks_out_only_after_drawing(self):
        for hand_size in (6, 7):
            with self.subTest(hand_size=hand_size):
                rig, e, ctx = self.ctx('SM10.Mismagius_78', 'Mysterious Message')
                for card in list(ctx.hand())[hand_size:]:
                    rig.to_area(card, P1, 'discard')
                while len(ctx.hand()) < hand_size:
                    rig.to_area(ctx.deck()[0], P1, 'hand')
                await ctx.ability.effect(ctx)
                self.assertEqual(len(ctx.hand()), 7)
                self.assertEqual(ctx.source in ctx.knockouts, hand_size == 6)

    async def test_exploding_energy_search_attaches_shuffles_and_knocks_out(self):
        rig, e, ctx = self.ctx('SV2.Forretressex_5', 'Exploding Energy')
        grass = next(card for card in ctx.deck()
                     if card.archetype_id.lower() == self.energies[PokemonTypes.GRASS.value].lower())
        receiver = ctx.my_bench()[0]
        ctx.search_deck = AsyncMock(return_value=[grass])
        ctx.choose_pokemon = AsyncMock(return_value=receiver)
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertTrue(ctx.search_deck.call_args.args[0](grass))
        self.assertIn(grass, ctx.attached_energies(receiver))
        ctx.shuffle_deck.assert_awaited_once()
        self.assertIn(ctx.source, ctx.knockouts)

    async def test_call_signal_knocks_out_after_search_even_with_no_match(self):
        rig, e, ctx = self.ctx('SM12.Magneton_69', 'Call Signal')
        ctx.search_deck = AsyncMock(return_value=[])
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.search_deck.assert_awaited_once()
        ctx.shuffle_deck.assert_awaited_once()
        self.assertIn(ctx.source, ctx.knockouts)

    async def test_six_feet_under_knocks_out_then_distributes_three_counters(self):
        rig, e, ctx = self.ctx('BW9.Cofagrigus_56', 'Six Feet Under')
        target = ctx.opponent_active()
        hp_before = target.get_attribute(AttrID.HP)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ctx.ability.effect(ctx)
        self.assertIn(ctx.source, ctx.knockouts)
        self.assertEqual(target.get_attribute(AttrID.HP), hp_before - 30)


if __name__ == '__main__':
    unittest.main()
