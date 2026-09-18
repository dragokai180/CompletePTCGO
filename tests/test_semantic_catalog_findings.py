"""Positive and negative outcomes for findings in the full-catalog review."""
import re
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage
from spirit.game.data_utils import Attack, prize_value, def_for
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import effective_pokemon_types, effective_attack_cost
from spirit.tools.effect_smoke import P1, P2


class SemanticCatalogFindingsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add


    async def test_self_attack_restrictions_belong_to_abilities_not_copied_attacks(self):
        from spirit.game.session.passives import attacks_blocked
        cases = (
            ("SV10.TeamRocketsMewtwoex_81", "Erasure Ball", "team"),
            ("SVP.TeamRocketsMewtwoex_205", "Erasure Ball", "team"),
            ("ME2PT5.TeamRocketsMewtwoex_281", "Erasure Ball", "team"),
            ("PGO.SlakingV_58", "Heavy Impact", "prizes"),
            ("PGO.SlakingV_77", "Heavy Impact", "prizes"),
            ("SWSH7.Slaking_131", "Rout", "stadium"),
        )
        for path, title, mode in cases:
            with self.subTest(card=path):
                rig, e, ctx = self.ctx(path, title)
                self.assertIsNone(ctx.ability.condition)
                if mode == "stadium":
                    stadium = self.add(rig, fixtures.definition("BW4.SkyarrowBridge_91"), P1, "hand")
                    area = rig.board.find_global_area("activeStadium")
                    rig.board.move_card(stadium.entity_id, area.entity_id)
                if mode == "prizes":
                    prizes = rig.board.find_player_area(P1, "prizePile")
                    while len(prizes.children) > 2:
                        rig.to_area(prizes.children[-1], P1, "hand")
                    while len(prizes.children) < 2:
                        self.add(rig, self.filler, P1, "prizePile")
                self.assertTrue(attacks_blocked(rig.board, ctx.source))
                self.assertFalse(attacks_blocked(rig.board, ctx.opponent_bench()[0]))
                state = rig.session.turn_state
                state.abilities_disabled_through_turn = state.turn_number
                self.assertFalse(attacks_blocked(rig.board, ctx.source))
                state.abilities_disabled_through_turn = -1
                if mode == "team":
                    definition = fixtures.definition("SV10.TeamRocketsMewtwoex_81")
                    for _ in range(3):
                        self.add(rig, definition, P1, "bench")
                elif mode == "prizes":
                    rig.to_area(prizes.children[-1], P1, "hand")
                else:
                    rig.to_area(stadium, P1, "discard")
                self.assertFalse(attacks_blocked(rig.board, ctx.source))

    def test_printed_gx_classification_and_stage_survive_reprints(self):
        for path in ("SM5.DialgaGX_100", "SM5.DialgaGX_146", "SM5.DialgaGX_164"):
            card = fixtures.definition(path)
            self.assertIn("GX", card.subtypes)
            self.assertEqual(prize_value(card.guid), 2)
            self.assertTrue(next(a for a in card.abilities if a.title == "Timeless-GX").gx)
        for number in (61, 266, 278):
            card = fixtures.definition("ME2PT5.MegaEelektrossex_" + str(number))
            self.assertEqual(card.extra_attributes[str(AttrID.STAGE.value)]["value"], PokemonStage.STAGE2.value)
            self.assertNotIn("Stage 1", card.subtypes)

    async def test_watchog_has_confusion_and_coin_gated_damage(self):
        rig, e, ctx = self.ctx("BW1.Watchog_79", "Confuse Ray")
        await ctx.ability.effect(ctx)
        self.assertIn("Confused", ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS))
        for heads in (False, True):
            rig, e, ctx = self.ctx("BW1.Watchog_79", "Hyper Fang")
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.deal_damage = AsyncMock(return_value=60 if heads else 0)
            await ctx.ability.effect(ctx)
            amounts = [c.args[0] if c.args else ctx.ability.damage for c in ctx.deal_damage.await_args_list]
            self.assertEqual(sum(amounts), 60 if heads else 0)

    def test_mega_promos_award_the_rule_box_prizes(self):
        for stem in ("MegaCharizardXex_23", "MegaCharizardXex_29", "MegaCharizardYex_30",
                     "MegaClefableex_72", "MegaEmboarex_35", "MegaFeraligatrex_36",
                     "MegaGardevoirex_32", "MegaGengarex_73", "MegaGreninjaex_81",
                     "MegaKangaskhanex_25", "MegaLatiasex_11", "MegaLucarioex_12",
                     "MegaLucarioex_33", "MegaMeganiumex_34", "MegaVenusaurex_13",
                     "MegaZygardeex_71"):
            with self.subTest(card=stem):
                self.assertEqual(prize_value(fixtures.definition("MEP." + stem).guid), 3)
        self.assertEqual(prize_value(fixtures.definition("MEP.Oricorioex_24").guid), 2)

    async def test_redirected_sunlight_counts_opponents_fire_only(self):
        rig, e, ctx = self.ctx("SV06.Sunflora_7", "Redirected Sunlight")
        for pokemon in ctx.opponent_pokemon_in_play():
            for energy in list(ctx.attached_energies(pokemon)):
                rig.to_area(energy, P2, "discard")
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(sum(c.args[0] for c in ctx.deal_damage.await_args_list), 0)
        rig.attach_energy_type(P1, ctx.source, PokemonTypes.FIRE.value)
        rig.attach_energy_type(P2, ctx.defender, PokemonTypes.FIRE.value)
        extra = self.add(rig, fixtures.definition("BW1.FireEnergy_106"), P2, "hand")
        rig.attach(extra, ctx.opponent_bench()[0])
        rig.attach_energy_type(P2, ctx.opponent_bench()[0], PokemonTypes.WATER.value)
        ctx.deal_damage.reset_mock()
        await ctx.ability.effect(ctx)
        self.assertEqual(sum(c.args[0] for c in ctx.deal_damage.await_args_list), 120)

    async def test_retaliatory_incisors_counts_only_own_benched_rattata(self):
        rig, e, ctx = self.ctx("ME3.Raticate_61", "Retaliatory Incisors")
        rattata = fixtures.definition("BW9.Rattata_87")
        own = self.add(rig, rattata, P1, "bench")
        other = self.add(rig, rattata, P2, "bench")
        for card, damage in ((own, 20), (other, 30)):
            card.set_attribute(AttrID.HP, card.get_attribute(AttrID.HP) - damage)
        ctx.source.set_attribute(AttrID.HP, 50)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(sum(c.args[0] for c in ctx.deal_damage.await_args_list), 80)

    async def test_slurp_slurp_all_four_coin_outcomes(self):
        for coins in ([False, False], [True, False], [False, True], [True, True]):
            with self.subTest(coins=coins):
                rig, e, ctx = self.ctx("SV06.Slurpuff_90", "Slurp Slurp")
                ctx.flip_coins = AsyncMock(return_value=coins)
                ctx.deal_damage = AsyncMock(return_value=90 * sum(coins))
                await ctx.ability.effect(ctx)
                self.assertEqual(sum(c.args[0] for c in ctx.deal_damage.await_args_list), 90 * sum(coins))
                self.assertEqual("Confused" in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), not any(coins))

    async def test_flaring_magic_pays_fire_then_draws_to_seven(self):
        for path in ("ME4.Delphox_13", "MEP.Delphox_74"):
            with self.subTest(path=path):
                rig, e, ctx = self.ctx(path, "Flaring Magic")
                for card in list(ctx.hand()):
                    rig.to_area(card, P1, "deck")
                self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
                fire = self.add(rig, fixtures.definition("BW1.FireEnergy_106"), P1, "hand")
                for _ in range(6):
                    self.add(rig, self.filler, P1, "hand")
                self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
                draw = ctx.deck_top(1)[0]
                ctx.choose_cards = AsyncMock(return_value=[fire])
                await ctx.ability.effect(ctx)
                self.assertIn(fire, ctx.discard_pile())
                self.assertEqual(len(ctx.hand()), 7)
                self.assertIn(draw, ctx.hand())

    async def test_every_shared_fixed_coin_multiplier_family(self):
        from spirit.game.card_effects.bw_era import bw_legacy_attack
        families = {}
        for model in loader.cards:
            definition = def_for(model.guid)
            for ability in getattr(definition, "abilities", []):
                if not isinstance(ability, Attack) or ability.effect is not bw_legacy_attack:
                    continue
                text = " ".join((ability.game_text or "").lower().split())
                match = re.fullmatch(r"flip (\d+) coins\. (?:this attack )?does (\d+) damage (?:for each|times the number of) heads\.", text)
                if match:
                    path = loader.script_by_guid[model.guid]
                    from pathlib import Path
                    module = ".".join(Path(path).relative_to(loader.scripts_dir).with_suffix("").parts)
                    families.setdefault((int(match[1]), int(match[2])), (module, ability.title))
        self.assertGreater(len(families), 10)
        for (count, per_head), (path, title) in families.items():
            for heads in range(count + 1):
                with self.subTest(path=path, title=title, heads=heads):
                    rig, e, ctx = self.ctx(path, title)
                    ctx.flip_coins = AsyncMock(return_value=[True] * heads + [False] * (count - heads))
                    ctx.deal_damage = AsyncMock(return_value=per_head * heads)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(sum(call.args[0] for call in ctx.deal_damage.await_args_list), per_head * heads)

    async def test_beckoning_tail_pays_specific_card_before_switching(self):
        rig, e, ctx = self.ctx("SV08.Meowstic_85", "Beckoning Tail")
        for card in list(ctx.hand()):
            rig.to_area(card, P1, "deck")
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        toy = self.add(rig, fixtures.definition("SV08.ChillTeaserToy_166"), P1, "hand")
        target = ctx.opponent_bench()[0]
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.choose_cards = AsyncMock(return_value=[toy])
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ctx.ability.effect(ctx)
        self.assertIn(toy, ctx.discard_pile())
        self.assertIs(rig.board.active_pokemon(P2), target)

    async def test_subjugating_chains_excludes_all_prints_and_uses_live_types(self):
        rig, e, ctx = self.ctx("SV065.Pecharuntex_39", "Subjugating Chains")
        for card in list(ctx.my_bench()):
            rig.to_area(card, P1, "hand")
        variants = [self.add(rig, fixtures.definition(path), P1, "bench") for path in
                    ("SV065.Pecharuntex_85", "SV085.Pecharuntex_163")]
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        target = self.add(rig, fixtures.definition("SWSH6.Kecleon_122"), P1, "bench")
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        energy = self.add(rig, fixtures.definition("BW1.DarknessEnergy_111"), P1, "hand")
        rig.attach(energy, target)
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_pokemon.await_args.args[0], [target])
        self.assertIs(ctx.my_active(), target)
        self.assertIn("Poisoned", target.get_attribute(AttrID.SPECIAL_CONDITIONS))

    def test_seasoned_skill_matches_attack_name_not_an_unmodified_cost(self):
        rig, e, ctx = self.ctx("SV06.BloodmoonUrsalunaex_141", "Blood Moon")
        other = Attack(title="Other Attack", cost={PokemonTypes.COLORLESS: 5}, damage=10)
        with patch.object(rig.board, "prizes_taken", return_value=2):
            for original in (4, 5, 6):
                self.assertEqual(effective_attack_cost(rig.board, ctx.source,
                    {"Colorless": original}, attack=ctx.ability), {"Colorless": original - 2})
            self.assertEqual(effective_attack_cost(rig.board, ctx.source,
                {"Colorless": 5}, attack=other), {"Colorless": 5})
        self.assertTrue(ctx.ability.locks_next_turn)
        self.assertIn("can't attack", ctx.ability.game_text)
        self.assertNotIn("can't attack", fixtures.definition("SV06.BloodmoonUrsalunaex_141").abilities[0].game_text)

    def test_reprinted_legend_halves_preserve_both_weaknesses(self):
        import json
        for first, second in (("HGSS2.RaikouSuicuneLEGEND_92", "HGSS2.RaikouSuicuneLEGEND_93"),
                              ("HGSS2.SuicuneEnteiLEGEND_94", "HGSS2.SuicuneEnteiLEGEND_95"),
                              ("HGSS3.KyogreGroudonLEGEND_87", "HGSS3.KyogreGroudonLEGEND_88"),
                              ("HGSS3.RayquazaDeoxysLEGEND_89", "HGSS3.RayquazaDeoxysLEGEND_90"),
                              ("HGSS4.DarkraiCresseliaLEGEND_99", "HGSS4.DarkraiCresseliaLEGEND_100"),
                              ("HGSS4.PalkiaDialgaLEGEND_101", "HGSS4.PalkiaDialgaLEGEND_102")):
            with self.subTest(card=second):
                def weaknesses(path):
                    return json.loads(fixtures.definition(path).extra_attributes[str(AttrID.WEAKNESS_TYPES.value)]["value"])
                self.assertEqual(len(weaknesses(second)), 2)
                self.assertEqual(weaknesses(first), weaknesses(second))

    async def test_flock_finds_other_arrokuda_prints_even_when_copied(self):
        rig, e, ctx = self.ctx("SWSH4.Arrokuda_41", "Flock")
        choices = [self.add(rig, fixtures.definition(path), P1, "deck") for path in
                   ("SWSH2.Arrokuda_52", "SV10.Arrokuda_62")]
        # A copied attack's source does not change the printed species filter.
        ctx.source = ctx.my_bench()[0]
        ctx.search_deck = AsyncMock(return_value=choices)
        await ctx.ability.effect(ctx)
        predicate = ctx.search_deck.await_args.args[0]
        # Check after moving them back so the bench-placement predicate applies.
        for card in choices:
            self.assertIn(card, ctx.my_bench())
            rig.to_area(card, P1, "deck")
        self.assertTrue(all(predicate(card) for card in choices))
        # The effect shuffles; deck[0] can legitimately be another Arrokuda.
        unrelated = self.add(rig, self.filler, P1, "deck")
        self.assertFalse(predicate(unrelated))

    async def test_lum_berry_below_break_is_discarded_after_curing(self):
        rig, e = self.rig("XY8.RaichuBREAK_50")
        source = e["target"]
        lower = self.add(rig, self.filler, P1, "hand")
        rig.attach(lower, source)
        berry_def = fixtures.definition("SWSH1.LumBerry_168")
        berry = self.add(rig, berry_def, P1, "hand")
        rig.attach(berry, lower)
        source.set_attribute(AttrID.SPECIAL_CONDITIONS, ["Poisoned", "Asleep"])
        source.set_attribute(AttrID.HP, 10)
        ctx = EffectContext(rig.session, P1, source, None)
        await rig.session._fire_end_of_turn_triggers(P2)
        self.assertFalse(source.get_attribute(AttrID.SPECIAL_CONDITIONS))
        self.assertIn(berry, ctx.discard_pile())
        await rig.session._run_pokemon_checkup(P2)
        self.assertIs(rig.board.active_pokemon(P1), source)
        self.assertEqual(source.get_attribute(AttrID.HP), 10)

    async def test_berries_resolve_before_checkup_and_discard_only_themselves(self):
        for owner_turn in (P1, P2):
            for path, damage, special, expected_heal in (
                    ("SWSH1.LumBerry_168", 40, ["Poisoned"], 0),
                    ("SWSH1.LumBerry_168", 40, [], 0),
                    ("SWSH1.SitrusBerry_182", 20, [], 0),
                    ("SWSH1.SitrusBerry_182", 40, ["Poisoned"], 30)):
                with self.subTest(path=path, damage=damage, turn=owner_turn):
                    rig, e, ctx = self.ctx("BW1.Serperior_6", "Royal Heal")
                    pokemon = ctx.my_bench()[0]
                    # The holder has another Tool; Sitrus must not discard it.
                    other = self.add(rig, fixtures.definition("BW7.RockyHelmet_133"), P1, "hand")
                    rig.attach(other, pokemon)
                    berry = self.add(rig, fixtures.definition(path), P1, "hand")
                    rig.attach(berry, pokemon)
                    before = ctx.max_hp(pokemon) - damage
                    pokemon.set_attribute(AttrID.HP, before)
                    pokemon.set_attribute(AttrID.SPECIAL_CONDITIONS, special)
                    # Call the Tool's event directly so unrelated Royal Heal
                    # in the fixture cannot affect this HP assertion.
                    hook_ctx = EffectContext(rig.session, owner_turn, berry, None)
                    await fixtures.definition(path).passive.on_end_turn(hook_ctx, berry)
                    self.assertEqual(pokemon.get_attribute(AttrID.HP), before + expected_heal)
                    should_discard = bool(special) if "LumBerry" in path else damage >= 30
                    self.assertEqual(berry in ctx.discard_pile(), should_discard)
                    self.assertNotIn(other, ctx.discard_pile())

    async def test_duskull_attack_accepts_other_prints_and_respects_bench(self):
        for path in ("SV065.Duskull_18", "SV065.Duskull_68", "SV085.Duskull_35"):
            rig, e, ctx = self.ctx(path, "Come and Get You")
            self.assertIsInstance(ctx.ability, Attack)
            self.assertEqual(ctx.ability.cost, {PokemonTypes.PSYCHIC: 1})
            duskull = self.add(rig, fixtures.definition("BW7.Duskull_61"), P1, "discard")
            while len(ctx.my_bench()) < 4:
                self.add(rig, self.filler, P1, "bench")
            ctx.choose_cards = AsyncMock(return_value=[duskull])
            await ctx.ability.effect(ctx)
            self.assertIn(duskull, ctx.my_bench())
            self.assertEqual(len(ctx.my_bench()), 5)
            self.assertEqual(ctx.choose_cards.await_args.args[1], 1)

    async def test_double_type_is_in_play_only(self):
        rig, e, ctx = self.ctx("SWSH3.Blaziken_24", "Double Type")
        source = e["target"]
        self.assertEqual(source.get_attribute(AttrID.POKEMON_TYPES), [PokemonTypes.FIRE.value])
        self.assertEqual(set(effective_pokemon_types(rig.board, source)),
                         {PokemonTypes.FIRE.value, PokemonTypes.FIGHTING.value})
        rig.to_area(source, P1, "discard")
        self.assertEqual(effective_pokemon_types(rig.board, source), [PokemonTypes.FIRE.value])

    async def test_up_tempo_accounts_for_bottom_deck_cost_before_draw(self):
        rig, e, ctx = self.ctx("SV08.Quaquaval_52", "Up-Tempo")
        while len(ctx.hand()) > 5:
            rig.to_area(ctx.hand()[-1], P1, "deck")
        while len(ctx.hand()) < 5:
            rig.to_area(ctx.deck()[0], P1, "hand")
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        card = ctx.hand()[0]
        ctx.choose_cards = AsyncMock(return_value=[card])
        draw = ctx.deck_top(1)[0]
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.hand()), 5)
        self.assertNotIn(card, ctx.hand())
        self.assertIn(draw, ctx.hand())
        self.assertIn(card, ctx.deck())
        rig.to_area(ctx.deck()[0], P1, "hand")
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        for card in list(ctx.hand()):
            rig.to_area(card, P1, "deck")
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_dimension_transfer_reveals_item_and_puts_it_on_top(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx("HGSS4.PorygonZ_7", "Dimension Transfer")
            item = self.add(rig, fixtures.definition("BW1.Potion_100"), P1, "discard")
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.choose_cards = AsyncMock(return_value=[item])
            ctx.reveal_cards = AsyncMock()
            await ctx.ability.effect(ctx)
            if heads:
                self.assertIs(ctx.deck_top(1)[0], item)
                ctx.reveal_cards.assert_awaited()
            else:
                self.assertIn(item, ctx.discard_pile())
                ctx.choose_cards.assert_not_awaited()

    async def test_energy_traps_are_attack_effects_on_the_original_defender(self):
        for path, title, damage, condition in (
            ("SWSH12.Chimecho_74", "Dreaming Tone", 0, "Asleep"),
            ("SWSH4.Eelektross_59", "Electrified Bite Mark", 60, None),
        ):
            rig, e, ctx = self.ctx(path, title)
            self.assertTrue(all(isinstance(a, Attack) for a in fixtures.definition(path).abilities))
            target = ctx.defender
            target.set_attribute(AttrID.HP, 500)
            before = target.get_attribute(AttrID.HP)
            await ctx.ability.effect(ctx)
            if not damage:
                self.assertEqual(target.get_attribute(AttrID.HP), before)
            self.assertNotIn("Asleep", target.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
            marks = [p for p in rig.board.temporary_passives if p.carrier_entity_id == target.entity_id]
            self.assertEqual(len(marks), 1)
            event = EffectContext(rig.session, P2, target, None)
            event.attaching_player_id = P2
            event.energy_receiver = target
            # Not during the turn when the mark was created.
            after_attack = target.get_attribute(AttrID.HP)
            await marks[0].passive.on_energy_attached(event, target)
            self.assertEqual(target.get_attribute(AttrID.HP), after_attack)
            rig.session.turn_state.turn_number += 1
            # The attack remains after its original attacker leaves play.
            rig.to_area(ctx.source, P1, "discard")
            await marks[0].passive.on_energy_attached(event, target)
            self.assertEqual(target.get_attribute(AttrID.HP), after_attack - damage)
            if condition:
                self.assertIn(condition, target.get_attribute(AttrID.SPECIAL_CONDITIONS))

    async def test_spark_trap_registers_a_temporary_attack_effect_not_an_ability(self):
        for number in (59, 210):
            path = "SWSH7.DracozoltVMAX_" + str(number)
            rig, e, ctx = self.ctx(path, "Spark Trap")
            self.assertTrue(all(isinstance(a, Attack) for a in fixtures.definition(path).abilities))
            await ctx.ability.effect(ctx)
            marks = [p for p in rig.board.temporary_passives if p.carrier_entity_id == ctx.source.entity_id]
            self.assertEqual(len(marks), 1)
            self.assertTrue(marks[0].from_attack)
            self.assertEqual(marks[0].passive.counters, 12)
