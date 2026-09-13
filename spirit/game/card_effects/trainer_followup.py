"""Explicit Trainer rules where generic text resolution loses constraints."""
from spirit.game.attributes import AttrID, SpecialConditions
from spirit.game.data_utils import Ability, Activations
from spirit.game.session.effects import is_evolution_pokemon, is_pokemon_card
from spirit.game.session.passives import (
    effective_max_hp, effective_pokemon_types, evolution_blocked, effective_bench_capacity,
)


def last_card_recovery(pokemon_type):
    """Archie/Maxie: mandatory typed recovery, then draw; any Stage is legal."""
    def candidates(board, player_id):
        discard = board.find_player_area(player_id, 'discard')
        return [card for card in (discard.children if discard is not None else [])
                if is_pokemon_card(card)
                and pokemon_type in (card.get_attribute(AttrID.POKEMON_TYPES) or [])]

    def condition(board, player_id, source=None):
        hand = board.find_player_area(player_id, 'hand')
        cards = list(hand.children) if hand is not None else []
        if source is None:
            if len(cards) != 1:
                return False
        elif any(card is not source for card in cards):
            return False
        bench = board.find_player_area(player_id, 'bench')
        return bool(bench is not None
                    and len(bench.children) < effective_bench_capacity(board, player_id)
                    and candidates(board, player_id))

    async def effect(ctx):
        # The Supporter has already left hand when its effect resolves.
        if not condition(ctx.board, ctx.player_id, ctx.source):
            return
        pool = candidates(ctx.board, ctx.player_id)
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Choose a Pokémon from your discard pile")
        if not picks or picks[0] not in pool:
            return
        if await ctx.bench_pokemon(picks[0]):
            await ctx.flush_choreography()
            await ctx.draw_cards(5)

    return effect, condition


def healing_stadium_ability(game_text, amount, types=(), *, all_targets=False,
                            cure=False, requires_sleep=False, end_turn=False):
    """Share target selection between activation permission and resolution."""
    def targets(board, player_id):
        candidates = [board.active_pokemon(player_id)] if requires_sleep \
            else board.pokemon_in_play(player_id)
        eligible = []
        for pokemon in candidates:
            if pokemon is None:
                continue
            conditions = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            if requires_sleep and 'Asleep' not in conditions:
                continue
            if types and not set(types).intersection(effective_pokemon_types(board, pokemon)):
                continue
            damaged = pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)
            if damaged or (cure and conditions) or requires_sleep:
                eligible.append(pokemon)
        return eligible

    def condition(board, player_id, source=None):
        return bool(targets(board, player_id))

    async def effect(ctx):
        eligible = targets(ctx.board, ctx.player_id)
        if not eligible:
            return
        if all_targets or requires_sleep:
            selected = eligible
        else:
            chosen = await ctx.choose_pokemon(eligible, "Choose a Pokémon to heal")
            selected = [chosen] if chosen in eligible else []
        healed = 0
        for pokemon in selected:
            healed += await ctx.heal(amount, target=pokemon)
            if requires_sleep:
                await ctx.cure_condition(pokemon, SpecialConditions.ASLEEP)
            elif cure:
                for status in SpecialConditions:
                    if status != SpecialConditions.UNSET:
                        await ctx.cure_condition(pokemon, status)
        if end_turn and healed > 0:
            ctx.ends_turn = True

    return Ability(title="Stadium Effect", game_text=game_text,
                   activation=Activations.ONCE_PER_TURN,
                   effect=effect, condition=condition)


def evosoda_targets(board, player_id):
    state = getattr(board, 'turn_state', None)
    if state is None or state.turn_number <= 2:
        return []
    return [pokemon for pokemon in board.pokemon_in_play(player_id)
            if state.may_evolve_target(pokemon.entity_id)
            and not evolution_blocked(board, player_id, pokemon)]


def evosoda_condition(board, player_id, source=None):
    deck = board.find_player_area(player_id, 'deck')
    # Never inspect private deck contents to determine permission.
    return bool(deck is not None and deck.children and evosoda_targets(board, player_id))


async def evosoda(ctx):
    if not evosoda_condition(ctx.board, ctx.player_id):
        return
    candidates = evosoda_targets(ctx.board, ctx.player_id)
    target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to evolve")
    if target not in candidates:
        return
    name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(
        lambda card: is_evolution_pokemon(card)
        and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
        count=1, minimum=0, prompt="Choose the direct evolution of that Pokémon",
    )
    if picks:
        await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()
