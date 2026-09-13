import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from spirit.game.card_effects import bw_era


class AbilityDeckSearchTests(unittest.IsolatedAsyncioTestCase):
    async def test_scoundrel_ring_finds_three_non_hoopa_pokemon_ex(self):
        hoopa = object()
        rayquaza = object()
        keldeo = object()
        modern_ex = object()
        ordinary = object()
        deck = [hoopa, rayquaza, keldeo, modern_ex, ordinary]
        names = {
            hoopa: "Hoopa-EX",
            rayquaza: "Rayquaza-EX",
            keldeo: "Keldeo-EX",
            modern_ex: "Charizard ex",
            ordinary: "Snivy",
        }

        async def search_deck(predicate, count, minimum, prompt, reveal_result=False):
            self.assertEqual(3, count)
            self.assertEqual(0, minimum)
            self.assertTrue(reveal_result)
            return [card for card in deck if predicate(card)][:count]

        ctx = SimpleNamespace(
            ability=SimpleNamespace(
                title="Scoundrel Ring",
                trigger="on_play",
                game_text=(
                    "When you play this Pokémon from your hand onto your Bench, "
                    "you may search your deck for up to 3 Pokémon-EX (except for "
                    "Hoopa-EX), reveal them, and put them into your hand. Shuffle "
                    "your deck afterward."
                ),
            ),
            source=hoopa,
            hand=lambda: [],
            ask_yes_no=AsyncMock(return_value=True),
            search_deck=AsyncMock(side_effect=search_deck),
            put_in_hand=AsyncMock(),
            shuffle_deck=AsyncMock(),
        )

        with (
            patch.object(bw_era, "_name", side_effect=names.get),
            patch.object(
                bw_era, "_pokemon_ex",
                side_effect=lambda card: card in (hoopa, rayquaza, keldeo),
            ),
        ):
            await bw_era.bw_legacy_ability(ctx)

        ctx.ask_yes_no.assert_awaited_once()
        ctx.put_in_hand.assert_awaited_once_with(
            [rayquaza, keldeo], reveal=True,
        )
        ctx.shuffle_deck.assert_awaited_once()

    def test_uppercase_pokemon_ex_does_not_include_modern_ex(self):
        legacy = SimpleNamespace(archetype_id="legacy")
        modern = SimpleNamespace(archetype_id="modern")
        definitions = {
            "legacy": SimpleNamespace(subtypes=["Basic", "EX"]),
            "modern": SimpleNamespace(subtypes=["Basic", "ex"]),
        }

        with (
            patch.object(bw_era, "def_for", side_effect=definitions.get),
            patch.object(
                bw_era, "_name",
                side_effect=lambda card: (
                    "Rayquaza-EX" if card is legacy else "Charizard ex"
                ),
            ),
        ):
            self.assertTrue(bw_era._pokemon_ex(legacy))
            self.assertFalse(bw_era._pokemon_ex(modern))


if __name__ == "__main__":
    unittest.main()
