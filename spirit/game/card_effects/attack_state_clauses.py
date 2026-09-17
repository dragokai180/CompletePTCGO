"""Public-state attack clauses, evaluated before damage changes that state.

Unknown clauses return None, never an assumed True. Payment/coin clauses
remain in their transactional resolvers rather than being guessed here.
"""
import re

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, SpecialConditions, TrainerType
from spirit.game.data_utils import def_for, subtypes_for, is_pokemon_v
from spirit.game.session.effects import full_stack, is_basic_energy, is_pokemon_card, is_pokemon_tool, is_special_energy
from spirit.game.session.passives import effective_pokemon_types, effective_retreat_cost, energy_provided_options


def _name(card):
    return (getattr(def_for(card.archetype_id), 'display_name', '') or '').casefold()


def _energy(ctx, pokemon, kind=None):
    wanted = getattr(PokemonTypes, kind.upper(), None) if kind else None
    if kind and wanted is None:
        return sum(_name(e) == kind + ' energy' for e in ctx.attached_energies(pokemon))
    return sum(max((option.count(wanted.value) if wanted else len(option)
                    for option in energy_provided_options(ctx.board, energy)), default=0)
               for energy in ctx.attached_energies(pokemon))


def _matches(ctx, pokemon, descriptor):
    descriptor = descriptor.strip().removesuffix(' pokémon')
    types = effective_pokemon_types(ctx.board, pokemon)
    subtypes = set(subtypes_for(pokemon.archetype_id) or [])
    stage = pokemon.get_attribute(AttrID.STAGE)
    if descriptor in ('basic', 'stage 1', 'stage 2'):
        return stage == {'basic': PokemonStage.BASIC, 'stage 1': PokemonStage.STAGE1,
                         'stage 2': PokemonStage.STAGE2}[descriptor].value
    if descriptor == 'evolution':
        return stage not in (PokemonStage.BASIC.value, PokemonStage.RESTORED.value)
    if descriptor.startswith('stage 2 '):
        return stage == PokemonStage.STAGE2.value and _matches(ctx, pokemon, descriptor[8:])
    if descriptor.upper() in PokemonTypes.__members__:
        return getattr(PokemonTypes, descriptor.upper()).value in types
    choices = {'pokémon ex': {'ex'}, 'pokémon-ex': {'EX'}, 'pokémon-gx': {'GX'},
               'pokémon break': {'BREAK'}, 'mega evolution': {'MEGA', 'SV_Mega'},
               'ultra beast': {'Ultra Beast'}, 'tag team': {'TAG TEAM'},
               'tera': {'Tera'}, 'future': {'Future'}, 'ancient': {'Ancient'},
               'team aqua': {'Team Aqua'}, 'team magma': {'Team Magma'}}
    if descriptor in choices:
        return bool(subtypes & choices[descriptor])
    if descriptor == 'pokémon v':
        return is_pokemon_v(pokemon.archetype_id)
    if descriptor in ('pokémon ex or pokémon v', 'pokémon-gx or a pokémon-ex'):
        left, right = descriptor.split(' or ')
        return _matches(ctx, pokemon, left) or _matches(ctx, pokemon, right.removeprefix('a '))
    return _name(pokemon) == descriptor


