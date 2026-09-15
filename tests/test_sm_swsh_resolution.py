"""Integration cases for GX knockouts, searches, and private inspection."""
import unittest
from importlib import import_module
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1, P2


class SmSwshResolutionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_altered_creation_extra_prize_through_actual_ko_resolution(self):
        rig, e, ctx = self.ctx('SM12.ArceusDialgaPalkiaGX_156', 'Altered Creation-GX')
        for kind in (PokemonTypes.METAL, PokemonTypes.WATER):
            rig.attach_energy_type(P1, ctx.attacker, kind.value)
        await ctx.ability.effect(ctx)
        prizes = rig.board.find_player_area(P1, 'prizePile')
        before = len(prizes.children)
        ctx.defender.set_attribute(AttrID.HP, 10)
        await ctx.deal_damage(100)
        await rig.session.resolve_knockouts(ctx)
        self.assertEqual(len(prizes.children), before - 2)

    async def test_one_card_inspection_still_shows_card_privately(self):
        cases = [
            ('SWSH1.Orbeetle_19', 'bugs_radar', P2),
            ('SWSH3.Lunatone_72', 'future_sight', P1),
            ('SWSH3.Gothita_73', 'fortunate_eye', P2),
            ('SWSH11.Porygon_140', 'branch_calculation', P1),
            ('SWSH4.Duskull_69', 'future_sight', P1),
        ]
        for path, function, owner in cases:
            with self.subTest(card=path):
                rig, e = self.rig(path)
                ctx = EffectContext(rig.session, P1, e['target'], None)
                for card in list(ctx.deck(owner))[1:]:
                    rig.to_area(card, owner, 'discard')
                ctx.choose = AsyncMock(return_value=0)
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.reveal_cards = AsyncMock()
                await getattr(import_module('spirit.game.scripts.cards.' + path), function)(ctx)
                ctx.reveal_cards.assert_awaited_once_with(ctx.deck_top(1, owner), to_player=P1)

    async def test_arc_phone_never_offers_face_up_prize(self):
        rig, e = self.rig('SWSH11.ArcPhone_152', 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        prizes = rig.board.find_player_area(P1, 'prizePile').children
        for card in prizes:
            card.publicly_revealed = True
        ctx.present_card_choice = AsyncMock(return_value=0)
        rig.session._prompt_prize_pick = AsyncMock(return_value=[])
        await fixtures.definition('SWSH11.ArcPhone_152').effect(ctx)
        rig.session._prompt_prize_pick.assert_not_awaited()
        prizes[-1].publicly_revealed = False
        await fixtures.definition('SWSH11.ArcPhone_152').effect(ctx)
        self.assertEqual(rig.session._prompt_prize_pick.call_args.args[1], [prizes[-1].entity_id])

    async def test_rainbow_brush_failed_search_keeps_original_energy(self):
        for succeeds in (False, True):
            rig, e = self.rig('SM7.RainbowBrush_141', 'trainer')
            ctx = EffectContext(rig.session, P1, e['target'], None)
            target = ctx.my_active()
            old = rig.pull_guid(P1, self.energies[PokemonTypes.WATER.value])
            rig.attach(old, target)
            new = rig.pull_guid(P1, self.energies[PokemonTypes.FIRE.value])
            ctx.choose_cards = AsyncMock(return_value=[old])
            ctx.search_deck = AsyncMock(return_value=[new] if succeeds else [])
            await fixtures.definition('SM7.RainbowBrush_141').effect(ctx)
            self.assertEqual(old in ctx.attached_energies(target), not succeeds)
            self.assertEqual(new in ctx.attached_energies(target), succeeds)
            if succeeds:
                self.assertIn(old, ctx.deck())


    async def test_conditional_evolution_abilities_pay_cost_then_evolve(self):
        for path, title, next_path, cost_path, count in (
            ('SM4.Karrablast_7', 'Shell On', 'SM4.Escavalier_69', 'SM4.Shelmet_8', 1),
            ('SM12.Duskull_83', 'Spiritborne Evolution', 'SM12.Dusclops_84', None, 3),
        ):
            rig, e, ctx = self.ctx(path, title)
            for card in list(ctx.hand()):
                rig.to_area(card, P1, 'deck')
            costs = [self.add(rig, fixtures.definition(cost_path) if cost_path else self.item,
                              P1, 'hand') for _ in range(count)]
            evolution = self.add(rig, fixtures.definition(next_path), P1, 'deck')
            ctx.search_deck = AsyncMock(return_value=[evolution])
            await ctx.ability.effect(ctx)
            self.assertTrue(all(card in ctx.discard_pile() for card in costs), title)
            self.assertIn(evolution, ctx.my_pokemon_in_play())
            self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)

    async def test_channeler_removes_attack_effects_not_other_passives(self):
        from spirit.game.session.passives import Passive
        rig, e = self.rig('SM11.Channeler_190', 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        attacked = Passive()
        ordinary = Passive()
        ctx.add_temporary_passive(ctx.my_active(), attacked)
        rig.board.temporary_passives[-1].from_attack = True
        ctx.add_temporary_passive(ctx.my_active(), ordinary)
        await fixtures.definition('SM11.Channeler_190').effect(ctx)
        remaining = [entry.passive for entry in rig.board.temporary_passives]
        self.assertNotIn(attacked, remaining)
        self.assertIn(ordinary, remaining)

    async def test_dusk_stone_requires_public_pre_evolution_not_hidden_match(self):
        definition = fixtures.definition('SM10.DuskStone_167')
        rig, e = self.rig('SM10.DuskStone_167', 'trainer')
        self.assertFalse(trainer_condition_met(definition.condition, rig.board, P1, e['target']))
        self.add(rig, fixtures.definition('SM10.Murkrow_108'), P1, 'bench')
        # The fixture has no Honchkrow in its deck; private failure remains legal.
        self.assertTrue(trainer_condition_met(definition.condition, rig.board, P1, e['target']))
