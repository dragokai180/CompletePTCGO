"""Explicit XY compound attacks; copied attacks retain their printed identity."""
import re

from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import subtypes_for
from spirit.game.session.effects import is_pokemon_tool, is_special_energy, is_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type


class _DecisionSession:
    """Redirect choices, never card ownership or shared session state."""
    _choices = {
        'prompt_player_choice', 'prompt_choice_panel', 'prompt_entity_picker',
        'prompt_card_chooser', 'prompt_card_chooser_groups',
        'prompt_energy_unit_picker', 'prompt_prize_reveal_pick',
        'prompt_damage_counter_placement', 'prompt_attack_selection',
        'prompt_view_cards',
    }

    def __init__(self, session, controller):
        object.__setattr__(self, '_session', session)
        object.__setattr__(self, '_controller', controller)

    def __getattr__(self, name):
        method = getattr(self._session, name)
        if name not in self._choices:
            return method

        async def choose(player_id, *args, **kwargs):
            if name == 'prompt_choice_panel':
                # The controlled Supporter belongs to the other player;
                # a source-bound panel cannot be anchored to their card.
                source, buttons, prompt = args[:3]
                return await self._session.prompt_player_choice(
                    self._controller, prompt, buttons)
            return await method(self._controller, *args, **kwargs)
        return choose

    def __setattr__(self, name, value):
        setattr(self._session, name, value)


