import asyncio
import unittest
from unittest.mock import AsyncMock

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.data_utils import CARD_DEFS_BY_GUID, Attack, EnergyCardDef
from spirit.game.models.board import BoardState, create_card_entity
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.scripts.cards.SV07.Hydrappleex_14 import (
    ripening_charge, ripening_charge_condition, syrup_storm,
)
from spirit.game.session.constants import SelectionKind
from spirit.game.session.legal_actions import (
    ACTION_PLAY_STADIUM, TurnState, _retreat_entry, compute_legal_actions,
    trainer_condition_met,
)
from spirit.game.session.effects import resolve_attack
from spirit.game.session.passives import (
    ability_locked, compute_damage, conditions_blocked,
    effective_bench_capacity, effective_max_hp, energy_provided_options,
    trainer_play_blocked,
)
from spirit.game.card_effects.standard_era import (
    _trainer_energy_targets_on_board, hex_maniac_effect, karen_condition,
    steam_up, steam_up_condition,
)
from spirit.game.card_effects.bw_era import _ability_search_count


P1 = "playability-p1"
P2 = "playability-p2"


class PlayabilityConditionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()

    def setUp(self):
        self.board = BoardState("playability-test", [P1, P2])
        self.turn = TurnState()
        self.board.turn_state = self.turn
        self.turn.begin_turn(P1, self.board)
        self.turn.begin_turn(P2, self.board)
        self.turn.begin_turn(P1, self.board)

    @staticmethod
    def definition(set_code, collector_number):
        return next(
            definition for definition in CARD_DEFS_BY_GUID.values()
            if definition.set_code == set_code
            and definition.collector_number == collector_number
        )

    @staticmethod
    def card_model(definition):
        return (
            card_loader.cards_by_guid.get(definition.guid)
            or card_loader.cards_by_guid[definition.guid.lower()]
        )

    def add(self, definition, area_name):
        entity = create_card_entity(self.card_model(definition), P1)
        area = self.board.find_player_area(P1, area_name)
        self.board.add_card_to_area(entity, area)
        return entity

    def add_stadium(self, definition, owner=P1):
        entity = create_card_entity(self.card_model(definition), owner)
        self.board.add_card_to_area(
            entity, self.board.find_global_area("activeStadium")
        )
        # Global areas have no owner; the real Stadium executor restores the
        # player who played it immediately after moving the card there.
        entity.owning_player_id = owner
        return entity

    def fire_energy_definition(self):
        return next(
            definition for definition in CARD_DEFS_BY_GUID.values()
            if isinstance(definition, EnergyCardDef)
            and definition.energy_type == PokemonTypes.FIRE
        )

    def grass_energy_definition(self):
        return next(
            definition for definition in CARD_DEFS_BY_GUID.values()
            if isinstance(definition, EnergyCardDef)
            and definition.energy_type == PokemonTypes.GRASS
            and str(AttrID.IS_SPECIAL_ENERGY.value)
            not in definition.extra_attributes
        )

    def test_steam_up_requires_fire_energy_in_hand(self):
        volcanion = self.add(self.definition("XY11", 26), "bench")
        self.assertFalse(steam_up_condition(self.board, P1, volcanion))
        self.add(self.grass_energy_definition(), "hand")
        self.assertFalse(steam_up_condition(self.board, P1, volcanion))
        self.add(self.fire_energy_definition(), "hand")
        self.assertTrue(steam_up_condition(self.board, P1, volcanion))

    def test_steam_up_discards_fire_and_adds_basic_fire_modifier(self):
        fire = self.add(self.fire_energy_definition(), "hand")
        modifiers = []
        ctx = type("Ctx", (), {
            "board": self.board,
            "player_id": P1,
            "discard_from_hand": AsyncMock(return_value=[fire]),
            "add_turn_damage_modifier": modifiers.append,
        })()
        asyncio.run(steam_up(ctx))
        self.assertEqual(len(modifiers), 1)
        basic_fire = self.add(self.definition("BW1", 15), "bench")
        evolved_fire = self.add(self.definition("BW1", 17), "bench")
        self.assertTrue(modifiers[0].source_predicate(basic_fire))
        self.assertFalse(modifiers[0].source_predicate(evolved_fire))

    def test_karen_requires_a_discarded_pokemon_on_either_side(self):
        self.assertFalse(karen_condition(self.board, P1))
        self.add(self.definition("BW1", 1), "discard")
        self.assertTrue(karen_condition(self.board, P1))

    def test_hex_maniac_locks_abilities_through_opponents_next_turn(self):
        pokemon = self.add(self.definition("BW1", 1), "bench")
        ctx = type("Ctx", (), {
            "session": type("Session", (), {"turn_state": self.turn})(),
        })()
        asyncio.run(hex_maniac_effect(ctx))
        self.assertTrue(ability_locked(self.board, pokemon))
        self.turn.begin_turn(P2, self.board)
        self.assertTrue(ability_locked(self.board, pokemon))
        self.turn.begin_turn(P1, self.board)
        self.assertFalse(ability_locked(self.board, pokemon))

    def test_hex_maniac_disables_trevenants_forest_curse(self):
        trevenant_definition = self.definition("XY1", 55)
        trevenant = create_card_entity(
            self.card_model(trevenant_definition), P2,
        )
        self.board.add_card_to_area(
            trevenant,
            self.board.find_player_area(P2, "activePokemonArea"),
        )
        item = self.add(self.definition("XY1", 128), "hand")

        self.assertTrue(trainer_play_blocked(self.board, P1, item))
        ctx = type("Ctx", (), {
            "session": type("Session", (), {"turn_state": self.turn})(),
        })()
        asyncio.run(hex_maniac_effect(ctx))
        self.assertFalse(trainer_play_blocked(self.board, P1, item))

        self.turn.begin_turn(P2, self.board)
        self.assertFalse(trainer_play_blocked(self.board, P1, item))
        self.turn.begin_turn(P1, self.board)
        self.assertTrue(trainer_play_blocked(self.board, P1, item))

    def test_fighting_fury_belt_only_buffs_basic_pokemon(self):
        basic = self.add(self.definition("XY11", 26), "activePokemonArea")
        target = create_card_entity(
            self.card_model(self.definition("BW1", 1)), P2,
        )
        self.board.add_card_to_area(
            target, self.board.find_player_area(P2, "activePokemonArea"),
        )
        belt_def = self.definition("XY9", 99)
        belt = self.add(belt_def, "hand")
        self.board.attach_card(belt.entity_id, basic.entity_id)
        self.assertEqual(effective_max_hp(self.board, basic), 220)
        self.assertEqual(compute_damage(self.board, basic, target, 20).amount, 30)

        stage_one = self.add(self.definition("BW1", 3), "bench")
        self.board.attach_card(belt.entity_id, stage_one.entity_id)
        self.assertEqual(
            effective_max_hp(self.board, stage_one),
            stage_one.get_attribute(AttrID.HP),
        )
        self.assertEqual(compute_damage(self.board, stage_one, target, 20).amount, 20)

    def test_parallel_city_orientation_and_native_play_picker(self):
        definition = self.definition("XY8", 145)
        stadium = self.add_stadium(definition)

        stadium.set_attribute(AttrID.CARD_ORIENTATION, 0)
        self.assertEqual(effective_bench_capacity(self.board, P2), 3)
        self.assertGreater(effective_bench_capacity(self.board, P1), 3)
        stadium.set_attribute(AttrID.CARD_ORIENTATION, 1)
        self.assertEqual(effective_bench_capacity(self.board, P1), 3)
        self.assertGreater(effective_bench_capacity(self.board, P2), 3)

        # A second copy remains playable and its action opens the native
        # rotate-card node before replacing the first copy.
        incoming = self.add(definition, "hand")
        self.add(self.definition("BW1", 1), "activePokemonArea")
        entry = next(
            action for action in compute_legal_actions(
                self.board, self.turn, P1, "orientation-test"
            )
            if action["entityID"] == incoming.entity_id
            and action["selectableAction"]["description"] == ACTION_PLAY_STADIUM
        )
        self.assertEqual(
            entry["targetInfoLst"][0]["name"],
            SelectionKind.ORIENTATION_CUSTOM_CHOICE.value,
        )

    def test_reverse_valley_orientation_controls_each_side(self):
        stadium = self.add_stadium(self.definition("XY9", 110))
        attacker = self.add(self.definition("BW1", 1), "activePokemonArea")
        target = create_card_entity(
            self.card_model(self.definition("BW1", 15)), P2
        )
        self.board.add_card_to_area(
            target, self.board.find_player_area(P2, "activePokemonArea")
        )
        target.set_attribute(AttrID.WEAKNESS_TYPES, [])
        target.set_attribute(AttrID.RESISTANCE_TYPES, -1)

        stadium.set_attribute(AttrID.CARD_ORIENTATION, 0)
        attacker.set_attribute(
            AttrID.POKEMON_TYPES, [PokemonTypes.DARKNESS.value]
        )
        target.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
        self.assertEqual(compute_damage(self.board, attacker, target, 20).amount, 30)

        stadium.set_attribute(AttrID.CARD_ORIENTATION, 1)
        self.assertEqual(compute_damage(self.board, attacker, target, 20).amount, 20)

        attacker.set_attribute(
            AttrID.POKEMON_TYPES, [PokemonTypes.FIGHTING.value]
        )
        target.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.METAL.value])
        stadium.set_attribute(AttrID.CARD_ORIENTATION, 0)
        self.assertEqual(compute_damage(self.board, attacker, target, 20).amount, 10)
        stadium.set_attribute(AttrID.CARD_ORIENTATION, 1)
        self.assertEqual(compute_damage(self.board, attacker, target, 20).amount, 20)

    def test_chaos_tower_orientation_controls_condition_immunity(self):
        stadium = self.add_stadium(self.definition("XY10", 94))
        own = self.add(self.definition("BW1", 1), "activePokemonArea")
        opposing = create_card_entity(
            self.card_model(self.definition("BW1", 15)), P2
        )
        self.board.add_card_to_area(
            opposing, self.board.find_player_area(P2, "activePokemonArea")
        )

        stadium.set_attribute(AttrID.CARD_ORIENTATION, 0)
        self.assertTrue(conditions_blocked(
            self.board, own, SpecialConditions.ASLEEP
        ))
        self.assertFalse(conditions_blocked(
            self.board, own, SpecialConditions.CONFUSED
        ))
        self.assertTrue(conditions_blocked(
            self.board, opposing, SpecialConditions.POISONED
        ))

        stadium.set_attribute(AttrID.CARD_ORIENTATION, 1)
        self.assertTrue(conditions_blocked(
            self.board, own, SpecialConditions.CONFUSED
        ))
        self.assertFalse(conditions_blocked(
            self.board, own, SpecialConditions.ASLEEP
        ))

    def test_ultra_ball_requires_two_other_hand_cards(self):
        ultra_def = self.definition("CZ", 146)
        ultra = self.add(ultra_def, "hand")

        self.assertFalse(trainer_condition_met(
            ultra_def.condition, self.board, P1, ultra,
        ))
        self.add(self.definition("BW1", 1), "hand")
        self.assertFalse(trainer_condition_met(
            ultra_def.condition, self.board, P1, ultra,
        ))
        self.add(self.definition("BW1", 15), "hand")
        self.assertTrue(trainer_condition_met(
            ultra_def.condition, self.board, P1, ultra,
        ))

    def test_rare_candy_requires_matching_stage_two_in_hand(self):
        snivy = self.add(self.definition("BW1", 1), "activePokemonArea")
        rare_def = self.definition("CZ", 141)
        rare = self.add(rare_def, "hand")

        self.assertFalse(trainer_condition_met(
            rare_def.condition, self.board, P1, rare,
        ))
        self.add(self.definition("BW1", 5), "hand")
        self.assertTrue(trainer_condition_met(
            rare_def.condition, self.board, P1, rare,
        ))
        self.turn.mark_entered_play(snivy.entity_id)
        self.assertFalse(trainer_condition_met(
            rare_def.condition, self.board, P1, rare,
        ))

    def test_inferno_fandango_requires_fire_energy_in_hand(self):
        emboar_def = self.definition("BW1", 20)
        emboar = self.add(emboar_def, "activePokemonArea")
        ability = next(a for a in emboar_def.abilities
                       if a.title == "Inferno Fandango")

        self.assertFalse(ability.condition(self.board, P1, emboar))
        self.add(self.fire_energy_definition(), "hand")
        self.assertTrue(ability.condition(self.board, P1, emboar))

    def test_lanas_aid_requires_a_public_discard_target(self):
        lana_def = self.definition("SV06", 155)
        lana = self.add(lana_def, "hand")

        self.assertFalse(trainer_condition_met(
            lana_def.condition, self.board, P1, lana,
        ))
        self.add(self.definition("BW1", 1), "discard")
        self.assertTrue(trainer_condition_met(
            lana_def.condition, self.board, P1, lana,
        ))

    def test_night_stretcher_requires_a_public_discard_target(self):
        stretcher_def = self.definition("SV065", 61)
        stretcher = self.add(stretcher_def, "hand")

        self.assertFalse(trainer_condition_met(
            stretcher_def.condition, self.board, P1, stretcher,
        ))
        self.add(self.definition("BW1", 1), "discard")
        self.assertTrue(trainer_condition_met(
            stretcher_def.condition, self.board, P1, stretcher,
        ))

    def test_max_elixir_requires_a_basic_benched_target_and_nonempty_deck(self):
        max_elixir_def = self.definition("XY9", 102)
        max_elixir = self.add(max_elixir_def, "hand")
        self.add(self.definition("BW1", 1), "activePokemonArea")

        self.assertFalse(trainer_condition_met(
            max_elixir_def.condition, self.board, P1, max_elixir,
        ))
        self.add(self.definition("BW1", 105), "deck")
        self.assertFalse(trainer_condition_met(
            max_elixir_def.condition, self.board, P1, max_elixir,
        ))
        self.add(self.definition("BW1", 17), "bench")
        self.assertFalse(trainer_condition_met(
            max_elixir_def.condition, self.board, P1, max_elixir,
        ))
        self.add(self.definition("BW1", 15), "bench")
        self.assertTrue(trainer_condition_met(
            max_elixir_def.condition, self.board, P1, max_elixir,
        ))

    def test_mega_turbo_only_offers_mega_evolution_targets(self):
        self.add(self.definition("BW1", 1), "activePokemonArea")
        mega = self.add(self.definition("XY6", 61), "bench")
        self.add(self.definition("BW1", 15), "bench")

        targets = _trainer_energy_targets_on_board(
            self.board, P1,
            "attach a basic energy card from your discard pile to 1 of your "
            "mega evolution pokémon.",
        )

        self.assertEqual(targets, [mega])

    def test_power_heater_attaches_to_two_distinct_benched_pokemon(self):
        attack = next(
            ability for ability in self.definition("XY11", 25).abilities
            if ability.title == "Power Heater"
        )
        bench_a = self.add(self.definition("BW1", 1), "bench")
        bench_b = self.add(self.definition("BW1", 15), "bench")
        energy_a = self.add(self.fire_energy_definition(), "discard")
        energy_b = self.add(self.fire_energy_definition(), "discard")
        choose_cards = AsyncMock(side_effect=[
            [energy_a, energy_b],
            [bench_b, bench_a],
        ])
        attach_energy = AsyncMock(return_value=True)
        deal_damage = AsyncMock()
        discard = self.board.find_player_area(P1, "discard")
        bench = self.board.find_player_area(P1, "bench")
        ctx = type("Ctx", (), {
            "ability": attack,
            "deal_damage": deal_damage,
            "hand": lambda _self: [],
            "discard_pile": lambda _self: list(discard.children),
            "my_bench": lambda _self: list(bench.children),
            "choose_cards": choose_cards,
            "attach_energy": attach_energy,
        })()

        asyncio.run(attack.effect(ctx))

        deal_damage.assert_awaited_once_with(20)
        self.assertEqual(choose_cards.await_count, 2)
        energy_call, target_call = choose_cards.await_args_list
        self.assertEqual(
            {card.entity_id for card in target_call.args[0]},
            {bench_a.entity_id, bench_b.entity_id},
        )
        self.assertEqual(
            {card.entity_id for card in energy_call.args[0]},
            {energy_a.entity_id, energy_b.entity_id},
        )
        attached = {
            (call.args[0].entity_id, call.args[1].entity_id)
            for call in attach_energy.await_args_list
        }
        self.assertEqual(attached, {
            (energy_a.entity_id, bench_b.entity_id),
            (energy_b.entity_id, bench_a.entity_id),
        })

    def test_shared_ability_pays_typed_hand_cost_before_benefit(self):
        definition = self.definition("XY2", 7)
        ability = next(a for a in definition.abilities if a.title == "Leaf Draw")
        source = self.add(definition, "activePokemonArea")
        fire = self.add(self.fire_energy_definition(), "hand")
        grass = self.add(self.grass_energy_definition(), "hand")

        self.assertTrue(ability.condition(self.board, P1, source))
        discard_from_hand = AsyncMock(return_value=[grass])
        draw_cards = AsyncMock()
        ctx = type("Ctx", (), {
            "ability": ability,
            "source": source,
            "hand": lambda _self: [fire, grass],
            "discard_from_hand": discard_from_hand,
            "draw_cards": draw_cards,
        })()

        asyncio.run(ability.effect(ctx))

        discard_from_hand.assert_awaited_once()
        self.assertFalse(discard_from_hand.await_args.kwargs["predicate"](fire))
        self.assertTrue(discard_from_hand.await_args.kwargs["predicate"](grass))
        draw_cards.assert_awaited_once_with(3)

    def test_clairvoyant_sense_requires_energy_and_bench_target(self):
        definition = self.definition("SV4", 72)
        source = self.add(definition, "activePokemonArea")
        ability = next(
            a for a in definition.abilities if a.title == "Clairvoyant Sense"
        )
        self.assertFalse(ability.condition(self.board, P1, source))
        self.add(self.definition("BW1", 1), "bench")
        self.assertFalse(ability.condition(self.board, P1, source))
        psychic = next(
            definition for definition in CARD_DEFS_BY_GUID.values()
            if isinstance(definition, EnergyCardDef)
            and definition.energy_type == PokemonTypes.PSYCHIC
            and str(AttrID.IS_SPECIAL_ENERGY.value)
            not in definition.extra_attributes
        )
        self.add(psychic, "hand")
        self.assertTrue(ability.condition(self.board, P1, source))

    def test_deck_energy_search_preserves_up_to_quantity(self):
        self.assertEqual(_ability_search_count(
            "search your deck for up to 2 basic energy cards and attach them "
            "to your pokémon in any way you like."
        ), 2)

    def test_burning_road_requires_move_from_bench_to_active_this_turn(self):
        for set_code, collector_number in (("XY12", 18), ("SM11", 25)):
            with self.subTest(set_code=set_code):
                definition = self.definition(set_code, collector_number)
                pokemon = self.add(definition, "bench")
                ability = next(
                    ability for ability in definition.abilities
                    if ability.title == "Burning Road"
                )
                active = self.board.active_pokemon(P1)
                if active is None:
                    active = self.add(
                        self.definition("BW1", 1), "activePokemonArea"
                    )
                energy = self.add(self.fire_energy_definition(), "hand")
                self.board.attach_card(energy.entity_id, active.entity_id)

                self.assertFalse(ability.condition(self.board, P1, pokemon))
                bench = self.board.find_player_area(P1, "bench")
                self.board.move_card(active.entity_id, bench.entity_id)
                self.board.move_card(
                    pokemon.entity_id,
                    self.board.find_player_area(P1, "activePokemonArea").entity_id,
                )
                self.assertFalse(ability.condition(self.board, P1, pokemon))
                self.turn.became_active_turn[pokemon.entity_id] = \
                    self.turn.turn_number
                self.assertTrue(ability.condition(self.board, P1, pokemon))

    def test_burning_road_only_moves_fire_energy(self):
        definition = self.definition("SM11", 25)
        source = self.add(definition, "activePokemonArea")
        ability = next(
            ability for ability in definition.abilities
            if ability.title == "Burning Road"
        )
        other = self.add(self.definition("BW1", 1), "bench")
        move_energy_freely = AsyncMock(return_value=[])
        ctx = type("Ctx", (), {
            "ability": ability,
            "source": source,
            "hand": lambda _self: [],
            "my_pokemon_in_play": lambda _self: [source, other],
            "move_energy_freely": move_energy_freely,
        })()

        asyncio.run(ability.effect(ctx))

        move_energy_freely.assert_awaited_once()
        call = move_energy_freely.await_args
        self.assertEqual(call.args[0], [other])
        self.assertEqual(call.args[1], [source])
        self.assertTrue(call.kwargs["predicate"](
            self.add(self.fire_energy_definition(), "hand")
        ))
        self.assertFalse(call.kwargs["predicate"](
            self.add(self.grass_energy_definition(), "hand")
        ))

    def test_geomancy_distributes_energy_to_two_distinct_bench_targets(self):
        attack = next(
            ability for ability in self.definition("XY1", 96).abilities
            if ability.title == "Geomancy"
        )
        bench_a = self.add(self.definition("BW1", 1), "bench")
        bench_b = self.add(self.definition("BW1", 15), "bench")
        energy_a = self.add(self.grass_energy_definition(), "deck")
        energy_b = self.add(self.grass_energy_definition(), "deck")
        choose_pokemon = AsyncMock(return_value=bench_b)
        search_deck = AsyncMock(return_value=[energy_a, energy_b])
        attach_energy = AsyncMock(return_value=True)
        ctx = type("Ctx", (), {
            "ability": attack,
            "my_bench": lambda _self: [bench_a, bench_b],
            "choose_pokemon": choose_pokemon,
            "search_deck": search_deck,
            "attach_energy": attach_energy,
            "shuffle_deck": AsyncMock(),
        })()

        asyncio.run(attack.effect(ctx))

        attached_targets = [call.args[1] for call in attach_energy.await_args_list]
        self.assertEqual(attached_targets, [bench_b, bench_a])

    def test_energy_grace_knocks_out_source_and_uses_one_non_ex_target(self):
        attack = next(
            ability for ability in self.definition("XY2", 23).abilities
            if ability.title == "Energy Grace"
        )
        source = self.add(self.definition("XY2", 23), "bench")
        target = self.add(self.definition("BW1", 1), "bench")
        energies = [self.add(self.fire_energy_definition(), "discard")
                    for _ in range(3)]
        knock_out = AsyncMock()
        attach_energy = AsyncMock(return_value=True)
        ctx = type("Ctx", (), {
            "ability": attack,
            "source": source,
            "my_pokemon_in_play": lambda _self: [source, target],
            "discard_pile": lambda _self: energies,
            "choose_cards": AsyncMock(return_value=energies),
            "choose_pokemon": AsyncMock(return_value=target),
            "knock_out": knock_out,
            "attach_energy": attach_energy,
        })()

        asyncio.run(attack.effect(ctx))

        knock_out.assert_awaited_once_with(source)
        self.assertEqual(
            [call.args[1] for call in attach_energy.await_args_list],
            [target, target, target],
        )

    def test_both_volcanic_heat_printings_lock_the_next_turn(self):
        for collector_number in (26, 107):
            attack = next(
                ability for ability in self.definition(
                    "XY11", collector_number,
                ).abilities if ability.title == "Volcanic Heat"
            )
            self.assertTrue(attack.locks_next_turn)
            self.assertIsNotNone(attack.effect)
            self.assertIn("can't attack", attack.game_text.casefold())

    def test_xy_active_and_bench_ability_position_requirements(self):
        reshiram = self.add(self.definition("XY6", 63), "bench")
        turboblaze = next(
            ability for ability in self.definition("XY6", 63).abilities
            if ability.title == "Turboblaze"
        )
        self.add(self.fire_energy_definition(), "hand")
        self.assertFalse(turboblaze.condition(self.board, P1, reshiram))
        active = self.board.find_player_area(P1, "activePokemonArea")
        self.board.move_card(reshiram.entity_id, active.entity_id)
        self.assertTrue(turboblaze.condition(self.board, P1, reshiram))
        reshiram.set_attribute(AttrID.HP, 100)

        jynx = self.add(self.definition("XY3", 37), "bench")
        jynx.set_attribute(AttrID.HP, 70)
        victory_kiss = next(
            ability for ability in self.definition("XY3", 37).abilities
            if ability.title == "Victory Kiss"
        )
        self.assertTrue(victory_kiss.condition(self.board, P1, jynx))
        self.board.move_card(jynx.entity_id, active.entity_id)
        self.assertFalse(victory_kiss.condition(self.board, P1, jynx))

    def test_energy_grace_requires_and_targets_non_ex_pokemon(self):
        milotic = self.add(self.definition("XY2", 23), "bench")
        energy_grace = next(
            ability for ability in self.definition("XY2", 23).abilities
            if ability.title == "Energy Grace"
        )
        self.add(self.fire_energy_definition(), "discard")
        self.add(self.definition("XY6", 61), "bench")
        self.assertFalse(energy_grace.condition(self.board, P1, milotic))
        self.add(self.definition("BW1", 1), "bench")
        self.assertTrue(energy_grace.condition(self.board, P1, milotic))
        self.assertIn("EX", self.definition("XY6", 61).subtypes)

    def test_deck_search_factory_requires_a_nonempty_deck_only(self):
        search_def = self.definition("CZ", 128)
        search = self.add(search_def, "hand")

        self.assertFalse(trainer_condition_met(
            search_def.condition, self.board, P1, search,
        ))
        # The actual contents remain private: any card makes the search legal.
        self.add(self.definition("BW1", 1), "deck")
        self.assertTrue(trainer_condition_met(
            search_def.condition, self.board, P1, search,
        ))

    def test_bw_revive_requires_bench_space_and_basic_in_discard(self):
        revive_def = self.definition("BW1", 102)
        revive = self.add(revive_def, "hand")
        self.add(self.definition("BW1", 1), "activePokemonArea")

        self.assertFalse(trainer_condition_met(
            revive_def.condition, self.board, P1, revive,
        ))
        self.add(self.definition("BW1", 15), "discard")
        self.assertTrue(trainer_condition_met(
            revive_def.condition, self.board, P1, revive,
        ))

    def test_scoop_up_net_requires_a_non_v_or_gx_target(self):
        scoop_def = self.definition("SWSH2", 165)
        scoop = self.add(scoop_def, "hand")
        self.add(self.definition("SWSH9", 22), "activePokemonArea")

        self.assertFalse(trainer_condition_met(
            scoop_def.condition, self.board, P1, scoop,
        ))
        self.add(self.definition("BW1", 1), "bench")
        self.assertTrue(trainer_condition_met(
            scoop_def.condition, self.board, P1, scoop,
        ))

    def test_imported_wild_growth_doubles_basic_grass_energy_once(self):
        meganium_def = self.definition("MEP", 1)
        meganium = self.add(meganium_def, "activePokemonArea")
        grass_def = self.grass_energy_definition()
        energy = create_card_entity(self.card_model(grass_def), P1)
        meganium.add_child(energy)
        self.board._register_entity(energy)

        self.assertEqual(
            energy_provided_options(self.board, energy),
            [[PokemonTypes.GRASS.value, PokemonTypes.GRASS.value]],
        )

    def test_wild_growth_value_is_used_by_energy_counting_attacks(self):
        attacker = self.add(self.definition("SV06", 25), "activePokemonArea")
        self.add(self.definition("MEP", 1), "bench")
        energy = create_card_entity(
            self.card_model(self.grass_energy_definition()), P1,
        )
        attacker.add_child(energy)
        self.board._register_entity(energy)

        class Context:
            def __init__(inner_self):
                inner_self.board = self.board
                inner_self.attacker = attacker

            def attached_energies(inner_self, pokemon):
                return self.board.attached_energies(pokemon)

        self.assertEqual(count_energy("self")(Context()), 2)

    def test_wild_growth_exact_retreat_cost_is_paid_automatically(self):
        active = self.add(self.definition("MEP", 1), "activePokemonArea")
        bench = self.add(self.definition("BW1", 1), "bench")
        energy = create_card_entity(
            self.card_model(self.grass_energy_definition()), P1,
        )
        active.add_child(energy)
        self.board._register_entity(energy)

        entries = _retreat_entry(self.board, self.turn, P1, "game")
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["_autoRetreatEnergyIDs"], [energy.entity_id])
        kinds = {info["name"] for info in entries[0]["targetInfoLst"]}
        self.assertEqual(kinds, {SelectionKind.RETREAT_NEW_ACTIVE.value})
        self.assertIn(bench.entity_id, entries[0]["targetInfoLst"][0]["validTargets"])

    def test_wild_growth_overpaying_retreat_uses_both_required_cards(self):
        active = self.add(self.definition("BW1", 17), "activePokemonArea")
        self.add(self.definition("MEP", 1), "bench")
        energies = []
        for _ in range(2):
            energy = create_card_entity(
                self.card_model(self.grass_energy_definition()), P1,
            )
            active.add_child(energy)
            self.board._register_entity(energy)
            energies.append(energy)

        self.assertEqual(active.get_attribute(AttrID.RETREAT_COST), 3)
        entries = _retreat_entry(self.board, self.turn, P1, "game")
        self.assertEqual(len(entries), 1)
        self.assertCountEqual(
            entries[0]["_autoRetreatEnergyIDs"],
            [energy.entity_id for energy in energies],
        )
        kinds = {info["name"] for info in entries[0]["targetInfoLst"]}
        self.assertEqual(kinds, {SelectionKind.RETREAT_NEW_ACTIVE.value})

    def test_boomerang_energy_reattach_is_flushed_after_attack(self):
        attacker = self.add(self.definition("BW1", 1), "activePokemonArea")
        boomerang_def = self.definition("SV06", 166)
        energy = create_card_entity(self.card_model(boomerang_def), P1)
        attacker.add_child(energy)
        self.board._register_entity(energy)

        async def discard_boomerang(ctx):
            await ctx.discard_cards([energy])

        ability = Attack(title="Boomerang regression", effect=discard_boomerang)
        ability.ability_id = "boomerang-regression"

        class Session:
            def __init__(inner_self):
                inner_self.game_id = "game"
                inner_self.board_state = self.board
                inner_self.turn_state = self.turn
                inner_self.players = {}
                inner_self.flushed = []

            def _opponent_id(inner_self, player_id):
                return P2 if player_id == P1 else P1

            def _build_msg(inner_self, name, data):
                return {"name": name, **data}

            def _entity_introduced_msg(inner_self, card):
                return {"introduced": card.entity_id}

            def _entity_moved_msg(inner_self, entity_id, destination_id,
                                  position, **_kwargs):
                return {
                    "entityID": entity_id,
                    "destinationID": destination_id,
                    "position": position,
                }

            async def _broadcast_attack_sources(inner_self, _sources):
                return None

            async def resolve_knockouts(inner_self, _ctx):
                return None

            async def _flush_effect_runs(inner_self, ctx):
                inner_self.flushed.append(list(ctx._messages))

            async def enforce_bench_capacity(inner_self):
                return None

        session = Session()
        asyncio.run(resolve_attack(
            session, P1, attacker, ability, ability.ability_id,
        ))

        self.assertIs(energy.parent, attacker)
        self.assertTrue(session.flushed)
        followup_messages = [
            message
            for run in session.flushed
            for _viewer, message, _bracket in run
        ]
        self.assertTrue(any(
            message.get("entityID") == energy.entity_id
            and message.get("destinationID") == attacker.entity_id
            for message in followup_messages
        ))

    def test_ripening_charge_attaches_to_an_undamaged_pokemon(self):
        hydrapple = self.add(self.definition("SV07", 14), "activePokemonArea")
        energy = self.add(self.grass_energy_definition(), "hand")
        self.assertTrue(ripening_charge_condition(self.board, P1, hydrapple))

        class Context:
            def __init__(inner_self):
                inner_self.attached = None
                inner_self.healed = None

            def hand(inner_self):
                return [energy]

            def my_pokemon_in_play(inner_self):
                return [hydrapple]

            async def choose_cards(inner_self, cards, count, prompt=""):
                return [cards[0]]

            async def choose_pokemon(inner_self, cards, prompt=""):
                return cards[0]

            async def attach_energy(inner_self, picked, target,
                                    counts_as_attachment=False):
                inner_self.attached = (picked, target, counts_as_attachment)
                return True

            async def heal(inner_self, amount, target):
                inner_self.healed = (amount, target)
                return 0

        ctx = Context()
        asyncio.run(ripening_charge(ctx))
        self.assertEqual(ctx.attached, (energy, hydrapple, True))
        self.assertEqual(ctx.healed, (30, hydrapple))

    def test_syrup_storm_counts_grass_energy_across_the_whole_board(self):
        hydrapple = self.add(self.definition("SV07", 14), "activePokemonArea")
        bench = self.add(self.definition("BW1", 1), "bench")
        for pokemon in (hydrapple, bench):
            energy = create_card_entity(
                self.card_model(self.grass_energy_definition()), P1,
            )
            pokemon.add_child(energy)
            self.board._register_entity(energy)

        class Context:
            def __init__(inner_self):
                inner_self.board = self.board
                inner_self.attacker = hydrapple
                inner_self.ability = next(
                    ability for ability in self.definition("SV07", 14).abilities
                    if ability.title == "Syrup Storm"
                )
                inner_self.damage = None

            def my_pokemon_in_play(inner_self):
                return self.board.pokemon_in_play(P1)

            def attached_energies(inner_self, pokemon):
                return self.board.attached_energies(pokemon)

            async def deal_damage(inner_self, amount):
                inner_self.damage = amount

        ctx = Context()
        asyncio.run(syrup_storm(ctx))
        self.assertEqual(ctx.damage, 90)


if __name__ == "__main__":
    unittest.main()
