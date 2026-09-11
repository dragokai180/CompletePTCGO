import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from spirit.game.card_effects.bw10 import red_signal, verdant_wind_cure
from spirit.game.attributes import AttrID, CardType, PokemonTypes
from spirit.game.data_utils import Ability, Triggers
from spirit.game.session import effects


class Bw10EnergyTriggerVisualTests(unittest.IsolatedAsyncioTestCase):
    async def test_engine_suppresses_every_message_less_energy_trigger(self):
        async def no_op(_ctx):
            return

        ability = Ability(
            "Conditional Energy Ability",
            effect=no_op,
            trigger=Triggers.ON_ENERGY_ATTACHED,
        )
        session = SimpleNamespace(
            board_state=object(),
            game_id="test-game",
            _opponent_id=lambda _player_id: "p2",
        )
        pokemon = SimpleNamespace()

        with (
            patch.object(effects, "ability_locked", return_value=False),
            patch.object(
                effects, "_send_ability_brackets", new_callable=AsyncMock,
            ) as send_brackets,
        ):
            ctx = await effects.resolve_triggered_ability(
                session, "p1", pokemon, ability,
            )

        self.assertTrue(ctx.suppress_announce)
        send_brackets.assert_awaited_once()

    async def test_engine_keeps_a_real_energy_trigger_visible(self):
        async def visible_effect(ctx):
            ctx._messages.append((None, {"type": "state-change"}, None))

        ability = Ability(
            "Effective Energy Ability",
            effect=visible_effect,
            trigger=Triggers.ON_ENERGY_ATTACHED,
        )
        session = SimpleNamespace(
            board_state=object(),
            game_id="test-game",
            _opponent_id=lambda _player_id: "p2",
        )

        with (
            patch.object(effects, "ability_locked", return_value=False),
            patch.object(
                effects, "_send_ability_brackets", new_callable=AsyncMock,
            ),
        ):
            ctx = await effects.resolve_triggered_ability(
                session, "p1", SimpleNamespace(), ability,
            )

        self.assertFalse(ctx.suppress_announce)

    async def test_verdant_wind_noop_does_not_announce(self):
        ctx = SimpleNamespace(
            suppress_announce=False,
            my_pokemon_in_play=lambda: [],
            cure_all_conditions=AsyncMock(),
        )

        await verdant_wind_cure(ctx)

        self.assertTrue(ctx.suppress_announce)
        ctx.cure_all_conditions.assert_not_awaited()

    async def test_verdant_wind_still_announces_a_real_cure(self):
        energy_attrs = {
            AttrID.CARD_TYPE: CardType.ENERGY.value,
            AttrID.ENERGY_INFO: {
                "options": [[PokemonTypes.GRASS.value]],
            },
        }
        grass_energy = SimpleNamespace(
            get_attribute=lambda attr: energy_attrs.get(attr),
        )
        pokemon = SimpleNamespace(children=[grass_energy])
        ctx = SimpleNamespace(
            suppress_announce=False,
            my_pokemon_in_play=lambda: [pokemon],
            cure_all_conditions=AsyncMock(return_value=True),
        )

        await verdant_wind_cure(ctx)

        self.assertFalse(ctx.suppress_announce)
        ctx.cure_all_conditions.assert_awaited_once_with(pokemon)

    async def test_red_signal_non_plasma_attachment_does_not_announce(self):
        source = object()
        ctx = SimpleNamespace(
            suppress_announce=False,
            attaching_player_id="p1",
            player_id="p1",
            energy_receiver=source,
            source=source,
            attached_energy=SimpleNamespace(get_attribute=lambda _attr: False),
            opponent_bench=lambda: [object()],
        )

        await red_signal(ctx)

        self.assertTrue(ctx.suppress_announce)


if __name__ == "__main__":
    unittest.main()
