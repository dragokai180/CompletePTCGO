"""Shared mechanics for Black & White -- Plasma Blast (BW10).

The individual card scripts remain declarative and import the effects below.
This module holds only mechanics that are shared by a printing or are large
enough that keeping them in the card data would make the set hard to audit.
"""

from typing import Optional

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import (
    condition_attack,
    discard_random_from_hand,
    flip_bonus,
    flip_damage,
    flip_or_nothing,
    ignore_effects_attack,
)
from spirit.game.card_effects.passives_common import (
    AttackDebuffPassive,
    apply_own_next_turn_boost,
    flip_protection,
    protect_next_turn,
)
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import (
    deck_nonempty,
    is_basic_energy_card,
    professors_research,
    ultra_ball,
)
from spirit.game.data_utils import def_for, subtypes_for
from spirit.game.session.effects import (
    full_stack,
    is_basic_energy,
    is_basic_pokemon,
    is_energy_card,
    is_energy_of_type,
    is_item_card,
    is_pokemon_card,
    is_pokemon_tool,
    is_special_energy,
    is_stage2_pokemon,
    is_supporter_card,
)
from spirit.game.session.legal_actions import energy_provided_count
from spirit.game.session.passives import (
    Passive,
    TurnDamageModifier,
    carrier_pokemon,
    effective_bench_capacity,
    effective_max_hp,
    effective_retreat_cost,
)


def card_name(card) -> str:
    definition = def_for(getattr(card, "archetype_id", ""))
    return getattr(definition, "display_name", "") or ""


def is_team_plasma(card) -> bool:
    return "Team Plasma" in subtypes_for(getattr(card, "archetype_id", ""))


def is_pokemon_ex(card) -> bool:
    return "EX" in subtypes_for(getattr(card, "archetype_id", ""))


def is_grass_pokemon(card) -> bool:
    return (
        is_basic_pokemon(card)
        and PokemonTypes.GRASS.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])
    )


def is_basic_energy_of_type(card, energy_type: PokemonTypes) -> bool:
    return is_basic_energy(card) and is_energy_of_type(card, energy_type)


def is_plasma_energy(card) -> bool:
    return is_special_energy(card) and card_name(card) == "Plasma Energy"


def is_fossil_item(card) -> bool:
    return is_item_card(card) and "Fossil" in card_name(card)


def holder_of(card, pokemon_pool):
    for pokemon in pokemon_pool:
        if card in pokemon.children:
            return pokemon
    return None


def root_of(entity):
    while getattr(entity, "parent", None) is not None:
        entity = entity.parent
    return entity


def walk_entities(entity):
    yield entity
    for child in getattr(entity, "children", ()):
        yield from walk_entities(child)


def opposing_active(entity):
    owner = entity.owning_player_id
    for candidate in walk_entities(root_of(entity)):
        parent = getattr(candidate, "parent", None)
        if (
            candidate.owning_player_id not in (None, owner)
            and parent is not None
            and parent.get_attribute(AttrID.NAME) == "activePokemonArea"
        ):
            return candidate
    return None


# ---------------------------------------------------------------------------
# Continuous effects
# ---------------------------------------------------------------------------


class VerdantWindPassive(Passive):
    def blocks_special_conditions(self, target, condition, carrier):
        if target.owning_player_id != carrier.owning_player_id:
            return False
        return any(
            energy_provides_type(energy, PokemonTypes.GRASS.value)
            for energy in target.children
            if is_energy_card(energy)
        )


class SafeguardPassive(Passive):
    def _protects(self, target, carrier) -> bool:
        if carrier_pokemon(carrier) is not target:
            return False
        attacker = opposing_active(target)
        return attacker is not None and is_pokemon_ex(attacker)

    def prevents_damage(self, calc, carrier):
        return (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.target
            and calc.attacker is not None
            and is_pokemon_ex(calc.attacker)
        )

    def blocks_attack_effects(self, target, carrier):
        return self._protects(target, carrier)


