"""Deck searches naming several card categories resolve every category."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1


class CompoundDeckSearchTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_volkner_finds_both_item_and_lightning_energy(self):
        rig, entities = self.rig('SM5.Volkner_135', 'trainer')
        item = self.add(rig, fixtures.definition('SV1.NestBall_181'), P1, 'deck')
        energy = self.add(
            rig, def_for(self.energies[PokemonTypes.LIGHTNING.value]), P1, 'deck')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        rig.session.prompt_card_chooser_groups = AsyncMock(
            return_value=[[item.entity_id], [energy.entity_id]])

        await fixtures.definition('SM5.Volkner_135').effect(ctx)

        specs = rig.session.prompt_card_chooser_groups.await_args.args[2]
        self.assertIn(item, specs[0]['cards'])
        self.assertNotIn(energy, specs[0]['cards'])
        self.assertIn(energy, specs[1]['cards'])
        self.assertNotIn(item, specs[1]['cards'])
        self.assertIn(item, ctx.hand())
        self.assertIn(energy, ctx.hand())

    async def test_other_compound_trainer_searches_find_each_printed_category(self):
        cases = (
            ('XY6.Steven_90', (
                'SM5.Volkner_135', PokemonTypes.GRASS)),
            ('XY3.Korrina_95', (
                'BW1.Timburr_58', 'SV1.NestBall_181')),
            ('TATM.TeamMagmasGreatBall_31', (
                'TATM.TeamMagmasNumel_1', PokemonTypes.FIGHTING)),
            ('TATM.TeamAquasGreatBall_27', (
                'TATM.TeamAquasCarvanha_20', PokemonTypes.WATER)),
            ('SV085.LarrysSkill_115', (
                'BW1.Snivy_1', 'SM5.Volkner_135', PokemonTypes.GRASS)),
        )
        for path, requests in cases:
            with self.subTest(card=path):
                rig, entities = self.rig(path, 'trainer')
                selected = [self.add(
                    rig,
                    def_for(self.energies[request.value])
                    if isinstance(request, PokemonTypes)
                    else fixtures.definition(request),
                    P1, 'deck',
                ) for request in requests]
                ctx = EffectContext(rig.session, P1, entities['target'], None)
                rig.session.prompt_card_chooser_groups = AsyncMock(
                    return_value=[[card.entity_id] for card in selected])

                await fixtures.definition(path).effect(ctx)

                specs = rig.session.prompt_card_chooser_groups.await_args.args[2]
                self.assertEqual(len(specs), len(selected))
                for index, card in enumerate(selected):
                    self.assertIn(card, specs[index]['cards'])
                    self.assertIn(card, ctx.hand())

    async def test_colress_tenacity_keeps_one_found_category(self):
        rig, entities = self.rig('SV065.ColresssTenacity_57', 'trainer')
        stadium = self.add(
            rig, fixtures.definition('SV1.Mesagoza_178'), P1, 'deck')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        ctx.search_deck_groups = AsyncMock(return_value=[[stadium], []])
        ctx.shuffle_deck = AsyncMock()

        await fixtures.definition('SV065.ColresssTenacity_57').effect(ctx)

        self.assertIn(stadium, ctx.hand())
        ctx.shuffle_deck.assert_awaited_once()

    async def test_shared_attack_and_ability_searches_keep_separate_slots(self):
        cases = (
            ('Promo_SWSH.Oricorio_210', 'Mixed Call',
             ('BW1.Snivy_1', 'SM5.Volkner_135')),
            ('SM6.Scatterbug_5', 'Abnormal Outbreak',
             ('SM6.Spewpa_7', 'SM6.Vivillon_8')),
            ('SM1.Dratini_94', 'Signs of Evolution',
             ('SM1.Dratini_94', 'SM1.Dragonair_95', 'SM1.Dragonite_96')),
        )
        for path, title, requested in cases:
            with self.subTest(card=path):
                rig, _, ctx = self.ctx(path, title)
                selected = [self.add(
                    rig, fixtures.definition(request), P1, 'deck')
                    for request in requested]
                rig.session.prompt_card_chooser_groups = AsyncMock(
                    return_value=[[card.entity_id] for card in selected])

                await ctx.ability.effect(ctx)

                specs = rig.session.prompt_card_chooser_groups.await_args.args[2]
                self.assertEqual(len(specs), len(selected))
                for index, card in enumerate(selected):
                    self.assertIn(card, specs[index]['cards'])
                    self.assertIn(card, ctx.hand())


if __name__ == '__main__':
    unittest.main()
