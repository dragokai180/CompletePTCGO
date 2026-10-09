"""Optional evolution triggers offer a choice before opening their effect UI."""
import unittest
from unittest.mock import AsyncMock, Mock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import PokemonTypes
from spirit.game.scripts.cards import loader
from spirit.tools.effect_smoke import P1


class OptionalEvolutionConfirmationTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_declining_frost_over_and_triple_gears_opens_no_picker(self):
        for path, title in (
                ('SWSH6.Froslass_36', 'Frost Over'),
                ('SWSH7.Froslass_226', 'Frost Over'),
                ('SWSH12.Klinklang_125', 'Triple Gears')):
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, title)
                ctx.ask_yes_no = AsyncMock(return_value=False)
                ctx.choose_cards = AsyncMock()
                ctx.search_deck = AsyncMock()
                ctx.attach_energy = AsyncMock()
                ctx.shuffle_deck = AsyncMock()

                await ctx.ability.effect(ctx)

                ctx.ask_yes_no.assert_awaited_once_with(f'Use {title}?')
                ctx.choose_cards.assert_not_awaited()
                ctx.search_deck.assert_not_awaited()
                ctx.attach_energy.assert_not_awaited()
                ctx.shuffle_deck.assert_not_awaited()
                self.assertTrue(ctx.suppress_announce)

    async def test_accepting_frost_over_offers_discard_energy(self):
        rig, _, ctx = self.ctx('SWSH6.Froslass_36', 'Frost Over')
        energy_def = loader.cards_by_guid[self.energies[PokemonTypes.WATER.value].lower()]
        energy = self.add(rig, energy_def, P1, 'discard')
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.choose_cards = AsyncMock(return_value=[energy])
        ctx.choose_pokemon = AsyncMock(return_value=ctx.source)
        ctx.attach_energy = AsyncMock(return_value=True)

        await ctx.ability.effect(ctx)

        ctx.choose_cards.assert_awaited_once()
        self.assertIn(energy, ctx.choose_cards.await_args.args[0])
        ctx.attach_energy.assert_awaited_once_with(energy, ctx.source)

    async def test_accepting_triple_gears_opens_deck_search(self):
        _, _, ctx = self.ctx('SWSH12.Klinklang_125', 'Triple Gears')
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.search_deck = AsyncMock(return_value=[])
        ctx.shuffle_deck = AsyncMock()

        await ctx.ability.effect(ctx)

        self.assertEqual(ctx.search_deck.await_args.kwargs['count'], 3)
        ctx.shuffle_deck.assert_awaited_once()

    async def test_declined_shared_trigger_does_not_announce(self):
        _, _, ctx = self.ctx('HGSS3.Weavile_25', 'Claw Snag')
        ctx.ask_yes_no = AsyncMock(return_value=False)
        ctx.choose_from_revealed_hand = AsyncMock()

        await ctx.ability.effect(ctx)

        ctx.ask_yes_no.assert_awaited_once_with('Use Claw Snag?')
        ctx.choose_from_revealed_hand.assert_not_awaited()
        self.assertTrue(ctx.suppress_announce)

    async def test_more_optional_entry_triggers_confirm_before_picker(self):
        cases = (
            ('SWSH4.Trumbeak_144', 'Charging Trumpet', None),
            ('SWSH8.Granbull_116', 'Dig Up', 'SWSH1.AirBalloon_156'),
            ('SWSH7.GalarianArticuno_63', 'Cruel Charge', PokemonTypes.PSYCHIC),
            ('SWSH7.GalarianZapdos_82', 'Strong Legs Charge', PokemonTypes.FIGHTING),
        )
        for path, title, card_to_add in cases:
            with self.subTest(card=path):
                rig, _, ctx = self.ctx(path, title)
                if isinstance(card_to_add, str):
                    self.add(rig, definition(card_to_add), P1, 'discard')
                elif card_to_add is not None:
                    energy_def = loader.cards_by_guid[
                        self.energies[card_to_add.value].lower()]
                    self.add(rig, energy_def, P1, 'hand')
                ctx.ask_yes_no = AsyncMock(return_value=False)
                ctx.deck_top = Mock(side_effect=AssertionError('deck opened'))
                ctx.choose_cards = AsyncMock()
                ctx.put_in_hand = AsyncMock()
                ctx.attach_energy = AsyncMock()
                ctx.shuffle_deck = AsyncMock()

                await ctx.ability.effect(ctx)

                ctx.ask_yes_no.assert_awaited_once_with(f'Use {title}?')
                ctx.deck_top.assert_not_called()
                ctx.choose_cards.assert_not_awaited()
                ctx.put_in_hand.assert_not_awaited()
                ctx.attach_energy.assert_not_awaited()
                ctx.shuffle_deck.assert_not_awaited()
                self.assertTrue(ctx.suppress_announce)

    async def test_accepting_charging_trumpet_looks_at_top_cards(self):
        _, _, ctx = self.ctx('SWSH4.Trumbeak_144', 'Charging Trumpet')
        cards = ctx.deck_top(3)
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.deck_top = Mock(return_value=cards)
        ctx.choose_cards = AsyncMock(return_value=[])
        ctx.shuffle_deck = AsyncMock()

        await ctx.ability.effect(ctx)

        ctx.deck_top.assert_called_once_with(3)
        ctx.choose_cards.assert_awaited_once()
        ctx.shuffle_deck.assert_awaited_once()
