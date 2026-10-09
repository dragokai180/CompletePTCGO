"""Opponent-deck mill follows the Supporter condition printed on the attack."""
import unittest

from tests import test_hgss_rules as fixtures

from spirit.game.attributes import TrainerType
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class SupporterGatedMillTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig

    async def assert_mill(self, pokemon_path, attack_title, supporter_path, expected,
                          trainer_type=TrainerType.SUPPORTER.value):
        rig, entities = self.rig(pokemon_path)
        attack = next(ability for ability in fixtures.definition(pokemon_path).abilities
                      if ability.title == attack_title)
        if supporter_path:
            supporter = fixtures.definition(supporter_path)
            rig.session.turn_state.trainers_played.append(
                (supporter.guid, supporter.display_name, trainer_type))
        ctx = EffectContext(rig.session, P1, entities['target'], attack)
        deck = ctx.deck(P2)
        original_top = ctx.deck_top(expected, P2)
        before = len(deck)
        discard_before = {card.entity_id for card in ctx.discard_pile(P2)}
        await attack.effect(ctx)
        self.assertEqual(before - len(ctx.deck(P2)), expected)
        self.assertEqual(
            {card.entity_id for card in ctx.discard_pile(P2)} - discard_before,
            {card.entity_id for card in original_top},
        )

    async def test_land_collapse_requires_ancient_supporter(self):
        for supporter, expected, kind in (
            (None, 1, TrainerType.SUPPORTER.value),
            ('SV05.Salvatore_160', 1, TrainerType.SUPPORTER.value),
            ('SV05.ExplorersGuidance_147', 4, TrainerType.SUPPORTER.value),
            ('SV4.ProfessorSadasVitality_170', 4, TrainerType.SUPPORTER.value),
            ('SV05.ExplorersGuidance_147', 1, TrainerType.ITEM.value),
        ):
            with self.subTest(supporter=supporter, kind=kind):
                await self.assert_mill('SV05.GreatTusk_97', 'Land Collapse',
                                       supporter, expected, kind)

    async def test_dirty_work_replaces_base_mill_after_giovanni(self):
        for supporter, expected in (
            (None, 1), ('SV05.ExplorersGuidance_147', 1),
            ('SM10.GiovannisExile_174', 5),
        ):
            with self.subTest(supporter=supporter):
                await self.assert_mill('SM10.Rhydon_94', 'Dirty Work',
                                       supporter, expected)

    async def test_twister_spewing_mills_only_after_tarragon(self):
        for supporter, expected in (
            (None, 0), ('SV05.ExplorersGuidance_147', 0),
            ('ME3.Tarragon_85', 3),
        ):
            with self.subTest(supporter=supporter):
                await self.assert_mill('ME3.Hippowdon_40', 'Twister Spewing',
                                       supporter, expected)


if __name__ == '__main__':
    unittest.main()
