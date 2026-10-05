"""Horror House-GX locks every kind of hand play for one opposing turn."""

import unittest
from unittest.mock import AsyncMock

from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import ACTION_EVOLVE, compute_legal_actions
from spirit.tools.effect_smoke import P1, P2
from tests import test_hgss_rules as fixtures


class HorrorHouseGxTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def setup_attack(self, extra_psychic=False):
        rig, _, ctx = self.ctx('SM9.GengarMimikyuGX_53', 'Horror House-GX')
        for energy in list(ctx.attached_energies(ctx.attacker)):
            rig.to_area(energy, P1, 'deck')
        psychic = CARD_DEFS_BY_GUID[self.energies[PokemonTypes.PSYCHIC.value].lower()]
        for _ in range(2 if extra_psychic else 1):
            rig.attach(self.add(rig, psychic, P1, 'hand'), ctx.attacker)
        return rig, ctx

    def hand_offers(self, rig, player_id):
        hand = rig.board.find_player_area(player_id, 'hand')
        hand_ids = {card.entity_id for card in hand.children}
        return {entry['entityID'] for entry in compute_legal_actions(
            rig.board, rig.session.turn_state, player_id, rig.session.game_id)
            if entry['entityID'] in hand_ids}

    async def test_all_hand_plays_locked_only_for_opponents_next_turn(self):
        rig, ctx = self.setup_attack()
        basic = self.add(rig, self.filler, P2, 'hand')
        item = self.add(rig, self.item, P2, 'hand')
        rattata = self.add(rig, fixtures.definition('XY12.Rattata_66'), P2, 'bench')
        evolution = self.add(rig, fixtures.definition('XY12.Raticate_67'), P2, 'hand')
        energy = next(card for card in ctx.hand(P2)
                      if card.archetype_id.lower() ==
                      self.energies[PokemonTypes.PSYCHIC.value].lower())
        hand_cards = (basic, evolution, item, energy)
        evolution_entry = next(entry for entry in compute_legal_actions(
            rig.board, rig.session.turn_state, P2, rig.session.game_id)
            if entry['entityID'] == evolution.entity_id
            and entry['selectableAction']['description'] == ACTION_EVOLVE)
        self.assertTrue({card.entity_id for card in hand_cards}
                        <= self.hand_offers(rig, P2))

        await ctx.ability.effect(ctx)
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertFalse({card.entity_id for card in hand_cards}
                         & self.hand_offers(rig, P2))
        await rig.session._execute_play_basic(P2, basic)
        self.assertIn(basic, ctx.hand(P2))
        self.assertFalse(await rig.session._execute_evolve(
            P2, evolution, evolution_entry, [rattata.entity_id]))
        self.assertIn(evolution, ctx.hand(P2))

        rig.session.turn_state.begin_turn(P1, rig.board)
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertTrue({card.entity_id for card in hand_cards}
                        <= self.hand_offers(rig, P2))

    async def test_extra_psychic_draws_both_players_to_seven(self):
        for boosted in (False, True):
            with self.subTest(boosted=boosted):
                rig, ctx = self.setup_attack(extra_psychic=boosted)
                for pid in (P1, P2):
                    hand = rig.board.find_player_area(pid, 'hand')
                    deck = rig.board.find_player_area(pid, 'deck')
                    for card in list(hand.children)[1:]:
                        rig.board.move_card(card.entity_id, deck.entity_id)

                await ctx.ability.effect(ctx)

                expected = 7 if boosted else 1
                for pid in (P1, P2):
                    self.assertEqual(len(ctx.hand(pid)), expected)
                self.assertTrue(rig.session.turn_state.play_locks.get(P2))

    async def test_effects_cannot_put_hand_cards_in_play_but_deck_and_discard_work(self):
        rig, ctx = self.setup_attack()
        psychic = CARD_DEFS_BY_GUID[self.energies[PokemonTypes.PSYCHIC.value].lower()]
        hand_energy = self.add(rig, psychic, P2, 'hand')
        discard_energy = self.add(rig, psychic, P2, 'discard')
        hand_basic = self.add(rig, self.filler, P2, 'hand')
        deck_basic = self.add(rig, self.filler, P2, 'deck')
        hand_evolution = self.add(
            rig, fixtures.definition('XY12.Raticate_67'), P2, 'hand')
        await ctx.ability.effect(ctx)
        rig.session.turn_state.begin_turn(P2, rig.board)
        effect = EffectContext(rig.session, P2, rig.board.active_pokemon(P2), None)
        active = rig.board.active_pokemon(P2)

        self.assertFalse(await effect.attach_energy(hand_energy, active))
        self.assertIn(hand_energy, ctx.hand(P2))
        self.assertTrue(await effect.attach_energy(discard_energy, active))
        self.assertIn(discard_energy, active.children)
        self.assertFalse(await effect.bench_pokemon(hand_basic))
        self.assertIn(hand_basic, ctx.hand(P2))
        self.assertTrue(await effect.bench_pokemon(deck_basic))
        self.assertIn(deck_basic, rig.board.find_player_area(P2, 'bench').children)
        self.assertFalse(await effect.evolve_pokemon(deck_basic, hand_evolution))
        self.assertIn(hand_evolution, ctx.hand(P2))

    async def test_hand_ability_is_unavailable_under_lock(self):
        rig, ctx = self.setup_attack()
        pyukumuku = self.add(
            rig, fixtures.definition('SWSH8.Pyukumuku_77'), P2, 'hand')
        ability_entry = next(entry for entry in compute_legal_actions(
            rig.board, rig.session.turn_state, P2, rig.session.game_id)
            if entry['entityID'] == pyukumuku.entity_id
            and entry['selectableAction']['description'] == 'UsePokemonAbility')

        await ctx.ability.effect(ctx)
        rig.session.turn_state.begin_turn(P2, rig.board)

        self.assertNotIn(pyukumuku.entity_id, self.hand_offers(rig, P2))
        self.assertFalse(await rig.session._execute_use_ability(
            P2, pyukumuku, ability_entry))
        self.assertIn(pyukumuku, ctx.hand(P2))

    async def test_ice_dance_does_not_offer_locked_hand_energy(self):
        rig, ctx = self.setup_attack()
        frosmoth_def = fixtures.definition('SWSH1.Frosmoth_64')
        frosmoth = self.add(rig, frosmoth_def, P2, 'bench')
        self.add(rig, fixtures.definition('MEP.Sobble_54'), P2, 'bench')
        water = self.add(rig, CARD_DEFS_BY_GUID[
            self.energies[PokemonTypes.WATER.value].lower()], P2, 'hand')
        effect = EffectContext(rig.session, P2, frosmoth, frosmoth_def.abilities[0])
        effect.choose_cards = AsyncMock()

        await ctx.ability.effect(ctx)
        rig.session.turn_state.begin_turn(P2, rig.board)
        await effect.ability.effect(effect)

        effect.choose_cards.assert_not_awaited()
        self.assertIn(water, ctx.hand(P2))


if __name__ == '__main__':
    unittest.main()
