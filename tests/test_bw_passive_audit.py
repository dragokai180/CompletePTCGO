"""Scope and units of BW passive rules."""
import unittest
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.passives import compute_damage, effective_max_hp, energy_provided_options
from spirit.tools.effect_smoke import P1,P2


class BwPassiveAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def strip(self,rig,pokemon):
        for energy in list(rig.board.attached_energies(pokemon)):
            rig.to_area(energy,pokemon.owning_player_id,'deck')

    async def test_leaf_tailor_requires_energy_not_tools(self):
        rig,e,ctx=self.ctx('BW3.Leavanny_3','Leaf Tailor')
        target=ctx.my_bench()[0]
        target.set_attribute(AttrID.WEAKNESS_TYPES,[PokemonTypes.FIRE.value])
        target.set_attribute(AttrID.RESISTANCE_TYPES,0)
        ctx.defender.set_attribute(AttrID.POKEMON_TYPES,[PokemonTypes.FIRE.value])
        self.strip(rig,target)
        self.assertEqual(compute_damage(rig.board,ctx.defender,target,20).amount,40)
        energy=rig.pull_guid(P1,self.energies[PokemonTypes.FIRE.value]); rig.attach(energy,target)
        self.assertEqual(compute_damage(rig.board,ctx.defender,target,20).amount,20)

    async def test_solar_revelation_needs_energy_not_just_an_attachment(self):
        rig,e,ctx=self.ctx('BW5.Espeon_48','Solar Revelation')
        target=ctx.my_bench()[0]
        self.strip(rig,target)
        tool=self.add(rig,definition('BW9.FloatStone_99'),P1,'hand'); target.add_child(tool)
        passive=ctx.ability.passive
        self.assertFalse(passive.blocks_attack_effects(target,ctx.source))
        energy=rig.pull_guid(P1,self.energies[PokemonTypes.FIRE.value]);rig.attach(energy,target)
        self.assertTrue(passive.blocks_attack_effects(target,ctx.source))

    async def test_sealing_scream_blocks_both_players(self):
        rig,e,ctx=self.ctx('BW11.Spiritomb_87','Sealing Scream')
        ace=self.add(rig,definition('BW7.ComputerSearch_137'),P1,'hand')
        for pid in (P1,P2):
            self.assertTrue(ctx.ability.passive.blocks_trainer_play(ace,pid,ctx.source))

    async def test_craftsmanship_counts_energy_units(self):
        rig,e,ctx=self.ctx('BW3.Conkeldurr_64','Craftsmanship')
        self.strip(rig,ctx.source)
        base=effective_max_hp(rig.board,ctx.source)
        energy=rig.pull_guid(P1,self.energies[PokemonTypes.FIGHTING.value]);rig.attach(energy,ctx.source)
        energy.set_attribute(AttrID.ENERGY_INFO,{'options':[[PokemonTypes.FIGHTING.value]*2]})
        self.assertEqual(effective_max_hp(rig.board,ctx.source),base+40)

    async def test_dark_aura_preserves_units_and_only_affects_holder(self):
        rig,e,ctx=self.ctx('BW3.Hydreigon_79','Dark Aura')
        energy=rig.pull_guid(P1,self.energies[PokemonTypes.FIRE.value]);rig.attach(energy,ctx.source)
        energy.set_attribute(AttrID.ENERGY_INFO,{'options':[[PokemonTypes.FIRE.value]*2]})
        self.assertEqual(energy_provided_options(rig.board,energy),[[PokemonTypes.DARKNESS.value]*2])
        rig.attach(energy,ctx.my_bench()[-1])
        self.assertEqual(energy_provided_options(rig.board,energy),[[PokemonTypes.FIRE.value]*2])

    async def test_psychic_mirage_does_not_stack(self):
        rig,e,ctx=self.ctx('BW4.Gardevoir_57','Psychic Mirage')
        self.add(rig,definition('BW4.Gardevoir_57'),P1,'bench')
        energy=rig.pull_guid(P1,self.energies[PokemonTypes.PSYCHIC.value]);rig.attach(energy,ctx.source)
        self.assertEqual(energy_provided_options(rig.board,energy),[[PokemonTypes.PSYCHIC.value]*2])
        other=ctx.my_bench()[0];other.set_attribute(AttrID.POKEMON_TYPES,[PokemonTypes.FIRE.value]);rig.attach(energy,other)
        self.assertEqual(energy_provided_options(rig.board,energy),[[PokemonTypes.PSYCHIC.value]])
