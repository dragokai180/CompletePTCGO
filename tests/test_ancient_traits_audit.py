"""Ancient Trait regressions, including alternate printings and attachments."""
import unittest
import json
from pathlib import Path
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.game.session.passives import active_passives, compute_damage, effective_max_hp, tool_slots_free, extra_manual_energy_attachments, effective_heal_amount
from spirit.tools.effect_smoke import P1, P2
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.passives import def_for
from spirit.tools.import_xy_sets import internal_number
from spirit.tools.import_standard_sets import mechanics_signature
from spirit.game.card_effects.energies import RegenerativeEnergyPassive

class AncientTraitTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        fixtures.HgssRulesTests.setUpClass()
        cls.fixture = fixtures.HgssRulesTests()

    def rig(self, path):
        return self.fixture.rig(path)

    def add(self, rig, path, owner=P1, zone='hand'):
        return self.fixture.add(rig, fixtures.definition(path), owner, zone)

    def actions(self, rig, card=None):
        actions = compute_legal_actions(rig.board, rig.session.turn_state, P1, rig.session.game_id)
        return [a for a in actions if card is None or a['entityID'] == card.entity_id]

    async def test_all_traits_survive_ability_locks(self):
        paths = ['XY5.Swampert_36', 'XY5.Ludicolo_37', 'XY6.Altaria_74', 'XY6.Articuno_17', 'XY6.MRayquazaEX_61', 'XY7.Entei_15', 'XY7.PrimalKyogreEX_96', 'XY7.Golurk_35', 'XY5.Bunnelby_121', 'XY5.PrimalGroudonEX_86']
        for path in paths:
            for lock in ('none', 'hex', 'garbotoxin'):
                with self.subTest(path=path, lock=lock):
                    rig, e = self.rig(path)
                    if lock == 'hex':
                        rig.session.turn_state.abilities_disabled_through_turn = 99
                    elif lock == 'garbotoxin':
                        garbo = self.add(rig, 'XY9.Garbodor_57', P2, 'bench')
                        rig.attach(self.add(rig, 'BW9.FloatStone_99', P2), garbo)
                    passive = def_for(e['target'].archetype_id).passive
                    self.assertTrue(any(p is passive and c is e['target'] for p, c in active_passives(rig.board)))

    async def test_all_58_printings_match_printed_trait(self):
        source_dir = Path(__file__).resolve().parents[1] / 'tools/card-builder/data/pokemon-tcg-data/cards/en'
        stems = ('xy5', 'xy6', 'xy7', 'xyp')
        if not all((source_dir / (stem + '.json')).is_file() for stem in stems):
            self.skipTest('Optional local pokemon-tcg-data snapshot is not installed')
        count = 0
        for stem in stems:
            source = source_dir / (stem + '.json')
            for card in json.loads(source.read_text(encoding='utf-8')):
                if not card.get('ancientTrait'):
                    continue
                count += 1
                with self.subTest(card=card['id'], trait=card['ancientTrait']['name']):
                    code = 'Promo_XY' if stem == 'xyp' else stem.upper()
                    matches = [d for d in CARD_DEFS_BY_GUID.values() if d.set_code == code and str(d.collector_number) == str(internal_number(card, stem))]
                    self.assertEqual(len(matches), 1)
                    self.assertEqual(matches[0].passive.text, card['ancientTrait']['text'].lower())
        self.assertEqual(count, 58)

    async def test_alpha_growth_manual_limit(self):
        rig, e = self.rig('XY5.Swampert_36')
        target = e['target']
        self.assertEqual(extra_manual_energy_attachments(rig.board, target), 1)
        first = self.add(rig, 'BW1.WaterEnergy_107')
        await rig.session._execute_attach_energy(P1, first, self.actions(rig, first)[0], [target.entity_id])
        second = self.add(rig, 'BW1.FireEnergy_106')
        entry = self.actions(rig, second)[0]
        self.assertIn(target.entity_id, str(entry['targetInfoLst']))
        for other in rig.board.pokemon_in_play(P1):
            if other is not target:
                self.assertNotIn(other.entity_id, str(entry['targetInfoLst']))
        await rig.session._execute_attach_energy(P1, second, entry, [target.entity_id])
        self.assertFalse(self.actions(rig, self.add(rig, 'BW1.WaterEnergy_107')))

    async def test_alpha_growth_effect_does_not_consume_manual_attachment(self):
        rig, e = self.rig('XY5.Swampert_36')
        energy = self.add(rig, 'BW1.WaterEnergy_107')
        await EffectContext(rig.session, P1, e['target'], None).attach_energy(energy, e['target'])
        self.assertFalse(rig.session.turn_state.energy_attached)
        self.assertIsNone(rig.session.turn_state.bonus_energy_target_id)

    async def test_alpha_recovery_double_and_hp_cap(self):
        rig, e = self.rig('XY5.Ludicolo_37')
        target = e['target']
        target.set_attribute(AttrID.HP, effective_max_hp(rig.board, target) - 80)
        ctx = EffectContext(rig.session, P1, target, None)
        self.assertEqual(await ctx.heal(30, target), 60)
        self.assertEqual(await ctx.heal(30, target), 20)
        self.assertEqual(effective_heal_amount(rig.board, e['p2_active'], 30), 30)

    async def test_delta_evolution_first_turn(self):
        rig, e = self.rig('XY6.Altaria_74')
        basic = self.add(rig, 'XY6.Swablu_73', P1, 'bench')
        evolution = self.add(rig, 'XY6.Altaria_74')
        state = rig.session.turn_state
        state.turn_number = 1
        state.mark_entered_play(basic.entity_id)
        self.assertFalse(state.may_evolve_target(basic.entity_id))
        self.assertIn(basic.entity_id, str(self.actions(rig, evolution)))

    async def test_delta_plus_damage_only_and_bench(self):
        path = 'XY6.Articuno_17'
        rig, e = self.rig(path)
        definition = fixtures.definition(path)
        ctx = EffectContext(rig.session, P1, e['target'], definition.abilities[0])
        for target in rig.board.pokemon_in_play(P2):
            ctx.attack_damage.clear()
            self.assertEqual(definition.passive.modify_prizes_for_knockout(target, ctx, 1, e['target']), 1)
            ctx.attack_damage[target.entity_id] = 100
            self.assertEqual(definition.passive.modify_prizes_for_knockout(target, ctx, 1, e['target']), 2)
        ctx.attack_damage[e['target'].entity_id] = 100
        self.assertEqual(definition.passive.modify_prizes_for_knockout(e['target'], ctx, 1, e['target']), 1)

    async def test_delta_wild_four_types(self):
        rig, e = self.rig('XY6.MRayquazaEX_61')
        for kind in (PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.DARKNESS):
            with self.subTest(kind=kind):
                e['p2_active'].set_attribute(AttrID.POKEMON_TYPES, [kind.value])
                result = compute_damage(rig.board, e['p2_active'], e['target'], 50, ignore_weakness=True, ignore_resistance=True)
                expected = 30 if kind in (PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING) else 50
                self.assertEqual(result.amount, expected)

    async def test_theta_double_tool_limit(self):
        rig, e = self.rig('XY7.Entei_15')
        self.assertEqual(tool_slots_free(rig.board, e['target']), 2)
        for remaining in (1, 0):
            rig.attach(self.add(rig, 'BW9.FloatStone_99'), e['target'])
            self.assertEqual(tool_slots_free(rig.board, e['target']), remaining)
        self.assertNotIn(e['target'].entity_id, str(self.actions(rig, self.add(rig, 'BW9.FloatStone_99'))))

    async def test_theta_max_evolution_heal(self):
        for base, evolved in [('XY5.KyogreEX_54', 'XY7.PrimalKyogreEX_96'), ('XY5.GroudonEX_85', 'XY7.PrimalGroudonEX_97'), ('XY6.RayquazaEX_75', 'XY7.MRayquazaEX_98')]:
            with self.subTest(evolved=evolved):
                rig, e = self.rig(base)
                e['target'].set_attribute(AttrID.HP, 20)
                evolution = self.add(rig, evolved)
                ctx = EffectContext(rig.session, P1, e['target'], None)
                self.assertTrue(await ctx.evolve_pokemon(e['target'], evolution))
                self.assertEqual(evolution.get_attribute(AttrID.HP), effective_max_hp(rig.board, evolution))

    async def test_theta_stop_opposing_ability_counters(self):
        rig, e = self.rig('XY7.Golurk_35')
        source = self.add(rig, 'XY4.Golbat_32', P2, 'bench')
        ability = next(a for a in fixtures.definition('XY4.Golbat_32').abilities if a.title == 'Sneaky Bite')
        target = e['target']
        hp = target.get_attribute(AttrID.HP)
        await EffectContext(rig.session, P2, source, ability).deal_damage(20, target, as_counters=True)
        self.assertEqual(target.get_attribute(AttrID.HP), hp)
        await EffectContext(rig.session, P1, target, ability).deal_damage(20, target, as_counters=True)
        self.assertEqual(target.get_attribute(AttrID.HP), hp - 20)

    async def test_omega_barrage_two_attacks(self):
        rig, e = self.rig('XY5.Bunnelby_121')
        rig.session.prompt_player_choice = AsyncMock(return_value=0)
        attack = next(a for a in self.actions(rig, e['target']) if a['selectableAction']['description'] == 'UsePokemonAttack')
        before = len(rig.board.find_player_area(P2, 'deck').children)
        self.assertFalse(await rig.session._execute_attack(P1, e['target'], attack))
        self.assertEqual(len(rig.board.find_player_area(P2, 'deck').children), before - 1)
        self.assertFalse(self.actions(rig, self.add(rig, 'BW1.WaterEnergy_107')))
        self.assertTrue(await rig.session._execute_attack(P1, e['target'], attack))
        self.assertEqual(len(rig.board.find_player_area(P2, 'deck').children), before - 2)

    async def test_omega_barrier_sources(self):
        rig, e = self.rig('XY5.PrimalGroudonEX_86')
        for path, owner, expected in [('BW1.PlusPower_96', P2, True), ('XY2.Lysandre_90', P2, True), ('BW9.FloatStone_99', P2, False), ('BW1.PlusPower_96', P1, False)]:
            with self.subTest(path=path, owner=owner):
                trainer = self.add(rig, path, owner)
                ctx = EffectContext(rig.session, owner, trainer, None)
                ctx.is_trainer_effect = True
                self.assertEqual(ctx._trainer_blocked(e['target']), expected)

    async def test_omega_barrage_second_attack_after_knockout_and_promotion(self):
        rig, e = self.rig('XY5.Medicham_81')
        rig.session.prompt_player_choice = AsyncMock(return_value=0)
        e['p2_active'].set_attribute(AttrID.HP, 10)
        attack = [a for a in self.actions(rig, e['target']) if a['selectableAction']['description'] == 'UsePokemonAttack'][-1]
        self.assertFalse(await rig.session._execute_attack(P1, e['target'], attack))
        promoted = rig.board.find_player_area(P2, 'activePokemonArea').children[0]
        self.assertIsNot(promoted, e['p2_active'])
        self.assertTrue(any(a['selectableAction']['description'] == 'UsePokemonAttack' for a in self.actions(rig, e['target'])))
        self.assertTrue(await rig.session._execute_attack(P1, e['target'], attack))

    async def test_delta_wild_after_weakness_not_damage_counters(self):
        rig, e = self.rig('XY6.MRayquazaEX_61')
        target = e['target']
        target.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.FIRE.value])
        e['p2_active'].set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        self.assertEqual(compute_damage(rig.board, e['p2_active'], target, 50).amount, 80)
        hp = target.get_attribute(AttrID.HP)
        ctx = EffectContext(rig.session, P2, e['p2_active'], fixtures.definition('XY6.MRayquazaEX_61').abilities[0])
        await ctx.deal_damage(30, target, as_counters=True)
        self.assertEqual(target.get_attribute(AttrID.HP), hp - 30)

    async def test_omega_barrier_blocks_actual_crushing_hammer(self):
        rig, e = self.rig('XY5.PrimalGroudonEX_86')
        energy = rig.board.attached_energies(e['target'])[0]
        trainer = self.add(rig, 'BW2.CrushingHammer_92', P2)
        ctx = EffectContext(rig.session, P2, trainer, None)
        ctx.is_trainer_effect = True
        ctx.flip_coins = AsyncMock(return_value=[True])
        async def choose_target(pool, *args, **kwargs):
            self.assertIn(e['target'], pool)
            return e['target']
        async def choose_energy(pool, *args, **kwargs):
            self.assertIn(energy, pool)
            return [energy]
        ctx.choose_pokemon = AsyncMock(side_effect=choose_target)
        ctx.choose_cards = AsyncMock(side_effect=choose_energy)
        await def_for(trainer.archetype_id).effect(ctx)
        self.assertIn(energy, rig.board.attached_energies(e['target']))

    async def test_omega_barrier_does_not_block_stadium(self):
        rig, e = self.rig('XY5.PrimalGroudonEX_86')
        stadium = self.add(rig, 'XY3.FightingStadium_90', P2)
        ctx = EffectContext(rig.session, P2, stadium, None)
        ctx.is_trainer_effect = True
        self.assertFalse(ctx._trainer_blocked(e['target']))

    async def test_importer_distinguishes_traits_but_not_alternate_art(self):
        root = Path(__file__).resolve().parents[1] / 'tools/card-builder/data/pokemon-tcg-data/cards/en'
        cards = {}
        for stem in ('xy5', 'xy6', 'xy7'):
            cards.update((c['id'], c) for c in json.loads((root / (stem + '.json')).read_text(encoding='utf-8')))
        for base, new in [('xy5-55', 'xy7-96'), ('xy5-86', 'xy7-97'), ('xy6-76', 'xy7-98')]:
            with self.subTest(card=new):
                self.assertNotEqual(mechanics_signature(cards[base]), mechanics_signature(cards[new]))
        self.assertEqual(mechanics_signature(cards['xy5-55']), mechanics_signature(cards['xy5-149']))

    async def test_theta_max_evolution_from_deck_also_heals(self):
        rig, e = self.rig('XY5.KyogreEX_54')
        e['target'].set_attribute(AttrID.HP, 20)
        evolution = self.add(rig, 'XY7.PrimalKyogreEX_96', P1, 'deck')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        self.assertTrue(await ctx.evolve_pokemon(e['target'], evolution))
        self.assertEqual(evolution.get_attribute(AttrID.HP), 240)

    async def test_theta_max_does_not_keep_old_traits_or_mutate_originals(self):
        rig, e = self.rig('XY7.PrimalKyogreEX_96')
        self.assertEqual(extra_manual_energy_attachments(rig.board, e['target']), 0)
        original = self.add(rig, 'XY5.PrimalKyogreEX_55', P1, 'bench')
        self.assertEqual(extra_manual_energy_attachments(rig.board, original), 1)
        rig, e = self.rig('XY7.PrimalGroudonEX_97')
        trainer = self.add(rig, 'BW2.CrushingHammer_92', P2)
        ctx = EffectContext(rig.session, P2, trainer, None)
        ctx.is_trainer_effect = True
        self.assertFalse(ctx._trainer_blocked(e['target']))
        original = self.add(rig, 'XY5.PrimalGroudonEX_86', P1, 'bench')
        self.assertTrue(ctx._trainer_blocked(original))
        rig, e = self.rig('XY6.RayquazaEX_75')
        state = rig.session.turn_state
        state.turn_number = 1
        state.mark_entered_play(e['target'].entity_id)
        self.assertFalse(self.actions(rig, self.add(rig, 'XY7.MRayquazaEX_98')))
        self.assertTrue(self.actions(rig, self.add(rig, 'XY6.MRayquazaEX_76')))

    async def test_omega_barrier_attachment_shield_exceptions(self):
        for path, owner, blocked in [('BW2.CrushingHammer_92', P2, True),
                                     ('XY1.TeamFlareGrunt_129', P2, True),
                                     ('BW2.CrushingHammer_92', P1, False),
                                     ('XY3.FightingStadium_90', P2, False),
                                     ('BW9.FloatStone_99', P2, False)]:
            with self.subTest(path=path, owner=owner):
                rig, e = self.rig('XY5.PrimalGroudonEX_86')
                tool = self.add(rig, 'BW9.FloatStone_99')
                rig.attach(tool, e['target'])
                energy = rig.board.attached_energies(e['target'])[0]
                trainer = self.add(rig, path, owner)
                ctx = EffectContext(rig.session, owner, trainer, None)
                ctx.is_trainer_effect = True
                for attachment in (energy, tool):
                    self.assertEqual(ctx._trainer_blocked(attachment), blocked)
                await ctx.discard_cards([energy, tool])
                self.assertEqual(energy.parent is e['target'], blocked)
                self.assertEqual(tool.parent is e['target'], blocked)

    async def test_omega_barrier_does_not_prevent_attack_energy_discard(self):
        rig, e = self.rig('XY5.PrimalGroudonEX_86')
        energy = rig.board.attached_energies(e['target'])[0]
        attack = fixtures.definition('XY5.PrimalGroudonEX_86').abilities[0]
        ctx = EffectContext(rig.session, P2, e['p2_active'], attack)
        await ctx.discard_cards([energy])
        self.assertNotIn(energy, rig.board.attached_energies(e['target']))

    async def test_regenerative_energy_retains_from_hand_restriction(self):
        from spirit.game.card_effects import energies
        from unittest.mock import patch
        rig, e = self.rig('XY5.KyogreEX_54')
        energy = rig.board.attached_energies(e['target'])[0]
        passive = RegenerativeEnergyPassive()
        with patch.object(energies, 'is_pokemon_v', return_value=True):
            self.assertEqual(passive.heal_on_evolve(e['target'], e['target'], P1, energy, from_hand=True), 100)
            self.assertEqual(passive.heal_on_evolve(e['target'], e['target'], P1, energy, from_hand=False), 0)

    async def test_wyndon_stadium_retains_from_hand_restriction(self):
        for zone, healing in [('hand', 100), ('deck', 0)]:
            with self.subTest(zone=zone):
                rig, e = self.rig('SWSH4.AegislashV_126')
                base_max = effective_max_hp(rig.board, e['target'])
                e['target'].set_attribute(AttrID.HP, base_max - 150)
                stadium = self.add(rig, 'SWSH4.WyndonStadium_161')
                slot = rig.board.find_global_area('activeStadium')
                rig.board.move_card(stadium.entity_id, slot.entity_id)
                evolution = self.add(rig, 'SWSH4.AegislashVMAX_127', P1, zone)
                ctx = EffectContext(rig.session, P1, e['target'], None)
                self.assertTrue(await ctx.evolve_pokemon(e['target'], evolution))
                self.assertEqual(evolution.get_attribute(AttrID.HP),
                                 effective_max_hp(rig.board, evolution) - 150 + healing)

if __name__ == '__main__':
    unittest.main()
