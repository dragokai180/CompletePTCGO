"""Shared behaviours for Special Energy cards.

Keep card-specific continuous effects here instead of approximating them as
basic Colorless Energy in generated card scripts.  Every hook is scoped to
the physical Energy's carrier so multiple copies stack only when the printed
card says they do.
"""

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.data_utils import is_pokemon_v, subtypes_for
from spirit.game.models.board import PokemonEntity
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import (
    Passive,
    carrier_pokemon,
    effective_pokemon_types,
)

# Aurora Energy provides every type of Energy, one at a time.
ALL_TYPES_ONE_AT_A_TIME = [
    [t] for t in (
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
        PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
        PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.FAIRY,
        PokemonTypes.DRAGON, PokemonTypes.COLORLESS,
    )
]


def _board_for(entity):
    root = entity
    while getattr(root, "parent", None) is not None:
        root = root.parent
    return getattr(root, "_board_state", None)


def _pokemon_has_type(pokemon, pokemon_type: PokemonTypes, board=None) -> bool:
    board = board or _board_for(pokemon)
    types = effective_pokemon_types(board, pokemon) if board is not None \
        else (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
    return pokemon_type.value in types


def _is_active(pokemon) -> bool:
    parent = getattr(pokemon, "parent", None)
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"


def has_battle_style(pokemon, style: str) -> bool:
    return style in subtypes_for(getattr(pokemon, "archetype_id", None))


def is_single_strike(pokemon) -> bool:
    return has_battle_style(pokemon, "Single Strike")


def is_rapid_strike(pokemon) -> bool:
    return has_battle_style(pokemon, "Rapid Strike")


def is_fusion_strike(pokemon) -> bool:
    return has_battle_style(pokemon, "Fusion Strike")


def another_card_in_hand(board, player_id) -> bool:
    """Aurora's gate: the hand must hold a second card to discard."""
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) >= 2


async def aurora_attach_cost(ctx) -> bool:
    """Attaching Aurora Energy costs discarding another card from hand."""
    picks = await ctx.discard_from_hand(
        1, prompt="Discard a card to attach Aurora Energy", exclude=[ctx.source]
    )
    return bool(picks)


async def capture_on_attach(ctx):
    """On attach from hand: search the deck for a Basic onto the Bench."""
    if len(ctx.my_bench()) == BENCH_CAPACITY:
        return
    
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


def _is_basic_of_type(card, pokemon_type: PokemonTypes) -> bool:
    return is_basic_pokemon(card) and _pokemon_has_type(card, pokemon_type)


async def telepathic_psychic_on_attach(ctx):
    """On attach from hand to a Psychic Pokemon: bench up to 2 Basic Psychic."""
    if not _pokemon_has_type(ctx.attached_to, PokemonTypes.PSYCHIC):
        return
    space = BENCH_CAPACITY - len(ctx.my_bench())
    take = min(2, space)
    if take <= 0:
        return
    picks = await ctx.search_deck(
        lambda c: _is_basic_of_type(c, PokemonTypes.PSYCHIC),
        count=take, minimum=0,
        prompt="Choose up to 2 Basic Psychic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def speed_lightning_on_attach(ctx):
    """On attach from hand: draw 2 cards only if the target is a Lightning Pokemon."""
    if _pokemon_has_type(ctx.attached_to, PokemonTypes.LIGHTNING):
        await ctx.draw_cards(2)


class PowerfulColorlessPassive(Passive):
    """+20 damage to the opponent's Active from the Colorless carrier."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker:
            return
        if _pokemon_has_type(pokemon, PokemonTypes.COLORLESS):
            calc.amount += 20


class DoubleTurboPassive(Passive):
    """The carrier's attacks do 20 less damage."""

    def modify_damage_dealt(self, calc, carrier):
        if (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.attacker
        ):
            calc.amount -= 20


class HeatFirePassive(Passive):
    """The Fire Pokemon this card is attached to gets +20 max HP."""

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is pokemon \
                and _pokemon_has_type(pokemon, PokemonTypes.FIRE):
            return 20
        return 0


class HidingDarknessPassive(Passive):
    """A Darkness holder has no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon \
                and _pokemon_has_type(pokemon, PokemonTypes.DARKNESS, board):
            return 0
        return cost


class HorrorPsychicPassive(Passive):
    """A damaged Psychic holder places 2 counters on the attacker."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not target or not _pokemon_has_type(
                holder, PokemonTypes.PSYCHIC):
            return None
        if not calc.is_attack or not calc.is_opposing or calc.amount <= 0 \
                or calc.attacker is None:
            return None
        attacker_id = calc.attacker.entity_id

        async def retaliate():
            attacker = ctx.board.get_entity(attacker_id)
            if not ctx.pokemon_is_in_play(attacker):
                return
            await ctx.deal_damage(
                20, target=attacker, apply_modifiers=False,
                as_counters=True, is_attack=False,
            )
            if ctx.knockouts:
                await ctx.flush_choreography()
                await ctx.session.resolve_knockouts(ctx)

        ctx.deferred_actions.append(retaliate)
        return None


class TwinEnergyPassive(Passive):
    """Twin provides only one Colorless while attached to a Pokemon V/GX."""

    def modify_energy_provided(self, options, energy, holder, board, carrier=None):
        if holder is None or carrier is not energy:
            return options
        subtypes = subtypes_for(holder.archetype_id)
        count = 1 if is_pokemon_v(holder.archetype_id) or "GX" in subtypes else 2
        return [[PokemonTypes.COLORLESS.value] * count]


class AromaticGrassPassive(Passive):
    """A Grass holder cannot receive Special Conditions."""

    def blocks_special_conditions(self, target, condition, carrier):
        return carrier_pokemon(carrier) is target \
            and _pokemon_has_type(target, PokemonTypes.GRASS)


