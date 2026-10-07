"""Returning a public Pokemon must not expose the owner's private hand."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext, full_stack
from spirit.tools.effect_smoke import P1, P2


class ReturnToHandVisibilityTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    @staticmethod
    def events(ctx, viewer):
        return [msg for _, messages in ctx.bracket_runs_for(viewer)
                for msg in messages]

    async def test_scoop_up_cyclone_hides_returned_stack_and_clears_damage(self):
        rig, entries = self.rig('SV06.ScoopUpCyclone_162', 'trainer')
        target = rig.board.find_player_area(P1, 'bench').children[0]
        stack = full_stack(target)
        printed_hp = target.attribute_originals[AttrID.HP.value]
        target.set_attribute(AttrID.HP, printed_hp - 40)
        target.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned'])
        ctx = EffectContext(rig.session, P1, entries['target'], None)
        ctx.choose_pokemon = AsyncMock(return_value=target)

        await fixtures.definition('SV06.ScoopUpCyclone_162').effect(ctx)

        owner = self.events(ctx, P1)
        opponent = self.events(ctx, P2)
        for card in stack:
            self.assertIn(card, rig.board.find_player_area(P1, 'hand').children)
            self.assertIsNone(card.serialize(P2)['attributes'])
            self.assertNotIn(card.entity_id, [m['value']['entityID'] for m in opponent
                                     if m['name'].endswith('EntityIntroduced')])
            moves = [i for i, m in enumerate(opponent)
                     if m['name'].endswith('EntityMoved')
                     and m['value']['entityID'] == card.entity_id]
            resets = [i for i, m in enumerate(opponent)
                      if m['name'].endswith('AttributesReset')
                      and m['value']['entityID'] == card.entity_id]
            self.assertEqual(len(moves), 1)
            self.assertEqual(len(resets), 1)
            self.assertLess(moves[0], resets[0])

        self.assertEqual(target.get_attribute(AttrID.HP), printed_hp)
        self.assertEqual(target.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        move_at = next(i for i, m in enumerate(owner)
                       if m['name'].endswith('EntityMoved')
                       and m['value']['entityID'] == target.entity_id)
        hp_at = next(i for i, m in enumerate(owner)
                     if m['name'].endswith('AttributeModified')
                     and m['value']['entityID'] == target.entity_id
                     and m['value']['attribute']['name'] == AttrID.HP.value)
        self.assertLess(move_at, hp_at)
        self.assertEqual(owner[hp_at]['value']['attribute']['value'], printed_hp)
        self.assertTrue(any(m['name'].endswith('AttributeModified')
                            and m['value']['entityID'] == target.entity_id
                            and m['value']['attribute']['name'] == AttrID.SPECIAL_CONDITIONS.value
                            and m['value']['attribute']['value'] == []
                            for m in owner))

    async def test_explicit_reveal_happens_before_returned_card_is_hidden(self):
        rig, entries = self.rig('SV06.ScoopUpCyclone_162', 'trainer')
        target = rig.board.find_player_area(P1, 'bench').children[0]
        printed_hp = target.attribute_originals[AttrID.HP.value]
        target.set_attribute(AttrID.HP, printed_hp - 30)
        ctx = EffectContext(rig.session, P1, entries['target'], None)

        await ctx.put_in_hand([target], reveal=True)

        opponent = self.events(ctx, P2)
        def position(suffix):
            return next(i for i, m in enumerate(opponent)
                        if m['name'].endswith(suffix)
                        and m['value']['entityID'] == target.entity_id)

        self.assertLess(position('EntityIntroduced'), position('EntityMoved'))
        self.assertLess(position('EntityMoved'), position('AttributesReset'))
        owner = self.events(ctx, P1)
        self.assertTrue(any(m['name'].endswith('AttributeModified')
                            and m['value']['entityID'] == target.entity_id
                            and m['value']['attribute']['name'] == AttrID.HP.value
                            and m['value']['attribute']['value'] == printed_hp
                            for m in owner))

    async def test_opponents_pokemon_returns_to_its_owners_hand(self):
        rig, entries = self.rig('SV06.ScoopUpCyclone_162', 'trainer')
        target = rig.board.find_player_area(P2, 'bench').children[0]
        ctx = EffectContext(rig.session, P1, entries['target'], None)

        await ctx.put_in_hand([target], reveal=False)

        self.assertIn(target, rig.board.find_player_area(P2, 'hand').children)
        self.assertTrue(any(m['name'].endswith('AttributesReset')
                            and m['value']['entityID'] == target.entity_id
                            for m in self.events(ctx, P1)))
        self.assertFalse(any(m['name'].endswith('AttributesReset')
                             and m['value']['entityID'] == target.entity_id
                             for m in self.events(ctx, P2)))

    async def test_devolution_hides_returned_evolution_from_opponent(self):
        rig, _ = self.rig('BW1.Snivy_1')
        basic = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
        evolution = self.add(rig, fixtures.definition('BW1.Servine_3'), P1, 'hand')
        await rig.session.perform_evolution(P1, evolution, basic)
        rig.session.send_game_sequence = AsyncMock()

        await rig.session.perform_devolution(evolution)

        reset_calls = [call for call in rig.session.send_game_sequence.await_args_list
                       if any(m['name'].endswith('AttributesReset')
                              for m in call.args[2])]
        self.assertEqual(len(reset_calls), 1)
        self.assertEqual(reset_calls[0].args[0], [rig.session.players[P2]])
        self.assertEqual(reset_calls[0].args[2][0]['value']['entityID'],
                         evolution.entity_id)
        self.assertIn(evolution, rig.board.find_player_area(P1, 'hand').children)


if __name__ == '__main__':
    unittest.main()
