"""Real-board regressions for the community bug report and current TCG errata.

Rules references:
https://play.pokemon.com/en-us/resources/documents/tcg-errata/
https://asia.pokemon-card.com/sg/card-search/detail/25085/
"""

import unittest
from importlib import import_module
from unittest.mock import AsyncMock, patch

from spirit.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonTypes, SpecialConditions,
)
from spirit.game.card_effects.bw_era import bw_legacy_attack
from spirit.game.card_effects.pokemon import ally_ko_last_turn
from spirit.game.data_utils import Attack
from spirit.game.models.board import create_card_entity
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import (
    EffectContext, full_stack, is_basic_energy, resolve_attack,
)
from spirit.game.session.game_session import GameOver
from spirit.game.session.legal_actions import (
    _stadium_ability_entries, trainer_condition_met,
)
from spirit.game.session.passives import compute_damage, effective_max_hp
from spirit.tools.effect_smoke import (
    P1, P2, Rig, basic_energy_guids, pick_filler_basic, pick_filler_item,
)


def definition(path):
    return import_module("spirit.game.scripts.cards." + path).card


class ReportedCardRegressions(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        loader.load_all()
        cls.filler = pick_filler_basic()
        cls.energies = basic_energy_guids()
        cls.item = pick_filler_item()

    def rig(self, path, kind="pokemon"):
        rig = Rig(definition(path), self.filler, self.energies, self.item)
        entities = rig.setup(kind)
        for pid in (P1, P2):
            for pokemon in rig.board.pokemon_in_play(pid):
                pokemon.set_attribute(AttrID.HP, effective_max_hp(rig.board, pokemon))
        return rig, entities

    def add(self, rig, card_def, owner, zone):
        card = create_card_entity(loader.cards_by_guid[card_def.guid.lower()], owner)
        area = rig.board.find_global_area(zone) if zone == "activeStadium" \
            else rig.board.find_player_area(owner, zone)
        rig.board.add_card_to_area(card, area)
        card.owning_player_id = owner
        return card

    async def test_big_jump_promotes_after_returning_the_entire_stack(self):
        rig, e = self.rig("XY2.Lopunny_85")
        active = e["target"]
        stack = list(full_stack(active))
        bench = list(rig.board.find_player_area(P1, "bench").children)
        ability = definition("XY2.Lopunny_85").abilities[0]
        with patch.object(rig.session, "_promote_new_active",
                          wraps=rig.session._promote_new_active) as promote:
            ended = await rig.session._execute_use_ability(
                P1, active, {"selectableAction": {"actionID": ability.ability_id}},
            )
        promote.assert_awaited_once_with(P1)
        self.assertFalse(ended)
        self.assertIn(rig.board.active_pokemon(P1), bench)
        self.assertTrue(all(card in rig.board.find_player_area(P1, "hand").children
                            for card in stack))
        self.assertFalse(rig.session.turn_state.kos_suffered)

    async def test_big_jump_with_no_replacement_ends_the_game(self):
        rig, e = self.rig("XY2.Lopunny_85")
        for card in list(rig.board.find_player_area(P1, "bench").children):
            rig.to_area(card, P1, "deck")
        ability = definition("XY2.Lopunny_85").abilities[0]
        with self.assertRaises(GameOver):
            await rig.session._execute_use_ability(
                P1, e["target"], {"selectableAction": {"actionID": ability.ability_id}},
            )

    async def test_deck_and_cover_applies_both_conditions_and_shuffles_stack(self):
        rig, e = self.rig("BW5.Accelgor_11")
        stack = list(full_stack(e["target"]))
        attack = definition("BW5.Accelgor_11").abilities[1]
        await resolve_attack(rig.session, P1, e["target"], attack, attack.ability_id)
        conditions = e["p2_active"].get_attribute(AttrID.SPECIAL_CONDITIONS)
        for condition in (SpecialConditions.PARALYZED, SpecialConditions.POISONED):
            self.assertIn(CLIENT_SPECIAL_CONDITION_NAMES[condition], conditions)
        self.assertTrue(all(card in rig.board.find_player_area(P1, "deck").children
                            for card in stack))

    async def test_combined_conditions_obey_the_same_coin_clause(self):
        for heads in (True, False):
            with self.subTest(heads=heads):
                rig, e = self.rig("BW5.Accelgor_11")
                attack = Attack(
                    "Coin status", cost={}, damage=0,
                    game_text="Flip a coin. If heads, the Defending Pokémon is now Paralyzed and Poisoned.",
                    effect=bw_legacy_attack,
                )
                ctx = EffectContext(rig.session, P1, e["target"], attack)
                ctx.flip_coins = AsyncMock(return_value=[heads])
                await attack.effect(ctx)
                conditions = e["p2_active"].get_attribute(AttrID.SPECIAL_CONDITIONS) or []
                self.assertEqual(len(conditions), 2 if heads else 0)

    async def test_sand_slammer_is_automatic_and_only_from_active(self):
        rig, e = self.rig("BW7.Flygon_99")
        opponents = list(rig.board.pokemon_in_play(P2))
        hp = {card.entity_id: card.get_attribute(AttrID.HP) for card in opponents}
        with patch.object(EffectContext, "choose_cards", new=AsyncMock(
                side_effect=AssertionError("Sand Slammer must not ask for targets"))):
            await rig.session._run_pokemon_checkup(P1)
        for card in opponents:
            # The bench also contains a Flygon. It must not add another 10.
            self.assertEqual(card.get_attribute(AttrID.HP), hp[card.entity_id] - 10)
        rig.to_area(e["target"], P1, "deck")
        await rig.session._promote_new_active(P1)
        for flygon in list(rig.board.pokemon_in_play(P1)):
            if flygon.archetype_id == definition("BW7.Flygon_99").guid:
                rig.to_area(flygon, P1, "deck")
        await rig.session._promote_new_active(P1)
        await rig.session._run_pokemon_checkup(P1)
        for card in opponents:
            self.assertEqual(card.get_attribute(AttrID.HP), hp[card.entity_id] - 10)

    async def test_checkup_knockouts_never_enable_flip_the_script(self):
        for cause in ("sand", "poison", "burn"):
            with self.subTest(cause=cause):
                rig, e = self.rig("BW7.Flygon_99" if cause == "sand"
                                  else "XY2.Lopunny_85")
                victim = e["p2_active"]
                victim.set_attribute(AttrID.HP, 10)
                if cause != "sand":
                    condition = SpecialConditions.POISONED if cause == "poison" \
                        else SpecialConditions.BURNED
                    ctx = EffectContext(rig.session, P1, e["target"], None)
                    await ctx.apply_special_condition(victim, condition)
                await rig.session._run_pokemon_checkup(P1)
                self.assertIn(victim, rig.board.find_player_area(P2, "discard").children)
                self.assertFalse(rig.session.turn_state.in_checkup)
                rig.session.turn_state.begin_turn(P2, rig.board)
                self.assertFalse(ally_ko_last_turn(rig.board, P2))

    async def test_in_turn_ability_ko_still_enables_flip_the_script(self):
        rig, e = self.rig("XY2.Lopunny_85")
        e["p2_active"].set_attribute(AttrID.HP, 10)
        ctx = EffectContext(rig.session, P1, e["target"], None)
        await ctx.deal_damage(10, e["p2_active"], as_counters=True, is_attack=False)
        await rig.session.resolve_knockouts(ctx)
        await rig.session._run_pokemon_checkup(P1)
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertTrue(ally_ko_last_turn(rig.board, P2))
        self.assertFalse(rig.session.turn_state.kos_by_attack_last_turn)

    async def test_checkup_phase_is_restored_after_exception(self):
        rig, _ = self.rig("XY2.Lopunny_85")
        async def fail(active_id):
            self.assertTrue(rig.session.turn_state.in_checkup)
            raise RuntimeError("test")
        with patch.object(rig.session, "_resolve_pokemon_checkup", side_effect=fail):
            with self.assertRaises(RuntimeError):
                await rig.session._run_pokemon_checkup(P1)
        self.assertFalse(rig.session.turn_state.in_checkup)

    async def test_tropical_beach_has_a_client_activation_for_both_players(self):
        for path in ("PROMO_BW.TropicalBeach_BW28", "PROMO_BW.TropicalBeach_BW50"):
            for player in (P1, P2):
                with self.subTest(path=path, player=player):
                    rig, e = self.rig(path, "trainer")
                    stadium = e["target"]
                    rig.board.move_card(stadium.entity_id,
                        rig.board.find_global_area("activeStadium").entity_id)
                    stadium.owning_player_id = P1
                    if player == P2:
                        rig.session.turn_state.begin_turn(P2, rig.board)
                    hand = rig.board.find_player_area(player, "hand")
                    for card in list(hand.children)[3:]:
                        rig.to_area(card, player, "deck")
                    entries = _stadium_ability_entries(rig.board,
                        rig.session.turn_state, player, rig.session.game_id)
                    self.assertEqual(len(entries), 1)
                    ability = definition(path).ability
                    self.assertIn(ability.ability_id, [entry["abilityID"]
                        for entry in stadium.get_attribute(AttrID.PIE_ABILITIES)])
                    self.assertTrue(await rig.session._execute_use_ability(
                        player, stadium, entries[0]))
                    self.assertEqual(len(hand.children), 7)
                    self.assertFalse(_stadium_ability_entries(rig.board,
                        rig.session.turn_state, player, rig.session.game_id))

    async def test_power_connect_only_boosts_plasma_attacks_to_active(self):
        for path in ("BW9.DeoxysEX_53", "BW9.DeoxysEX_111", "PROMO_BW.DeoxysEX_BW82"):
            with self.subTest(path=path):
                rig, e = self.rig("BW9.ThundurusEX_38")
                deoxys = self.add(rig, definition(path), P1, "bench")
                bench = rig.board.find_player_area(P2, "bench").children[0]
                def damage(attacker, target):
                    return compute_damage(rig.board, attacker, target, 50,
                                          apply_modifiers=False).amount
                self.assertEqual(damage(e["target"], e["p2_active"]), 60)
                self.assertEqual(damage(e["target"], bench), 50)
                self.assertEqual(damage(deoxys, e["p2_active"]), 50)
                self.assertEqual(damage(e["p2_active"], e["target"]), 50)
                self.add(rig, definition(path), P1, "bench")
                self.assertEqual(damage(e["target"], e["p2_active"]), 70)
                self.assertEqual(damage(e["target"], bench), 50)
                self.assertEqual(damage(deoxys, e["p2_active"]), 50)

    async def test_sacred_ash_all_prints_accept_one_to_five(self):
        for path in ("XY2.SacredAsh_96", "SV10.SacredAsh_168", "ME3.SacredAsh_115"):
            for count in (0, 1, 4, 5, 6):
                with self.subTest(path=path, count=count):
                    rig, e = self.rig(path, "trainer")
                    pool = [self.add(rig, self.filler, P1, "discard") for _ in range(count)]
                    self.assertEqual(trainer_condition_met(definition(path).condition, rig.board,
                                                         P1, e["target"]), count > 0)
                    ctx = EffectContext(rig.session, P1, e["target"], None)
                    ctx.choose_cards = AsyncMock(return_value=pool[:1])
                    await definition(path).effect(ctx)
                    if count:
                        args, kwargs = ctx.choose_cards.call_args
                        self.assertEqual(args[1], min(5, count))
                        self.assertEqual(kwargs["minimum"], 1)
                        self.assertIn(pool[0], rig.board.find_player_area(P1, "deck").children)
                        self.assertTrue(all(c in ctx.discard_pile() for c in pool[1:]))
                    else:
                        ctx.choose_cards.assert_not_awaited()

    async def test_retrieval_errata_allows_fewer_and_excludes_discard_cost(self):
        for path, cap in (("BW1.EnergyRetrieval_92", 2),
                          ("BW9.SuperiorEnergyRetrieval_103", 4),
                          ("SV2.SuperiorEnergyRetrieval_189", 4)):
            with self.subTest(path=path):
                rig, e = self.rig(path, "trainer")
                ctx = EffectContext(rig.session, P1, e["target"], None)
                original = [card for card in ctx.discard_pile() if is_basic_energy(card)]
                cost = [card for card in ctx.hand() if is_basic_energy(card)][:2]
                async def pay(*args, **kwargs):
                    await ctx.discard_cards(cost)
                    return cost
                ctx.discard_from_hand = AsyncMock(side_effect=pay)
                ctx.choose_cards = AsyncMock(return_value=original[:1])
                await definition(path).effect(ctx)
                args, kwargs = ctx.choose_cards.call_args
                self.assertEqual(args[1], cap)
                self.assertLessEqual(kwargs["minimum"], 1)
                self.assertTrue(all(card not in args[0] for card in cost))
                self.assertIn(original[0], ctx.hand())
                self.assertTrue(all(card in ctx.discard_pile() for card in original[1:]))

    async def test_double_thread_errata_bench_only_with_weakness(self):
        rig, e = self.rig("XY11.Galvantula_42")
        active_hp = e["p2_active"].get_attribute(AttrID.HP)
        bench = list(rig.board.find_player_area(P2, "bench").children)
        attack_type = e["target"].get_attribute(AttrID.POKEMON_TYPES)[0]
        before = [card.get_attribute(AttrID.HP) for card in bench]
        for card in bench:
            card.set_attribute(AttrID.WEAKNESS_TYPES, [attack_type])
            card.set_attribute(AttrID.WEAKNESS_AMOUNT, 2)
            card.set_attribute(AttrID.RESISTANCE_TYPES, PokemonTypes.UNSET.value)
        attack = definition("XY11.Galvantula_42").abilities[0]
        await resolve_attack(rig.session, P1, e["target"], attack, attack.ability_id)
        self.assertEqual(e["p2_active"].get_attribute(AttrID.HP), active_hp)
        for card, hp in zip(bench, before):
            self.assertEqual(card.get_attribute(AttrID.HP), hp - 60)

    async def test_other_recovery_errata_still_allow_partial_selection(self):
        for path, candidate_path, cap in (
            ("BW3.SuperRod_95", "XY2.Lopunny_85", 3),
            ("XY2.PalPad_92", "BW8.Colress_118", 2),
            ("XY7.EnergyRecycler_72", None, 5),
        ):
            with self.subTest(path=path):
                rig, e = self.rig(path, "trainer")
                if candidate_path:
                    chosen = self.add(rig, definition(candidate_path), P1, "discard")
                    self.add(rig, definition(candidate_path), P1, "discard")
                else:
                    chosen = next(card for card in rig.board.find_player_area(
                        P1, "discard").children if is_basic_energy(card))
                ctx = EffectContext(rig.session, P1, e["target"], None)
                ctx.choose_cards = AsyncMock(return_value=[chosen])
                await definition(path).effect(ctx)
                args, kwargs = ctx.choose_cards.call_args
                self.assertEqual(args[1], cap)
                self.assertLessEqual(kwargs["minimum"], 1)
                self.assertIn(chosen, rig.board.find_player_area(P1, "deck").children)

    async def test_cinderace_errata_retreat_is_one(self):
        rig, e = self.rig("SWSH1.Cinderace_36")
        self.assertEqual(e["target"].get_attribute(AttrID.RETREAT_COST), 1)


if __name__ == "__main__":
    unittest.main()
