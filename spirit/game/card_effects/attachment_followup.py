"""Target restrictions and consequences of shared Energy-attachment effects."""
import re

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import subtypes_for
from spirit.game.session.passives import effective_pokemon_types


def attachment_counters(text):
    match = re.search(
        r'(?:if you do|if you attached energy to a pokémon in this way), '
        r'(?:put|place) (\d+) damage counters? on that pokémon', text)
    return int(match.group(1)) * 10 if match else 0


def attachment_targets(board, pid, source, text):
    match = re.search(
        r'(?:from your (?:hand|discard pile)|and attach (?:it|them)) to (.+?)(?:\.|$)', text)
    phrase = match.group(1) if match else ''
    targets = list(board.pokemon_in_play(pid))
    if 'this pokémon' in phrase:
        targets = [p for p in targets if p is source]
    elif 'active pokémon' in phrase:
        targets = [p for p in targets if p is board.active_pokemon(pid)]
    elif 'benched' in phrase:
        bench = board.find_player_area(pid, 'bench')
        targets = list(bench.children) if bench else []
    typed = re.search(
        r'(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon) pokémon', phrase)
    if typed:
        kind = getattr(PokemonTypes, typed.group(1).upper()).value
        targets = [p for p in targets if kind in effective_pokemon_types(board, p)]
    for team in ('Single Strike', 'Rapid Strike', 'Fusion Strike'):
        if team.lower() in phrase:
            targets = [p for p in targets if team in (subtypes_for(p.archetype_id) or [])]
    counters = attachment_counters(text)
    if counters and "can't use this ability on a pokémon that would be knocked out" in text:
        targets = [p for p in targets if p.get_attribute(AttrID.HP, 0) > counters]
    return targets


async def attach_with_followup(ctx, energy, target, text):
    if not await ctx.attach_energy(energy, target):
        return False
    counters = attachment_counters(text)
    if counters:
        await ctx.deal_damage(counters, target=target, is_attack=False, as_counters=True)
    heal = re.search(r'heal (\d+) damage from that pokémon', text)
    if heal:
        await ctx.heal(int(heal.group(1)), target)
    return True