class CursedGlarePassive(Passive):
    def blocks_energy_attachment(self, attaching_player_id, energy, target, carrier):
        owner = carrier.owning_player_id
        return (
            getattr(carrier, "parent", None) is not None
            and carrier.parent.get_attribute(AttrID.NAME) == "activePokemonArea"
            and attaching_player_id != owner
            and is_special_energy(energy)
        )


class DriftingBalloonPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        opponent = next((pid for pid in board.player_ids if pid != pokemon.owning_player_id), None)
        discount = sum(
            1 for p in (board.pokemon_in_play(opponent) if opponent else [])
            if is_team_plasma(p)
        )
        colorless = max(0, cost.get("Colorless", 0) - discount)
        if colorless:
            cost["Colorless"] = colorless
        else:
            cost.pop("Colorless", None)
        return cost


class MentalShroudPassive(Passive):
    def modify_weakness(self, calc, carrier):
        if calc.target.owning_player_id != carrier.owning_player_id:
            return
        names = {card_name(p) for p in calc.board.pokemon_in_play(carrier.owning_player_id)}
        if {"Uxie", "Azelf"}.issubset(names):
            calc.weakness_applies = False


class ToolboxPassive(Passive):
    def tool_capacity(self, pokemon, carrier):
        return 4 if carrier_pokemon(carrier) is pokemon else 1


class BadgeOfDisciplinePassive(Passive):
    def modify_resistance(self, calc, carrier):
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != carrier.owning_player_id:
            return
        if PokemonTypes.FIGHTING.value in (attacker.get_attribute(AttrID.POKEMON_TYPES) or []):
            calc.resistance_applies = False


class ExtraDamageTakenPassive(Passive):
    def __init__(self, amount: int):
        self.amount = amount

    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target:
            calc.amount += self.amount


class SilverBanglePassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if holder is not calc.attacker or holder is None or is_pokemon_ex(holder):
            return
        if is_pokemon_ex(calc.target):
            calc.amount += 30


class SilverMirrorPassive(Passive):
    def _holder_is_protected(self, target, carrier) -> bool:
        holder = carrier_pokemon(carrier)
        return holder is target and holder is not None and not is_pokemon_ex(holder)

    def prevents_damage(self, calc, carrier):
        return (
            calc.is_attack
            and calc.is_opposing
            and self._holder_is_protected(calc.target, carrier)
            and calc.attacker is not None
            and is_team_plasma(calc.attacker)
        )

    def blocks_attack_effects(self, target, carrier):
        if not self._holder_is_protected(target, carrier):
            return False
        attacker = opposing_active(target)
        return attacker is not None and is_team_plasma(attacker)


# ---------------------------------------------------------------------------
# Activated and triggered Abilities
# ---------------------------------------------------------------------------


def tool_reversal_condition(board, player_id, pokemon=None):
    return any(
        is_pokemon_tool(card)
        for p in board.pokemon_in_play(player_id)
        for card in p.children
    )


async def tool_reversal(ctx):
    tools = [
        card for p in ctx.my_pokemon_in_play() for card in p.children
        if is_pokemon_tool(card)
    ]
    picks = await ctx.choose_cards(tools, 1, prompt="Choose a Pokémon Tool to put into your hand")
    await ctx.put_in_hand(picks, reveal=False)


async def prehistoric_call(ctx):
    await ctx.put_on_bottom_of_deck(ctx.source)


async def verdant_wind_cure(ctx):
    cured_any = False
    for pokemon in ctx.my_pokemon_in_play():
        if any(
            energy_provides_type(energy, PokemonTypes.GRASS.value)
            for energy in pokemon.children if is_energy_card(energy)
        ):
            cured_any = await ctx.cure_all_conditions(pokemon) or cured_any
    # Verdant Wind is continuously enforced by VerdantWindPassive.  Its
    # ON_PLAY/ON_ENERGY_ATTACHED hook exists only to remove conditions that
    # were already present; when there is nothing to cure it must not display
    # the ability activation banner.
    if not cured_any:
        ctx.suppress_announce = True


