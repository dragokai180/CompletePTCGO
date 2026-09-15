"""Energy-unit discard effects versus explicit per-card damage bonuses."""
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from tests import test_sm_swsh_final_trainers as helpers
from spirit.game.attributes import PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class EnergyDiscardClosureTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    energy = helpers.RemainingTrainerTests.energy
    stadium = helpers.RemainingTrainerTests.stadium

    async def test_numeric_and_coin_count_discards_accept_double_energy(self):
        for path, title, opposing, flips in (
            ('SWSH1.Seaking_47', 'Ripping Horn', True, [True, True, False]),
            ('SWSH11.GalarianStunfisk_127', 'Field Trap', True, []),
            ('SWSH2.Zacian_139', 'Smashing Edge', False, [False]),
            ('SWSH5.Heatmor_26', 'Burning Licks', True, [True, True]),
            ('SWSH8.Magcargo_35', 'Body Splash', False, [False, False, True]),
        ):
            with self.subTest(path=path):
                rig, e = self.rig(path)
                ability = next(a for a in fixtures.definition(path).abilities if a.title == title)
                ctx = EffectContext(rig.session, P1, e['target'], ability)
                pid, target = (P2, ctx.defender) if opposing else (P1, ctx.attacker)
                for energy in list(ctx.attached_energies(target)): rig.to_area(energy, pid, 'hand')
                double = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), pid, 'hand')
                spare = self.energy(rig, pid=pid)
                rig.attach(double, target); rig.attach(spare, target)
                if 'Stunfisk' in path: self.stadium(rig, 'SM11.GiantHearth_197', P2)
                ctx.flip_coins = AsyncMock(return_value=flips)
                ctx.deal_damage = AsyncMock(return_value=10)
                rig.session.prompt_energy_unit_picker = AsyncMock(return_value=[double.entity_id])
                await ability.effect(ctx)
                self.assertIn(double, ctx.discard_pile(pid))
                self.assertIs(spare.parent, target)
                self.assertEqual(rig.session.prompt_energy_unit_picker.call_args.args[3], 2)

    async def test_typed_discards_use_units_and_keep_nonmatching_energy(self):
        # The unit primitive is deliberately given a doubled Lightning card;
        # independent Energy-provider tests cover the actual doubling passives.
        for path, title, amount in (('SWSH7.Ampharos_56', 'Electron Crush', 3),
                                    ('SWSH8.Vikavolt_101', 'Electro Blaster', 2)):
            with self.subTest(path=path):
                rig, e = self.rig(path)
                ability = next(a for a in fixtures.definition(path).abilities if a.title == title)
                ctx = EffectContext(rig.session, P1, e['target'], ability)
                for energy in list(ctx.attached_energies(ctx.attacker)): rig.to_area(energy, P1, 'hand')
                double = self.energy(rig, PokemonTypes.LIGHTNING)
                spare = self.energy(rig, PokemonTypes.LIGHTNING)
                wrong = self.energy(rig, PokemonTypes.METAL)
                picked = [double]
                for c in (double, spare, wrong): rig.attach(c, ctx.attacker)
                if amount == 3:
                    extra = self.energy(rig, PokemonTypes.LIGHTNING)
                    rig.attach(extra, ctx.attacker); picked.append(extra)
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.choose_pokemon = AsyncMock(return_value=ctx.defender)
                ctx.deal_damage = AsyncMock(return_value=10)
                rig.session.prompt_energy_unit_picker = AsyncMock(return_value=[c.entity_id for c in picked])
                with patch('spirit.game.session.effects.energy_provided_count', side_effect=lambda c, board: 2 if c is double else 1):
                    await ability.effect(ctx)
                self.assertTrue(all(c in ctx.discard_pile() for c in picked))
                self.assertIs(spare.parent, ctx.attacker)
                self.assertIs(wrong.parent, ctx.attacker)
                self.assertNotIn(wrong, rig.session.prompt_energy_unit_picker.call_args.args[2])

    async def test_max_lance_bonus_counts_discarded_cards_not_energy_units(self):
        for number in (46, 202, 203):
            rig, e = self.rig(f'SWSH6.IceRiderCalyrexVMAX_{number}')
            ability = fixtures.definition(f'SWSH6.IceRiderCalyrexVMAX_{number}').abilities[1]
            ctx = EffectContext(rig.session, P1, e['target'], ability)
            double = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), P1, 'hand')
            rig.attach(double, ctx.attacker)
            ctx.ask_yes_no = AsyncMock(return_value=True)
            ctx.choose_cards = AsyncMock(return_value=[double])
            ctx.deal_damage = AsyncMock(return_value=130)
            await ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], 130)
