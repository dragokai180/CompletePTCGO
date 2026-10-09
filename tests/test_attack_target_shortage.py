"""Multi-target effects remain playable with fewer Pokémon than printed targets."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures

from spirit.game.attributes import AttrID, TrainerType
from spirit.tools.effect_smoke import P1, P2


class AttackTargetShortageTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def set_bench(self, rig, pid, count):
        bench = rig.board.find_player_area(pid, 'bench')
        for pokemon in list(bench.children):
            rig.to_area(pokemon, pid, 'deck')
        result = [self.add(rig, self.filler, pid, 'bench') for _ in range(count)]
        for pokemon in result:
            pokemon.set_attribute(AttrID.HP, 200)
        return result

    async def assert_selection_size(self, card_path, attack_title, side, count,
                                    supporter=False):
        rig, _, ctx = self.ctx(card_path, attack_title)
        targets = self.set_bench(rig, side, count)
        if supporter:
            brawly = fixtures.definition('SWSH6.Brawly_131')
            rig.session.turn_state.trainers_played.append(
                (brawly.guid, brawly.display_name, TrainerType.SUPPORTER.value))
        ctx.opponent_active().set_attribute(AttrID.HP, 300)

        async def pick(player_id, source_id, candidates, requested,
                       minimum, prompt, **kwargs):
            self.assertLessEqual(requested, len(candidates))
            self.assertEqual(requested, min(2, len(candidates)))
            return [pokemon.entity_id for pokemon in candidates[:requested]]

        rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
        if attack_title == 'Double Gunner':
            ctx.discard_from_hand = AsyncMock(return_value=[object()])
        if attack_title in ('Follow-Up', 'Cheerful Charge'):
            ctx.search_deck = AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        expected_calls = int(count > 0 or attack_title == 'Astral Barrage')
        self.assertEqual(rig.session.prompt_entity_picker.await_count, expected_calls)
        return targets

    async def test_opponent_bench_attacks(self):
        cases = (
            ('CEL25.Kyogre_3', 'Aqua Storm', False),
            ('SWSH6.Zangoose_120', 'Gale Claws', True),
        )
        for card_path, title, supporter in cases:
            for count in (0, 1, 2):
                with self.subTest(card=card_path, bench=count):
                    await self.assert_selection_size(card_path, title, P2,
                                                     count, supporter)

    async def test_astral_barrage_with_only_one_opposing_pokemon(self):
        for card_path in (
            'SWSH6.ShadowRiderCalyrexV_74',
            'SWSH6.ShadowRiderCalyrexV_171',
            'SWSH6.ShadowRiderCalyrexV_172',
        ):
            for count in (0, 1):
                with self.subTest(card=card_path, bench=count):
                    rig, _, ctx = self.ctx(card_path, 'Astral Barrage')
                    self.set_bench(rig, P2, count)

                    async def pick(_pid, _source, candidates, requested,
                                   minimum, _prompt, **kwargs):
                        self.assertEqual(requested, min(2, 1 + count))
                        return [pokemon.entity_id for pokemon in candidates[:requested]]

                    rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
                    await ctx.ability.effect(ctx)
                    rig.session.prompt_entity_picker.assert_awaited_once()

    async def test_own_bench_attack(self):
        for count in (0, 1, 2):
            with self.subTest(bench=count):
                await self.assert_selection_size('SWSH5.Vivillon_13',
                                                 'Vital Powder', P1, count)

    async def test_optional_own_bench_attacks(self):
        for card_path, title in (
            ('SWSH12.Cobalion_126', 'Follow-Up'),
            ('SWSH10.HisuianVoltorb_2', 'Cheerful Charge'),
        ):
            for count in (0, 1, 2):
                with self.subTest(card=card_path, bench=count):
                    await self.assert_selection_size(card_path, title, P1, count)

    async def test_double_gunner_printings(self):
        for card_path in ('SWSH8.InteleonVMAX_79',
                          'SWSH8.InteleonVMAX_266'):
            for count in (0, 1, 2):
                with self.subTest(card=card_path, bench=count):
                    await self.assert_selection_size(card_path, 'Double Gunner',
                                                     P2, count)

    async def test_shared_chooser_clamps_other_dynamic_target_pools(self):
        rig, _, ctx = self.ctx('SWSH3.Decidueye_13', 'Splitting Arrow')
        bench = self.set_bench(rig, P2, 1)

        async def pick(_pid, _source, candidates, requested,
                       minimum, _prompt, **kwargs):
            self.assertEqual(candidates, bench)
            self.assertEqual(requested, 1)
            return [bench[0].entity_id]

        rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
        self.assertEqual(await ctx.choose_cards(bench, 2), bench)


if __name__ == '__main__':
    unittest.main()
