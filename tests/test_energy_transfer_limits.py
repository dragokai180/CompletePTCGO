"""Transfer limits count physical cards and bind the printed source/target."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.standard_era import standard_trainer_effect
from spirit.game.data_utils import CARD_DEFS_BY_GUID, def_for
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import carrier_pokemon
from spirit.tools.effect_smoke import P1, Rig


class EnergyTransferLimitTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    add = fixtures.HgssRulesTests.add

    def transfer_rig(self, card_def):
        rig = Rig(card_def, self.filler, self.energies, self.item)
        entities = rig.setup('trainer')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        pokemon = ctx.my_pokemon_in_play()
        for holder in pokemon:
            for energy in list(ctx.attached_energies(holder)):
                rig.to_area(energy, P1, 'discard')
        donors = [pokemon[0], pokemon[1]]
        for donor in donors:
            for _ in range(3):
                # Use real basic Energy archetypes, preserving distinct copies.
                energy = self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]),
                                  P1, 'hand')
                rig.attach(energy, donor)
        ctx.choose_cards = AsyncMock(side_effect=lambda cards, *a, **kw: list(cards)[:1])
        ctx.choose_pokemon = AsyncMock(side_effect=lambda cards, *a, **kw: list(cards)[-1])
        return rig, ctx, pokemon

    async def test_every_energy_switch_print_moves_only_one_basic(self):
        prints = [d for d in CARD_DEFS_BY_GUID.values()
                  if d.display_name == 'Energy Switch']
        self.assertGreaterEqual(len(prints), 10)
        for card_def in prints:
            with self.subTest(set=card_def.set_code, number=card_def.collector_number):
                rig, ctx, pokemon = self.transfer_rig(card_def)
                special = self.add(rig, definition('SM1.DoubleColorlessEnergy_136'),
                                   P1, 'hand')
                rig.attach(special, pokemon[0])
                await card_def.effect(ctx)
                self.assertEqual(ctx.choose_cards.await_count, 1)
                self.assertEqual(len(ctx.attached_energies(pokemon[-1])), 1)
                self.assertNotIn(special, ctx.choose_cards.call_args.args[0])
                self.assertIs(carrier_pokemon(special), pokemon[0])

    async def test_generic_singular_and_numbered_wording(self):
        for wording, count in [('a basic Energy', 1), ('an Energy', 1),
                               ('up to 2 basic Energy', 2), ('2 Energy', 2)]:
            rig, ctx, pokemon = self.transfer_rig(definition('HGSS1.EnergySwitch_91'))
            await standard_trainer_effect(
                f'Move {wording} from 1 of your Pokémon to another of your Pokémon.'
            )(ctx)
            self.assertEqual(len(ctx.attached_energies(pokemon[-1])), count, wording)

    async def test_poppy_and_tag_switch_keep_one_source_and_destination(self):
        for path in ['SV3.Poppy_193', 'SM11.TagSwitch_209']:
            with self.subTest(path=path):
                card_def = definition(path)
                rig, ctx, pokemon = self.transfer_rig(card_def)
                if 'TagSwitch' in path:
                    tag = definition('SM9.PikachuZekromGX_33')
                    for index in (0, 1):
                        replacement = self.add(rig, tag, P1, 'bench')
                        for energy in list(ctx.attached_energies(pokemon[index])):
                            rig.attach(energy, replacement)
                        rig.to_area(pokemon[index], P1, 'discard')
                        pokemon[index] = replacement
                donor, other, target = pokemon
                other_ids = {e.entity_id for e in ctx.attached_energies(other)}
                pools = []
                def pick(cards, *a, **kw):
                    pools.append(list(cards))
                    if len(pools) == 1:
                        return [next(c for c in cards if carrier_pokemon(c) is donor)]
                    # Would switch donors without the binding restriction.
                    return [next((c for c in cards if c.entity_id in other_ids), cards[0])]
                def target_pick(cards, *a, **kw):
                    if ctx.choose_pokemon.await_count == 1:
                        return target
                    return other if other in cards else cards[0]
                ctx.choose_cards = AsyncMock(side_effect=pick)
                ctx.choose_pokemon = AsyncMock(side_effect=target_pick)
                await card_def.effect(ctx)
                self.assertEqual(len(pools), 2)
                self.assertTrue(all(c.entity_id not in other_ids for c in pools[1]))
                self.assertEqual(len(ctx.attached_energies(donor)), 1)
                self.assertEqual(len(ctx.attached_energies(other)), 3)
                self.assertEqual(len(ctx.attached_energies(target)), 2)
                self.assertEqual(ctx.choose_pokemon.call_args.args[0], [target])

    async def test_multi_switch_moves_one_special_card_not_one_energy_unit(self):
        for path in ['SM2.MultiSwitch_129', 'SM3.MultiSwitch_164']:
            card_def = definition(path)
            rig, ctx, pokemon = self.transfer_rig(card_def)
            special = self.add(rig, definition('SM1.DoubleColorlessEnergy_136'), P1, 'hand')
            rig.attach(special, pokemon[1])
            ctx.choose_cards = AsyncMock(return_value=[special])
            await card_def.effect(ctx)
            self.assertEqual(ctx.choose_cards.await_count, 1)
            self.assertIs(carrier_pokemon(special), ctx.my_active())

    async def test_tag_switch_requires_a_tag_team_with_attached_energy(self):
        card_def = definition('SM11.TagSwitch_209')
        rig, ctx, pokemon = self.transfer_rig(card_def)
        self.assertFalse(card_def.condition(rig.board, P1))
        tag = self.add(rig, definition('SM9.PikachuZekromGX_33'), P1, 'bench')
        self.assertFalse(card_def.condition(rig.board, P1))
        rig.attach(ctx.attached_energies(pokemon[0])[0], tag)
        self.assertTrue(card_def.condition(rig.board, P1))

    async def test_unlimited_redistribution_still_moves_all_selected_cards(self):
        rig, ctx, pokemon = self.transfer_rig(definition('HGSS1.EnergySwitch_91'))
        moved = await ctx.move_energy_freely(pokemon, pokemon)
        self.assertEqual(len(moved), 6)
        self.assertEqual(len(ctx.attached_energies(pokemon[-1])), 6)

    async def test_cancel_and_no_distinct_target_make_no_moves(self):
        rig, ctx, pokemon = self.transfer_rig(definition('HGSS1.EnergySwitch_91'))
        self.assertEqual(await ctx.move_energy_freely([pokemon[0]], [pokemon[0]]), [])
        ctx.choose_cards.assert_not_awaited()
        ctx.choose_cards = AsyncMock(return_value=[])
        self.assertEqual(await ctx.move_energy_freely(pokemon, pokemon, max_count=1), [])
        ctx.choose_pokemon.assert_not_awaited()


if __name__ == '__main__':
    unittest.main()
