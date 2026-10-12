"""Regression coverage for compound self-discard abilities and Stadium ownership."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import effective_retreat_cost
from spirit.tools.effect_smoke import P1, P2


class SelfDiscardAndStadiumOwnershipTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def stadium(self, rig, owner):
        stadium = self.add(rig, fixtures.definition('SV1.Mesagoza_178'), owner, 'hand')
        rig.board.move_card(
            stadium.entity_id,
            rig.board.find_global_area('activeStadium').entity_id,
        )
        stadium.owning_player_id = owner
        return stadium

    async def test_hyper_blower_discards_source_and_attachments_after_switch(self):
        rig, e = self.rig('SV4.IronBundle_56')
        source = next(p for p in rig.board.pokemon_in_play(P1)
                      if p is not e['target'] and p.archetype_id == e['target'].archetype_id)
        attachment = next(iter(rig.board.attached_energies(e['target'])))
        rig.attach(attachment, source)
        ability = next(a for a in fixtures.definition('SV4.IronBundle_56').abilities
                       if a.title == 'Hyper Blower')
        ctx = EffectContext(rig.session, P1, source, ability)
        old_active = ctx.opponent_active()
        replacement = ctx.opponent_bench()[0]
        ctx.choose_pokemon = AsyncMock(return_value=replacement)
        await ability.effect(ctx)
        self.assertIs(ctx.opponent_active(), replacement)
        self.assertIn(old_active, ctx.opponent_bench())
        self.assertIn(source, ctx.discard_pile())
        self.assertIn(attachment, ctx.discard_pile())

    async def test_hyper_blower_does_not_discard_without_switch(self):
        rig, e = self.rig('SV4.IronBundle_56')
        source = next(p for p in rig.board.pokemon_in_play(P1)
                      if p is not e['target'] and p.archetype_id == e['target'].archetype_id)
        for pokemon in list(rig.board.find_player_area(P2, 'bench').children):
            rig.to_area(pokemon, P2, 'discard')
        ability = next(a for a in fixtures.definition('SV4.IronBundle_56').abilities
                       if a.title == 'Hyper Blower')
        ctx = EffectContext(rig.session, P1, source, ability)
        await ability.effect(ctx)
        self.assertIn(source, ctx.my_bench())

    async def test_hyper_blower_does_not_discard_when_switch_is_blocked(self):
        rig, e = self.rig('SV4.IronBundle_56')
        source = next(p for p in rig.board.pokemon_in_play(P1)
                      if p is not e['target'] and p.archetype_id == e['target'].archetype_id)
        ability = next(a for a in fixtures.definition('SV4.IronBundle_56').abilities
                       if a.title == 'Hyper Blower')
        ctx = EffectContext(rig.session, P1, source, ability)
        ctx.choose_pokemon = AsyncMock(return_value=ctx.opponent_bench()[0])
        ctx.switch_active = AsyncMock(return_value=False)
        await ability.effect(ctx)
        self.assertIn(source, ctx.my_bench())

    async def test_mysterious_comet_discards_only_when_counter_is_placed(self):
        for placed in (0, 20):
            with self.subTest(placed=placed):
                rig, e, ctx = self.ctx('SV035.Starmie_121', 'Mysterious Comet')
                ctx.choose_cards = AsyncMock(return_value=[ctx.opponent_active()])
                ctx.deal_damage = AsyncMock(return_value=placed)
                await ctx.ability.effect(ctx)
                self.assertEqual(e['target'] in ctx.discard_pile(), bool(placed))

    async def test_stadium_retreat_requires_own_stadium(self):
        for path, title, printed in (
            ('SWSH45.Thwackey_12', 'Lay of the Land', 2),
            ('SM9.Squirtle_22', 'Floating Shell', 1),
        ):
            for owner in (None, P2, P1):
                with self.subTest(path=path, owner=owner):
                    rig, e = self.rig(path)
                    if owner:
                        self.stadium(rig, owner)
                    self.assertEqual(effective_retreat_cost(rig.board, e['target']),
                                     0 if owner == P1 else printed)

    async def test_magma_gain_requires_own_stadium(self):
        for path in ('SWSH10.HeatranVMAX_26', 'SWSH10.HeatranVMAX_191'):
            for owner in (None, P2, P1):
                with self.subTest(path=path, owner=owner):
                    rig, e, ctx = self.ctx(path, 'Magma Gain')
                    e['target'].set_attribute(AttrID.HP, 100)
                    if owner:
                        self.stadium(rig, owner)
                    self.assertEqual(ctx.ability.condition(rig.board, P1, e['target']),
                                     owner == P1)

    async def test_hand_block_requires_own_stadium(self):
        for owner in (P2, P1):
            with self.subTest(owner=owner):
                rig, e = self.rig('XY10.Barbaracle_23')
                self.stadium(rig, owner)
                passive = fixtures.definition('XY10.Barbaracle_23').abilities[0].passive
                energy = self.add(rig, fixtures.definition('SWSH1.AuroraEnergy_186'),
                                  P2, 'hand')
                self.assertEqual(passive.blocks_energy_attachment(
                    P2, energy, rig.board.active_pokemon(P2), e['target']),
                    owner == P1)

    async def test_generic_attack_bonus_requires_own_stadium(self):
        for path, title, base, bonus in (
            ('ME1.Dhelmise_18', 'Earthen Power', 30, 50),
            ('XY8.Mamoswine_82', 'Primordial Boom', 80, 40),
            ('SM12.BlackKyurem_61', 'Dazzling Blizzard', 100, 100),
            ('SM10.Dugtrio_86', 'Home Ground', 30, 60),
        ):
            for owner in (None, P2, P1):
                with self.subTest(path=path, owner=owner):
                    rig, e, ctx = self.ctx(path, title)
                    if owner:
                        self.stadium(rig, owner)
                    ctx.deal_damage = AsyncMock(return_value=0)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(ctx.deal_damage.await_args.args[0],
                                     base + (bonus if owner == P1 else 0))

    async def test_falkner_draws_extra_only_with_own_stadium(self):
        path = 'SV2.Falkner_180'
        for owner in (None, P2, P1):
            with self.subTest(owner=owner):
                rig, e = self.rig(path, 'trainer')
                if owner:
                    self.stadium(rig, owner)
                ctx = EffectContext(rig.session, P1, e['target'], None)
                ctx.draw_cards = AsyncMock()
                await fixtures.definition(path).effect(ctx)
                ctx.draw_cards.assert_awaited_once_with(4 if owner == P1 else 2)

    async def test_mamoswine_heals_only_with_opponents_stadium(self):
        path = 'XY8.Mamoswine_82'
        for owner in (P1, P2):
            with self.subTest(owner=owner):
                rig, e, ctx = self.ctx(path, 'Primordial Boom')
                self.stadium(rig, owner)
                e['target'].set_attribute(AttrID.HP, 100)
                before = e['target'].get_attribute(AttrID.HP)
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertEqual(e['target'].get_attribute(AttrID.HP),
                                 before + (40 if owner == P2 else 0))
