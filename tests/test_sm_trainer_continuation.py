"""Public-zone Trainer prerequisites and multi-category SM recovery."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.game.session.passives import compute_damage
from spirit.tools.effect_smoke import P1, P2


class SmTrainerContinuationTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_card(self,path):
        rig,e=self.rig(path,'trainer')
        return rig,e,EffectContext(rig.session,P1,e['target'],None),fixtures.definition(path)

    def playable(self,rig,ctx,definition):
        return trainer_condition_met(definition.condition,rig.board,P1,ctx.source)

    def energy(self,rig,kind=PokemonTypes.WATER,zone='hand'):
        return self.add(rig,CARD_DEFS_BY_GUID[self.energies[kind.value].lower()],P1,zone)

    def clear_discard(self,rig,ctx):
        for card in list(ctx.discard_pile()):rig.to_area(card,P1,'deck')

    async def test_aether_employee_only_recovers_alolan_pokemon(self):
        rig,e,ctx,definition=self.setup_card('SM8.AetherFoundationEmployee_168')
        self.clear_discard(rig,ctx)
        wrong=self.add(rig,self.filler,P1,'discard')
        self.assertFalse(self.playable(rig,ctx,definition))
        valid=[self.add(rig,fixtures.definition('Promo_SM.AlolanMarowakGX_187'),P1,'discard') for _ in range(3)]
        self.assertTrue(self.playable(rig,ctx,definition))
        await definition.effect(ctx)
        self.assertTrue(all(c in ctx.hand() for c in valid))
        self.assertIn(wrong,ctx.discard_pile())

    async def test_lusamine_accepts_stadium_and_supporter_not_item(self):
        rig,e,ctx,definition=self.setup_card('SM4.Lusamine_96')
        self.clear_discard(rig,ctx)
        wrong=self.add(rig,self.item,P1,'discard')
        self.assertFalse(self.playable(rig,ctx,definition))
        stadium=self.add(rig,fixtures.definition('SM11.GiantHearth_197'),P1,'discard')
        self.assertTrue(self.playable(rig,ctx,definition))
        supporter=self.add(rig,fixtures.definition('SM9.Dana_137'),P1,'discard')
        await definition.effect(ctx)
        self.assertIn(stadium,ctx.hand())
        self.assertIn(supporter,ctx.hand())
        self.assertIn(wrong,ctx.discard_pile())

    async def test_lanas_fishing_rod_recovers_one_of_each_available_category(self):
        for pokemon_count,tool_count in ((2,2),(1,0),(0,1)):
            rig,e,ctx,definition=self.setup_card('SM12.LanasFishingRod_195')
            self.clear_discard(rig,ctx)
            self.energy(rig,zone='discard')
            self.assertFalse(self.playable(rig,ctx,definition))
            pokemon=[self.add(rig,self.filler,P1,'discard') for _ in range(pokemon_count)]
            tools=[self.add(rig,fixtures.definition('SM3.WishfulBaton_128'),P1,'discard') for _ in range(tool_count)]
            self.assertTrue(self.playable(rig,ctx,definition))
            await definition.effect(ctx)
            self.assertEqual(sum(c in ctx.deck() for c in pokemon),min(1,pokemon_count))
            self.assertEqual(sum(c in ctx.deck() for c in tools),min(1,tool_count))

    async def test_beast_ball_inspects_all_prizes_and_swaps_only_ultra_beast(self):
        rig,e,ctx,definition=self.setup_card('SM7.BeastBall_125')
        beast=self.add(rig,fixtures.definition('SM10.PheromosaBuzzwoleGX_1'),P1,'prizePile')
        before=len(rig.board.find_player_area(P1,'prizePile').children)
        ctx.reveal_cards=AsyncMock()
        ctx.choose_cards=AsyncMock(return_value=[beast])
        await definition.effect(ctx)
        self.assertIn(beast,ctx.hand())
        self.assertIs(ctx.source.parent,rig.board.find_player_area(P1,'prizePile'))
        self.assertEqual(len(ctx.source.parent.children),before)
        self.assertEqual(ctx.choose_cards.call_args.args[0],[beast])
        self.assertEqual(len(ctx.reveal_cards.call_args_list[0].args[0]),before)

    async def test_lusamine_prism_protects_ultra_beasts_and_expires(self):
        rig,e,ctx,definition=self.setup_card('SM8.Lusamine_182')
        self.assertFalse(self.playable(rig,ctx,definition))
        beast=self.add(rig,fixtures.definition('SM10.PheromosaBuzzwoleGX_1'),P1,'bench')
        prizes=rig.board.find_player_area(P2,'prizePile')
        for c in list(prizes.children)[3:]:rig.to_area(c,P2,'deck')
        self.assertTrue(self.playable(rig,ctx,definition))
        rig.session.turn_state.turn_number=4
        await definition.effect(ctx)
        rig.session.turn_state.begin_turn(P2,rig.board)
        attacker=ctx.opponent_active()
        def damage(target):
            return compute_damage(rig.board,attacker,target,50,ignore_weakness=True,ignore_resistance=True).amount
        self.assertEqual(damage(beast),0)
        self.assertEqual(damage(ctx.my_active()),50)
        rig.session.turn_state.begin_turn(P1,rig.board)
        self.assertEqual(damage(beast),50)

    async def test_zinnia_requires_prior_ko_and_attaches_to_one_dragon(self):
        rig,e,ctx,definition=self.setup_card('DM.Zinnia_64')
        target=self.add(rig,fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'),P1,'bench')
        other=self.add(rig,fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'),P1,'bench')
        energies=[self.energy(rig) for _ in range(2)]
        self.assertFalse(self.playable(rig,ctx,definition))
        rig.session.turn_state.kos_suffered_last_turn={P1:[{'archetype_id':target.archetype_id}]}
        self.assertTrue(self.playable(rig,ctx,definition))
        ctx.choose_cards=AsyncMock(return_value=energies)
        ctx.choose_pokemon=AsyncMock(return_value=target)
        await definition.effect(ctx)
        self.assertTrue(all(c.parent is target for c in energies))
        self.assertEqual(ctx.choose_pokemon.call_args.args[0],[target,other])
        ctx.choose_pokemon.assert_awaited_once()

    async def test_aqua_patch_benched_water_and_masked_royal_stage_two_only(self):
        for path,target_path,kind,zone in (
            ('SM2.AquaPatch_119','PGO.Lunatone_34',PokemonTypes.WATER,'discard'),
            ('SM7.TheMaskedRoyal_139','SL.Venusaur_3',PokemonTypes.GRASS,'hand'),
        ):
            rig,e,ctx,definition=self.setup_card(path)
            target=self.add(rig,fixtures.definition(target_path),P1,'bench')
            if 'AquaPatch' in path:target.set_attribute(AttrID.POKEMON_TYPES,[PokemonTypes.WATER.value])
            energy=self.energy(rig,kind,zone)
            self.assertTrue(self.playable(rig,ctx,definition))
            ctx.choose_cards=AsyncMock(return_value=[energy])
            ctx.choose_pokemon=AsyncMock(return_value=target)
            await definition.effect(ctx)
            self.assertIs(energy.parent,target)
            if ctx.choose_pokemon.await_count:self.assertEqual(ctx.choose_pokemon.call_args.args[0],[target])

    async def test_cyrus_opponent_selects_two_survivors_and_other_stacks_return(self):
        rig,e,ctx,definition=self.setup_card('SM5.Cyrus_120')
        active=ctx.my_active()
        active.set_attribute(AttrID.POKEMON_TYPES,[PokemonTypes.FIRE.value])
        self.assertFalse(self.playable(rig,ctx,definition))
        active.set_attribute(AttrID.POKEMON_TYPES,[PokemonTypes.METAL.value])
        while len(ctx.opponent_bench())<4:self.add(rig,self.filler,P2,'bench')
        keep=ctx.opponent_bench()[:2]
        removed=ctx.opponent_bench()[2:]
        attached=self.energy(rig)
        rig.attach(attached,removed[0])
        self.assertTrue(self.playable(rig,ctx,definition))
        ctx.choose_cards=AsyncMock(return_value=keep)
        await definition.effect(ctx)
        self.assertEqual(ctx.opponent_bench(),keep)
        self.assertEqual(ctx.choose_cards.call_args.kwargs['player_id'],P2)
        self.assertTrue(all(c in ctx.deck(P2) for c in removed))
        self.assertIn(attached,ctx.deck(P2))
        self.assertFalse(self.playable(rig,ctx,definition))

    async def test_nanu_keeps_damage_attachments_and_rejects_nonbasic_darkness(self):
        rig,e,ctx,definition=self.setup_card('SM9.Nanu_150')
        self.clear_discard(rig,ctx)
        wrong=self.add(rig,fixtures.definition('SWSH7.Zoroark_103'),P1,'discard')
        self.assertFalse(self.playable(rig,ctx,definition))
        incoming=self.add(rig,fixtures.definition('SWSH7.Zorua_102'),P1,'discard')
        outgoing=ctx.my_active()
        energy=self.energy(rig)
        rig.attach(energy,outgoing)
        outgoing.set_attribute(AttrID.HP,ctx.max_hp(outgoing)-30)
        ctx.choose_cards=AsyncMock(return_value=[incoming])
        ctx.choose_pokemon=AsyncMock(return_value=outgoing)
        self.assertTrue(self.playable(rig,ctx,definition))
        await definition.effect(ctx)
        self.assertIs(ctx.my_active(),incoming)
        self.assertIs(energy.parent,incoming)
        self.assertEqual(incoming.get_attribute(AttrID.HP),ctx.max_hp(incoming)-30)
        self.assertNotIn(wrong,ctx.choose_cards.call_args.args[0])

    async def test_gardenia_requires_damage_and_attached_grass_not_grass_pokemon(self):
        rig,e,ctx,definition=self.setup_card('SM5.Gardenia_124')
        for pokemon in ctx.my_pokemon_in_play():
            for energy in list(ctx.attached_energies(pokemon)):rig.to_area(energy,P1,'discard')
        target=self.add(rig,fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'),P1,'bench')
        self.assertFalse(self.playable(rig,ctx,definition))
        target.set_attribute(AttrID.HP,ctx.max_hp(target)-100)
        self.assertFalse(self.playable(rig,ctx,definition))
        rig.attach(self.energy(rig,PokemonTypes.GRASS),target)
        self.assertTrue(self.playable(rig,ctx,definition))
        await definition.effect(ctx)
        self.assertEqual(target.get_attribute(AttrID.HP),ctx.max_hp(target)-20)

    async def test_cheryl_heals_evolutions_only_and_discards_energy_only_if_healed(self):
        rig,e,ctx,definition=self.setup_card('SWSH5.Cheryl_123')
        evolved=self.add(rig,fixtures.definition('SM12.Jolteon_70'),P1,'bench')
        healthy=self.add(rig,fixtures.definition('SM12.Flareon_25'),P1,'bench')
        basic=ctx.my_active()
        evolved.set_attribute(AttrID.HP,ctx.max_hp(evolved)-20)
        basic.set_attribute(AttrID.HP,ctx.max_hp(basic)-20)
        energies=[self.energy(rig) for _ in range(3)]
        for energy,target in zip(energies,(evolved,healthy,basic)):rig.attach(energy,target)
        tool=self.add(rig,fixtures.definition('SM3.WishfulBaton_128'),P1,'hand')
        rig.attach(tool,evolved)
        await definition.effect(ctx)
        self.assertEqual(evolved.get_attribute(AttrID.HP),ctx.max_hp(evolved))
        self.assertEqual(basic.get_attribute(AttrID.HP),ctx.max_hp(basic)-20)
        self.assertIn(energies[0],ctx.discard_pile())
        self.assertIs(energies[1].parent,healthy)
        self.assertIs(energies[2].parent,basic)
        self.assertIs(tool.parent,evolved)

    async def test_crasher_wake_requires_two_water_and_searches_up_to_two_any_cards(self):
        rig,e,ctx,definition=self.setup_card('SM6.CrasherWake_104')
        for card in list(ctx.hand()):
            if card is not ctx.source:rig.to_area(card,P1,'deck')
        water=self.energy(rig)
        self.energy(rig,PokemonTypes.FIRE)
        self.assertFalse(self.playable(rig,ctx,definition))
        second=self.energy(rig)
        self.assertTrue(self.playable(rig,ctx,definition))
        ctx.search_deck=AsyncMock(return_value=[])
        await definition.effect(ctx)
        self.assertIn(water,ctx.discard_pile())
        self.assertIn(second,ctx.discard_pile())
        self.assertIsNone(ctx.search_deck.call_args.args[0])
        self.assertEqual(ctx.search_deck.call_args.kwargs['count'],2)
        self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'],0)
