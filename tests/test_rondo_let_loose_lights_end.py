"""Regression cases for damaged-Pokemon damage, hand resets, and typed shields."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.bw_era import _formula_damage, _norm
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import compute_damage
from spirit.tools.effect_smoke import P1, P2


class RondoLetLooseLightsEndTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    ctx = fixtures.HgssRulesTests.ctx
    rig = fixtures.HgssRulesTests.rig

    def formula(self, ctx):
        return _formula_damage(ctx, _norm(ctx.ability.game_text))

    def test_horrifying_rondo_counts_only_damaged_bench_pokemon(self):
        _, _, ctx = self.ctx('ME4.Gourgeistex_41', 'Horrifying Rondo')
        bench = ctx.my_bench()
        self.assertEqual(self.formula(ctx), 30)
        bench[0].set_attribute(AttrID.HP, bench[0].get_attribute(AttrID.HP) - 10)
        self.assertEqual(self.formula(ctx), 80)
        bench[1].set_attribute(AttrID.HP, bench[1].get_attribute(AttrID.HP) - 20)
        self.assertEqual(self.formula(ctx), 130)

    async def test_horrifying_rondo_attack_uses_the_filtered_total(self):
        _, _, ctx = self.ctx('ME4.Gourgeistex_41', 'Horrifying Rondo')
        bench = ctx.my_bench()
        bench[0].set_attribute(AttrID.HP, bench[0].get_attribute(AttrID.HP) - 10)
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        self.assertEqual(ctx.deal_damage.call_args.args[0], 80)

    def test_related_damaged_pokemon_formulas(self):
        _, _, ctx = self.ctx('BW11.Gallade_81', 'Pandemonium Blade')
        self.assertEqual(self.formula(ctx), 60)
        bench = ctx.my_bench()
        bench[0].set_attribute(AttrID.HP, bench[0].get_attribute(AttrID.HP) - 10)
        self.assertEqual(self.formula(ctx), 80)

        _, _, ctx = self.ctx('SM10.Stunfisk_56', 'Electric Trap')
        self.assertEqual(self.formula(ctx), 0)
        ctx.attacker.set_attribute(
            AttrID.HP, ctx.attacker.get_attribute(AttrID.HP) - 10)
        self.assertEqual(self.formula(ctx), 30)

    async def test_let_loose_resets_both_hands_to_four_cards(self):
        rig, entities, ctx = self.ctx('Promo_SM.Marshadow_85', 'Let Loose')
        rig.to_area(entities['target'], P1, 'bench')
        own_hand = list(ctx.hand(P1))
        opposing_hand = list(ctx.hand(P2))
        events = []

        async def shuffle(cards, player_id):
            events.append(('shuffle', player_id, list(cards)))

        async def draw(count, player_id):
            events.append(('draw', player_id, count))

        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.shuffle_into_deck = AsyncMock(side_effect=shuffle)
        ctx.draw_cards = AsyncMock(side_effect=draw)
        await ctx.ability.effect(ctx)

        self.assertEqual(events, [
            ('shuffle', P1, own_hand),
            ('shuffle', P2, opposing_hand),
            ('draw', P1, 4),
            ('draw', P2, 4),
        ])

    async def test_ilima_gives_each_player_their_own_coin(self):
        rig, entities = self.rig('SM1.Ilima_121', 'trainer')
        source = entities['target']
        rig.to_area(source, P1, 'discard')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.shuffle_into_deck = AsyncMock()
        ctx.flip_coins = AsyncMock(side_effect=[[True], [False]])
        ctx.draw_cards = AsyncMock()

        await fixtures.definition('SM1.Ilima_121').effect(ctx)

        self.assertEqual(
            [call.kwargs['player_id'] for call in ctx.flip_coins.call_args_list],
            [P1, P2])
        self.assertEqual(
            [(call.args[0], call.kwargs['player_id'])
             for call in ctx.draw_cards.call_args_list],
            [(6, P1), (3, P2)])
        self.assertEqual(ctx.shuffle_into_deck.await_count, 2)

    async def test_harlequin_uses_one_coin_for_both_draw_counts(self):
        for heads, expected in ((True, (5, 3)), (False, (3, 5))):
            with self.subTest(heads=heads):
                rig, entities = self.rig('RSV10PT5.Harlequin_83', 'trainer')
                source = entities['target']
                rig.to_area(source, P1, 'discard')
                ctx = EffectContext(rig.session, P1, source, None)
                ctx.shuffle_into_deck = AsyncMock()
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.draw_cards = AsyncMock()

                await fixtures.definition('RSV10PT5.Harlequin_83').effect(ctx)

                ctx.flip_coins.assert_awaited_once()
                self.assertEqual(
                    [(call.args[0], call.kwargs['player_id'])
                     for call in ctx.draw_cards.call_args_list],
                    [(expected[0], P1), (expected[1], P2)])
                self.assertEqual(ctx.shuffle_into_deck.await_count, 2)

    def test_lights_end_only_blocks_colorless_attackers(self):
        rig, entities = self.rig('Promo_SM.NecrozmaGX_58')
        target = entities['target']
        attacker = entities['p2_active']
        for pokemon_type, expected in (
            (PokemonTypes.PSYCHIC, 50),
            (PokemonTypes.FIRE, 50),
            (PokemonTypes.COLORLESS, 0),
        ):
            with self.subTest(pokemon_type=pokemon_type):
                attacker.set_attribute(AttrID.POKEMON_TYPES, [pokemon_type.value])
                result = compute_damage(
                    rig.board, attacker, target, 50,
                    ignore_weakness=True, ignore_resistance=True,
                )
                self.assertEqual(result.amount, expected)

    def test_other_typed_shields_respect_attacker_type(self):
        for path, protected_type, other_type in (
            ('SM1.Araquanid_46', PokemonTypes.FIRE, PokemonTypes.PSYCHIC),
            ('SV3.Bellibolt_78', PokemonTypes.LIGHTNING, PokemonTypes.FIRE),
        ):
            with self.subTest(path=path):
                rig, entities = self.rig(path)
                attacker = entities['p2_active']
                target = entities['target']
                for pokemon_type, expected in (
                    (protected_type, 0), (other_type, 50)):
                    attacker.set_attribute(AttrID.POKEMON_TYPES, [pokemon_type.value])
                    result = compute_damage(
                        rig.board, attacker, target, 50,
                        ignore_weakness=True, ignore_resistance=True,
                    )
                    self.assertEqual(result.amount, expected)


if __name__ == '__main__':
    unittest.main()
