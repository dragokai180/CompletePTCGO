"""SM/SWSH knockout effects: real destinations, ownership and transfer limits."""
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Attack, CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class SmKnockoutTimingTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add


    async def test_spell_tag_requires_psychic_and_attack_damage(self):
        for psychic, damage in ((True, True), (False, True), (True, False)):
            rig, e = self.rig('SM11.Aegislash_95')
            victim = e['target']
            victim.set_attribute(AttrID.POKEMON_TYPES, [(PokemonTypes.PSYCHIC if psychic else PokemonTypes.METAL).value])
            tool = self.add(rig, fixtures.definition('SM8.SpellTag_190'), P1, 'hand')
            rig.attach(tool, victim)
            ctx = self.attack_context(rig, victim)
            with patch.object(EffectContext, 'place_damage_counters', AsyncMock()) as counters:
                if damage:await ctx.deal_damage(1000, target=victim)
                else:await ctx.knock_out(victim)
                await rig.session.resolve_knockouts(ctx)
            self.assertEqual(counters.await_count, int(psychic and damage))
            if psychic and damage:self.assertEqual(counters.call_args.args[0], 4)

    async def test_durable_blade_does_not_trigger_from_self_damage(self):
        rig, e = self.rig('SM11.Aegislash_95')
        victim = e['target']
        ctx = EffectContext(rig.session, P1, victim, Attack(title='Self hit', cost={}, damage=1000))
        await ctx.deal_damage(1000, target=victim, apply_modifiers=False)
        await rig.session.resolve_knockouts(ctx)
        self.assertIn(victim, ctx.discard_pile(P1))

    async def test_grounding_does_not_reuse_an_energy_already_moved(self):
        rig, e = self.rig('SM7.Lanturn_50')
        lanturn = e['target']
        rig.to_area(lanturn, P1, 'bench')
        self.add(rig, fixtures.definition('SM7.Lanturn_50'), P1, 'bench')
        victim = self.add(rig, self.filler, P1, 'activePokemonArea')
        energy = self.energy(rig, victim)
        ctx = self.attack_context(rig, victim)
        with patch.object(EffectContext, 'ask_yes_no', AsyncMock(return_value=True)) as ask:
            await ctx.deal_damage(1000, target=victim)
            await rig.session.resolve_knockouts(ctx)
        self.assertEqual(energy.parent.archetype_id, lanturn.archetype_id)
        self.assertIn(energy.parent, rig.board.pokemon_in_play(P1))
        ask.assert_awaited_once()

    async def test_gift_energy_draws_only_for_opposing_attack_damage(self):
        for damage in (True, False):
            rig, e = self.rig('SM11.Aegislash_95')
            victim = e['target']
            card = self.add(rig, fixtures.definition('SWSH11.GiftEnergy_171'), P1, 'hand')
            rig.attach(card, victim)
            ctx = self.attack_context(rig, victim)
            with patch.object(EffectContext, 'draw_until', AsyncMock()) as draw:
                if damage:await ctx.deal_damage(1000, target=victim)
                else:await ctx.knock_out(victim)
                await rig.session.resolve_knockouts(ctx)
            self.assertEqual(draw.await_count, int(damage))
            if damage:draw.assert_awaited_once_with(7)

    async def test_emergency_jelly_fires_on_either_turn_and_consumes_itself(self):
        for owner in (P1, P2):
            rig, e = self.rig('SM11.Aegislash_95')
            pokemon = rig.board.active_pokemon(owner)
            tool = self.add(rig, fixtures.definition('SWSH12.EmergencyJelly_155'), owner, 'hand')
            other = self.add(rig, fixtures.definition('SM3.WishfulBaton_128'), owner, 'hand')
            rig.attach(other, pokemon)
            rig.attach(tool, pokemon)
            pokemon.set_attribute(AttrID.HP, 30)
            await rig.session._fire_end_of_turn_triggers(P1)
            self.assertEqual(pokemon.get_attribute(AttrID.HP), min(150, EffectContext(rig.session, owner, pokemon, None).max_hp(pokemon)))
            self.assertIs(tool.parent, rig.board.find_player_area(owner, 'discard'))
            self.assertIs(other.parent, pokemon)

    async def test_emergency_jelly_not_consumed_above_threshold_or_without_healing(self):
        rig, e = self.rig('SM11.Aegislash_95')
        pokemon = e['target']
        tool = self.add(rig, fixtures.definition('SWSH12.EmergencyJelly_155'), P1, 'hand')
        rig.attach(tool, pokemon)
        pokemon.set_attribute(AttrID.HP, 31)
        await rig.session._fire_end_of_turn_triggers(P2)
        self.assertIs(tool.parent, pokemon)
        pokemon.set_attribute(AttrID.HP, 30)
        with patch.object(EffectContext, 'heal', AsyncMock(return_value=0)):
            await rig.session._fire_end_of_turn_triggers(P2)
        self.assertIs(tool.parent, pokemon)


    async def test_golden_wing_can_split_two_energy_between_targets(self):
        rig, e = self.rig('Promo_SM.ShiningHoOh_70')
        victim = e['target']
        for card in list(rig.board.attached_energies(victim)):
            rig.to_area(card, P1, 'deck')
        energies = [self.energy(rig, victim) for _ in range(2)]
        bench = list(rig.board.find_player_area(P1, 'bench').children)
        ctx = self.attack_context(rig, victim)
        with patch.object(EffectContext, 'choose_cards', AsyncMock(return_value=energies)), \
             patch.object(EffectContext, 'choose_pokemon', AsyncMock(side_effect=bench[:2])):
            await ctx.deal_damage(1000, target=victim)
            await rig.session.resolve_knockouts(ctx)
        self.assertIn(energies[0], rig.board.attached_energies(bench[0]))
        self.assertIn(energies[1], rig.board.attached_energies(bench[1]))

    async def test_scatter_only_opponents_turn_tails_and_returns_full_stack(self):
        rig, e = self.rig('SM12.Wishiwashi_62')
        pokemon = e['target']
        energy = self.energy(rig, pokemon)
        pokemon.set_attribute(AttrID.HP, 100)
        with patch.object(EffectContext, 'flip_coins', AsyncMock(return_value=[False])) as flip:
            await rig.session._fire_end_of_turn_triggers(P1)
            flip.assert_not_awaited()
            await rig.session._fire_end_of_turn_triggers(P2)
        self.assertIn(pokemon, EffectContext(rig.session, P1, pokemon, None).deck())
        self.assertIn(energy, EffectContext(rig.session, P1, pokemon, None).deck())
        self.assertIsNot(rig.board.active_pokemon(P1), pokemon)

    def attack_context(self, rig, victim):
        owner = P2 if victim.owning_player_id == P1 else P1
        return EffectContext(rig.session, owner, rig.board.active_pokemon(owner),
                             Attack(title='Audit hit', cost={}, damage=1000))

    def energy(self, rig, victim):
        card = self.add(rig, CARD_DEFS_BY_GUID[self.energies[PokemonTypes.WATER.value].lower()],
                        victim.owning_player_id, 'hand')
        rig.attach(card, victim)
        return card

    async def test_durable_blade_returns_pokemon_stack_without_energy(self):
        rig, e = self.rig('SM11.Aegislash_95')
        victim = e['target']
        tucked = [self.add(rig, fixtures.definition(p), P1, 'hand') for p in
                  ('SM11.Honedge_93', 'SM11.Doublade_94')]
        for card in tucked:rig.attach(card, victim)
        energy = self.energy(rig, victim)
        ctx = self.attack_context(rig, victim)
        await ctx.deal_damage(1000, target=victim)
        await rig.session.resolve_knockouts(ctx)
        self.assertIn(victim, ctx.hand(P1))
        self.assertTrue(all(c in ctx.hand(P1) for c in tucked))
        self.assertIn(energy, ctx.discard_pile(P1))

    async def test_energy_grounding_moves_to_surviving_lanturn_only(self):
        rig, e = self.rig('SM7.Lanturn_50')
        lanturn = e['target']
        rig.to_area(lanturn, P1, 'bench')
        victim = rig.board.find_player_area(P1, 'bench').children[0]
        rig.to_area(victim, P1, 'activePokemonArea')
        energy = self.energy(rig, victim)
        ctx = self.attack_context(rig, victim)
        with patch.object(EffectContext, 'ask_yes_no', AsyncMock(return_value=True)):
            await ctx.deal_damage(1000, target=victim)
            await rig.session.resolve_knockouts(ctx)
        self.assertIn(energy, rig.board.attached_energies(lanturn))

    async def test_hypnotic_pendulum_chooses_opposing_promotion_on_heads(self):
        rig, e = self.rig('SM10.Hypno_72')
        for card in list(rig.board.find_player_area(P1, 'bench').children):
            if card.archetype_id == e['target'].archetype_id:
                rig.to_area(card, P1, 'discard')
        victim = rig.board.active_pokemon(P2)
        chosen = rig.board.find_player_area(P2, 'bench').children[-1]
        ctx = self.attack_context(rig, victim)
        with patch.object(EffectContext, 'flip_coins', AsyncMock(return_value=[True])) as flip, \
             patch.object(EffectContext, 'choose_pokemon', AsyncMock(return_value=chosen)) as choose:
            await ctx.deal_damage(1000, target=victim)
            await rig.session.resolve_knockouts(ctx)
        flip.assert_awaited_once()
        self.assertEqual(flip.call_args.kwargs['player_id'], P1)
        self.assertIs(rig.board.active_pokemon(P2), chosen)

    async def test_wishful_baton_uses_one_destination_for_all_energy(self):
        rig, e = self.rig('SM11.Aegislash_95')
        # Use an ordinary Active to avoid interacting with Durable Blade.
        victim = rig.board.find_player_area(P1, 'bench').children[0]
        rig.to_area(e['target'], P1, 'deck')
        rig.to_area(victim, P1, 'activePokemonArea')
        extra = self.add(rig, self.filler, P1, 'bench')
        tool = self.add(rig, fixtures.definition('SM3.WishfulBaton_128'), P1, 'hand')
        rig.attach(tool, victim)
        energies = [self.energy(rig, victim) for _ in range(3)]
        bench = list(rig.board.find_player_area(P1, 'bench').children)
        choices = [bench[0], bench[-1], bench[0]]
        async def pick(cards, *args, **kwargs):
            return choices.pop(0) if choices else cards[0]
        ctx = self.attack_context(rig, victim)
        with patch.object(EffectContext, 'choose_cards', AsyncMock(return_value=energies)), \
             patch.object(EffectContext, 'choose_pokemon', AsyncMock(side_effect=pick)) as choose:
            await ctx.deal_damage(1000, target=victim)
            await rig.session.resolve_knockouts(ctx)
        self.assertTrue(all(c in rig.board.attached_energies(bench[0]) for c in energies),
                        ([(c.parent.entity_id, c.parent.get_attribute(AttrID.NAME)) for c in energies], choose.call_args_list))
        choose.assert_awaited_once()
