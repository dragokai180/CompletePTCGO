"""Action-menu permissions must reject impossible public prerequisites."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID, Ability, Attack
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.game.session.passives import effective_max_hp
from spirit.tools.effect_smoke import P1, P2, Rig


class ActivationResourcePermissionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def clear(self, rig, pid, zone, destination='deck'):
        for card in list(rig.board.find_player_area(pid, zone).children):
            rig.to_area(card, pid, destination)

    def stadium(self, card_def):
        rig = Rig(card_def, self.filler, self.energies, self.item)
        source = rig.setup('trainer')['target']
        rig.board.move_card(source.entity_id, rig.board.find_global_area('activeStadium').entity_id)
        source.owning_player_id = P1
        for pid in (P1, P2):
            for p in rig.board.pokemon_in_play(pid):
                p.set_attribute(AttrID.HP, effective_max_hp(rig.board, p))
        return rig, source

    def offered(self, rig, source, ability, pid=P1):
        return any(e['entityID'] == source.entity_id and
                   e['selectableAction']['actionID'] == ability.ability_id
                   for e in compute_legal_actions(rig.board, rig.session.turn_state,
                                                 pid, rig.session.game_id))

    def stadium_defs(self, names):
        return [d for d in CARD_DEFS_BY_GUID.values() if d.display_name in names
                and getattr(d, 'ability', None) is not None]

    async def test_tropical_beach_threshold_both_players_all_prints(self):
        for d in self.stadium_defs({'Tropical Beach'}):
            for pid in (P1, P2):
                for hand_size in (0, 6, 7, 8):
                    with self.subTest(card=d.guid, player=pid, hand=hand_size):
                        rig, source = self.stadium(d)
                        self.clear(rig, pid, 'hand')
                        for _ in range(hand_size):
                            self.add(rig, self.filler, pid, 'hand')
                        self.assertEqual(self.offered(rig, source, d.ability, pid), hand_size < 7)
                        self.clear(rig, pid, 'deck', 'discard')
                        self.assertFalse(self.offered(rig, source, d.ability, pid))

    async def test_invalid_beach_request_cannot_end_turn(self):
        d = definition('PROMO_BW.TropicalBeach_BW28')
        rig, source = self.stadium(d)
        while len(rig.board.find_player_area(P1, 'hand').children) < 7:
            self.add(rig, self.filler, P1, 'hand')
        with patch('spirit.game.session.game_session.resolve_activated_ability',
                   new_callable=AsyncMock) as effect:
            self.assertFalse(await rig.session._execute_use_ability(
                P1, source, {'selectableAction': {'actionID': d.ability.ability_id}}))
            effect.assert_not_awaited()

    async def test_stadium_searches_need_deck_but_not_hidden_matches(self):
        names = {'Artazon', 'Brooklet Hill', 'Lumiose City', 'Stormy Mountains',
                 'Fossil Quarry', 'Pokémon Research Lab', 'Mesagoza', 'Town Store',
                 'Turffield Stadium', 'Ultra Space', 'Spikemuth Gym'}
        for d in self.stadium_defs(names):
            with self.subTest(name=d.display_name, guid=d.guid):
                rig, source = self.stadium(d)
                self.clear(rig, P1, 'deck', 'discard')
                self.assertFalse(self.offered(rig, source, d.ability))
                # An Item cannot satisfy any of these searches, but that is private.
                self.add(rig, definition('HGSS1.Switch_102'), P1, 'deck')
                self.assertTrue(self.offered(rig, source, d.ability))

    async def test_bench_search_stadiums_require_space(self):
        names = {'Artazon', 'Brooklet Hill', 'Lumiose City', 'Pokémon Research Lab'}
        for d in self.stadium_defs(names):
            rig, source = self.stadium(d)
            bench = rig.board.find_player_area(P1, 'bench')
            while len(bench.children) < 5:
                self.add(rig, self.filler, P1, 'bench')
            with self.subTest(name=d.display_name):
                self.assertFalse(self.offered(rig, source, d.ability))

    async def test_discard_to_search_stadiums_require_payment_and_deck(self):
        for d in self.stadium_defs({'Giant Hearth', 'Viridian Forest'}):
            rig, source = self.stadium(d)
            self.clear(rig, P1, 'hand')
            self.assertFalse(self.offered(rig, source, d.ability))
            self.add(rig, self.filler, P1, 'hand')
            self.assertTrue(self.offered(rig, source, d.ability))
            self.clear(rig, P1, 'deck', 'discard')
            self.assertFalse(self.offered(rig, source, d.ability))

    async def test_public_energy_recovery_stadiums_filter_resources(self):
        specs = {'Burned Tower': PokemonTypes.FIRE, 'Training Court': PokemonTypes.FIRE,
                 'Mt. Coronet': PokemonTypes.METAL, 'Levincia': PokemonTypes.LIGHTNING}
        for d in self.stadium_defs(set(specs)):
            rig, source = self.stadium(d)
            self.clear(rig, P1, 'discard')
            self.add(rig, self.filler, P1, 'discard')
            with self.subTest(name=d.display_name, guid=d.guid):
                self.assertFalse(self.offered(rig, source, d.ability))
                energy_def = CARD_DEFS_BY_GUID[self.energies[specs[d.display_name].value].lower()]
                self.add(rig, energy_def, P1, 'discard')
                self.assertTrue(self.offered(rig, source, d.ability))

    async def test_healing_stadiums_require_own_eligible_damage(self):
        for d in self.stadium_defs({'Pokémon Center', 'Champions Festival'}):
            rig, source = self.stadium(d)
            if d.display_name == 'Champions Festival':
                while len(rig.board.pokemon_in_play(P1)) < 6:
                    self.add(rig, self.filler, P1, 'bench')
            self.assertFalse(self.offered(rig, source, d.ability))
            target = rig.board.find_player_area(P1, 'bench').children[0]
            target.set_attribute(AttrID.HP, effective_max_hp(rig.board, target) - 10)
            self.assertTrue(self.offered(rig, source, d.ability))

    async def test_draw_stadiums_and_shuffle_exception(self):
        for d in self.stadium_defs({'Battle City', 'Rose Tower', 'Jubilife Village'}):
            rig, source = self.stadium(d)
            self.clear(rig, P1, 'hand')
            self.assertTrue(self.offered(rig, source, d.ability))
            self.clear(rig, P1, 'deck', 'discard')
            self.assertFalse(self.offered(rig, source, d.ability))
            self.add(rig, self.filler, P1, 'hand')
            self.assertEqual(self.offered(rig, source, d.ability), d.display_name == 'Jubilife Village')

    async def test_pokemon_draw_and_search_actions_require_resources_all_prints(self):
        titles = {'Aerial Draw', 'Battle Sense', 'Buddy Catch', 'Cotton Lift', 'Dream Gift',
                  'Giga Magnet', 'Glaciated World', 'Greedy Tail', 'Hurried Gait', 'Instant Charge',
                  'Intrepid Sword', 'Metal Maker', 'Metallic Signal', 'Primal Turbo',
                  'Rapid Strike Search', 'Recon Directive', 'Roar of the Sword',
                  'Run Away Draw', 'Shining Arcana', 'Single Strike Roar', 'Starbirth',
                  'Sun-Drenched Shell', 'Tempting Tune', 'Vitality Spring', 'Voltage Beat',
                  'Azure Pulse', 'Phantom Star', 'Regal Stance', 'Abyssal Hand',
                  'Fusion Strike System', 'Dragon\'s Hoard', 'Gormandize'}
        checked = 0
        for d in list(CARD_DEFS_BY_GUID.values()):
            for a in getattr(d, 'abilities', []):
                if a.title not in titles:
                    continue
                rig = Rig(d, self.filler, self.energies, self.item)
                source = rig.setup('pokemon')['target']
                self.clear(rig, P1, 'deck', 'discard')
                with self.subTest(card=d.display_name, title=a.title, guid=d.guid):
                    self.assertFalse(self.offered(rig, source, a))
                checked += 1
        self.assertGreater(checked, 70)

    async def test_primate_wisdom_needs_both_hand_and_deck(self):
        rig, _, ctx = fixtures.HgssRulesTests.ctx(self, 'SWSH1.Oranguru_148', 'Primate Wisdom')
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
        self.clear(rig, P1, 'hand')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        self.add(rig, self.filler, P1, 'hand')
        self.clear(rig, P1, 'deck', 'discard')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))

    async def test_watch_over_only_counts_active_damage(self):
        rig, _, ctx = fixtures.HgssRulesTests.ctx(self, 'SWSH1.IndeedeeV_91', 'Watch Over')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        bench = rig.board.find_player_area(P1, 'bench').children[0]
        bench.set_attribute(AttrID.HP, effective_max_hp(rig.board, bench) - 10)
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        ctx.source.set_attribute(AttrID.HP, effective_max_hp(rig.board, ctx.source) - 10)
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))

    async def test_rumbling_engine_requires_energy_and_pays_before_hand_limit(self):
        rig, _, ctx = fixtures.HgssRulesTests.ctx(self, 'SV1.Revavroom_142', 'Rumbling Engine')
        self.clear(rig, P1, 'hand')
        for _ in range(5):
            self.add(rig, self.filler, P1, 'hand')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        energy = self.add(rig, CARD_DEFS_BY_GUID[self.energies[PokemonTypes.METAL.value].lower()], P1, 'hand')
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
        extra = self.add(rig, self.filler, P1, 'hand')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        rig.to_area(extra, P1, 'deck')
        before = len(ctx.deck())
        await ctx.ability.effect(ctx)
        self.assertIn(energy, rig.board.find_player_area(P1, 'discard').children)
        self.assertEqual(len(ctx.hand()), 6)
        self.assertEqual(len(ctx.deck()), before - 1)

    async def test_typed_discard_draw_stadiums_need_cost_and_deck(self):
        specs = {'Cycling Road': PokemonTypes.WATER, 'Heat Factory ◇': PokemonTypes.FIRE,
                 'Scorched Earth': PokemonTypes.FIGHTING}
        for d in self.stadium_defs(set(specs)):
            with self.subTest(card=d.display_name, guid=d.guid):
                rig, source = self.stadium(d)
                self.clear(rig, P1, 'hand')
                self.add(rig, self.filler, P1, 'hand')
                self.assertFalse(self.offered(rig, source, d.ability))
                self.add(rig, CARD_DEFS_BY_GUID[self.energies[specs[d.display_name].value].lower()], P1, 'hand')
                self.assertTrue(self.offered(rig, source, d.ability))
                self.clear(rig, P1, 'deck', 'discard')
                self.assertFalse(self.offered(rig, source, d.ability))

    async def test_prism_tower_requires_two_cards_and_a_nonempty_deck(self):
        for d in self.stadium_defs({'Prism Tower'}):
            rig, source = self.stadium(d)
            self.clear(rig, P1, 'hand')
            self.add(rig, self.filler, P1, 'hand')
            self.assertFalse(self.offered(rig, source, d.ability))
            self.add(rig, self.filler, P1, 'hand')
            self.assertTrue(self.offered(rig, source, d.ability))
            self.clear(rig, P1, 'deck', 'discard')
            self.assertFalse(self.offered(rig, source, d.ability))

    async def test_moonlit_hill_requires_psychic_payment_and_damage(self):
        for d in self.stadium_defs({'Moonlit Hill'}):
            rig, source = self.stadium(d)
            self.clear(rig, P1, 'hand')
            self.add(rig, CARD_DEFS_BY_GUID[self.energies[PokemonTypes.PSYCHIC.value].lower()], P1, 'hand')
            self.assertFalse(self.offered(rig, source, d.ability))
            target = rig.board.active_pokemon(P1)
            target.set_attribute(AttrID.HP, effective_max_hp(rig.board, target) - 10)
            self.assertTrue(self.offered(rig, source, d.ability))
            self.clear(rig, P1, 'hand')
            self.assertFalse(self.offered(rig, source, d.ability))

    async def test_mystery_garden_compares_hand_after_discard(self):
        for d in self.stadium_defs({'Mystery Garden'}):
            rig, source = self.stadium(d)
            self.clear(rig, P1, 'hand')
            for p in rig.board.pokemon_in_play(P1):
                p.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.PSYCHIC.value])
            count = len(rig.board.pokemon_in_play(P1))
            self.add(rig, CARD_DEFS_BY_GUID[self.energies[PokemonTypes.FIRE.value].lower()], P1, 'hand')
            for _ in range(count - 1):
                self.add(rig, self.filler, P1, 'hand')
            self.assertTrue(self.offered(rig, source, d.ability))
            extra = self.add(rig, self.filler, P1, 'hand')
            self.assertFalse(self.offered(rig, source, d.ability))
            rig.to_area(extra, P1, 'deck')
            self.clear(rig, P1, 'deck', 'discard')
            self.assertFalse(self.offered(rig, source, d.ability))

    async def test_unusable_stadium_effect_does_not_prevent_playing_stadium(self):
        d = definition('PROMO_BW.TropicalBeach_BW28')
        rig, source = self.stadium(d)
        rig.to_area(source, P1, 'hand')
        while len(rig.board.find_player_area(P1, 'hand').children) < 9:
            self.add(rig, self.filler, P1, 'hand')
        self.assertTrue(any(e['entityID'] == source.entity_id for e in compute_legal_actions(
            rig.board, rig.session.turn_state, P1, rig.session.game_id)))

    async def test_empty_public_resources_all_affected_ability_prints(self):
        titles = {'Downpour', 'Incendiary Song', 'Stance Change', 'Schooling',
                  'Evidence Gathering', 'Second Sight', 'Mischievous Trick', 'Shuffle Dance',
                  'Scampering Tail', 'Dimension Transfer', 'Wondrous Gift', 'Snack Search',
                  "Mermaid's Call", 'Voraciousness', 'Unseen Flash', 'Hurricane Charge',
                  'Pyro Dance', 'Busybody Nurse', 'Happiness Supplement', 'Boisterous Wind',
                  'Teleport Room', 'Scornful Storm', 'Wicked Ruler', 'Weed Out',
                  'Shady Move', 'Ominous Posture', 'Rocket Brain', 'Strange Behavior',
                  'Shadow Ear', 'Wormadam First', 'Shadow Void', 'Jet Geyser',
                  'Portrait', 'Psyscan', 'Night Scope', 'Search the Premises',
                  'Revealing Echo', 'Look for Prey', 'Dark Invitation', 'Irresistible Aroma',
                  'Sky Hunt', 'Peppy Pick'}
        seen = set()
        for d in list(CARD_DEFS_BY_GUID.values()):
            for a in getattr(d, 'abilities', []):
                if a.title not in titles or isinstance(a, Attack):
                    continue
                rig = Rig(d, self.filler, self.energies, self.item)
                source = rig.setup('pokemon')['target']
                for pid in (P1, P2):
                    for zone in ('hand', 'deck', 'discard'):
                        self.clear(rig, pid, zone, 'lostZone')
                    for p in rig.board.pokemon_in_play(pid):
                        p.set_attribute(AttrID.HP, effective_max_hp(rig.board, p))
                        for card in list(p.children):
                            rig.to_area(card, pid, 'lostZone')
                with self.subTest(title=a.title, card=d.guid):
                    self.assertFalse(self.offered(rig, source, a))
                seen.add(a.title)
        self.assertEqual(seen, titles)

    async def test_inline_discard_costs_require_correct_energy(self):
        for path, title, ptype in [('DM.Feraligatr_24', 'Downpour', PokemonTypes.WATER),
                                   ('SV4.Skeledirgeex_137', 'Incendiary Song', PokemonTypes.FIRE)]:
            rig, _, ctx = fixtures.HgssRulesTests.ctx(self, path, title)
            self.clear(rig, P1, 'hand')
            self.add(rig, CARD_DEFS_BY_GUID[self.energies[PokemonTypes.METAL.value].lower()], P1, 'hand')
            self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
            self.add(rig, CARD_DEFS_BY_GUID[self.energies[ptype.value].lower()], P1, 'hand')
            self.assertTrue(self.offered(rig, ctx.source, ctx.ability))

    async def test_stance_change_requires_named_card_not_any_pokemon(self):
        rig, _, ctx = fixtures.HgssRulesTests.ctx(self, 'XY1.Aegislash_85', 'Stance Change')
        self.clear(rig, P1, 'hand')
        self.add(rig, self.filler, P1, 'hand')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        self.add(rig, definition('XY1.Aegislash_86'), P1, 'hand')
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))

    async def test_metal_transfer_requires_matching_energy_and_distinct_target(self):
        rig, _, ctx = fixtures.HgssRulesTests.ctx(self, 'SWSH5.Bronzong_102', 'Metal Transfer')
        for p in rig.board.pokemon_in_play(P1):
            for c in list(p.children):
                rig.to_area(c, P1, 'discard')
        water = self.add(rig, CARD_DEFS_BY_GUID[self.energies[PokemonTypes.WATER.value].lower()], P1, 'hand')
        rig.attach(water, ctx.source)
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        metal = self.add(rig, CARD_DEFS_BY_GUID[self.energies[PokemonTypes.METAL.value].lower()], P1, 'hand')
        rig.attach(metal, ctx.source)
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
        self.clear(rig, P1, 'bench')
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))

    async def test_damage_transfer_counts_the_right_side(self):
        rig, _, ctx = fixtures.HgssRulesTests.ctx(self, 'SWSH5.Meowstic_61', 'Ear Moves')
        enemy = rig.board.active_pokemon(P2)
        enemy.set_attribute(AttrID.HP, effective_max_hp(rig.board, enemy) - 10)
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        ctx.source.set_attribute(AttrID.HP, effective_max_hp(rig.board, ctx.source) - 10)
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))

    async def test_required_public_target_or_attachment_all_prints(self):
        titles = {'Toxic Powder', 'Toxic Wetland', 'Shocking Light', 'Ancient Wing', 'Tag Transport'}
        seen = set()
        for d in list(CARD_DEFS_BY_GUID.values()):
            for a in getattr(d, 'abilities', []):
                if a.title not in titles:
                    continue
                rig = Rig(d, self.filler, self.energies, self.item)
                source = rig.setup('pokemon')['target']
                with self.subTest(title=a.title, guid=d.guid):
                    self.assertFalse(self.offered(rig, source, a))
                seen.add(a.title)
        self.assertEqual(seen, titles)

    async def test_heal_bench_does_not_count_active_only_damage(self):
        rig, _, ctx = fixtures.HgssRulesTests.ctx(self, 'SWSH9.ShayminVSTAR_14', 'Star Bloom')
        ctx.source.set_attribute(AttrID.HP, effective_max_hp(rig.board, ctx.source) - 30)
        self.assertFalse(self.offered(rig, ctx.source, ctx.ability))
        bench = rig.board.find_player_area(P1, 'bench').children[0]
        bench.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
        bench.set_attribute(AttrID.HP, effective_max_hp(rig.board, bench) - 10)
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))

    async def test_independent_potion_tails_branch_remains_available(self):
        rig, _, ctx = fixtures.HgssRulesTests.ctx(self, 'SWSH6.GalarianSlowking_98', 'Mysterious Potion')
        self.assertTrue(all(p.get_attribute(AttrID.HP) == effective_max_hp(rig.board, p)
                            for p in rig.board.pokemon_in_play(P1)))
        self.assertTrue(self.offered(rig, ctx.source, ctx.ability))