def public_attack_condition(ctx, clause):
    c = ' '.join(clause.replace('’', "'").casefold().split())
    c = c.replace("your opponent's active pokémon", 'the defending pokémon')
    source, defender = ctx.attacker, ctx.defender
    if _name(source) and c.startswith(_name(source) + ' ') and 'on your bench' not in c:
        c = 'this pokémon' + c[len(_name(source)):]
    state = ctx.session.turn_state
    own, other = ctx.player_id, ctx.opponent_id
    def prizes(pid):
        pile = ctx.board.find_player_area(pid, 'prizePile')
        return len(pile.children) if pile is not None else 0
    def counters(p):
        return max(0, (ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10)
    if c == 'you have no cards in your hand':
        return not ctx.hand()
    if c in ('you have more cards in your hand than your opponent',
             'you have the same number of cards in your hand as your opponent'):
        a, b = len(ctx.hand()), len(ctx.hand(other))
        return a > b if 'more' in c else a == b
    m = re.fullmatch(r'(you have|your opponent has) (exactly |at least )?(\d+)( or fewer| or more)? cards? in (?:your|their) hand', c)
    if m:
        value = len(ctx.hand(own if m[1] == 'you have' else other))
        limit = int(m[3])
        return value <= limit if m[4] == ' or fewer' else value >= limit if m[4] == ' or more' or m[2] == 'at least ' else value == limit
    if c in ('you have more prize cards left than your opponent', 'you have more prize cards remaining than your opponent'):
        return prizes(own) > prizes(other)
    m = re.fullmatch(r'(you have|your opponent has) (?:(exactly|only|at least) )?(\d+)(?: or (\d+))?( or fewer| or more)? prize cards? (?:remaining|left)', c)
    if m:
        value, limit = prizes(own if m[1] == 'you have' else other), int(m[3])
        return value <= limit if m[5] == ' or fewer' else value >= limit if m[5] == ' or more' or m[2] == 'at least' else value in {limit, int(m[4] or m[3])}
    if c == 'each player has exactly 1 prize card remaining':
        return prizes(own) == prizes(other) == 1
    if c in ('you have used your gx attack', 'your opponent has already used their gx attack'):
        return (other if c.startswith('your opponent') else own) in state.gx_used
    if c in ('a stadium is in play', 'there is any stadium card in play'):
        return ctx.stadium_in_play() is not None
    if c in ('you have a stadium in play', 'you have a stadium card in play', 'you have any stadium card in play'):
        stadium = ctx.stadium_in_play()
        return stadium is not None and stadium.owning_player_id == own
    if c == 'your opponent has a stadium card in play':
        stadium = ctx.stadium_in_play()
        return stadium is not None and stadium.owning_player_id == other
    if c == 'lysandre labs is in play':
        stadium = ctx.stadium_in_play()
        return stadium is not None and _name(stadium) == 'lysandre labs'
    if c == 'you have fewer pokémon in play than your opponent':
        return len(ctx.my_pokemon_in_play()) < len(ctx.opponent_pokemon_in_play())
    m = re.fullmatch(r'you have (?:at least )?(\d+)(?: or more)? (?:(\w+) )?energy in play', c)
    if m:
        return sum(_energy(ctx, p, m[2]) for p in ctx.my_pokemon_in_play()) >= int(m[1])
    m = re.fullmatch(r'(this pokémon|the defending pokémon) (.+)', c)
    if m:
        pokemon = source if m[1] == 'this pokémon' else defender
        rule = m[2].removeprefix('already ')
        if pokemon is None:
            return False
        if rule in ('has any damage counters on it', 'has no damage counters on it', 'has full hp'):
            return bool(counters(pokemon)) if rule.startswith('has any') else counters(pokemon) == 0
        if n := re.fullmatch(r'has (\d+) or more damage counters on it', rule):
            return counters(pokemon) >= int(n[1])
        if rule == 'is affected by a special condition':
            return bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS))
        if n := re.fullmatch(r'is (asleep|burned|confused|paralyzed|poisoned)(?: or (burned|poisoned))?', rule):
            conditions = {s.casefold() for s in pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []}
            return bool(conditions & {n[1], n[2]})
        if rule == 'has any special energy attached to it' or rule == 'has any special energy attached':
            return any(is_special_energy(e) for e in ctx.attached_energies(pokemon))
        if n := re.fullmatch(r'has any (.+?) energy attached(?: to it)?', rule):
            return _energy(ctx, pokemon, n[1]) > 0
        if n := re.fullmatch(r'has (\d+) or more (\w+) energy attached', rule):
            return _energy(ctx, pokemon, n[2]) >= int(n[1])
        if rule == 'has no energy attached to it':
            return not ctx.attached_energies(pokemon)
        if rule in ('has a pokémon tool attached', 'has a pokémon tool card attached to it'):
            return any(is_pokemon_tool(e) for e in full_stack(pokemon)[1:])
        if rule == 'has a pokémon tool card that has "fairy charm" in its name attached to it':
            return any(is_pokemon_tool(e) and 'fairy charm' in _name(e) for e in full_stack(pokemon)[1:])
        if rule == 'has a karate belt card attached to it':
            return any(is_pokemon_tool(e) and _name(e) == 'karate belt' for e in full_stack(pokemon)[1:])
        if rule == 'has 2 or more different types of basic energy attached to it':
            return len({t for e in ctx.attached_energies(pokemon) if is_basic_energy(e)
                        for option in energy_provided_options(ctx.board, e) for t in option}) >= 2
        if rule == 'has an ability':
            from spirit.game.card_effects.bw_era import _has_pokemon_ability
            return _has_pokemon_ability(pokemon)
        if rule == 'has no retreat cost':
            return effective_retreat_cost(ctx.board, pokemon) == 0
        if rule == 'has fighting resistance':
            resistance = pokemon.get_attribute(AttrID.RESISTANCE_TYPES)
            return PokemonTypes.FIGHTING.value in (resistance if isinstance(resistance, list) else [resistance])
        if rule.startswith(('is a ', 'is an ')):
            return _matches(ctx, pokemon, re.sub(r'^is an? ', '', rule))
        if rule == 'has more energy attached than the defending pokémon':
            return _energy(ctx, pokemon) > _energy(ctx, defender)
        if re.fullmatch(r"has at least \d+ extra (?:\w+ )?energy attached(?: to it)? \(in addition to this attack's cost\)", rule):
            from spirit.game.card_effects.sm_tag_team_gx import extra_energy_satisfied
            return extra_energy_satisfied(ctx, 'if ' + c)
        if rule == 'was healed during this turn':
            return pokemon.entity_id in state.healed_entities
        if rule in ('moved from your bench to the active spot this turn', 'was on the bench and became your active pokémon this turn'):
            return state.became_active_turn.get(pokemon.entity_id) == state.turn_number
        if n := re.fullmatch(r'used (.+) during your last turn', rule):
            return any(eid == pokemon.entity_id and title.casefold() == n[1]
                       for eid, guid, title in state.attacks_prev_turn_by_player.get(own, []))
        if n := re.fullmatch(r'evolved from (.+) during this turn', rule):
            return state.entered_play_turn.get(pokemon.entity_id) == state.turn_number and any(
                is_pokemon_card(card) and _name(card) == n[1] for card in pokemon.children)
    m = re.fullmatch(r"this pokémon's remaining hp is (\d+) or less", c)
    if m:
        return source.get_attribute(AttrID.HP, 0) <= int(m[1])
    if c in ('this pokémon and the defending pokémon have the same amount of energy attached',
             'this pokémon and the defending pokémon have the same amount of energy attached to them'):
        return _energy(ctx, source) == _energy(ctx, defender)
    if c == 'the retreat cost of the defending pokémon is colorlesscolorless or more':
        return effective_retreat_cost(ctx.board, defender) >= 2
    if c == 'there are 3 or fewer cards in your deck':
        return len(ctx.deck()) <= 3
    m = re.fullmatch(r'you have any (.+) on your bench', c)
    if m:
        return any(_matches(ctx, p, m[1]) for p in ctx.my_bench())
    m = re.fullmatch(r"your opponent has (?:any |an )?(.+?) in play", c)
    if m:
        descriptor = m[1]
        names = re.fullmatch(r'(.+) \(including (.+)\)', descriptor)
        return any(_name(p) in names.groups() if names else _matches(ctx, p, descriptor)
                   for p in ctx.opponent_pokemon_in_play())
    m = re.fullmatch(r'your opponent has (\d+) or more benched pokémon', c)
    if m:
        return len(ctx.opponent_bench()) >= int(m[1])
    m = re.fullmatch(r'(.+) (is|are) on your bench(?: and has any damage counters on it)?', c)
    if m:
        return all(any(_name(p) == name and (not c.endswith('counters on it') or counters(p))
                       for p in ctx.my_bench()) for name in m[1].split(' and '))
    m = re.fullmatch(r'any of your benched (.+) have any damage counters on them', c)
    if m:
        return any(_name(p) == m[1] and counters(p) for p in ctx.my_bench())
    if c == 'your benched pokémon have any damage counters on them':
        return any(counters(p) for p in ctx.my_bench())
    if c == 'all of your benched pokémon have at least 1 damage counter on them':
        return bool(ctx.my_bench()) and all(counters(p) for p in ctx.my_bench())
    if c == "you don't have any pokémon-gx or pokémon-ex on your bench":
        return not any(set(subtypes_for(p.archetype_id) or []) & {'GX', 'EX'} for p in ctx.my_bench())
    if c == 'you played a supporter card from your hand during this turn':
        return bool(ctx.supporters_played_this_turn())
    m = re.fullmatch(r'you played a (future|tag team) supporter card from your hand during this turn', c)
    if m:
        tag = 'Future' if m[1] == 'future' else 'TAG TEAM'
        return any(kind == TrainerType.SUPPORTER.value and tag in (subtypes_for(guid) or [])
                   for guid, name, kind in state.trainers_played)
    m = re.fullmatch(r'you played (.+) from your hand during this turn', c)
    if m:
        return any(name.casefold() == m[1] for guid, name, kind in state.trainers_played)
    m = re.fullmatch(r'(.+) is in your discard pile', c)
    if m:
        return any(_name(card) == m[1] for card in ctx.discard_pile())
    if c == 'you have any lightning energy cards in the lost zone':
        from spirit.game.card_effects.pokemon import energy_provides_type
        pile = ctx.board.find_player_area(own, 'lostZone')
        return pile is not None and any(energy_provides_type(e, PokemonTypes.LIGHTNING.value) for e in pile.children)
    if c == 'you have 10 or more basic fire energy cards in your discard pile':
        from spirit.game.card_effects.pokemon import energy_provides_type
        return sum(is_basic_energy(e) and energy_provides_type(e, PokemonTypes.FIRE.value) for e in ctx.discard_pile()) >= 10
    if c == "you have 4 or more pokémon that have the hide 'n' sneak ability in your discard pile":
        return sum(is_pokemon_card(p) and any(a.title.casefold() == "hide 'n' sneak"
                   for a in getattr(def_for(p.archetype_id), 'abilities', ())) for p in ctx.discard_pile()) >= 4
    if c == 'you attached a pokémon tool card from your hand to this pokémon during this turn':
        return source.entity_id in state.tools_attached_from_hand
    if c == "this pokémon was damaged by an attack during your opponent's last turn while it was your active pokémon":
        return source.entity_id in state.active_attack_damage_taken_last_turn
    if c == 'any of your water pokémon was healed during this turn':
        return any(p.entity_id in state.healed_entities and PokemonTypes.WATER.value in
                   effective_pokemon_types(ctx.board, p) for p in ctx.my_pokemon_in_play())
    if c == 'any of your pokémon in play are the same type as any of your opponent\'s pokémon in play':
        return bool({t for p in ctx.my_pokemon_in_play() for t in effective_pokemon_types(ctx.board, p)} &
                    {t for p in ctx.opponent_pokemon_in_play() for t in effective_pokemon_types(ctx.board, p)})
    if c == "1 of your opponent's pokémon in play has the same name as 1 of your pokémon in play":
        return bool({_name(p) for p in ctx.my_pokemon_in_play()} & {_name(p) for p in ctx.opponent_pokemon_in_play()})
    if c == "any of your opponent's pokémon have any darkness energy attached to them":
        return any(_energy(ctx, p, 'darkness') for p in ctx.opponent_pokemon_in_play())
    if c == 'your benched pokémon have any shadowy darkness energy attached':
        return any(_energy(ctx, p, 'shadowy darkness') for p in ctx.my_bench())
    previous = state.attacks_prev_turn_by_player.get(own, [])
    m = re.fullmatch(r'1 of your pokémon used (.+) during your last turn', c)
    if m:
        return any(title.casefold() == m[1] for eid, guid, title in previous)
    m = re.fullmatch(r'your (.+) used (.+) during your last turn', c)
    if m:
        return any((getattr(def_for(guid), 'display_name', '') or '').casefold() == m[1]
                   and title.casefold() == m[2] for eid, guid, title in previous)
    if c == '1 of your other ancient pokémon used an attack during your last turn':
        return any(eid != source.entity_id and 'Ancient' in (subtypes_for(guid) or [])
                   for eid, guid, title in previous)
    m = re.fullmatch(r"any of your (?:(.+?) )?pokémon were knocked out by damage from (?:an attack during your opponent's last turn|an opponent's attack during (?:their|his or her) last turn)", c)
    if m:
        records = state.kos_by_attack_last_turn.get(own, [])
        if not m[1]:
            return bool(records)
        ptype = getattr(PokemonTypes, m[1].upper(), None)
        if ptype is not None:
            return any(ptype.value in record.get('pokemon_types',
                       [getattr(t, 'value', t) for t in getattr(def_for(record.get('archetype_id')), 'elements', [])])
                       for record in records)
        return any((getattr(def_for(r.get('archetype_id')), 'display_name', '') or '').casefold().startswith(m[1] + ' ')
                   for r in records)
    if c == 'you go second':
        return state.turn_number == 2
    return None


