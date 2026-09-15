"""Final conditional Trainer regression scenarios for the SM/SWSH audit."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1, P2


class RemainingTrainerTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_card(self, path):
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        ctx.is_trainer_effect = True
        return rig, ctx, fixtures.definition(path)

    def legal(self, rig, ctx, definition):
        return trainer_condition_met(definition.condition, rig.board, P1, ctx.source)

    def energy(self, rig, kind=PokemonTypes.METAL, zone='hand', pid=P1):
        return self.add(rig, CARD_DEFS_BY_GUID[self.energies[kind.value].lower()], pid, zone)

    def stadium(self, rig, path, pid=P2):
        card = self.add(rig, fixtures.definition(path), pid, 'hand')
        rig.board.move_card(card.entity_id, rig.board.find_global_area('activeStadium').entity_id)
        card.owning_player_id = pid
        return card

    async def test_faba_rejects_own_attachments_and_protected_stadium(self):
        rig, ctx, d = self.setup_card('SM8.Faba_173')
        tool = self.add(rig, fixtures.definition('SM3.WishfulBaton_128'), P1, 'hand')
        rig.attach(tool, ctx.my_active())
        self.assertFalse(self.legal(rig, ctx, d))
        stadium = self.stadium(rig, 'SM8.ThunderMountain_191')
        self.assertFalse(self.legal(rig, ctx, d))
        await d.effect(ctx)
        self.assertIs(stadium.parent, rig.board.find_global_area('activeStadium'))

    async def test_stadium_discard_honors_prism_protection_and_pokemon_replacement(self):
        for path in ('SM6.Bonnie_103', 'SWSH6.Flannery_139', 'SM9.DangerousDrill_138'):
            rig, ctx, d = self.setup_card(path)
            self.add(rig, fixtures.definition('SWSH5.Houndoom_96'), P1, 'hand')
            stadium = self.stadium(rig, 'SM8.ThunderMountain_191')
            if 'Bonnie' in path:
                self.assertTrue(self.legal(rig, ctx, d))
                await d.effect(ctx)
                self.assertIn('zygarde-gx', rig.session.turn_state.gx_repeat_names_this_turn[P1])
            else:
                self.assertFalse(self.legal(rig, ctx, d), path)
            self.assertIsNone(await ctx.discard_stadium())
            self.assertIs(stadium.parent, rig.board.find_global_area('activeStadium'))
            # An attack is not an Item/Supporter: Prism Star still goes to Lost Zone.
            ctx.source = ctx.my_active()
            ctx.is_trainer_effect = False
            self.assertIs(await ctx.discard_stadium(), stadium)
            self.assertIn(stadium, rig.board.find_player_area(P2, 'lostZone').children)

    async def test_private_searches_require_nonempty_deck_not_matching_cards(self):
        for path in ('SWSH10.Adaman_135', 'SWSH11.MirageGate_163',
                     'SWSH3.FamiliarBell_161', 'SWSH10.WaitandSeeTurbo_158'):
            rig, ctx, d = self.setup_card(path)
            self.energy(rig); self.energy(rig)
            self.add(rig, fixtures.definition('SWSH5.Houndoom_96'), P1, 'discard')
            for _ in range(7): self.energy(rig, zone='lostZone')
            rig.session.turn_state.turn_number = 2
            self.assertTrue(self.legal(rig, ctx, d), path)
            for card in list(ctx.deck(P1)): rig.to_area(card, P1, 'discard')
            self.assertFalse(self.legal(rig, ctx, d), path)

    async def test_food_tin_requires_damage_and_discards_only_one_psychic_energy(self):
        for path in ('SWSH35.SuspiciousFoodTin_66', 'SWSH35.SuspiciousFoodTin_80'):
            rig, ctx, d = self.setup_card(path)
            target = ctx.my_active()
            energies = [self.energy(rig, PokemonTypes.PSYCHIC) for _ in range(2)]
            for card in energies: rig.attach(card, target)
            self.assertFalse(self.legal(rig, ctx, d))
            target.set_attribute(AttrID.HP, ctx.max_hp(target)-30)
            self.assertTrue(self.legal(rig, ctx, d))
            ctx.choose_pokemon = AsyncMock(return_value=target)
            ctx.discard_energy_from = AsyncMock()
            await d.effect(ctx)
            self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target))
            self.assertEqual(ctx.discard_energy_from.call_args.args, (target, 1))

    async def test_volo_discards_entire_benched_v_stack_without_prizes(self):
        rig, ctx, d = self.setup_card('SWSH11.Volo_169')
        target = self.add(rig, fixtures.definition('CZ.ZamazentaVSTAR_99'), P1, 'bench')
        previous = self.add(rig, fixtures.definition('SWSH12.HisuianArcanineV_90'), P1, 'hand')
        energy = self.energy(rig)
        tool = self.add(rig, fixtures.definition('SM3.WishfulBaton_128'), P1, 'hand')
        for card in (previous, energy, tool): rig.attach(card, target)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        before = len(rig.board.find_player_area(P2, 'prizePile').children)
        self.assertTrue(self.legal(rig, ctx, d))
        await d.effect(ctx)
        for card in (target, previous, energy, tool): self.assertIn(card, ctx.discard_pile())
        self.assertEqual(len(rig.board.find_player_area(P2, 'prizePile').children), before)
        self.assertNotIn(ctx.my_active(), ctx.choose_pokemon.call_args.args[0])

    async def test_echoing_horn_restores_opponents_basic_to_opponents_bench(self):
        rig, ctx, d = self.setup_card('SWSH6.EchoingHorn_136')
        basic = self.add(rig, fixtures.definition('SWSH12.HisuianArcanineV_90'), P2, 'discard')
        basic.set_attribute(AttrID.HP, 0)
        ctx.choose_cards = AsyncMock(return_value=[basic])
        self.assertTrue(self.legal(rig, ctx, d))
        await d.effect(ctx)
        self.assertIn(basic, ctx.opponent_bench())
        self.assertNotIn(basic, ctx.my_bench())
        self.assertEqual(basic.get_attribute(AttrID.HP), ctx.max_hp(basic))

    async def test_toy_catcher_uses_remaining_hp_and_players_choice(self):
        rig, ctx, d = self.setup_card('SWSH7.ToyCatcher_163')
        for pokemon in ctx.opponent_bench(): pokemon.set_attribute(AttrID.HP, 60)
        self.assertFalse(self.legal(rig, ctx, d))
        target = ctx.opponent_bench()[0]
        target.set_attribute(AttrID.HP, 50)
        self.assertTrue(self.legal(rig, ctx, d))
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await d.effect(ctx)
        self.assertIs(ctx.opponent_active(), target)
        self.assertEqual(ctx.choose_pokemon.call_args.args[0], [target])

    async def test_crossceiver_requires_second_copy_and_recovers_no_items(self):
        rig, ctx, d = self.setup_card('SWSH8.Crossceiver_231')
        for card in list(ctx.hand()):
            if card is not ctx.source: rig.to_area(card, P1, 'deck')
        self.assertFalse(self.legal(rig, ctx, d))
        pair = self.add(rig, d, P1, 'hand')
        target = self.add(rig, fixtures.definition('SM6.Diantha_105'), P1, 'discard')
        ctx.choose_cards = AsyncMock(return_value=[target])
        self.assertTrue(self.legal(rig, ctx, d))
        await d.effect(ctx)
        self.assertIn(pair, ctx.discard_pile())
        self.assertIn(target, ctx.hand())
        self.assertNotIn(pair, ctx.choose_cards.call_args.args[0])
        self.assertEqual(ctx.choose_cards.call_args.args[1], 1)

    async def test_team_yells_cheer_excludes_itself_and_laventon_requires_hisuian(self):
        for path, target_path in (
                ('SWSH9.TeamYellsCheer_149', 'SWSH10.Roxanne_150'),
                ('SWSH12.ProfessorLaventon_162', 'SWSH12.HisuianArcanineV_90')):
            rig, ctx, d = self.setup_card(path)
            for card in list(ctx.discard_pile()): rig.to_area(card, P1, 'deck')
            wrong = self.add(rig, d, P1, 'discard')
            self.assertFalse(self.legal(rig, ctx, d))
            target = self.add(rig, fixtures.definition(target_path), P1, 'discard')
            ctx.choose_cards = AsyncMock(return_value=[target])
            self.assertTrue(self.legal(rig, ctx, d))
            await d.effect(ctx)
            self.assertIn(wrong, ctx.discard_pile())
            self.assertIn(target, ctx.deck(P1) if 'Cheer' in path else ctx.hand())
            self.assertEqual(ctx.choose_cards.call_args.args[1], 3)

    async def test_phoebe_and_kartenvoy_cover_new_attackers_only_against_active(self):
        from unittest.mock import patch
        from spirit.game.session.passives import compute_damage
        for path, pokemon_path in (
                ('SWSH5.Phoebe_130', 'SWSH1.SnorlaxVMAX_142'),
                ('SM10.UltraForestKartenvoy_188', 'SM4.BuzzwoleGX_57')):
            rig, ctx, d = self.setup_card(path)
            await d.effect(ctx)
            attacker = self.add(rig, fixtures.definition(pokemon_path), P1, 'bench')
            attack = fixtures.definition(pokemon_path).abilities[-1]
            attack_ctx = EffectContext(rig.session, P1, attacker, attack)
            for target in (ctx.opponent_active(), ctx.opponent_bench()[0]):
                with patch('spirit.game.session.effects.compute_damage', wraps=compute_damage) as spy:
                    await attack_ctx.deal_damage(10, target=target)
                    self.assertEqual(spy.call_args.kwargs['ignore_target_effects'],
                                     target is ctx.opponent_active())
            rig.session.turn_state.begin_turn(P2, rig.board)
            with patch('spirit.game.session.effects.compute_damage', wraps=compute_damage) as spy:
                await attack_ctx.deal_damage(10, target=ctx.opponent_active())
                self.assertFalse(spy.call_args.kwargs['ignore_target_effects'])

    async def test_fan_of_waves_and_eneporter_move_only_one_opponents_special_energy(self):
        for path in ('SWSH5.FanofWaves_127', 'SM6.Eneporter_106'):
            rig, ctx, d = self.setup_card(path)
            source, target = ctx.opponent_active(), ctx.opponent_bench()[0]
            special = self.add(rig, fixtures.definition('SM1.RainbowEnergy_137'), P2, 'hand')
            basic = self.energy(rig, pid=P2)
            rig.attach(special, source); rig.attach(basic, source)
            ctx.choose_cards = AsyncMock(return_value=[special])
            ctx.choose_pokemon = AsyncMock(return_value=target)
            self.assertTrue(self.legal(rig, ctx, d))
            await d.effect(ctx)
            self.assertIs(basic.parent, source)
            if 'FanofWaves' in path:
                self.assertIs(special, ctx.deck(P2)[0])
            else:
                self.assertIs(special.parent, target)

    async def test_returning_attachments_survive_discarding_the_entire_pokemon_stack(self):
        from spirit.game.session.effects import full_stack
        rig, ctx, d = self.setup_card('SWSH11.Volo_169')
        target = self.add(rig, fixtures.definition('SWSH12.HisuianArcanineV_90'), P1, 'bench')
        recycled = self.add(rig, fixtures.definition('SM11.RecycleEnergy_212'), P1, 'hand')
        tool = self.add(rig, fixtures.definition('SM11.UTurnBoard_211'), P1, 'hand')
        ordinary = self.energy(rig)
        for card in (recycled, tool, ordinary): rig.attach(card, target)
        await ctx.discard_cards(full_stack(target))
        self.assertIn(target, ctx.discard_pile())
        self.assertIn(ordinary, ctx.discard_pile())
        self.assertIn(recycled, ctx.hand())
        self.assertIn(tool, ctx.hand())
        # The same cards discarded from hand have no in-play replacement.
        await ctx.discard_cards([recycled, tool])
        self.assertIn(recycled, ctx.discard_pile())
        self.assertIn(tool, ctx.discard_pile())

    async def test_dragon_talon_and_giant_bomb_only_react_to_qualifying_attack_damage(self):
        from spirit.game.data_utils import Attack
        for path, damage, expected in (
                ('DM.DragonTalon_59', 10, 30),
                ('SM11.GiantBomb_196', 170, 0),
                ('SM11.GiantBomb_196', 180, 100)):
            for bench, counters in ((False, False), (True, False), (False, True)):
                rig, ctx, d = self.setup_card(path)
                target = self.add(rig, fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'), P1, 'bench')
                if not bench:
                    rig.to_area(ctx.my_active(), P1, 'bench')
                    rig.to_area(target, P1, 'activePokemonArea')
                rig.attach(ctx.source, target)
                attacker = ctx.opponent_active()
                before = attacker.get_attribute(AttrID.HP)
                attack_ctx = EffectContext(rig.session, P2, attacker, Attack(title='Test hit', cost={}, damage=damage))
                await attack_ctx.deal_damage(damage, target=target, apply_modifiers=False, as_counters=counters)
                for action in list(attack_ctx.deferred_actions): await action()
                self.assertEqual(before-attacker.get_attribute(AttrID.HP),
                                 expected if not bench and not counters else 0)

    async def test_giant_bomb_expires_after_opponent_turn_only(self):
        rig, ctx, d = self.setup_card('SM11.GiantBomb_196')
        target = ctx.my_active()
        rig.attach(ctx.source, target)
        await d.passive.on_end_turn(ctx, ctx.source)
        self.assertIs(ctx.source.parent, target)
        other = EffectContext(rig.session, P2, ctx.opponent_active(), None)
        await d.passive.on_end_turn(other, ctx.source)
        self.assertIn(ctx.source, ctx.discard_pile())

    async def test_returning_attachments_also_work_in_actual_knockout_resolution(self):
        rig, ctx, d = self.setup_card('SWSH11.Volo_169')
        target = ctx.opponent_active()
        cards = [self.add(rig, fixtures.definition(path), P2, 'hand')
                 for path in ('SM11.RecycleEnergy_212', 'SM11.UTurnBoard_211')]
        for card in cards: rig.attach(card, target)
        await ctx.knock_out(target)
        await rig.session.resolve_knockouts(ctx)
        self.assertIn(target, ctx.discard_pile(P2))
        for card in cards: self.assertIn(card, ctx.hand(P2))

    async def test_slaking_v_prize_restriction_disappears_when_ability_is_suppressed(self):
        from unittest.mock import patch
        for path in ('PGO.SlakingV_58', 'PGO.SlakingV_77'):
            rig, e = self.rig(path)
            d = fixtures.definition(path)
            pokemon = e['target']
            attack = d.abilities[1]
            prizes = rig.board.find_player_area(P1, 'prizePile')
            for count in (6, 5, 4, 3, 2, 1):
                while len(prizes.children) > count: rig.to_area(prizes.children[-1], P1, 'hand')
                self.assertEqual(attack.condition(rig.board, P1, pokemon), count % 2 == 1)
                with patch('spirit.game.session.legal_actions.ability_locked', return_value=True):
                    self.assertTrue(attack.condition(rig.board, P1, pokemon))

    async def test_brocks_training_selects_named_pokemon_and_allows_special_energy(self):
        rig, ctx, d = self.setup_card('HF.BrocksTraining_55')
        target = self.add(rig, fixtures.definition('HF.OnixGX_36'), P1, 'bench')
        energy = self.add(rig, fixtures.definition('SM1.RainbowEnergy_137'), P1, 'hand')
        ctx.choose_cards = AsyncMock(return_value=[energy])
        ctx.choose_pokemon = AsyncMock(return_value=target)
        self.assertTrue(self.legal(rig, ctx, d))
        await d.effect(ctx)
        self.assertIs(energy.parent, target)
        ctx.choose_pokemon.assert_not_awaited()  # The only named recipient is automatic.
        rig.to_area(target, P1, 'discard')
        self.assertFalse(self.legal(rig, ctx, d))

    async def test_last_chance_potion_uses_remaining_not_printed_hp(self):
        rig, ctx, d = self.setup_card('SM7.LastChancePotion_135')
        target = self.add(rig, fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'), P1, 'bench')
        target.set_attribute(AttrID.HP, 40)
        self.assertFalse(self.legal(rig, ctx, d))
        target.set_attribute(AttrID.HP, 30)
        self.assertTrue(self.legal(rig, ctx, d))
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await d.effect(ctx)
        self.assertEqual(target.get_attribute(AttrID.HP), 150)
        self.assertEqual(ctx.choose_pokemon.call_args.args[0], [target])

    async def test_giovannis_exile_only_healthy_bench_and_whole_stack(self):
        rig, ctx, d = self.setup_card('SM10.GiovannisExile_174')
        target = ctx.my_bench()[0]
        damaged = self.add(rig, fixtures.definition('SWSH12.HisuianArcanineV_90'), P1, 'bench')
        damaged.set_attribute(AttrID.HP, ctx.max_hp(damaged)-10)
        energy = self.energy(rig)
        rig.attach(energy, target)
        ctx.choose_cards = AsyncMock(return_value=[target])
        await d.effect(ctx)
        self.assertIn(target, ctx.discard_pile())
        self.assertIn(energy, ctx.discard_pile())
        self.assertNotIn(damaged, ctx.choose_cards.call_args.args[0])
        self.assertNotIn(ctx.my_active(), ctx.choose_cards.call_args.args[0])
        self.assertEqual(ctx.choose_cards.call_args.args[1], 2)

    async def test_welcoming_lantern_and_scrounge_recover_only_their_categories(self):
        for path, target_path, pokemon_card in (
                ('SWSH6.WelcomingLantern_156', 'SWSH6.Flannery_139', False),
                ('SWSH6.Skwovet_127', 'SM3.WishfulBaton_128', True)):
            rig, e = self.rig(path, 'pokemon' if pokemon_card else 'trainer')
            d = fixtures.definition(path)
            ability = d.abilities[0] if pokemon_card else None
            ctx = EffectContext(rig.session, P1, e['target'], ability)
            for card in list(ctx.discard_pile()): rig.to_area(card, P1, 'deck')
            wrong = self.add(rig, fixtures.definition('SWSH5.Houndoom_96'), P1, 'discard')
            target = self.add(rig, fixtures.definition(target_path), P1, 'discard')
            ctx.choose_cards = AsyncMock(return_value=[target])
            await (ability.effect(ctx) if pokemon_card else d.effect(ctx))
            self.assertIn(target, ctx.hand())
            self.assertIn(wrong, ctx.discard_pile())
            self.assertEqual(ctx.choose_cards.call_args.args[1], 1)

    async def test_dream_ball_only_uses_prize_window_and_can_bench_an_evolution(self):
        rig, ctx, d = self.setup_card('SWSH7.DreamBall_146')
        self.assertFalse(self.legal(rig, ctx, d))
        target = self.add(rig, fixtures.definition('SM12.Flareon_25'), P1, 'deck')
        ctx.search_deck = AsyncMock(return_value=[target])
        await d.effect(ctx)
        self.assertTrue(ctx.search_deck.call_args.args[0](target))
        self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)
        self.assertIn(target, ctx.my_bench())
