"""Regression coverage for manually activated Powers and printed GX damage."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.card_effects.bw_era import bw_legacy_attack
from spirit.game.data_utils import Activations, Triggers
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.game.session.passives import compute_damage
from spirit.tools.effect_smoke import P1, P2


class IncompleteVstarGxEffectsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_manually_used_powers_are_offered_and_vstar_limit_applies(self):
        paths = (
            'SWSH10.DarkraiVSTAR_99', 'CZ.DarkraiVSTAR_210',
            'CZ.LeafeonVSTAR_14', 'CZ.RegigigasVSTAR_114',
            'SWSH10.HisuianDecidueyeVSTAR_84',
            'SWSH10.HisuianDecidueyeVSTAR_195',
            'SWSH10.HisuianLilligantVSTAR_18',
            'SWSH10.HisuianLilligantVSTAR_190',
            'SWSH12.MawileVSTAR_71', 'SWSH12.MawileVSTAR_200',
            'SWSH7.LeafeonV_7', 'SWSH7.LeafeonV_166',
            'SWSH7.LeafeonV_167',
        )
        for path in paths:
            with self.subTest(card=path):
                rig, entities = self.rig(path)
                ability = fixtures.definition(path).abilities[0]
                self.assertEqual(ability.activation, Activations.ONCE_PER_TURN)
                source = entities['target']
                if ability.title == 'Star Rondo':
                    source = next(p for p in rig.board.pokemon_in_play(P1)
                                  if p is not source and
                                  p.archetype_id == source.archetype_id)
                if ability.title == 'Star Guardian':
                    prizes = rig.board.find_player_area(P2, 'prizePile')
                    for card in list(prizes.children)[:-1]:
                        rig.to_area(card, P2, 'discard')
                if ability.title == 'Star of Fortune':
                    hand = rig.board.find_player_area(P1, 'hand')
                    for card in list(hand.children)[5:]:
                        rig.to_area(card, P1, 'discard')

                def offered():
                    return any(
                        entry['entityID'] == source.entity_id and
                        entry['selectableAction']['actionID'] == ability.ability_id
                        for entry in compute_legal_actions(
                            rig.board, rig.session.turn_state, P1,
                            rig.session.game_id)
                    )

                self.assertTrue(offered())
                if ability.vstar:
                    rig.session.turn_state.vstar_used.add(P1)
                    self.assertFalse(offered())

    async def test_star_abyss_moves_two_items_from_discard_to_hand(self):
        rig, entities = self.rig('SWSH10.DarkraiVSTAR_99')
        items = [self.add(rig, fixtures.definition('CZ.RareCandy_141'),
                          P1, 'discard') for _ in range(2)]
        ability = fixtures.definition('SWSH10.DarkraiVSTAR_99').abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        ctx.choose_cards = AsyncMock(return_value=items)

        await ability.effect(ctx)

        hand = rig.board.find_player_area(P1, 'hand').children
        self.assertTrue(all(item in hand for item in items))

    async def test_star_of_fortune_draws_without_a_second_confirmation(self):
        rig, entities = self.rig('SWSH10.HisuianDecidueyeVSTAR_84')
        ability = fixtures.definition(
            'SWSH10.HisuianDecidueyeVSTAR_84').abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        ctx.ask_yes_no = AsyncMock(side_effect=AssertionError('extra prompt'))
        ctx.draw_until = AsyncMock()

        await ability.effect(ctx)

        ctx.draw_until.assert_awaited_once_with(8)

    async def test_timeless_gx_deals_printed_damage_before_extra_turn(self):
        for path in ('SM5.DialgaGX_100', 'SM6.DialgaGX_82',
                     'SM6.DialgaGX_125', 'SM6.DialgaGX_138'):
            with self.subTest(card=path):
                rig, entities = self.rig(path)
                attack = next(a for a in fixtures.definition(path).abilities
                              if a.title == 'Timeless-GX')
                ctx = EffectContext(rig.session, P1, entities['target'], attack)
                defender = ctx.defender
                defender.set_attribute(AttrID.HP, 500)
                expected = compute_damage(
                    rig.board, ctx.attacker, defender, 150).amount
                self.assertGreater(expected, 0)

                await attack.effect(ctx)

                self.assertEqual(defender.get_attribute(AttrID.HP),
                                 500 - expected)
                self.assertTrue(rig.session.extra_turn_pending)

    async def test_generic_extra_turn_attack_keeps_printed_damage(self):
        rig, entities = self.rig('SM6.DialgaGX_82')
        attack = fixtures.definition('SM6.DialgaGX_82').abilities[2]
        ctx = EffectContext(rig.session, P1, entities['target'], attack)
        ctx.defender.set_attribute(AttrID.HP, 500)

        await bw_legacy_attack(ctx)

        self.assertLess(ctx.defender.get_attribute(AttrID.HP), 500)
        self.assertTrue(rig.session.extra_turn_pending)

    async def test_exploding_needles_has_knockout_trigger_and_places_counters(self):
        rig, entities = self.rig('SV09.Maractus_8')
        ability = fixtures.definition('SV09.Maractus_8').abilities[0]
        self.assertEqual(ability.trigger, Triggers.ON_KNOCKED_OUT)
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        ctx.ko_from_attack = True
        ctx.was_active_at_ko = True
        ctx.ko_attacker = rig.board.active_pokemon(P2)
        ctx.deal_damage = AsyncMock()

        await ability.effect(ctx)

        ctx.deal_damage.assert_awaited_once_with(
            60, target=ctx.ko_attacker, apply_modifiers=False,
            as_counters=True)


if __name__ == '__main__':
    unittest.main()
