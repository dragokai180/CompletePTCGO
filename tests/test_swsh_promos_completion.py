"""Promo catalog parity, compound outcomes, alternate V-UNION and installer."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from PIL import Image
from tests import test_hgss_rules as f
from spirit.game.attributes import AttrID
from spirit.game.data_utils import CARD_DEFS_BY_GUID, Attack, def_for, Triggers
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext
from spirit.game.vunion import can_assemble, assemble
from spirit.tools.effect_smoke import P1, P2
from spirit.tools import install_recent_card_art as installer


class SwshPromoTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(f.HgssRulesTests.setUpClass.__func__)
    rig = f.HgssRulesTests.rig
    add = f.HgssRulesTests.add

    def card(self, rig, path, owner=P1, zone='hand'):
        return self.add(rig, f.definition(path), owner, zone)

    def ctx(self, path, title):
        rig, e = self.rig('Promo_SWSH.' + path)
        source = e['target']
        ability = next(a for a in def_for(source.archetype_id).abilities if a.title == title)
        return rig, source, EffectContext(rig.session, P1, source, ability)

    def test_all_prints_have_identity_stats_attacks_and_art_urls(self):
        rows = json.loads((installer.DATA_ROOT / 'swshp.json').read_text(encoding='utf-8'))
        definitions = {d.collector_number: d for d in CARD_DEFS_BY_GUID.values() if d.set_code == 'Promo_SWSH'}
        self.assertEqual(len(rows), 304)
        self.assertEqual(len(definitions), 298)
        urls = installer.load_image_urls(installer.RECENT_SETS['swshp'])
        for row in rows:
            n = int(row['number'][4:])
            if any('cannot be used at official tournaments' in text.lower() for text in row.get('rules', [])):
                self.assertNotIn(n, definitions)
                continue
            d = definitions[n]
            with self.subTest(number=n):
                self.assertEqual(d.display_name, row['name'])
                self.assertIn(str(n), urls)
                self.assertIn(row['number'], urls[str(n)])
                if row['supertype'] != 'Pokémon' or 'V-UNION' in row.get('subtypes', []): continue
                model = loader.cards_by_guid[d.guid.lower()]
                self.assertEqual(model.get_attribute_value(AttrID.HP), int(row['hp']))
                attacks = [a for a in d.abilities if isinstance(a, Attack)]
                self.assertEqual(len(attacks), len(row.get('attacks', [])))
                for a, printed in zip(attacks, row.get('attacks', [])):
                    self.assertEqual(a.title, printed['name'])
                    self.assertEqual(sum(a.cost.values()), printed['convertedEnergyCost'])
                    if '1 VSTAR Power' in printed.get('text', ''):
                        self.assertTrue(a.vstar, a.title)

    async def test_teapot_bottoms_one_random_card_only_after_opposing_active_hit(self):
        rig, source, ctx = self.ctx('PolteageistV_21', 'Teapot of Surprises')
        self.assertTrue(ctx.ability.has_trigger(Triggers.ON_DAMAGED_BY_ATTACK))
        ctx.damage_amount = 10
        ctx.damaged_by = ctx.opponent_active()
        victim = ctx.hand(P2)[0]
        with patch('spirit.game.card_effects.swsh_promos.random.choice', return_value=victim):
            await ctx.ability.effect(ctx)
        self.assertIn(victim, ctx.deck(P2))
        self.assertNotIn(victim, ctx.hand(P2))
        before = len(ctx.hand(P2))
        rig.to_area(source, P1, 'bench')
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.hand(P2)), before)

    async def test_twinkle_counts_live_types_and_does_not_reveal_results(self):
        rig, source, ctx = self.ctx('RadiantEevee_230', 'Twinkle Gathering')
        self.card(rig, 'BW1.Tepig_15', P1, 'bench')
        ctx.search_deck = AsyncMock(return_value=[])
        ctx.put_in_hand = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertGreaterEqual(ctx.search_deck.call_args.kwargs['count'], 2)
        self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)
        self.assertNotIn('reveal', ctx.put_in_hand.call_args.kwargs)

    async def test_tail_charge_and_flight_up_attach_three_to_one_recipient(self):
        for path, title, energy in [('PikachuVMAX_286','Tail Charge','BW1.LightningEnergy_108'),
                                     ('Flapple_189','Flight Up','BW1.FireEnergy_106')]:
            rig, source, ctx = self.ctx(path, title)
            cards = [self.card(rig, energy, P1, 'discard') for _ in range(3)]
            target = ctx.my_bench()[0]
            ctx.choose_cards = AsyncMock(return_value=cards)
            ctx.choose_pokemon = AsyncMock(return_value=target)
            await ctx.ability.effect(ctx)
            self.assertTrue(all(c.parent is target for c in cards))
            ctx.choose_pokemon.assert_awaited_once()

    async def test_manaphy_benches_opponents_basics_not_own(self):
        rig, source, ctx = self.ctx('Manaphy_275', 'Pulling Currents')
        cards = [self.card(rig, 'BW1.Snivy_1', P2) for _ in range(2)]
        ctx.choose_cards = AsyncMock(return_value=cards)
        await ctx.ability.effect(ctx)
        self.assertTrue(all(c in ctx.opponent_bench() for c in cards))
        self.assertTrue(all(c not in ctx.my_bench() for c in cards))

    async def test_pursuit_claw_uses_selected_bench_damage_not_active(self):
        rig, source, ctx = self.ctx('Weavile_246', 'Pursuit Claw')
        target = ctx.opponent_bench()[0]
        target.set_attribute(AttrID.HP, ctx.max_hp(target) - 20)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args, (40, target))

    async def test_alternate_morpeko_accepts_mixed_art_but_not_duplicate_quadrants(self):
        rig, _ = self.rig('BW1.Snivy_1')
        duplicates = [self.card(rig, f'Promo_SWSH.MorpekoVUNION_{n}', P1, 'discard')
                      for n in (287, 215, 288, 216)]
        self.assertFalse(can_assemble(rig.board, P1, duplicates[0]))
        for mixed in (False, True):
            rig, e = self.rig('BW1.Snivy_1')
            nums = (287, 216, 289, 218) if mixed else (287, 288, 289, 290)
            parts = [self.card(rig, f'Promo_SWSH.MorpekoVUNION_{n}', P1, 'discard') for n in nums]
            self.assertTrue(can_assemble(rig.board, P1, parts[0]))
            ctx = EffectContext(rig.session, P1, parts[0], def_for(parts[0].archetype_id).abilities[0])
            result = await assemble(ctx)
            self.assertEqual(result.get_attribute(AttrID.COLLECTOR_NUMBER), 287)
            self.assertEqual(result.get_attribute(AttrID.IMAGE_FALLBACK_1), 'to290')
            self.assertEqual(len(result.physical_parts), 4)

    def test_installer_promos_use_padded_ids_even_without_metadata(self):
        urls = installer.image_candidates(installer.RECENT_SETS['swshp'], '1', {})
        self.assertEqual(urls[0], 'https://images.pokemontcg.io/swshp/SWSH001_hires.png')
        self.assertIn('SWSH001', urls[1])

    def test_installer_prefers_native_promos_without_erasing_downloads_for_gaps(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / 'scripts' / 'Promo_SWSH'
            assets = root / 'assets' / 'Promo_SWSH'
            scripts.mkdir(parents=True); assets.mkdir(parents=True)
            for stem in ('Grookey_1', 'Arcanine_304'):
                (scripts / (stem + '.py')).touch()
                Image.new('RGB', (10,20), 'blue').save(assets / (stem + '.png'))
            def restore(code, number, destination, **kwargs):
                if number == '1':
                    Image.new('RGB', (10,20), 'red').save(destination)
                    return True
                return False
            with patch.object(installer, 'SCRIPTS_ROOT', scripts.parent), \
                    patch.object(installer, 'ASSETS_ROOT', assets.parent), \
                    patch('spirit.tools.ptcgo_local_assets.import_swsh_promo_foils') as foils, \
                    patch('spirit.tools.import_vunion.import_vunion', return_value=[]) as composites, \
                    patch('spirit.tools.ptcgo_local_assets.install_card_art', side_effect=restore) as native:
                installer.restore_native_promos('native-cache')
                foils.assert_called_once_with(Path('native-cache'))
                composites.assert_called_once_with(Path('native-cache'))
                with Image.open(assets / 'Grookey_1.png') as image:
                    self.assertEqual(image.getpixel((0,0)), (255,0,0))
                with Image.open(assets / 'Arcanine_304.png') as image:
                    self.assertEqual(image.getpixel((0,0)), (0,0,255))
                self.assertTrue(all(c.kwargs['source'] == 'native-cache' for c in native.call_args_list))

    def test_installer_combines_alternate_quadrants_and_preserves_native(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / 'scripts' / 'Promo_SWSH'
            assets = root / 'assets' / 'Promo_SWSH'
            scripts.mkdir(parents=True); assets.mkdir(parents=True)
            colors = ['red', 'green', 'blue', 'yellow']
            for n, color in zip(range(287,291), colors):
                (scripts / f'MorpekoVUNION_{n}.py').touch()
                Image.new('RGB', (10,20), color).save(assets / f'MorpekoVUNION_{n}.png')
            with patch.object(installer, 'SCRIPTS_ROOT', scripts.parent), patch.object(installer, 'ASSETS_ROOT', assets.parent):
                self.assertEqual(installer.assemble_downloaded_vunion_faces(), [])
                target = assets / 'MorpekoVUNION_alternate_combined.png'
                before = target.read_bytes()
                with Image.open(target) as image:
                    self.assertEqual(image.size, (20,40))
                    self.assertEqual(image.getpixel((15,30)), (255,255,0))
                self.assertEqual(installer.assemble_downloaded_vunion_faces(), [])
                self.assertEqual(target.read_bytes(), before)
