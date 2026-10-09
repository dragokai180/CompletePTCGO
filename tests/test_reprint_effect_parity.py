"""Mechanically identical printings must run the same card effects."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _out_of_zone_ability_entries
from spirit.game.session.passives import ability_locked, compute_damage
from spirit.game.attributes import AttrID
from spirit.game.models.board import PokemonEntity
from spirit.tools.effect_smoke import P1, P2


class ReprintEffectParityTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_klefki_printings_lock_basic_abilities_and_joust_discards_tools(self):
        for path in ('SV1.Klefki_96', 'SV045.Klefki_159'):
            with self.subTest(card=path):
                rig, entities = self.rig(path)
                oranguru_def = fixtures.definition('SWSH1.Oranguru_148')
                oranguru = self.add(rig, oranguru_def, P2, 'bench')
                self.assertTrue(ability_locked(
                    rig.board, oranguru, oranguru_def.abilities[0]))

                tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'),
                                P2, 'hand')
                rig.attach(tool, rig.board.active_pokemon(P2))
                attack = next(a for a in fixtures.definition(path).abilities
                              if a.title == 'Joust')
                await attack.effect(EffectContext(
                    rig.session, P1, entities['target'], attack))
                self.assertIn(tool, rig.board.find_player_area(P2, 'discard').children)

    def test_bastiodon_printings_protect_team_only_while_benched(self):
        for path in ('ME5.Bastiodon_62', 'MEP.Bastiodon_85'):
            with self.subTest(card=path):
                rig, entities = self.rig(path)
                attacker = rig.board.active_pokemon(P2)
                target = entities['target']
                self.assertEqual(compute_damage(
                    rig.board, attacker, target, 100).amount, 0)

                bench_source = next(p for p in rig.board.pokemon_in_play(P1)
                                    if p is not target and
                                    p.archetype_id == target.archetype_id)
                self.assertFalse(is_in_active_spot(bench_source))
                rig.to_area(bench_source, P1, 'hand')
                self.assertGreater(compute_damage(
                    rig.board, attacker, target, 100).amount, 0)

    def test_pikachu_ex_printings_keep_tera_bench_protection(self):
        for path in (
            'SV08.Pikachuex_57', 'SV08.Pikachuex_219',
            'SV08.Pikachuex_238', 'SV08.Pikachuex_247',
            'ME2PT5.Pikachuex_57', 'ME2PT5.Pikachuex_277',
            'SV085.Pikachuex_179',
        ):
            with self.subTest(card=path):
                definition = fixtures.definition(path)
                self.assertIn('Tera', definition.subtypes)
                self.assertIn('Tera', definition.searchable_by)
                rig, entities = self.rig(path)
                attacker = rig.board.active_pokemon(P2)
                active = entities['target']
                benched = next(p for p in rig.board.pokemon_in_play(P1)
                               if p is not active and
                               p.archetype_id == active.archetype_id)
                self.assertGreater(compute_damage(
                    rig.board, attacker, active, 100).amount, 0)
                self.assertEqual(compute_damage(
                    rig.board, attacker, benched, 100).amount, 0)

    def test_propagation_can_be_offered_again_after_zone_change(self):
        for path in ('BW9.Exeggcute_4', 'BW10.Exeggcute_102'):
            with self.subTest(card=path):
                rig, entities = self.rig(path)
                discard = rig.board.find_player_area(P1, 'discard')
                egg = next(card for card in discard.children
                           if card.archetype_id == entities['target'].archetype_id)
                actions = _out_of_zone_ability_entries(
                    rig.board, rig.session.turn_state, P1, rig.session.game_id)
                action = next(entry for entry in actions
                              if entry['entityID'] == egg.entity_id)
                rig.session.turn_state.used_abilities.add((
                    egg.entity_id, action['selectableAction']['actionID']))
                self.assertTrue(any(entry['entityID'] == egg.entity_id
                                    for entry in _out_of_zone_ability_entries(
                                        rig.board, rig.session.turn_state,
                                        P1, rig.session.game_id)))

    async def test_explosion_y_reprints_discard_before_choosing_damage_target(self):
        for path in ('ME2PT5.MegaCharizardYex_22',
                     'MEP.MegaCharizardYex_30'):
            with self.subTest(card=path):
                rig, entities = self.rig(path)
                attack = fixtures.definition(path).abilities[0]
                ctx = EffectContext(rig.session, P1, entities['target'], attack)
                target = ctx.opponent_bench()[0]
                target.set_attribute(AttrID.HP, 500)
                while len(ctx.attached_energies(ctx.attacker)) < 3:
                    energy = rig.pull_guid(P1, next(iter(self.energies.values())))
                    self.assertIsNotNone(energy)
                    rig.attach(energy, ctx.attacker)
                energy_count = len(ctx.attached_energies(ctx.attacker))

                async def choose(candidates, count, **kwargs):
                    if candidates and isinstance(candidates[0], PokemonEntity):
                        return [target]
                    return list(candidates)[:count]

                ctx.choose_cards = AsyncMock(side_effect=choose)
                deal_damage = ctx.deal_damage

                async def damage_after_discard(*args, **kwargs):
                    self.assertEqual(len(ctx.attached_energies(ctx.attacker)),
                                     energy_count - 3)
                    return await deal_damage(*args, **kwargs)

                ctx.deal_damage = damage_after_discard
                await attack.effect(ctx)
                self.assertEqual(target.get_attribute(AttrID.HP), 220)


if __name__ == '__main__':
    unittest.main()
