"""BW Trainer ordering, public Prizes and Special Energy regressions."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext, is_supporter_card
from spirit.game.session.passives import energy_provided_options
from spirit.tools.effect_smoke import P1, P2


class BwTrainerEnergyTests(unittest.IsolatedAsyncioTestCase):
    setUpClass=classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig=fixtures.HgssRulesTests.rig
    ctx=fixtures.HgssRulesTests.ctx
    add=fixtures.HgssRulesTests.add

    async def test_random_receiver_reads_top_first(self):
        path='BW5.RandomReceiver_99'
        rig,e=self.rig(path,'trainer')
        ctx=EffectContext(rig.session,P1,e['target'],None)
        supporter=self.add(rig,definition('BW1.ProfessorJuniper_101'),P1,'deck')
        ctx.reveal_cards=AsyncMock();ctx.put_in_hand=AsyncMock()
        await definition(path).effect(ctx)
        ctx.reveal_cards.assert_awaited_once_with([supporter])
        ctx.put_in_hand.assert_awaited_once_with([supporter],reveal=True)

    async def test_town_map_keeps_prizes_public(self):
        path='BW7.TownMap_136'
        rig,e=self.rig(path,'trainer')
        ctx=EffectContext(rig.session,P1,e['target'],None)
        await definition(path).effect(ctx)
        prizes=rig.board.find_player_area(P1,'prizePile').children
        self.assertTrue(prizes)
        self.assertTrue(all(not p.is_hidden_from(P1) and not p.is_hidden_from(P2) for p in prizes))

    async def test_communication_reveals_before_returning_without_early_shuffle(self):
        path='BW1.PokmonCommunication_99'
        rig,e=self.rig(path,'trainer')
        ctx=EffectContext(rig.session,P1,e['target'],None)
        events=[]
        async def reveal(cards): events.append('reveal')
        async def top(card): events.append('top')
        async def search(*args,**kwargs):events.append('search');return []
        async def shuffle(*args,**kwargs):events.append('shuffle')
        ctx.reveal_cards=AsyncMock(side_effect=reveal)
        ctx.put_on_top_of_deck=AsyncMock(side_effect=top)
        ctx.search_deck=AsyncMock(side_effect=search)
        ctx.shuffle_deck=AsyncMock(side_effect=shuffle)
        ctx.shuffle_into_deck=AsyncMock()
        await definition(path).effect(ctx)
        self.assertEqual(events,['reveal','top','search','shuffle'])
        ctx.shuffle_into_deck.assert_not_awaited()

    async def test_bw_special_energy_values(self):
        paths=[
            ('BW4.DoubleColorlessEnergy_92',[[PokemonTypes.COLORLESS.value]*2]),
            ('BW6.BlendEnergyGrassFirePsychicDarkness_117',[[p.value] for p in
                (PokemonTypes.GRASS,PokemonTypes.FIRE,PokemonTypes.PSYCHIC,PokemonTypes.DARKNESS)]),
            ('BW6.BlendEnergyWaterLightningFightingMetal_118',[[p.value] for p in
                (PokemonTypes.WATER,PokemonTypes.LIGHTNING,PokemonTypes.FIGHTING,PokemonTypes.METAL)]),
            ('BW8.PlasmaEnergy_127',[[PokemonTypes.COLORLESS.value]]),
        ]
        rig,e,ctx=self.ctx('BW1.Snivy_1','Tackle')
        for path,expected in paths:
            with self.subTest(path=path):
                card=self.add(rig,definition(path),P1,'hand')
                rig.attach(card,ctx.attacker)
                self.assertEqual(energy_provided_options(rig.board,card),expected)

    async def test_prism_energy_requires_basic_holder(self):
        rig,e,ctx=self.ctx('BW4.Vanilluxe_33','Slippery Soles')
        energy=self.add(rig,definition('BW4.PrismEnergy_93'),P1,'hand')
        rig.attach(energy,ctx.attacker)
        self.assertEqual(energy_provided_options(rig.board,energy),[[PokemonTypes.COLORLESS.value]])
        basic=self.add(rig,definition('BW1.Snivy_1'),P1,'bench')
        rig.attach(energy,basic)
        options=energy_provided_options(rig.board,energy)
        self.assertIn([PokemonTypes.GRASS.value],options)
        self.assertTrue(all(len(option)==1 for option in options))
