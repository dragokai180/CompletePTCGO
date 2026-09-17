"""Assert complete outcomes, not merely that generic text effects did something."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.bw_era import bw_legacy_ability
from spirit.game.data_utils import def_for
from spirit.game.session.legal_actions import _ability_entries
from spirit.tools.effect_smoke import P1, P2


class GenericTextRegressions(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_flare_witch_attaches_without_damage(self):
        rig, e, ctx = self.ctx('XY10.DelphoxBREAK_14', 'Flare Witch')
        energy = next(c for c in ctx.deck() if c.archetype_id.lower() ==
                      self.energies[PokemonTypes.FIRE.value].lower())
        target = ctx.my_bench()[0]
        hp = target.get_attribute(AttrID.HP)
        ctx.search_deck = AsyncMock(return_value=[energy])
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.shuffle_deck = AsyncMock()
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertIn(energy, ctx.attached_energies(target))
        self.assertEqual(target.get_attribute(AttrID.HP), hp)
        ctx.deal_damage.assert_not_awaited()
        ctx.shuffle_deck.assert_awaited_once()
        self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)

    async def test_sinister_surge_reprint_uses_same_effect_and_condition(self):
        regular = fixtures.definition('ME2.Toxtricity_68').abilities[0]
        promo = fixtures.definition('MEP.Toxtricity_17').abilities[0]
        self.assertIs(promo.effect, regular.effect)
        self.assertIs(promo.condition, regular.condition)

    async def test_flare_navigate_requires_a_successful_attachment_for_counters(self):
        rig, e, ctx = self.ctx('BW9.Chandelure_16', 'Flare Navigate')
        energy = next(c for c in ctx.deck() if c.archetype_id.lower() ==
                      self.energies[PokemonTypes.FIRE.value].lower())
        ctx.search_deck = AsyncMock(return_value=[energy])
        ctx.choose_pokemon = AsyncMock(return_value=ctx.my_bench()[0])
        ctx.attach_energy = AsyncMock(return_value=False)
        ctx.deal_damage = AsyncMock()
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.attach_energy.assert_awaited_once()
        ctx.deal_damage.assert_not_awaited()

    async def test_sinister_surge_targets_and_conditional_counters(self):
        for path in ('ME2.Toxtricity_68', 'MEP.Toxtricity_17'):
            for succeeds in (False, True):
                with self.subTest(path=path, succeeds=succeeds):
                    rig, e, ctx = self.ctx(path, 'Sinister Surge')
                    valid = ctx.my_bench()[0]
                    valid.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.DARKNESS.value])
                    for pokemon in ctx.my_bench()[1:]:
                        pokemon.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
                    energy = next(c for c in ctx.deck() if c.archetype_id.lower() ==
                                  self.energies[PokemonTypes.DARKNESS.value].lower())
                    ctx.ask_yes_no = AsyncMock(return_value=True)
                    ctx.search_deck = AsyncMock(return_value=[energy])
                    ctx.choose_pokemon = AsyncMock(return_value=valid)
                    ctx.attach_energy = AsyncMock(return_value=succeeds)
                    ctx.deal_damage = AsyncMock()
                    ctx.shuffle_deck = AsyncMock()
                    await ctx.ability.effect(ctx)
                    self.assertEqual(ctx.choose_pokemon.call_args.args[0], [valid])
                    ctx.attach_energy.assert_awaited_once_with(energy, valid)
                    if succeeds:
                        ctx.deal_damage.assert_awaited_once_with(
                            20, target=valid, apply_modifiers=False,
                            as_counters=True, is_attack=False)
                    else:
                        ctx.deal_damage.assert_not_awaited()
                    ctx.shuffle_deck.assert_awaited_once()

    async def test_sinister_surge_permission_uses_public_targets_not_deck_contents(self):
        rig, e, ctx = self.ctx('MEP.Toxtricity_17', 'Sinister Surge')
        for p in ctx.my_bench():
            p.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.my_bench()[0].set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.DARKNESS.value])
        for c in list(ctx.deck()):
            rig.to_area(c, P1, 'discard')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        self.add(rig, self.filler, P1, 'deck')
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_lunar_cycle_reprint_requires_solrock_and_pays_energy(self):
        for path in ('ME1.Lunatone_74', 'MEP.Lunatone_4'):
            with self.subTest(path=path):
                rig, e, ctx = self.ctx(path, 'Lunar Cycle')
                energy = self.add(rig, def_for(self.energies[PokemonTypes.FIGHTING.value]), P1, 'hand')
                self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
                self.add(rig, fixtures.definition('ME1.Solrock_75'), P1, 'bench')
                self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
                self.assertEqual(ctx.ability.shared_once_per_turn, 'Lunar Cycle')
                ctx.discard_from_hand = AsyncMock(return_value=[energy])
                ctx.draw_cards = AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.draw_cards.assert_awaited_once_with(3)
                ctx.discard_from_hand.return_value = []
                ctx.draw_cards.reset_mock()
                await ctx.ability.effect(ctx)
                ctx.draw_cards.assert_not_awaited()

    async def test_solar_transfer_filters_type_and_basic_on_both_printings(self):
        for path in ('ME1.MegaVenusaurex_3', 'MEP.MegaVenusaurex_13'):
            with self.subTest(path=path):
                rig, e, ctx = self.ctx(path, 'Solar Transfer')
                grass = self.add(rig, def_for(self.energies[PokemonTypes.GRASS.value]), P1, 'hand')
                fire = self.add(rig, def_for(self.energies[PokemonTypes.FIRE.value]), P1, 'hand')
                special = self.add(rig, fixtures.definition('HGSS1.RainbowEnergy_104'), P1, 'hand')
                rig.attach(grass, ctx.source)
                rig.attach(fire, ctx.source)
                rig.attach(special, ctx.source)
                self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
                ctx.move_energy_freely = AsyncMock()
                await ctx.ability.effect(ctx)
                predicate = ctx.move_energy_freely.call_args.kwargs['predicate']
                self.assertTrue(predicate(grass))
                self.assertFalse(predicate(fire))
                self.assertFalse(predicate(special))
                self.assertEqual(ctx.move_energy_freely.call_args.kwargs['max_count'], 1)
                # The shared interpreter must preserve the same qualifier
                # for future imports, even when no bespoke alias is present.
                await bw_legacy_ability(ctx)
                predicate = ctx.move_energy_freely.call_args.kwargs['predicate']
                self.assertTrue(predicate(grass))
                self.assertFalse(predicate(fire))
                self.assertFalse(predicate(special))

    async def test_run_errand_shared_limit_blocks_an_unused_promo(self):
        rig, e, ctx = self.ctx('MEP.MegaKangaskhanex_25', 'Run Errand')
        self.assertEqual(ctx.ability.shared_once_per_turn, 'Run Errand')
        state = rig.session.turn_state
        entries = lambda: _ability_entries(rig.board, state, P1, rig.session.game_id, [ctx.source])
        self.assertTrue(entries())
        state.used_named_abilities.add('Run Errand')
        self.assertFalse(entries())
        state.used_named_abilities.clear()
        self.assertTrue(entries())

    async def test_other_imported_named_limits_are_preserved(self):
        for path, title in (('SM10.PersianGX_149', 'Cat Walk'),
                            ('SV3.Pidgeotex_164', 'Quick Search')):
            with self.subTest(path=path):
                ability = next(a for a in fixtures.definition(path).abilities if a.title == title)
                self.assertEqual(ability.shared_once_per_turn, title)

    async def test_quick_search_is_not_available_from_a_second_copy(self):
        rig, e, ctx = self.ctx('SV3.Pidgeotex_164', 'Quick Search')
        second = ctx.my_bench()[0]
        state = rig.session.turn_state
        entries = lambda: _ability_entries(rig.board, state, P1, rig.session.game_id, [second])
        self.assertTrue(entries())
        state.used_named_abilities.add('Quick Search')
        self.assertFalse(entries())

    async def test_excited_heal_requires_own_live_grass_modern_mega(self):
        rig, e, ctx = self.ctx('ME2.Ludicolo_7', 'Excited Heal')
        ctx.source.set_attribute(AttrID.HP, 50)
        legal = lambda: ctx.ability.condition(rig.board, P1, ctx.source)
        self.assertFalse(legal())
        mega = self.add(rig, fixtures.definition('ME1.MegaVenusaurex_3'), P2, 'bench')
        self.assertFalse(legal())
        rig.to_area(mega, P1, 'hand')
        self.assertFalse(legal())
        rig.to_area(mega, P1, 'bench')
        mega.owning_player_id = P1
        self.assertTrue(legal())
        mega.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        self.assertFalse(legal())
        mega.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
        ctx.choose_pokemon = AsyncMock(return_value=ctx.source)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.source.get_attribute(AttrID.HP), 110)


if __name__ == '__main__':
    unittest.main()
