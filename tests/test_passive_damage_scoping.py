import unittest
import uuid
from importlib import import_module

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import CARD_DEFS_BY_GUID, EnergyCardDef, PokemonCardDef
from spirit.game.models.board import BoardEntity, BoardState, create_card_entity
from spirit.game.models.card import Card
from spirit.game.session.passives import compute_damage


class PassiveDamageScopingTests(unittest.TestCase):
    def setUp(self):
        self.board = BoardState("damage-scoping", ["p1", "p2"])

    def _definition(self, path):
        return import_module("spirit.game.scripts.cards." + path).card

    def _place(self, definition, owner="p1", area="activeStadium", holder=None):
        raw = definition.to_archetype_dict()
        entity = create_card_entity(Card(
            raw["guid"], raw["key"], raw["attributes"],
            definition.display_name, subtypes=definition.subtypes,
        ), owner)
        destination = holder or (
            self.board.find_global_area(area) if area == "activeStadium"
            else self.board.find_player_area(owner, area)
        )
        destination.add_child(entity)
        self.board._register_entity(entity)
        return entity

    def _pokemon(self, owner, *, name="Test Pokemon", element=PokemonTypes.WATER,
                 stage=PokemonStage.BASIC, subtypes=(), area="activePokemonArea"):
        guid = str(uuid.uuid4())
        definition = PokemonCardDef(
            guid=guid, key="TEST", name=name, display_name=name,
            collector_number=1, set_code="TEST", rarity=Rarities.Common,
            hp=300, elements=[element], stage=stage, subtypes=list(subtypes),
        )
        self.addCleanup(CARD_DEFS_BY_GUID.pop, guid, None)
        return self._place(definition, owner, area)

    def _energy(self, pokemon, *, special=False, element=PokemonTypes.FIGHTING):
        guid = str(uuid.uuid4())
        definition = EnergyCardDef(
            guid=guid, key="TEST", name="Test Energy", collector_number=1,
            set_code="TEST", rarity=Rarities.Common, energy_type=element,
            is_special=special, provides=[[element]],
        )
        self.addCleanup(CARD_DEFS_BY_GUID.pop, guid, None)
        return self._place(definition, pokemon.owning_player_id, holder=pokemon)

    def _prizes(self, owner, count):
        pile = self.board.find_player_area(owner, "prizePile")
        for _ in range(count):
            pile.add_child(BoardEntity(owning_player_id=owner))

    def _damage(self, attacker, target, *, base=100, weakness=False, **kwargs):
        return compute_damage(
            self.board, attacker, target, base,
            ignore_weakness=not weakness, ignore_resistance=True, **kwargs,
        ).amount

    def test_dojo_both_prints_and_players_use_the_attackers_prizes(self):
        for printing in ("SM10.MartialArtsDojo_179", "SM12.MartialArtsDojo_268"):
            for owner in ("p1", "p2"):
                for attacker_id, defender_id in (("p1", "p2"), ("p2", "p1")):
                    for ours, theirs, expected in ((6, 6, 110), (6, 4, 140),
                                                   (3, 5, 110)):
                        with self.subTest(printing=printing, owner=owner,
                                          attacker=attacker_id, prizes=(ours, theirs)):
                            self.board = BoardState("dojo", ["p1", "p2"])
                            self._place(self._definition(printing), owner)
                            attacker = self._pokemon(attacker_id)
                            defender = self._pokemon(defender_id)
                            self._energy(attacker)
                            self._prizes(attacker_id, ours)
                            self._prizes(defender_id, theirs)
                            self.assertEqual(self._damage(attacker, defender), expected)

    def test_dojo_requires_basic_fighting_on_the_attacker(self):
        self._place(self._definition("SM10.MartialArtsDojo_179"))
        attacker, defender = self._pokemon("p1"), self._pokemon("p2")
        self._energy(self._pokemon("p1", area="bench"))
        self.assertEqual(self._damage(attacker, defender), 100)
        self._energy(attacker, special=True)
        self.assertEqual(self._damage(attacker, defender), 100)
        self._energy(attacker, element=PokemonTypes.WATER)
        self.assertEqual(self._damage(attacker, defender), 100)
        self._energy(attacker)
        self._energy(attacker)
        self.assertEqual(self._damage(attacker, defender), 110)

    def test_dojo_accepts_evolutions_and_other_types_but_not_ultra_beasts(self):
        self._place(self._definition("SM10.MartialArtsDojo_179"))
        defender = self._pokemon("p2")
        for subtypes, expected in (((), 110), (("Ultra Beast",), 100)):
            with self.subTest(subtypes=subtypes):
                attacker = self._pokemon("p1", element=PokemonTypes.FIRE,
                                         stage=PokemonStage.STAGE2, subtypes=subtypes)
                self._energy(attacker)
                self.assertEqual(self._damage(attacker, defender), expected)

    def test_dojo_only_modifies_attacks_to_the_opposing_active(self):
        stadium = self._place(self._definition("SM10.MartialArtsDojo_179"))
        attacker, defender = self._pokemon("p1"), self._pokemon("p2")
        bench = self._pokemon("p2", area="bench")
        self._energy(attacker)
        self.assertEqual(self._damage(attacker, bench), 100)
        self.assertEqual(self._damage(attacker, attacker), 100)
        self.assertEqual(self._damage(attacker, defender, is_attack=False), 100)
        self.assertEqual(self._damage(attacker, defender), 110)
        self.board.move_card(stadium.entity_id,
                             self.board.find_player_area("p1", "discard").entity_id)
        self.assertEqual(self._damage(attacker, defender), 100)

    def test_dojo_bonus_precedes_weakness_and_combines_with_choice_band(self):
        self._place(self._definition("SM10.MartialArtsDojo_179"))
        attacker = self._pokemon("p1", element=PokemonTypes.FIGHTING)
        defender = self._pokemon("p2", subtypes=["EX"])
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.FIGHTING.value])
        self._energy(attacker)
        self.assertEqual(self._damage(attacker, defender, weakness=True), 220)
        self._prizes("p1", 6)
        self._prizes("p2", 4)
        self.assertEqual(self._damage(attacker, defender, weakness=True), 280)
        self._place(self._definition("SM2.ChoiceBand_121"), holder=attacker)
        self.assertEqual(self._damage(attacker, defender, weakness=True), 340)

    def test_other_offensive_stadiums_apply_only_to_eligible_active_damage(self):
        cases = (
            ("HF.MistysCeruleanCityGym_61", {"name": "Starmie-GX"}, 140),
            ("SM4.DevouredField_93", {"element": PokemonTypes.DARKNESS}, 110),
            ("SM4.DevouredField_93", {"element": PokemonTypes.DRAGON}, 110),
            ("SV2.PracticeStudio_186", {"stage": PokemonStage.STAGE1}, 110),
            ("SV09.Postwick_154", {"name": "Hop's Snorlax"}, 130),
        )
        for path, properties, expected in cases:
            for attacker_id, defender_id in (("p1", "p2"), ("p2", "p1")):
                with self.subTest(stadium=path, attacker=attacker_id):
                    self.board = BoardState("other-stadiums", ["p1", "p2"])
                    self._place(self._definition(path))
                    attacker = self._pokemon(attacker_id, **properties)
                    defender = self._pokemon(defender_id)
                    bench = self._pokemon(defender_id, area="bench")
                    self.assertEqual(self._damage(attacker, defender), expected)
                    self.assertEqual(self._damage(attacker, bench), 100)
                    ineligible = self._pokemon(attacker_id)
                    self.assertEqual(self._damage(ineligible, defender), 100)

    def test_fighting_stadium_is_exclusive_to_fighting_against_uppercase_ex(self):
        self._place(self._definition("XY3.FightingStadium_90"))
        attacker = self._pokemon("p1", element=PokemonTypes.FIGHTING)
        for label, expected in (("EX", 120), ("GX", 100), ("ex", 100), ("V", 100)):
            with self.subTest(target=label):
                defender = self._pokemon("p2", subtypes=[label])
                self.assertEqual(self._damage(attacker, defender), expected)
                self.board.move_card(defender.entity_id,
                                     self.board.find_player_area("p2", "bench").entity_id)
                self.assertEqual(self._damage(attacker, defender), 100)
        defender = self._pokemon("p2", subtypes=["EX"])
        attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        self.assertEqual(self._damage(attacker, defender), 100)

    def test_choice_band_still_allows_ex_and_gx_but_never_bench_or_modern_ex(self):
        attacker = self._pokemon("p1")
        self._place(self._definition("SM2.ChoiceBand_121"), holder=attacker)
        for label, expected in (("EX", 130), ("GX", 130), ("ex", 100), ("V", 100)):
            with self.subTest(target=label):
                defender = self._pokemon("p2", subtypes=[label])
                self.assertEqual(self._damage(attacker, defender), expected)
                self.board.move_card(defender.entity_id,
                                     self.board.find_player_area("p2", "bench").entity_id)
                self.assertEqual(self._damage(attacker, defender), 100)

    def test_defensive_stadiums_never_reduce_the_protected_pokemons_own_attack(self):
        cases = (
            ("SM2.AetherParadiseConservationArea_116", {"element": PokemonTypes.GRASS}, 70),
            ("SM2.AetherParadiseConservationArea_116", {"element": PokemonTypes.LIGHTNING}, 70),
            ("HF.BrocksPewterCityGym_54", {"name": "Onix-GX"}, 60),
            ("SV05.FullMetalLab_148", {"element": PokemonTypes.METAL}, 70),
            ("SV10.GraniteCave_166", {"name": "Steven's Metagross ex"}, 70),
        )
        for path, properties, expected in cases:
            for owner, opponent in (("p1", "p2"), ("p2", "p1")):
                with self.subTest(stadium=path, owner=owner, properties=properties):
                    self.board = BoardState("defensive-stadium", ["p1", "p2"])
                    self._place(self._definition(path))
                    protected = self._pokemon(owner, **properties)
                    other = self._pokemon(opponent)
                    self.assertEqual(self._damage(protected, other), 100)
                    self.assertEqual(self._damage(other, protected), expected)
                    self.board.move_card(protected.entity_id,
                                         self.board.find_player_area(owner, "bench").entity_id)
                    self.assertEqual(self._damage(other, protected), expected)

    def test_full_metal_lab_reduction_is_once_after_weakness(self):
        self._place(self._definition("SV05.FullMetalLab_148"))
        attacker = self._pokemon("p1", element=PokemonTypes.FIRE)
        defender = self._pokemon("p2", element=PokemonTypes.METAL)
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.FIRE.value])
        self.assertEqual(self._damage(attacker, defender, weakness=True), 170)
        self.assertEqual(self._damage(attacker, defender, is_attack=False), 100)

    def test_aether_paradise_excludes_evolutions_and_other_types(self):
        self._place(self._definition("SM2.AetherParadiseConservationArea_116"))
        attacker = self._pokemon("p1")
        for element, stage in ((PokemonTypes.GRASS, PokemonStage.STAGE1),
                               (PokemonTypes.LIGHTNING, PokemonStage.STAGE2),
                               (PokemonTypes.WATER, PokemonStage.BASIC)):
            with self.subTest(element=element, stage=stage):
                defender = self._pokemon("p2", element=element, stage=stage)
                self.assertEqual(self._damage(attacker, defender), 100)

    def test_perilous_jungle_does_not_add_attack_damage(self):
        self._place(self._definition("SV05.PerilousJungle_156"))
        attacker, defender = self._pokemon("p1"), self._pokemon("p2")
        self.assertEqual(self._damage(attacker, defender), 100)

    def test_pressure_reduces_once_before_weakness_and_protects_bench_too(self):
        attacker = self._pokemon("p1", element=PokemonTypes.WATER)
        defender = self._place(self._definition("SV3.Entei_30"), "p2", "activePokemonArea")
        bench = self._pokemon("p2", area="bench")
        self.assertEqual(self._damage(attacker, defender, weakness=True), 160)
        self.assertEqual(self._damage(attacker, bench), 80)
        self.assertEqual(self._damage(defender, attacker), 100)
        self.board.move_card(defender.entity_id,
                             self.board.find_player_area("p2", "bench").entity_id)
        self.assertEqual(self._damage(attacker, bench), 100)

    def test_shield_energy_errata_reduces_after_weakness(self):
        attacker = self._pokemon("p1", element=PokemonTypes.FIRE)
        defender = self._pokemon("p2", element=PokemonTypes.METAL)
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.FIRE.value])
        self._place(self._definition("XY5.ShieldEnergy_143"), "p2", holder=defender)
        self.assertEqual(self._damage(attacker, defender, weakness=True), 190)
        self.assertEqual(self._damage(defender, attacker), 100)
        bench = self._pokemon("p2", area="bench")
        self.assertEqual(self._damage(attacker, bench), 100)
        self._place(self._definition("XY5.ShieldEnergy_143"), "p2", holder=defender)
        self.assertEqual(self._damage(attacker, defender, weakness=True), 180)

    def test_own_team_auras_never_boost_the_opponent_and_keep_nonstacking(self):
        aura = self._definition("SM10.Incineroar_29")
        self._place(aura, "p1", "bench")
        self._place(aura, "p1", "bench")
        attacker, defender = self._pokemon("p1"), self._pokemon("p2")
        self.assertEqual(self._damage(attacker, defender), 130)
        self.assertEqual(self._damage(defender, attacker), 100)
        self._place(aura, "p2", "bench")
        self.assertEqual(self._damage(attacker, defender), 130)
        self.assertEqual(self._damage(defender, attacker), 130)

    def test_named_team_auras_apply_to_the_named_ally_not_the_source_or_enemy(self):
        cases = (
            ("XY11.Nidoking_45", "Nidoqueen", 120),
            ("Promo_SM.Regirock_74", "Registeel", 110),
            ("SM11.Zygarde_124", "Zygarde-GX", 120),
            ("DM.Wishiwashi_31", "Wishiwashi-GX", 120),
        )
        for path, name, expected in cases:
            with self.subTest(source=path, ally=name):
                self.board = BoardState("named-auras", ["p1", "p2"])
                self._place(self._definition(path), "p1", "bench")
                attacker = self._pokemon("p1", name=name)
                defender = self._pokemon("p2", name=name)
                self.assertEqual(self._damage(attacker, defender), expected)
                self.assertEqual(self._damage(defender, attacker), 100)
                unnamed = self._pokemon("p1")
                self.assertEqual(self._damage(unnamed, defender), 100)
                bench = self._pokemon("p2", name=name, area="bench")
                self.assertEqual(self._damage(attacker, bench), 100)

    def test_pressure_singular_attack_wording_is_also_before_weakness(self):
        attacker = self._pokemon("p1", element=PokemonTypes.WATER)
        defender = self._place(self._definition("Promo_SM.Mewtwo_77"), "p2", "activePokemonArea")
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.WATER.value])
        self.assertEqual(self._damage(attacker, defender, weakness=True), 160)
        self.assertEqual(self._damage(attacker, self._pokemon("p2", area="bench")), 80)
        self.assertEqual(self._damage(defender, attacker), 100)


if __name__ == "__main__":
    unittest.main()