async def red_signal(ctx):
    if (
        ctx.attaching_player_id != ctx.player_id
        or ctx.energy_receiver is not ctx.source
        or ctx.attached_energy is None
        or not is_plasma_energy(ctx.attached_energy)
        or not ctx.opponent_bench()
    ):
        # ON_ENERGY_ATTACHED is broadcast to every Pokemon in play.  A
        # non-matching attachment is not a Red Signal activation and should
        # therefore remain completely silent on both clients.
        ctx.suppress_announce = True
        return
    if not await ctx.ask_yes_no("Use Red Signal?"):
        ctx.suppress_announce = True
        return
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose your opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


def deluge_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(
        is_basic_energy_of_type(card, PokemonTypes.WATER)
        for card in hand.children
    ) and bool(board.pokemon_in_play(player_id))


async def deluge(ctx):
    energies = [
        card for card in ctx.hand()
        if is_basic_energy_of_type(card, PokemonTypes.WATER)
    ]
    picked = await ctx.choose_cards(energies, 1, prompt="Choose a Water Energy to attach")
    if not picked:
        return
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pokémon to attach it to")
    if target is not None:
        await ctx.attach_energy(picked[0], target)


async def stellar_guidance(ctx):
    if not ctx.deck() or not await ctx.ask_yes_no("Use Stellar Guidance?"):
        ctx.suppress_announce = True
        return
    picks = await ctx.search_deck(
        is_supporter_card, count=1, minimum=0,
        prompt="Choose a Supporter card to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def breakwing(ctx):
    tools = [
        card for p in ctx.opponent_pokemon_in_play() for card in p.children
        if is_pokemon_tool(card) and not ctx.effects_blocked(p)
    ]
    if not tools or not await ctx.ask_yes_no("Discard all Pokémon Tools attached to your opponent's Pokémon?"):
        ctx.suppress_announce = True
        return
    await ctx.discard_cards(tools)


def plasma_transfer_condition(board, player_id, pokemon=None):
    in_play = board.pokemon_in_play(player_id)
    return len(in_play) > 1 and any(
        is_plasma_energy(energy)
        for p in in_play for energy in board.attached_energies(p)
    )


async def plasma_transfer(ctx):
    energies = [
        energy for p in ctx.my_pokemon_in_play()
        for energy in ctx.attached_energies(p) if is_plasma_energy(energy)
    ]
    picked = await ctx.choose_cards(energies, 1, prompt="Choose a Plasma Energy to move")
    if not picked:
        return
    energy = picked[0]
    source = carrier_pokemon(energy)
    targets = [p for p in ctx.my_pokemon_in_play() if p is not source]
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to receive the Energy")
    if target is not None:
        await ctx.move_energy(energy, target)


def sinister_hand_condition(board, player_id, pokemon=None):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None or len(board.pokemon_in_play(opponent)) < 2:
        return False
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in board.pokemon_in_play(opponent)
    )


