"""Invalid powers must not be offered, even without generated conditions."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID
from spirit.game.data_utils import CARD_DEFS_BY_GUID, Activations
from spirit.game.card_effects.standard_era import ability_position_allowed
from spirit.game.session.legal_actions import _ability_entries, compute_legal_actions
from spirit.game.session.passives import effective_max_hp
from spirit.tools.effect_smoke import P1, P2, Rig


class AbilityMenuPermissionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def offered(self, rig, source, ability):
        return any(e['entityID'] == source.entity_id and
                   e['selectableAction']['actionID'] == ability.ability_id
                   for e in compute_legal_actions(rig.board, rig.session.turn_state,
                                                 P1, rig.session.game_id))

    async def test_portrait_and_forest_breath_are_not_offered_on_bench(self):
        for path, title in [('HGSS3.Smeargle_8', 'Portrait'),
                            ('COL.Smeargle_21', 'Portrait'),
                            ('HGSS4.Celebi_92', 'Forest Breath')]:
            for condition in (None, lambda *args: True):
                with self.subTest(path=path, condition=condition):
                    rig, e, ctx = self.ctx(path, title)
                    with patch.object(ctx.ability, 'condition', condition):
                        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
                        rig.to_area(ctx.source, P1, 'bench')
                        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))

    async def test_invalid_click_does_not_consume_power_or_run_effect(self):
        for path, title in [('HGSS3.Smeargle_8', 'Portrait'),
                            ('HGSS4.Celebi_92', 'Forest Breath')]:
            rig, e, ctx = self.ctx(path, title)
            rig.to_area(ctx.source, P1, 'bench')
            with patch.object(ctx.ability, 'condition', None), patch(
                'spirit.game.session.game_session.resolve_activated_ability',
                new_callable=AsyncMock,
            ) as resolve:
                self.assertFalse(await rig.session._execute_use_ability(
                    P1, ctx.source,
                    {'selectableAction': {'actionID': ctx.ability.ability_id}}))
                resolve.assert_not_awaited()
                self.assertNotIn((ctx.source.entity_id, ctx.ability.ability_id),
                                 rig.session.turn_state.used_abilities)

    async def test_forest_breath_requires_grass_energy_even_without_callback(self):
        rig, e, ctx = self.ctx('HGSS4.Celebi_92', 'Forest Breath')
        with patch.object(ctx.ability, 'condition', None):
            self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
            for card in list(ctx.hand()):
                rig.to_area(card, P1, 'deck')
            self.assertFalse(self.offered(rig, ctx.source, ctx.ability))

    async def test_power_status_restrictions_survive_missing_callback(self):
        rig, e, ctx = self.ctx('HGSS3.Smeargle_8', 'Portrait')
        with patch.object(ctx.ability, 'condition', None):
            for condition in ['Asleep', 'Burned', 'Confused', 'Paralyzed', 'Poisoned']:
                ctx.source.set_attribute(AttrID.SPECIAL_CONDITIONS, [condition])
                self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
            ctx.source.set_attribute(AttrID.SPECIAL_CONDITIONS, [])
            self.assertTrue(self.offered(rig, ctx.source, ctx.ability))

    async def test_tasting_bench_bonus_is_not_an_active_only_requirement(self):
        rig, e, ctx = self.ctx('XY4.Slurpuff_69', 'Tasting')
        rig.to_area(ctx.source, P1, 'bench')
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))

    async def test_active_only_catalog_does_not_depend_on_authored_conditions(self):
        checked = 0
        for card_def in list(CARD_DEFS_BY_GUID.values()):
            abilities = [a for a in getattr(card_def, 'abilities', ())
                         if a.activation in (Activations.UNLIMITED, Activations.ONCE_PER_TURN)
                         and 'active' in a.game_text.casefold()]
            if not abilities:
                continue
            rig = Rig(card_def, self.filler, self.energies, self.item)
            source = rig.setup('pokemon')['target']
            rig.to_area(source, P1, 'bench')
            for ability in abilities:
                if ability_position_allowed(rig.board, P1, source, ability.game_text):
                    continue
                checked += 1
                with self.subTest(set=card_def.set_code, title=ability.title), \
                     patch.object(ability, 'condition', lambda *args: True):
                    entries = _ability_entries(rig.board, rig.session.turn_state,
                                               P1, rig.session.game_id, [source])
                    self.assertFalse(any(e['selectableAction']['actionID'] == ability.ability_id
                                         for e in entries))
        self.assertGreaterEqual(checked, 100)

    async def test_unown_hand_threshold(self):
        rig, e, ctx = self.ctx('SM8.Unown_91', 'HAND')
        while len(ctx.hand()) < 34:
            self.add(rig, self.filler, P1, 'hand')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        card = self.add(rig, self.filler, P1, 'hand')
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
        rig.to_area(card, P1, 'deck')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))

    async def test_unown_damage_counts_only_bench_and_exact_threshold(self):
        rig, e, ctx = self.ctx('SM8.Unown_90', 'DAMAGE')
        for card in list(ctx.my_bench()):
            rig.to_area(card, P1, 'deck')
        targets = [self.add(rig, definition('SWSH6.BlisseyV_119'), P1, 'bench')
                   for _ in range(3)]
        for card in targets:
            card.set_attribute(AttrID.HP, effective_max_hp(rig.board, card) - 220)
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
        targets[0].set_attribute(AttrID.HP, targets[0].get_attribute(AttrID.HP) + 10)
        ctx.source.set_attribute(AttrID.HP, effective_max_hp(rig.board, ctx.source) - 10)
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))

    async def test_unown_missing_counts_only_opposing_lost_supporters(self):
        rig, e, ctx = self.ctx('SM8.Unown_92', 'MISSING')
        supporter = definition('BW1.ProfessorJuniper_101')
        for _ in range(12):
            self.add(rig, supporter, P1, 'lostZone')
        for _ in range(11):
            self.add(rig, supporter, P2, 'lostZone')
        self.add(rig, self.filler, P2, 'lostZone')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        ctx.win_game = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.win_game.assert_not_awaited()
        self.add(rig, supporter, P2, 'lostZone')
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
        await ctx.ability.effect(ctx)
        ctx.win_game.assert_awaited_once()


if __name__ == '__main__':
    unittest.main()
