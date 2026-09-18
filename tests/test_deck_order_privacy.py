"""The effect's user, not the deck owner, privately inspects and orders cards."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class DeckOrderPrivacyTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def check_second_sight(self, path, actor, owner, size):
        rig, _ = self.rig(path)
        card = definition(path)
        source = self.add(rig, card, actor, 'bench')
        ability = next(a for a in card.abilities if a.title == 'Second Sight')
        ctx = EffectContext(rig.session, actor, source, ability)
        ctx.choose = AsyncMock(return_value=0 if owner == actor else 1)
        deck = rig.board.find_player_area(owner, 'deck')
        for candidate in list(deck.children):
            rig.to_area(candidate, owner, 'discard')
        for _ in range(size):
            self.add(rig, self.filler, owner, 'deck')
        other = rig.board.find_player_area(P2 if owner == P1 else P1, 'deck')
        other_before = list(other.children)
        before = list(deck.children)
        top = ctx.deck_top(3, owner)
        ordered = list(reversed(top))

        async def answer(viewer, source_id, offer, kind, valid, count, minimum, forced):
            self.assertEqual(viewer, actor)
            self.assertEqual(source_id, source.entity_id)
            self.assertEqual(set(offer['revealEntities']), {c.entity_id for c in top})
            self.assertEqual(valid, [c.entity_id for c in top])
            self.assertTrue(offer['ordered'])
            self.assertEqual(count, len(top))
            self.assertEqual(minimum, len(top))
            self.assertTrue(forced)
            # The chooser is the only recipient of these inline card faces;
            # no EntityIntroduced messages may leak them to the deck's owner.
            self.assertEqual(ctx._messages, [])
            return [c.entity_id for c in ordered]

        with patch('spirit.game.session.game_session.AIPlayer', type('NotAI', (), {})), \
                patch.object(rig.session, '_run_pick_offer', side_effect=answer) as offer:
            await ability.effect(ctx)

        if top:
            offer.assert_awaited_once()
            self.assertEqual(ctx.deck_top(3, owner), ordered)
            self.assertEqual(deck.children[:-len(top)], before[:-len(top)])
            self.assertEqual([msg['name'] for _, msg, _ in ctx._messages], ['PileReordered'])
            payload = ctx._messages[0][1]['value']
            self.assertEqual(set(payload), {'gameID', 'entityID', 'children'})
            self.assertEqual(payload['entityID'], deck.entity_id)
        else:
            offer.assert_not_awaited()
            self.assertEqual(ctx._messages, [])
        self.assertEqual(other.children, other_before)
        self.assertCountEqual(deck.children, before)
        self.assertTrue(all(c.parent is deck for c in before))

    async def test_second_sight_private_viewer_and_order_on_either_side(self):
        for path in ('HGSS1.Slowking_12', 'COL.Slowking_32'):
            for actor in (P1, P2):
                for owner in (P1, P2):
                    with self.subTest(path=path, actor=actor, owner=owner):
                        await self.check_second_sight(path, actor, owner, 5)

    async def test_single_remaining_card_is_still_shown_to_activator(self):
        for owner in (P1, P2):
            with self.subTest(owner=owner):
                await self.check_second_sight('HGSS1.Slowking_12', P1, owner, 1)

    async def test_empty_deck_has_no_offer(self):
        await self.check_second_sight('HGSS1.Slowking_12', P1, P2, 0)
