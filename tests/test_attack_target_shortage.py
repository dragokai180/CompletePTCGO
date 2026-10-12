"""Multi-target effects remain playable with fewer Pokémon than printed targets."""
import unittest
from unittest.mock import AsyncMock, Mock

from tests import test_hgss_rules as fixtures

from spirit.game.attributes import AttrID, PokemonTypes, TrainerType
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
                                    supporter=False, automatic=False):
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
        expected_calls = int(count > 0 and not (automatic and count <= 2))
        self.assertEqual(rig.session.prompt_entity_picker.await_count, expected_calls)
        return targets

    async def test_opponent_bench_attacks(self):
        cases = (
            ('CEL25.Kyogre_3', 'Aqua Storm', False),
            ('SWSH6.Zangoose_120', 'Gale Claws', True),
        )
        for card_path, title, supporter in cases:
            for count in (0, 1, 2, 3):
                with self.subTest(card=card_path, bench=count):
                    await self.assert_selection_size(card_path, title, P2,
                                                     count, supporter,
                                                     automatic=True)

    async def test_generic_fixed_bench_damage_skips_only_redundant_choices(self):
        cases = (
            ('BW3.Archeops_67', 'Rock Slide', 10),
            ('HGSS2.Zubat_70', 'Double Attack', 10),
        )
        for path, title, damage in cases:
            for count in (1, 2, 3):
                with self.subTest(card=path, bench=count):
                    rig, _, ctx = self.ctx(path, title)
                    bench = self.set_bench(rig, P2, count)
                    if count <= 2:
                        ctx.choose_cards = AsyncMock(side_effect=AssertionError(
                            'all eligible targets must be hit automatically'))
                    else:
                        ctx.choose_cards = AsyncMock(return_value=bench[:2])
                    await ctx.ability.effect(ctx)
                    self.assertEqual(
                        [target.get_attribute(AttrID.HP) for target in bench],
                        [200 - damage] * min(count, 2)
                        + [200] * max(0, count - 2))
                    self.assertEqual(ctx.choose_cards.await_count, int(count > 2))

    async def test_aqua_storm_damages_every_available_bench_target(self):
        rig, _, ctx = self.ctx('CEL25.Kyogre_3', 'Aqua Storm')
        bench = self.set_bench(rig, P2, 2)
        energy = rig.pull_guid(P1, self.energies[PokemonTypes.WATER.value])
        self.assertIsNotNone(energy)
        ctx.deck_top = Mock(return_value=[energy])
        ctx.choose_cards = AsyncMock(side_effect=AssertionError(
            'both targets are mandatory'))
        await ctx.ability.effect(ctx)
        self.assertEqual([target.get_attribute(AttrID.HP) for target in bench],
                         [150, 150])
        ctx.choose_cards.assert_not_awaited()

    async def test_gale_claws_damages_every_available_bench_target(self):
        rig, _, ctx = self.ctx('SWSH6.Zangoose_120', 'Gale Claws')
        bench = self.set_bench(rig, P2, 2)
        brawly = fixtures.definition('SWSH6.Brawly_131')
        rig.session.turn_state.trainers_played.append(
            (brawly.guid, brawly.display_name, TrainerType.SUPPORTER.value))
        ctx.choose_cards = AsyncMock(side_effect=AssertionError(
            'both targets are mandatory'))
        await ctx.ability.effect(ctx)
        self.assertEqual([target.get_attribute(AttrID.HP) for target in bench],
                         [150, 150])
        ctx.choose_cards.assert_not_awaited()

    async def test_split_bomb_auto_targets_only_when_all_pokemon_are_needed(self):
        rig, _, ctx = self.ctx('ME2PT5.MegaEelektrossex_61', 'Split Bomb')
        bench = self.set_bench(rig, P2, 1)
        active = ctx.opponent_active()
        active.set_attribute(AttrID.HP, 300)
        active.set_attribute(AttrID.WEAKNESS_TYPES, [])
        active.set_attribute(AttrID.RESISTANCE_TYPES, [])
        ctx.choose_cards = AsyncMock(side_effect=AssertionError(
            'both targets are mandatory'))
        await ctx.ability.effect(ctx)
        self.assertEqual(active.get_attribute(AttrID.HP), 240)
        self.assertEqual(bench[0].get_attribute(AttrID.HP), 140)
        ctx.choose_cards.assert_not_awaited()

    async def test_bespoke_fixed_damage_attacks_skip_redundant_choices(self):
        cases = (
            ('SWSH12.Reuniclus_78', 'Cell Fork', 30, False),
            ('SWSH11.Spectrier_81', 'Night Footsteps', 20, True),
            ('SV05.IronCrownex_81', 'Twin Shotels', 50, True),
        )
        for path, title, bench_damage, targets_active in cases:
            with self.subTest(card=path):
                rig, _, ctx = self.ctx(path, title)
                bench = self.set_bench(rig, P2, 1)
                if targets_active:
                    ctx.opponent_active().set_attribute(AttrID.HP, 300)
                    ctx.opponent_active().set_attribute(AttrID.WEAKNESS_TYPES, [])
                    ctx.opponent_active().set_attribute(AttrID.RESISTANCE_TYPES, [])
                ctx.choose_cards = AsyncMock(side_effect=AssertionError(
                    'all eligible targets must be hit automatically'))
                await ctx.ability.effect(ctx)
                self.assertEqual(bench[0].get_attribute(AttrID.HP),
                                 200 - bench_damage)
                ctx.choose_cards.assert_not_awaited()

    async def test_astral_barrage_with_only_one_opposing_pokemon(self):
        for card_path in (
            'SWSH6.ShadowRiderCalyrexV_74',
            'SWSH6.ShadowRiderCalyrexV_171',
            'SWSH6.ShadowRiderCalyrexV_172',
        ):
            for count in (0, 1, 2):
                with self.subTest(card=card_path, bench=count):
                    rig, _, ctx = self.ctx(card_path, 'Astral Barrage')
                    self.set_bench(rig, P2, count)

                    async def pick(_pid, _source, candidates, requested,
                                   minimum, _prompt, **kwargs):
                        self.assertEqual(requested, min(2, 1 + count))
                        return [pokemon.entity_id for pokemon in candidates[:requested]]

                    rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(
                        rig.session.prompt_entity_picker.await_count,
                        int(count >= 2))

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
