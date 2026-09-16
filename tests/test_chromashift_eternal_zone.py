"""Live type changes must reach Eternal Zone and Dread End."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext, is_pokemon_of_type
from spirit.game.session.passives import effective_bench_capacity, effective_pokemon_types, compute_damage
from spirit.tools.effect_smoke import P1, P2


PRINTS = ('SWSH3.EternatusVMAX_117', 'SWSH3.EternatusVMAX_192',
          'SWSH11.EternatusVMAX_239')


class ChromashiftEternalZoneTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_field(self, path=PRINTS[0], owner=P1):
        rig, _ = self.rig(path)
        for pid in (P1, P2):
            for card in list(rig.board.pokemon_in_play(pid)):
                rig.to_area(card, pid, 'hand')
        definition = fixtures.definition(path)
        attacker = self.add(rig, definition, owner, 'activePokemonArea')
        opponent = P2 if owner == P1 else P1
        self.add(rig, self.filler, opponent, 'activePokemonArea')
        kecleon = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), owner, 'bench')
        attack = next(a for a in definition.abilities if a.title == 'Dread End')
        return rig, kecleon, EffectContext(rig.session, owner, attacker, attack)

    def attach_basic(self, rig, pokemon, kind=PokemonTypes.DARKNESS):
        rig.attach_energy_type(pokemon.owning_player_id, pokemon, kind.value)
        return rig.board.attached_energies(pokemon)[-1]

    async def assert_attack_damage(self, rig, ctx, base):
        ctx.defender.set_attribute(AttrID.HP, 1000)
        expected = compute_damage(rig.board, ctx.attacker, ctx.defender, base).amount
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.defender.get_attribute(AttrID.HP), 1000 - expected)

    async def test_all_prints_and_both_players_recognize_darkness_kecleon(self):
        for path in PRINTS:
            for owner in (P1, P2):
                with self.subTest(path=path, owner=owner):
                    rig, kecleon, ctx = self.setup_field(path, owner)
                    self.assertEqual(effective_bench_capacity(rig.board, owner), 5)
                    self.attach_basic(rig, kecleon)
                    self.assertEqual(effective_pokemon_types(rig.board, kecleon),
                                     [PokemonTypes.DARKNESS.value])
                    self.assertEqual(effective_bench_capacity(rig.board, owner), 8)
                    self.assertEqual(effective_bench_capacity(rig.board, ctx.opponent_id), 5)
                    await self.assert_attack_damage(rig, ctx, 60)

    async def test_multiple_types_and_energy_removal_update_both_effects(self):
        rig, kecleon, ctx = self.setup_field()
        dark = self.attach_basic(rig, kecleon)
        self.attach_basic(rig, kecleon, PokemonTypes.WATER)
        self.assertEqual(set(effective_pokemon_types(rig.board, kecleon)),
                         {PokemonTypes.DARKNESS.value, PokemonTypes.WATER.value})
        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)
        await self.assert_attack_damage(rig, ctx, 60)
        rig.to_area(dark, P1, 'discard')
        self.assertEqual(effective_bench_capacity(rig.board, P1), 5)
        await self.assert_attack_damage(rig, ctx, 30)

    async def test_special_darkness_energy_does_not_trigger_chromashift(self):
        rig, kecleon, ctx = self.setup_field()
        energy = self.add(rig, fixtures.definition('SWSH3.HidingDarknessEnergy_175'), P1, 'hand')
        rig.attach(energy, kecleon)
        self.assertEqual(effective_pokemon_types(rig.board, kecleon), [PokemonTypes.COLORLESS.value])
        self.assertEqual(effective_bench_capacity(rig.board, P1), 5)
        await self.assert_attack_damage(rig, ctx, 30)

    async def test_silent_lab_disables_chromashift_and_removal_restores_it(self):
        rig, kecleon, ctx = self.setup_field()
        self.attach_basic(rig, kecleon)
        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)
        lab = self.add(rig, fixtures.definition('XY5.SilentLab_140'), P2, 'hand')
        rig.board.move_card(lab.entity_id, rig.board.find_global_area('activeStadium').entity_id)
        self.assertEqual(effective_pokemon_types(rig.board, kecleon), [PokemonTypes.COLORLESS.value])
        self.assertEqual(effective_bench_capacity(rig.board, P1), 5)
        await self.assert_attack_damage(rig, ctx, 30)
        rig.to_area(lab, P2, 'discard')
        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)
        await self.assert_attack_damage(rig, ctx, 60)

    async def test_other_non_darkness_pokemon_still_prevents_expanded_bench(self):
        rig, kecleon, ctx = self.setup_field()
        self.attach_basic(rig, kecleon)
        other = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), P1, 'bench')
        self.assertEqual(effective_bench_capacity(rig.board, P1), 5)
        await self.assert_attack_damage(rig, ctx, 60)
        rig.to_area(other, P1, 'hand')
        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)

    async def test_losing_darkness_enforces_bench_reduction_without_prizes(self):
        rig, kecleon, ctx = self.setup_field()
        dark = self.attach_basic(rig, kecleon)
        extras = [self.add(rig, fixtures.definition('SWSH3.EternatusV_116'), P1, 'bench')
                  for _ in range(6)]
        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)
        self.assertEqual(len(ctx.my_bench()), 7)
        rig.to_area(dark, P1, 'discard')
        with patch.object(rig.session, 'prompt_entity_picker',
                          AsyncMock(return_value=[p.entity_id for p in extras[:2]])) as pick, \
                patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
            await rig.session.enforce_bench_capacity()
        pick.assert_awaited_once()
        self.assertEqual(pick.call_args.args[3], 2)
        self.assertEqual(len(ctx.my_bench()), 5)
        self.assertTrue(all(p in ctx.discard_pile(P1) for p in extras[:2]))
        prizes.assert_not_awaited()

    async def test_out_of_play_filters_keep_printed_types(self):
        rig, kecleon, ctx = self.setup_field()
        self.attach_basic(rig, kecleon)
        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)
        for zone in ('hand', 'deck', 'discard'):
            rig.to_area(kecleon, P1, zone)
            self.assertTrue(is_pokemon_of_type(kecleon, PokemonTypes.COLORLESS))
            self.assertFalse(is_pokemon_of_type(kecleon, PokemonTypes.DARKNESS))
            await self.assert_attack_damage(rig, ctx, 30)


if __name__ == '__main__':
    unittest.main()
