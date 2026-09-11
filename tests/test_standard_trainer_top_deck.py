import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock

from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.models.board import create_card_entity
from spirit.game.scripts.cards import loader as card_loader


P1 = "top-deck-p1"


class StandardTrainerTopDeckTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()

    @staticmethod
    def definition(set_code, collector_number):
        return next(
            definition for definition in CARD_DEFS_BY_GUID.values()
            if definition.set_code == set_code
            and definition.collector_number == collector_number
        )

    @staticmethod
    def entity(set_code, collector_number):
        definition = StandardTrainerTopDeckTests.definition(
            set_code, collector_number,
        )
        model = (
            card_loader.cards_by_guid.get(definition.guid)
            or card_loader.cards_by_guid[definition.guid.lower()]
        )
        return create_card_entity(model, P1)

    async def test_max_elixir_only_offers_basic_energy_from_the_top_six(self):
        max_elixir_def = self.definition("XY9", 102)
        max_elixir = self.entity("XY9", 102)
        basic_energy = self.entity("BW1", 105)
        second_basic_energy = self.entity("BW1", 106)
        special_energy = self.entity("BW4", 92)
        filler = [self.entity("BW1", 1) for _ in range(3)]
        viewed = [
            filler[0], special_energy, basic_energy,
            second_basic_energy, *filler[1:],
        ]
        bench_basic = self.entity("BW1", 15)

        choose_cards = AsyncMock(return_value=[basic_energy])
        ctx = SimpleNamespace(
            source=max_elixir,
            deck_top=lambda count: viewed[:count],
            choose_cards=choose_cards,
            my_bench=lambda: [bench_basic],
            my_pokemon_in_play=lambda: [bench_basic],
            choose_pokemon=AsyncMock(),
            attach_energy=AsyncMock(return_value=True),
            shuffle_deck=AsyncMock(),
        )

        await max_elixir_def.effect(ctx)

        offered = choose_cards.await_args.args[0]
        self.assertEqual(offered, [basic_energy, second_basic_energy])
        self.assertEqual(choose_cards.await_args.args[1], 1)
        self.assertEqual(choose_cards.await_args.kwargs["minimum"], 0)
        self.assertEqual(choose_cards.await_args.kwargs["display_cards"], viewed)
        ctx.attach_energy.assert_awaited_once_with(basic_energy, bench_basic)
        ctx.choose_pokemon.assert_not_awaited()
        ctx.shuffle_deck.assert_awaited_once()

    async def test_electric_generator_requires_basic_lightning_energy(self):
        generator_def = self.definition("SV1", 170)
        generator = self.entity("SV1", 170)
        lightning = self.entity("BW1", 108)
        grass = self.entity("BW1", 105)
        lightning_target = self.entity("BW1", 40)
        viewed = [grass, lightning]

        choose_cards = AsyncMock(return_value=[lightning])
        ctx = SimpleNamespace(
            source=generator,
            deck_top=lambda count: viewed[:count],
            choose_cards=choose_cards,
            my_bench=lambda: [lightning_target],
            my_pokemon_in_play=lambda: [lightning_target],
            choose_pokemon=AsyncMock(),
            attach_energy=AsyncMock(return_value=True),
            shuffle_deck=AsyncMock(),
        )

        await generator_def.effect(ctx)

        self.assertEqual(choose_cards.await_args.args[0], [lightning])
        ctx.attach_energy.assert_awaited_once_with(lightning, lightning_target)
        ctx.shuffle_deck.assert_awaited_once()

    async def test_acro_bike_discards_the_unselected_top_card(self):
        acro_bike_def = self.definition("XY5", 122)
        chosen = self.entity("BW1", 1)
        other = self.entity("BW1", 15)
        ctx = SimpleNamespace(
            source=self.entity("XY5", 122),
            deck_top=lambda _count: [chosen, other],
            choose_cards=AsyncMock(return_value=[chosen]),
            choose_card_groups=AsyncMock(),
            put_in_hand=AsyncMock(),
            discard_cards=AsyncMock(),
        )

        await acro_bike_def.effect(ctx)

        ctx.put_in_hand.assert_awaited_once_with([chosen], reveal=False)
        ctx.discard_cards.assert_awaited_once_with([other])

    async def test_mistys_determination_pays_its_cost_before_looking(self):
        misty_def = self.definition("XY9", 104)
        cost = self.entity("BW1", 1)
        picked = self.entity("BW1", 15)
        events = []

        async def discard_from_hand(*_args, **_kwargs):
            events.append("discard")
            return [cost]

        async def choose_cards(*_args, **_kwargs):
            events.append("choose")
            return [picked]

        ctx = SimpleNamespace(
            source=self.entity("XY9", 104),
            hand=lambda: [cost],
            discard_from_hand=discard_from_hand,
            deck_top=lambda _count: [picked],
            choose_cards=choose_cards,
            choose_card_groups=AsyncMock(),
            put_in_hand=AsyncMock(),
            shuffle_deck=AsyncMock(),
        )

        await misty_def.effect(ctx)

        self.assertEqual(events, ["discard", "choose"])
        ctx.put_in_hand.assert_awaited_once_with([picked], reveal=False)
        ctx.shuffle_deck.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()
