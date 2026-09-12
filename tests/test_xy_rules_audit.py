"""XY semantic regressions using real card definitions."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.session.effects import EffectContext
from spirit.game.attributes import PokemonTypes
from spirit.game.session.passives import ability_locked, out_of_play_ability_locked
from spirit.game.card_effects.bw_era import _BWTurnShield
from spirit.tools.effect_smoke import P1, P2


class XyRulesAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_regice_shields_only_against_uppercase_EX(self):
        rig, e, ctx = self.ctx('XY7.Regice_24', 'Resistance Blizzard')
        ctx.add_passive_through_opponents_turn = Mock()
        await ctx.ability.effect(ctx)
        shield = ctx.add_passive_through_opponents_turn.call_args.args[1]
        for path, protected in [('BW1.Snivy_1', False),
                                ('BW7.KeldeoEX_49', True),
                                ('SV05.IronCrownex_81', False)]:
            with self.subTest(path=path):
                rig.to_area(rig.board.active_pokemon(P2), P2, 'bench')
                attacker = self.add(rig, definition(path), P2, 'activePokemonArea')
                calc = SimpleNamespace(target=ctx.attacker, attacker=attacker,
                                       is_attack=True, amount=40)
                self.assertEqual(shield.prevents_damage(calc, ctx.attacker), protected)
                self.assertEqual(shield.blocks_attack_effects(ctx.attacker, ctx.attacker), protected)

    async def test_ranger_does_not_shuffle(self):
        rig, e = self.rig('XY11.PokmonRanger_104', 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        ctx.shuffle_deck = AsyncMock()
        await definition('XY11.PokmonRanger_104').effect(ctx)
        ctx.shuffle_deck.assert_not_awaited()

    async def test_ranger_preserves_non_attack_temporary_effects(self):
        rig, e, attack = self.ctx('BW1.Snivy_1', 'Tackle')
        trainer = EffectContext(rig.session, P1, e['target'], None)
        attack.add_temporary_passive(attack.attacker, _BWTurnShield(prevent_all=True), 3)
        trainer.add_temporary_passive(attack.attacker, _BWTurnShield(amount=20), 3)
        kept = rig.board.temporary_passives[-1]
        await definition('XY11.PokmonRanger_104').effect(trainer)
        self.assertEqual(rig.board.temporary_passives, [kept])

    async def test_shadow_stitching_covers_opponent_including_later_arrivals(self):
        rig, e, ctx = self.ctx('XY9.Greninja_40', 'Shadow Stitching')
        await ctx.ability.effect(ctx)
        self.assertFalse(ability_locked(rig.board, ctx.attacker))
        self.assertTrue(ability_locked(rig.board, ctx.defender))
        for zone in ('hand', 'discard', 'bench'):
            target = self.add(rig, definition('BW1.Snivy_1'), P2, zone)
            check = ability_locked if zone == 'bench' else out_of_play_ability_locked
            self.assertTrue(check(rig.board, target))
        lock = rig.board.temporary_passives[-1]
        self.assertEqual(lock.expires_after_turn, rig.session.turn_state.turn_number + 1)
        await definition('XY11.PokmonRanger_104').effect(
            EffectContext(rig.session, P2, ctx.defender, None))
        self.assertFalse(ability_locked(rig.board, ctx.defender))

    async def test_moonlight_slash_bonus_requires_optional_return(self):
        for accept in (False, True):
            with self.subTest(accept=accept):
                rig, e, ctx = self.ctx('XY9.Greninja_40', 'Moonlight Slash')
                energy = rig.pull_guid(P1, self.energies[PokemonTypes.WATER.value])
                rig.attach(energy, ctx.attacker)
                ctx.choose_cards = AsyncMock(return_value=[energy] if accept else [])
                ctx.deal_damage = AsyncMock(return_value=60)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args_list[0].args[0], 80 if accept else 60)
                ctx.choose_cards.assert_awaited_once()
                self.assertEqual(energy in ctx.hand(), accept)