class CoatingMetalPassive(Passive):
    """A Metal holder has no Weakness."""

    def modify_weakness(self, calc, carrier):
        if carrier_pokemon(carrier) is calc.target \
                and _pokemon_has_type(calc.target, PokemonTypes.METAL):
            calc.weakness_applies = False


class StoneFightingPassive(Passive):
    """A Fighting holder takes 20 less attack damage after W/R."""

    def modify_damage_taken(self, calc, carrier):
        if carrier_pokemon(carrier) is calc.target \
                and _pokemon_has_type(calc.target, PokemonTypes.FIGHTING) \
                and calc.is_attack and calc.is_opposing:
            calc.amount = max(0, calc.amount - 20)


class WashWaterPassive(Passive):
    """A Water holder ignores effects of opposing attacks (not damage)."""

    def blocks_attack_effects(self, target, carrier):
        return carrier_pokemon(carrier) is target \
            and _pokemon_has_type(target, PokemonTypes.WATER)


class SingleStrikeEnergyPassive(Passive):
    """Each copy adds 20 damage to its Single Strike holder's attacks."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is calc.attacker and is_single_strike(holder) \
                and calc.is_attack and calc.is_opposing and calc.to_active:
            calc.amount += 20


class _ConditionShieldPassive(Passive):
    condition = None

    def blocks_special_conditions(self, target, condition, carrier):
        return carrier_pokemon(carrier) is target and condition == self.condition


class ImpactEnergyPassive(_ConditionShieldPassive):
    condition = SpecialConditions.POISONED


class SpiralEnergyPassive(_ConditionShieldPassive):
    condition = SpecialConditions.PARALYZED


class LuckyEnergyPassive(Passive):
    """Draw one when the Active holder is damaged by an opposing attack."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not target or not _is_active(holder) \
                or not calc.is_attack or not calc.is_opposing or calc.amount <= 0:
            return None
        owner_id = carrier.owning_player_id

        async def draw_card():
            await ctx.draw_cards(1, player_id=owner_id)

        ctx.deferred_actions.append(draw_card)
        return None


class FusionStrikeEnergyPassive(Passive):
    """Protect the Fusion Strike holder from opposing Pokemon Abilities."""

    def blocks_ability_effects(self, target, carrier):
        return carrier_pokemon(carrier) is target


class RegenerativeEnergyPassive(Passive):
    """Heal 100 after the attached Pokemon V is evolved from the hand."""

    def heal_on_evolve(self, evolved, pre_evolution, player_id, carrier):
        if carrier_pokemon(carrier) is evolved \
                and is_pokemon_v(pre_evolution.archetype_id):
            return 100
        return 0


class PrismEnergyPassive(Passive):
    """Prism provides every type on a Basic Pokemon, Colorless otherwise."""

    def modify_energy_provided(self, options, energy, holder, board, carrier=None):
        if carrier is not energy:
            return options
        if holder is not None and is_basic_pokemon(holder):
            return [[option[0].value] for option in ALL_TYPES_ONE_AT_A_TIME]
        return [[PokemonTypes.COLORLESS.value]]


async def cure_all_on_attach(ctx, energy, pokemon):
    if _pokemon_has_type(pokemon, PokemonTypes.GRASS):
        await ctx.cure_all_conditions(pokemon)


async def cure_poison_on_attach(ctx, energy, pokemon):
    await ctx.cure_condition(pokemon, SpecialConditions.POISONED)


async def cure_paralysis_on_attach(ctx, energy, pokemon):
    await ctx.cure_condition(pokemon, SpecialConditions.PARALYZED)


async def treasure_on_taken_as_prize(ctx):
    """Offer Treasure Energy's optional attachment during its owner's turn."""
    if ctx.session.turn_state.active_player_id != ctx.player_id:
        return
    targets = list(ctx.my_pokemon_in_play())
    if not targets or not await ctx.ask_yes_no(
            "Attach Treasure Energy to 1 of your Pokémon?"):
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Choose a Pokémon for Treasure Energy")
    if target is not None:
        await ctx.attach_energy(ctx.source, target)


class GrowingGrassPassive(Passive):
    """The Grass Pokemon this card is attached to gets +20 max HP."""

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is pokemon \
                and _pokemon_has_type(pokemon, PokemonTypes.GRASS):
            return 20
        return 0


async def boomerang_reattach(ctx, energy, pokemon):
    """After the carrier's attack discards this card, attach it again."""
    if pokemon is None or pokemon in ctx.knockouts:
        return
    in_play = ctx.board.pokemon_in_play(pokemon.owning_player_id)
    if pokemon not in in_play:
        return
    if energy not in ctx.discard_pile(energy.owning_player_id):
        return
    await ctx.attach_energy(energy, pokemon)


async def enriching_energy_on_attach(ctx):
    """When attached from hand: draw 4 cards."""
    await ctx.draw_cards(4)


async def gift_energy_on_ko(ctx):
    """When the carrier is Knocked Out by an opponent's attack: draw cards
    until you have 7 cards in your hand."""
    await ctx.draw_until(7)


class VGuardPassive(Passive):
    """The carrier takes 30 less damage from opposing Pokemon V (after W/R)."""

    def modify_damage_taken(self, calc, carrier):
        if (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.target
            and calc.attacker is not None
            and is_pokemon_v(calc.attacker.archetype_id)
            # "This effect can't be applied more than once at a time."
            and not getattr(calc, "_v_guard_applied", False)
        ):
            calc._v_guard_applied = True
            calc.amount = max(0, calc.amount - 30)
