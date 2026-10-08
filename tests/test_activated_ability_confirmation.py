import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from spirit.game.scripts.cards.SWSH1.Cinccino_147 import make_do
from spirit.game.scripts.cards.SWSH2.GalarianMeowth_126 import evolution_roar
from spirit.game.scripts.cards.SWSH6 import Gardevoir_61
from spirit.game.scripts.cards.SWSH6.GalarianArticunoV_58 import reconstitute
from spirit.game.scripts.cards.SWSH12.Gardevoir_69 import refinement
from spirit.game.scripts.cards.SWSH12.RegidragoVSTAR_136 import legacy_star as legacy_star_136
from spirit.game.scripts.cards.SWSH12.RegidragoVSTAR_201 import legacy_star as legacy_star_201


class ActivatedAbilityConfirmationTests(unittest.IsolatedAsyncioTestCase):
    async def test_shining_arcana_resolves_after_activation_without_yes_no(self):
        top = [object(), object()]
        ctx = SimpleNamespace(
            deck_top=lambda count: top,
            choose_cards=AsyncMock(return_value=[]),
            put_in_hand=AsyncMock(),
            ask_yes_no=AsyncMock(side_effect=AssertionError("redundant confirmation")),
        )

        with patch.object(Gardevoir_61, "is_basic_energy_card", return_value=False):
            await Gardevoir_61.shining_arcana(ctx)

        ctx.ask_yes_no.assert_not_awaited()
        ctx.choose_cards.assert_awaited_once()
        ctx.put_in_hand.assert_awaited_once_with(top, reveal=False)

    async def test_make_do_draws_after_discard_without_yes_no(self):
        ctx = SimpleNamespace(
            discard_from_hand=AsyncMock(return_value=[object()]),
            draw_cards=AsyncMock(),
            ask_yes_no=AsyncMock(side_effect=AssertionError("redundant confirmation")),
        )

        await make_do(ctx)

        ctx.ask_yes_no.assert_not_awaited()
        ctx.draw_cards.assert_awaited_once_with(2)

    async def test_legacy_star_discards_before_recovery_without_confirmation(self):
        for effect in (legacy_star_136, legacy_star_201):
            with self.subTest(effect=effect.__module__):
                top = [object(), object()]
                discard = [object()]

                async def discard_cards(cards):
                    self.assertEqual(cards, top)
                    discard.extend(cards)

                async def choose_cards(cards, count, *, minimum, prompt):
                    self.assertEqual(cards, discard)
                    self.assertEqual((count, minimum), (2, 0))
                    return [top[0]]

                ctx = SimpleNamespace(
                    deck_top=lambda count: top[:count],
                    discard_cards=AsyncMock(side_effect=discard_cards),
                    discard_pile=lambda: list(discard),
                    choose_cards=AsyncMock(side_effect=choose_cards),
                    put_in_hand=AsyncMock(),
                    ask_yes_no=AsyncMock(side_effect=AssertionError("redundant confirmation")),
                )

                await effect(ctx)

                ctx.ask_yes_no.assert_not_awaited()
                ctx.discard_cards.assert_awaited_once_with(top)
                ctx.choose_cards.assert_awaited_once()
                ctx.put_in_hand.assert_awaited_once_with([top[0]], reveal=False)

    async def test_cancelled_discard_does_not_grant_ability_benefit(self):
        for effect in (refinement, evolution_roar, reconstitute):
            with self.subTest(effect=effect.__name__):
                ctx = SimpleNamespace(
                    discard_from_hand=AsyncMock(return_value=[]),
                    draw_cards=AsyncMock(),
                    search_deck=AsyncMock(),
                )

                await effect(ctx)

                ctx.draw_cards.assert_not_awaited()
                ctx.search_deck.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
