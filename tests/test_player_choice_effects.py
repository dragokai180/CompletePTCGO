"""Controller, viewer, and destination are separate roles in player-choice effects."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.session.effects import EffectContext
from spirit.game.card_effects.standard_era import standard_trainer_effect
from spirit.tools.effect_smoke import P1, P2


ORDER_CASES = (
    ('HGSS1.Slowking_12', 'Second Sight', 3, 'either'),
    ('COL.Slowking_32', 'Second Sight', 3, 'either'),
    ('HGSS4.Celebi_3', 'Future Sight', 5, 'either'),
    ('XY7.Baltoy_32', 'Future Spin', 3, 'either'),
    ('XY6.Xatu_29', 'Future Sight', 5, 'either'),
    ('SM2.Absol_81', 'Future Sight', 4, 'either'),
    ('SM11.Munna_88', 'Future Sight', 4, 'either'),
    ('SM12.Natu_78', 'Future Sight', 4, 'either'),
    ('SV3.Absolex_135', 'Future Sight', 3, 'either'),
    ('SWSH3.Lunatone_72', 'Future Sight', 4, 'either'),
    ('SWSH4.Duskull_69', 'Future Sight', 4, 'either'),
    ('SWSH11.Porygon_140', 'Branch Calculation', 4, 'either'),
    ('SWSH3.Gothita_73', 'Fortunate Eye', 5, 'opponent'),
    ('SWSH1.Orbeetle_19', "Bug's Radar", 3, 'opponent'),
    ('XY11.Aipom_90', 'Fiddle Around', 3, 'opponent'),
    ('BW6.Gothita_55', 'Future Sight', 5, 'self'),
    ('BW3.Reuniclus_52', 'Future Sight', 5, 'self'),
    ('BW11.Reuniclus_76', 'Future Sight', 5, 'self'),
)


class PlayerChoiceEffectsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def context(self, path, actor, title=None):
        rig, _ = self.rig(path, 'pokemon' if title else 'trainer')
        card = definition(path)
        source = self.add(rig, card, actor, 'bench' if title else 'hand')
        ability = next(a for a in card.abilities if a.title == title) if title else None
        return rig, EffectContext(rig.session, actor, source, ability), ability.effect if ability else card.effect

    def replace_pile(self, rig, owner, zone, size):
        pile = rig.board.find_player_area(owner, zone)
        for card in list(pile.children):
            rig.to_area(card, owner, 'lostZone')
        return [self.add(rig, self.filler, owner, zone) for _ in range(size)]

    async def test_order_effects_private_chooser_and_wire_order_both_players(self):
        for path, title, count, mode in ORDER_CASES:
            for actor in (P1, P2):
                opponent = P2 if actor == P1 else P1
                owners = (actor, opponent) if mode == 'either' else (actor if mode == 'self' else opponent,)
                for owner in owners:
                    for size in (0, 1, 7):
                        with self.subTest(path=path, actor=actor, owner=owner, size=size):
                            rig, ctx, effect = self.context(path, actor, title)
                            before = self.replace_pile(rig, owner, 'deck', size)
                            other = P2 if owner == P1 else P1
                            other_before = list(ctx.deck(other))
                            top = ctx.deck_top(count, owner)
                            ordered = list(reversed(top))
                            ctx.choose = AsyncMock(return_value=0 if owner == actor else 1)
                            ctx.ask_yes_no = AsyncMock(return_value=True)
                            async def answer(viewer, source, offer, kind, valid, maximum, minimum, forced):
                                self.assertEqual(viewer, actor)
                                self.assertEqual(set(offer['revealEntities']), {c.entity_id for c in top})
                                self.assertTrue(offer['ordered'])
                                self.assertEqual((maximum, minimum, forced), (len(top), len(top), True))
                                return [c.entity_id for c in ordered]
                            with patch('spirit.game.session.game_session.AIPlayer', type('NotAI', (), {})), \
                                    patch.object(rig.session, '_run_pick_offer', side_effect=answer) as offer:
                                await effect(ctx)
                            self.assertEqual(offer.await_count, int(bool(top)))
                            self.assertEqual(ctx.deck_top(count, owner), ordered)
                            self.assertEqual(ctx.deck(other), other_before)
                            self.assertCountEqual(ctx.deck(owner), before)
                            messages = [msg for _, msg, _ in ctx._messages]
                            self.assertEqual([msg['name'] for msg in messages], ['PileReordered'] if top else [])
                            if top:
                                self.assertEqual(messages[0]['value']['entityID'], rig.board.find_player_area(owner, 'deck').entity_id)
                                self.assertEqual(messages[0]['value']['children'], [c.entity_id for c in ctx.deck(owner)])

    async def test_hiker_and_ice_axe_private_mandatory_choice_and_target(self):
        for path, count, either in (('SM7.Hiker_133', 5, True), ('HF.Hiker_185', 5, True),
                                    ('SM10.ChipChipIceAxe_165', 3, False)):
            for actor in (P1, P2):
                opponent = P2 if actor == P1 else P1
                for owner in ((actor, opponent) if either else (opponent,)):
                    for size in (1, 7):
                        with self.subTest(path=path, actor=actor, owner=owner, size=size):
                            rig, ctx, effect = self.context(path, actor)
                            before = self.replace_pile(rig, owner, 'deck', size)
                            other = P2 if owner == P1 else P1
                            other_before = list(ctx.deck(other))
                            viewed = ctx.deck_top(count, owner)
                            chosen = viewed[-1]
                            ctx.choose = AsyncMock(return_value=0 if owner == actor else 1)
                            async def answer(viewer, source, offer, kind, valid, maximum, minimum, forced):
                                self.assertEqual(viewer, actor)
                                self.assertEqual(set(offer['revealEntities']), {c.entity_id for c in viewed})
                                self.assertEqual((maximum, minimum, forced), (1, 1, True))
                                return [chosen.entity_id]
                            with patch('spirit.game.session.game_session.AIPlayer', type('NotAI', (), {})), \
                                    patch.object(rig.session, '_run_pick_offer', side_effect=answer) as offer:
                                await effect(ctx)
                            offer.assert_awaited_once()
                            self.assertIs(ctx.deck_top(1, owner)[0], chosen)
                            self.assertEqual(ctx.deck(other), other_before)
                            self.assertCountEqual(ctx.deck(owner), before)
                            self.assertTrue(all(msg['name'] != 'EntityIntroduced' for _, msg, _ in ctx._messages))

    def test_trainer_permissions_use_the_decks_named_in_the_text(self):
        for path, either in (('SM7.Hiker_133', True), ('HF.Hiker_185', True),
                             ('SM10.ChipChipIceAxe_165', False), ('XY2.TrickShovel_98', True)):
            for actor in (P1, P2):
                for own_size, opposing_size in ((0, 0), (0, 3), (3, 0), (3, 3)):
                    with self.subTest(path=path, actor=actor, sizes=(own_size, opposing_size)):
                        rig, ctx, _ = self.context(path, actor)
                        self.replace_pile(rig, actor, 'deck', own_size)
                        self.replace_pile(rig, ctx.opponent_id, 'deck', opposing_size)
                        expected = bool(own_size or opposing_size) if either else bool(opposing_size)
                        self.assertEqual(bool(definition(path).condition(rig.board, actor, ctx.source)), expected)

    async def test_chosen_hand_resets_only_selected_player(self):
        for path, title, bottom in (('XY5.Flygon_110', 'Sand Flap', False),
                                    ('SV2.Farigiraf_155', 'Either Face', False),
                                    ('SWSH11.Kingdra_37', 'Seething Currents', True)):
            for actor in (P1, P2):
                for owner in (P1, P2):
                    with self.subTest(path=path, actor=actor, owner=owner):
                        rig, ctx, effect = self.context(path, actor, title)
                        hand = self.replace_pile(rig, owner, 'hand', 3)
                        deck = self.replace_pile(rig, owner, 'deck', 7)
                        other = P2 if owner == P1 else P1
                        other_before = (list(ctx.hand(other)), list(ctx.deck(other)))
                        ctx.choose = AsyncMock(return_value=0 if owner == actor else 1)
                        ctx.ask_yes_no = AsyncMock(return_value=True)
                        await effect(ctx)
                        self.assertEqual(len(ctx.hand(owner)), 4)
                        self.assertEqual((ctx.hand(other), ctx.deck(other)), other_before)
                        self.assertCountEqual(ctx.hand(owner) + ctx.deck(owner), hand + deck)
                        if bottom:
                            self.assertCountEqual(ctx.hand(owner), deck[-4:])
                            self.assertCountEqual(ctx.deck(owner)[:3], hand)

    async def test_opponents_choice_assigns_pick_to_opponent_not_power_user(self):
        # Slowking's HGSS3 power reveals cards and gives the choice to the opponent.
        for actor in (P1, P2):
            rig, ctx, effect = self.context('HGSS3.Slowking_85', actor, "Opponent's Choice")
            top = ctx.deck_top(2)
            ctx.choose_cards = AsyncMock(return_value=[top[1]])
            await effect(ctx)
            self.assertEqual(ctx.choose_cards.await_args.kwargs['player_id'], ctx.opponent_id)
            self.assertIn(top[1], ctx.hand())
            self.assertIs(ctx.deck()[0], top[0])

    async def test_hiker_skips_empty_target_deck_and_does_not_leak_chosen_card(self):
        for actor in (P1, P2):
            for owner in (P1, P2):
                with self.subTest(actor=actor, owner=owner):
                    rig, ctx, effect = self.context('SM7.Hiker_133', actor)
                    other = P2 if owner == P1 else P1
                    self.replace_pile(rig, other, 'deck', 0)
                    viewed = self.replace_pile(rig, owner, 'deck', 2)
                    ctx.choose = AsyncMock()
                    ctx.choose_cards = AsyncMock(return_value=[viewed[0]])
                    await effect(ctx)
                    ctx.choose.assert_not_awaited()
                    self.assertIs(ctx.deck_top(1, owner)[0], viewed[0])
                    self.assertEqual(ctx.deck(other), [])
                    self.assertTrue(all(m['name'] != 'EntityIntroduced' for _, m, _ in ctx._messages))

    async def test_trick_shovel_only_shows_top_to_actor_and_discards_for_owner(self):
        for actor in (P1, P2):
            for owner in (P1, P2):
                for discard in (False, True):
                    with self.subTest(actor=actor, owner=owner, discard=discard):
                        rig, ctx, effect = self.context('XY2.TrickShovel_98', actor)
                        other = P2 if owner == P1 else P1
                        before = list(ctx.deck(owner))
                        untouched = list(ctx.deck(other))
                        top = ctx.deck_top(1, owner)[0]
                        ctx.choose = AsyncMock(return_value=0 if owner == actor else 1)
                        ctx.ask_yes_no = AsyncMock(return_value=discard)
                        await effect(ctx)
                        self.assertEqual(ctx.deck(other), untouched)
                        self.assertEqual(ctx.deck(owner), before[:-1] if discard else before)
                        if discard:
                            self.assertIn(top, ctx.discard_pile(owner))
                        else:
                            intros = [(viewer, m) for viewer, m, _ in ctx._messages if m['name'] == 'EntityIntroduced']
                            self.assertEqual([viewer for viewer, _ in intros], [actor])
                            self.assertEqual(intros[0][1]['value']['entityID'], top.entity_id)

    async def test_borne_ashore_uses_selected_cards_owner_and_available_bench(self):
        for path in ('SM2.Alomomola_36', 'SWSH10.Mantine_34'):
            for actor in (P1, P2):
                for owner in (P1, P2):
                    for expanded in (False, True):
                        with self.subTest(path=path, actor=actor, owner=owner, expanded=expanded):
                            rig, ctx, effect = self.context(path, actor, 'Borne Ashore')
                            other = P2 if owner == P1 else P1
                            for pid in (P1, P2):
                                self.replace_pile(rig, pid, 'discard', 0)
                            target = self.add(rig, self.filler, owner, 'discard')
                            invalid = self.add(rig, self.filler, other, 'discard')
                            if expanded:
                                stadium = self.add(rig, definition('XY6.SkyField_89'), actor, 'hand')
                                rig.board.move_card(stadium.entity_id, rig.board.find_global_area('activeStadium').entity_id)
                            self.replace_pile(rig, other, 'bench', 8 if expanded else 5)
                            self.replace_pile(rig, owner, 'bench', 5 if expanded else 2)
                            async def choose(cards, count, **kwargs):
                                self.assertIn(target, cards)
                                self.assertNotIn(invalid, cards)
                                self.assertEqual(kwargs.get('minimum', count), 1)
                                return [target]
                            ctx.choose_cards = AsyncMock(side_effect=choose)
                            await effect(ctx)
                            ctx.choose_cards.assert_awaited_once()
                            self.assertIs(target.parent, rig.board.find_player_area(owner, 'bench'))
                            self.assertIn(invalid, ctx.discard_pile(other))

    async def test_trick_moves_tool_only_between_chosen_owners_pokemon(self):
        for actor in (P1, P2):
            for owner in (P1, P2):
                with self.subTest(actor=actor, owner=owner):
                    rig, ctx, effect = self.context('XY5.MrMime_101', actor, 'Trick')
                    holder = rig.board.active_pokemon(owner)
                    target = next(p for p in rig.board.pokemon_in_play(owner) if p is not holder)
                    tool = self.add(rig, definition('SM3.WishfulBaton_128'), owner, 'hand')
                    rig.attach(tool, holder)
                    ctx.choose_cards = AsyncMock(return_value=[tool])
                    async def choose(candidates, prompt, **kwargs):
                        self.assertTrue(all(p.owning_player_id == owner for p in candidates))
                        self.assertNotIn(holder, candidates)
                        self.assertIn(target, candidates)
                        return target
                    ctx.choose_pokemon = AsyncMock(side_effect=choose)
                    await effect(ctx)
                    self.assertIs(tool.parent, target)
                    self.assertEqual(tool.owning_player_id, owner)

    async def test_shared_trainer_order_clause_honors_either_player(self):
        effect = standard_trainer_effect(
            "Look at the top 3 cards of either player's deck and put them back "
            "on top of that player's deck in any order.")
        for actor in (P1, P2):
            for owner in (P1, P2):
                with self.subTest(actor=actor, owner=owner):
                    _, ctx, _ = self.context('SM7.Hiker_133', actor)
                    ctx.choose = AsyncMock(return_value=0 if owner == actor else 1)
                    ctx.reorder_deck_top = AsyncMock()
                    await effect(ctx)
                    ctx.choose.assert_awaited_once()
                    ctx.reorder_deck_top.assert_awaited_once_with(3, player_id=owner)