async def sinister_hand(ctx):
    damaged = [
        p for p in ctx.opponent_pokemon_in_play()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    source = await ctx.choose_pokemon(damaged, "Choose a Pokémon to move damage from")
    if source is None:
        return
    targets = [p for p in ctx.opponent_pokemon_in_play() if p is not source]
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to receive the damage counter")
    if target is not None:
        await ctx.move_damage_counters(source, target, max_count=1)


# ---------------------------------------------------------------------------
# Pokémon attacks
# ---------------------------------------------------------------------------


async def sweet_scent(ctx):
    damaged = [p for p in ctx.my_pokemon_in_play() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if damaged:
        target = await ctx.choose_pokemon(damaged, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(20, target)


async def spiral_drain_10(ctx):
    await ctx.deal_damage()
    await ctx.heal(10, ctx.attacker)


async def spiral_drain_20(ctx):
    await ctx.deal_damage()
    await ctx.heal(20, ctx.attacker)


async def lifesplosion(ctx):
    # Lifesplosion counts attached Energy *cards*, not the amount of Energy
    # they provide (Double Colorless Energy therefore counts once).
    energy_count = len(ctx.attached_energies(ctx.attacker))
    free = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    count = min(energy_count, max(0, free))
    if count > 0:
        picks = await ctx.search_deck(
            is_stage2_pokemon, count=count, minimum=0,
            prompt="Choose Stage 2 Pokémon to put onto your Bench",
        )
        for pokemon in picks:
            await ctx.bench_pokemon(pokemon)
    await ctx.shuffle_deck()


async def return_to_six(ctx):
    await ctx.deal_damage()
    await ctx.draw_until(6)


async def energy_press(ctx):
    count = sum(
        energy_provided_count(e, ctx.board)
        for e in ctx.attached_energies(ctx.defender)
    ) if ctx.defender is not None else 0
    await ctx.deal_damage(20 + 20 * count)


yawn = condition_attack(SpecialConditions.ASLEEP)
signal_beam = condition_attack(SpecialConditions.CONFUSED)
bubble = condition_attack(SpecialConditions.PARALYZED, flip=True)
powder_snow = condition_attack(SpecialConditions.ASLEEP)
bang_heads = condition_attack(SpecialConditions.CONFUSED, both_actives=True)
creepy_wind = condition_attack(SpecialConditions.CONFUSED, flip=True)
psybeam = condition_attack(SpecialConditions.CONFUSED)
paralyzing_gaze = condition_attack(SpecialConditions.PARALYZED, flip=True)
tone_deaf = condition_attack(SpecialConditions.CONFUSED)
dark_clamp = condition_attack(no_retreat=True)
hide = flip_protection(prevent=True, effects_too=True)
barrier_attack = protect_next_turn(reduce=30)
double_spin = flip_damage(coins=2, per_heads=30)
slam = flip_damage(coins=2, per_heads=30)
thunder_tempest = flip_damage(coins=4, per_heads=50)
freestyle_strike = flip_damage(coins=2, per_heads=30)
acrobatics = flip_damage(coins=2, base=20, bonus_per_heads=20)
iron_head_10 = flip_damage(until_tails=True, per_heads=10)
iron_head_50 = flip_damage(until_tails=True, per_heads=50)
big_swing = flip_or_nothing(coins=2)
comet_punch = flip_damage(coins=4, per_heads=20)
tri_attack = flip_damage(coins=3, per_heads=50)
fury_swipes = flip_damage(coins=3, per_heads=10)
jet_impact = flip_bonus(20)
focused_wish_10 = flip_bonus(20)
focused_wish_20 = flip_bonus(20)
ambush = flip_bonus(10)
knock_away = flip_bonus(20)
shred = ignore_effects_attack()


async def retribution(ctx):
    await ctx.deal_damage()
    ledger = ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, [])
    if not any(card_name_from_guid(entry.get("archetype_id")) == "Escavalier" for entry in ledger):
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.put_in_hand(list(ctx.attached_energies(defender)), reveal=False)


def card_name_from_guid(guid: Optional[str]) -> str:
    definition = def_for(guid or "")
    return getattr(definition, "display_name", "") or ""


async def emerald_slash(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench or not ctx.deck():
        return
    if not await ctx.ask_yes_no("Search your deck for up to 2 Grass Energy cards?"):
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to receive the Energy")
    if target is None:
        return
    picks = await ctx.search_deck(
        lambda c: is_basic_energy_of_type(c, PokemonTypes.GRASS),
        count=2, minimum=0, prompt="Choose up to 2 Grass Energy cards",
    )
    for energy in picks:
        await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


async def call_for_family_grass(ctx):
    await search_basics_to_bench(ctx, 2, predicate=is_grass_pokemon)


async def call_for_family(ctx):
    await search_basics_to_bench(ctx, 2)


async def search_basics_to_bench(ctx, count, predicate=is_basic_pokemon):
    free = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    take = min(count, max(0, free))
    if take > 0:
        picks = await ctx.search_deck(
            predicate, count=take, minimum=0,
            prompt=f"Choose up to {take} Basic Pokémon to put onto your Bench",
        )
        for pokemon in picks:
            await ctx.bench_pokemon(pokemon)
    await ctx.shuffle_deck()


async def megalo_cannon(ctx):
    await ctx.deal_damage()
    if ctx.opponent_bench():
        target = await ctx.choose_pokemon(ctx.opponent_bench(), "Choose a Benched Pokémon to take 20 damage")
        if target is not None:
            await ctx.deal_damage(20, target=target, apply_modifiers=False)


async def discard_own_energy(ctx):
    await ctx.deal_damage()
    await ctx.discard_energy_from(ctx.attacker, 1)


async def solar_transporter(ctx):
    top = ctx.deck_top(5)
    if not top:
        return
    await ctx.reveal_cards(top)
    plasma = [card for card in top if is_team_plasma(card)]
    others = [card for card in top if card not in plasma]
    await ctx.put_in_hand(plasma, reveal=False)
    await ctx.discard_cards(others)


async def leech_life(ctx):
    dealt = await ctx.deal_damage()
    await ctx.heal(dealt, ctx.attacker)


async def hydro_pump(ctx):
    water = sum(
        max(1, energy_provided_count(e, ctx.board))
        for e in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(e, PokemonTypes.WATER.value)
    )
    await ctx.deal_damage(60 + 10 * water)


async def cleanse_away(ctx):
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


async def bubble_beam(ctx):
    await bubble(ctx)


async def sharpshooting(ctx):
    targets = ctx.opponent_pokemon_in_play()
    target = await ctx.choose_pokemon(targets, "Choose an opponent's Pokémon to take 30 damage")
    if target is not None:
        await ctx.deal_damage(30, target=target, apply_modifiers=None)


async def splatter(ctx):
    targets = ctx.opponent_pokemon_in_play()
    target = await ctx.choose_pokemon(targets, "Choose an opponent's Pokémon to take 20 damage")
    if target is not None:
        await ctx.deal_damage(20, target=target, apply_modifiers=None)


async def reflect_energy(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = [
        e for e in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(e, PokemonTypes.WATER.value)
    ]
    if not bench or not energies:
        return
    energy = (await ctx.choose_cards(energies, 1, prompt="Choose a Water Energy to move"))[0]
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to receive the Energy")
    if target is not None:
        await ctx.move_energy(energy, target)


async def blizzard(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.opponent_bench():
        await ctx.deal_damage(10, target=pokemon, apply_modifiers=False)


async def fossil_hunt(ctx):
    fossils = [card for card in ctx.discard_pile() if is_fossil_item(card)]
    if not fossils:
        return
    count = min(2, len(fossils))
    picks = await ctx.choose_cards(fossils, count, prompt="Choose Fossil Item cards to put into your hand")
    await ctx.put_in_hand(picks, reveal=False)


async def fossil_clutch(ctx):
    fossils = [card for card in ctx.hand() if is_fossil_item(card)]
    use = bool(fossils) and await ctx.ask_yes_no("Discard a Fossil Item card for 50 more damage?")
    if use:
        picks = await ctx.choose_cards(fossils, 1, prompt="Choose a Fossil Item card to discard")
        await ctx.discard_cards(picks)
        await ctx.deal_damage(100)
    else:
        await ctx.deal_damage(50)


async def outrage(ctx):
    damage = max(0, ctx.max_hp(ctx.attacker) - ctx.attacker.get_attribute(AttrID.HP, 0))
    await ctx.deal_damage(30 + damage)


async def giga_frost(ctx):
    await ctx.deal_damage()
    await ctx.discard_energy_units_from(
        ctx.attacker, 2,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.WATER.value),
        partial=True,
    )


async def crush_and_burn(ctx):
    energies = [
        e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
    ]
    picks = await ctx.choose_cards(
        energies, len(energies), minimum=0,
        prompt="Choose Energy cards to discard",
    ) if energies else []
    await ctx.discard_cards(picks)
    await ctx.deal_damage(30 * len(picks))


async def wind_blast(ctx):
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to take 40 damage")
        if target is not None:
            await ctx.deal_damage(40, target=target, apply_modifiers=False)


async def derail(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = [e for e in ctx.attached_energies(defender) if is_special_energy(e)]
    if energies:
        picks = await ctx.choose_cards(energies, 1, prompt="Choose a Special Energy to discard")
        await ctx.discard_cards(picks)


async def psypower(ctx):
    await ctx.place_damage_counters(3, ctx.opponent_pokemon_in_play())


async def trading_places(ctx):
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


async def psyjamming(ctx):
    sources = [p for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)]
    await ctx.move_energy_freely(
        sources, ctx.opponent_pokemon_in_play(), predicate=is_special_energy,
        prompt="Choose a Special Energy to move",
    )


async def precognitive_dream(ctx):
    await ctx.draw_cards(3)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


async def telekinesis_of_nobility(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


async def iron_fist_of_justice(ctx):
    if not any(is_team_plasma(p) for p in ctx.my_pokemon_in_play()):
        await ctx.deal_damage()


async def shadow_punch(ctx):
    await ctx.deal_damage(ignore_resistance=True)


async def last_chance_chop(ctx):
    await ctx.deal_damage(90 if ctx.attacker.get_attribute(AttrID.HP, 0) == 10 else 20)


async def close_combat(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Close Combat")
    if results and not results[0]:
        ctx.add_passive_through_opponents_turn(ctx.attacker, ExtraDamageTakenPassive(30))


async def knock_off(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        await discard_random_from_hand(ctx, ctx.opponent_id, 1)


async def reinforced_lariat(ctx):
    has_tool = any(is_pokemon_tool(c) for c in ctx.attacker.children)
    await ctx.deal_damage(120 if has_tool else 80)


async def shoulder_throw(ctx):
    retreat = effective_retreat_cost(ctx.board, ctx.defender) if ctx.defender is not None else 0
    await ctx.deal_damage(max(0, 80 - 20 * retreat))


async def kick_of_righteousness(ctx):
    await ctx.deal_damage(50 if ctx.defender is not None and is_team_plasma(ctx.defender) else 10)


async def swift_dive(ctx):
    await ctx.deal_damage(50 if ctx.attacker.get_attribute(AttrID.HP, 0) <= 50 else 100)


async def roar(ctx):
    bench = ctx.opponent_bench()
    if bench and ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        target = await ctx.choose_pokemon(
            bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id
        )
        await ctx.switch_active(ctx.opponent_id, target or bench[0])


async def blazing_claws(ctx):
    plasma = ctx.defender is not None and is_team_plasma(ctx.defender)
    await ctx.deal_damage(120 if plasma else 60)
    if plasma:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


async def knock_back(ctx):
    await ctx.deal_damage()
    await roar(ctx)


async def aura_of_the_land(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_bench() + ctx.opponent_bench():
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


async def hypnostrike(ctx):
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


async def steamroll(ctx):
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to take 20 damage")
        if target is not None:
            await ctx.deal_damage(20, target=target, apply_modifiers=False)


async def gaia_crush(ctx):
    await ctx.deal_damage()
    await ctx.discard_stadium()


async def reverse_edge(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Reverse Edge")
    if results and results[0] and ctx.discard_pile():
        picks = await ctx.choose_cards(ctx.discard_pile(), 1, prompt="Choose a card to put into your hand")
        await ctx.put_in_hand(picks, reveal=False)


async def fast_forward(ctx):
    await ctx.deal_damage()
    count = sum(1 for e in ctx.attached_energies(ctx.attacker) if is_plasma_energy(e))
    await ctx.discard_cards(ctx.deck_top(count, ctx.opponent_id))


async def strafe(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench and await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


async def dimension_heal(ctx):
    await ctx.deal_damage()
    count = sum(1 for e in ctx.attached_energies(ctx.attacker) if is_plasma_energy(e))
    await ctx.heal(20 * count, ctx.attacker)


async def strong_bond(ctx):
    picks = await ctx.search_deck(
        lambda c: is_supporter_card(c) and card_name(c) == "Iris",
        count=1, minimum=0, prompt="Choose an Iris card to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def dragonaxe(ctx):
    amount = sum(
        max(1, energy_provided_count(e, ctx.board))
        for e in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(e, PokemonTypes.METAL.value)
    )
    await ctx.deal_damage(40 * amount)


async def strike_of_the_champion(ctx):
    if ctx.defender is not None and is_team_plasma(ctx.defender):
        await ctx.knock_out(ctx.defender)


async def destructive_beam(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Destructive Beam")
    defender = ctx.defender
    if not results or not results[0] or defender is None or ctx.effects_blocked(defender):
        return
    energies = list(ctx.attached_energies(defender))
    if energies:
        picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy to discard")
        await ctx.discard_cards(picks)


async def adrenalash(ctx):
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, 50)


async def misinformation(ctx):
    tools = [
        card for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
        for card in p.children if is_pokemon_tool(card)
    ]
    await ctx.discard_cards(tools)


async def leaf_wallop(ctx):
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, 40, attack_title="Leaf Wallop")


async def double_draw(ctx):
    await ctx.draw_cards(2)


# ---------------------------------------------------------------------------
# Trainers, tools, fossils, and ACE SPEC
# ---------------------------------------------------------------------------


async def caitlin(ctx):
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, len(hand), minimum=0, ordered=True,
        prompt="Choose cards to put on the bottom of your deck",
    )
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)
    await ctx.draw_cards(len(picks))


async def iris(ctx):
    bonus = 10 * ctx.prizes_taken(ctx.opponent_id)
    if bonus <= 0:
        return
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        bonus, ctx.player_id, opposing_active_only=True,
    ))


def fossil_restore(restored_name: str):
    async def effect(ctx):
        bottom = list(ctx.deck()[:7])
        candidates = [
            card for card in bottom
            if is_pokemon_card(card) and card_name(card) == restored_name
        ]
        picks = await ctx.choose_cards(
            candidates, 1, minimum=0,
            prompt=f"Choose {restored_name} to put onto your Bench",
            display_cards=bottom,
        )
        if picks:
            await ctx.bench_pokemon(picks[0])
        await ctx.shuffle_deck()
    return effect


cover_fossil = fossil_restore("Tirtouga")
plume_fossil = fossil_restore("Archen")
root_fossil_lileep = fossil_restore("Lileep")


async def pokemon_catcher(ctx):
    if not ctx.opponent_bench():
        return
    results = await ctx.flip_coins(1, "Pokémon Catcher")
    if not results or not results[0]:
        return
    target = await ctx.choose_pokemon(ctx.opponent_bench(), "Choose your opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def master_ball(ctx):
    picks = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=0,
        prompt="Choose a Pokémon to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def scoop_up_cyclone(ctx):
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pokémon to put into your hand")
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.put_in_hand(full_stack(target), reveal=False)
    if was_active:
        async def promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(ctx.opponent_id, f"{name} has no Pokémon left")
        ctx.deferred_actions.append(promote)


async def reversal_trigger(ctx):
    if not ctx.ko_from_attack or not is_team_plasma(ctx.source):
        return
    picks = await ctx.search_deck(
        count=1, minimum=min(1, len(ctx.deck())), prompt="Choose a card to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


def genesect_ex_only(board, player_id, pokemon=None):
    return pokemon is not None and card_name(pokemon) == "Genesect-EX"


async def g_booster(ctx):
    await ctx.deal_damage(ignore_target_effects=True)
    await ctx.discard_energy_units_from(ctx.attacker, 2, partial=True)


async def g_scope(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to take 100 damage")
    if target is not None:
        await ctx.deal_damage(100, target=target, apply_modifiers=False)
