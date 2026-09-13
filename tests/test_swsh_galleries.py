"""Gallery identities, reused mechanics, exclusive effects and image downloads."""
import importlib
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

from spirit.game.attributes import AttrID
from spirit.game.gallery_catalog import GALLERY_SETS, gallery_number
from spirit.game.card_effects import galleries
from spirit.game.data_utils import Attack
from spirit.tools import install_recent_card_art as installer
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.tools.effect_smoke import P1, P2
from spirit.game.session.effects import EffectContext


class GalleryCatalogTests(unittest.TestCase):
    def test_all_190_prints_have_unique_identity_and_printed_numbers(self):
        guids = set()
        count = 0
        for stem, (code, offset, size) in GALLERY_SETS.items():
            prefix = "GG" if stem.endswith("gg") else "TG"
            for n in range(1, size + 1):
                number = gallery_number(stem, f"{prefix}{n:02d}")
                paths = list((installer.SCRIPTS_ROOT / code).glob(f"*_{number}.py"))
                self.assertEqual(len(paths), 1, (code, number))
                module = importlib.import_module(f"spirit.game.scripts.cards.{code}.{paths[0].stem}")
                card = module.card
                self.assertEqual(card.collector_number, offset + n)
                self.assertEqual(card.set_code, code)
                self.assertEqual(card.extra_attributes["200790"]["value"], f"{prefix}{n:02d}")
                self.assertNotIn(card.guid, guids)
                guids.add(card.guid)
                count += 1
                if hasattr(module, "base_card"):
                    base = module.base_card
                    for attr in (AttrID.HP, AttrID.RETREAT_COST, AttrID.STAGE,
                                 AttrID.POKEMON_TYPES, AttrID.WEAKNESS_TYPES,
                                 AttrID.RESISTANCE_TYPES):
                        self.assertEqual(card.extra_attributes.get(str(attr.value)),
                                         base.extra_attributes.get(str(attr.value)),
                                         (code, number, attr))
                    self.assertNotEqual(card.guid, base.guid)
                    self.assertEqual(len(card.abilities), len(base.abilities))
                    for a, b in zip(card.abilities, base.abilities):
                        for field in ("title", "game_text", "vstar"):
                            self.assertEqual(getattr(a, field), getattr(b, field))
                        if isinstance(a, Attack):
                            self.assertEqual((a.cost, a.damage), (b.cost, b.damage))
        self.assertEqual(count, 190)

    def test_gallery_number_validation(self):
        for stem, (_code, offset, size) in GALLERY_SETS.items():
            prefix = "GG" if stem.endswith("gg") else "TG"
            self.assertEqual(gallery_number(stem, f"{prefix}01"), offset + 1)
            for bad in ("1", f"{prefix}00", f"{prefix}{size+1}"):
                with self.assertRaises(ValueError):
                    gallery_number(stem, bad)

    def test_installer_maps_gallery_slots_to_printed_urls(self):
        for stem, (code, offset, size) in GALLERY_SETS.items():
            entry = next(e for e in installer.RECENT_SETS.values() if e.set_code == code)
            urls = installer.load_image_urls(entry)
            prefix = "GG" if stem.endswith("gg") else "TG"
            for n in range(1, size + 1):
                candidates = installer.image_candidates(entry, str(offset+n), urls)
                self.assertIn(f"/{stem}/{prefix}{n:02d}_hires.png", candidates[0])
                self.assertIn(f"https://images.scrydex.com/pokemon/{stem}-{prefix}{n:02d}/large", candidates)
            self.assertIn("1", urls)

    def test_clean_checkout_fetches_catalog_without_live_or_bundles(self):
        response = Mock()
        response.json.return_value = [{"id": "swsh9tg-TG01"}]
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(installer, "DATA_ROOT", Path(directory)), \
                 patch.object(installer.requests, "get", return_value=response) as request:
                self.assertEqual(installer.load_catalog("swsh9tg"), response.json.return_value)
                self.assertIn("pokemon-tcg-data/master/cards/en/swsh9tg.json",
                              request.call_args.args[0])
                response.raise_for_status.assert_called_once()

    def test_deoxys_pre_evolution_is_downloadable_and_legal_in_expanded(self):
        entry = installer.RECENT_SETS["swshp"]
        self.assertEqual(entry.set_code, "Promo_SWSH")
        self.assertIn("/SWSH266_hires.png", installer.load_image_urls(entry)["266"])
        formats = json.loads((installer.ROOT / "spirit/database/json_data/formats.json").read_text())
        expanded = next(f for f in formats["formats"] if f["key"] == "Expanded")
        self.assertIn("Promo_SWSH", expanded["sets"])


class GalleryEffectsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_burnet_discards_up_to_two_and_can_fail(self):
        rig, e = self.rig("SWSH12.ProfessorBurnet_241", "trainer")
        ctx = EffectContext(rig.session, P1, e["target"], None)
        candidates = ctx.deck()[:2]
        ctx.choose_cards = AsyncMock(return_value=candidates)
        ctx.shuffle_deck = AsyncMock()
        await galleries.professor_burnet(ctx)
        self.assertTrue(all(c in ctx.discard_pile() for c in candidates))
        self.assertEqual(ctx.choose_cards.await_args.kwargs["minimum"], 0)
        ctx.shuffle_deck.assert_awaited_once()
        ctx.choose_cards = AsyncMock(return_value=[])
        await galleries.professor_burnet(ctx)
        self.assertEqual(ctx.shuffle_deck.await_count, 2)

    async def test_icicle_shot_locks_only_unprotected_defender(self):
        rig, e, ctx = self.ctx("CZ.GlaceonVSTAR_200", "Icicle Shot")
        ctx.deal_damage = AsyncMock()
        ctx.lock_retreat = Mock()
        ctx.effects_blocked = Mock(return_value=True)
        await ctx.ability.effect(ctx)
        ctx.lock_retreat.assert_not_called()
        ctx.effects_blocked.return_value = False
        await ctx.ability.effect(ctx)
        ctx.lock_retreat.assert_called_once_with(ctx.defender)

    async def test_crystal_star_is_vstar_and_grants_full_temporary_protection(self):
        rig, e, ctx = self.ctx("CZ.GlaceonVSTAR_200", "Crystal Star")
        self.assertTrue(ctx.ability.vstar)
        ctx.deal_damage = AsyncMock()
        ctx.add_passive_through_opponents_turn = Mock()
        await ctx.ability.effect(ctx)
        target, shield = ctx.add_passive_through_opponents_turn.call_args.args
        self.assertIs(target, ctx.attacker)
        self.assertTrue(shield.prevent_all)

    async def test_max_drain_heals_after_damage(self):
        rig, e, ctx = self.ctx("CZ.DeoxysVMAX_205", "Max Drain")
        calls = []
        async def hit(*a, **kw): calls.append("damage")
        async def heal(amount, target): calls.append((amount, target))
        ctx.deal_damage, ctx.heal = hit, heal
        await ctx.ability.effect(ctx)
        self.assertEqual(calls, ["damage", (30, ctx.attacker)])

    async def test_javelin_offers_only_opposing_benched_pokemon_v(self):
        rig, e, ctx = self.ctx("CZ.DeoxysVSTAR_206", "Psychic Javelin")
        v = self.add(rig, definition("CZ.GlaceonV_38"), P2, "bench")
        ctx.deal_damage = AsyncMock()
        ctx.choose_pokemon = AsyncMock(return_value=v)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_pokemon.await_args.args[0], [v])
        self.assertEqual(ctx.deal_damage.await_args.args, (60,))
        self.assertFalse(ctx.deal_damage.await_args.kwargs["apply_modifiers"])

    async def test_star_force_counts_energy_units_from_both_actives(self):
        rig, e, ctx = self.ctx("CZ.DeoxysVSTAR_206", "Star Force")
        self.assertTrue(ctx.ability.vstar)
        ctx.deal_damage = AsyncMock()
        with patch.object(galleries, "count_energy", side_effect=[lambda c: 2, lambda c: 3]):
            await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(300)

    async def test_protective_dna_reduces_only_opposing_vstar_attack_damage(self):
        carrier = SimpleNamespace(owning_player_id=P1)
        calc = SimpleNamespace(is_attack=True, is_opposing=True,
                               attacker=SimpleNamespace(archetype_id="test"),
                               target=SimpleNamespace(owning_player_id=P1), amount=100)
        passive = galleries.ProtectiveDNAPassive()
        with patch.object(galleries, "subtypes_for", return_value=["VSTAR"]):
            passive.modify_damage_taken(calc, carrier)
            self.assertEqual(calc.amount, 70)
            calc.is_attack = False
            passive.modify_damage_taken(calc, carrier)
            self.assertEqual(calc.amount, 70)
        calc.is_attack = True
        with patch.object(galleries, "subtypes_for", return_value=["VMAX"]):
            passive.modify_damage_taken(calc, carrier)
            self.assertEqual(calc.amount, 70)
