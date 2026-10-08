"""Energy acceleration that attaches one card to each eligible Pokémon."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures

from spirit.game.session.effects import EffectContext, is_pokemon_card
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1


class DistributedEnergyAttachmentTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def clear_discard(self, rig):
        discard = rig.board.find_player_area(P1, 'discard')
        for card in list(discard.children):
            rig.to_area(card, P1, 'hand')

    def energy(self, rig, path):
        return self.add(rig, fixtures.definition(path), P1, 'discard')

    async def test_sada_attaches_to_two_distinct_ancient_pokemon_then_draws(self):
        rig, entries = self.rig('SV085.RoaringMoonex_162')
        self.clear_discard(rig)
        first = entries['target']
        second = self.add(rig, fixtures.definition('SV085.SandyShocksex_56'),
                          P1, 'bench')
        ordinary = self.add(rig, fixtures.definition('BW1.Snivy_1'),
                            P1, 'bench')
        energies = [self.energy(rig, 'BW1.FireEnergy_106') for _ in range(2)]
        card = fixtures.definition('SV085.ProfessorSadasVitality_120')
        supporter = self.add(rig, card, P1, 'hand')
        ctx = EffectContext(rig.session, P1, supporter, None)
        ctx.is_trainer_effect = True
        ctx.draw_cards = AsyncMock()
        selection_order = []

        async def choose(pool, count, **kwargs):
            if pool and is_pokemon_card(pool[0]):
                selection_order.append('pokemon')
                self.assertEqual(count, 2)
                self.assertTrue({first, second}.issubset(pool))
                self.assertNotIn(ordinary, pool)
                return [first, second]
            selection_order.append('energy')
            self.assertEqual(count, 1)
            return [pool[0]]

        ctx.choose_cards = AsyncMock(side_effect=choose)
        self.assertTrue(trainer_condition_met(card.condition, rig.board, P1,
                                              supporter))

        await card.effect(ctx)

        self.assertEqual(selection_order, ['pokemon', 'energy', 'energy'])
        self.assertEqual(len(set(rig.board.attached_energies(first))
                             & set(energies)), 1)
        self.assertEqual(len(set(rig.board.attached_energies(second)) & set(energies)), 1)
        self.assertFalse(set(rig.board.attached_energies(ordinary)) & set(energies))
        ctx.draw_cards.assert_awaited_once_with(3)

    def test_sada_requires_ancient_target_and_basic_energy(self):
        rig, _ = self.rig('BW1.Snivy_1')
        self.clear_discard(rig)
        card = fixtures.definition('SV085.ProfessorSadasVitality_120')
        supporter = self.add(rig, card, P1, 'hand')
        basic = self.energy(rig, 'BW1.FireEnergy_106')
        self.assertFalse(trainer_condition_met(card.condition, rig.board,
                                               P1, supporter))

        self.add(rig, fixtures.definition('SV085.ScreamTail_42'), P1, 'bench')
        self.assertTrue(trainer_condition_met(card.condition, rig.board,
                                              P1, supporter))
        rig.to_area(basic, P1, 'hand')
        self.energy(rig, 'SM11.RecycleEnergy_212')
        self.assertFalse(trainer_condition_met(card.condition, rig.board,
                                               P1, supporter))

    async def test_sada_draws_with_only_one_energy_available(self):
        rig, entries = self.rig('SV085.RoaringMoonex_162')
        self.clear_discard(rig)
        first = entries['target']
        self.add(rig, fixtures.definition('SV085.SandyShocksex_56'), P1,
                 'bench')
        energy = self.energy(rig, 'BW1.FireEnergy_106')
        card = fixtures.definition('SV085.ProfessorSadasVitality_120')
        source = self.add(rig, card, P1, 'hand')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.is_trainer_effect = True
        ctx.draw_cards = AsyncMock()

        async def choose(pool, count, **kwargs):
            return [first] if pool and is_pokemon_card(pool[0]) else [energy]

        ctx.choose_cards = AsyncMock(side_effect=choose)
        await card.effect(ctx)

        self.assertIn(energy, rig.board.attached_energies(first))
        ctx.draw_cards.assert_awaited_once_with(3)

    async def test_sada_does_not_draw_when_attachment_fails(self):
        rig, entries = self.rig('SV085.RoaringMoonex_162')
        self.clear_discard(rig)
        energy = self.energy(rig, 'BW1.FireEnergy_106')
        card = fixtures.definition('SV085.ProfessorSadasVitality_120')
        source = self.add(rig, card, P1, 'hand')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.is_trainer_effect = True
        ctx.draw_cards = AsyncMock()
        ctx.attach_energy = AsyncMock(return_value=False)

        async def choose(pool, count, **kwargs):
            return [entries['target']] if pool and is_pokemon_card(pool[0]) \
                else [energy]

        ctx.choose_cards = AsyncMock(side_effect=choose)
        await card.effect(ctx)

        ctx.attach_energy.assert_awaited_once_with(energy, entries['target'])
        ctx.draw_cards.assert_not_awaited()

    async def test_reboot_pod_still_attaches_only_to_future_pokemon(self):
        rig, entries = self.rig('SV085.IronHandsex_31')
        self.clear_discard(rig)
        first = entries['target']
        second = self.add(rig, fixtures.definition('SV05.IronBoulderex_99'),
                          P1, 'bench')
        ordinary = self.add(rig, fixtures.definition('BW1.Snivy_1'),
                            P1, 'bench')
        energies = [self.energy(rig, 'BW1.FireEnergy_106') for _ in range(2)]
        card = fixtures.definition('SV05.RebootPod_158')
        source = self.add(rig, card, P1, 'hand')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.is_trainer_effect = True
        ctx.choose_cards = AsyncMock(return_value=energies)
        ctx.choose_pokemon = AsyncMock(side_effect=[first, second])

        await card.effect(ctx)

        self.assertEqual(len(set(rig.board.attached_energies(first))
                             & set(energies)), 1)
        self.assertEqual(len(set(rig.board.attached_energies(second))
                             & set(energies)), 1)
        self.assertFalse(set(rig.board.attached_energies(ordinary))
                         & set(energies))
        for call in ctx.choose_pokemon.await_args_list:
            self.assertNotIn(ordinary, call.args[0])

    async def test_attacks_attach_one_energy_to_each_printed_target(self):
        cases = (
            ('SV4.Volcanion_22', 'Dual Turbo',
             'BW1.FireEnergy_106', ('BW1.Snivy_1', 'BW1.Tepig_15')),
            ('SV05.Mudsdale_92', 'Mud Stock',
             'BW1.FightingEnergy_110', ('BW1.Snivy_1', 'BW1.Tepig_15')),
            ('SM7.Latias_107', 'Dreamy Mist',
             'BW1.FireEnergy_106', ('SM7.Bagon_103', 'SM7.Bagon_104')),
        )
        for path, title, energy_path, target_paths in cases:
            with self.subTest(path=path):
                rig, entries = self.rig(path)
                self.clear_discard(rig)
                for pokemon in list(rig.board.find_player_area(P1, 'bench').children):
                    rig.to_area(pokemon, P1, 'hand')
                targets = [self.add(rig, fixtures.definition(target_path),
                                    P1, 'bench') for target_path in target_paths]
                ordinary = self.add(rig, fixtures.definition('BW1.Snivy_1'),
                                    P1, 'bench') if title == 'Dreamy Mist' else None
                wrong_energy = self.energy(rig, 'BW1.WaterEnergy_107') \
                    if title != 'Dreamy Mist' else None
                energies = [self.energy(rig, energy_path) for _ in range(2)]
                attack = next(a for a in fixtures.definition(path).abilities
                              if a.title == title)
                ctx = EffectContext(rig.session, P1, entries['target'], attack)
                ctx.deal_damage = AsyncMock()

                async def choose(pool, count, **kwargs):
                    if pool and is_pokemon_card(pool[0]):
                        self.assertEqual(count, 2)
                        return targets
                    return [pool[0]]

                ctx.choose_cards = AsyncMock(side_effect=choose)
                ctx.choose_pokemon = AsyncMock(return_value=targets[0])
                await attack.effect(ctx)

                self.assertEqual(len(set(rig.board.attached_energies(targets[0]))
                                     & set(energies)), 1)
                self.assertEqual(len(set(rig.board.attached_energies(targets[1]))
                                     & set(energies)), 1)
                if ordinary is not None:
                    self.assertFalse(set(rig.board.attached_energies(ordinary))
                                     & set(energies))
                if wrong_energy is not None:
                    self.assertIn(wrong_energy, ctx.discard_pile())


if __name__ == '__main__':
    unittest.main()
