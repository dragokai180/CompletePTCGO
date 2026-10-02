"""Stadium bench-entry effects distinguish placement from the deck and hand."""
import unittest
from unittest.mock import AsyncMock

from spirit.game.attributes import AttrID
from spirit.game.models.board import create_card_entity
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2
from tests import test_hgss_rules as fixtures


class RiskyRuinsBenchingTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_stadium(self, path):
        rig, entities = self.rig('SV05.BuddyBuddyPoffin_144', kind='trainer')
        stadium_def = fixtures.definition(path)
        stadium = create_card_entity(
            fixtures.loader.cards_by_guid[stadium_def.guid.lower()], P1)
        rig.board.add_card_to_area(
            stadium, rig.board.find_global_area('activeStadium'))
        basic = self.add(rig, fixtures.definition('MEP.Sobble_54'), P1, 'deck')
        return rig, entities, basic

    async def play_poffin_for(self, rig, entities, *basics):
        definition = fixtures.definition('SV05.BuddyBuddyPoffin_144')
        ctx = EffectContext(rig.session, P1, entities['target'], None)

        async def search(predicate, **kwargs):
            self.assertTrue(all(predicate(basic) for basic in basics))
            return list(basics)

        ctx.search_deck = AsyncMock(side_effect=search)
        await definition.effect(ctx)
        return ctx

    async def test_risky_ruins_damages_basic_benched_by_buddy_buddy_poffin(self):
        rig, entities, basic = self.setup_stadium('ME1.RiskyRuins_127')
        second = self.add(rig, fixtures.definition('MEP.Sobble_54'), P1, 'deck')
        hp = {card.entity_id: card.get_attribute(AttrID.HP)
              for card in (basic, second)}

        await self.play_poffin_for(rig, entities, basic, second)

        for card in (basic, second):
            self.assertIn(card, rig.board.find_player_area(P1, 'bench').children)
            self.assertEqual(card.get_attribute(AttrID.HP), hp[card.entity_id] - 20)

    async def test_risky_ruins_also_observes_effect_entry_from_discard(self):
        rig, entities, basic = self.setup_stadium('ME1.RiskyRuins_127')
        rig.to_area(basic, P1, 'discard')
        hp = basic.get_attribute(AttrID.HP)
        ctx = EffectContext(rig.session, P1, entities['target'], None)

        self.assertTrue(await ctx.bench_pokemon(basic))

        self.assertEqual(basic.get_attribute(AttrID.HP), hp - 20)

    async def test_risky_ruins_requires_basic_non_darkness_on_owners_turn(self):
        for path, active_player in (
            ('SWSH3.EternatusV_116', P1),
            ('SWSH1.Drizzile_56', P1),
            ('MEP.Sobble_54', P2),
        ):
            with self.subTest(path=path, active_player=active_player):
                rig, entities, _ = self.setup_stadium('ME1.RiskyRuins_127')
                card = self.add(rig, fixtures.definition(path), P1, 'discard')
                hp = card.get_attribute(AttrID.HP)
                rig.session.turn_state.active_player_id = active_player
                ctx = EffectContext(rig.session, P1, entities['target'], None)

                self.assertTrue(await ctx.bench_pokemon(card))

                self.assertEqual(card.get_attribute(AttrID.HP), hp)

    async def test_gapejaw_bog_ignores_basic_benched_from_deck(self):
        rig, entities, basic = self.setup_stadium('SWSH10.GapejawBog_142')
        hp = basic.get_attribute(AttrID.HP)

        await self.play_poffin_for(rig, entities, basic)

        self.assertEqual(basic.get_attribute(AttrID.HP), hp)

    async def test_gapejaw_bog_still_damages_manual_bench_play(self):
        rig, _, basic = self.setup_stadium('SWSH10.GapejawBog_142')
        rig.to_area(basic, P1, 'hand')
        hp = basic.get_attribute(AttrID.HP)

        await rig.session._execute_play_basic(P1, basic)

        self.assertEqual(basic.get_attribute(AttrID.HP), hp - 20)


if __name__ == '__main__':
    unittest.main()