async def resolve_xy_attack(ctx, text, printed):
    code = getattr(ctx.ability, 'printed_set_code', '') or ''
    if not re.fullmatch(r'XY\d+|TwentiethAnn|Promo_XY', code):
        return False
    title = ctx.ability.title
    from spirit.game.card_effects.bw_era import _BWTurnShield, _name, _energy_count, _BWTemporaryCombatRule
    if title == 'Hand Control':
        from spirit.game.data_utils import def_for
        from spirit.game.session.effects import is_supporter_card, resolve_trainer_effect
        from spirit.game.session.legal_actions import trainer_condition_met
        hand = list(ctx.hand(ctx.opponent_id))
        await ctx.reveal_cards(hand)
        candidates = [
            card for card in hand if is_supporter_card(card)
            and (
                getattr(def_for(card.archetype_id), 'condition', None) is None
                or trainer_condition_met(def_for(card.archetype_id).condition,
                                         ctx.board, ctx.opponent_id, card)
            )
        ]
        picks = await ctx.choose_cards(candidates, 1, minimum=0,
                                        prompt='Choose a Supporter for your opponent to play')
        if not picks:
            return True
        card = picks[0]
        area = ctx.board.find_global_area('activeTrainer')
        if not area or not ctx.board.move_card(card.entity_id, area.entity_id):
            return True
        card.owning_player_id = ctx.opponent_id
        ctx._queue_intro_and_move(card, area.entity_id, 0)
        controlled = _DecisionSession(ctx.session, ctx.player_id)
        result = await resolve_trainer_effect(controlled, ctx.opponent_id, card)
        if result is not None:
            if card.parent is area:
                await result.discard_cards([card])
            ctx._messages.extend(result._messages)
            ctx.knockouts.extend(result.knockouts)
            ctx.deferred_actions.extend(result.deferred_actions)
            ctx.coin_results.extend(result.coin_results)
            ctx.visual_targets.extend(result.visual_targets)
        else:
            await ctx.discard_cards([card])
        return True
    if title == 'Solar Birth':
        from spirit.game.session.effects import is_basic_pokemon, is_basic_energy
        from spirit.game.session.passives import effective_bench_capacity
        if len(ctx.my_bench()) < effective_bench_capacity(ctx.board, ctx.player_id):
            picks = await ctx.search_deck(is_basic_pokemon, 1, minimum=0,
                                          prompt='Choose a Basic Pokémon')
            if picks and await ctx.bench_pokemon(picks[0]):
                target = picks[0]
                energies = await ctx.search_deck(is_basic_energy, 2, minimum=0,
                                                 prompt='Choose up to 2 Basic Energy cards')
                for energy in energies:
                    await ctx.attach_energy(energy, target)
        await ctx.shuffle_deck()
        return True
    if title in ('Burning Icicles', 'Frosty Thunder'):
        await ctx.deal_damage(printed)
        kind = 'fire' if title == 'Burning Icicles' else 'lightning'
        if _energy_count(ctx, ctx.attacker, kind):
            pool = list(ctx.opponent_bench())
            targets = []
            if title == 'Frosty Thunder':
                targets = pool
            else:
                for _ in range(min(2, len(pool))):
                    target = await ctx.choose_pokemon(pool, 'Choose a Benched Pokémon')
                    if target is None:
                        break
                    pool.remove(target)
                    targets.append(target)
            for target in targets:
                await ctx.deal_damage(20, target=target, apply_modifiers=False)
        return True
    if title == 'Lock-On' and 'increased by 120' in text:
        ctx.lock_retreat(ctx.defender)
        ctx.add_passive_through_own_next_turn(ctx.defender,
                                             _BWTemporaryCombatRule(damage_taken_add=120))
        return True
    if title == 'Vanishing Strike':
        enabled = ctx.stadium_in_play() is not None
        await ctx.deal_damage(printed + (50 if enabled else 0),
                              ignore_resistance=enabled, ignore_target_effects=enabled)
        return True
    if title == 'Stardust' and 'special energy' in text:
        if printed:
            await ctx.deal_damage(printed)
        removed = await ctx.discard_energy_from(ctx.defender, 1, predicate=is_special_energy)
        if any(card in ctx.discard_pile(ctx.opponent_id) for card in removed):
            ctx.add_passive_through_opponents_turn(ctx.attacker, _BWTurnShield(prevent_all=True))
        return True
    if title == 'Magical Symphony':
        await ctx.deal_damage(printed)
        if ctx.session.turn_state.supporter_played and ctx.opponent_bench():
            target = await ctx.choose_pokemon(ctx.opponent_bench(), 'Choose a Benched Pokémon')
            if target is not None:
                await ctx.deal_damage(50, target=target, apply_modifiers=False)
        return True
    if title == 'Link Fusion':
        names = {_name(p).casefold() for p in ctx.my_bench()}
        bonus = sum(amount for name, amount in (
            ('solosis', 30), ('duosion', 60), ('reuniclus', 90)) if name in names)
        await ctx.deal_damage(printed + bonus)
        return True
    if title in ('Energy Glide', 'Quiver Dance') and 'search your deck' in text:
        from spirit.game.session.effects import is_basic_energy
        predicate = (lambda card: is_energy_card(card) and
                     energy_provides_type(card, PokemonTypes.LIGHTNING.value)) \
                    if title == 'Energy Glide' else is_basic_energy
        picks = await ctx.search_deck(predicate, 1, minimum=0, prompt='Choose an Energy')
        attached = bool(picks) and await ctx.attach_energy(picks[0], ctx.attacker)
        await ctx.shuffle_deck()
        if attached:
            if title == 'Quiver Dance':
                await ctx.heal(40, ctx.attacker)
            elif ctx.my_bench():
                target = await ctx.choose_pokemon(ctx.my_bench(), 'Choose your new Active Pokémon')
                if target is not None:
                    await ctx.switch_active(ctx.player_id, target)
        return True
    if title == 'Flare Up':
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)
                and energy_provides_type(c, PokemonTypes.FIRE.value)]
        if len(pool) >= 10:
            await ctx.deal_damage(printed)
            picks = await ctx.choose_cards(pool, 10, minimum=10,
                                           prompt='Choose 10 Fire Energy cards')
            await ctx.shuffle_into_deck(picks)
        return True
    if title == 'Tidal Storm':
        await ctx.deal_damage(printed)
        if ctx.my_bench():
            pool = ctx.attached_energies(ctx.attacker)
            from spirit.game.session.legal_actions import energy_provided_count
            if sum(energy_provided_count(c, ctx.board) for c in pool) <= 2:
                picks = pool
            else:
                selected = await ctx.session.prompt_energy_unit_picker(
                    ctx.player_id, ctx.source.entity_id, pool, 2, 'Choose Energy to move')
                picks = [c for c in pool if c.entity_id in selected]
            target = await ctx.choose_pokemon(ctx.my_bench(), 'Choose a Benched Pokémon') if picks else None
            if target is not None:
                for energy in picks:
                    await ctx.move_energy(energy, target)
        for pokemon in list(ctx.opponent_bench()):
            if 'EX' in (subtypes_for(pokemon.archetype_id) or []):
                await ctx.deal_damage(30, target=pokemon, apply_modifiers=False)
        return True
    if title == 'Coordinate':
        pool = [p for p in ctx.my_bench() if not any(is_pokemon_tool(c) for c in p.children)]
        targets = []
        for _ in range(min(2, len(pool))):
            # "Up to" permits choosing fewer than two recipients.
            picks = await ctx.choose_cards(pool, 1, minimum=0,
                                           prompt='Choose a Benched Pokémon for a Tool')
            if not picks:
                break
            target = picks[0]
            pool.remove(target)
            targets.append(target)
        for target in targets:
            picks = await ctx.search_deck(is_pokemon_tool, 1, minimum=0,
                                          prompt='Choose a Pokémon Tool')
            if picks:
                await ctx.attach_card(picks[0], target)
        await ctx.shuffle_deck()
        return True
    return False
