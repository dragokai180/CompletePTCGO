"""Explicit hand-entry Abilities, distinct from evolving or playing a Basic."""
import re

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import effective_bench_capacity, pokemon_entry_blocked


def is_hand_entry(text):
    return bool(re.search(r'this pokémon is (?:the last card )?in your hand', text)) and bool(re.search(
        r'(?:put|play) (?:this pokémon|it) (?:onto your bench|as your new active pokémon)', text))


def hand_entry_allowed(board, pid, source, ability, text):
    """None means this is not the recognized family."""
    if not is_hand_entry(text):
        return None
    hand = board.find_player_area(pid, 'hand')
    bench = board.find_player_area(pid, 'bench')
    if source is None or hand is None or source not in hand.children \
            or bench is None or len(bench.children) >= effective_bench_capacity(board, pid) \
            or pokemon_entry_blocked(board, pid, source, source=source, ability=ability):
        return False
    other = next(p for p in board.player_ids if p != pid)
    if 'last card in your hand' in text and len(hand.children) != 1:
        return False
    if 'more prize cards remaining than your opponent' in text:
        if len(board.find_player_area(pid, 'prizePile').children) <= len(
                board.find_player_area(other, 'prizePile').children):
            return False
    if 'opponent has any stage 2 pokémon in play' in text and not any(
            p.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value
            for p in board.pokemon_in_play(other)):
        return False
    if 'at least 4 lightning energy cards in play' in text:
        # Count physical Energy cards, not the units a multi-Energy provides.
        if sum(energy_provides_type(e, PokemonTypes.LIGHTNING.value)
               for p in board.pokemon_in_play(pid) for e in board.attached_energies(p)) < 4:
            return False
    return True


async def resolve_hand_entry(ctx, text):
    if not is_hand_entry(text):
        return False
    allowed = hand_entry_allowed(ctx.board, ctx.player_id, ctx.source, ctx.ability, text)
    if allowed is None:
        return False
    if not allowed or not await ctx.bench_pokemon(ctx.source):
        ctx.suppress_announce = True
        return True
    # Reveal and place the formerly hidden source before announcing its power
    # or requesting any secondary choice (Electric Swamp / Elusive Master).
    await ctx.flush_choreography()
    if 'new active pokémon' in text:
        await ctx.switch_active(ctx.player_id, ctx.source)
    if 'move any number of lightning energy' in text:
        await ctx.move_energy_freely(
            [p for p in ctx.my_pokemon_in_play() if p is not ctx.source], [ctx.source],
            predicate=lambda e: energy_provides_type(e, PokemonTypes.LIGHTNING.value),
            max_count=None, prompt='Choose Lightning Energy to move, or Done')
    draw = re.search(r'draw (\d+) cards', text)
    if draw:
        await ctx.draw_cards(int(draw.group(1)))
    return True
