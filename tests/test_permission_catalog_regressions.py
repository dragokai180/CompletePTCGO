"""Cross-expansion public prerequisites and alternative Trainer effects."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonStage
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1, P2


class PermissionCatalogRegressions(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_card(self, path, others=0):
        rig, _ = self.rig('BW1.Snivy_1')
        for c in list(rig.board.find_player_area(P1, 'hand').children):
            rig.to_area(c, P1, 'deck')
        source = self.add(rig, definition(path), P1, 'hand')
        for _ in range(others):
            self.add(rig, definition('BW1.Snivy_1'), P1, 'hand')
        return rig, source

    def allowed(self, rig, source):
        from spirit.game.data_utils import def_for
        return trainer_condition_met(def_for(source.archetype_id).condition, rig.board, P1, source)

    def empty_deck(self, rig):
        for c in list(rig.board.find_player_area(P1, 'deck').children):
            rig.to_area(c, P1, 'discard')

    async def test_lillie_first_turn_limit_and_resolution(self):
        rig, source = self.setup_card('SM1.Lillie_122', 7)
        rig.board.turn_state = rig.session.turn_state
        rig.session.turn_state.turn_number = 2
        self.assertTrue(self.allowed(rig, source))
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.draw_until = AsyncMock()
        await definition('SM1.Lillie_122').effect(ctx)
        ctx.draw_until.assert_awaited_once_with(8)
        rig.session.turn_state.turn_number = 3
        self.assertFalse(self.allowed(rig, source))
        self.empty_deck(rig)
        rig.session.turn_state.turn_number = 2
        self.assertFalse(self.allowed(rig, source))

    async def test_hau_requires_deck(self):
        rig, source = self.setup_card('SM1.Hau_120')
        self.assertTrue(self.allowed(rig, source))
        self.empty_deck(rig)
        self.assertFalse(self.allowed(rig, source))

    async def test_public_up_to_recovery_requires_matching_card(self):
        from spirit.game.card_effects.standard_era import standard_trainer_condition
        rig, source = self.setup_card('SM1.Hau_120')
        for c in list(rig.board.find_player_area(P1, 'discard').children):
            rig.to_area(c, P1, 'deck')
        check = standard_trainer_condition('Put up to 3 Pokémon from your discard pile into your hand.')
        self.assertFalse(check(rig.board, P1, source))
        self.add(rig, definition('SM1.Hau_120'), P1, 'discard')
        self.assertFalse(check(rig.board, P1, source))
        self.add(rig, definition('BW1.Snivy_1'), P1, 'discard')
        self.assertTrue(check(rig.board, P1, source))

    async def test_declared_permissions_across_catalog_do_not_raise(self):
        from spirit.game.data_utils import CARD_DEFS_BY_GUID
        from spirit.game.models.board import create_card_entity
        from spirit.game.scripts.cards import loader
        rig, _ = self.rig('BW1.Snivy_1')
        rig.board.turn_state = rig.session.turn_state
        checked = 0
        for d in list(CARD_DEFS_BY_GUID.values()):
            # Other unit tests register synthetic definitions without a
            # catalog model; they are not shipped cards in this inventory.
            if d.guid.lower() not in loader.cards_by_guid:
                continue
            source = create_card_entity(loader.cards_by_guid[d.guid.lower()], P1)
            checks = [getattr(d, 'condition', None), getattr(d, 'attach_condition', None),
                      getattr(getattr(d, 'ability', None), 'condition', None)]
            checks += [getattr(a, 'condition', None) for a in getattr(d, 'abilities', [])]
            for check in checks:
                if check is not None:
                    with self.subTest(card=d.display_name, key=d.key):
                        trainer_condition_met(check, rig.board, P1, source)
                    checked += 1
        self.assertGreater(checked, 2000)

    async def test_other_draw_supporters_all_prints_require_deck(self):
        from spirit.game.data_utils import CARD_DEFS_BY_GUID
        names = {'Doctor', 'Dancer', 'Schoolboy', 'Schoolgirl', 'Bug Catcher'}
        for d in list(CARD_DEFS_BY_GUID.values()):
            if d.display_name not in names:
                continue
            with self.subTest(card=d.display_name, key=d.key, number=d.collector_number):
                rig, _ = self.rig('BW1.Snivy_1')
                source = self.add(rig, d, P1, 'hand')
                self.assertTrue(self.allowed(rig, source))
                self.empty_deck(rig)
                self.assertFalse(self.allowed(rig, source))

    async def test_caitlin_cannot_count_itself_but_can_replenish_empty_deck(self):
        for path in ('BW10.Caitlin_78', 'SWSH6.Caitlin_132'):
            rig, source = self.setup_card(path)
            self.assertFalse(self.allowed(rig, source))
            self.empty_deck(rig)
            self.add(rig, definition('BW1.Snivy_1'), P1, 'hand')
            self.assertTrue(self.allowed(rig, source))

    async def test_gwynn_requires_non_rule_box_pokemon_and_deck(self):
        rig, source = self.setup_card('ME5.Gwynn_78')
        self.assertFalse(self.allowed(rig, source))
        from spirit.game.data_utils import CARD_DEFS_BY_GUID, has_rule_box
        rule_box = next(d for d in CARD_DEFS_BY_GUID.values() if has_rule_box(d.guid)
                        and type(d).__name__ == 'PokemonCardDef')
        self.add(rig, rule_box, P1, 'hand')
        self.assertFalse(self.allowed(rig, source))
        self.add(rig, definition('BW1.Snivy_1'), P1, 'hand')
        self.assertTrue(self.allowed(rig, source))
        self.empty_deck(rig)
        self.assertFalse(self.allowed(rig, source))

    async def test_draw_powers_require_deck_but_shuffle_powers_can_replenish_it(self):
        from spirit.game.card_effects.standard_era import standard_ability_condition
        texts = [
            'Once during your turn (before your attack), you may discard a card from your hand. If you do, draw 2 cards.',
            'Once during your turn (before your attack), you may discard a card from your hand. If you do, draw 3 cards.',
            'Once during your turn, you may draw 3 cards.',
        ]
        rig, _ = self.rig('BW1.Snivy_1')
        active = rig.board.active_pokemon(P1)
        self.add(rig, definition('BW1.Snivy_1'), P1, 'hand')
        for text in texts:
            self.assertTrue(standard_ability_condition(text)(rig.board, P1, active))
        self.empty_deck(rig)
        for text in texts:
            self.assertFalse(standard_ability_condition(text)(rig.board, P1, active))
        shuffle = standard_ability_condition(
            'Once during your turn, you may shuffle your hand into your deck and draw 4 cards.')
        self.assertTrue(shuffle(rig.board, P1, active))

    async def test_electrocharger_needs_electropower_not_any_discard(self):
        rig, source = self.setup_card('SM9.Electrocharger_139')
        for c in list(rig.board.find_player_area(P1, 'discard').children):
            rig.to_area(c, P1, 'deck')
        self.add(rig, definition('BW1.Snivy_1'), P1, 'discard')
        self.assertFalse(self.allowed(rig, source))
        from spirit.game.data_utils import CARD_DEFS_BY_GUID
        target = next(d for d in CARD_DEFS_BY_GUID.values() if d.display_name == 'Electropower')
        self.add(rig, target, P1, 'discard')
        self.assertTrue(self.allowed(rig, source))

    async def test_sightseer_can_reduce_large_hand_but_needs_deck(self):
        rig, source = self.setup_card('SM8.Sightseer_189', 8)
        self.assertTrue(self.allowed(rig, source))
        self.empty_deck(rig)
        self.assertFalse(self.allowed(rig, source))

    async def test_private_search_can_fail_without_matching_card(self):
        rig, source = self.setup_card('SM9.Dana_137')
        rig.board.active_pokemon(P2).set_attribute(AttrID.STAGE, PokemonStage.STAGE2.value)
        self.assertTrue(self.allowed(rig, source))
        from spirit.game.card_effects.standard_era import standard_trainer_condition
        private = standard_trainer_condition('Search your deck for a Fairy Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.')
        self.assertTrue(private(rig.board, P1, source))

    async def test_erika_counts_other_hand_cards(self):
        rig, source = self.setup_card('SM9.ErikasHospitality_140', 4)
        self.assertTrue(self.allowed(rig, source))
        self.add(rig, definition('BW1.Snivy_1'), P1, 'hand')
        self.assertFalse(self.allowed(rig, source))

    async def test_dana_and_evelyn_stage_and_private_search(self):
        for path, stage in [('SM9.Dana_137', PokemonStage.STAGE2),
                            ('SM9.Evelyn_141', PokemonStage.STAGE1)]:
            rig, source = self.setup_card(path)
            active = rig.board.active_pokemon(P2)
            active.set_attribute(AttrID.STAGE, PokemonStage.BASIC.value)
            self.assertFalse(self.allowed(rig, source))
            active.set_attribute(AttrID.STAGE, stage.value)
            self.assertTrue(self.allowed(rig, source))
            self.empty_deck(rig)
            self.assertFalse(self.allowed(rig, source))

    async def test_judge_whistle_alternatives(self):
        rig, source = self.setup_card('SM9.JudgeWhistle_146')
        for c in list(rig.board.find_player_area(P1, 'discard').children):
            rig.to_area(c, P1, 'deck')
        self.assertTrue(self.allowed(rig, source))
        self.empty_deck(rig)
        self.assertFalse(self.allowed(rig, source))
        from spirit.game.data_utils import CARD_DEFS_BY_GUID
        judge = next(d for d in CARD_DEFS_BY_GUID.values() if d.display_name == 'Judge')
        self.add(rig, judge, P1, 'discard')
        self.assertTrue(self.allowed(rig, source))

    async def test_judge_whistle_resolves_only_available_branch(self):
        rig, source = self.setup_card('SM9.JudgeWhistle_146')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.draw_cards = AsyncMock()
        ctx.choose = AsyncMock()
        ctx.put_in_hand = AsyncMock()
        await definition('SM9.JudgeWhistle_146').effect(ctx)
        ctx.draw_cards.assert_awaited_once_with(1)
        ctx.choose.assert_not_awaited()
        self.empty_deck(rig)
        from spirit.game.data_utils import CARD_DEFS_BY_GUID
        judge = next(d for d in CARD_DEFS_BY_GUID.values() if d.display_name == 'Judge')
        target = self.add(rig, judge, P1, 'discard')
        ctx.choose_cards = AsyncMock(return_value=[target])
        await definition('SM9.JudgeWhistle_146').effect(ctx)
        ctx.put_in_hand.assert_awaited_once_with([target], reveal=True)
        ctx.draw_cards.assert_awaited_once_with(1)

    async def test_custom_catcher_needs_at_least_one_usable_mode(self):
        from spirit.game.data_utils import CARD_DEFS_BY_GUID
        prints = [d for d in CARD_DEFS_BY_GUID.values() if d.display_name == 'Custom Catcher']
        self.assertGreaterEqual(len(prints), 2)
        rig, source = self.setup_card('SM8.CustomCatcher_171', 3)
        self.assertFalse(self.allowed(rig, source))
        different = next(d for d in prints if d.guid.lower() != source.archetype_id.lower())
        second = self.add(rig, different, P1, 'hand')
        self.assertTrue(self.allowed(rig, source))
        rig.to_area(source, P1, 'discard')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.ask_yes_no = AsyncMock(return_value=False)
        ctx.discard_cards = AsyncMock()
        ctx.switch_active = AsyncMock()
        ctx.choose_pokemon = AsyncMock(return_value=rig.board.find_player_area(P2, 'bench').children[0])
        await definition('SM8.CustomCatcher_171').effect(ctx)
        ctx.discard_cards.assert_awaited_once_with([second])
        ctx.ask_yes_no.assert_not_awaited()
        for p in list(rig.board.find_player_area(P2, 'bench').children):
            rig.to_area(p, P2, 'discard')
        self.assertFalse(self.allowed(rig, source))


if __name__ == '__main__':
    unittest.main()
