"""Authored SWSH effects previously skipped by the generic smoke fixture."""
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext, full_stack
from spirit.game.session.passives import effective_bench_capacity
from spirit.tools.effect_smoke import P1, P2


class SwshConditionalCoverageTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def energy(self, rig, kind=PokemonTypes.PSYCHIC, zone='hand'):
        return self.add(rig, CARD_DEFS_BY_GUID[self.energies[kind.value].lower()], P1, zone)

    async def test_named_energy_targets_hand_and_discard(self):
        for path, target_path, energy_type, zone in (
            ('SWSH8.Latias_193','SWSH8.Latios_194',PokemonTypes.PSYCHIC,'hand'),
            ('SWSH8.Latios_194','SWSH8.Latias_193',PokemonTypes.PSYCHIC,'hand'),
            ('PGO.Solrock_39','PGO.Lunatone_34',PokemonTypes.PSYCHIC,'discard'),
            ('CZ.Solrock_69','PGO.Lunatone_34',PokemonTypes.PSYCHIC,'discard'),
            ('SWSH11.Finneon_40','SWSH11.Lumineon_41',PokemonTypes.WATER,'hand'),
        ):
            with self.subTest(card=path):
                rig, e = self.rig(path)
                ability = fixtures.definition(path).abilities[0]
                ctx = EffectContext(rig.session, P1, e['target'], ability)
                self.assertFalse(ability.condition(rig.board, P1, e['target']))
                target = self.add(rig, fixtures.definition(target_path), P1, 'bench')
                for c in list(ctx.hand() if zone == 'hand' else ctx.discard_pile()):
                    if c is not e['target']:rig.to_area(c, P1, 'deck')
                self.assertFalse(ability.condition(rig.board, P1, e['target']))
                energy = self.energy(rig, energy_type, zone)
                wrong = self.energy(rig, PokemonTypes.FIRE, zone)
                self.assertTrue(ability.condition(rig.board, P1, e['target']))
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.choose_cards = AsyncMock(return_value=[energy])
                ctx.choose_pokemon = AsyncMock(return_value=target)
                await ability.effect(ctx)
                self.assertIs(energy.parent, target)
                self.assertNotIn(wrong, ctx.choose_cards.call_args.args[0])
                self.assertEqual(ctx.choose_pokemon.call_args.args[0], [target])

    async def test_ancient_wisdom_requires_every_regi_and_moves_special_energy(self):
        rig, e = self.rig('SWSH10.Regigigas_130')
        ability = fixtures.definition('SWSH10.Regigigas_130').abilities[0]
        ctx = EffectContext(rig.session, P1, e['target'], ability)
        self.assertFalse(ability.condition(rig.board, P1, e['target']))
        for pokemon in list(ctx.my_bench()):rig.to_area(pokemon, P1, 'discard')
        for name in ('Regirock_75','Regice_37','Registeel_108','Regieleki_51'):
            self.add(rig, fixtures.definition('SWSH10.' + name), P1, 'bench')
        self.assertFalse(ability.condition(rig.board, P1, e['target']))
        self.add(rig, fixtures.definition('SWSH10.Regidrago_118'), P1, 'bench')
        self.assertTrue(ability.condition(rig.board, P1, e['target']))
        energies = [self.energy(rig, zone='discard') for _ in range(2)]
        energies.append(self.add(rig, fixtures.definition('SM11.RecycleEnergy_212'), P1, 'discard'))
        ctx.choose_cards = AsyncMock(return_value=energies)
        ctx.choose_pokemon = AsyncMock(return_value=e['target'])
        await ability.effect(ctx)
        self.assertTrue(all(c.parent is e['target'] for c in energies))
        ctx.choose_pokemon.assert_awaited_once()

    async def test_phantom_transformation_replaces_active_without_damage_or_attachments(self):
        rig, e = self.rig('SWSH7.Zoroark_103')
        source = e['target']
        ability = fixtures.definition('SWSH7.Zoroark_103').abilities[0]
        ctx = EffectContext(rig.session, P1, source, ability)
        for c in list(ctx.discard_pile()):rig.to_area(c, P1, 'deck')
        duplicate = self.add(rig, fixtures.definition('SWSH7.Zoroark_103'), P1, 'discard')
        self.assertFalse(ability.condition(rig.board, P1, source))
        target = self.add(rig, fixtures.definition('SM12.Jolteon_70'), P1, 'discard')
        energy = self.energy(rig)
        rig.attach(energy, source)
        source.set_attribute(AttrID.HP, 10)
        self.assertTrue(ability.condition(rig.board, P1, source))
        ctx.choose_cards = AsyncMock(return_value=[target])
        await ability.effect(ctx)
        self.assertIs(ctx.my_active(), target)
        self.assertNotIn(duplicate, ctx.choose_cards.call_args.args[0])
        self.assertIn(source, ctx.discard_pile())
        self.assertIn(energy, ctx.discard_pile())
        self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target))
        self.assertFalse(ctx.knockouts)

    async def test_special_transfer_excludes_basic_and_original_holder(self):
        rig, e = self.rig('SWSH9.Dusknoir_62')
        ability = fixtures.definition('SWSH9.Dusknoir_62').abilities[0]
        ctx = EffectContext(rig.session, P1, e['target'], ability)
        for pokemon in ctx.my_pokemon_in_play():
            for energy in list(ctx.attached_energies(pokemon)):rig.to_area(energy,P1,'discard')
        self.assertFalse(ability.condition(rig.board,P1,e['target']))
        energy = self.add(rig, fixtures.definition('SM11.RecycleEnergy_212'),P1,'hand')
        rig.attach(energy,e['target'])
        basic = self.energy(rig)
        rig.attach(basic,e['target'])
        target = ctx.my_bench()[0]
        self.assertTrue(ability.condition(rig.board,P1,e['target']))
        ctx.choose_cards = AsyncMock(return_value=[energy])
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ability.effect(ctx)
        self.assertIs(energy.parent,target)
        self.assertNotIn(basic,ctx.choose_cards.call_args.args[0])
        self.assertNotIn(e['target'],ctx.choose_pokemon.call_args.args[0])

    async def test_summoning_star_respects_expanded_bench_and_rule_boxes(self):
        rig, e = self.rig('SWSH12.LugiaVStar_139')
        ability = fixtures.definition('SWSH12.LugiaVStar_139').abilities[0]
        ctx = EffectContext(rig.session,P1,e['target'],ability)
        for card in list(ctx.discard_pile()):rig.to_area(card,P1,'deck')
        valid = [self.add(rig,fixtures.definition('SWSH12.Archeops_147'),P1,'discard') for _ in range(2)]
        wrong = self.add(rig,fixtures.definition('SWSH12.LugiaVStar_139'),P1,'discard')
        stadium = self.add(rig,fixtures.definition('XY6.SkyField_89'),P1,'hand')
        rig.board.move_card(stadium.entity_id,rig.board.find_global_area('activeStadium').entity_id)
        self.assertEqual(effective_bench_capacity(rig.board,P1),8)
        while len(ctx.my_bench()) < 7:self.add(rig,self.filler,P1,'bench')
        self.assertTrue(ability.condition(rig.board,P1,e['target']))
        ctx.choose_cards = AsyncMock(return_value=[valid[0]])
        await ability.effect(ctx)
        self.assertIn(valid[0],ctx.my_bench())
        self.assertEqual(ctx.choose_cards.call_args.args[1],1)
        self.assertNotIn(wrong,ctx.choose_cards.call_args.args[0])
        self.assertFalse(ability.condition(rig.board,P1,e['target']))

    async def test_electric_start_only_second_player_and_both_setup_positions(self):
        rig, e = self.rig('Promo_SM.Manectric_130')
        rig.board.setup_first_player_id = P1
        first = self.add(rig, fixtures.definition('Promo_SM.Manectric_130'),P1,'hand')
        second = self.add(rig, fixtures.definition('Promo_SM.Manectric_130'),P2,'hand')
        self.assertNotIn(first,rig.board.setup_active_candidates(P1))
        self.assertNotIn(first,rig.board.setup_bench_candidates(P1))
        self.assertIn(second,rig.board.setup_active_candidates(P2))
        self.assertIn(second,rig.board.setup_bench_candidates(P2))
        self.assertNotIn(second,rig.board.basic_pokemon_in_hand(P2))

    def previous_turn(self, rig, records):
        state=rig.session.turn_state
        state.active_player_id=P1
        state.attacks_used=list(records)
        state.begin_turn(P2,rig.board)
        opponent=rig.board.active_pokemon(P2)
        state.attacks_used=[(opponent.entity_id,opponent.archetype_id,'Opponent attack')]
        state.begin_turn(P1,rig.board)

    async def test_named_attack_chains_survive_intervening_turn_and_departure(self):
        from spirit.game.data_utils import Attack
        for path, prior_path, prior_title, title in (
            ('SWSH12.Dedenne_85','SWSH12.Togedemaru_127','Toge Dash','Dede-Short'),
            ('SWSH12.Morpeko_116','SWSH12.Dedenne_85','Dede-Short','Peko Blaster'),
        ):
            rig,e=self.rig(path)
            attack=next(a for a in fixtures.definition(path).abilities if isinstance(a,Attack) and a.title==title)
            self.assertFalse(attack.condition(rig.board,P1,e['target']))
            old=self.add(rig,fixtures.definition(prior_path),P1,'discard')
            self.previous_turn(rig,[(old.entity_id,old.archetype_id,prior_title)])
            self.assertTrue(attack.condition(rig.board,P1,e['target']))
            ctx=EffectContext(rig.session,P1,e['target'],attack)
            ctx.deal_damage=AsyncMock(return_value=60)
            ctx.apply_special_condition=AsyncMock()
            await attack.effect(ctx)
            if title=='Dede-Short':ctx.apply_special_condition.assert_awaited_once()
            else:self.assertEqual(ctx.deal_damage.await_count,len(ctx.opponent_pokemon_in_play()))
            # Passing a turn clears the player's chain; an opponent's use never supplies it.
            rig.session.turn_state.attacks_used=[]
            rig.session.turn_state.begin_turn(P2,rig.board)
            rig.session.turn_state.attacks_used=[(old.entity_id,old.archetype_id,prior_title)]
            rig.session.turn_state.begin_turn(P1,rig.board)
            self.assertFalse(attack.condition(rig.board,P1,e['target']))

    async def test_cavern_tackle_cannot_chain_after_previous_user_leaves(self):
        rig,e=self.rig('SWSH12.Terrakion_97')
        attack=fixtures.definition('SWSH12.Terrakion_97').abilities[0]
        self.assertTrue(attack.condition(rig.board,P1,e['target']))
        old=self.add(rig,fixtures.definition('SWSH12.Terrakion_97'),P1,'discard')
        self.previous_turn(rig,[(old.entity_id,old.archetype_id,'Cavern Tackle')])
        self.assertFalse(attack.condition(rig.board,P1,e['target']))

    async def test_self_attack_history_and_immediate_retaliation_history_are_separate(self):
        from spirit.game.card_effects.attacks_common import previous_attack_matches
        rig,e=self.rig('SWSH9.Breloom_4')
        attack=fixtures.definition('SWSH9.Breloom_4').abilities[-1]
        self.previous_turn(rig,[(e['target'].entity_id,e['target'].archetype_id,'Spore Ball')])
        self.assertTrue(attack.condition(rig.board,P1,e['target']))
        self.assertFalse(attack.condition(rig.board,P1,rig.board.pokemon_in_play(P1)[-1]))
        ctx=EffectContext(rig.session,P1,e['target'],attack)
        self.assertFalse(ctx.attack_used_last_turn(title='Spore Ball',entity=e['target']))
        self.assertTrue(previous_attack_matches(rig.board,P1,title='Spore Ball',entity=e['target']))
        rig.session.turn_state.attacks_used=[]
        rig.session.turn_state.begin_turn(P1,rig.board)
        self.assertFalse(previous_attack_matches(rig.board,P1,title='Spore Ball',entity=e['target']))

    async def test_cross_fist_uses_departed_rapid_strike_not_opponents_history(self):
        rig,e=self.rig('SWSH6.ZeraoraV_53')
        attack=fixtures.definition('SWSH6.ZeraoraV_53').abilities[0]
        prior=self.add(rig,fixtures.definition('SWSH6.Zebstrika_51'),P1,'discard')
        self.previous_turn(rig,[(prior.entity_id,prior.archetype_id,'An attack')])
        ctx=EffectContext(rig.session,P1,e['target'],attack)
        ctx.deal_damage=AsyncMock(return_value=100)
        ctx.choose_pokemon=AsyncMock(return_value=ctx.opponent_bench()[0])
        await attack.effect(ctx)
        self.assertEqual(ctx.deal_damage.await_count,2)
        self.assertEqual(ctx.deal_damage.call_args.args[0],160)
        self.assertFalse(ctx.deal_damage.call_args.kwargs['apply_modifiers'])
        rig.session.turn_state.attacks_prev_turn_by_player[P1]=[]
        ctx.deal_damage.reset_mock()
        await attack.effect(ctx)
        ctx.deal_damage.assert_awaited_once()

    async def test_lost_zone_attacks_require_ten_and_execute_effect_not_damage(self):
        from spirit.game.data_utils import Attack
        for path,title in (('SWSH11.GiratinaVSTAR_131','Star Requiem'),('SWSH11.Sableye_70','Lost Mine')):
            rig,e=self.rig(path)
            attack=next(a for a in fixtures.definition(path).abilities if isinstance(a,Attack) and a.title==title)
            for _ in range(9):self.add(rig,self.filler,P1,'lostZone')
            self.assertFalse(attack.condition(rig.board,P1,e['target']))
            self.add(rig,self.filler,P1,'lostZone')
            self.assertTrue(attack.condition(rig.board,P1,e['target']))
            ctx=EffectContext(rig.session,P1,e['target'],attack)
            ctx.knock_out=AsyncMock()
            ctx.place_damage_counters=AsyncMock()
            await attack.effect(ctx)
            if title=='Star Requiem':ctx.knock_out.assert_awaited_once_with(ctx.opponent_active())
            else:ctx.place_damage_counters.assert_awaited_once_with(12,ctx.opponent_pokemon_in_play())

    async def test_twilight_inspiration_requires_one_opposing_prize_and_awards_two(self):
        rig,e=self.rig('PGO.Slowbro_20')
        attack=fixtures.definition('PGO.Slowbro_20').abilities[-1]
        self.assertFalse(attack.condition(rig.board,P1,e['target']))
        prizes=rig.board.find_player_area(P2,'prizePile')
        for card in list(prizes.children)[1:]:rig.to_area(card,P2,'deck')
        self.assertTrue(attack.condition(rig.board,P1,e['target']))
        ctx=EffectContext(rig.session,P1,e['target'],attack)
        ctx.take_prizes=AsyncMock()
        await attack.effect(ctx)
        ctx.take_prizes.assert_awaited_once_with(2)
