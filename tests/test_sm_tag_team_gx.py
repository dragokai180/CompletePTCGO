"""TAG TEAM GX tests assert bonus thresholds, base effects and real choices."""
import re
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.sm_tag_team_gx import extra_energy_satisfied
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.passives import effective_max_hp
from spirit.tools.effect_smoke import P1, P2

CASES = [
 ('SM10.GardevoirSylveonGX_130','Magical Miracle-GX'),
 ('SM10.GreninjaZoroarkGX_107','Dark Union-GX'),
 ('SM10.MarshadowMachampGX_82','Acme of Heroism-GX'),
 ('SM10.MukAlolanMukGX_61','Nasty Goo Mix-GX'),
 ('SM10.PheromosaBuzzwoleGX_1','Beast Game-GX'),
 ('SM11.MegaSableyeTyranitarGX_126','Gigafall-GX'),
 ('SM11.RaichuAlolanRaichuGX_54','Lightning Ride-GX'),
 ('SM11.RowletAlolanExeggutorGX_1','Tropical Hour-GX'),
 ('SM11.SlowpokePsyduckGX_35','Thrilling Times-GX'),
 ('SM12.BlastoisePiplupGX_38','Bubble Launcher-GX'),
 ('SM12.MegaLopunnyJigglypuffGX_165','Puffy Smashers-GX'),
 ('SM12.NaganadelGuzzlordGX_158','Chaotic Order-GX'),
 ('SM12.TogepiCleffaIgglybuffGX_143','Supreme Puff-GX'),
 ('SM9.GengarMimikyuGX_53','Horror House-GX'),
 ('SM9.LatiasLatiosGX_113','Aero Unit-GX'),
 ('Promo_SM.CharizardBraixenGX_230','Crimson Flame Pillar-GX'),
 ('Promo_SM.EspeonDeoxysGX_240','Cross Division-GX'),
 ('Promo_SM.UmbreonDarkraiGX_241','Dark Moon-GX'),
 ('Promo_SM.ReshiramCharizardGX_201','Double Blaze-GX'),
 ('Promo_SM.CelebiVenusaurGX_167','Evergreen-GX'),
 ('Promo_SM.LucarioMelmetalGX_192','Full Metal Wall-GX'),
 ('Promo_SM.GarchompGiratinaGX_193','GG End-GX'),
 ('Promo_SM.EeveeSnorlaxGX_169','Megaton Friends-GX'),
 ('Promo_SM.MewtwoMewGX_191','Miraculous Duo-GX'),
 ('Promo_SM.TrevenantDusknoirGX_217','Pale Moon-GX'),
 ('Promo_SM.MoltresZapdosArticunoGX_210','Sky Legends-GX'),
 ('Promo_SM.VenusaurSnivyGX_229','Solar Plant-GX'),
 ('Promo_SM.PikachuZekromGX_168','Tag Bolt-GX'),
 ('Promo_SM.MagikarpWailordGX_166','Towering Splash-GX'),
]


class TagTeamGxTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def setup_gx(self, path, title, boosted):
        rig, e, ctx = self.ctx(path, title)
        for energy in list(ctx.attached_energies(ctx.attacker)):
            rig.to_area(energy, P1, 'deck')
        def attach(kind, n):
            ptype = PokemonTypes.GRASS if kind == PokemonTypes.COLORLESS else kind
            definition = CARD_DEFS_BY_GUID[self.energies[ptype.value].lower()]
            for _ in range(n):
                rig.attach(self.add(rig, definition, P1, 'hand'), ctx.attacker)
        for kind, n in ctx.ability.cost.items():
            attach(kind, n)
        if boosted:
            clause = re.search(r"at least (.+?) attached to it", ctx.ability.game_text.lower()).group(1)
            for n, kind in re.findall(r"(\d+) extra (?:(\w+) )?energy", clause):
                attach(getattr(PokemonTypes, (kind or 'colorless').upper()), int(n))
            if title == 'Sky Legends-GX':
                for kind in (PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING):
                    attach(kind, 1)
        return rig, e, ctx

    async def test_every_gx_requires_bonus_energy_beyond_base_cost(self):
        for path, title in CASES:
            for boosted in (False, True):
                with self.subTest(title=title, boosted=boosted):
                    rig, e, ctx = self.setup_gx(path, title, boosted)
                    self.assertEqual(extra_energy_satisfied(ctx, ctx.ability.game_text), boosted)
                    ctx.deal_damage = AsyncMock(return_value=0)
                    ctx.apply_special_condition = AsyncMock()
                    ctx.shuffle_into_deck = AsyncMock()
                    ctx.discard_cards = AsyncMock()
                    ctx.take_prizes = AsyncMock()
                    ctx.reveal_cards = AsyncMock()
                    ctx.draw_until = AsyncMock()
                    ctx.heal = AsyncMock()
                    ctx.knock_out = AsyncMock()
                    ctx.place_damage_counters = AsyncMock()
                    ctx.choose_cards = AsyncMock(side_effect=lambda cards, n, **kw: cards[:n])
                    ctx.flip_coins = AsyncMock(side_effect=lambda n, *a: [True] * n)
                    ctx.choose_pokemon = AsyncMock(side_effect=lambda cards, *a: cards[0] if cards else None)
                    await ctx.ability.effect(ctx)
                    if title in ('Magical Miracle-GX', 'Tropical Hour-GX', 'Supreme Puff-GX'):
                        self.assertEqual(ctx.shuffle_into_deck.await_count, int(boosted))
                    if title == 'Gigafall-GX':
                        self.assertEqual(ctx.discard_cards.await_count, int(boosted))
                        if boosted:
                            self.assertEqual(len(ctx.discard_cards.call_args.args[0]), 15)
                    if title == 'Chaotic Order-GX':
                        ctx.reveal_cards.assert_awaited_once()
                        self.assertEqual(ctx.take_prizes.await_count, int(boosted))
                        if boosted:ctx.take_prizes.assert_awaited_once_with(2)
                    if title == 'Nasty Goo Mix-GX':
                        self.assertEqual(ctx.apply_special_condition.await_count, 2)
                        self.assertEqual(ctx.apply_special_condition.call_args.kwargs['poison_counters'],
                                         15 if boosted else 1)
                    if title == 'Bubble Launcher-GX':
                        ctx.deal_damage.assert_awaited_once_with(250 if boosted else 100)
                        ctx.apply_special_condition.assert_awaited_once()
                    if title == 'Lightning Ride-GX':
                        ctx.deal_damage.assert_awaited_once_with(250 if boosted else 150)
                        self.assertIsNot(rig.board.active_pokemon(P1), e['target'])
                    if title == 'Thrilling Times-GX':
                        ctx.flip_coins.assert_awaited_once_with(10 if boosted else 1, title)
                        ctx.deal_damage.assert_awaited_once_with(1010 if boosted else 110)
                    if title == 'Puffy Smashers-GX':
                        ctx.apply_special_condition.assert_awaited_once()
                        self.assertEqual(ctx.deal_damage.await_count, int(boosted))
                        if boosted:self.assertIn(ctx.deal_damage.call_args.kwargs['target'], ctx.opponent_bench())
                    if title == 'Beast Game-GX':
                        self.assertEqual(rig.session.turn_state.extra_prize_watchers[-1]['prizes'], 3 if boosted else 1)
                    if title == 'Horror House-GX':
                        self.assertEqual(ctx.draw_until.await_count, 2 if boosted else 0)
                    if title in ('Aero Unit-GX', 'Acme of Heroism-GX'):
                        self.assertEqual(bool(rig.board.temporary_passives), boosted)
                    if title == 'Crimson Flame Pillar-GX':
                        self.assertEqual(ctx.apply_special_condition.await_count, 2 if boosted else 0)
                    if title == 'Cross Division-GX':
                        self.assertEqual(ctx.place_damage_counters.call_args.args[0], 20 if boosted else 10)
                    if title == 'Dark Moon-GX':
                        self.assertEqual(ctx.knock_out.await_count, int(boosted))
                    if title == 'Double Blaze-GX':
                        ctx.deal_damage.assert_awaited_once_with(300 if boosted else 200, ignore_target_effects=boosted)
                    if title == 'Evergreen-GX':
                        ctx.heal.assert_awaited_once()
                        self.assertEqual(ctx.shuffle_into_deck.await_count, int(boosted))
                    if title == 'Full Metal Wall-GX':
                        self.assertTrue(rig.board.temporary_passives)
                        self.assertEqual(ctx.discard_cards.await_count, int(boosted))
                    if title == 'GG End-GX':
                        self.assertEqual(ctx.discard_cards.await_count, 2 if boosted else 1)
                    if title == 'Megaton Friends-GX':
                        self.assertEqual(ctx.draw_until.await_count, int(boosted))
                        if boosted:ctx.draw_until.assert_awaited_once_with(10)
                    if title == 'Miraculous Duo-GX':
                        self.assertEqual(ctx.heal.await_count, len(ctx.my_pokemon_in_play()) if boosted else 0)
                    if title == 'Pale Moon-GX':
                        self.assertEqual(len(rig.session.scheduled_effects), 1)
                        self.assertEqual(ctx.discard_cards.await_count, int(boosted))
                    if title == 'Sky Legends-GX':
                        ctx.shuffle_into_deck.assert_awaited_once()
                        self.assertEqual(ctx.deal_damage.await_count, min(3, len(ctx.opponent_pokemon_in_play())) if boosted else 0)
                    if title == 'Solar Plant-GX':
                        self.assertEqual(ctx.deal_damage.await_count, len(ctx.opponent_pokemon_in_play()))
                        self.assertEqual(ctx.heal.await_count, len(ctx.my_pokemon_in_play()) if boosted else 0)
                    if title == 'Tag Bolt-GX':
                        self.assertEqual(ctx.deal_damage.await_count, 2 if boosted else 1)
                    if title == 'Towering Splash-GX':
                        self.assertEqual(ctx.deal_damage.await_count, 1 + (len(ctx.opponent_bench()) if boosted else 0))

    async def test_dark_union_only_dark_gx_ex_and_two_energies_per_resurrected_pokemon(self):
        rig, e, ctx = self.setup_gx('SM10.GreninjaZoroarkGX_107', 'Dark Union-GX', True)
        one = self.add(rig, fixtures.definition('SM10.GreninjaZoroarkGX_107'), P1, 'discard')
        two = self.add(rig, fixtures.definition('SM11.MegaSableyeTyranitarGX_126'), P1, 'discard')
        # Preserve just the two explicit eligible Pokemon.
        for card in list(ctx.discard_pile()):
            if card not in (one, two) and getattr(card, 'archetype_id', '') == ctx.attacker.archetype_id:
                rig.to_area(card, P1, 'deck')
        before = set(ctx.my_bench())
        await ctx.ability.effect(ctx)
        entered = set(ctx.my_bench()) - before
        self.assertEqual(entered, {one, two})
        for pokemon in entered:
            self.assertEqual(len(ctx.attached_energies(pokemon)), 2)


    async def test_acme_survives_lethal_attack_only_with_bonus(self):
        from spirit.game.session.effects import EffectContext
        for boosted in (False, True):
            rig, e, ctx = self.setup_gx('SM10.MarshadowMachampGX_82', 'Acme of Heroism-GX', boosted)
            ctx.deal_damage = AsyncMock()
            await ctx.ability.effect(ctx)
            reply = EffectContext(rig.session, P2, ctx.defender, ctx.ability)
            await reply.deal_damage(1000, target=ctx.attacker)
            self.assertEqual(ctx.attacker.get_attribute(AttrID.HP), 10 if boosted else 0)

    async def test_pale_moon_delayed_effect_is_removed_by_switching(self):
        rig, e, ctx = self.setup_gx('Promo_SM.TrevenantDusknoirGX_217', 'Pale Moon-GX', False)
        await ctx.ability.effect(ctx)
        scheduled = rig.session.scheduled_effects[-1]
        self.assertTrue(scheduled['guard'](rig.board))
        original = ctx.defender
        replacement = ctx.opponent_bench()[0]
        await ctx.switch_active(P2, replacement)
        await ctx.switch_active(P2, original)
        self.assertFalse(scheduled['guard'](rig.board))

    async def test_gx_effects_respect_pokemon_shields(self):
        from spirit.game.session.passives import Passive
        class Shield(Passive):
            def blocks_attack_effects(self, target, carrier):
                return target is carrier
        for path, title in (
            ('Promo_SM.GarchompGiratinaGX_193', 'GG End-GX'),
            ('Promo_SM.TrevenantDusknoirGX_217', 'Pale Moon-GX'),
            ('Promo_SM.LucarioMelmetalGX_192', 'Full Metal Wall-GX'),
        ):
            rig, e, ctx = self.setup_gx(path, title, True)
            ctx.add_temporary_passive(ctx.defender, Shield())
            ctx.choose_cards = AsyncMock(return_value=[ctx.defender])
            ctx.discard_cards = AsyncMock()
            await ctx.ability.effect(ctx)
            ctx.discard_cards.assert_not_awaited()
            if title == 'Pale Moon-GX':
                self.assertFalse(rig.session.scheduled_effects)

    async def test_nasty_goo_mix_sets_real_poison_severity(self):
        for boosted in (False, True):
            rig, e, ctx = self.setup_gx('SM10.MukAlolanMukGX_61', 'Nasty Goo Mix-GX', boosted)
            await ctx.ability.effect(ctx)
            self.assertIn('Poisoned', ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS))
            self.assertIn('Paralyzed', ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS))