async def resolve_public_conditional_damage(ctx, text, printed):
    """Resolve complete, supported conditional-bonus texts exactly once."""
    if not text.startswith('if '):
        return False
    text = text.replace("(you can't use more than 1 gx attack in a game.)", '').strip()
    if _name(ctx.attacker) and text.startswith('if ' + _name(ctx.attacker) + ' is poisoned,'):
        text = text.replace('and remove the special condition poisoned from ' + _name(ctx.attacker),
                            '. then, remove that special condition from this pokémon')
    pattern = re.compile(r'if (.+?), (.+?)\.(?: |$)')
    remaining = text.rstrip('.') + '.'
    plans = []
    while (match := pattern.match(remaining)) is not None:
        condition, body = match.groups()
        damage = re.fullmatch(r'this attack does (?:\d+ damage plus )?(\d+) more damage(.*)', body)
        bonus, suffix = (damage[1], damage[2]) if damage else ('0', body)
        allowed = public_attack_condition(ctx, condition)
        if allowed is None:
            return False
        factor = 1
        if suffix == ' during your first turn' and condition == 'you go second':
            suffix = ''
        if suffix == ' for each damage counter on this pokémon':
            factor = max(0, (ctx.max_hp(ctx.attacker) - ctx.attacker.get_attribute(AttrID.HP, 0)) // 10)
            suffix = ''
        elif suffix == ' for each pokémon fewer you have in play':
            factor = max(0, len(ctx.opponent_pokemon_in_play()) - len(ctx.my_pokemon_in_play()))
            suffix = ''
        suffix = suffix.removeprefix(',').strip().removeprefix('and ').strip()
        suffix = suffix.removesuffix(' (before applying weakness and resistance)')
        if suffix == '(before applying weakness and resistance)':
            suffix = ''
        status = re.fullmatch(r'(both active pokémon are|the defending pokémon is|this pokémon is) now (.+)', suffix)
        heal = re.fullmatch(r'heal (\d+) damage from (this pokémon|each of your pokémon)', suffix)
        discard = re.fullmatch(r'discard (all|\d+) energy from this pokémon', suffix)
        spread = re.fullmatch(r"this attack does (\d+) damage to each of your opponent's benched pokémon", suffix)
        if suffix and not (status or heal or discard or spread):
            return False
        if status and any(word not in SpecialConditions.__members__ for word in
                          (s.strip().upper() for s in re.split(r',? and |, ', status[2]))):
            return False
        plans.append((allowed, int(bonus) * factor, status, heal, discard, spread))
        remaining = remaining[match.end():]
    cleanup = remaining.strip().rstrip('.')
    if cleanup == "(don't apply weakness and resistance for benched pokémon.)":
        cleanup = ''
    if not plans or cleanup not in ('', 'then, remove all special conditions from this pokémon',
                                   'then, remove that special condition from this pokémon',
                                   'then, remove all special conditions from that pokémon',
                                   'discard that stadium card', 'then, discard that stadium card',
                                   'discard that stadium', 'then, discard that stadium',
                                   "this attack's damage isn't affected by weakness"):
        return False
    await ctx.deal_damage(printed + sum(b for allowed, b, *_ in plans if allowed),
                          ignore_weakness='weakness' in cleanup)
    for allowed, _, status, heal, discard, spread in plans:
        if not allowed:
            continue
        if status:
            targets = [ctx.attacker, ctx.defender] if status[1].startswith('both') else [
                ctx.attacker if status[1].startswith('this') else ctx.defender]
            for word in re.split(r',? and |, ', status[2]):
                for target in targets:
                    await ctx.apply_special_condition(target, getattr(SpecialConditions, word.strip().upper()))
        if heal:
            for target in [ctx.attacker] if heal[2] == 'this pokémon' else ctx.my_pokemon_in_play():
                await ctx.heal(int(heal[1]), target)
        if discard:
            if discard[1] == 'all':
                await ctx.discard_cards(list(ctx.attached_energies(ctx.attacker)))
            else:
                await ctx.discard_energy_units_from(ctx.attacker, int(discard[1]), partial=True)
        if spread:
            for target in list(ctx.opponent_bench()):
                await ctx.deal_damage(int(spread[1]), target=target)
    if cleanup == 'then, remove all special conditions from this pokémon':
        await ctx.cure_all_conditions(ctx.attacker)
    elif cleanup == 'then, remove that special condition from this pokémon':
        await ctx.cure_condition(ctx.attacker, SpecialConditions.POISONED)
    elif cleanup == 'then, remove all special conditions from that pokémon':
        await ctx.cure_all_conditions(ctx.defender)
    elif 'discard that stadium' in cleanup:
        await ctx.discard_stadium()
    return True
