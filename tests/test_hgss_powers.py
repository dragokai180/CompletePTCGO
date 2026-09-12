"""HGSS copied effects and Energy movement use real board outcomes."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import granted_extra_attacks
from spirit.tools.effect_smoke import P1, P2


class PowerTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    ctx = fixtures.HgssRulesTests.ctx

    async def test_lost_link_reads_both_lost_zones_only(self):
        rig, e = self.rig('HGSS4.Mew_97')
        self.add(rig, definition('HGSS1.Pikachu_78'), P1, 'lostZone')
        self.add(rig, definition('HGSS1.Raichu_10'), P2, 'lostZone')
        self.add(rig, definition('HGSS3.Togepi_70'), P1, 'discard')
        # A LEGEND half has no usable attacks outside play (Lost Link FAQ).
        self.add(rig, definition('HGSS1.HoOhLEGEND_111'), P1, 'lostZone')
        attacks = granted_extra_attacks(rig.board, e['target'])
        titles = {a.title for a in attacks}
        self.assertIn('Quick Attack', titles)
        self.assertIn('Iron Tail', titles)
        self.assertNotIn('Plead', titles)
        self.assertNotIn('Bright Wing', titles)
        self.assertFalse(granted_extra_attacks(rig.board, rig.board.active_pokemon(P2)))

    async def test_evolution_memories_own_eeveelutions_only(self):
        rig, e = self.rig('HGSS3.Espeon_81')
        self.add(rig, definition('HGSS3.Leafeon_17'), P1, 'bench')
        self.add(rig, definition('HGSS3.Umbreon_86'), P2, 'bench')
        titles = {a.title for a in granted_extra_attacks(rig.board, e['target'])}
        self.assertIn('Miasma Wind', titles)
        self.assertNotIn('Evoblast', titles)

    async def test_portrait_uses_effect_without_moving_supporter(self):
        rig, e, ctx = self.ctx('HGSS3.Smeargle_8', 'Portrait')
        for card in list(ctx.hand(P2)):
            rig.to_area(card, P2, 'deck')
        bill = self.add(rig, definition('HGSS1.Bill_89'), P2, 'hand')
        hand = ctx.hand_size()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.hand_size(), hand + 2)
        self.assertIn(bill, ctx.hand(P2))
        self.assertIs(ctx.source, e['target'])

    async def test_portrait_cannot_copy_twins_with_equal_prizes(self):
        rig, e, ctx = self.ctx('HGSS3.Smeargle_8', 'Portrait')
        for card in list(ctx.hand(P2)):
            rig.to_area(card, P2, 'deck')
        self.add(rig, definition('HGSS4.Twins_89'), P2, 'hand')
        ctx.choose_cards = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.choose_cards.assert_not_awaited()

    async def test_transfer_eligibility_and_destinations(self):
        cases = [('HGSS2.Blastoise_13', 'Wash Out', PokemonTypes.WATER),
                 ('HGSS3.Raichu_83', 'Voltage Increase', PokemonTypes.LIGHTNING),
                 ('HGSS1.Meganium_109', 'Leaf Trans', PokemonTypes.GRASS),
                 ('HGSS2.Mismagius_5', 'Magical Trans', PokemonTypes.PSYCHIC)]
        for path, title, kind in cases:
            with self.subTest(title=title):
                rig, e, ctx = self.ctx(path, title)
                for pokemon in ctx.my_pokemon_in_play():
                    for energy in list(ctx.attached_energies(pokemon)):
                        rig.to_area(energy, P1, 'deck')
                self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
                donor = ctx.my_bench()[0]
                energy = rig.pull_guid(P1, self.energies[kind.value])
                rig.attach(energy, donor)
                self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
                ctx.move_energy_freely = AsyncMock()
                await ctx.ability.effect(ctx)
                sources, targets = ctx.move_energy_freely.call_args.args[:2]
                self.assertIn(donor, sources)
                if title in ('Wash Out', 'Voltage Increase'):
                    self.assertEqual(targets, [ctx.source])
                    self.assertNotIn(ctx.source, sources)

    async def test_active_volcano_attaches_actual_fire_only(self):
        for kind in (PokemonTypes.FIRE, PokemonTypes.WATER):
            rig, e, ctx = self.ctx('HGSS3.Slugma_67', 'Active Volcano')
            card = rig.pull_guid(P1, self.energies[kind.value])
            rig.to_area(card, P1, 'deck')
            self.assertIs(ctx.deck_top(1)[0], card)
            await ctx.ability.effect(ctx)
            self.assertIs(card.parent, ctx.source if kind == PokemonTypes.FIRE
                          else rig.board.find_player_area(P1, 'discard'))

    async def test_trick_reveal_shows_each_hand_to_other_player(self):
        rig, e, ctx = self.ctx('COL.MrMime_29', 'Trick Reveal')
        ctx.reveal_hand = AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        self.assertEqual([call.args for call in ctx.reveal_hand.call_args_list], [(P1, P2), (P2, P1)])
