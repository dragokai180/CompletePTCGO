"""Shared mechanics for the Black & White era (BW1--BW11, Dragon Vault,
and BW Black Star Promos).

The original client contains many identical reprints and hundreds of attacks
whose wording differs only slightly.  Keeping those effects here gives every
printing one implementation and prevents the generated card files from
drifting apart.
"""

from __future__ import annotations

import random
import re
from typing import Iterable, Optional

from spirit.game.attributes import (
    AttrID,
    AbilityTypes,
    CardType,
    CLIENT_SPECIAL_CONDITION_NAMES,
    PokemonStage,
    PokemonTypes,
    SpecialConditions,
    TrainerType,
)
from spirit.game.data_utils import (
    Ability, Attack, Activations, CARD_DEFS_BY_GUID, Triggers, def_for,
    evolves_from, has_rule_box, subtypes_for, unimplemented,
)
from spirit.game.models.board import CardEntity, PokemonEntity
from spirit.game.session.passives import (
    Passive,
    TurnDamageModifier,
    carrier_pokemon,
    effective_bench_capacity,
    effective_max_hp,
    effective_pokemon_types,
    effective_retreat_cost,
    energy_provided_options,
)
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.attacks_common import (
    lock_all_attacks,
    lock_defender_attacks,
)
from spirit.game.session.effects import (
    EffectContext,
    full_stack,
    is_basic_energy,
    is_basic_pokemon,
    is_energy_card,
    is_evolution_pokemon,
    is_item_card,
    is_pokemon_card,
    is_pokemon_tool,
    is_special_energy,
    is_stadium_card,
    is_supporter_card,
    is_trainer_card,
    split_pokemon_stack,
)


BW_SET_CODES = {
    "BW1", "BW2", "BW3", "BW4", "BW5", "BW6", "DV", "BW7",
    "BW8", "BW9", "BW10", "BW11", "PROMO_BW",
}

_ALL_ENERGY_TYPES = [
    PokemonTypes.GRASS.value, PokemonTypes.FIRE.value,
    PokemonTypes.WATER.value, PokemonTypes.LIGHTNING.value,
    PokemonTypes.PSYCHIC.value, PokemonTypes.FIGHTING.value,
    PokemonTypes.DARKNESS.value, PokemonTypes.METAL.value,
    PokemonTypes.FAIRY.value,
]


def _name(entity) -> str:
    definition = def_for(getattr(entity, "archetype_id", None))
    return (getattr(definition, "display_name", "") or "").replace(
        "Pok�mon", "Pokémon").strip()


def _is_type(card, pokemon_type: PokemonTypes) -> bool:
    return is_pokemon_card(card) and pokemon_type.value in (
        card.get_attribute(AttrID.POKEMON_TYPES) or []
    )


def _energy_type(card, pokemon_type: PokemonTypes) -> bool:
    return is_energy_card(card) and energy_provides_type(card, pokemon_type.value)


def inferno_fandango_condition(board, player_id, pokemon=None) -> bool:
    """Inferno Fandango is useful only with a Fire Energy in hand."""
    hand = board.find_player_area(player_id, "hand")
    return bool(board.pokemon_in_play(player_id)) and any(
        _energy_type(card, PokemonTypes.FIRE)
        for card in (hand.children if hand is not None else [])
    )


def movable_energy_condition(pokemon_type: PokemonTypes):
    """Gate an unlimited Energy-moving Ability until it has a legal move."""
    def check(board, player_id, pokemon=None):
        in_play = board.pokemon_in_play(player_id)
        if len(in_play) < 2:
            return False
        return any(
            energy_provides_type(energy, pokemon_type.value)
            for target in in_play
            for energy in board.attached_energies(target)
        )
    return check


def _team_plasma(card) -> bool:
    if "Team Plasma" in (getattr(def_for(card.archetype_id), "subtypes", []) or []):
        return True
    # Team Plasma Badge makes its holder a Team Plasma Pokémon for every
    # card effect, without mutating the printed definition.
    return isinstance(card, PokemonEntity) and any(
        _name(attached) == "Team Plasma Badge" for attached in full_stack(card)[1:]
    )


def _has_plasma_energy(ctx, pokemon) -> bool:
    return any(_name(e) == "Plasma Energy" for e in ctx.attached_energies(pokemon))


def _pokemon_ex(card) -> bool:
    definition = def_for(card.archetype_id)
    # Upper-case Pokemon-EX and the modern lower-case Pokemon ex are distinct
    # rule-box classes.  Do not case-fold this subtype: old effects such as
    # Scoundrel Ring must never find a Scarlet & Violet Pokemon ex.
    subtypes = {str(value) for value in
                (getattr(definition, "subtypes", []) or [])}
    return "EX" in subtypes or _name(card).endswith("-EX")


def _has_tool(pokemon) -> bool:
    return any(is_pokemon_tool(card) for card in full_stack(pokemon)[1:])


def _has_named_ability(card, title: str) -> bool:
    definition = def_for(getattr(card, "archetype_id", None))
    return any(getattr(ability, "title", "") == title
               for ability in (getattr(definition, "abilities", None) or []))


def _has_pokemon_ability(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", None))
    return any(getattr(ability, "ability_type", None) not in (
        AbilityTypes.ATTACK, AbilityTypes.NON_DAMAGING_ATTACK,
    ) for ability in (getattr(definition, "abilities", None) or []))


def _has_attack_named(card, title: str) -> bool:
    definition = def_for(getattr(card, "archetype_id", None))
    return any(isinstance(ability, Attack) and ability.title == title
               for ability in (getattr(definition, "abilities", None) or []))


def _stage(card):
    return card.get_attribute(AttrID.STAGE) if card is not None else None


def _has_subtype(card, label: str) -> bool:
    return label.casefold() in {
        str(value).casefold()
        for value in (subtypes_for(getattr(card, "archetype_id", None)) or [])
    }


def _has_exact_subtype(card, label: str) -> bool:
    return label in {
        str(value) for value in (
            subtypes_for(getattr(card, "archetype_id", None)) or []
        )
    }


def _prizes_remaining(card, player_id: str) -> int:
    area = _area_from(card, player_id, "prizePile")
    return len(area.children) if area is not None else 0


def _other_player_id(board, player_id: str) -> Optional[str]:
    return next((pid for pid in board.player_ids if pid != player_id), None)


def _pokemon_in_play_from(entity, player_id: str) -> list[PokemonEntity]:
    # The entity tree ends at PlayMat, while the authoritative helpers live on
    # BoardState (kept as PlayMat._board_state).  Walking the raw tree here also
    # visits previous Evolution stages.  Their localized NAME attribute is a
    # dict (for example {"id": "Snivy"}), which used to be tested against a
    # set of area names and raised ``TypeError: unhashable type: 'dict'``.
    # That exception could happen immediately after a Prize/promotion and the
    # session's safety handler would incorrectly end the game.
    board = _board_for(entity)
    if hasattr(board, "pokemon_in_play"):
        return list(board.pokemon_in_play(player_id))
    root = _tree_root(entity)
    return [
        node for node in _walk(root)
        if isinstance(node, PokemonEntity)
        and node.owning_player_id == player_id
        and _attribute_id(getattr(
            getattr(node, "parent", None),
            "get_attribute", lambda *_: None,
        )(AttrID.NAME)) in {"activePokemonArea", "bench"}
    ]


def _has_named_in_play(entity, player_id: str, *names: str) -> bool:
    wanted = {name.casefold() for name in names}
    return any(
        _name(pokemon).casefold() in wanted
        for pokemon in _pokemon_in_play_from(entity, player_id)
    )


def _has_energy_type(pokemon, pokemon_type: PokemonTypes) -> bool:
    return any(
        energy_provides_type(energy, pokemon_type.value)
        for energy in _attached(pokemon)
    )


def _damage_counters_on(pokemon) -> int:
    printed = pokemon.attribute_originals.get(
        AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
    )
    return max(0, int(printed) - int(pokemon.get_attribute(AttrID.HP, 0))) // 10


def _is_active(pokemon) -> bool:
    parent = getattr(pokemon, "parent", None)
    return bool(parent) and _attribute_id(
        parent.get_attribute(AttrID.NAME)
    ) == "activePokemonArea"


def _attribute_id(value):
    """Unwrap a client-localized attribute while retaining raw server values."""
    if isinstance(value, dict):
        return value.get("id")
    return value


def _tree_root(entity):
    node = entity
    while getattr(node, "parent", None) is not None:
        node = node.parent
    return node


def _board_for(entity):
    """Return the BoardState owning an entity tree, when available."""
    root = _tree_root(entity)
    return getattr(root, "_board_state", root)


def _walk(entity):
    yield entity
    for child in getattr(entity, "children", []) or []:
        yield from _walk(child)


def _area_from(entity, player_id: str, name: str):
    return next((node for node in _walk(_tree_root(entity))
                 if node.owning_player_id == player_id
                 and _attribute_id(node.get_attribute(AttrID.NAME)) == name), None)


def _active_from(entity, player_id: str):
    area = _area_from(entity, player_id, "activePokemonArea")
    return next((card for card in (getattr(area, "children", []) or [])
                 if isinstance(card, PokemonEntity)), None)


def _damaged(ctx, pokemon) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)


async def _choose_one(ctx, cards, prompt, *, optional=False, player_id=None):
    picks = await ctx.choose_cards(
        list(cards), 1, minimum=0 if optional else None,
        prompt=prompt, player_id=player_id,
    )
    return picks[0] if picks else None


async def _shuffle_hand_draw(ctx, player_id: str, count: int) -> None:
    cards = list(ctx.hand(player_id))
    if cards:
        await ctx.shuffle_into_deck(cards, player_id=player_id)
    await ctx.draw_cards(count, player_id=player_id)


async def _use_trainer_effect_as_attack(ctx, card) -> bool:
    """Runs a Trainer's printed effect without treating it as a played card.

    Bewitching Eyes/Impersonation borrow only the effect: they do not consume
    the Supporter allowance and Trainer-immunity effects do not apply because
    the source of the effect remains an attack.
    """
    definition = def_for(getattr(card, "archetype_id", None))
    effect = getattr(definition, "effect", None)
    if effect is None or effect is unimplemented or not callable(effect):
        return False
    original_source = ctx.source
    try:
        ctx.source = card
        await effect(ctx)
    finally:
        ctx.source = original_source
    return True


async def _adjust_hand_to_five(ctx, player_id: str) -> None:
    size = ctx.hand_size(player_id)
    if size > 5:
        await ctx.discard_from_hand(
            size - 5, player_id=player_id,
            prompt="Choose cards to discard until you have 5 cards",
        )
    elif size < 5:
        await ctx.draw_cards(5 - size, player_id=player_id)


# ---------------------------------------------------------------------------
# Trainer effects
# ---------------------------------------------------------------------------

def bw_trainer_playable(board, player_id, source=None) -> bool:
    """Public-information legality for Trainers handled by the BW dispatcher.

    Searches only inspect whether the deck is nonempty; their contents stay
    private and never prevent a card from being played.  Costs and targets in
    hand, discard, or play are public to their owner and must exist up front.
    """
    name = _name(source) if source is not None else ""
    hand_area = board.find_player_area(player_id, "hand")
    hand = list(hand_area.children) if hand_area else []
    source_id = getattr(source, "entity_id", None)
    other_hand = [
        card for card in hand
        if source_id is None or card.entity_id != source_id
    ]
    discard_area = board.find_player_area(player_id, "discard")
    discard = list(discard_area.children) if discard_area else []
    deck_area = board.find_player_area(player_id, "deck")
    deck_nonempty = bool(deck_area and deck_area.children)
    in_play = board.pokemon_in_play(player_id)

    if name == "Max Potion":
        return any(
            pokemon.get_attribute(AttrID.HP, 0)
            < effective_max_hp(board, pokemon)
            for pokemon in in_play
        )
    if name == "Pokémon Communication":
        return deck_nonempty and any(is_pokemon_card(card) for card in other_hand)
    if name == "Revive":
        bench = board.find_player_area(player_id, "bench")
        has_space = bool(
            bench is not None
            and len(bench.children) < effective_bench_capacity(board, player_id)
        )
        return has_space and any(is_basic_pokemon(card) for card in discard)
    if name == "Recycle":
        return bool(discard)
    if name == "Devolution Spray":
        return any(
            (pokemon.get_attribute(AttrID.STAGE) or 0)
            > PokemonStage.BASIC.value
            for pokemon in in_play
        )
    if name == "Computer Search":
        return deck_nonempty and len(other_hand) >= 2
    if name == "Dowsing Machine":
        return (
            len(other_hand) >= 2
            and any(is_trainer_card(card) for card in discard)
        )
    if name == "Team Plasma Grunt":
        return any(_team_plasma(card) for card in other_hand)
    if name == "Shadow Triad":
        return any(_team_plasma(card) for card in discard)
    if name == "Superior Energy Retrieval":
        return (
            len(other_hand) >= 2
            and any(is_basic_energy(card) for card in discard)
        )
    if name == "Colress Machine":
        return deck_nonempty and any(_team_plasma(pokemon) for pokemon in in_play)
    if name in {
        "Pokédex", "Pokedex", "Random Receiver", "Cilan", "Elesa",
        "Heavy Ball", "Old Amber Aerodactyl", "Ether", "Team Plasma Ball",
    }:
        return deck_nonempty
    return True

async def bw_trainer_effect(ctx):
    """Exact dispatcher for the non-passive BW-era Trainers.

    Reprints call this same function; the visible name determines the rule,
    never the set/collector number.
    """
    name = _name(ctx.source)

    if name == "Max Potion":
        candidates = [p for p in ctx.my_pokemon_in_play()
                      if _damaged(ctx, p)]
        target = await ctx.choose_pokemon(candidates, "Choose a damaged Pokémon") \
            if candidates else None
        if target is not None:
            await ctx.heal(ctx.max_hp(target), target)
            await ctx.discard_cards(ctx.attached_energies(target))
        return

    if name == "N":
        for pid in (ctx.opponent_id, ctx.player_id):
            area = ctx.board.find_player_area(pid, "prizePile")
            await _shuffle_hand_draw(ctx, pid, len(area.children) if area else 0)
        return

    if name == "Random Receiver":
        revealed = []
        supporter = None
        for card in ctx.deck():
            revealed.append(card)
            if is_supporter_card(card):
                supporter = card
                break
        if revealed:
            await ctx.reveal_cards(revealed)
        if supporter is not None:
            await ctx.put_in_hand([supporter], reveal=True)
        await ctx.shuffle_deck()
        return

    if name == "Colress":
        count = len(ctx.my_bench()) + len(ctx.opponent_bench())
        await _shuffle_hand_draw(ctx, ctx.player_id, count)
        return

    if name == "Ghetsis":
        hand = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        items = [c for c in hand if is_item_card(c)]
        if items:
            await ctx.shuffle_into_deck(items, player_id=ctx.opponent_id)
        await ctx.draw_cards(len(items))
        return

    if name == "PlusPower":
        ctx.add_turn_damage_modifier(TurnDamageModifier(
            amount=10, player_id=ctx.player_id, opposing_active_only=True,
        ))
        return

    if name in ("Pokédex", "Pokedex"):
        await ctx.reorder_deck_top(min(5, len(ctx.deck())))
        return

    if name == "Pokémon Communication":
        pokemon = await _choose_one(
            ctx, [c for c in ctx.hand() if is_pokemon_card(c)],
            "Choose a Pokémon in your hand to shuffle into your deck",
        )
        if pokemon is None:
            return
        await ctx.shuffle_into_deck([pokemon])
        pick = await ctx.search_deck(is_pokemon_card, count=1, minimum=0,
                                     prompt="Choose a Pokémon")
        await ctx.put_in_hand(pick, reveal=True)
        await ctx.shuffle_deck()
        return

    if name == "Revive":
        candidates = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
        card = await _choose_one(ctx, candidates,
                                 "Choose a Basic Pokémon to put onto your Bench")
        if card is not None:
            await ctx.bench_pokemon(card)
        return

    if name == "Super Scoop Up":
        if (await ctx.flip_coins(1, name))[0]:
            target = await ctx.choose_pokemon(
                ctx.my_pokemon_in_play(), "Choose a Pokémon to return to your hand"
            )
            if target is not None:
                await ctx.put_in_hand(full_stack(target), reveal=False)
        return

    if name == "Recycle":
        if (await ctx.flip_coins(1, name))[0]:
            card = await _choose_one(ctx, ctx.discard_pile(),
                                     "Choose a card to put on top of your deck")
            if card is not None:
                await ctx.put_on_top_of_deck(card)
        return

    if name in ("Cilan", "Elesa"):
        if name == "Cilan":
            pred, count = is_basic_energy, 3
            prompt = "Choose up to 3 basic Energy cards"
        else:
            pred, count = is_pokemon_tool, 3
            prompt = "Choose up to 3 Pokémon Tool cards"
        picks = await ctx.search_deck(pred, count=count, minimum=0, prompt=prompt)
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
        return

    if name == "Heavy Ball":
        def heavy(card):
            return is_pokemon_card(card) and (card.get_attribute(AttrID.RETREAT_COST) or 0) >= 3
        picks = await ctx.search_deck(heavy, count=1, minimum=0,
                                     prompt="Choose a Pokémon with Retreat Cost 3 or more")
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
        return

    if name == "Hooligans Jim & Cas":
        if not (await ctx.flip_coins(1, name))[0]:
            return
        hand = list(ctx.hand(ctx.opponent_id))
        cards = random.sample(hand, min(3, len(hand)))
        await ctx.reveal_cards(cards)
        if cards:
            await ctx.shuffle_into_deck(cards, player_id=ctx.opponent_id)
        return

    if name == "Old Amber Aerodactyl":
        bottom = list(ctx.deck())[-7:]
        matches = [c for c in bottom if _name(c) == "Aerodactyl"]
        pick = await _choose_one(ctx, matches, "Choose an Aerodactyl",
                                 optional=True) if matches else None
        if pick is not None:
            await ctx.bench_pokemon(pick)
        await ctx.shuffle_deck()
        return

    if name == "Devolution Spray":
        candidates = [p for p in ctx.my_pokemon_in_play()
                      if (p.get_attribute(AttrID.STAGE) or 0) > PokemonStage.BASIC.value]
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to devolve") \
            if candidates else None
        if target is not None:
            await ctx.devolve_pokemon(target, 1, destination="hand")
        return

    if name == "Computer Search":
        paid = await ctx.discard_from_hand(2, prompt="Discard 2 cards")
        if len(paid) != 2:
            return
        picks = await ctx.search_deck(None, 1, minimum=0, prompt="Choose a card")
        await ctx.put_in_hand(picks, reveal=False)
        await ctx.shuffle_deck()
        return

    if name == "Hugh":
        await _adjust_hand_to_five(ctx, ctx.opponent_id)
        await _adjust_hand_to_five(ctx, ctx.player_id)
        return

    if name == "Town Map":
        prizes = ctx.board.find_player_area(ctx.player_id, "prizePile")
        if prizes:
            await ctx.reveal_cards(list(prizes.children))
        return

    if name == "Colress Machine":
        picks = await ctx.search_deck(
            lambda c: _name(c) == "Plasma Energy", count=1, minimum=0,
            prompt="Choose a Plasma Energy",
        )
        candidates = [p for p in ctx.my_pokemon_in_play() if _team_plasma(p)]
        if picks and candidates:
            target = await ctx.choose_pokemon(candidates,
                                              "Choose a Team Plasma Pokémon")
            if target is not None:
                await ctx.attach_energy(picks[0], target)
        await ctx.shuffle_deck()
        return

    if name == "Dowsing Machine":
        paid = await ctx.discard_from_hand(2, prompt="Discard 2 cards")
        if len(paid) != 2:
            return
        cards = [c for c in ctx.discard_pile()
                 if is_trainer_card(c) and c is not ctx.source]
        pick = await _choose_one(ctx, cards, "Choose a Trainer card") \
            if cards else None
        if pick is not None:
            await ctx.put_in_hand([pick], reveal=False)
        return

    if name == "Ether":
        top = ctx.deck_top(1)
        if not top:
            return
        await ctx.reveal_cards(top)
        if is_basic_energy(top[0]) and ctx.my_active() is not None:
            await ctx.attach_energy(top[0], ctx.my_active())
        return

    if name == "Hypnotoxic Laser":
        target = ctx.opponent_active()
        if target is None:
            return
        await ctx.apply_special_condition(target, SpecialConditions.POISONED)
        if (await ctx.flip_coins(1, name))[0]:
            await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)
        return

    if name == "Team Plasma Grunt":
        plasma = [c for c in ctx.hand() if _team_plasma(c)]
        card = await _choose_one(ctx, plasma, "Discard a Team Plasma card") \
            if plasma else None
        if card is not None:
            await ctx.discard_cards([card])
            await ctx.draw_cards(4)
        return

    if name == "Shadow Triad":
        cards = [c for c in ctx.discard_pile() if _team_plasma(c)]
        pick = await _choose_one(ctx, cards, "Choose a Team Plasma card") \
            if cards else None
        if pick is not None:
            await ctx.put_in_hand([pick], reveal=True)
        return

    if name == "Superior Energy Retrieval":
        paid = await ctx.discard_from_hand(2, prompt="Discard 2 cards")
        if len(paid) != 2:
            return
        paid_ids = {card.entity_id for card in paid}
        energies = [c for c in ctx.discard_pile()
                    if is_basic_energy(c) and c.entity_id not in paid_ids]
        picks = await ctx.choose_cards(
            energies, min(4, len(energies)), minimum=0,
            prompt="Choose up to 4 basic Energy cards",
        ) if energies else []
        await ctx.put_in_hand(picks, reveal=True)
        return

    if name == "Team Plasma Ball":
        picks = await ctx.search_deck(
            lambda c: is_pokemon_card(c) and _team_plasma(c),
            count=1, minimum=0, prompt="Choose a Team Plasma Pokémon",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
        return

    if name == "Battle City":
        # The Stadium's clickable Ability owns this effect; this branch keeps
        # old/reprint definitions functional if they still register an effect.
        await battle_city(ctx)
        return

    if name == "Cedric Juniper":
        # The physical card asks the opponent to reveal a Pokémon from hand,
        # then lets the user guess its height.  Height is absent from the
        # protocol card model, so preserve the meaningful hidden-information
        # interaction and use a fair guess coin: correct -> draw 3.
        pokemon = [c for c in ctx.hand(ctx.opponent_id) if is_pokemon_card(c)]
        if pokemon:
            shown = random.choice(pokemon)
            await ctx.reveal_cards([shown])
            if (await ctx.flip_coins(1, name))[0]:
                await ctx.draw_cards(3)
        return

    # First Ticket modifies pre-game setup, outside normal Trainer resolution.
    # If an old client nevertheless plays it, it intentionally has no effect.


bw_trainer_effect.play_condition = bw_trainer_playable


# ---------------------------------------------------------------------------
# Stadium abilities and triggered effects
# ---------------------------------------------------------------------------

async def tropical_beach(ctx):
    await ctx.draw_until(7)


async def pokemon_center(ctx):
    candidates = [p for p in ctx.my_bench() if _damaged(ctx, p)]
    target = await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon") \
        if candidates else None
    if target is not None:
        await ctx.heal(20, target)


async def twist_mountain(ctx):
    if not (await ctx.flip_coins(1, "Twist Mountain"))[0]:
        return
    cards = [c for c in ctx.hand()
             if is_pokemon_card(c)
             and c.get_attribute(AttrID.STAGE) == PokemonStage.RESTORED.value]
    pick = await _choose_one(ctx, cards, "Choose a Restored Pokémon") \
        if cards else None
    if pick is not None:
        await ctx.bench_pokemon(pick)


async def battle_city(ctx):
    if (await ctx.flip_coins(1, "Battle City"))[0]:
        await ctx.draw_cards(1)


async def champions_festival(ctx):
    if len(ctx.my_pokemon_in_play()) < 6:
        return
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(10, pokemon)


async def frozen_city_trigger(ctx):
    receiver = getattr(ctx, "energy_receiver", None)
    attaching = getattr(ctx, "attaching_player_id", None)
    if receiver is None or attaching is None or _team_plasma(receiver):
        return
    if getattr(ctx, "attached_energy", None) is None:
        return
    await ctx.deal_damage(20, target=receiver, apply_modifiers=False,
                          as_counters=True)


def bw_stadium_ability(name: str) -> Optional[Ability]:
    table = {
        "Tropical Beach": (tropical_beach, True),
        "Pokémon Center": (pokemon_center, False),
        "Twist Mountain": (twist_mountain, False),
        "Battle City": (battle_city, False),
        "Champions Festival": (champions_festival, False),
    }
    spec = table.get(name)
    if spec is None:
        return None
    effect, ends_turn = spec
    return Ability(
        title=name,
        game_text="Use this Stadium's effect.",
        activation=Activations.ONCE_PER_TURN,
        effect=effect,
        ends_turn=ends_turn,
    )


def bw_stadium_triggers(name: str) -> list[Ability]:
    if name != "Frozen City":
        return []
    return [Ability(
        title="Frozen City",
        game_text="Whenever a player attaches an Energy from hand to a non-Team Plasma Pokémon, put 2 damage counters on it.",
        trigger=Triggers.ON_ENERGY_ATTACHED,
        effect=frozen_city_trigger,
    )]


# ---------------------------------------------------------------------------
# BW Tool/Stadium and generated Ability passives
# ---------------------------------------------------------------------------

class _BasicDamageReduction(Passive):
    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not calc.target or not calc.is_attack or not calc.is_opposing:
            return
        if holder.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value:
            calc.amount = max(0, calc.amount - 20)


class _HolderDamageBoost(Passive):
    def __init__(self, amount, holder_pred=None, target_pred=None):
        self.amount = amount
        self.holder_pred = holder_pred
        self.target_pred = target_pred

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not calc.attacker or not calc.is_attack or not calc.is_opposing:
            return
        if self.holder_pred and not self.holder_pred(holder):
            return
        if self.target_pred and not self.target_pred(calc.target):
            return
        calc.amount += self.amount


class _GlobalHpBonus(Passive):
    def __init__(self, amount, pred):
        self.amount, self.pred = amount, pred

    def max_hp_bonus(self, pokemon, carrier):
        return self.amount if self.pred(pokemon) else 0


class _GlobalRetreatDiscount(Passive):
    def __init__(self, amount, pred):
        self.amount, self.pred = amount, pred

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        return max(0, cost - self.amount) if self.pred(pokemon) else cost


class _NoWeaknessWithPlasmaEnergy(Passive):
    def modify_weakness(self, calc, carrier):
        target = calc.target
        if any(_name(e) == "Plasma Energy" for e in _attached(target)):
            calc.weakness_applies = False


class _VirbankPassive(Passive):
    def modify_poison_counters(self, counters, pokemon, carrier):
        return counters + 2


class _ToolboxHp(Passive):
    def __init__(self, amount, name, holder_pred=None):
        self.amount, self.name = amount, name
        self.holder_pred = holder_pred

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        if self.holder_pred is not None and not self.holder_pred(pokemon):
            return 0
        return self.amount


def _attached(pokemon) -> list:
    out, stack = [], list(getattr(pokemon, "children", []) or [])
    while stack:
        card = stack.pop()
        if is_energy_card(card):
            out.append(card)
        stack.extend(getattr(card, "children", []) or [])
    return out


def bw_trainer_passive(name: str) -> Optional[Passive]:
    if name == "Eviolite":
        return _BasicDamageReduction()
    if name == "Dark Claw":
        return _HolderDamageBoost(20, lambda p: PokemonTypes.DARKNESS.value in
                                  (p.get_attribute(AttrID.POKEMON_TYPES) or []))
    if name == "Giant Cape":
        return _ToolboxHp(20, name)
    if name == "Skyarrow Bridge":
        return _GlobalRetreatDiscount(
            1, lambda p: p.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value)
    if name == "Aspertia City Gym":
        return _GlobalHpBonus(
            20, lambda p: PokemonTypes.COLORLESS.value in
            (p.get_attribute(AttrID.POKEMON_TYPES) or []))
    if name == "Plasma Frigate":
        return _NoWeaknessWithPlasmaEnergy()
    if name == "Virbank City Gym":
        return _VirbankPassive()
    if name == "Crystal Edge":
        return _HolderDamageBoost(50, lambda p: _name(p) == "White Kyurem-EX")
    if name == "Crystal Wall":
        return _ToolboxHp(130, name, lambda p: _name(p) == "Black Kyurem-EX")
    if name == "Victory Piece":
        return _VictoryPiecePassive()
    return None


class _VictoryPiecePassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon and _name(pokemon) == "Victini-EX":
            return {}
        return cost


async def rock_guard_trigger(ctx):
    attacker = getattr(ctx, "damaged_by", None)
    if attacker is not None and attacker.owning_player_id != ctx.source.owning_player_id:
        await ctx.deal_damage(60, target=attacker, apply_modifiers=False,
                              as_counters=True)


async def rescue_scarf_trigger(ctx):
    pokemon = ctx.source
    # ON_KNOCKED_OUT resolves after the public Knockout movement.  Use the
    # pre-move snapshot supplied by the resolver because the evolution cards
    # are separate discard-pile children by the time this trigger runs.
    stack = getattr(ctx, "knocked_out_stack", None) or full_stack(pokemon)
    # Follow the printed evolution line so an attached Pokémon Tool is not
    # incorrectly returned as a prior stage.
    cards, _ = split_pokemon_stack(pokemon, stack)
    await ctx.put_in_hand(cards, reveal=False)


def bw_tool_abilities(name: str) -> list[Ability]:
    if name == "Rock Guard":
        return [Ability(
            title="Rock Guard", game_text="Put 6 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK, effect=rock_guard_trigger,
        )]
    if name == "Rescue Scarf":
        return [Ability(
            title="Rescue Scarf", game_text="Return the Knocked Out Pokémon to your hand.",
            trigger=Triggers.ON_KNOCKED_OUT, effect=rescue_scarf_trigger,
        )]
    return []


class _BWTextPassive(Passive):
    """Continuous BW Pokémon text represented directly by its printed text.

    This covers the recurring prevention, HP, retreat, Weakness and team-damage
    templates used throughout the block.  Bespoke passives remain in their
    card scripts and therefore take precedence over this fallback.
    """
    def __init__(self, text: str):
        self.text = _norm(text)
        if "doesn't stack" in self.text \
                or "can't apply more than 1" in self.text:
            self.stacking_key = f"shared-text:{self.text}"

    def _claim_nonstacking(self, calc) -> bool:
        if self.stacking_key is None:
            return True
        if self.stacking_key in calc.applied_once:
            return False
        calc.applied_once.add(self.stacking_key)
        return True

    async def damage_interceptor(self, ctx, calc, target, carrier):
        """Coin-based prevention/reduction that cannot be represented by a
        synchronous damage hook (Carracosta's Solid Rock)."""
        holder = carrier_pokemon(carrier)
        if holder is not target or not calc.is_attack or not calc.is_opposing \
                or calc.amount <= 0:
            return None
        t = self.text
        attacker = calc.attacker
        attacker_types = set(effective_pokemon_types(calc.board, attacker))
        holder_types = set(effective_pokemon_types(calc.board, holder))
        lethal_hit = calc.amount >= holder.get_attribute(AttrID.HP, 0)

        # Echolocation / Drifting Dodge / Fluffy Cotton.  This is evaluated
        # after every ordinary modifier, just before HP changes, exactly once
        # for the hit.  The prevention animation is driven by calc.prevented.
        if "if any damage is done to this pokémon by attacks" in t \
                and "if heads, prevent that damage" in t:
            if (await ctx.flip_coins(1, "Damage prevention"))[0]:
                calc.prevented = True
                return 0

        # Guts / Durable Body / Tenacious Body do not require full HP.  Static
        # Sturdy/Resolute Heart shares the same replacement without the flip.
        if "would be knocked out by damage from an attack" in t \
                and "remaining hp becomes 10" in t \
                and "has full hp" not in t:
            hp = holder.get_attribute(AttrID.HP, 0)
            if calc.amount >= hp:
                if "flip a coin" not in t \
                        or (await ctx.flip_coins(1, "Survive the Knock Out"))[0]:
                    return max(0, hp - 10)

        # Focus Sash / Survival Brace: replace a lethal hit from full HP and
        # discard the Tool after the attack choreography.
        if "has full hp and would be knocked out" in t:
            if "fighting pokémon" in t \
                    and PokemonTypes.FIGHTING.value not in holder_types:
                return None
            hp = holder.get_attribute(AttrID.HP, 0)
            if hp >= effective_max_hp(calc.board, holder) and calc.amount >= hp:
                async def discard_survival_tool():
                    if getattr(carrier, "parent", None) is not None:
                        await ctx.discard_cards([carrier])
                ctx.deferred_actions.append(discard_survival_tool)
                return max(0, hp - 10)

        deferred = []
        # Type Berries reduce synchronously; this hook consumes the Berry.
        berry = re.search(
            r"damaged by an attack from your opponent's (darkness|dragon|fire|"
            r"metal|psychic|water) pokémon, it takes \d+ less damage.*discard this card",
            t,
        )
        if berry:
            required = getattr(PokemonTypes, berry.group(1).upper()).value
            if required in attacker_types:
                async def discard_berry():
                    if getattr(carrier, "parent", None) is not None:
                        await ctx.discard_cards([carrier])
                deferred.append(discard_berry)

        counters = 0
        counter_match = re.search(
            r"put (\d+) damage counters on the attacking pokémon", t
        ) or re.search(
            r"place (\d+) damage counters on the attacking pokémon", t
        )
        if counter_match:
            counters = int(counter_match.group(1))
            if "is knocked out by damage" in t and "even if" not in t \
                    and not lethal_hit:
                counters = 0
            if "dragon pokémon this card is attached to" in t \
                    and PokemonTypes.DRAGON.value not in holder_types:
                counters = 0
            if "darkness pokémon this card is attached to" in t \
                    and PokemonTypes.DARKNESS.value not in holder_types:
                counters = 0
            if "attacking pokémon-ex" in t and not _pokemon_ex(attacker):
                counters = 0
            if "is your active pokémon" in t and not _is_active(holder):
                counters = 0
            threshold = re.search(r"takes (\d+) or more damage", t)
            if threshold and calc.amount < int(threshold.group(1)):
                counters = 0
            if "mega evolution pokémon ex" in t and not _has_subtype(attacker, "MEGA"):
                counters = 0
            if "attached to isn't a mega evolution pokémon ex" in t \
                    and _has_subtype(holder, "MEGA"):
                counters = 0
            if counters and "flip a coin" in t and "if heads, put" in t:
                if not (await ctx.flip_coins(1, "Knock Out reaction"))[0]:
                    counters = 0
        status = None
        if "attacking pokémon is now confused" in t:
            status = SpecialConditions.CONFUSED
        elif "attacking pokémon is now poisoned" in t:
            status = SpecialConditions.POISONED
        elif "attacking pokémon is now asleep" in t:
            status = SpecialConditions.ASLEEP
        elif "attacking pokémon is now burned" in t:
            status = SpecialConditions.BURNED
        if status is not None and "is your active pokémon" in t and not _is_active(holder):
            status = None
        if status is not None and "team rocket's pokémon this card is attached to" in t \
                and not _name(holder).casefold().startswith("team rocket's "):
            status = None

        if counters or status is not None:
            async def retaliate():
                live_attacker = ctx.board.get_entity(attacker.entity_id)
                if not isinstance(live_attacker, PokemonEntity):
                    return
                if counters:
                    await ctx.deal_damage(
                        counters * 10, target=live_attacker,
                        apply_modifiers=False, as_counters=True, is_attack=False,
                    )
                if status is not None:
                    await ctx.apply_special_condition(live_attacker, status)
                if "discard this card" in t and getattr(carrier, "parent", None) is not None:
                    await ctx.discard_cards([carrier])
                if ctx.knockouts:
                    await ctx.session.resolve_knockouts(ctx)
            deferred.append(retaliate)

        if "draw 3 cards" in t and "has weakness to your opponent's active" in t \
                and _is_active(holder) and set(
                    holder.get_attribute(AttrID.WEAKNESS_TYPES) or []
                ).intersection(attacker_types):
            async def draw_three():
                await ctx.draw_cards(3, player_id=holder.owning_player_id)
            deferred.append(draw_three)

        if "discard a random card from your opponent's hand" in t \
                and _is_active(holder):
            async def discard_random():
                hand = ctx.hand(attacker.owning_player_id)
                if hand:
                    await ctx.discard_cards([random.choice(hand)])
            deferred.append(discard_random)

        bench_counters = re.search(
            r"put (\d+) damage counters on each of your benched pokémon", t
        )
        if bench_counters and _is_active(holder):
            async def damage_own_bench():
                for benched in list(ctx.board.pokemon_in_play(holder.owning_player_id)):
                    if _is_active(benched):
                        continue
                    await ctx.deal_damage(
                        int(bench_counters.group(1)) * 10, target=benched,
                        apply_modifiers=False, as_counters=True, is_attack=False,
                    )
                if ctx.knockouts:
                    await ctx.session.resolve_knockouts(ctx)
            deferred.append(damage_own_bench)

        if "search your deck for up to 2 pokémon that have \"koffing\"" in t \
                and _is_active(holder):
            async def bench_koffing():
                capacity = effective_bench_capacity(
                    ctx.board, holder.owning_player_id)
                open_slots = max(0, capacity - len([
                    pokemon for pokemon in ctx.board.pokemon_in_play(
                        holder.owning_player_id) if not _is_active(pokemon)
                ]))
                cards = await ctx.search_deck(
                    lambda card: is_basic_pokemon(card)
                    and "koffing" in _name(card).casefold(),
                    min(2, open_slots), minimum=0,
                    prompt="Choose Koffing to put onto your Bench",
                    player_id=holder.owning_player_id,
                )
                for card in cards:
                    await ctx.bench_pokemon(card)
                await ctx.shuffle_deck(holder.owning_player_id)
            deferred.append(bench_koffing)

        if deferred:
            ctx.deferred_actions.extend(deferred)

        if "flip a coin" not in t or "reduce that damage by 50" not in t:
            return None
        heads = bool((await ctx.flip_coins(1, "Solid Rock"))[0])
        return max(0, calc.amount - 50) if heads else None

    async def attack_followup(self, ctx, carrier):
        # Retaliations are snapshotted by damage_interceptor before a Knock
        # Out moves the Tool/Energy out of play.  Keeping the old post-KO path
        # here made Dangerous Energy fire twice whenever its holder survived.
        return

    def modify_damage_dealt(self, calc, carrier):
        t = self.text
        if not (calc.is_attack and calc.is_opposing and calc.attacker is not None):
            return
        # Only attack-output clauses belong before Weakness/Resistance.
        # "Take N less damage" is defensive, and "N more damage counters"
        # belongs to Checkup; neither changes the carrier's own attacks.
        modifier = re.search(
            r"\b(?:do|does) (\d+) (more|less) damage\b(?! counters?)([^.]*)", t
        )
        if modifier is None:
            return
        amount = int(modifier.group(1)) if modifier.group(2) == "more" else 0
        less = int(modifier.group(1)) if modifier.group(2) == "less" else 0
        damage_clause = modifier.group(0)
        if re.search(
                r"\bto (?:your opponent's |the opponent's |the )?"
                r"(?:active|defending)\b", damage_clause) and not calc.to_active:
            return
        owner = carrier.owning_player_id
        holder = carrier_pokemon(carrier)
        # Some outgoing modifiers name the opposing attacker as their
        # subject but restrict the damage destination to this holder.
        holder_target = re.search(
            r"\bto the (?:(grass|fire|water|lightning|psychic|fighting|darkness|"
            r"metal|fairy|dragon|colorless) )?pokémon this card is attached to",
            damage_clause,
        )
        if holder_target:
            if holder is not calc.target:
                return
            if holder_target.group(1) and getattr(
                    PokemonTypes, holder_target.group(1).upper()).value not in \
                    effective_pokemon_types(calc.board, calc.target):
                return
            if self._claim_nonstacking(calc):
                calc.amount += amount - less
            return
        if holder is not None and "as long as this pokémon is on your bench" in t \
                and _is_active(holder):
            return
        if holder is not None and (
                "as long as this pokémon is your active pokémon" in t
                or "as long as this pokémon is in the active spot" in t
        ) and not _is_active(holder):
            return
        named_attackers = {
            "zygarde's and zygarde-gx's attacks": {"zygarde", "zygarde-gx"},
            "attacks used by your marowak": {"marowak"},
            "your passimian's attacks": {"passimian"},
            "your nidoqueen's attacks": {"nidoqueen"},
            "your registeel's attacks": {"registeel"},
            "your wishiwashi-gx": {"wishiwashi-gx"},
        }
        opposing_active_attacks = bool(re.search(
            r"\byour opponent's active pokémon's attacks?\b|"
            r"\battacks used by your opponent's active pokémon\b", t
        ))
        team_wide = any(phrase in t for phrase in (
            "your pokémon's attacks", "your dragon pokémon's attacks",
            "your team plasma pokémon's attacks",
            "attacks used by your ", "attacks of your ",
            "each of your basic pokémon's attacks",
            "the attacks of your ", "all of your pokémon",
            "your opponent's active pokémon's attacks",
            "attacks used by your opponent's active pokémon",
            "pokémon in play (both yours and your opponent's)",
            "pokémon (both yours and your opponent's)",
        )) or _has_subtype(carrier, "Stadium") or opposing_active_attacks \
            or any(phrase in t for phrase in named_attackers)
        if not team_wide and holder is not calc.attacker:
            return
        if team_wide and "your " in t and "both yours and your opponent's" not in t \
                and calc.attacker.owning_player_id != owner:
            # Intimidating Fang/Pressure modifies the opposing attacker while
            # its source remains Active.  Every other "your ... attacks"
            # family benefits the carrier's side.
            # Mentioning the opposing Active as the DAMAGE TARGET does not
            # make an own-team aura apply to the opposing attacker.
            if not opposing_active_attacks:
                return
        if opposing_active_attacks and (
                calc.attacker.owning_player_id == owner
                or not _is_active(calc.attacker)):
            return
        if "this ↓ player's darkness pokémon" in t and (
                calc.attacker.owning_player_id != owner
                or PokemonTypes.DARKNESS.value not in set(
                    effective_pokemon_types(calc.board, calc.attacker))):
            return
        attacker_types = set(effective_pokemon_types(calc.board, calc.attacker))
        target_types = set(effective_pokemon_types(calc.board, calc.target))
        if "basic pokémon this card is attached to" in t and \
                _stage(holder) != PokemonStage.BASIC.value:
            return
        if "stage 1 pokémon" in t and _stage(calc.attacker) != PokemonStage.STAGE1.value:
            return
        if "basic pokémon" in t and "this card is attached to" not in t \
                and _stage(calc.attacker) != PokemonStage.BASIC.value:
            return
        if "non-ultra beast pokémon" in t and _has_subtype(calc.attacker, "Ultra Beast"):
            return
        if "ultra beast" in t and "non-ultra beast" not in t \
                and not _has_subtype(calc.attacker, "Ultra Beast"):
            return
        if "future pokémon" in t and not _has_subtype(calc.attacker, "Future"):
            return
        if "hop's pokémon" in t and not _name(calc.attacker).casefold().startswith("hop's "):
            return
        if "starmie-gx" in t and _name(calc.attacker).casefold() != "starmie-gx":
            return
        if "pikachu ex" in t and _name(calc.attacker).casefold() != "pikachu ex":
            return
        if "darkness pokémon" in t and "dragon pokémon" in t:
            if not attacker_types.intersection({
                    PokemonTypes.DARKNESS.value, PokemonTypes.DRAGON.value}):
                return
        elif "darkness pokémon" in t and PokemonTypes.DARKNESS.value not in attacker_types:
            return
        if "fighting pokémon" in t and PokemonTypes.FIGHTING.value not in attacker_types:
            return
        if "dragon pokémon" in t and "darkness pokémon" not in t \
                and PokemonTypes.DRAGON.value not in attacker_types:
            return
        if "team plasma pokémon's attacks" in t and not _team_plasma(calc.attacker):
            return
        if "your basic pokémon's attacks" in t \
                or "each of your basic pokémon's attacks" in t:
            if _stage(calc.attacker) != PokemonStage.BASIC.value:
                return
        if "evolution fire pokémon" in t and not (
                _stage(calc.attacker) != PokemonStage.BASIC.value
                and PokemonTypes.FIRE.value in attacker_types):
            return
        if "your grass pokémon and fire pokémon" in t \
                and not attacker_types.intersection({
                    PokemonTypes.GRASS.value, PokemonTypes.FIRE.value}):
            return
        if "your metal pokémon" in t and PokemonTypes.METAL.value not in attacker_types:
            return
        if "your fighting pokémon" in t and PokemonTypes.FIGHTING.value not in attacker_types:
            return
        if "your lightning pokémon" in t and PokemonTypes.LIGHTNING.value not in attacker_types:
            return
        if "your tag team pokémon" in t and not _has_subtype(calc.attacker, "TAG TEAM"):
            return
        if "your ultra beasts" in t and not _has_subtype(calc.attacker, "Ultra Beast"):
            return
        if "your pokémon-gx in play that evolve from eevee" in t and not (
                _has_subtype(calc.attacker, "GX")
                and evolves_from(calc.attacker.archetype_id, "Eevee")):
            return
        for phrase, names in named_attackers.items():
            if phrase in t and _name(calc.attacker).casefold() not in names:
                return
        if "your cynthia's pokémon" in t \
                and not _name(calc.attacker).casefold().startswith("cynthia's "):
            return
        if "excluding regirock-ex" in t \
                and _name(calc.attacker).casefold() == "regirock-ex":
            return
        if "excluding deoxys-ex" in t \
                and _name(calc.attacker).casefold() == "deoxys-ex":
            return
        if "excluding" in t and calc.attacker is carrier:
            return
        if "basic fighting energy attached" in t and not any(
                is_basic_energy(e) and energy_provides_type(e, PokemonTypes.FIGHTING.value)
                for e in _attached(calc.attacker)):
            return
        if "affected by a special condition" in t and not \
                (holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            return
        if "has any darkness energy attached" in t \
                and not _has_energy_type(calc.attacker, PokemonTypes.DARKNESS):
            return
        if "has any special energy attached" in t and not any(
                is_special_energy(e) for e in _attached(calc.attacker)):
            return
        if "has any damage counters on it" in t and not _damage_counters_on(calc.attacker):
            return
        minimum_counters = re.search(r"has (\d+) or more damage counters", t)
        if minimum_counters and _damage_counters_on(calc.attacker) < int(minimum_counters.group(1)):
            return
        remaining_limit = re.search(r"remaining hp is (\d+) or less", t)
        if remaining_limit and calc.attacker.get_attribute(AttrID.HP, 0) \
                > int(remaining_limit.group(1)):
            return
        if "has full hp" in t and calc.attacker.get_attribute(AttrID.HP, 0) \
                < effective_max_hp(calc.board, calc.attacker):
            return
        if "darkness mega evolution pokémon ex in play" in t and not any(
                _pokemon_ex(p) and _has_subtype(p, "MEGA")
                and PokemonTypes.DARKNESS.value in effective_pokemon_types(calc.board, p)
                for p in _pokemon_in_play_from(carrier, owner)):
            return
        if "if you have nidoqueen in play" in t \
                and not _has_named_in_play(carrier, owner, "Nidoqueen"):
            return
        if "if you have simisage, simisear, and simipour in play" in t \
                and not all(_has_named_in_play(carrier, owner, name)
                            for name in ("Simisage", "Simisear", "Simipour")):
            return
        if "if you have lunala in play" in t \
                and not _has_named_in_play(carrier, owner, "Lunala"):
            return
        if "as long as you don't have more pokémon in play than your opponent" in t:
            opponent_id = _other_player_id(calc.board, owner)
            if opponent_id is None or len(_pokemon_in_play_from(carrier, owner)) \
                    > len(_pokemon_in_play_from(carrier, opponent_id)):
                return
        if "30 hp or less remaining" in t and (
                holder.get_attribute(AttrID.HP, 0) > 30
                or holder.get_attribute(AttrID.HP, 0) >= effective_max_hp(calc.board, holder)):
            return
        if "more prize cards remaining than your opponent" in t:
            opponent_id = _other_player_id(calc.board, calc.attacker.owning_player_id)
            if opponent_id is None or _prizes_remaining(carrier, calc.attacker.owning_player_id) \
                    <= _prizes_remaining(carrier, opponent_id):
                return
        if "same number of cards in your hand as your opponent" in t:
            own = _area_from(carrier, carrier.owning_player_id, "hand")
            opponent_id = _other_player_id(calc.board, carrier.owning_player_id)
            other = _area_from(carrier, opponent_id, "hand") if opponent_id else None
            if own is None or other is None or len(own.children) != len(other.children):
                return
        targets_gx = "active pokémon-gx" in damage_clause \
            or "defending pokémon-gx" in damage_clause
        targets_ex = "active pokémon-ex" in damage_clause \
            or "defending pokémon-ex" in damage_clause
        if targets_gx or targets_ex:
            if not (targets_gx and _has_subtype(calc.target, "GX")
                    or targets_ex and _pokemon_ex(calc.target)):
                return
        if "active pokémon ex" in t and not _has_exact_subtype(calc.target, "ex"):
            return
        if "active evolution pokémon" in t \
                and _stage(calc.target) == PokemonStage.BASIC.value:
            return
        if "active pokémon that has an ability" in t and not _has_pokemon_ability(calc.target):
            return
        for word, ptype in (
            ("grass", PokemonTypes.GRASS), ("darkness", PokemonTypes.DARKNESS),
        ):
            if f"opponent's {word} pokémon" in t and ptype.value not in target_types:
                return
        if not self._claim_nonstacking(calc):
            return
        if "for each prize card you have taken" in t:
            dealt = getattr(calc.board, "prizes_dealt", {}).get(
                calc.attacker.owning_player_id, 6)
            amount = (amount or 0) * max(
                0, int(dealt) - _prizes_remaining(carrier, calc.attacker.owning_player_id)
            )
        if "for each prize card your opponent has taken" in t:
            opponent_id = _other_player_id(calc.board, calc.attacker.owning_player_id)
            dealt = getattr(calc.board, "prizes_dealt", {}).get(opponent_id, 6)
            amount = (amount or 0) * max(
                0, int(dealt) - _prizes_remaining(carrier, opponent_id)
            )
        if "for each of their pokémon-gx and pokémon-ex in play" in t:
            opponent_id = _other_player_id(calc.board, calc.attacker.owning_player_id)
            amount = (amount or 0) * sum(
                _has_subtype(p, "GX") or _pokemon_ex(p)
                for p in _pokemon_in_play_from(carrier, opponent_id)
            )
        if "those attacks do 40 more damage instead" in t:
            opponent_id = _other_player_id(calc.board, calc.attacker.owning_player_id)
            if opponent_id is not None and _prizes_remaining(
                    carrier, calc.attacker.owning_player_id) > _prizes_remaining(
                    carrier, opponent_id):
                amount = 40
        calc.amount += (amount or 0) - (less or 0)

    def modify_damage_taken(self, calc, carrier):
        t = self.text
        if not (calc.is_attack and calc.is_opposing):
            return
        reduction = re.search(r"\b(?:take|takes) (\d+) less damage\b", t)
        if reduction is None and "reduced by" not in t:
            # An opposing attack that "does N less" was already modified
            # before W/R. Do not subtract it again on the defender's side.
            return
        holder = carrier_pokemon(carrier)
        stadium = _has_subtype(carrier, "Stadium")
        if holder is not None and "as long as this pokémon is on your bench" in t \
                and _is_active(holder):
            return
        if holder is not None and (
                "as long as this pokémon is your active pokémon" in t
                or "as long as this pokémon is in the active spot" in t
        ) and not _is_active(holder):
            return
        team_wide = stadium or "pokémon (both yours and your opponent's)" in t \
            or "pokémon in play (both yours and your opponent's)" in t \
            or "all of your pokémon" in t or "your grass pokémon" in t \
            or "your metal pokémon" in t or "your ultra beasts" in t \
            or "your tag team pokémon" in t or "your pokémon by" in t \
            or "all of your steven's pokémon" in t \
            or "each of your water pokémon" in t
        if not team_wide and holder is not calc.target:
            return
        if team_wide and "both yours and your opponent's" not in t \
                and calc.target.owning_player_id != carrier.owning_player_id:
            return
        attacker_types = set(effective_pokemon_types(calc.board, calc.attacker))
        target_types = set(effective_pokemon_types(calc.board, calc.target))
        if "this ↓ player's metal pokémon" in t and (
                calc.target.owning_player_id != carrier.owning_player_id
                or PokemonTypes.METAL.value not in target_types):
            return
        if _name(carrier).casefold() == "metal energy" \
                and PokemonTypes.METAL.value not in target_types:
            return
        if "opponent's grass, fire, water, or lightning pokémon" in t \
                or "opponent's grass, fire, water, or lightning pokémon" in t:
            protected_from = {
                PokemonTypes.GRASS.value, PokemonTypes.FIRE.value,
                PokemonTypes.WATER.value, PokemonTypes.LIGHTNING.value,
            }
            if not attacker_types & protected_from:
                return
        opponent_type = re.search(
            r"opponent's (grass|fire|water|lightning|psychic|fighting|darkness|metal|dragon) pokémon",
            t,
        )
        if opponent_type:
            required = getattr(PokemonTypes, opponent_type.group(1).upper()).value
            if required not in attacker_types:
                return
        target_type = re.search(
            r"(?:the |each )?(grass|fire|water|lightning|psychic|fighting|darkness|metal|dragon) "
            r"pokémon (?:this card is attached to|\(both yours)", t,
        )
        # Aether Paradise names two eligible types. The trailing Lightning
        # phrase alone must not filter out the Grass Pokemon in the same rule.
        if target_type and "basic grass and basic lightning pokémon" not in t:
            required = getattr(PokemonTypes, target_type.group(1).upper()).value
            if required not in target_types:
                return
        if "stage 1 pokémon" in t and _stage(calc.target) != PokemonStage.STAGE1.value:
            return
        if "your grass pokémon" in t and PokemonTypes.GRASS.value not in target_types:
            return
        if "your metal pokémon" in t and PokemonTypes.METAL.value not in target_types:
            return
        if "each of your water pokémon" in t and PokemonTypes.WATER.value not in target_types:
            return
        if "your ultra beasts" in t and not _has_subtype(calc.target, "Ultra Beast"):
            return
        if "your tag team pokémon" in t and not _has_subtype(calc.target, "TAG TEAM"):
            return
        if "steven's pokémon" in t \
                and not _name(calc.target).casefold().startswith("steven's "):
            return
        if "that have any metal energy attached" in t \
                and not _has_energy_type(calc.target, PokemonTypes.METAL):
            return
        if "that has any water energy attached" in t \
                and not _has_energy_type(calc.target, PokemonTypes.WATER):
            return
        for word, ptype in (
            ("grass", PokemonTypes.GRASS), ("lightning", PokemonTypes.LIGHTNING),
            ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
            ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
        ):
            if f"has any {word} energy attached" in t \
                    and not _has_energy_type(calc.target, ptype):
                return
        if "has any basic energy attached" in t and not any(
                is_basic_energy(e) for e in _attached(calc.target)):
            return
        if "has any energy attached" in t and not _attached(calc.target):
            return
        if "has any special energy attached" in t and not any(
                is_special_energy(e) for e in _attached(calc.target)):
            return
        if "has full hp" in t and calc.target.get_attribute(AttrID.HP, 0) \
                < effective_max_hp(calc.board, calc.target):
            return
        if "basic grass and basic lightning pokémon" in t and not (
                _stage(calc.target) == PokemonStage.BASIC.value
                and target_types.intersection({PokemonTypes.GRASS.value,
                                               PokemonTypes.LIGHTNING.value})):
            return
        if "steven's pokémon" in t and not _name(calc.target).casefold().startswith("steven's "):
            return
        if "onix-gx" in t and _name(calc.target).casefold() != "onix-gx":
            return
        if "regirock, regice, registeel, or regigigas" in t \
                and _name(calc.target).casefold() not in {
                    "regirock", "regice", "registeel", "regigigas"}:
            return
        if "opponent's pokémon that have an ability" in t \
                and not _has_pokemon_ability(calc.attacker):
            return
        if "opponent's non-fire pokémon" in t \
                and PokemonTypes.FIRE.value in attacker_types:
            return
        if "opponent's pokémon-gx and pokémon-ex" in t \
                and not (_has_subtype(calc.attacker, "GX") or _pokemon_ex(calc.attacker)):
            return
        if "any special energy attached" in t and not any(
                is_special_energy(e) for e in _attached(calc.attacker)):
            return
        if "more prize cards remaining than your opponent" in t:
            opponent_id = _other_player_id(calc.board, calc.target.owning_player_id)
            if opponent_id is None or _prizes_remaining(carrier, calc.target.owning_player_id) \
                    <= _prizes_remaining(carrier, opponent_id):
                return
        if "if you have lunala in play" in t \
                and not _has_named_in_play(carrier, carrier.owning_player_id, "Lunala"):
            return
        if "your solgaleo and lunala" in t \
                and _name(calc.target).casefold() not in {"solgaleo", "lunala"}:
            return
        if "as long as you don't have more pokémon in play than your opponent" in t:
            opponent_id = _other_player_id(calc.board, carrier.owning_player_id)
            if opponent_id is None or len(_pokemon_in_play_from(
                    carrier, carrier.owning_player_id)) > len(
                        _pokemon_in_play_from(carrier, opponent_id)):
                return
        # Dynamic reductions (for example Lonely Bone) are handled below.  Do
        # not also apply their printed per-card value as a flat reduction.
        amount = None if (
            "flip a coin" in t or "reduced by" in t and " for each " in t
        ) else (_number_after(t, "reduced by") or
                (int(reduction.group(1)) if reduction else None))
        if amount is not None:
            if not self._claim_nonstacking(calc):
                return
            calc.amount = max(0, calc.amount - amount)
        lonely = re.search(
            r"reduced by (\d+) for each marowak in your discard pile", t
        )
        if lonely:
            discard = _area_from(carrier, carrier.owning_player_id, "discard")
            reduction = int(lonely.group(1)) * sum(
                1 for card in (discard.children if discard else [])
                if _name(card) == "Marowak"
            )
            calc.amount = max(0, calc.amount - reduction)
        heavy = re.search(
            r"reduced by (\d+) for each colorless in your opponent's active "
            r"pokémon's retreat cost", t,
        )
        if heavy:
            reduction = int(heavy.group(1)) * effective_retreat_cost(
                calc.board, calc.attacker)
            calc.amount = max(0, calc.amount - reduction)

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        t = self.text
        holder = carrier_pokemon(carrier)
        if holder is not None and "as long as this pokémon is on your bench" in t \
                and _is_active(holder):
            return cost
        if holder is not None and (
                "as long as this pokémon is your active pokémon" in t
                or "as long as this pokémon is in the active spot" in t
        ) and not _is_active(holder):
            return cost
        # Determine the subject from the cost clause, not from unrelated text
        # elsewhere on the card.  Head Ringer, for example, says it attaches
        # to an opponent's Pokemon-EX before stating that *the holder's*
        # attacks cost more; treating every occurrence of "your opponent's"
        # as a team-wide scope switches its own passive off.  The same mistake
        # affected self-scoped Pokemon whose discount depends on the opposing
        # Bench (Incineroar ex).
        holder_scoped = any(phrase in t for phrase in (
            "this pokémon's attacks",
            "attacks of this pokémon",
            "attacks used by this pokémon",
            "attacks of the pokémon this card is attached to",
            "attacks used by the pokémon this card is attached to",
            "the attacks of the pokémon this card is attached to",
        ))
        team_wide = not holder_scoped and (
            "pokémon in play (both yours and your opponent's)" in t
            or "pokémon (both yours and your opponent's)" in t
            or "each psychic pokémon's attacks" in t
            or "attacks used by each basic pokémon" in t
            or "each of your pokémon" in t
            or "your pokémon" in t and "attacks" in t
            or "your opponent's" in t and "attacks" in t
        )
        if not team_wide and holder is not pokemon:
            return cost
        if team_wide and "both yours and your opponent's" not in t:
            opponent_cost = "your opponent's" in t
            if opponent_cost == (pokemon.owning_player_id == carrier.owning_player_id):
                return cost
        live_types = set(effective_pokemon_types(board, pokemon))
        if holder is pokemon and "any tera pokémon in play" in t \
                and "double-edge attack for psychic" in t:
            # The Ability title is not part of this stored rule text.  This
            # printing has one Double-Edge, whose alternate printed cost is
            # exactly one Psychic Energy.
            if any(
                _has_subtype(candidate, "Tera")
                for candidate in _pokemon_in_play_from(
                    carrier, carrier.owning_player_id)
            ):
                return {"Psychic": 1}
        if "ignore all energy in the attack cost" in t \
                and "pokémon tool cards in your discard pile" in t:
            discard = _area_from(carrier, carrier.owning_player_id, "discard")
            tools = [card for card in (discard.children if discard else [])
                     if is_pokemon_tool(card)]
            required = int((re.search(r"(\d+) or more pokémon tool", t)
                            or [None, 0])[1])
            return {} if len(tools) >= required else cost
        own = _area_from(carrier, carrier.owning_player_id, "hand")
        opponent_id = next(
            (pid for pid in board.player_ids if pid != carrier.owning_player_id), None
        )
        other = _area_from(carrier, opponent_id, "hand") if opponent_id else None
        if "same number of cards in your hand as your opponent" in t \
                and own is not None and other is not None \
                and len(own.children) == len(other.children) \
                and ("attack cost" in t or "ignore all energy" in t):
            return {}
        exact = re.search(r"if you have exactly (\d+) cards in your hand", t)
        if exact and own is not None and len(own.children) == int(exact.group(1)) \
                and "ignore all energy" in t:
            return {}
        if "ignore all energy in the attack costs" in t \
                or "ignore all energy in the costs of attacks" in t:
            allowed = True
            if "caturday attack" in t:
                allowed = _has_attack_named(pokemon, "Caturday")
            if "poliwag, poliwhirl, and poliwrath" in t:
                allowed = _name(pokemon).casefold() in {"poliwag", "poliwhirl", "poliwrath"}
            if "if you have nidoqueen in play" in t:
                allowed = _has_named_in_play(carrier, carrier.owning_player_id, "Nidoqueen")
            if "simisage, simisear, and simipour" in t:
                allowed = all(_has_named_in_play(carrier, carrier.owning_player_id, name)
                              for name in ("Simisage", "Simisear", "Simipour"))
            if "exactly 4 cards in their hand" in t:
                opponent_id = _other_player_id(board, carrier.owning_player_id)
                hand = _area_from(carrier, opponent_id, "hand") if opponent_id else None
                allowed = hand is not None and len(hand.children) == 4
            if allowed:
                return {}
        if "more prize cards remaining than your opponent" in t:
            opponent_id = _other_player_id(board, pokemon.owning_player_id)
            if opponent_id is None or _prizes_remaining(carrier, pokemon.owning_player_id) \
                    <= _prizes_remaining(carrier, opponent_id):
                return cost
        if "basic pokémon" in t and _stage(pokemon) != PokemonStage.BASIC.value:
            return cost
        if "non-fairy pokémon" in t and PokemonTypes.FAIRY.value in live_types:
            return cost
        if "psychic pokémon" in t and PokemonTypes.PSYCHIC.value not in live_types:
            return cost
        if "basic pokémon" in t and _stage(pokemon) != PokemonStage.BASIC.value:
            return cost
        if "opponent's basic pokémon" in t and _stage(pokemon) != PokemonStage.BASIC.value:
            return cost
        if "pokémon-gx in play that evolve from eevee" in t and not (
                _has_subtype(pokemon, "GX")
                and evolves_from(pokemon.archetype_id, "Eevee")):
            return cost
        if "hop's pokémon" in t and not _name(pokemon).casefold().startswith("hop's "):
            return cost
        discount = 0
        if "cost colorless less for each kofu card in your discard pile" in t:
            discard = _area_from(carrier, carrier.owning_player_id, "discard")
            discount = sum(
                1 for card in (discard.children if discard else [])
                if _name(card) == "Kofu"
            )
        if "less for each of your opponent's benched pokémon" in t:
            opponent_id = _other_player_id(board, pokemon.owning_player_id)
            discount += max(0, len(_pokemon_in_play_from(carrier, opponent_id)) - 1)
        if discount:
            colorless = "Colorless"
            # Costs received from legal_actions are keyed by client enum name.
            if colorless in cost:
                cost = dict(cost)
                cost[colorless] = max(0, cost[colorless] - discount)
                if not cost[colorless]:
                    cost.pop(colorless)
        colorless_change = 0
        compact_less = re.search(r"cost (colorless)+ less", t)
        compact_more = re.search(r"cost (colorless)+ more", t)
        if compact_less:
            colorless_change = -compact_less.group(0).count("colorless")
        elif compact_more:
            colorless_change = compact_more.group(0).count("colorless")
        elif "cost colorlesscolorless less" in t:
            colorless_change = -2
        elif "cost colorless less" in t:
            colorless_change = -1
        elif "cost colorlesscolorless more" in t:
            colorless_change = 2
        elif "cost colorless more" in t:
            colorless_change = 1
        if colorless_change:
            cost = dict(cost)
            value = max(0, cost.get("Colorless", 0) + colorless_change)
            if value:
                cost["Colorless"] = value
            else:
                cost.pop("Colorless", None)
        if "cost fighting less" in t:
            cost = dict(cost)
            value = max(0, cost.get("Fighting", 0) - 1)
            if value:
                cost["Fighting"] = value
            else:
                cost.pop("Fighting", None)
        if "cost fairy less" in t:
            cost = dict(cost)
            value = max(0, cost.get("Fairy", 0) - 1)
            if value:
                cost["Fairy"] = value
            else:
                cost.pop("Fairy", None)
        return cost

    def prevents_damage(self, calc, carrier):
        if not calc.is_attack:
            return False
        holder = carrier_pokemon(carrier)
        if "by attacks it uses" in self.text:
            return holder is calc.attacker and holder is calc.target
        if not calc.is_opposing:
            return False
        # Plasma Steel protects every Metal Pokémon on Klinklang's side,
        # rather than only Klinklang itself.
        if "your metal pokémon" in self.text and "pokémon-ex" in self.text:
            return bool(
                calc.target.owning_player_id == carrier.owning_player_id
                and PokemonTypes.METAL.value in effective_pokemon_types(calc.board, calc.target)
                and _pokemon_ex(calc.attacker)
            )
        if "your benched pokémon" in self.text and "prevent all damage" in self.text:
            return calc.target.owning_player_id == carrier.owning_player_id \
                and not _is_active(calc.target)
        if "benched pokémon (both yours and your opponent's)" in self.text:
            return not _is_active(calc.target)
        if "pokémon that don't have a rule box" in self.text:
            return bool(
                not has_rule_box(calc.target.archetype_id)
                and (_has_exact_subtype(calc.attacker, "ex")
                     or _has_exact_subtype(calc.attacker, "V"))
            )
        if holder is not calc.target:
            return False
        holder_types = set(effective_pokemon_types(calc.board, holder))
        attacker_types = set(effective_pokemon_types(calc.board, calc.attacker))
        if "fairy pokémon this card is attached to" in self.text \
                and PokemonTypes.FAIRY.value not in holder_types:
            return False
        typed = re.search(
            r"attacks from your opponent's (grass|fire|water|lightning|psychic|"
            r"fighting|darkness|metal|dragon) pokémon", self.text,
        )
        if typed:
            ptype = getattr(PokemonTypes, typed.group(1).upper()).value
            if ptype not in attacker_types:
                return False
        if "ultra beast pokémon" in self.text and not _has_subtype(calc.attacker, "Ultra Beast"):
            return False
        if "opponent's pokémon-ex" in self.text and not _pokemon_ex(calc.attacker):
            return False
        if "pokémon-gx and" in self.text \
                and not (_has_subtype(calc.attacker, "GX") or _pokemon_ex(calc.attacker)):
            return False
        if "opponent's pokémon with abilities" in self.text \
                and not _has_pokemon_ability(calc.attacker):
            return False
        return "prevent all effects of attacks, including damage" in self.text \
            or "prevent all damage done" in self.text

    def modify_resistance(self, calc, carrier):
        t = self.text
        if "no resistance" in t:
            calc.resistance_applies = False
            return
        stronger = re.search(r"resistance is now -(\d+)", t)
        if not stronger or calc.target.owning_player_id != carrier.owning_player_id:
            return
        target_types = set(effective_pokemon_types(calc.board, calc.target))
        if "metal pokémon" in t and PokemonTypes.METAL.value not in target_types:
            return
        if "fairy pokémon" in t and PokemonTypes.FAIRY.value not in target_types:
            return
        calc.resistance_reduction = int(stronger.group(1))

    def modify_weakness(self, calc, carrier):
        t = self.text
        if "apply weakness" in t and "as 4 instead" in t:
            calc.weakness_multiplier = 4
            return
        if "no weakness" not in t:
            return
        holder = carrier_pokemon(carrier)
        target_types = set(effective_pokemon_types(calc.board, calc.target))
        if "both yours and your opponent's" in t or "each pokémon in play" in t:
            applies = True
        elif "each of your pokémon" in t:
            applies = calc.target.owning_player_id == carrier.owning_player_id \
                and bool(_attached(calc.target))
        else:
            applies = holder is calc.target
        if "basic pokémon" in t and _stage(calc.target) != PokemonStage.BASIC.value:
            applies = False
        for word, ptype in (
            ("fire", PokemonTypes.FIRE), ("metal", PokemonTypes.METAL),
            ("lightning", PokemonTypes.LIGHTNING),
        ):
            if "fire pokémon and metal pokémon" in t and word in {"fire", "metal"}:
                continue
            if f"{word} pokémon" in t and ptype.value not in target_types:
                applies = False
        if "fire pokémon and metal pokémon" in t and not target_types.intersection(
                {PokemonTypes.FIRE.value, PokemonTypes.METAL.value}):
            applies = False
        if applies and "psychic energy" in t and not any(
                energy_provides_type(e, PokemonTypes.PSYCHIC.value)
                for e in _attached(calc.target)):
            applies = False
        if applies and "darkness energy" in t and not any(
                energy_provides_type(e, PokemonTypes.DARKNESS.value)
                for e in _attached(calc.target)):
            applies = False
        if applies:
            calc.weakness_applies = False

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        t = self.text
        holder = carrier_pokemon(carrier)
        stadium = "stadium" in {
            s.casefold() for s in (subtypes_for(carrier.archetype_id) or [])
        }
        team_wide = stadium or "each of your pokémon" in t \
            or "pokémon in play (both yours and your opponent's)" in t \
            or "pokémon (both yours and your opponent's)" in t \
            or "each pokémon" in t or "your pokémon in play" in t \
            or "all of your pokémon" in t or "your active pokémon" in t \
            or "your opponent's active pokémon" in t \
            or "retreat cost for" in t or "retreat cost of each" in t
        if team_wide:
            if "both yours and your opponent's" not in t:
                opponent_target = "your opponent's" in t
                if opponent_target == (
                        pokemon.owning_player_id == carrier.owning_player_id):
                    return cost
        elif holder is not pokemon:
            return cost
        types = set(effective_pokemon_types(board, pokemon))
        if "basic pokémon" in t and _stage(pokemon) != PokemonStage.BASIC.value:
            return cost
        if "basic non-fighting pokémon" in t and (
                _stage(pokemon) != PokemonStage.BASIC.value
                or PokemonTypes.FIGHTING.value in types):
            return cost
        if "basic darkness pokémon" in t and (
                _stage(pokemon) != PokemonStage.BASIC.value
                or PokemonTypes.DARKNESS.value not in types):
            return cost
        if "stage 2 pokémon" in t and _stage(pokemon) != PokemonStage.STAGE2.value:
            return cost
        if "each psyduck" in t and _name(pokemon).casefold() != "psyduck":
            return cost
        if "porygon, porygon2, and porygon-z" in t \
                and _name(pokemon).casefold() not in {"porygon", "porygon2", "porygon-z"}:
            return cost
        if "your latios" in t and _name(pokemon).casefold() != "latios":
            return cost
        if "retreat cost for latios" in t and _name(pokemon).casefold() != "latios":
            return cost
        if "your dragon pokémon" in t and PokemonTypes.DRAGON.value not in types:
            return cost
        if "pokémon in play have no retreat cost, except pokémon-gx and pokémon-ex" in t \
                and (_has_subtype(pokemon, "GX") or _pokemon_ex(pokemon)):
            return cost
        if "that has any water energy attached" in t \
                and not _has_energy_type(pokemon, PokemonTypes.WATER):
            return cost
        if "that have psychic energy attached" in t \
                and not _has_energy_type(pokemon, PokemonTypes.PSYCHIC):
            return cost
        if "that have metal energy attached" in t \
                and not _has_energy_type(pokemon, PokemonTypes.METAL):
            return cost
        if "that has any lightning energy attached" in t \
                and not _has_energy_type(pokemon, PokemonTypes.LIGHTNING):
            return cost
        if "that has any fairy energy attached" in t \
                and not _has_energy_type(pokemon, PokemonTypes.FAIRY):
            return cost
        if "except for team aqua pokémon" in t and _has_subtype(pokemon, "Team Aqua"):
            return cost
        if "no retreat cost" in t or "retreat cost is 0" in t \
                or "retreat cost for that pokémon is 0" in t:
            if "any darkness energy" in t and not any(
                    energy_provides_type(e, PokemonTypes.DARKNESS.value)
                    for e in _attached(pokemon)):
                return cost
            if "any grass energy" in t and not any(
                    energy_provides_type(e, PokemonTypes.GRASS.value)
                    for e in _attached(pokemon)):
                return cost
            if "remaining hp is 30 or less" in t \
                    and pokemon.get_attribute(AttrID.HP, 0) > 30:
                return cost
            if "has any water energy attached" in t \
                    and not _has_energy_type(pokemon, PokemonTypes.WATER):
                return cost
            if "has any fire energy attached" in t \
                    and not _has_energy_type(pokemon, PokemonTypes.FIRE):
                return cost
            if "has any lightning energy attached" in t \
                    and not _has_energy_type(pokemon, PokemonTypes.LIGHTNING):
                return cost
            if "has any psychic energy attached" in t \
                    and not _has_energy_type(pokemon, PokemonTypes.PSYCHIC):
                return cost
            if "has any fighting energy attached" in t \
                    and not _has_energy_type(pokemon, PokemonTypes.FIGHTING):
                return cost
            if "has any energy attached" in t and not _attached(pokemon):
                return cost
            if "has no energy attached" in t and _attached(pokemon):
                return cost
            if "2 or fewer energy attached" in t \
                    and len([e for e in _attached(pokemon) if is_energy_card(e)]) > 2:
                return cost
            if "any stadium card in play" in t:
                area = next((node for node in _walk(_tree_root(carrier))
                             if node.get_attribute(AttrID.NAME) == "activeStadium"), None)
                if area is None or not area.children:
                    return cost
            if "opponent has any pokémon-gx or pokémon-ex in play" in t:
                opponent_id = _other_player_id(board, pokemon.owning_player_id)
                if not any(_has_subtype(p, "GX") or _pokemon_ex(p)
                           for p in _pokemon_in_play_from(carrier, opponent_id)):
                    return cost
            if "if you have latias in play" in t \
                    and not _has_named_in_play(carrier, pokemon.owning_player_id, "Latias"):
                return cost
            if "if you have any fairy pokémon in play" in t and not any(
                    PokemonTypes.FAIRY.value in effective_pokemon_types(board, p)
                    for p in _pokemon_in_play_from(carrier, pokemon.owning_player_id)):
                return cost
            if "during your first turn" in t and getattr(
                    board, "turn_state", None) is not None \
                    and board.turn_state.turn_number != 1:
                return cost
            return 0
        if "retreat cost of each of your team plasma pokémon" in t \
                and pokemon.owning_player_id == carrier.owning_player_id \
                and _team_plasma(pokemon):
            discount = max(1, t.count("colorless"))
            return max(0, cost - discount)
        if "retreat cost of each of your opponent's pokémon" in t \
                and pokemon.owning_player_id != carrier.owning_player_id:
            surcharge = max(1, t.count("colorless"))
            return cost + surcharge
        if "retreat cost of the pokémon this card is attached to" in t \
                and holder is pokemon and "less" in t:
            discount = max(1, t.count("colorless"))
            return max(0, cost - discount)
        if "retreat cost" in t and "less" in t:
            if "psychic or darkness energy attached" in t and not any(
                    energy_provides_type(e, PokemonTypes.PSYCHIC.value)
                    or energy_provides_type(e, PokemonTypes.DARKNESS.value)
                    for e in _attached(pokemon)):
                return cost
            discount = max(1, t.count("colorless"))
            named_bench = re.search(r"less for each (beldum|magnemite) on your bench", t)
            if named_bench:
                bench = _area_from(carrier, pokemon.owning_player_id, "bench")
                discount = sum(
                    _name(card).casefold() == named_bench.group(1)
                    for card in (bench.children if bench else [])
                )
            typed_attached = re.search(
                r"less for each (fire|water|lightning) energy attached", t)
            if typed_attached:
                ptype = getattr(PokemonTypes, typed_attached.group(1).upper())
                discount = sum(energy_provides_type(e, ptype.value)
                               for e in _attached(pokemon))
            return max(0, cost - discount)
        if "retreat cost" in t and "more" in t:
            return cost + max(1, t.count("colorless"))
        return cost

    def max_hp_bonus(self, pokemon, carrier):
        t = self.text
        owner = carrier.owning_player_id
        if "all of your pokémon in play get +" in t:
            match = re.search(r"get \+(\d+) hp", t)
            return int(match.group(1)) if match \
                and pokemon.owning_player_id == owner else 0
        if "each of your grass pokémon in play gets +" in t:
            match = re.search(r"gets \+(\d+) hp", t)
            return int(match.group(1)) if match \
                and pokemon.owning_player_id == owner \
                and PokemonTypes.GRASS.value in effective_pokemon_types(
                    _board_for(pokemon), pokemon) else 0
        if "your wishiwashi-gx in play get +" in t:
            match = re.search(r"get \+(\d+) hp", t)
            return int(match.group(1)) if match \
                and pokemon.owning_player_id == owner \
                and _name(pokemon).casefold() == "wishiwashi-gx" else 0
        if "your pokémon-gx in play that evolve from eevee get +" in t:
            match = re.search(r"get \+(\d+) hp", t)
            return int(match.group(1)) if match \
                and pokemon.owning_player_id == owner \
                and _has_subtype(pokemon, "GX") \
                and evolves_from(pokemon.archetype_id, "Eevee") else 0
        if "mega floette ex in play" in t:
            return 150 if _name(pokemon).casefold() == "mega floette ex" else 0
        if "pokémon legend in play" in t:
            return 30 if _has_subtype(pokemon, "LEGEND") else 0
        if "stage 1 and stage 2 pokémon in play" in t:
            return 30 if _stage(pokemon) in (
                PokemonStage.STAGE1.value, PokemonStage.STAGE2.value) else 0
        if "each of your team plasma pokémon" in self.text:
            match = re.search(r"gets \+(\d+) hp", self.text)
            if match and pokemon.owning_player_id == carrier.owning_player_id \
                    and _team_plasma(pokemon):
                return int(match.group(1))
            return 0
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        if "gets -100 hp" in t and (
                _has_subtype(pokemon, "GX") or _pokemon_ex(pokemon)):
            return -100
        match = re.search(r"gets \+(\d+) hp for each (\w+) energy", self.text)
        if match:
            ptype = getattr(PokemonTypes, match.group(2).upper(), None)
            return int(match.group(1)) * sum(
                1 for e in _attached(pokemon)
                if ptype is not None and energy_provides_type(e, ptype.value)
            )
        match = re.search(r"gets \+(\d+) hp for each prize card your opponent has taken", t)
        if match:
            board = _board_for(pokemon)
            opponent_id = _other_player_id(board, pokemon.owning_player_id)
            dealt = getattr(board, "prizes_dealt", {}).get(opponent_id, 6)
            return int(match.group(1)) * max(
                0, int(dealt) - _prizes_remaining(carrier, opponent_id)
            )
        match = re.search(r"gets \+(\d+) hp for each of your benched pokémon", t)
        if match:
            bench = _area_from(carrier, pokemon.owning_player_id, "bench")
            return int(match.group(1)) * len(bench.children if bench else []) \
                if _is_active(pokemon) else 0
        match = re.search(r"gets \+(\d+) hp for each nidoqueen you have in play", t)
        if match:
            return int(match.group(1)) * sum(
                _name(entry).casefold() == "nidoqueen"
                for entry in _pokemon_in_play_from(carrier, pokemon.owning_player_id)
            )
        match = re.search(r"gets \+(\d+) hp", self.text)
        if not match:
            return 0
        if "doesn't have a rule box" in t and has_rule_box(pokemon.archetype_id):
            return 0
        if "pokémon-gx or pokémon-ex" in t \
                and not (_has_subtype(pokemon, "GX") or _pokemon_ex(pokemon)):
            return 0
        if "basic pokémon this card is attached to" in self.text and \
                pokemon.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
            return 0
        if "stage 1 pokémon this card is attached to" in t \
                and _stage(pokemon) != PokemonStage.STAGE1.value:
            return 0
        if "any special energy attached" in t and not any(
                is_special_energy(e) for e in _attached(pokemon)):
            return 0
        if "any darkness energy attached" in t \
                and not _has_energy_type(pokemon, PokemonTypes.DARKNESS):
            return 0
        metal_count = re.search(r"has (\d+) or more metal energy attached", t)
        if metal_count and sum(
                energy_provides_type(e, PokemonTypes.METAL.value)
                for e in _attached(pokemon)) < int(metal_count.group(1)):
            return 0
        if "retreat cost of exactly 4" in t \
                and effective_retreat_cost(_board_for(pokemon), pokemon) != 4:
            return 0
        if "ancient pokémon" in t and not _has_subtype(pokemon, "Ancient"):
            return 0
        if "cynthia's pokémon" in t \
                and not _name(pokemon).casefold().startswith("cynthia's "):
            return 0
        return int(match.group(1))

    def blocks_attack_effects(self, target, carrier):
        holder = carrier_pokemon(carrier)
        if "benched pokémon (both yours and your opponent's)" in self.text:
            return not _is_active(target)
        if "each of your pokémon that has any energy attached" in self.text:
            if target.owning_player_id != carrier.owning_player_id or not _attached(target):
                return False
        elif holder is not target:
            return False
        if "prevent all effects of your opponent's attacks, except damage" in self.text:
            return True
        if "prevent all effects of attacks, including damage" in self.text:
            # Damage is handled by prevents_damage; this hook shields riders.
            return True
        return False

    def blocks_retreat(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is pokemon and "this card can't retreat" in self.text:
            return True
        return "opponent's active pokémon can't retreat" in self.text \
            and _is_active(carrier) \
            and _is_active(pokemon) \
            and pokemon.owning_player_id != carrier.owning_player_id

    def retreats_despite_conditions(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon \
            and "can retreat even if it's asleep or paralyzed" in self.text

    def blocks_special_conditions(self, target, condition, carrier):
        t = self.text
        holder = carrier_pokemon(carrier)
        applies = holder is target
        if "each metal pokémon (both yours and your opponent's)" in t:
            applies = PokemonTypes.METAL.value in effective_pokemon_types(
                _board_for(target), target)
        if "this ↓ player's pokémon" in t:
            applies = target.owning_player_id == carrier.owning_player_id
        if not applies:
            return False
        if "can't be affected by any special conditions" in t:
            return True
        condition_name = getattr(condition, "name", str(condition)).casefold()
        if "can't be affected by those special conditions" in t \
                and "asleep, confused, or paralyzed" in t:
            return condition_name in {"asleep", "confused", "paralyzed"}
        if "can't be confused or poisoned" in t:
            return condition_name in {"confused", "poisoned"}
        if "can't be asleep or paralyzed" in t:
            return condition_name in {"asleep", "paralyzed"}
        if "can't be confused" in t:
            return condition_name == "confused"
        return False

    def preserves_special_conditions_on_evolution(self, pokemon, carrier):
        return "special conditions are not removed when pokémon" in self.text \
            and "evolve or devolve" in self.text

    def blocks_attacks(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if "40 hp or less remaining" in self.text:
            return pokemon.owning_player_id != carrier.owning_player_id \
                and pokemon.get_attribute(AttrID.HP, 0) <= 40
        if "opponent's basic pokémon can't attack" in self.text:
            return holder is not None and _is_active(holder) \
                and pokemon.owning_player_id != holder.owning_player_id \
                and _stage(pokemon) == PokemonStage.BASIC.value
        if holder is not pokemon:
            return False
        board = _board_for(pokemon)
        opponent_id = _other_player_id(board, pokemon.owning_player_id)
        if "opponent has no pokémon ex or pokémon v in play" in self.text:
            return not any(
                _has_exact_subtype(entry, "ex") or _has_exact_subtype(entry, "V")
                for entry in _pokemon_in_play_from(carrier, opponent_id)
            )
        own_count = len(_pokemon_in_play_from(carrier, pokemon.owning_player_id))
        if "if you have 4 or fewer pokémon in play" in self.text:
            return own_count <= 4
        if "can't attack unless you have 4 or more team rocket's pokémon" in self.text:
            return sum(
                _has_subtype(entry, "Team Rocket")
                for entry in _pokemon_in_play_from(carrier, pokemon.owning_player_id)
            ) < 4
        team_saver = re.search(
            r"if there are 4 or fewer team (aqua|magma) pokémon in play", self.text)
        if team_saver:
            label = f"Team {team_saver.group(1).title()}"
            total = sum(
                _has_subtype(entry, label)
                for pid in getattr(board, "player_ids", [])
                for entry in _pokemon_in_play_from(carrier, pid)
            )
            return total <= 4
        if "unless regirock, regice, and registeel are on your bench" in self.text:
            bench = _area_from(carrier, pokemon.owning_player_id, "bench")
            names = {_name(entry).casefold()
                     for entry in (bench.children if bench else [])}
            return not {"regirock", "regice", "registeel"}.issubset(names)
        if "prize cards left" in self.text:
            prizes = _area_from(pokemon, pokemon.owning_player_id, "prizePile")
            return bool(prizes) and len(prizes.children) in (2, 4, 6)
        if "opponent's active pokémon is a basic pokémon" in self.text:
            active = next((node for node in _walk(_tree_root(pokemon))
                           if isinstance(node, PokemonEntity)
                           and node.owning_player_id != pokemon.owning_player_id
                           and _is_active(node)), None)
            return active is not None and active.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        return False

    def blocks_trainer_play(self, card, player_id, carrier):
        t = self.text
        card_subtypes = {
            str(value).casefold()
            for value in (subtypes_for(card.archetype_id) or [])
        }
        if "each player can't play any trainer cards" in t:
            return is_trainer_card(card)
        if "each player can't play any item cards" in t:
            return is_item_card(card)
        if "each player can't play any stadium cards" in t:
            return "stadium" in card_subtypes
        if "each player can't attach any pokémon tool cards" in t:
            return is_pokemon_tool(card)
        if player_id == carrier.owning_player_id:
            return False
        if "as long as you have fewer pokémon in play than your opponent" in t:
            own = len(_pokemon_in_play_from(carrier, carrier.owning_player_id))
            theirs = len(_pokemon_in_play_from(carrier, player_id))
            if own >= theirs:
                return False
        if "active pokémon" in t and not _is_active(carrier):
            return False
        if "can't play any item cards" in t:
            return is_item_card(card)
        if "can't play any supporter cards" in t:
            return is_supporter_card(card)
        if "can't play any stadium cards" in t:
            return "stadium" in card_subtypes
        if "can't play any pokémon tool" in t:
            return is_pokemon_tool(card)
        if "can't play any ace spec cards" in t:
            return "ACE SPEC" in (subtypes_for(card.archetype_id) or [])
        return False

    def blocks_pokemon_play(self, card, player_id, carrier):
        t = self.text
        holder = carrier_pokemon(carrier)
        if player_id == carrier.owning_player_id or holder is None:
            return False
        if "active spot" in t and not _is_active(holder):
            return False
        if "can't play any pokémon that has an ability from their hand" not in t:
            return False
        if "except for team rocket's pokémon" in t \
                and _has_subtype(card, "Team Rocket"):
            return False
        return _has_pokemon_ability(card)

    def blocks_trainer_targeting(self, target, carrier):
        return target is carrier and (
            "prevent all effects of that card done to this stadium card" in self.text
            or "can't be put into your hand or deck from the discard pile" in self.text
        )

    def supporter_limit(self, player_id, carrier):
        if "may play 2 supporter cards" in self.text \
                and player_id == carrier.owning_player_id:
            return 2
        return 1

    def blocks_trainer_effects(self, affected_player_id, trainer_card,
                               trainer_type, carrier, affected_entity=None,
                               board=None):
        holder = carrier_pokemon(carrier)
        if "prevent all effects of any stadium done to your pokémon in play" \
                in self.text:
            if trainer_type != TrainerType.STADIUM.value \
                    or affected_player_id != carrier.owning_player_id \
                    or affected_entity is None:
                return False
            affected = carrier_pokemon(affected_entity)
            return affected is not None \
                and affected.owning_player_id == carrier.owning_player_id \
                and _has_named_in_play(
                    carrier, carrier.owning_player_id, "Solrock")
        if "excluding pokémon tools and stadium cards" in self.text \
                and affected_entity is holder \
                and affected_player_id == carrier.owning_player_id \
                and trainer_card.owning_player_id != carrier.owning_player_id \
                and trainer_type in (
                    TrainerType.ITEM.value, TrainerType.SUPPORTER.value,
                ):
            return True
        return "whenever your opponent plays an item card" in self.text \
            and _is_active(carrier) \
            and affected_player_id == carrier.owning_player_id \
            and trainer_card.owning_player_id != carrier.owning_player_id \
            and trainer_type == TrainerType.ITEM.value

    def blocks_ability_effects(self, target, carrier):
        return carrier_pokemon(carrier) is target \
            and "prevent all effects of your opponent's pokémon's abilities" \
                in self.text

    def heal_multiplier(self, target, carrier):
        return 2 if carrier_pokemon(carrier) is target \
            and "when this pokémon is healed, double the amount healed" \
                in self.text else 1

    def extra_manual_energy_attachments(self, pokemon, carrier):
        return 1 if carrier_pokemon(carrier) is pokemon \
            and "you may attach 2 energy cards" in self.text else 0

    def tool_capacity(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is pokemon and "may have up to 4 pokémon tools" in self.text:
            return 4
        if "each of your pokémon that has \"rotom\" in its name" in self.text:
            return 2 if pokemon.owning_player_id == carrier.owning_player_id \
                and "rotom" in _name(pokemon).casefold() else 1
        return 2 if holder is pokemon \
            and "may have up to 2 pokémon tool cards" in self.text else 1

    def blocks_energy_attachment(self, attaching_player_id, energy, target, carrier):
        if attaching_player_id == carrier.owning_player_id \
                or not is_special_energy(energy):
            return False
        t = self.text
        holder = carrier_pokemon(carrier)
        if "hand block" in t and "stadium card in play" in t:
            stadium = _area_from(carrier, None, "activeStadium")
            return bool(stadium and stadium.children)
        return holder is not None and _is_active(holder) \
            and "can't play any pokémon tool, special energy, or stadium cards" in t

    def bench_capacity(self, player_id, carrier):
        t = self.text
        holder = carrier_pokemon(carrier)
        if player_id == carrier.owning_player_id:
            return None
        if "number of benched pokémon your opponent can have is now 4" in t:
            return 4
        if "opponent can't have more than 3 benched pokémon" in t \
                and holder is not None and _is_active(holder):
            return 3
        return None

    def attacks_on_first_turn(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon \
            and "can use attacks during your first turn" in self.text

    def ignores_defender_effects(self, pokemon, carrier):
        t = self.text
        holder = carrier_pokemon(carrier)
        if "attacks used by this pokémon isn't affected by any effects" in t \
                or "this pokémon's attacks isn't affected by any effects" in t:
            return holder is pokemon
        if "damage from the attacks of your lightning pokémon isn't affected" in t:
            return pokemon.owning_player_id == carrier.owning_player_id \
                and PokemonTypes.LIGHTNING.value in effective_pokemon_types(
                    _board_for(pokemon), pokemon)
        return False

    def attack_keeps_turn(self, attacker, ability, ctx, carrier):
        if carrier_pokemon(carrier) is not attacker \
                or "may attack twice a turn" not in self.text:
            return False
        uses = [entry for entry in ctx.session.turn_state.attacks_used
                if entry[0] == attacker.entity_id]
        return len(uses) == 1

    def may_evolve_early(self, pokemon, carrier):
        return "you may play this card from your hand to evolve a pokémon" \
            in self.text

    def heal_on_evolve(self, evolved, pre_evolution, player_id, carrier):
        return 10 ** 6 if carrier_pokemon(carrier) is evolved \
            and "when 1 of your pokémon becomes this pokémon, heal all damage" \
                in self.text else 0

    def offers_attack_coin_reroll(self, player_id, carrier, attacker=None):
        return "ignore all effects of those coin flips" in self.text \
            and player_id == carrier.owning_player_id

    def coin_result_override(self, player_id, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not _is_active(holder):
            return None
        board = _board_for(holder)
        if player_id == holder.owning_player_id \
                or getattr(board, "turn_state", None) is None \
                or board.turn_state.active_player_id != player_id:
            return None
        if "whenever your opponent flips a coin" in self.text \
                and "treat it as tails" in self.text:
            return False
        return None

    def prevents_trainer_end_turn(self, card, player_id, carrier):
        holder = carrier_pokemon(carrier)
        return holder is not None and _is_active(holder) \
            and holder.owning_player_id == player_id \
            and _name(card).casefold() == "steven's resolve" \
            and "turn does not end when you play steven's resolve" in self.text

    async def on_energy_attached(self, ctx, carrier):
        t = self.text
        receiver = getattr(ctx, "energy_receiver", None)
        energy = getattr(ctx, "attached_energy", None)
        if receiver is None:
            return
        if "basic non-water pokémon" in t and "put 2 damage counters" in t:
            types = set(effective_pokemon_types(ctx.board, receiver))
            if _stage(receiver) == PokemonStage.BASIC.value \
                    and PokemonTypes.WATER.value not in types:
                await ctx.deal_damage(
                    20, target=receiver, apply_modifiers=False,
                    as_counters=True, is_attack=False,
                )
            return
        holder = carrier_pokemon(carrier)
        if holder is receiver and "whenever you attach an energy from your hand to it" in t \
                and "it is now asleep" in t:
            await ctx.apply_special_condition(holder, SpecialConditions.ASLEEP)
        if holder is receiver and "when you attach an energy from your hand to this pokémon" in t \
                and "opponent's active pokémon is now asleep" in t:
            active = ctx.opponent_active()
            if active is not None and await ctx.ask_yes_no(
                    "Use Hyper Hypnosis?"):
                await ctx.apply_special_condition(active, SpecialConditions.ASLEEP)
        if holder is receiver and "heal 20 damage" in t:
            required = re.search(
                r"attach a (water|grass|fire|lightning|psychic|fighting|darkness|metal) energy",
                t,
            )
            if required is None or (
                    energy is not None and energy_provides_type(
                        energy, getattr(PokemonTypes, required.group(1).upper()).value)):
                await ctx.heal(20, holder)
        if holder is not None and _is_active(holder) \
                and receiver.owning_player_id == holder.owning_player_id \
                and ("heal 90 damage from that pokémon" in t):
            await ctx.heal(90, receiver)
        if holder is not receiver \
                or getattr(ctx, "attaching_player_id", None) != holder.owning_player_id:
            return
        if "remove all special conditions from it" in t:
            await ctx.cure_all_conditions(holder)
        if "remove a damage counter from onix" in t \
                and _name(holder).casefold() == "onix":
            await ctx.heal(10, holder)
        if "remove 2 damage counters from golduck" in t \
                and _name(holder).casefold() == "golduck" \
                and energy is not None \
                and energy_provides_type(energy, PokemonTypes.WATER.value):
            await ctx.heal(20, holder)
        if "whenever you attach an energy card from your hand to shuckle" in t \
                and _name(holder).casefold() == "shuckle":
            await ctx.draw_cards(1)
        if "energy signal" in t:
            active = ctx.opponent_active()
            if active is not None and not (holder.get_attribute(
                    AttrID.SPECIAL_CONDITIONS) or []) and energy is not None:
                condition = None
                if energy_provides_type(energy, PokemonTypes.GRASS.value):
                    condition = SpecialConditions.CONFUSED
                elif energy_provides_type(energy, PokemonTypes.PSYCHIC.value):
                    condition = SpecialConditions.POISONED
                if condition is not None and await ctx.ask_yes_no(
                        "Use Energy Signal?"):
                    await ctx.apply_special_condition(active, condition)
        if "water down" in t and energy is not None \
                and energy_provides_type(energy, PokemonTypes.WATER.value) \
                and len(ctx.my_bench()) < effective_bench_capacity(
                    ctx.board, holder.owning_player_id):
            cards = await ctx.search_deck(
                lambda card: is_basic_pokemon(card)
                and _name(card).casefold() == "goomy",
                1, minimum=0, prompt="Choose Goomy to put onto your Bench",
            )
            if cards:
                await ctx.bench_pokemon(cards[0])
            await ctx.shuffle_deck()
        if "energy evolution" in t and energy is not None \
                and is_basic_energy(energy):
            energy_types = {
                option for choice in energy_provided_options(ctx.board, energy)
                for option in choice
            }
            logic = holder.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
            cards = await ctx.search_deck(
                lambda card: is_evolution_pokemon(card)
                and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic
                and bool(energy_types.intersection(
                    card.get_attribute(AttrID.POKEMON_TYPES) or [])),
                1, minimum=0,
                prompt="Choose a matching Evolution Pokémon",
            )
            if cards:
                await ctx.evolve_pokemon(holder, cards[0])
            await ctx.shuffle_deck()

    async def on_tool_attached(self, ctx, carrier):
        holder = carrier_pokemon(carrier)
        receiver = getattr(ctx, "tool_receiver", None)
        tool = getattr(ctx, "attached_tool", None)
        if holder is not receiver or tool is None:
            return
        if "fairy charm" not in _name(tool).casefold() \
                or "leave your opponent's active pokémon confused" not in self.text:
            return
        active = ctx.opponent_active()
        if active is not None and await ctx.ask_yes_no("Use Charmed Charm?"):
            await ctx.apply_special_condition(active, SpecialConditions.CONFUSED)

    async def on_move_to_active(self, ctx, carrier):
        t = self.text
        new_active = getattr(ctx, "new_active", None)
        previous = getattr(ctx, "previous_active", None)
        switching_player = getattr(ctx, "switching_player_id", None)
        if new_active is None or previous is None or switching_player is None:
            return

        holder = carrier_pokemon(carrier)
        opponent_switch = switching_player != carrier.owning_player_id
        during_switchers_turn = \
            ctx.session.turn_state.active_player_id == switching_player

        # Swirling Prose, Lava Zone and Holes observe the opponent moving its
        # Active to the Bench during that opponent's turn.
        if holder is not None and _is_active(holder) and opponent_switch \
                and during_switchers_turn:
            if "their new active pokémon is now confused" in t:
                await ctx.apply_special_condition(
                    new_active, SpecialConditions.CONFUSED)
            if "their new active pokémon is now burned" in t:
                await ctx.apply_special_condition(
                    new_active, SpecialConditions.BURNED)
            if "place 2 damage counters on that pokémon" in t \
                    and "moves to the bench" in t:
                await ctx.deal_damage(
                    20, target=previous, apply_modifiers=False,
                    as_counters=True, is_attack=False,
                )

        # Toxic Spikes observes a retreat specifically, not an attack or
        # Trainer switch.
        if holder is not None and opponent_switch \
                and getattr(ctx, "switch_reason", "") == "retreat" \
                and "active pokémon retreats" in t \
                and "new active pokémon is poisoned" in t:
            await ctx.apply_special_condition(
                new_active, SpecialConditions.POISONED)

        # Dust Island transfers Poison only when a Trainer effect switches the
        # Active. The common switch primitive clears the old Active first, so
        # its condition snapshot travels on the event context.
        previous_conditions = set(
            getattr(ctx, "previous_active_conditions", []) or [])
        poisoned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
        if getattr(ctx, "switch_reason", "") == "trainer" \
                and "switches their poisoned active pokémon" in t \
                and poisoned in previous_conditions:
            await ctx.apply_special_condition(
                new_active, SpecialConditions.POISONED)

    async def on_pokemon_benched(self, ctx, carrier):
        pokemon = getattr(ctx, "benched_pokemon", None)
        if pokemon is None:
            return

        if "basic pokémon (except for team magma pokémon)" in self.text \
                and _stage(pokemon) == PokemonStage.BASIC.value \
                and not _has_subtype(pokemon, "Team Magma"):
            await ctx.deal_damage(
                20, target=pokemon, apply_modifiers=False,
                as_counters=True, is_attack=False,
            )

        # Eye of Disaster watches the opponent bench a Basic while Absol is
        # Active. The common event is only emitted for from-hand bench plays.
        holder = carrier_pokemon(carrier)
        if "eye of disaster" in self.text and holder is not None \
                and _is_active(holder) \
                and pokemon.owning_player_id != holder.owning_player_id \
                and _stage(pokemon) == PokemonStage.BASIC.value:
            await ctx.deal_damage(
                20, target=pokemon, apply_modifiers=False,
                as_counters=True, is_attack=False,
            )

        # Bursting Spores is optional and watches any Pokemon with an attack
        # literally named Spore played by its owner.
        if "bursting spores" in self.text \
                and pokemon.owning_player_id == carrier.owning_player_id:
            definition = def_for(pokemon.archetype_id)
            has_spore = any(
                isinstance(ability, Attack)
                and getattr(ability, "title", "").casefold() == "spore"
                for ability in (getattr(definition, "abilities", None) or [])
            )
            active = ctx.opponent_active()
            if has_spore and active is not None \
                    and await ctx.ask_yes_no("Use Bursting Spores?"):
                await ctx.apply_special_condition(
                    active, SpecialConditions.ASLEEP)
                await ctx.apply_special_condition(
                    active, SpecialConditions.POISONED)

    async def on_pokemon_evolved(self, ctx, carrier):
        pokemon = getattr(ctx, "evolved_pokemon", None)
        if pokemon is None:
            return
        if "whenever any player plays a pokémon from their hand to evolve" in self.text:
            await ctx.deal_damage(
                30, target=pokemon, apply_modifiers=False,
                as_counters=True, is_attack=False,
            )

        # Darkest Impulse watches only the opponent and explicitly does not
        # stack across multiple Ampharos.
        if "darkest impulse" in self.text \
                and pokemon.owning_player_id != carrier.owning_player_id:
            state = getattr(ctx, "passive_event_state", {})
            key = ("darkest-impulse", pokemon.entity_id)
            if not state.get(key):
                state[key] = True
                await ctx.deal_damage(
                    40, target=pokemon, apply_modifiers=False,
                    as_counters=True, is_attack=False,
                )

        # Alakazam-EX remains directly under the Mega Evolution after the
        # shared evolution primitive finishes, so Kinesis can identify the
        # exact evolution pair without relying on localized card names.
        if "kinesis" in self.text and carrier in pokemon.children \
                and _name(pokemon).casefold().replace(" ", "") \
                    in {"m alakazam-ex".replace(" ", ""), "mega alakazam ex".replace(" ", "")}:
            active = ctx.opponent_active()
            bench = ctx.opponent_bench()
            if active is not None and await ctx.ask_yes_no("Use Kinesis?"):
                await ctx.deal_damage(
                    20, target=active, apply_modifiers=False,
                    as_counters=True, is_attack=False,
                )
                if bench:
                    target = bench[0] if len(bench) == 1 else \
                        await ctx.choose_pokemon(
                            bench, "Choose a Benched Pokémon for Kinesis")
                    if target is not None:
                        await ctx.deal_damage(
                            30, target=target, apply_modifiers=False,
                            as_counters=True, is_attack=False,
                        )

    async def on_end_turn(self, ctx, carrier):
        t = self.text
        holder = carrier_pokemon(carrier)
        acting = ctx.player_id
        if holder is not None and "at the end of your opponent's turn" in t \
                and "shuffle this pokémon and all cards attached to it into your deck" in t \
                and acting != holder.owning_player_id \
                and _damage_counters_on(holder) > 0:
            heads = (await ctx.flip_coins(
                1, "Scatter", source=carrier,
                player_id=holder.owning_player_id,
            ))[0]
            if not heads:
                was_active = _is_active(holder)
                owner_id = holder.owning_player_id
                await ctx.shuffle_into_deck(full_stack(holder), player_id=owner_id)
                if was_active:
                    await ctx.flush_choreography()
                    if not await ctx.session._promote_new_active(owner_id):
                        await ctx.session.end_game(
                            ctx.session._opponent_id(owner_id),
                            f"{ctx.session.players[owner_id].screen_name} has no Pokémon left",
                        )
        if holder is not None and "at the end of your opponent's turn, heal 20 damage" in t \
                and acting != holder.owning_player_id \
                and _stage(holder) == PokemonStage.BASIC.value:
            await ctx.heal(20, holder)
        if holder is not None and "at the end of your turn" in t \
                and "heal 20 damage" in t \
                and acting == holder.owning_player_id and _is_active(holder):
            await ctx.heal(20, holder)
        should_discard = False
        if holder is not None and "discard it at the end of your opponent's turn" in t:
            should_discard = acting != holder.owning_player_id
        elif holder is not None and "discard it at the end of your turn" in t:
            should_discard = acting == holder.owning_player_id
        elif holder is not None and "discard it at the end of the turn" in t:
            should_discard = True
        if should_discard and getattr(carrier, "parent", None) is not None:
            await ctx.discard_cards([carrier])

    async def before_retreat(self, ctx, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if "slimy sliding" not in self.text \
                or holder is None \
                or holder.owning_player_id == pokemon.owning_player_id:
            return True
        return (await ctx.flip_coins(
            1, "Slimy Sliding", source=carrier,
        ))[0]

    def blocks_abilities(self, pokemon, carrier):
        if "except for garbotoxin" not in self.text or not _has_tool(carrier):
            if "pokémon-gx and pokémon-ex in play" in self.text:
                return _has_subtype(pokemon, "GX") or _pokemon_ex(pokemon)
            return False
        return not _has_named_ability(pokemon, "Garbotoxin")

    def blocks_ability(self, pokemon, ability, carrier):
        if "lose any ability that requires the pokémon using it to knock out itself" \
                not in self.text:
            return False
        ability_text = _norm(getattr(ability, "game_text", ""))
        return "knock out this pokémon" in ability_text

    def blocks_out_of_play_abilities(self, card, carrier):
        if "except for garbotoxin" not in self.text or not _has_tool(carrier):
            return False
        return is_pokemon_card(card) and not _has_named_ability(card, "Garbotoxin")

    def blocks_evolution(self, player_id, target, carrier):
        return "can't play any pokémon from" in self.text \
            and "to evolve" in self.text

    def prevents_healing(self, target, carrier):
        t = self.text
        if "damage counters can't be removed from any pokémon" in t:
            if "if you have lunatone in play" in t and not _has_named_in_play(
                    carrier, carrier.owning_player_id, "Lunatone"):
                return False
            return True
        if "pokémon (both yours and your opponent's) can't be healed" in t:
            if "if you have solrock in play" in t and not _has_named_in_play(
                    carrier, carrier.owning_player_id, "Solrock"):
                return False
            return True
        return "damage can't be healed from any pokémon" in t

    def blocks_damage_counters(self, target, carrier):
        return carrier_pokemon(carrier) is target \
            and "attacks and abilities can't put damage counters on it" in self.text

    def blocks_discard(self, card, carrier):
        holder = carrier_pokemon(carrier)
        if "cards in your deck can't be discarded" not in self.text \
                or holder is None or not _is_active(holder):
            return False
        return card.owning_player_id == holder.owning_player_id \
            and getattr(getattr(card, "parent", None), "get_attribute", lambda *_: None)(
                AttrID.NAME) == "deck"

    def blocks_move_to_hand(self, card, ctx, carrier):
        t = self.text
        protected_player = _other_player_id(
            _board_for(carrier), carrier.owning_player_id)
        if protected_player is None or card.owning_player_id != protected_player:
            return False
        card_holder = carrier_pokemon(card)
        if "opponent's pokémon in play and all attached cards can't be put" in t:
            return card_holder is not None and _is_active(card_holder) \
                or card_holder is not None and card_holder.parent is not None \
                and card_holder.parent.get_attribute(AttrID.NAME) == "bench"
        if "opponent's pokémon that have any damage counters" in t:
            return card_holder is not None and _damage_counters_on(card_holder) > 0
        if "cards in your opponent's discard pile can't be put into their hand" in t:
            in_discard = getattr(getattr(card, "parent", None), "get_attribute", lambda *_: None)(
                AttrID.NAME) == "discard"
            return in_discard and ctx.player_id == protected_player \
                and (ctx.is_ability_effect() or ctx.is_trainer_effect)
        return False

    def discard_destination(self, card, carrier):
        if card is carrier and "discarded from play" in self.text \
                and "put it into your hand instead" in self.text:
            return "hand"
        return None

    def suppresses_tool(self, tool, carrier):
        t = self.text
        if "have no effect" not in t and "has no effect" not in t:
            return False
        holder = carrier_pokemon(carrier)
        tool_holder = carrier_pokemon(tool)
        if "attached to your opponent's pokémon" in t:
            return tool_holder is not None \
                and tool_holder.owning_player_id != carrier.owning_player_id
        if "pokémon tool card" not in t or "in play" not in t:
            return False
        return holder is None or "active pokémon" not in t or _is_active(holder)

    def retreat_cost_destination(self, pokemon, energy, carrier):
        return "hand" if carrier_pokemon(carrier) is pokemon \
            and "discards energy for its retreat cost" in self.text \
            and "into your hand instead" in self.text else None

    def blocks_burn_recovery(self, pokemon, carrier):
        return "special condition burned" in self.text \
            and "isn't removed even if the result is heads" in self.text

    def may_evolve_same_turn(self, pokemon, carrier, evolution_card):
        return "grass pokémon can evolve during" in self.text \
            and PokemonTypes.GRASS.value in effective_pokemon_types(
                _board_for(pokemon), pokemon)

    def modify_burn_counters(self, counters, pokemon, carrier):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return counters
        replacement = re.search(
            r"put (\d+) damage counters instead of 2 on your opponent's burned",
            self.text,
        )
        if replacement:
            return int(replacement.group(1))
        extra = re.search(
            r"put (\d+) more damage counters? on your opponent's burned",
            self.text,
        )
        if extra:
            return counters + int(extra.group(1))
        if "put 4 damage counters instead of 2" in self.text:
            return 4
        return counters

    def modify_poison_counters(self, counters, pokemon, carrier):
        if "non-darkness pokémon (both yours and your opponent's)" in self.text:
            if PokemonTypes.DARKNESS.value in effective_pokemon_types(
                    _board_for(pokemon), pokemon):
                return counters
            extra = re.search(r"put (\d+) more damage counters", self.text)
            return counters + (int(extra.group(1)) if extra else 0)
        if pokemon.owning_player_id == carrier.owning_player_id:
            return counters
        replacement = re.search(
            r"put (\d+) damage counters instead of (?:1|2) on your opponent's poisoned",
            self.text,
        )
        if replacement:
            return int(replacement.group(1))
        extra = re.search(
            r"put (\d+) more damage counters? on your opponent's poisoned",
            self.text,
        )
        return counters + int(extra.group(1)) if extra else counters

    def modify_sleep_coins(self, coins, pokemon, carrier):
        applies = carrier_pokemon(carrier) is pokemon \
            or "both yours and your opponent's" in self.text
        return 2 if applies and "flip 2 coins instead of 1" in self.text else coins

    def checkup_damage_counters(self, pokemon, carrier):
        t = self.text
        if "mega evolution pokémon" in t and "between turns" in t:
            return 2 if _has_subtype(pokemon, "MEGA") else 0
        if "each pokémon-gx and pokémon-ex" in t and "between turns" in t:
            return 1 if (_has_subtype(pokemon, "GX") or _pokemon_ex(pokemon)) else 0
        if pokemon.owning_player_id == carrier.owning_player_id:
            return 0
        conditions = set(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        if "opponent's confused pokémon" in self.text \
                and CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED] in conditions:
            match = re.search(r"put (\d+) damage counters", self.text)
            return int(match.group(1)) if match else 0
        if "opponent's active pokémon" in self.text and "remains asleep" in self.text \
                and CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP] in conditions:
            match = re.search(r"put (\d+) damage counters", self.text)
            return int(match.group(1)) if match else 0
        return 0

    def modify_energy_provided(self, options, energy, holder, board, carrier=None):
        # A Special Energy's printed "this card provides ..." text belongs to
        # that physical card only.  Without this guard, one attached Rainbow/
        # Prism-style passive rewrote every other Energy on the same Pokémon.
        if carrier is not None and is_energy_card(carrier) and carrier is not energy:
            return options
        source = carrier_pokemon(carrier)
        if holder is None:
            return options
        t = self.text
        energy_name = _name(energy).casefold()
        if energy_name == "luminous energy" and "any other special energy attached" in t:
            others = [entry for entry in _attached(holder)
                      if entry is not energy and is_special_energy(entry)]
            if others:
                return [[PokemonTypes.COLORLESS.value]]
        if "provides every type of energy" in t:
            count = 1
            applies = True
            if energy_name == "reversal energy":
                opponent_id = _other_player_id(board, holder.owning_player_id)
                applies = bool(
                    opponent_id is not None
                    and _prizes_remaining(carrier, holder.owning_player_id)
                        > _prizes_remaining(carrier, opponent_id)
                    and _stage(holder) in (
                        PokemonStage.STAGE1.value, PokemonStage.STAGE2.value)
                    and not has_rule_box(holder.archetype_id)
                )
                count = 3
            elif energy_name == "counter energy":
                opponent_id = _other_player_id(board, holder.owning_player_id)
                applies = bool(
                    opponent_id is not None
                    and _prizes_remaining(carrier, holder.owning_player_id)
                        > _prizes_remaining(carrier, opponent_id)
                    and not (_has_subtype(holder, "GX") or _pokemon_ex(holder))
                )
                count = 2
            elif energy_name.startswith("super boost energy"):
                applies = _stage(holder) == PokemonStage.STAGE2.value
                stage_twos = sum(
                    _stage(pokemon) == PokemonStage.STAGE2.value
                    for pokemon in board.pokemon_in_play(holder.owning_player_id)
                )
                count = 4 if stage_twos >= 3 else 1
            else:
                explicit = re.search(r"provides only (\d+) energy at a time", t)
                count = int(explicit.group(1)) if explicit else 1
            if applies:
                return [[type_value] * count for type_value in _ALL_ENERGY_TYPES]
            return [[PokemonTypes.COLORLESS.value]]
        energy_burn = re.search(
            r"all energy attached to (?:this pokémon|[a-z0-9' .-]+) "
            r"are (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
            r"energy instead of their usual type",
            t,
        )
        if energy_burn and source is holder:
            energy_type = getattr(
                PokemonTypes, energy_burn.group(1).upper()).value
            return [
                [energy_type] * max(1, len(option))
                for option in options
            ]

        # Current-era imports spell Energy symbols either as ``GrassGrass``
        # or as ``[ [Grass] ] [ [Grass] ]``.  Both are the same recurring
        # continuous effect (Wild Growth, Burn Brightly, Psychic Mirage,
        # etc.).  Previously only the old Psychic wording was interpreted,
        # leaving the imported Wild Growth printing as a visual-only Ability.
        energy_text = " ".join(
            self.text.replace("[", "").replace("]", "").split()
        )
        for word, energy_type in (
            ("grass", PokemonTypes.GRASS),
            ("fire", PokemonTypes.FIRE),
            ("water", PokemonTypes.WATER),
            ("lightning", PokemonTypes.LIGHTNING),
            ("psychic", PokemonTypes.PSYCHIC),
            ("fighting", PokemonTypes.FIGHTING),
            ("darkness", PokemonTypes.DARKNESS),
            ("metal", PokemonTypes.METAL),
        ):
            if f"each basic {word} energy" not in energy_text:
                continue
            if not re.search(
                rf"provides\s+{word}\s*{word}\s+energy", energy_text
            ):
                continue
            if holder.owning_player_id != carrier.owning_player_id \
                    or not is_basic_energy(energy):
                return options
            # Psychic Mirage-like wording limits the benefit to Pokemon of a
            # named type; Wild Growth/Burn Brightly say merely "your Pokemon".
            if f"your {word} pokémon" in energy_text \
                    and energy_type.value not in effective_pokemon_types(board, holder):
                return options
            # Rewriting only a single-unit option naturally enforces the
            # printed non-stacking clause when another copy is already active.
            return [
                [energy_type.value, energy_type.value]
                if option == [energy_type.value] else option
                for option in options
            ]
        if "each basic psychic energy" in self.text \
                and holder.owning_player_id == carrier.owning_player_id \
                and PokemonTypes.PSYCHIC.value in effective_pokemon_types(board, holder) \
                and is_basic_energy(energy):
            rewritten = []
            for option in options:
                if option == [PokemonTypes.PSYCHIC.value]:
                    rewritten.append([PokemonTypes.PSYCHIC.value] * 2)
                else:
                    rewritten.append(option)
            return rewritten
        return options

    def modify_pokemon_types(self, types, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        t = self.text
        # Aqua/Flare/Electric Effect applies from the Ability carrier to every
        # Stage 1 Pokémon on its side, in addition to the printed type.
        stage_one_type = re.search(
            r"each of your stage 1 pokémon in play is now a "
            r"(grass|fire|water|lightning|psychic|fighting|darkness|metal) pokémon",
            t,
        )
        if stage_one_type and pokemon.owning_player_id == carrier.owning_player_id \
                and _stage(pokemon) == PokemonStage.STAGE1.value:
            ptype = getattr(PokemonTypes, stage_one_type.group(1).upper()).value
            return list(dict.fromkeys(types + [ptype]))
        if holder is not pokemon:
            return types
        pair = re.search(
            r"(?:it|this pokémon) is (?:a )?"
            r"(grass|fire|water|lightning|psychic|fighting|darkness|metal) and "
            r"(grass|fire|water|lightning|psychic|fighting|darkness|metal) type",
            t,
        )
        if pair:
            if "future booster energy capsule attached" in t and not any(
                    _name(card).casefold() == "future booster energy capsule"
                    for card in _attached(pokemon)):
                return types
            return list(dict.fromkeys(types + [
                getattr(PokemonTypes, pair.group(1).upper()).value,
                getattr(PokemonTypes, pair.group(2).upper()).value,
            ]))
        unit_types = {
            "unit energy grassfirewater": (
                PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER),
            "unit energy lightningpsychicmetal": (
                PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.METAL),
            "unit energy fightingdarknessfairy": (
                PokemonTypes.FIGHTING, PokemonTypes.DARKNESS, PokemonTypes.FAIRY),
        }
        for energy_name, values in unit_types.items():
            if energy_name in t and any(
                    _name(card).casefold().replace(" ", "")
                    == energy_name.replace(" ", "")
                    for card in _attached(pokemon)):
                return list(dict.fromkeys(types + [value.value for value in values]))
        if "type is both fighting and metal" in self.text and any(
                energy_provides_type(e, PokemonTypes.METAL.value)
                for e in _attached(pokemon)):
            return list(dict.fromkeys(types + [PokemonTypes.FIGHTING.value,
                                                PokemonTypes.METAL.value]))
        if "same type as" in self.text and _is_active(holder):
            active = next((node for node in _walk(_tree_root(pokemon))
                           if isinstance(node, PokemonEntity)
                           and node.owning_player_id != pokemon.owning_player_id
                           and _is_active(node)), None)
            if active is not None:
                return list(active.get_attribute(AttrID.POKEMON_TYPES) or types)
        memories = {
            "fighting memory": PokemonTypes.FIGHTING.value,
            "fire memory": PokemonTypes.FIRE.value,
            "grass memory": PokemonTypes.GRASS.value,
            "electric memory": PokemonTypes.LIGHTNING.value,
            "psychic memory": PokemonTypes.PSYCHIC.value,
            "water memory": PokemonTypes.WATER.value,
        }
        for label, type_value in memories.items():
            if _name(carrier).casefold() == label \
                    and _name(holder).casefold() == "silvally-gx":
                return [type_value]
        return types

    def granted_attacks(self, board, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if "attacks of any pokémon in play" in self.text:
            if holder is not pokemon:
                return []
            return [ability
                    for pid in board.player_ids
                    for other in board.pokemon_in_play(pid)
                    for ability in (getattr(def_for(other.archetype_id), "abilities", None) or [])
                    if isinstance(ability, Attack)]
        if "previous evolutions" in self.text:
            if pokemon.owning_player_id != carrier.owning_player_id:
                return []
            return [ability
                    for previous in full_stack(pokemon)[1:]
                    if isinstance(previous, PokemonEntity)
                    for ability in (getattr(def_for(previous.archetype_id), "abilities", None) or [])
                    if isinstance(ability, Attack)]
        if "attacks of any basic pokémon in your discard pile" in self.text:
            if holder is not pokemon:
                return []
            discard = _area_from(carrier, carrier.owning_player_id, "discard")
            return [
                ability
                for card in (discard.children if discard else [])
                if is_basic_pokemon(card)
                for ability in (
                    getattr(def_for(card.archetype_id), "abilities", None) or []
                )
                if isinstance(ability, Attack)
            ]
        return []

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        holder = carrier_pokemon(carrier)
        damage_ko = ctx.is_attack_effect() \
            and pokemon.entity_id in ctx.attack_damage
        if "can't take any prize cards for it" in self.text and pokemon is holder:
            if "opponent's pokémon ex" in self.text and not _pokemon_ex(ctx.attacker):
                return count
            return 0
        fewer_applies = pokemon is holder
        if "1 of your darkness pokémon is knocked out" in self.text:
            fewer_applies = pokemon.owning_player_id == carrier.owning_player_id \
                and PokemonTypes.DARKNESS.value in effective_pokemon_types(
                    ctx.board, pokemon)
        if "takes 1 fewer prize card" in self.text and fewer_applies and damage_ko:
            if "opponent's pokémon ex" in self.text and not _pokemon_ex(ctx.attacker):
                return count
            if "pecharunt ex in play" in self.text and not _has_named_in_play(
                    carrier, pokemon.owning_player_id, "Pecharunt ex"):
                return count
            return max(0, count - 1)
        if "that player takes 1 more prize card" in self.text and pokemon is holder \
                and damage_ko:
            if "doesn't have a rule box" not in self.text \
                    or not has_rule_box(pokemon.archetype_id):
                return count + 1
        if "take 1 more prize card" not in self.text:
            return count
        if not ctx.is_attack_effect() or ctx.attacker is not holder:
            return count
        if pokemon.owning_player_id == holder.owning_player_id:
            return count
        if pokemon.entity_id not in ctx.attack_damage:
            return count
        if "exactly 6 prize cards remaining" in self.text \
                and _prizes_remaining(carrier, holder.owning_player_id) != 6:
            return count
        if "ultra beast this card is attached to" in self.text \
                and not _has_subtype(holder, "Ultra Beast"):
            return count
        if "active pokémon-gx or pokémon-ex" in self.text \
                and not (_has_subtype(pokemon, "GX") or _pokemon_ex(pokemon)):
            return count
        return count + 1

    async def extra_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        holder = carrier_pokemon(carrier)
        if pokemon is not holder or "evanescent" not in self.text \
                or not ctx.is_attack_effect() \
                or pokemon.entity_id not in ctx.attack_damage:
            return 0
        if not _is_active(holder):
            return 0
        return -1 if (await ctx.flip_coins(1, "Evanescent"))[0] else 0

    def knockout_destination_for(self, pokemon, ctx, carrier):
        t = self.text
        holder = carrier_pokemon(carrier)
        damage_ko = ctx.is_attack_effect() \
            and pokemon.entity_id in ctx.attack_damage
        if "as long as gengar is your active pokémon" in t \
                and holder is not None and _is_active(holder) \
                and pokemon.owning_player_id != holder.owning_player_id:
            return "lostZone"
        if "put that pokémon and all cards attached to it in the lost zone" in t \
                and holder is ctx.attacker and damage_ko \
                and pokemon.owning_player_id != holder.owning_player_id:
            return "lostZone"
        if pokemon is not holder or not damage_ko:
            return None
        if "put it into your hand instead of the discard pile" in t \
                or "put that pokémon into your hand" in t \
                or "put that pokémon back into your hand" in t:
            return "hand"
        return None

    def knockout_attachment_destination(self, pokemon, ctx, carrier):
        holder = carrier_pokemon(carrier)
        if "put that pokémon and all cards attached to it in the lost zone" \
                in self.text and holder is ctx.attacker \
                and ctx.is_attack_effect() \
                and pokemon.entity_id in ctx.attack_damage:
            return "lostZone"
        return None

    async def on_knocked_out(self, ctx, pokemon, carrier):
        t = self.text
        holder = carrier_pokemon(carrier)
        from_attack = bool(getattr(ctx, "ko_from_attack", False))
        attacker = getattr(ctx, "ko_attacker", None)
        if "hypnotic pendulum" in t:
            if holder is None \
                    or pokemon.owning_player_id == holder.owning_player_id \
                    or not getattr(ctx, "was_active_at_ko", False):
                return
            bench = list(ctx.board.pokemon_in_play(pokemon.owning_player_id))
            bench = [candidate for candidate in bench
                     if getattr(getattr(candidate, "parent", None), "get_attribute", lambda *_: None)(
                         AttrID.NAME) == "bench"]
            if not bench:
                return
            heads = (await ctx.flip_coins(
                1, "Hypnotic Pendulum", source=carrier,
                player_id=holder.owning_player_id,
            ))[0]
            if not heads:
                return
            picked = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench,
                "Choose your opponent's new Active Pokémon",
                player_id=holder.owning_player_id,
            )
            if picked is not None:
                ctx.session._forced_promotion_ids[pokemon.owning_player_id] = \
                    picked.entity_id
            return
        if "damage from" in t and "attack" in t and not from_attack:
            return

        allied = pokemon.owning_player_id == carrier.owning_player_id
        if "1 of your" in t or "when 1 of your pokémon" in t:
            if not allied:
                return
            if "water pokémon" in t and PokemonTypes.WATER.value not in \
                    effective_pokemon_types(ctx.board, pokemon):
                return
        elif pokemon is not holder:
            return
        if "is your active pokémon" in t or "is in the active spot" in t:
            if not getattr(ctx, "was_active_at_ko", False):
                return

        attachments = list(getattr(ctx, "knocked_out_attachments", []) or [])
        energies = [card for card in attachments if is_energy_card(card)]

        random_discard = re.search(
            r"discard (\d+|a) random cards? from your opponent's hand", t
        )
        if random_discard:
            count = 1 if random_discard.group(1) == "a" \
                else int(random_discard.group(1))
            hand = ctx.hand(ctx.opponent_id)
            picks = random.sample(hand, min(count, len(hand))) if hand else []
            await ctx.discard_cards(picks)

        search = re.search(r"search your deck for (?:up to )?(\d+|a) cards?", t)
        if search:
            count = 1 if search.group(1) == "a" else int(search.group(1))
            minimum = 0 if "up to" in search.group(0) else count
            cards = await ctx.search_deck(
                None, count, minimum=minimum,
                prompt=f"Choose {count} card{'s' if count != 1 else ''}",
            )
            await ctx.put_in_hand(cards, reveal=False)
            await ctx.shuffle_deck()

        into_hand = "into your hand instead of the discard pile" in t \
            or "put all basic energy attached to that pokémon into your hand" in t
        if into_hand:
            candidates = [energy for energy in energies if is_basic_energy(energy)]
            if "basic water energy" in t:
                candidates = [energy for energy in candidates if energy_provides_type(
                    energy, PokemonTypes.WATER.value)]
            if "you may" in t and candidates and not await ctx.ask_yes_no(
                    "Move the Energy cards into your hand?"):
                candidates = []
            await ctx.put_in_hand(candidates, reveal=False)

        move_match = re.search(r"move up to (\d+) (?:basic )?(?:\[ \[)?"
                               r"(water|lightning)?(?:\] \])? ?energy cards?", t)
        grounding = "energy grounding" in t or "electrical grounding" in t
        if move_match or grounding:
            count = int(move_match.group(1)) if move_match else 1
            type_word = move_match.group(2) if move_match else (
                "lightning" if "electrical grounding" in t else None)
            candidates = [energy for energy in energies
                          if (not type_word or energy_provides_type(
                              energy, getattr(PokemonTypes, type_word.upper()).value))]
            if "basic energy" in t:
                candidates = [energy for energy in candidates if is_basic_energy(energy)]
            if grounding:
                target = holder
                if target is not None and target.parent is not None and candidates \
                        and await ctx.ask_yes_no("Move an Energy card?"):
                    picked = await ctx.choose_cards(
                        candidates, 1, prompt="Choose an Energy card")
                    if picked:
                        await ctx.attach_energy(picked[0], target)
            else:
                picked = await ctx.choose_cards(
                    candidates, count, minimum=0,
                    prompt="Choose Energy cards to keep in play",
                )
                knocked_out = getattr(ctx, "knocked_out_pokemon", None)
                bench = [entry for entry in ctx.my_bench()
                         if entry is not knocked_out]
                for energy in picked:
                    if not bench:
                        break
                    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                        bench, "Choose a Pokémon for this Energy")
                    if target is not None:
                        await ctx.attach_energy(energy, target)

        counter_match = re.search(
            r"put (\d+) damage counters on (?:1 of )?your opponent's pokémon", t
        )
        if counter_match:
            await ctx.place_damage_counters(
                int(counter_match.group(1)), ctx.opponent_pokemon_in_play())

        if attacker is not None and "attacking pokémon is knocked out" in t:
            if "flip a coin" not in t \
                    or (await ctx.flip_coins(1, "Knock Out the attacker"))[0]:
                await ctx.knock_out(attacker)


def bw_legacy_passive(text: str) -> Passive:
    return _BWTextPassive(text)


# ---------------------------------------------------------------------------
# Generated attack / activated-or-triggered Ability fallbacks
# ---------------------------------------------------------------------------

def _norm(text: str) -> str:
    normalized = re.sub(
        r"\[\s*\[\s*([a-z]+)\s*\]\s*\]", r"\1",
        (text or "").replace("Pok�mon", "Pokémon").lower(),
    )
    return " ".join(normalized.split())


def _number_before(text: str, phrase: str) -> Optional[int]:
    m = re.search(r"(\d+)\s+(?:more\s+)?damage[^.]*" + re.escape(phrase), text)
    if m:
        return int(m.group(1))
    m = re.search(r"(\d+)\s+" + re.escape(phrase), text)
    return int(m.group(1)) if m else None


def _number_after(text: str, phrase: str) -> Optional[int]:
    m = re.search(re.escape(phrase) + r"\s+(\d+)", text)
    return int(m.group(1)) if m else None


def _energy_count(ctx, pokemon, type_word: Optional[str] = None) -> int:
    energies = ctx.attached_energies(pokemon) if pokemon is not None else []
    if not type_word:
        return sum(
            max((len(option) for option in energy_provided_options(ctx.board, energy)),
                default=1)
            for energy in energies
        )
    ptype = getattr(PokemonTypes, type_word.upper(), None)
    if ptype is None:
        return 0
    return sum(
        max((option.count(ptype.value)
             for option in energy_provided_options(ctx.board, energy)), default=0)
        for energy in energies
    )


def _scoped_energy_count(ctx, subject: str) -> Optional[int]:
    """Count Energy named by an ``attached to all ... Pokémon`` clause.

    The imported card pool uses several equivalent wordings for this family:
    ``for each``, ``times the amount of``, typed Energy, and untyped Energy.
    Keeping the scope and descriptor parsing together prevents typed attacks
    such as Dark Pulse from either falling back to printed damage or counting
    unrelated Energy types.
    """
    if "attached to all of your opponent's pokémon" in subject:
        pokemon = ctx.opponent_pokemon_in_play()
        marker = "attached to all of your opponent's pokémon"
    elif own_match := re.search(
            r"attached to all of your (?:(.*?) )?pokémon", subject):
        pokemon = ctx.my_pokemon_in_play()
        marker = own_match.group(0)
        qualifier = (own_match.group(1) or "").strip()
        if qualifier == "benched":
            pokemon = ctx.my_bench()
        elif qualifier:
            ptype = getattr(PokemonTypes, qualifier.upper(), None)
            if ptype is not None:
                pokemon = [
                    target for target in pokemon
                    if ptype.value in effective_pokemon_types(ctx.board, target)
                ]
            else:
                prefix = f"{qualifier} "
                pokemon = [
                    target for target in pokemon
                    if _name(target).casefold().startswith(prefix)
                ]
    elif "attached to all pokémon" in subject:
        pokemon = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        marker = "attached to all pokémon"
    else:
        return None

    descriptor = subject.split(marker, 1)[0].strip()
    type_match = re.search(
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
        r"energy$",
        descriptor,
    )
    type_word = type_match.group(1) if type_match else None
    basic_only = "basic energy" in descriptor
    special_only = "special energy" in descriptor
    cards_only = "energy card" in descriptor

    # Named Special Energy (Fusion Strike Energy, Plasma Energy, etc.) is a
    # card identity, not an Energy type. Generic and typed descriptors are
    # handled by their provided Energy values below.
    generic_descriptors = {
        "energy", "energy card", "energy cards", "basic energy",
        "basic energy card", "basic energy cards", "special energy",
        "special energy card", "special energy cards",
    }
    named_energy = None
    if type_word is None and descriptor not in generic_descriptors \
            and descriptor.endswith(" energy"):
        named_energy = descriptor

    type_value = getattr(PokemonTypes, type_word.upper()).value \
        if type_word is not None else None
    total = 0
    for target in pokemon:
        for energy in ctx.attached_energies(target):
            if basic_only and not is_basic_energy(energy):
                continue
            if special_only and not is_special_energy(energy):
                continue
            if named_energy is not None \
                    and _name(energy).casefold() != named_energy:
                continue
            if cards_only or named_energy is not None:
                total += 1
            elif type_value is not None:
                total += max(
                    (option.count(type_value)
                     for option in energy_provided_options(ctx.board, energy)),
                    default=0,
                )
            else:
                total += max(
                    (len(option)
                     for option in energy_provided_options(ctx.board, energy)),
                    default=1,
                )
    return total


def _scoped_tool_count(ctx, subject: str) -> Optional[int]:
    """Count Tools for Tool Drop/Gadget Show-style field-wide formulas."""
    if "attached to all of your pokémon" in subject:
        pokemon = ctx.my_pokemon_in_play()
    elif "attached to all pokémon" in subject \
            or "attached to pokémon in play" in subject:
        pokemon = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    else:
        return None
    return sum(
        is_pokemon_tool(card)
        for target in pokemon
        for card in full_stack(target)[1:]
    )


def _scoped_damage_counter_count(ctx, subject: str) -> Optional[int]:
    """Count counters across a named in-play group instead of one Pokémon."""
    marker = re.search(r"damage counters? on all of (.+?)(?:\.|$)", subject)
    if marker is None:
        return None
    scope = marker.group(1).strip()
    if scope == "your opponent's pokémon":
        pokemon = ctx.opponent_pokemon_in_play()
    elif scope.startswith("your benched "):
        pokemon = ctx.my_bench()
        qualifier = scope.removeprefix("your benched ").strip()
        if qualifier != "pokémon":
            if qualifier.endswith(" pokémon"):
                qualifier = qualifier.removesuffix(" pokémon").strip()
            ptype = getattr(PokemonTypes, qualifier.upper(), None)
            if ptype is not None:
                pokemon = [
                    target for target in pokemon
                    if ptype.value in effective_pokemon_types(ctx.board, target)
                ]
            elif qualifier:
                prefix = f"{qualifier} "
                pokemon = [
                    target for target in pokemon
                    if _name(target).casefold() == qualifier
                    or _name(target).casefold().startswith(prefix)
                ]
    elif scope == "your pokémon":
        pokemon = ctx.my_pokemon_in_play()
    elif scope.startswith("your "):
        pokemon = ctx.my_pokemon_in_play()
        names = {
            name.strip()
            for name in re.split(r",| and ", scope.removeprefix("your "))
            if name.strip()
        }
        pokemon = [
            target for target in pokemon
            if _name(target).casefold() in names
        ]
    else:
        return None
    return sum(_damage_counter_count(ctx, target) for target in pokemon)


def _damage_counter_count(ctx, pokemon) -> int:
    return max(0, (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10)


def _formula_damage(ctx, text: str) -> Optional[int]:
    printed = getattr(ctx.ability, "damage", 0) or 0
    tool_mult = re.search(
        r"does (\d+) damage for each (pokémon tool(?: card)? attached to "
        r"(?:all of your pokémon|all pokémon|pokémon in play))",
        text,
    )
    if tool_mult:
        count = _scoped_tool_count(ctx, tool_mult.group(2))
        return int(tool_mult.group(1)) * (count or 0)
    # X damage times attached Energy / damage counters / Bench / in-play.
    mult = re.search(
        r"does (\d+) damage (?:times (?:the amount|the number) of|for each) "
        r"(.+?)(?:\.|$)",
        text,
    )
    if mult:
        per, subject = int(mult.group(1)), mult.group(2)
        scoped_energy = _scoped_energy_count(ctx, subject)
        if scoped_energy is not None:
            return per * scoped_energy
        scoped_counters = _scoped_damage_counter_count(ctx, subject)
        if scoped_counters is not None:
            return per * scoped_counters
        if "energy attached to this pokémon and the defending pokémon" in subject:
            return per * (_energy_count(ctx, ctx.attacker) + _energy_count(ctx, ctx.defender))
        mtype = re.search(r"(grass|fire|water|lightning|psychic|fighting|darkness|metal) energy attached to this pokémon", subject)
        if mtype:
            return per * _energy_count(ctx, ctx.attacker, mtype.group(1))
        if "energy attached to this pokémon" in subject:
            return per * _energy_count(ctx, ctx.attacker)
        if "damage counters on this pokémon" in subject:
            return per * _damage_counter_count(ctx, ctx.attacker)
        if "damage counters on the defending pokémon" in subject:
            return per * _damage_counter_count(ctx, ctx.defender)
        if "your benched pokémon" in subject:
            return per * len(ctx.my_bench())
        if "your pokémon that have the round attack" in subject:
            return per * sum(_has_attack_named(p, "Round")
                             for p in ctx.my_pokemon_in_play())
        if "reuniclus you have in play" in subject:
            return per * sum(_name(p) == "Reuniclus"
                             for p in ctx.my_pokemon_in_play())
        if "team plasma pokémon you have in play" in subject:
            return per * sum(_team_plasma(p) for p in ctx.my_pokemon_in_play())
        if "pokémon tool card attached to pokémon in play" in subject:
            return per * sum(
                is_pokemon_tool(card)
                for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
                for card in full_stack(p)[1:]
            )
        if "pokémon in play" in subject:
            return per * (len(ctx.my_pokemon_in_play()) + len(ctx.opponent_pokemon_in_play()))
        if "prize cards you have taken" in subject:
            return per * ctx.prizes_taken()
        if "prize cards both players have taken" in subject:
            return per * (ctx.prizes_taken() + ctx.prizes_taken(ctx.opponent_id))
        if "cards in your opponent's hand" in subject:
            return per * ctx.hand_size(ctx.opponent_id)
        if "cards in your hand" in subject:
            return per * ctx.hand_size()
        if "pokémon in your discard pile" in subject:
            return per * sum(is_pokemon_card(card) for card in ctx.discard_pile())
        if "energy cards in your discard pile" in subject:
            cards = [card for card in ctx.discard_pile() if is_energy_card(card)]
            if "basic energy" in subject:
                cards = [card for card in cards if is_basic_energy(card)]
            for word in (
                "grass", "fire", "water", "lightning", "psychic", "fighting",
                "darkness", "metal", "fairy",
            ):
                if f"{word} energy" in subject:
                    cards = [card for card in cards if _energy_predicate(word)(card)]
                    break
            return per * len(cards)

    # Printed base + N for each Energy/counter/bench member.
    more = re.search(
        r"does (\d+) more damage "
        r"(?:for each|times (?:the amount|the number) of) (.+?)(?:\.|$)",
        text,
    )
    if more:
        per, subject = int(more.group(1)), more.group(2)
        scoped_energy = _scoped_energy_count(ctx, subject)
        if scoped_energy is not None:
            return printed + per * scoped_energy
        scoped_counters = _scoped_damage_counter_count(ctx, subject)
        if scoped_counters is not None:
            return printed + per * scoped_counters
        if "energy attached to the defending pokémon" in subject:
            return printed + per * _energy_count(ctx, ctx.defender)
        if "plasma energy attached to this pokémon" in subject:
            return printed + per * sum(
                _name(e) == "Plasma Energy"
                for e in ctx.attached_energies(ctx.attacker)
            )
        if "grass energy attached to both your and your opponent's pokémon" in subject:
            return printed + per * sum(
                _energy_count(ctx, p, "grass")
                for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
            )
        mtype = re.search(r"(grass|fire|water|lightning|psychic|fighting|darkness|metal) energy attached to this pokémon", subject)
        if mtype:
            return printed + per * _energy_count(ctx, ctx.attacker, mtype.group(1))
        if "damage counter on the defending pokémon" in subject:
            return printed + per * _damage_counter_count(ctx, ctx.defender)
        if "damage counter on this pokémon" in subject:
            return printed + per * _damage_counter_count(ctx, ctx.attacker)
        if "opponent's benched pokémon" in subject:
            return printed + per * len(ctx.opponent_bench())
        if "nidoqueen on your bench" in subject:
            return printed + per * sum(_name(p) == "Nidoqueen" for p in ctx.my_bench())
        if "benched pokémon" in subject:
            return printed + per * len(ctx.my_bench())
        if "prize card your opponent has taken" in subject:
            return printed + per * ctx.prizes_taken(ctx.opponent_id)
        if "pokémon in your discard pile" in subject:
            return printed + per * sum(is_pokemon_card(c) for c in ctx.discard_pile())
        if "energy card" in subject and "in your discard pile" in subject:
            cards = [card for card in ctx.discard_pile() if is_energy_card(card)]
            if "basic energy" in subject:
                cards = [card for card in cards if is_basic_energy(card)]
            for word in (
                "grass", "fire", "water", "lightning", "psychic", "fighting",
                "darkness", "metal", "fairy",
            ):
                if f"{word} energy" in subject:
                    cards = [card for card in cards if _energy_predicate(word)(card)]
                    break
            return printed + per * len(cards)
    loose_more = re.search(r"does (\d+) (?:or )?more for each damage counter on this pokémon", text)
    if loose_more:
        return printed + int(loose_more.group(1)) * _damage_counter_count(
            ctx, ctx.attacker)
    minus = re.search(r"does (\d+) damage minus (\d+) damage for each damage counter on this pokémon", text)
    if minus:
        return max(0, int(minus.group(1))
                   - int(minus.group(2)) * _damage_counter_count(ctx, ctx.attacker))
    bench_damaged = re.search(r"does (\d+) more damage for each of your benched pokémon that has any damage counters", text)
    if bench_damaged:
        return printed + int(bench_damaged.group(1)) * sum(
            _damage_counter_count(ctx, p) > 0 for p in ctx.my_bench())
    if "number of trainer cards in your opponent's hand" in text:
        per = int((re.search(r"does (\d+) damage times", text) or [None, 0])[1])
        return per * sum(is_trainer_card(card) for card in ctx.hand(ctx.opponent_id))
    if "number of water energy cards and lightning energy cards in your discard pile" in text:
        per = int((re.search(r"does (\d+) damage times", text) or [None, 0])[1])
        return per * sum(
            is_energy_card(card) and (
                energy_provides_type(card, PokemonTypes.WATER.value)
                or energy_provides_type(card, PokemonTypes.LIGHTNING.value)
            ) for card in ctx.discard_pile())
    return None


class _BWTurnShield(Passive):
    def __init__(self, amount=0, *, outgoing=False, increase=False,
                 threshold=None, prevent_all=False, damage_only=False,
                 effects_only=False,
                 no_weakness=False,
                 attacker_predicate=None):
        self.amount = amount
        self.outgoing = outgoing
        self.increase = increase
        self.threshold = threshold
        self.prevent_all = prevent_all
        self.damage_only = damage_only
        self.effects_only = effects_only
        self.no_weakness = no_weakness
        self.attacker_predicate = attacker_predicate

    def modify_damage_dealt(self, calc, carrier):
        if not self.outgoing or calc.attacker is not carrier or not calc.is_attack:
            return
        calc.amount = max(0, calc.amount - self.amount)

    def modify_damage_taken(self, calc, carrier):
        if self.outgoing or calc.target is not carrier or not calc.is_attack:
            return
        if self.increase:
            calc.amount += self.amount
        elif not self.prevent_all and self.threshold is None:
            calc.amount = max(0, calc.amount - self.amount)

    def prevents_damage(self, calc, carrier):
        if calc.target is not carrier or not calc.is_attack:
            return False
        if self.attacker_predicate is not None \
                and not self.attacker_predicate(calc.attacker):
            return False
        return self.prevent_all or self.damage_only or (
            self.threshold is not None and calc.amount <= self.threshold
        )

    def modify_weakness(self, calc, carrier):
        if self.no_weakness and calc.target is carrier:
            calc.weakness_applies = False

    def blocks_attack_effects(self, target, carrier):
        return bool((self.prevent_all or self.effects_only) and target is carrier)


class _BWPlayerAttackShield(Passive):
    """One-turn protection for every Pokémon belonging to one player."""

    def __init__(self, player_id, *, damage=True, effects=True,
                 target_predicate=None, attacker_predicate=None,
                 active_source_id=None):
        self.player_id = player_id
        self.damage = damage
        self.effects = effects
        self.target_predicate = target_predicate
        self.attacker_predicate = attacker_predicate
        self.active_source_id = active_source_id

    def _matches(self, target, attacker=None, board=None):
        if target is None or target.owning_player_id != self.player_id:
            return False
        if self.active_source_id is not None and board is not None:
            active = board.active_pokemon(self.player_id)
            if active is None or active.entity_id != self.active_source_id:
                return False
        if self.target_predicate is not None and not self.target_predicate(target):
            return False
        return self.attacker_predicate is None or self.attacker_predicate(attacker)

    def prevents_damage(self, calc, carrier):
        return bool(self.damage and calc.is_attack and self._matches(
            calc.target, calc.attacker, calc.board,
        ))

    def blocks_attack_effects(self, target, carrier):
        # Effects are checked while the target is still in play.  The player
        # scoped carrier keeps the rule available for Pokémon entering later.
        return bool(self.effects and self._matches(target))


class _BWTemporaryPokemonType(Passive):
    """A clicked, end-of-turn type change such as Underwater Dive."""

    def __init__(self, pokemon_type):
        self.pokemon_type = pokemon_type

    def modify_pokemon_types(self, types, pokemon, carrier):
        return [self.pokemon_type.value] if pokemon is carrier else types


class _BWTemporaryEnergyType(Passive):
    """Side-wide Energy type rewrite used by Blazing Energy."""

    def __init__(self, player_id, pokemon_type):
        self.player_id = player_id
        self.pokemon_type = pokemon_type

    def modify_energy_provided(self, options, energy, holder, board, carrier=None):
        if holder is None or holder.owning_player_id != self.player_id:
            return options
        count = max((len(option) for option in options), default=1)
        return [[self.pokemon_type.value] * count]


class _BWTemporaryCombatRule(Passive):
    """Small, composable attack riders that expire with a temporary passive.

    Older sets express the same rule with dozens of card-name-specific
    wordings (Focus Energy, Work Up, Rock Polish, Sticky Liquid, Conversion).
    Keeping the state in one passive lets the normal damage/cost pipeline
    apply it to copied attacks and to a Pokemon that remains Active.
    """

    def __init__(self, *, damage_boost=0, damage_taken_add=0,
                 attack_title=None, base_damage=None,
                 retreat_zero=False, retreat_add=0, attack_cost_add=0,
                 weakness_type=None, attacks_blocked=False, unique_key=None):
        self.damage_boost = damage_boost
        self.damage_taken_add = damage_taken_add
        self.attack_title = attack_title.casefold() if attack_title else None
        self.base_damage = base_damage
        self.retreat_zero = retreat_zero
        self.retreat_add = retreat_add
        self.attack_cost_add = attack_cost_add
        self.weakness_type = weakness_type
        self.attacks_blocked = attacks_blocked
        self.unique_key = unique_key

    def _attack_matches(self, calc, carrier):
        if calc.attacker is not carrier or not calc.is_attack:
            return False
        return self.attack_title is None or (
            (calc.attack_title or "").casefold() == self.attack_title
        )

    def modify_damage_dealt(self, calc, carrier):
        if not self._attack_matches(calc, carrier):
            return
        if self.unique_key and self.unique_key in calc.applied_once:
            return
        if self.unique_key:
            calc.applied_once.add(self.unique_key)
        if self.base_damage is not None:
            calc.amount += self.base_damage - calc.base
        calc.amount += self.damage_boost

    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.target is carrier:
            calc.amount += self.damage_taken_add

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier or not self.attack_cost_add:
            return cost
        out = dict(cost)
        out["Colorless"] = out.get("Colorless", 0) + self.attack_cost_add
        return out

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        return 0 if self.retreat_zero else cost + self.retreat_add

    def modify_weakness(self, calc, carrier):
        if calc.target is carrier and self.weakness_type is not None:
            calc.weak_types = [self.weakness_type.value]

    def blocks_attacks(self, pokemon, carrier):
        return self.attacks_blocked and pokemon is carrier


class _BWPlayerCombatRule(Passive):
    """A lasting or turn-scoped rule carried by a player rather than a card."""

    def __init__(self, player_id, *, damage_boost=0, damage_reduction=0,
                 damage_reduction_types=None,
                 attacks_blocked=False, free_attack_types=None,
                 extra_prizes=0, max_attack_energy=None):
        self.player_id = player_id
        self.damage_boost = damage_boost
        self.damage_reduction = damage_reduction
        self.damage_reduction_types = set(damage_reduction_types or [])
        self.attacks_blocked = attacks_blocked
        self.free_attack_types = set(free_attack_types or [])
        self.extra_prizes = extra_prizes
        self.max_attack_energy = max_attack_energy

    def modify_damage_dealt(self, calc, carrier):
        if calc.is_attack and calc.attacker is not None \
                and calc.attacker.owning_player_id == self.player_id:
            calc.amount += self.damage_boost

    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.target.owning_player_id == self.player_id:
            if self.damage_reduction_types and not (
                set(effective_pokemon_types(calc.board, calc.target))
                & self.damage_reduction_types
            ):
                return
            calc.amount = max(0, calc.amount - self.damage_reduction)

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id != self.player_id:
            return cost
        live_types = set(effective_pokemon_types(board, pokemon))
        return {} if live_types & self.free_attack_types else cost

    def blocks_attacks(self, pokemon, carrier):
        if pokemon.owning_player_id != self.player_id:
            return False
        if self.attacks_blocked:
            return True
        if self.max_attack_energy is not None:
            board = getattr(carrier, "board", None)
            if board is None:
                board = getattr(pokemon, "board", None)
            # Card-count wording is rare here; Frigid Fangs says Energy, so
            # provided units (DCE=2) are the correct comparison.
            attached = []
            parent_board = getattr(pokemon, "_board", None) or board
            if parent_board is not None:
                attached = parent_board.attached_energies(pokemon)
            else:
                attached = full_stack(pokemon)[1:]
            provided = sum(
                max((len(option) for option in energy_provided_options(
                    parent_board, energy)), default=0)
                for energy in attached if is_energy_card(energy)
            )
            return provided <= self.max_attack_energy
        return False

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        attacker = getattr(ctx, "ko_attacker", None) or getattr(ctx, "attacker", None)
        if self.extra_prizes and attacker is not None \
                and attacker.owning_player_id == self.player_id \
                and pokemon.owning_player_id != self.player_id \
                and getattr(ctx, "ko_from_attack", False):
            return count + self.extra_prizes
        return count


class _BWKnockOutIfDamaged(Passive):
    """The next opposing attack that deals damage Knocks Out the holder."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if target is carrier and calc.is_attack and calc.is_opposing \
                and calc.amount > 0:
            return max(calc.amount, target.get_attribute(AttrID.HP, 0))
        return None


class _BWRetaliateWhenDamaged(Passive):
    """Damage-counter retaliation that still fires if its holder is KO'd."""

    def __init__(self, counters=0, *, mirror_damage=False,
                 discard_attacker_energy=False):
        self.counters = counters
        self.mirror_damage = mirror_damage
        self.discard_attacker_energy = discard_attacker_energy

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if target is not carrier or not calc.is_attack or not calc.is_opposing \
                or calc.amount <= 0 or calc.attacker is None:
            return None
        attacker_id = calc.attacker.entity_id
        amount = calc.amount if self.mirror_damage else self.counters * 10
        should_discard = self.discard_attacker_energy \
            and calc.amount >= target.get_attribute(AttrID.HP, 0)

        async def retaliate():
            attacker = ctx.board.get_entity(attacker_id)
            if not isinstance(attacker, PokemonEntity):
                return
            if should_discard:
                await ctx.discard_energy_from(attacker, 1)
            elif amount:
                await ctx.deal_damage(
                    amount, target=attacker, apply_modifiers=False,
                    as_counters=True, is_attack=False,
                )
            if ctx.knockouts:
                await ctx.session.resolve_knockouts(ctx)

        ctx.deferred_actions.append(retaliate)
        return None


class _BWPrizeRule(Passive):
    """A temporary mark on a Pokémon that modifies its eventual Prize award."""

    def __init__(self, beneficiary_id, *, bonus=0, suppress=False):
        self.beneficiary_id = beneficiary_id
        self.bonus = bonus
        self.suppress = suppress

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier:
            return count
        attacker = getattr(ctx, "ko_attacker", None) or getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id != self.beneficiary_id:
            return count
        if self.suppress:
            return 0
        return count + self.bonus


class _BWPoisonCounterRule(Passive):
    """Attack-applied poison severity carried by the affected Pokémon."""

    def __init__(self, *, replacement=None, extra=0):
        self.replacement = replacement
        self.extra = extra

    def modify_poison_counters(self, counters, pokemon, carrier):
        if pokemon is not carrier:
            return counters
        if self.replacement is not None:
            return self.replacement
        return counters + self.extra


class _BWAttachedPokemonRule(Passive):
    """Rules retained while a Pokemon card is functioning as a Tool.

    The carrier is the physical Shedinja/Klefki card and its holder is found
    through ``carrier_pokemon`` just like an ordinary Tool.
    """

    def __init__(self, *, fewer_prizes=0, block_mega_damage=False):
        self.fewer_prizes = fewer_prizes
        self.block_mega_damage = block_mega_damage

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if self.fewer_prizes and carrier_pokemon(carrier) is pokemon:
            return max(0, count - self.fewer_prizes)
        return count

    def prevents_damage(self, calc, carrier):
        return bool(
            self.block_mega_damage
            and calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.target
            and calc.attacker is not None
            and "MEGA" in (subtypes_for(calc.attacker.archetype_id) or [])
        )


def _energy_predicate(word: Optional[str]):
    ptype = getattr(PokemonTypes, (word or "").upper(), None)
    if word == "basic":
        return is_basic_energy
    if ptype is None:
        return is_energy_card
    return lambda card: is_energy_card(card) and energy_provides_type(
        card, ptype.value)


def _energy_phrase_predicate(phrase: Optional[str]):
    """Predicate for phrases such as ``basic Fighting Energy``.

    Treating ``basic`` and the printed type as mutually exclusive made a
    large family of acceleration attacks silently find no cards.
    """
    words = set((phrase or "").strip().split())
    type_word = next((word for word in words if getattr(
        PokemonTypes, word.upper(), None) is not None), None)
    ptype = getattr(PokemonTypes, type_word.upper(), None) if type_word else None

    def predicate(card):
        if not is_energy_card(card):
            return False
        if "basic" in words and not is_basic_energy(card):
            return False
        return ptype is None or energy_provides_type(card, ptype.value)

    return predicate


def _ability_hand_discard_cost(text: str):
    """Parse a public hand-discard cost from an activated Ability.

    Imported cards share :func:`bw_legacy_ability`.  The benefit side of the
    wording was historically interpreted independently from its ``if you
    do`` cost, which let several reprints draw, heal or place counters for
    free.  Return ``(count, predicate)`` here; ``count=None`` means the whole
    hand (which is legal even when it is empty).
    """
    if "you may discard your hand" in text:
        return None, (lambda card: True)
    match = re.search(
        r"you may discard (\d+|an?|one) (.+?) from your hand", text,
    )
    if not match:
        return None
    amount_word, descriptor = match.groups()
    count = int(amount_word) if amount_word.isdigit() else 1
    descriptor = re.sub(r"\s+cards?$", "", descriptor.strip())

    if "energy" in descriptor:
        if "special energy" in descriptor:
            predicate = is_special_energy
        else:
            predicate = _energy_phrase_predicate(descriptor)
    elif "ultra beast" in descriptor:
        predicate = lambda card: is_pokemon_card(card) \
            and _has_subtype(card, "Ultra Beast")
    elif "pokémon" in descriptor:
        type_word = next((word for word in (
            "grass", "fire", "water", "lightning", "psychic", "fighting",
            "darkness", "metal", "fairy", "dragon",
        ) if f"{word} pokémon" in descriptor), None)
        ptype = getattr(PokemonTypes, (type_word or "").upper(), None)
        predicate = lambda card, ptype=ptype: is_pokemon_card(card) and (
            ptype is None or _is_type(card, ptype)
        )
    elif descriptor in ("card", "other card"):
        predicate = lambda card: True
    else:
        wanted = descriptor.removesuffix(" card").strip().casefold()
        predicate = lambda card, wanted=wanted: _name(card).casefold() == wanted
    return count, predicate


def _ability_attached_energy_discard_cost(text: str):
    """Parse an Energy-card cost paid from the Ability user's source."""
    match = re.search(
        r"you may discard (\d+|an?|one) "
        r"((?:(?:basic|special|grass|fire|water|lightning|psychic|fighting|"
        r"darkness|metal|fairy) )?energy(?: cards?)?) "
        r"(?:attached to|from) (?:this pokémon|it)",
        text,
    )
    if not match:
        return None
    amount_word, descriptor = match.groups()
    count = int(amount_word) if amount_word.isdigit() else 1
    predicate = is_special_energy if "special energy" in descriptor \
        else _energy_phrase_predicate(descriptor)
    return count, predicate


def _ability_cost_handled_inline(text: str) -> bool:
    """Effects whose bespoke branch already pays its printed cost."""
    return bool(
        ("discard 1 card from your hand" in text and "draw 2 cards" in text)
        or (
            "discard a water energy card from your hand" in text
            and not any(phrase in text for phrase in ("if you do", "in order to"))
        )
        or (
            "discard a basic" in text
            and "attacks used by your pokémon do" in text
        )
        or (
            "discard a water energy card from your hand" in text
            and "your opponent switches their active" in text
        )
        or (
            "discard a special energy from this pokémon" in text
            and "heal 80 damage" in text
        )
    )


async def _pay_shared_ability_discard_cost(ctx, text: str) -> bool:
    """Pay a parsed activated-Ability cost exactly once."""
    if _ability_cost_handled_inline(text):
        return True
    hand_cost = _ability_hand_discard_cost(text)
    if hand_cost is not None:
        count, predicate = hand_cost
        if count is None:
            await ctx.discard_cards(list(ctx.hand()))
            return True
        candidates = [card for card in ctx.hand() if predicate(card)]
        if len(candidates) < count:
            return False
        picked = await ctx.discard_from_hand(
            count, minimum=count, predicate=predicate,
            prompt="Choose cards to discard",
        )
        return len(picked) == count

    attached_cost = _ability_attached_energy_discard_cost(text)
    if attached_cost is not None:
        count, predicate = attached_cost
        candidates = [energy for energy in ctx.attached_energies(ctx.source)
                      if predicate(energy)]
        if len(candidates) < count:
            return False
        picked = await ctx.discard_energy_from(
            ctx.source, count, predicate=predicate, minimum=count,
            prompt="Choose Energy to discard",
        )
        return len(picked) == count
    return True


def _ability_search_count(text: str) -> int:
    """Return the number of cards requested by a deck-search Ability."""
    match = re.search(r"search your deck for (?:up to )?(\d+)", text)
    return int(match.group(1)) if match else 1


def _ability_search_predicate(text: str):
    """Build the recurring card filter used by search-to-hand Abilities.

    This deliberately lives in the shared era interpreter: generated cards
    from XY onward reuse it, and previously every plural search (notably
    Scoundrel Ring) fell through the old singular-only branch as a no-op.
    """
    if "isn't a pokémon-gx or pokémon-ex" in text:
        return lambda card: (
            is_pokemon_card(card)
            and not _pokemon_ex(card)
            and "GX" not in (
                getattr(def_for(card.archetype_id), "subtypes", []) or []
            )
        )

    if "pokémon-ex" in text:
        excluded = None
        match = re.search(r"except for ([^)]+)", text)
        if match:
            excluded = match.group(1).strip().casefold()
        return lambda card: (
            _pokemon_ex(card)
            and (excluded is None or _name(card).casefold() != excluded)
        )

    if "pokémon-gx" in text:
        return lambda card: (
            is_pokemon_card(card)
            and "GX" in (getattr(def_for(card.archetype_id), "subtypes", []) or [])
        )

    if "team plasma card" in text:
        return _team_plasma
    if "team aqua pokémon" in text:
        return lambda card: (
            is_pokemon_card(card)
            and "Team Aqua" in (
                getattr(def_for(card.archetype_id), "subtypes", []) or []
            )
        )

    basic_typed_energy = re.search(
        r"basic (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) energy",
        text,
    )
    if basic_typed_energy:
        energy_type = getattr(PokemonTypes, basic_typed_energy.group(1).upper())
        return lambda card: (
            is_basic_energy(card)
            and energy_provides_type(card, energy_type.value)
        )
    if "basic energy" in text:
        return is_basic_energy
    if "special energy" in text:
        return is_special_energy

    typed_energy = re.search(
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) energy",
        text,
    )
    if typed_energy:
        return _energy_predicate(typed_energy.group(1))
    if "energy card" in text or "energy cards" in text:
        return is_energy_card
    if "pokémon tool" in text:
        return is_pokemon_tool
    if "supporter" in text:
        return is_supporter_card
    if "stadium" in text:
        return lambda card: (
            is_trainer_card(card)
            and "Stadium" in (getattr(def_for(card.archetype_id), "subtypes", []) or [])
        )
    if "item card" in text or "item cards" in text:
        return is_item_card
    if "trainer card" in text or "trainer cards" in text:
        return is_trainer_card

    basic_typed_pokemon = re.search(
        r"basic (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon) pokémon",
        text,
    )
    if basic_typed_pokemon:
        pokemon_type = getattr(PokemonTypes, basic_typed_pokemon.group(1).upper())
        return lambda card: is_basic_pokemon(card) and _is_type(card, pokemon_type)
    typed_pokemon = re.search(
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon) pokémon",
        text,
    )
    if typed_pokemon:
        pokemon_type = getattr(PokemonTypes, typed_pokemon.group(1).upper())
        return lambda card: _is_type(card, pokemon_type)
    if "basic pokémon" in text:
        return is_basic_pokemon
    if "pokémon that has the nuzzle attack" in text:
        return lambda card: is_pokemon_card(card) and _has_attack_named(card, "Nuzzle")
    owner_match = re.search(r"for (?:an? )?((?:ethan|cynthia|erika)'s) pokémon", text)
    if owner_match:
        owner = owner_match.group(1).casefold()
        return lambda card: (
            is_pokemon_card(card)
            and _name(card).casefold().startswith(owner + " ")
        )
    if "pokémon" in text:
        return is_pokemon_card

    named_card = re.search(
        r"search your deck for (?:an?|up to \d+) ([a-z0-9' -]+?) card(?:,| and|\.|$)",
        text,
    )
    if named_card:
        wanted = named_card.group(1).strip().casefold()
        return lambda card: _name(card).casefold() == wanted
    return None


def _attack_discard_predicate(descriptor: str, board=None):
    """Build the public predicate used by recurring attack discard costs.

    Attack text has accumulated many tiny wording variants (``Energy`` vs
    ``Energy cards``, named Pokémon, and retreat-cost filters).  Normalising
    those variants here prevents each new expansion from needing a bespoke
    handler for the same physical action.
    """
    descriptor = _norm(descriptor)
    descriptor = descriptor.replace("[", " ").replace("]", " ")
    descriptor = re.sub(r"\b(?:cards?|as you like)\b", "", descriptor)
    descriptor = re.sub(r"\s+", " ", descriptor).strip()
    retreat = re.search(r"pokémon with a retreat cost of exactly (\d+)", descriptor)
    if retreat:
        wanted = int(retreat.group(1))
        return lambda card: (
            is_pokemon_card(card)
            and effective_retreat_cost(board, card) == wanted
        )
    if "exeggcute" in descriptor:
        return lambda card: _name(card).casefold() == "exeggcute"
    if "team rocket" in descriptor and "supporter" in descriptor:
        return lambda card: (
            is_supporter_card(card)
            and "team rocket" in _name(card).casefold()
        )
    predicate = _ability_search_predicate(descriptor)
    return predicate or (lambda card: True)


async def bw_legacy_attack(ctx):
    """Rules-text interpreter for the recurring BW attack templates.

    It deliberately executes choices on the real board (not dialogs containing
    copies), so it follows the simulator's current interaction convention.
    """
    text = _norm(getattr(ctx.ability, "game_text", ""))
    # The API changed the same rules noun between generations.  Internally we
    # use the historical "Defending Pokémon" phrase so every existing branch
    # also handles modern "your opponent's Active Pokémon" printings.
    # Keep the article when normalising modern wording.  A large part of the
    # historical corpus literally says "the Defending Pokémon"; dropping
    # "the" made otherwise-identical regex families miss only modern cards.
    text = text.replace(
        "your opponent's active pokémon", "the defending pokémon"
    )
    printed = getattr(ctx.ability, "damage", 0) or 0
    primary_damage_dealt = 0

    # Multi-target deck acceleration needs both the printed target count and
    # its distribution rules.  A plain "search ... for a ... Energy" parser
    # sees only one card and loses the preceding Choose-N clause.
    geomancy = re.search(
        r"choose (\d+) of your benched pokémon\. for each of those pokémon, "
        r"search your deck for an? "
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
        r"energy card and attach it to that pokémon",
        text,
    )
    if geomancy:
        remaining = list(ctx.my_bench())
        targets = []
        for _ in range(min(int(geomancy.group(1)), len(remaining))):
            target = remaining[0] if len(remaining) == 1 else \
                await ctx.choose_pokemon(remaining, "Choose a Benched Pokémon")
            if target is None:
                break
            remaining.remove(target)
            targets.append(target)
        ptype = getattr(PokemonTypes, geomancy.group(2).upper())
        picks = await ctx.search_deck(
            lambda card: is_energy_card(card)
            and energy_provides_type(card, ptype.value),
            len(targets), minimum=0, prompt="Choose Energy cards",
        ) if targets else []
        for energy, target in zip(picks, targets):
            await ctx.attach_energy(energy, target)
        await ctx.shuffle_deck()
        return

    if "choose 3 of your pokémon" in text \
            and "a different type of basic energy card" in text \
            and "attach it to that pokémon" in text:
        remaining = list(ctx.my_pokemon_in_play())
        targets = []
        for _ in range(min(3, len(remaining))):
            target = remaining[0] if len(remaining) == 1 else \
                await ctx.choose_pokemon(remaining, "Choose a Pokémon")
            if target is None:
                break
            remaining.remove(target)
            targets.append(target)
        used_types = set()
        for target in targets:
            picks = await ctx.search_deck(
                lambda card, used_types=used_types: is_basic_energy(card)
                and any(
                    energy_type not in used_types
                    for option in energy_provided_options(ctx.board, card)
                    for energy_type in option
                ),
                1, minimum=0,
                prompt="Choose a basic Energy of a different type",
            )
            if not picks:
                continue
            energy = picks[0]
            provided = {
                energy_type
                for option in energy_provided_options(ctx.board, energy)
                for energy_type in option
            }
            used_types.update(provided)
            await ctx.attach_energy(energy, target)
        await ctx.shuffle_deck()
        return

    # Composite attacks whose short secondary clause used to fall through
    # the generic damage parser.  Keep these text-family based so every
    # reprint receives the same complete resolution.
    if "your opponent draws a card" in text:
        if printed:
            await ctx.deal_damage(printed)
        await ctx.draw_cards(1, player_id=ctx.opponent_id)
        return

    # Power Heater-style wording names one Energy per chosen Pokémon.  The
    # ordinary acceleration parser sees the singular "a Fire Energy card" and
    # would otherwise stop after one attachment, ignoring "Choose 2" and
    # "to each".  Resolve the parallel, distinct targets as one composite
    # effect before falling through to that generic branch.
    spread_attach = re.search(
        r"choose (\d+) of your benched pokémon\. attach an? "
        r"(?:(basic) )?"
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
        r"energy card from your (hand|discard pile) to each of those pokémon",
        text,
    )
    if spread_attach:
        if printed:
            await ctx.deal_damage(printed)
        requested = int(spread_attach.group(1))
        basic_only, type_word, zone_name = spread_attach.groups()[1:]
        zone = ctx.hand() if zone_name == "hand" else ctx.discard_pile()
        energies = [card for card in zone if is_energy_card(card)]
        if basic_only:
            energies = [card for card in energies if is_basic_energy(card)]
        if type_word:
            energies = [card for card in energies
                        if energy_provides_type(
                            card, getattr(PokemonTypes, type_word.upper()).value
                        )]
        remaining_targets = list(ctx.my_bench())
        maximum = min(requested, len(energies), len(remaining_targets))
        picks = await ctx.choose_cards(
            energies, maximum, minimum=maximum,
            prompt="Choose Energy cards",
        ) if maximum else []
        for energy in picks:
            target = remaining_targets[0] if len(remaining_targets) == 1 else \
                await ctx.choose_pokemon(
                    remaining_targets, "Choose a Benched Pokémon"
                )
            if target is None:
                break
            remaining_targets.remove(target)
            await ctx.attach_energy(energy, target)
        return

    if "opponent can't play any cards from their hand" in text \
            and "extra psychic energy attached" in text \
            and "each player draws cards until they have 7 cards" in text:
        ctx.lock_plays(ctx.opponent_id, lambda card: True)
        psychic_cost = sum(
            count for energy_type, count in (getattr(ctx.ability, "cost", None) or {}).items()
            if energy_type == PokemonTypes.PSYCHIC
            or energy_type == PokemonTypes.PSYCHIC.value
            or str(energy_type).casefold() == "psychic"
        )
        if _energy_count(ctx, ctx.attacker, "psychic") >= psychic_cost + 1:
            await ctx.draw_until(7, player_id=ctx.player_id)
            await ctx.draw_until(7, player_id=ctx.opponent_id)
        return

    if "attach up to 2 grass energy cards from your hand to your benched pokémon" in text \
            and "heal all damage from that pokémon" in text:
        if printed:
            await ctx.deal_damage(printed)
        energies = [
            card for card in ctx.hand()
            if is_energy_card(card)
            and energy_provides_type(card, PokemonTypes.GRASS.value)
        ]
        maximum = min(2, len(energies))
        picks = await ctx.choose_cards(
            energies, maximum, minimum=0,
            prompt="Choose Grass Energy cards to attach",
        ) if maximum and ctx.my_bench() else []
        healed = {}
        for energy in picks:
            bench = list(ctx.my_bench())
            target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon"
            ) if bench else None
            if target is not None and await ctx.attach_energy(energy, target):
                healed[target.entity_id] = target
        for target in healed.values():
            await ctx.heal(ctx.max_hp(target), target)
        return

    if "attach a basic grass energy card from your hand to 1 of your benched pokémon" in text \
            and "heal all damage from that pokémon" in text:
        if printed:
            await ctx.deal_damage(printed)
        energies = [
            card for card in ctx.hand()
            if is_basic_energy(card)
            and energy_provides_type(card, PokemonTypes.GRASS.value)
        ]
        energy = await _choose_one(ctx, energies, "Choose a Basic Grass Energy") \
            if energies and ctx.my_bench() else None
        bench = list(ctx.my_bench())
        target = bench[0] if energy is not None and len(bench) == 1 else \
            await ctx.choose_pokemon(bench, "Choose a Benched Pokémon") \
            if energy is not None and bench else None
        if target is not None and await ctx.attach_energy(energy, target):
            await ctx.heal(ctx.max_hp(target), target)
        return

    if "attach up to 3 water energy cards from your hand to your pokémon" in text \
            and "heal 50 damage from those pokémon for each card you attached" in text:
        if printed:
            await ctx.deal_damage(printed)
        energies = [
            card for card in ctx.hand()
            if is_energy_card(card)
            and energy_provides_type(card, PokemonTypes.WATER.value)
        ]
        maximum = min(3, len(energies))
        picks = await ctx.choose_cards(
            energies, maximum, minimum=0,
            prompt="Choose Water Energy cards to attach",
        ) if maximum else []
        attached_by_target = {}
        for energy in picks:
            targets = list(ctx.my_pokemon_in_play())
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None and await ctx.attach_energy(energy, target):
                entity_id = target.entity_id
                attached_by_target[entity_id] = (
                    target, attached_by_target.get(entity_id, (None, 0))[1] + 1
                )
        for target, count in attached_by_target.values():
            await ctx.heal(50 * count, target)
        return

    if "move a fairy energy from this pokémon to 1 of your benched pokémon" in text \
            and "heal 50 damage from that pokémon" in text:
        if printed:
            await ctx.deal_damage(printed)
        energies = [
            energy for energy in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(energy, PokemonTypes.FAIRY.value)
        ]
        energy = await _choose_one(ctx, energies, "Choose a Fairy Energy") \
            if energies and ctx.my_bench() else None
        bench = list(ctx.my_bench())
        target = bench[0] if energy is not None and len(bench) == 1 else \
            await ctx.choose_pokemon(bench, "Choose a Benched Pokémon") \
            if energy is not None and bench else None
        if target is not None and await ctx.move_energy(energy, target):
            await ctx.heal(50, target)
        return

    if text.startswith("discard an energy from this pokémon. if you do, switch it with") \
            and "benched pokémon" in text:
        if printed:
            await ctx.deal_damage(printed)
        paid = await ctx.discard_energy_units_from(
            ctx.attacker, 1, partial=False,
        )
        if paid and ctx.my_bench():
            bench = list(ctx.my_bench())
            target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench, "Choose your new Active Pokémon"
            )
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
        return

    moved_energy_damage = re.search(
        r"move any number of (grass|fire|water|lightning|psychic|fighting|"
        r"darkness|metal|fairy) energy from your benched pokémon to this "
        r"pokémon\. this attack does (\d+) damage for each energy card you moved",
        text,
    )
    if moved_energy_damage:
        predicate = _energy_predicate(moved_energy_damage.group(1))
        moved = await ctx.move_energy_freely(
            ctx.my_bench(), [ctx.attacker], predicate=predicate,
            prompt="Choose Energy to move",
        )
        await ctx.deal_damage(int(moved_energy_damage.group(2)) * len(moved))
        return

    if re.search(
        r"choose (?:1 of |an? )?(?:the )?(?:defending pokémon|opponent's active pokémon|"
        r"opponent's pokémon)(?:'s)? (?:non-gx )?attacks? and use it as this attack",
        text,
    ):
        definition = def_for(ctx.defender.archetype_id)
        candidates = [
            (ctx.defender, attack)
            for attack in (getattr(definition, "abilities", None) or [])
            if isinstance(attack, Attack)
        ]
        picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy") \
            if candidates else None
        if picked is not None:
            _, chosen_attack = picked
            await ctx.use_attack(chosen_attack)
        return

    # Copy effects that can inspect every opposing Pokemon, the previous
    # attack, or a revealed slice of the opponent's deck.  These all end by
    # delegating to use_attack so GX/VSTAR limits and nested copy protection
    # remain centralized in the engine.
    if "choose 1 of your opponent's pokémon's attacks and use it as this attack" in text \
            or "choose an attack from 1 of your opponent's pokémon in play" in text:
        candidates = [
            (pokemon, attack)
            for pokemon in ctx.opponent_pokemon_in_play()
            for attack in (getattr(def_for(pokemon.archetype_id), "abilities", None) or [])
            if isinstance(attack, Attack)
        ]
        picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack") \
            if candidates else None
        if picked is not None:
            await ctx.use_attack(picked[1])
        return

    if "opponent chooses an attack from 1 of their pokémon in play" in text:
        candidates = [
            (pokemon, attack)
            for pokemon in ctx.opponent_pokemon_in_play()
            for attack in (getattr(def_for(pokemon.archetype_id), "abilities", None) or [])
            if isinstance(attack, Attack)
        ]
        if candidates:
            index = await ctx.session.prompt_attack_selection(
                ctx.opponent_id, ctx.source, candidates, "Choose an attack"
            )
            if index is not None:
                await ctx.use_attack(candidates[index][1])
        return

    if "used an attack" in text and "during their last turn" in text \
            and "use it as this attack" in text \
            or "used an attack during his or her last turn" in text \
            and "use it as this attack" in text:
        records = list(ctx.session.turn_state.attacks_used_last_turn)
        candidates = []
        for _, archetype_id, attack_title in records:
            definition = def_for(archetype_id)
            attack = next((entry for entry in (
                getattr(definition, "abilities", None) or []
            ) if isinstance(entry, Attack) and entry.title == attack_title), None)
            if attack is not None and not (
                    "isn't a gx attack" in text and getattr(attack, "gx", False)):
                candidates.append((ctx.defender, attack))
        picked = await ctx.choose_attack_to_copy(candidates, "Choose the previous attack") \
            if len(candidates) > 1 else (candidates[0] if candidates else None)
        if picked is not None:
            await ctx.use_attack(picked[1])
        return

    top_attack = re.search(
        r"reveal the top (\d+) cards of your opponent's deck.*"
        r"choose an attack from a pokémon you find there and use it as this attack",
        text,
    )
    if top_attack:
        cards = ctx.deck_top(int(top_attack.group(1)), ctx.opponent_id)
        await ctx.reveal_cards(cards)
        candidates = [
            (card, attack) for card in cards if is_pokemon_card(card)
            for attack in (getattr(def_for(card.archetype_id), "abilities", None) or [])
            if isinstance(attack, Attack)
        ]
        picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack") \
            if candidates else None
        await ctx.shuffle_deck(ctx.opponent_id)
        if picked is not None:
            await ctx.use_attack(picked[1])
        return

    if "choose 1 of this pokémon's attacks from its previous evolutions" in text \
            or "choose an attack from 1 of this pokémon's previous evolutions" in text:
        candidates = [
            (ctx.attacker, attack)
            for previous in full_stack(ctx.attacker)[1:]
            if isinstance(previous, PokemonEntity)
            for attack in (getattr(def_for(previous.archetype_id), "abilities", None) or [])
            if isinstance(attack, Attack)
        ]
        picked = await ctx.choose_attack_to_copy(
            candidates, "Choose an attack from a previous Evolution"
        ) if candidates else None
        if picked is not None:
            await ctx.use_attack(picked[1])
        return

    if "choose a supporter card from your opponent's discard pile and use it" in text:
        candidates = [card for card in ctx.discard_pile(ctx.opponent_id)
                      if is_supporter_card(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a Supporter") \
            if candidates else None
        if chosen is not None:
            await _use_trainer_effect_as_attack(ctx, chosen)
        return

    if "discard a supporter card from your hand. if you do, use the effect" in text:
        candidates = [card for card in ctx.hand() if is_supporter_card(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a Supporter") \
            if candidates else None
        if chosen is not None:
            await ctx.discard_cards([chosen])
            await _use_trainer_effect_as_attack(ctx, chosen)
        return

    if "discard the top card of your deck, and if that card is a supporter card" in text \
            and "use the effect of that card" in text:
        cards = ctx.deck_top(1)
        if cards:
            card = cards[0]
            await ctx.discard_cards([card])
            if is_supporter_card(card):
                await _use_trainer_effect_as_attack(ctx, card)
        return

    if text.startswith("choose 2 cards from your discard pile. then, ask your opponent"):
        cards = list(ctx.discard_pile())
        picks = await ctx.choose_cards(
            cards, min(2, len(cards)), minimum=min(2, len(cards)),
            prompt="Choose 2 cards from your discard pile",
        ) if cards else []
        accepted = await ctx.ask_yes_no(
            "May your opponent put the chosen cards into their hand?",
            player_id=ctx.opponent_id,
        )
        if accepted:
            await ctx.put_in_hand(picks, reveal=True)
        else:
            await ctx.deal_damage(80)
        return

    if text.startswith("each player may attach up to 3 basic energy cards from their hand"):
        for player_id in (ctx.opponent_id, ctx.player_id):
            hand = list(ctx.hand(player_id))
            candidates = [card for card in hand if is_basic_energy(card)]
            picks = await ctx.choose_cards(
                candidates, min(3, len(candidates)), minimum=0,
                prompt="Choose Basic Energy cards to attach",
                player_id=player_id,
            ) if candidates else []
            for energy in picks:
                targets = list(ctx.board.pokemon_in_play(player_id))
                target = await ctx.choose_pokemon(
                    targets, "Choose a Pokémon", player_id=player_id,
                ) if targets else None
                if target is not None:
                    await ctx.attach_energy(energy, target)
        return

    # Mega Audino ex: each heads authorizes up to two independently placed
    # Basic Energy.  Search once so the private-zone chooser can select the
    # whole result, then let the player distribute the cards one by one.
    if text.startswith("flip 3 coins. for each heads, search your deck for up to 2 basic energy"):
        heads = sum(await ctx.flip_coins(3, ctx.ability.title))
        maximum = heads * 2
        picks = await ctx.search_deck(
            is_basic_energy, maximum, minimum=0,
            prompt="Choose Basic Energy cards to attach",
        ) if maximum else []
        for energy in picks:
            targets = list(ctx.my_pokemon_in_play())
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
        await ctx.shuffle_deck()
        return

    # Disaster Shock's optional rider is independent of the base damage but
    # requires the full printed two-Lightning payment.
    optional_paralysis = re.search(
        r"you may discard (\d+) lightning energy from this pokémon and make "
        r"(?:the defending|your opponent's active) pokémon paralyzed", text,
    )
    if optional_paralysis:
        await ctx.deal_damage(printed)
        required = int(optional_paralysis.group(1))
        available = _energy_count(ctx, ctx.attacker, "lightning")
        if available >= required and await ctx.ask_yes_no(
                "Discard Lightning Energy to Paralyze the Defending Pokémon?"):
            paid = await ctx.discard_energy_units_from(
                ctx.attacker, required,
                predicate=lambda energy: energy_provides_type(
                    energy, PokemonTypes.LIGHTNING.value
                ),
                partial=False,
            )
            if paid:
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.PARALYZED
                )
        return

    if "attach any number of metal energy cards from your discard pile to this pokémon" in text:
        candidates = [card for card in ctx.discard_pile()
                      if is_energy_card(card)
                      and energy_provides_type(card, PokemonTypes.METAL.value)]
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose Metal Energy cards to attach",
        ) if candidates else []
        for energy in picks:
            await ctx.attach_energy(energy, ctx.attacker)
        return

    if text.startswith("discard all energy attached to entei & raikou legend"):
        await ctx.discard_cards(list(ctx.attached_energies(ctx.attacker)))
        pool = list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play())
        for target in [pokemon for pokemon in pool if _has_pokemon_ability(pokemon)]:
            await ctx.deal_damage(
                80, target=target, apply_modifiers=False,
                ignore_weakness=True, ignore_resistance=True,
            )
        return

    if text.startswith("discard the top 5 cards from your opponent's deck") \
            and "damage times the number of energy cards you discarded" in text:
        cards = ctx.deck_top(5, ctx.opponent_id)
        energy_count = sum(is_energy_card(card) for card in cards)
        await ctx.discard_cards(cards)
        for target in list(ctx.opponent_bench()):
            await ctx.deal_damage(
                30 * energy_count, target=target, apply_modifiers=False,
            )
        return

    if text.startswith("discard 2 energy from this pokémon") \
            and "if you discarded any energy in this way" in text \
            and "shuffles their active pokémon" in text:
        paid = await ctx.discard_energy_units_from(
            ctx.attacker, 2, partial=True
        )
        if paid:
            await ctx.shuffle_into_deck(
                full_stack(ctx.defender), player_id=ctx.opponent_id
            )
        return

    if "put damage counters on the defending pokémon until its remaining hp is 10" in text \
            and "this attack also does 120 damage to this pokémon" in text:
        old_counters = _damage_counter_count(ctx, ctx.defender)
        new_counters = max(0, (ctx.max_hp(ctx.defender) - 10) // 10)
        await ctx.set_damage_counters(ctx.defender, new_counters)
        if new_counters > old_counters:
            await ctx.deal_damage(
                120, target=ctx.attacker, apply_modifiers=False
            )
        return

    if text.startswith("take another turn after this one"):
        ctx.take_extra_turn()
        if "at least 14 extra fairy energy attached" in text:
            cost = sum((getattr(ctx.ability, "cost", None) or {}).values())
            if _energy_count(ctx, ctx.attacker, "fairy") - cost >= 14:
                for target in list(ctx.opponent_bench()):
                    await ctx.shuffle_into_deck(
                        full_stack(target), player_id=ctx.opponent_id
                    )
        return

    if text.startswith("discard an energy from this pokémon. if you do, switch all damage counters"):
        paid = await ctx.discard_energy_units_from(
            ctx.attacker, 1, partial=False
        )
        if paid:
            attacker_count = _damage_counter_count(ctx, ctx.attacker)
            defender_count = _damage_counter_count(ctx, ctx.defender)
            await ctx.set_damage_counters(ctx.attacker, defender_count)
            await ctx.set_damage_counters(ctx.defender, attacker_count)
        return

    dual_tail = re.search(
        r"discard 2 energy from this pokémon, and this attack does (\d+) "
        r"damage to each of 2 of your opponent's pokémon", text,
    )
    if dual_tail:
        await ctx.discard_energy_units_from(ctx.attacker, 2, partial=True)
        targets = list(ctx.opponent_pokemon_in_play())
        picks = await ctx.choose_cards(
            targets, min(2, len(targets)), minimum=min(2, len(targets)),
            prompt="Choose 2 Pokémon to damage",
        ) if targets else []
        for target in picks:
            await ctx.deal_damage(
                int(dual_tail.group(1)), target=target,
                apply_modifiers=(target is ctx.defender),
                ignore_weakness=True, ignore_resistance=True,
            )
        return

    # Rayquaza-EX's Dragon Burst is a choice between two complete groups,
    # not an ordinary one-Energy after-effect.  Selecting any eligible card
    # chooses that type; every Basic Energy card of that type is discarded.
    if getattr(ctx.ability, "title", "") == "Dragon Burst":
        eligible = [
            energy for energy in ctx.attached_energies(ctx.attacker)
            if is_basic_energy(energy) and (
                energy_provides_type(energy, PokemonTypes.FIRE.value)
                or energy_provides_type(energy, PokemonTypes.LIGHTNING.value)
            )
        ]
        if not eligible:
            return
        chosen = await _choose_one(
            ctx, eligible,
            "Choose Fire or Lightning Energy to discard for Dragon Burst",
        )
        chosen_type = (
            PokemonTypes.FIRE if energy_provides_type(chosen, PokemonTypes.FIRE.value)
            else PokemonTypes.LIGHTNING
        )
        discarded = [
            energy for energy in eligible
            if energy_provides_type(energy, chosen_type.value)
        ]
        await ctx.discard_cards(discarded)
        await ctx.deal_damage(60 * len(discarded))
        return

    # Burst of Braying puts a variable number before "up to" rather than
    # after it, so it is intentionally separate from the ordinary
    # ``attach up to N`` parser below.
    if "choose basic lightning energy cards from your discard pile up to the " \
            "number of prize cards your opponent has taken" in text:
        requested = ctx.prizes_taken(ctx.opponent_id)
        candidates = [
            card for card in ctx.discard_pile()
            if is_basic_energy(card)
            and energy_provides_type(card, PokemonTypes.LIGHTNING.value)
        ]
        maximum = min(requested, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose Lightning Energy cards",
        ) if maximum else []
        for energy in picks:
            targets = list(ctx.my_pokemon_in_play())
            target = targets[0] if len(targets) == 1 else \
                await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
        return

    # A mandatory discard followed by "If you can't ... does nothing" is a
    # real precondition (Plasma Gale and its relatives), so pay it before the
    # damage instead of applying the generic after-effect below.
    prepaid_discard = False
    required = re.search(
        r"discard (\d+|an|a) ([a-z]+ )?energy attached to this pokémon\..*"
        r"if you can't discard", text,
    )
    if required:
        count = 1 if required.group(1) in ("a", "an") else int(required.group(1))
        kind = (required.group(2) or "").strip()
        if kind == "plasma":
            candidates = [e for e in ctx.attached_energies(ctx.attacker)
                          if _name(e) == "Plasma Energy"]
            if len(candidates) < count:
                return
            paid = await ctx.discard_energy_from(
                ctx.attacker, count, predicate=lambda e: _name(e) == "Plasma Energy")
        else:
            ptype = getattr(PokemonTypes, kind.upper(), None) if kind else None
            pred = (lambda e: energy_provides_type(e, ptype.value)) if ptype else None
            paid = await ctx.discard_energy_units_from(
                ctx.attacker, count, predicate=pred)
        if not paid:
            return
        prepaid_discard = True

    # Coin families determine damage before any riders.
    heads: Optional[int] = None
    coin_count = None
    m = re.search(r"flip (?:a|1) coin", text)
    if m:
        coin_count = 1
    m = re.search(r"flip (\d+) coins", text)
    if m:
        coin_count = int(m.group(1))
    if "flip a coin for each energy attached to this pokémon" in text:
        coin_count = _energy_count(ctx, ctx.attacker)
    # A few legacy exports lost the leading "Flip a coin." sentence while
    # retaining an otherwise impossible heads/tails clause (for example COL
    # Flaaffy's Thundershock).  The clause itself proves that one flip exists.
    if coin_count is None and ("if heads" in text or "if tails" in text):
        coin_count = 1
    if coin_count is not None:
        results = await ctx.flip_coins(coin_count, ctx.ability.title)
        heads = sum(bool(r) for r in results)

    if "choose 3 random cards from your opponent's hand" in text \
            and "shuffles them into his or her deck" in text:
        if heads:
            hand = list(ctx.hand(ctx.opponent_id))
            chosen = random.sample(hand, min(3, len(hand)))
            if chosen:
                await ctx.reveal_cards(chosen)
                await ctx.shuffle_into_deck(chosen, player_id=ctx.opponent_id)
        return

    pre_switched_opponent = False
    if "before doing damage, have your opponent switch" in text \
            and ctx.opponent_bench():
        target = await ctx.choose_pokemon(
            ctx.opponent_bench(), "Choose your new Active Pokémon",
            player_id=ctx.opponent_id,
        )
        if target is not None and await ctx.switch_active(ctx.opponent_id, target):
            pre_switched_opponent = True

    # Variable Lost Zone payments determine the attack's damage, so resolve
    # the player's board selection before the ordinary damage pipeline.
    lost_energy_damage = re.search(
        r"put (?:as many|any amount of) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal) )?"
        r"energy(?: cards?)? attached to your pokémon(?: as you like)? in the "
        r"lost zone.*?does (\d+) damage (?:times the (?:amount|number)|for each)",
        text,
    )
    if lost_energy_damage:
        type_word, per = lost_energy_damage.groups()
        predicate = _energy_predicate(type_word) if type_word else is_energy_card
        candidates = [
            energy for pokemon in ctx.my_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon) if predicate(energy)
        ]
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose Energy cards to put in the Lost Zone",
        ) if candidates else []
        if picks:
            await ctx.move_to_lost_zone(picks)
        await ctx.deal_damage(int(per) * len(picks))
        return

    shuffle_energy_damage = re.search(
        r"(?:choose as many|shuffle any amount of) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal) )?"
        r"energy (?:attached to|from) your pokémon(?: as you like)?.*?"
        r"this attack does (\d+) damage (?:times the number|for each)", text,
    )
    if shuffle_energy_damage:
        type_word, per = shuffle_energy_damage.groups()
        predicate = _energy_predicate(type_word) if type_word else is_energy_card
        candidates = [
            energy for pokemon in ctx.my_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon) if predicate(energy)
        ]
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose Energy cards to shuffle into your deck",
        ) if candidates else []
        if picks:
            await ctx.shuffle_into_deck(picks)
        await ctx.deal_damage(int(per) * len(picks))
        return

    pre_damage_override = None
    pre_damage_bonus = 0
    prepaid_top_discard = False
    hand_discard_paid = False
    optional_source_paid = False

    # Variable discard attacks must select and move the cards before damage:
    # the number actually discarded is part of the damage formula.
    variable_hand_discard = re.search(
        r"(?:you may )?discard (?:(up to) (\d+)|(any number of|as many)) "
        r"(.+?) from your hand[,.].*?this attack does (\d+) (more )?damage",
        text,
    )
    if variable_hand_discard:
        _, raw_max, _, descriptor, raw_per, more = \
            variable_hand_discard.groups()
        predicate = _attack_discard_predicate(descriptor, ctx.board)
        candidates = [card for card in ctx.hand() if predicate(card)]
        maximum = min(int(raw_max), len(candidates)) if raw_max else len(candidates)
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose cards to discard",
        ) if maximum else []
        if picks:
            await ctx.discard_cards(picks)
            hand_discard_paid = True
        per = int(raw_per)
        count = len(picks)
        if "for each type of basic energy" in text:
            represented = set()
            for energy in picks:
                for option in energy_provided_options(ctx.board, energy):
                    represented.update(option)
            count = len(represented)
        if "damage to 1 of your opponent's pokémon for each" in text:
            targets = list(ctx.opponent_pokemon_in_play())
            target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if targets else None
            if target is not None:
                await ctx.deal_damage(
                    per * count, target=target,
                    apply_modifiers=(target is ctx.defender),
                    ignore_weakness=target is not ctx.defender,
                    ignore_resistance=target is not ctx.defender,
                )
            return
        if more:
            pre_damage_bonus += per * count
        else:
            pre_damage_override = per * count
        if "draw that many cards" in text and picks:
            await ctx.draw_cards(len(picks))
        heal_per = re.search(
            r"heal (\d+) damage from this pokémon for each card you discarded",
            text,
        )
        if heal_per and picks:
            await ctx.heal(int(heal_per.group(1)) * len(picks), ctx.attacker)

    variable_board_discard = re.search(
        r"(?:you may )?discard (?:(up to) (\d+)|(any amount of|as many)) "
        r"(.*?energy(?: cards?)?) (?:attached to|from(?: among)?) "
        r"(this pokémon|your pokémon|your benched pokémon)(?: as you like)?"
        r"[,.].*?this attack does (\d+) (more )?damage",
        text,
    )
    if variable_board_discard:
        _, raw_max, _, descriptor, zone, raw_per, more = \
            variable_board_discard.groups()
        predicate = _attack_discard_predicate(descriptor, ctx.board)
        holders = [ctx.attacker] if zone == "this pokémon" else \
            list(ctx.my_bench()) if zone == "your benched pokémon" else \
            list(ctx.my_pokemon_in_play())
        candidates = [energy for pokemon in holders
                      for energy in ctx.attached_energies(pokemon)
                      if predicate(energy)]
        maximum = min(int(raw_max), len(candidates)) if raw_max else len(candidates)
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose Energy cards to discard",
        ) if maximum else []
        if picks:
            await ctx.discard_cards(picks)
        if zone == "this pokémon":
            prepaid_discard = True
        per = int(raw_per)
        if more:
            pre_damage_bonus += per * len(picks)
        else:
            pre_damage_override = per * len(picks)

    all_source_formula = re.search(
        r"discard all (basic )?"
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
        r"energy from this pokémon\. this attack does (\d+) more damage for "
        r"each card you discarded", text,
    )
    if all_source_formula:
        require_basic, type_word, raw_per = all_source_formula.groups()
        cards = list(ctx.attached_energies(ctx.attacker))
        if require_basic:
            cards = [card for card in cards if is_basic_energy(card)]
        if type_word:
            cards = [card for card in cards if _energy_predicate(type_word)(card)]
        if cards:
            await ctx.discard_cards(cards)
        pre_damage_bonus += int(raw_per) * len(cards)
        prepaid_discard = True

    variable_bench_discard = re.search(
        r"discard (?:any number of|as many of) your benched pokémon(?: as you like)?\. "
        r"this attack does (\d+) more damage for each", text,
    )
    if variable_bench_discard:
        bench = list(ctx.my_bench())
        picks = await ctx.choose_cards(
            bench, len(bench), minimum=0,
            prompt="Choose Benched Pokémon to discard",
        ) if bench else []
        for pokemon in picks:
            await ctx.discard_cards(full_stack(pokemon))
        pre_damage_bonus += int(variable_bench_discard.group(1)) * len(picks)

    # Top-deck mills whose composition determines damage (Eruption, Hard
    # Crush, Thumpalanche, etc.).  Keep the viewed batch stable until both the
    # damage count and every follow-up movement have been derived from it.
    top_formula = re.search(
        r"(?:you may )?discard the top (?:(\d+) cards?|card) (?:from|of) "
        r"your deck.*?this attack does (\d+) (more )?damage", text,
    )
    if top_formula:
        allowed = not text.startswith("you may discard") or \
            await ctx.ask_yes_no("Discard the top cards of your deck?")
        cards = ctx.deck_top(int(top_formula.group(1) or 1)) if allowed else []
        if cards:
            await ctx.discard_cards(cards)
        prepaid_top_discard = True
        if "supporter" in text:
            matching = [card for card in cards if is_supporter_card(card)]
        elif "pokémon with a retreat cost of exactly" in text:
            predicate = _attack_discard_predicate(
                re.search(r"pokémon with a retreat cost of exactly \d+", text).group(0),
                ctx.board,
            )
            matching = [card for card in cards if predicate(card)]
        elif "pokémon" in text and "energy" not in text:
            matching = [card for card in cards if is_pokemon_card(card)]
        elif "basic water energy" in text:
            matching = [card for card in cards
                        if is_basic_energy(card)
                        and energy_provides_type(card, PokemonTypes.WATER.value)]
        else:
            matching = [card for card in cards if is_energy_card(card)]
        value = int(top_formula.group(2)) * len(matching)
        if top_formula.group(3):
            pre_damage_bonus += value
        else:
            pre_damage_override = value

    paired_top_formula = re.search(
        r"(?:you may )?discard the top (?:(\d+) cards?|card) of each player's deck.*?"
        r"this attack does (\d+) more damage for each energy card", text,
    )
    if paired_top_formula:
        allowed = not text.startswith("you may discard") or \
            await ctx.ask_yes_no("Discard the top card of each deck?")
        cards = []
        if allowed:
            count = int(paired_top_formula.group(1) or 1)
            cards = ctx.deck_top(count) + ctx.deck_top(count, ctx.opponent_id)
            await ctx.discard_cards(cards)
        pre_damage_bonus += int(paired_top_formula.group(2)) * sum(
            is_energy_card(card) for card in cards
        )

    fixed_hand_discard = re.search(
        r"(?:^|\. )discard (\d+|an|a) (.+?) from your hand", text,
    )
    if fixed_hand_discard and not variable_hand_discard:
        count = 1 if fixed_hand_discard.group(1) in ("a", "an") \
            else int(fixed_hand_discard.group(1))
        descriptor = fixed_hand_discard.group(2)
        predicate = _attack_discard_predicate(descriptor, ctx.board)
        candidates = [card for card in ctx.hand() if predicate(card)]
        if len(candidates) < count and "if you can't" in text:
            return
        count = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, count, minimum=count, prompt="Choose cards to discard",
        ) if count else []
        if picks:
            await ctx.discard_cards(picks)
            hand_discard_paid = True

    optional_hand_discard = re.search(
        r"you may discard (an|a) (.+?) from your hand\. if you do, "
        r"this attack does (\d+) (more )?damage", text,
    )
    if optional_hand_discard:
        predicate = _attack_discard_predicate(
            optional_hand_discard.group(2), ctx.board,
        )
        candidates = [card for card in ctx.hand() if predicate(card)]
        chosen = await _choose_one(
            ctx, candidates, "Choose a card to discard", optional=True,
        ) if candidates else None
        if chosen is not None:
            await ctx.discard_cards([chosen])
            hand_discard_paid = True
            value = int(optional_hand_discard.group(3))
            if "damage to 1 of your opponent's pokémon" in text:
                targets = list(ctx.opponent_pokemon_in_play())
                target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                    if targets else None
                if target is not None:
                    await ctx.deal_damage(
                        value, target=target,
                        apply_modifiers=(target is ctx.defender),
                        ignore_weakness=target is not ctx.defender,
                        ignore_resistance=target is not ctx.defender,
                    )
                return
            if optional_hand_discard.group(4):
                pre_damage_bonus += value
            else:
                pre_damage_override = value

    optional_source_discard = re.search(
        r"you may discard (an|a) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
        r"energy from this pokémon\. if you do,", text,
    )
    if optional_source_discard:
        predicate = _energy_predicate(optional_source_discard.group(2)) \
            if optional_source_discard.group(2) else is_energy_card
        candidates = [energy for energy in ctx.attached_energies(ctx.attacker)
                      if predicate(energy)]
        if candidates and await ctx.ask_yes_no("Discard Energy for the extra effect?"):
            paid = await ctx.discard_energy_from(
                ctx.attacker, 1, predicate=predicate,
            )
            optional_source_paid = bool(paid)
            if optional_source_paid:
                extra = re.search(r"this attack does (\d+) more damage", text)
                if extra:
                    pre_damage_bonus += int(extra.group(1))
        prepaid_discard = True

    optional_all_source = re.search(
        r"you may discard all "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
        r"energy from this pokémon(?:\. if you do,| and have)", text,
    )
    if optional_all_source:
        predicate = _energy_predicate(optional_all_source.group(1)) \
            if optional_all_source.group(1) else is_energy_card
        candidates = [energy for energy in ctx.attached_energies(ctx.attacker)
                      if predicate(energy)]
        if candidates and await ctx.ask_yes_no("Discard all Energy for more damage?"):
            await ctx.discard_cards(candidates)
            optional_source_paid = True
            extra = re.search(r"(?:does|do) (\d+) more damage", text)
            if extra:
                pre_damage_bonus += int(extra.group(1))
        prepaid_discard = True

    named_variable_source = re.search(
        r"you may discard any number of "
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
        r"energy cards attached to ([a-z0-9 &'’-]+)\. if you do\s*,? this attack "
        r"does \d+ damage plus (\d+) more damage for each", text,
    )
    if named_variable_source and named_variable_source.group(2).casefold() \
            == _name(ctx.attacker).casefold():
        predicate = _energy_predicate(named_variable_source.group(1))
        candidates = [energy for energy in ctx.attached_energies(ctx.attacker)
                      if predicate(energy)]
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose Energy cards to discard",
        ) if candidates else []
        if picks:
            await ctx.discard_cards(picks)
            pre_damage_bonus += int(named_variable_source.group(3)) * len(picks)
        prepaid_discard = True

    variable_hand_utility = re.search(
        r"discard as many cards as you like from your hand", text,
    )
    if variable_hand_utility and not variable_hand_discard:
        hand = list(ctx.hand())
        picks = await ctx.choose_cards(
            hand, len(hand), minimum=0, prompt="Choose cards to discard",
        ) if hand else []
        if picks:
            await ctx.discard_cards(picks)
            hand_discard_paid = True
        if "draw that many cards" in text and picks:
            await ctx.draw_cards(len(picks))
        heal_per = re.search(
            r"heal (\d+) damage from this pokémon for each card you discarded",
            text,
        )
        if heal_per and picks:
            await ctx.heal(int(heal_per.group(1)) * len(picks), ctx.attacker)

    if "discard your hand" in text and not variable_hand_discard:
        allowed = not "you may discard your hand" in text or \
            await ctx.ask_yes_no("Discard your hand?")
        hand = list(ctx.hand()) if allowed else []
        if hand:
            await ctx.discard_cards(hand)
            hand_discard_paid = True
            bonus_match = re.search(
                r"if you discarded any cards in this way, this attack does (\d+) more damage",
                text,
            )
            if bonus_match:
                pre_damage_bonus += int(bonus_match.group(1))

    reveal_from_hand = re.search(
        r"reveal any number of (.+?) (?:from|in) your hand.*?this attack does "
        r"(\d+) damage for each card you revealed", text,
    )
    if reveal_from_hand:
        descriptor = reveal_from_hand.group(1)
        if all(name in descriptor for name in ("honedge", "doublade", "aegislash")):
            wanted = {"honedge", "doublade", "aegislash"}
            predicate = lambda card: _name(card).casefold() in wanted
        elif "moomoo milk" in descriptor:
            predicate = lambda card: _name(card).casefold() == "moomoo milk"
        else:
            predicate = _attack_discard_predicate(descriptor, ctx.board)
        candidates = [card for card in ctx.hand() if predicate(card)]
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose cards to reveal",
        ) if candidates else []
        if picks:
            await ctx.reveal_cards(picks)
        pre_damage_override = int(reveal_from_hand.group(2)) * len(picks)

    if "each player reveals his or her hand" in text \
            and "number of item cards revealed" in text:
        mine = await ctx.reveal_hand(ctx.player_id, ctx.opponent_id)
        theirs = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        per_match = re.search(r"does (\d+) damage times", text)
        pre_damage_override = int(per_match.group(1)) * sum(
            is_item_card(card) for card in mine + theirs
        ) if per_match else 0

    reveal_top_formula = re.search(
        r"reveal the top (\d+) cards of your deck\. this attack does "
        r"(\d+) (more )?damage (?:times .*?|for each) "
        r"(future card|water energy|energy card)", text,
    )
    if reveal_top_formula:
        count, raw_per, more, descriptor = reveal_top_formula.groups()
        viewed = ctx.deck_top(int(count))
        if viewed:
            await ctx.reveal_cards(viewed)
        if descriptor == "future card":
            matching = [card for card in viewed
                        if "Future" in (subtypes_for(card.archetype_id) or [])]
        elif descriptor == "water energy":
            matching = [card for card in viewed
                        if is_energy_card(card) and energy_provides_type(
                            card, PokemonTypes.WATER.value)]
        else:
            matching = [card for card in viewed if is_energy_card(card)]
        value = int(raw_per) * len(matching)
        if "damage to 1 of your opponent's pokémon" in text:
            targets = list(ctx.opponent_pokemon_in_play())
            target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if targets else None
            if target is not None:
                await ctx.deal_damage(
                    value, target=target,
                    apply_modifiers=(target is ctx.defender),
                    ignore_weakness=target is not ctx.defender,
                    ignore_resistance=target is not ctx.defender,
                )
        elif more:
            pre_damage_bonus += value
        else:
            pre_damage_override = value

        if "shuffle those energy cards back into your deck and discard the other" in text:
            await ctx.shuffle_into_deck(matching)
            await ctx.discard_cards([card for card in viewed if card not in matching])
        elif "discard those future cards and shuffle the other" in text:
            await ctx.discard_cards(matching)
            leftovers = [card for card in viewed if card not in matching]
            if leftovers:
                await ctx.shuffle_into_deck(leftovers)
        elif "discard those energy cards and shuffle the other" in text:
            await ctx.discard_cards(matching)
            leftovers = [card for card in viewed if card not in matching]
            if leftovers:
                await ctx.shuffle_into_deck(leftovers)
        elif "shuffle the revealed cards back into your deck" in text:
            await ctx.shuffle_into_deck(viewed)
        if "damage to 1 of your opponent's pokémon" in text:
            return

    whirltide = re.search(
        r"reveal the top (\d+) cards of your deck\. this attack does (\d+) "
        r"damage to 1 of your opponent's pokémon for each energy card", text,
    )
    if whirltide:
        viewed = ctx.deck_top(int(whirltide.group(1)))
        if viewed:
            await ctx.reveal_cards(viewed)
        energies = [card for card in viewed if is_energy_card(card)]
        targets = list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if targets else None
        if target is not None:
            await ctx.deal_damage(
                int(whirltide.group(2)) * len(energies), target=target,
                apply_modifiers=(target is ctx.defender),
                ignore_weakness=target is not ctx.defender,
                ignore_resistance=target is not ctx.defender,
            )
        await ctx.discard_cards(energies)
        leftovers = [card for card in viewed if card not in energies]
        if leftovers:
            await ctx.shuffle_into_deck(leftovers)
        return

    amount = _formula_damage(ctx, text)
    if "this pokémon was damaged by an attack during your opponent's last turn" in text \
            and "does the same amount of damage" in text:
        amount = ctx.damage_taken_last_turn(ctx.attacker)
    if heads is not None:
        m = re.search(r"does (\d+) damage times the number of heads", text)
        if m:
            amount = int(m.group(1)) * heads
        m = re.search(r"does (\d+) more damage for each heads", text)
        if m:
            amount = printed + int(m.group(1)) * heads
        if "if both of them are tails, this attack does nothing" in text \
                and heads == 0:
            amount = 0
        if "if tails, this attack does nothing" in text and heads == 0:
            amount = 0
        m = re.search(r"if heads, this attack does (\d+) more damage", text)
        if m and heads:
            amount = (printed if amount is None else amount) + int(m.group(1))

    # Common conditional bonuses.
    if amount is None:
        amount = printed
    if pre_damage_override is not None:
        amount = pre_damage_override
    amount += pre_damage_bonus
    # Conditional damage clauses shared by many otherwise-simple attacks.
    bonus_match = re.search(r"this attack does (\d+) more damage", text)
    bonus = int(bonus_match.group(1)) if bonus_match else 0
    defender_types = set(effective_pokemon_types(ctx.board, ctx.defender)) \
        if ctx.defender is not None else set()
    if bonus and "defending pokémon is a pokémon-ex" in text \
            and _pokemon_ex(ctx.defender):
        amount += bonus
    if bonus and "defending pokémon is a tera pokémon" in text \
            and "Tera" in (subtypes_for(ctx.defender.archetype_id) or []):
        amount += bonus
    if bonus and "this pokémon has fewer remaining hp than the defending pokémon" in text \
            and ctx.attacker.get_attribute(AttrID.HP, 0) < ctx.defender.get_attribute(AttrID.HP, 0):
        amount += bonus
    for word, ptype in (
        ("grass", PokemonTypes.GRASS), ("fire", PokemonTypes.FIRE),
        ("water", PokemonTypes.WATER), ("lightning", PokemonTypes.LIGHTNING),
        ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
        ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
        ("colorless", PokemonTypes.COLORLESS), ("dragon", PokemonTypes.DRAGON),
    ):
        if bonus and f"defending pokémon is a {word} pokémon" in text \
                and ptype.value in defender_types:
            amount += bonus
    if bonus and "has any plasma energy attached to it" in text \
            and _has_plasma_energy(ctx, ctx.attacker):
        # If the bonus is itself "for each", _formula_damage already included
        # it and only needed this gate.
        if "more damage for each" not in text:
            amount += bonus
    elif "has any plasma energy attached to it" in text \
            and "more damage for each" in text:
        amount = printed
    if bonus and "has a pokémon tool card attached to it" in text \
            and _has_tool(ctx.attacker):
        amount += bonus
    if bonus and "has a special energy attached to it" in text \
            and any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        amount += bonus
    if bonus and "more cards in your hand than your opponent" in text \
            and ctx.hand_size() > ctx.hand_size(ctx.opponent_id):
        amount += bonus
    if bonus and "same number of cards in your hand as your opponent" in text \
            and ctx.hand_size() == ctx.hand_size(ctx.opponent_id):
        amount += bonus
    if bonus and ("stadium card in play" in text or "stadium is in play" in text) \
            and ctx.stadium_in_play() is not None:
        amount += bonus
    if bonus and "defending pokémon has any resistance" in text \
            and ctx.defender.get_attribute(AttrID.RESISTANCE_TYPES):
        amount += bonus
    if bonus:
        named = re.search(r"if ([a-z0-9 .'-]+) is on your bench", text)
        if named and any(_name(p).casefold() == named.group(1).strip().casefold()
                         for p in ctx.my_bench()):
            amount += bonus
    if bonus:
        typed_bench = re.search(r"if you have any (\w+) pokémon on your bench", text)
        if typed_bench:
            bench_type = getattr(PokemonTypes, typed_bench.group(1).upper(), None)
            if bench_type is not None and any(
                    bench_type.value in effective_pokemon_types(ctx.board, p)
                    for p in ctx.my_bench()):
                amount += bonus

    optional_recoil = re.search(
        r"you may do (\d+) more damage\. if you do, this pokémon does (\d+) damage to itself",
        text,
    )
    optional_recoil_taken = False
    if optional_recoil and await ctx.ask_yes_no(
            f"Add {optional_recoil.group(1)} damage?"):
        amount += int(optional_recoil.group(1))
        optional_recoil_taken = True

    discard_all_bonus = re.search(
        r"you may discard all (\w+) energy attached to this pokémon\. "
        r"if you do, this attack does (\d+) more damage", text,
    )
    if discard_all_bonus and not prepaid_discard and await ctx.ask_yes_no(
            f"Discard all {discard_all_bonus.group(1).title()} Energy for more damage?"):
        ptype = getattr(PokemonTypes, discard_all_bonus.group(1).upper(), None)
        cards = [e for e in ctx.attached_energies(ctx.attacker)
                 if ptype is not None and energy_provides_type(e, ptype.value)]
        await ctx.discard_cards(cards)
        amount += int(discard_all_bonus.group(2))
    if "if the defending pokémon already has any damage counters" in text \
            and _damage_counter_count(ctx, ctx.defender):
        bonus = re.search(r"this attack does (\d+) more damage", text)
        if bonus:
            amount += int(bonus.group(1))
    if "if the defending pokémon is affected by a special condition" in text \
            and ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS):
        bonus = re.search(r"this attack does (\d+) more damage", text)
        if bonus:
            amount += int(bonus.group(1))
    if "were knocked out by damage from an opponent's attack" in text \
            and ctx.kos_suffered_last_turn() > 0:
        bonus = re.search(r"this attack does (\d+) more damage", text)
        if bonus:
            amount += int(bonus.group(1))

    # A printed damage value always hits the Active.  Many BW attacks then
    # snipe the Bench as a second hit (Night Spear, Rock Slide, Heavy Bullet).
    snipe = re.search(r"does (\d+) damage to (\d+|1) of your opponent's (benched )?pokémon", text)
    targeted_only = bool(
        snipe and not snipe.group(3)
        and text.startswith(("does ", "this attack does "))
        and printed == int(snipe.group(1))
    )
    switch_damage = re.search(
        r"(?:this attack does|if you do, this attack does) (\d+) damage to the new active pokémon",
        text,
    )
    if switch_damage:
        # The printed number belongs to the promoted target, not the Pokémon
        # that was Defending when the attack was declared.
        amount = 0
    if amount > 0 and not targeted_only:
        ignore_wr = "isn't affected by weakness or resistance" in text
        ignore_all = "or any other effects on the defending pokémon" in text
        primary_damage_dealt = await ctx.deal_damage(
            amount, ignore_weakness=ignore_wr,
            ignore_resistance=ignore_wr,
            ignore_target_effects=ignore_all,
        )
    snipe_allowed = snipe is not None
    if snipe_allowed and heads == 0 and "attack does nothing" in text:
        snipe_allowed = False
    if snipe_allowed and "if heads, this attack does" in text and not heads:
        snipe_allowed = False
    if snipe_allowed:
        damage, count = int(snipe.group(1)), int(snipe.group(2))
        pool = ctx.opponent_bench() if snipe.group(3) else ctx.opponent_pokemon_in_play()
        if "that has any damage counters" in text:
            pool = [p for p in pool if _damage_counter_count(ctx, p) > 0]
        snipe_scale = re.search(
            r"for each (grass|fire|water|lightning|psychic|fighting|darkness|metal) energy attached to this pokémon",
            text,
        )
        if snipe_scale:
            damage *= _energy_count(ctx, ctx.attacker, snipe_scale.group(1))
        picks = await ctx.choose_cards(pool, min(count, len(pool)), prompt="Choose Pokémon to damage") if pool else []
        for target in picks:
            # Double Thread explicitly applies W/R on the Bench.
            bench_wr = "apply weakness and resistance" in text \
                and "don't apply weakness" not in text \
                and "do not apply weakness" not in text
            await ctx.deal_damage(
                damage, target=target,
                apply_modifiers=True if bench_wr else None,
            )

    # Spread damage has no selection and never applies W/R to the Bench.
    spread = re.search(
        r"does (\d+) damage to each of your opponent's benched pokémon", text)
    if spread:
        for target in list(ctx.opponent_bench()):
            await ctx.deal_damage(int(spread.group(1)), target=target,
                                  apply_modifiers=None)
    spread_both = re.search(r"does (\d+) damage to each benched pokémon", text)
    if spread_both:
        for target in list(ctx.my_bench()) + list(ctx.opponent_bench()):
            await ctx.deal_damage(int(spread_both.group(1)), target=target,
                                  apply_modifiers=None)
    spread_side = re.search(
        r"(?:this attack )?does (\d+) damage to each of your opponent's pokémon",
        text,
    )
    if spread_side:
        for target in list(ctx.opponent_pokemon_in_play()):
            await ctx.deal_damage(
                int(spread_side.group(1)), target=target,
                apply_modifiers=(target is ctx.defender),
            )

    ability_spread = re.search(
        r"does (\d+) damage to each pokémon that has an ability", text,
    )
    if ability_spread:
        for target in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
            if _has_pokemon_ability(target):
                await ctx.deal_damage(
                    int(ability_spread.group(1)), target=target,
                    apply_modifiers=(target is ctx.defender),
                )

    rule_box_spread = re.search(
        r"does (\d+) damage to each pokémon-gx and pokémon-ex", text,
    )
    if rule_box_spread:
        for target in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
            subtypes = set(subtypes_for(target.archetype_id) or [])
            if "GX" not in subtypes and "EX" not in subtypes \
                    and not _name(target).endswith("-EX"):
                continue
            await ctx.deal_damage(
                int(rule_box_spread.group(1)), target=target,
                apply_modifiers=(target is ctx.defender),
            )

    targeted = re.search(
        r"choose 1 of your opponent's pokémon\. this attack does (\d+) damage to that pokémon",
        text,
    )
    if targeted:
        target = await ctx.choose_pokemon(
            ctx.opponent_pokemon_in_play(), "Choose a Pokémon to damage"
        ) if ctx.opponent_pokemon_in_play() else None
        if target is not None:
            await ctx.deal_damage(
                int(targeted.group(1)), target=target,
                apply_modifiers=(target is ctx.defender),
            )

    # Selection-first snipe wording (Blindside, Dual Splash, Double Attack).
    # The earlier snipe template handles "does X to N"; these cards state the
    # target count before the damage amount.
    selected_hits = re.search(
        r"choose (\d+) of your opponent's (benched )?pokémon(?:[^.]*?)\. "
        r"this attack does (\d+) damage to each of them", text,
    )
    if selected_hits:
        count = int(selected_hits.group(1))
        pool = list(ctx.opponent_bench() if selected_hits.group(2)
                    else ctx.opponent_pokemon_in_play())
        picks = await ctx.choose_cards(
            pool, min(count, len(pool)), minimum=min(count, len(pool)),
            prompt="Choose Pokémon to damage",
        ) if pool else []
        for target in picks:
            await ctx.deal_damage(
                int(selected_hits.group(3)), target=target,
                apply_modifiers=(target is ctx.defender),
            )

    # Some modern cards omit the leading "Choose" but still specify a fixed
    # number of targets (Split Bomb).  They are not an all-board spread.
    each_of_hits = re.search(
        r"(?:this attack )?does (\d+) damage to each of (\d+) of your "
        r"opponent's pokémon", text,
    )
    if each_of_hits:
        damage, count = map(int, each_of_hits.groups())
        pool = list(ctx.opponent_pokemon_in_play())
        picks = await ctx.choose_cards(
            pool, min(count, len(pool)), minimum=min(count, len(pool)),
            prompt="Choose Pokémon to damage",
        ) if pool else []
        for target in picks:
            await ctx.deal_damage(
                damage, target=target,
                apply_modifiers=(target is ctx.defender),
            )

    selected_hit = re.search(
        r"choose 1 of your opponent's (benched )?pokémon(?:[^.]*)\. "
        r"this attack does (\d+) damage to (?:that pokémon|it)", text,
    )
    if selected_hit:
        pool = list(ctx.opponent_bench() if selected_hit.group(1)
                    else ctx.opponent_pokemon_in_play())
        if "that has any damage counters" in text:
            pool = [pokemon for pokemon in pool if _damage_counter_count(ctx, pokemon)]
        target = await ctx.choose_pokemon(pool, "Choose a Pokémon to damage") \
            if pool else None
        if target is not None:
            await ctx.deal_damage(
                int(selected_hit.group(2)), target=target,
                apply_modifiers=(target is ctx.defender),
            )

    repeat_hits = re.search(
        r"choose 1 of your opponent's pokémon(?:-gx or pokémon-ex)? (\d+) times.*"
        r"for each time you chose a pokémon, do (\d+) damage to it", text,
    )
    if repeat_hits:
        for _ in range(int(repeat_hits.group(1))):
            targets = list(ctx.opponent_pokemon_in_play())
            target = await ctx.choose_pokemon(targets, "Choose a Pokémon to damage") \
                if targets else None
            if target is not None:
                await ctx.deal_damage(
                    int(repeat_hits.group(2)), target=target,
                    apply_modifiers=(target is ctx.defender),
                )

    opponent_chosen_hit = re.search(
        r"your opponent chooses 1 of their own pokémon\. this attack does "
        r"(\d+) damage to that pokémon", text,
    )
    if opponent_chosen_hit:
        targets = list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(
            targets, "Choose one of your Pokémon", player_id=ctx.opponent_id,
        ) if targets else None
        if target is not None:
            await ctx.deal_damage(
                int(opponent_chosen_hit.group(1)), target=target,
                apply_modifiers=(target is ctx.defender),
            )

    # Repeated distribution attacks choose the same target more than once.
    energy_rain = re.search(
        r"discard (?:as many|any amount of) "
        r"(lightning|metal) energy (?:attached to|from) this pokémon.*"
        r"for each energy(?: card)? (?:you )?discarded in this way, choose 1 "
        r"of your opponent's pokémon and do (\d+) damage to it", text,
    )
    if energy_rain:
        ptype = getattr(PokemonTypes, energy_rain.group(1).upper())
        eligible = [energy for energy in ctx.attached_energies(ctx.attacker)
                    if energy_provides_type(energy, ptype.value)]
        picks = await ctx.choose_cards(
            eligible, len(eligible), minimum=0,
            prompt="Choose Energy cards to discard",
        ) if eligible else []
        if picks:
            await ctx.discard_cards(picks)
        for _ in picks:
            targets = list(ctx.opponent_pokemon_in_play())
            target = await ctx.choose_pokemon(targets, "Choose a Pokémon to damage") \
                if targets else None
            if target is not None:
                await ctx.deal_damage(
                    int(energy_rain.group(2)), target=target,
                    apply_modifiers=(target is ctx.defender),
                    ignore_weakness=True, ignore_resistance=True,
                )

    named_board_snipe = re.search(
        r"this attack does (\d+) damage (?:(?:times|for) the number of|for each) "
        r"([a-z0-9 .'-]+) you have in play to 1 of your opponent's "
        r"(?:benched )?pokémon", text,
    )
    if named_board_snipe:
        wanted = named_board_snipe.group(2).strip().casefold()
        count = sum(_name(pokemon).casefold() == wanted
                    for pokemon in ctx.my_pokemon_in_play())
        pool = list(ctx.opponent_bench()) if "benched pokémon" in text \
            else list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(pool, "Choose a Pokémon to damage") \
            if pool else None
        if target is not None:
            await ctx.deal_damage(
                int(named_board_snipe.group(1)) * count, target=target,
                apply_modifiers=(target is ctx.defender),
            )

    named_discard_snipe = re.search(
        r"this attack does (\d+) damage for each pokémon in your discard "
        r"pile that has the ([a-z0-9 '-]+) attack to 1 of your opponent's "
        r"(?:benched )?pokémon", text,
    )
    if named_discard_snipe:
        count = sum(
            is_pokemon_card(card)
            and _has_attack_named(card, named_discard_snipe.group(2).strip())
            for card in ctx.discard_pile()
        )
        pool = list(ctx.opponent_bench()) if "benched pokémon" in text \
            else list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(pool, "Choose a Pokémon to damage") \
            if pool else None
        if target is not None:
            await ctx.deal_damage(
                int(named_discard_snipe.group(1)) * count, target=target,
                apply_modifiers=(target is ctx.defender),
            )

    target_energy_snipe = re.search(
        r"choose 1 of your opponent's pokémon\. this attack does (\d+) "
        r"damage for each energy attached to that pokémon", text,
    )
    if target_energy_snipe:
        pool = list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(pool, "Choose a Pokémon to damage") \
            if pool else None
        if target is not None:
            await ctx.deal_damage(
                int(target_energy_snipe.group(1)) * _energy_count(ctx, target),
                target=target, apply_modifiers=(target is ctx.defender),
            )

    nuzzle_snipe = re.search(
        r"does (\d+) damage for each of your pokémon in play that has the "
        r"([a-z0-9 '-]+) attack to 1 of your opponent's benched pokémon", text,
    )
    if nuzzle_snipe:
        count = sum(_has_attack_named(pokemon, nuzzle_snipe.group(2).strip())
                    for pokemon in ctx.my_pokemon_in_play())
        target = await ctx.choose_pokemon(
            ctx.opponent_bench(), "Choose a Benched Pokémon to damage"
        ) if ctx.opponent_bench() else None
        if target is not None:
            await ctx.deal_damage(
                int(nuzzle_snipe.group(1)) * count, target=target,
                apply_modifiers=False,
            )

    # Damage every Pokémon matching a printed board predicate.
    each_matching = re.search(
        r"does (\d+) damage to each pokémon (?:in play )?that has (?:any |an )?"
        r"(damage counters|poké-powers|an ability)", text,
    )
    if each_matching:
        pool = list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play())
        predicate = each_matching.group(2)
        if predicate == "damage counters":
            pool = [pokemon for pokemon in pool if _damage_counter_count(ctx, pokemon)]
        elif predicate == "an ability":
            pool = [pokemon for pokemon in pool if _has_pokemon_ability(pokemon)]
        else:
            pool = [pokemon for pokemon in pool if _has_pokemon_ability(pokemon)]
        if "except for this pokémon" in text:
            pool = [pokemon for pokemon in pool if pokemon is not ctx.attacker]
        for target in pool:
            await ctx.deal_damage(
                int(each_matching.group(1)), target=target,
                apply_modifiers=(target is ctx.defender),
                ignore_weakness=True, ignore_resistance=True,
            )

    rulebox_spread = re.search(
        r"does (\d+) damage to each pokémon-gx and pokémon-ex", text,
    )
    if rulebox_spread:
        for target in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
            subtypes = set(getattr(def_for(target.archetype_id), "subtypes", []) or [])
            if "GX" not in subtypes and not _pokemon_ex(target):
                continue
            await ctx.deal_damage(
                int(rulebox_spread.group(1)), target=target,
                apply_modifiers=(target is ctx.defender),
            )

    non_type_spread = re.search(
        r"does (\d+) damage to each non-([a-z]+) pokémon", text,
    ) or re.search(
        r"does (\d+) damage to each pokémon in play.*excluding any ([a-z]+) pokémon",
        text,
    )
    if non_type_spread:
        excluded_word = non_type_spread.group(2)
        excluded_type = getattr(PokemonTypes, excluded_word.upper(), None)
        for target in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
            if excluded_type is not None and excluded_type.value in \
                    effective_pokemon_types(ctx.board, target):
                continue
            await ctx.deal_damage(
                int(non_type_spread.group(1)), target=target,
                apply_modifiers=(target is ctx.defender),
            )

    # Coin recoil / ordinary recoil.
    recoil = re.search(r"this pokémon does (\d+) damage to itself", text)
    conditional_optional_recoil = "you may do" in text and "if you do" in text
    if recoil and (not conditional_optional_recoil or optional_recoil_taken) \
            and (heads is None or heads == 0 or "if tails" not in text):
        await ctx.deal_damage(int(recoil.group(1)), target=ctx.attacker,
                              apply_modifiers=False)

    # Special Conditions.  A heads/tails split is honored when present.
    condition_map = {
        "asleep": SpecialConditions.ASLEEP,
        "burned": SpecialConditions.BURNED,
        "confused": SpecialConditions.CONFUSED,
        "paralyzed": SpecialConditions.PARALYZED,
        "poisoned": SpecialConditions.POISONED,
    }
    # Preserve the condition's complete clause: "Paralyzed and Poisoned"
    # applies BOTH conditions, with the same coin requirement for each one.
    status_clauses = list(re.finditer(
        r"(?:(if heads|if tails), )?(?:the )?defending pokémon is now "
        r"((?:asleep|burned|confused|paralyzed|poisoned)"
        r"(?:(?:,? and |, )(?:asleep|burned|confused|paralyzed|poisoned))*)",
        text,
    ))
    for word, condition in condition_map.items():
        clauses = [match for match in status_clauses
                   if re.search(rf"\b{word}\b", match.group(2))]
        if not clauses:
            continue
        if not any(match.group(1) is None
                   or match.group(1) == "if heads" and heads
                   or match.group(1) == "if tails" and not heads
                   for match in clauses):
            continue
        poison = 1
        if condition == SpecialConditions.POISONED:
            stronger = re.search(r"put (\d+) damage counters instead of 1", text)
            poison = int(stronger.group(1)) if stronger else 1
        confusion_damage = 30
        if condition == SpecialConditions.CONFUSED:
            stronger = re.search(r"put (\d+) damage counters instead of 3", text)
            confusion_damage = int(stronger.group(1)) * 10 if stronger else 30
        await ctx.apply_special_condition(
            ctx.defender, condition, poison_counters=poison,
            confusion_damage=confusion_damage,
        )
    for word, condition in condition_map.items():
        if f"this pokémon is now {word}" in text:
            await ctx.apply_special_condition(ctx.attacker, condition)
        source_name = _name(ctx.attacker).casefold()
        if source_name and f"{source_name} is now {word}" in text:
            await ctx.apply_special_condition(ctx.attacker, condition)
        if f"both active pokémon are now {word}" in text:
            for target in (ctx.attacker, ctx.defender):
                if target is not None:
                    await ctx.apply_special_condition(target, condition)

    conditional_paralysis = False
    if "if the defending pokémon is a dragon pokémon, it is now paralyzed" in text:
        conditional_paralysis = PokemonTypes.DRAGON.value in effective_pokemon_types(
            ctx.board, ctx.defender)
    elif "if the defending pokémon is a metal pokémon, it is now paralyzed" in text:
        conditional_paralysis = PokemonTypes.METAL.value in effective_pokemon_types(
            ctx.board, ctx.defender)
    elif "if the defending pokémon has any water energy attached to it, it is now paralyzed" in text:
        conditional_paralysis = _energy_count(ctx, ctx.defender, "water") > 0
    elif "if the defending pokémon is confused, it is now paralyzed" in text:
        conditional_paralysis = (
            CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED]
            in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        )
    if conditional_paralysis:
        await ctx.apply_special_condition(
            ctx.defender, SpecialConditions.PARALYZED,
        )

    direct = re.search(
        r"(?:put|place) (\d+) damage counters? on (?:1 of )?your opponent's pokémon",
        text,
    )
    if direct:
        await ctx.place_damage_counters(
            int(direct.group(1)), ctx.opponent_pokemon_in_play())
    direct_active = re.search(
        r"(?:put|place) (\d+) damage counters? on (?:the )?defending pokémon",
        text,
    )
    if direct_active and ctx.defender is not None:
        await ctx.deal_damage(
            int(direct_active.group(1)) * 10, target=ctx.defender,
            apply_modifiers=False, as_counters=True,
        )
    bench_counter_spread = re.search(
        r"put (\d+) damage counters? on each of your opponent's benched pokémon",
        text,
    )
    if bench_counter_spread:
        for target in list(ctx.opponent_bench()):
            await ctx.deal_damage(
                int(bench_counter_spread.group(1)) * 10, target=target,
                apply_modifiers=False, as_counters=True,
            )
    hand_counters = re.search(
        r"for each card in your opponent's hand, put (\d+) damage counters? "
        r"on (?:their active|the defending) pokémon", text,
    )
    if hand_counters and ctx.defender is not None:
        await ctx.deal_damage(
            int(hand_counters.group(1)) * ctx.hand_size(ctx.opponent_id) * 10,
            target=ctx.defender, apply_modifiers=False, as_counters=True,
        )
    if "count the number of cards in your opponent's hand" in text \
            and "put that many damage counters on the defending pokémon" in text \
            and ctx.defender is not None:
        await ctx.deal_damage(
            ctx.hand_size(ctx.opponent_id) * 10, target=ctx.defender,
            apply_modifiers=False, as_counters=True,
        )
    if re.search(
        r"put damage counters on (?:the )?defending pokémon until its remaining hp is 10",
        text,
    ):
        await ctx.set_damage_counters(
            ctx.defender, max(0, (ctx.max_hp(ctx.defender) - 10) // 10))

    spread_counters = re.search(
        r"(?:put|place) (\d+) damage counters? on each of your opponent's pokémon",
        text,
    )
    if spread_counters:
        count = int(spread_counters.group(1))
        candidates = list(ctx.opponent_pokemon_in_play())
        if "that has any damage counters" in text:
            candidates = [p for p in candidates if _damage_counter_count(ctx, p)]
        if "that has any energy attached" in text:
            candidates = [p for p in candidates if ctx.attached_energies(p)]
        if "that has a pokémon tool" in text:
            candidates = [p for p in candidates if _has_tool(p)]
        for target in candidates:
            await ctx.deal_damage(
                count * 10, target=target, apply_modifiers=False,
                as_counters=True,
            )

    both_sides_spread_counters = re.search(
        r"(?:put|place) (\d+) damage counters? on each pokémon "
        r"\(both yours and your opponent's\)", text,
    )
    if both_sides_spread_counters:
        count = int(both_sides_spread_counters.group(1))
        for target in list(ctx.my_pokemon_in_play()) + list(
                ctx.opponent_pokemon_in_play()):
            await ctx.deal_damage(
                count * 10, target=target, apply_modifiers=False,
                as_counters=True,
            )

    until_hp = re.search(
        r"put damage counters on (?:your opponent's active|(?:the )?defending) pokémon "
        r"until its remaining hp is (\d+)", text,
    )
    if until_hp and ctx.defender is not None:
        remaining = int(until_hp.group(1))
        await ctx.set_damage_counters(
            ctx.defender,
            max(0, (ctx.max_hp(ctx.defender) - remaining) // 10),
        )

    # Fixed-remaining-HP effects can target any Pokémon or every Benched
    # Pokémon rather than only the Defending Pokémon.
    until_each_bench = re.search(
        r"put damage counters on each of your opponent's benched pokémon "
        r"until its remaining hp is (\d+)", text,
    )
    if until_each_bench:
        remaining = int(until_each_bench.group(1))
        for target in list(ctx.opponent_bench()):
            await ctx.set_damage_counters(
                target, max(0, (ctx.max_hp(target) - remaining) // 10)
            )

    until_any = re.search(
        r"put damage counters on 1 of your opponent's pokémon until its "
        r"remaining hp is (\d+)", text,
    )
    if until_any:
        targets = list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if targets else None
        if target is not None:
            remaining = int(until_any.group(1))
            await ctx.set_damage_counters(
                target, max(0, (ctx.max_hp(target) - remaining) // 10)
            )

    if "put damage counters on both active pokémon until the remaining hp of each pokémon is 10" in text:
        for target in (ctx.attacker, ctx.defender):
            if target is not None:
                await ctx.set_damage_counters(
                    target, max(0, (ctx.max_hp(target) - 10) // 10)
                )

    choose_counters = re.search(
        r"choose (\d+) of your opponent's (benched )?pokémon and put "
        r"(\d+) damage counters on each of them", text,
    )
    if choose_counters:
        pool = list(ctx.opponent_bench() if choose_counters.group(2)
                    else ctx.opponent_pokemon_in_play())
        count = min(int(choose_counters.group(1)), len(pool))
        picks = await ctx.choose_cards(
            pool, count, minimum=count, prompt="Choose Pokémon"
        ) if count else []
        for target in picks:
            await ctx.deal_damage(
                int(choose_counters.group(3)) * 10, target=target,
                apply_modifiers=False, as_counters=True,
            )

    loose_each_counters = re.search(
        r"put (\d+) damage counters each of your opponent's pokémon", text,
    )
    if loose_each_counters:
        for target in list(ctx.opponent_pokemon_in_play()):
            await ctx.deal_damage(
                int(loose_each_counters.group(1)) * 10, target=target,
                apply_modifiers=False, as_counters=True,
            )

    if "double the number of damage counters on each of your opponent's pokémon" in text:
        for target in list(ctx.opponent_pokemon_in_play()):
            counters = _damage_counter_count(ctx, target)
            if counters:
                await ctx.deal_damage(
                    counters * 10, target=target,
                    apply_modifiers=False, as_counters=True,
                )

    if text.startswith("choose grass fire water lightning psychic fighting darkness metal or colorless type"):
        names = ["Grass", "Fire", "Water", "Lightning", "Psychic",
                 "Fighting", "Darkness", "Metal", "Colorless"]
        index = await ctx.choose("Choose a Pokémon type", names)
        chosen = getattr(PokemonTypes, names[index].upper()).value
        for target in list(ctx.opponent_pokemon_in_play()):
            if chosen in effective_pokemon_types(ctx.board, target):
                await ctx.deal_damage(
                    10, target=target, apply_modifiers=False, as_counters=True,
                )

    # Healing templates.
    m = re.search(r"heal (\d+) damage from (?:this pokémon|it)", text)
    if m:
        await ctx.heal(int(m.group(1)), ctx.attacker)
    m = re.search(r"(?:^|\. )heal (\d+) damage(?: and|\.|$)", text)
    if m:
        await ctx.heal(int(m.group(1)), ctx.attacker)
    if "heal from this pokémon the same amount of damage you did" in text:
        await ctx.heal(primary_damage_dealt, ctx.attacker)
    variable_self_heal = re.search(
        r"heal from this pokémon (\d+) damage times the amount of energy "
        r"attached to (?:the defending|your opponent's active) pokémon", text,
    )
    if variable_self_heal:
        await ctx.heal(
            int(variable_self_heal.group(1)) * _energy_count(ctx, ctx.defender),
            ctx.attacker,
        )
    if "heal all damage from this pokémon" in text:
        await ctx.heal(ctx.max_hp(ctx.attacker), ctx.attacker)
    if "heal all damage from each of your tera pokémon" in text:
        for target in ctx.my_pokemon_in_play():
            if "Tera" in (subtypes_for(target.archetype_id) or []):
                await ctx.heal(ctx.max_hp(target), target)
    heal_one_allowed = not (
        "if both of them are heads" in text and heads != coin_count
    )
    if "heal all damage from 1 of your pokémon" in text and heal_one_allowed:
        candidates = [p for p in ctx.my_pokemon_in_play() if _damaged(ctx, p)]
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") \
            if candidates else None
        if target is not None:
            await ctx.heal(ctx.max_hp(target), target)
    source_name = _name(ctx.attacker).casefold()
    if source_name and re.search(
        rf"remove all damage counters from {re.escape(source_name)}", text,
    ):
        await ctx.heal(ctx.max_hp(ctx.attacker), ctx.attacker)
    m = re.search(r"heal (\d+) damage from 1 of your pokémon", text)
    if m:
        candidates = [p for p in ctx.my_pokemon_in_play() if _damaged(ctx, p)]
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") if candidates else None
        if target is not None:
            await ctx.heal(int(m.group(1)), target)
    m = re.search(r"heal (\d+) damage from 1 of your benched(?: [a-z]+)? pokémon", text)
    if m:
        candidates = [p for p in ctx.my_bench() if _damaged(ctx, p)]
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") \
            if candidates else None
        if target is not None:
            await ctx.heal(int(m.group(1)), target)
    m = re.search(
        r"heal (\d+) damage from each of your(?: basic| [a-z]+)? pokémon", text
    )
    if m:
        targets = list(ctx.my_pokemon_in_play())
        if "your basic pokémon" in m.group(0):
            targets = [target for target in targets if is_basic_pokemon(target)]
        else:
            for word, ptype in (
                ("grass", PokemonTypes.GRASS), ("fire", PokemonTypes.FIRE),
                ("water", PokemonTypes.WATER), ("lightning", PokemonTypes.LIGHTNING),
                ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
                ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
            ):
                if f"your {word} pokémon" in m.group(0):
                    targets = [target for target in targets if _is_type(target, ptype)]
                    break
        for target in targets:
            await ctx.heal(int(m.group(1)), target)
    heal_everyone = re.search(
        r"heal (\d+) damage from each pokémon \(both yours and your opponent's\)", text,
    )
    if heal_everyone:
        for target in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
            await ctx.heal(int(heal_everyone.group(1)), target)
    heal_both_active = re.search(r"heal (\d+) damage from both active pokémon", text)
    if heal_both_active:
        for target in (ctx.attacker, ctx.defender):
            if target is not None:
                await ctx.heal(int(heal_both_active.group(1)), target)
    if "remove all special conditions from this pokémon" in text:
        for condition in SpecialConditions:
            if condition != SpecialConditions.UNSET:
                await ctx.cure_condition(ctx.attacker, condition)
    source_name = _name(ctx.attacker).casefold()
    if source_name and f"remove all special conditions and" in text \
            and f"from {source_name}" in text:
        for condition in SpecialConditions:
            if condition != SpecialConditions.UNSET:
                await ctx.cure_condition(ctx.attacker, condition)
    remove_counters = re.search(
        r"remove (\d+) damage counters? from (?:1 of your pokémon|this pokémon|[a-z0-9 .'-]+)",
        text,
    )
    if remove_counters:
        amount = int(remove_counters.group(1)) * 10
        target = ctx.attacker
        if "1 of your pokémon" in remove_counters.group(0):
            candidates = [p for p in ctx.my_pokemon_in_play()
                          if _damage_counter_count(ctx, p)]
            target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") \
                if candidates else None
        if target is not None:
            await ctx.heal(amount, target)
    remove_each = re.search(
        r"remove (\d+) damage counters? from each of your pokémon", text
    )
    if remove_each:
        for target in list(ctx.my_pokemon_in_play()):
            await ctx.heal(int(remove_each.group(1)) * 10, target)

    if "remove all damage counters from each of your pokémon" in text:
        for target in list(ctx.my_pokemon_in_play()):
            await ctx.heal(ctx.max_hp(target), target)

    if re.search(
        r"move all damage counters from this pokémon to (?:the )?defending pokémon",
        text,
    ):
        await ctx.move_damage_counters(ctx.attacker, ctx.defender)
    elif re.search(
        r"move all damage counters from 1 of your benched pokémon to (?:the )?defending",
        text,
    ):
        sources = [p for p in ctx.my_bench() if _damage_counter_count(ctx, p)]
        source = await ctx.choose_pokemon(sources, "Choose a damaged Pokémon") \
            if sources else None
        if source is not None:
            await ctx.move_damage_counters(source, ctx.defender)
    elif "move 6 damage counters from any of your pokémon to the defending" in text:
        sources = [p for p in ctx.my_pokemon_in_play() if _damage_counter_count(ctx, p)]
        source = await ctx.choose_pokemon(sources, "Choose a damaged Pokémon") \
            if sources else None
        if source is not None:
            await ctx.move_damage_counters(source, ctx.defender, max_count=6)
    elif "move 1 damage counter from any of your pokémon to any of your opponent's" in text:
        sources = [p for p in ctx.my_pokemon_in_play() if _damage_counter_count(ctx, p)]
        source = await ctx.choose_pokemon(sources, "Choose a damaged Pokémon") \
            if sources else None
        target = await ctx.choose_pokemon(ctx.opponent_pokemon_in_play(),
                                          "Choose the target Pokémon") \
            if source is not None else None
        if target is not None:
            await ctx.move_damage_counters(source, target, max_count=1)
    elif "move any number of damage counters on your opponent's pokémon" in text:
        processed = set()
        while True:
            sources = [p for p in ctx.opponent_pokemon_in_play()
                       if p.entity_id not in processed
                       and _damage_counter_count(ctx, p)]
            source = await ctx.choose_pokemon(
                sources, "Choose a Pokémon to move damage from", optional=True
            ) if sources else None
            if source is None:
                break
            processed.add(source.entity_id)
            await ctx.move_damage_counters(
                source, ctx.opponent_pokemon_in_play(),
                prompt="Move those damage counters among your opponent's Pokémon",
            )

    elif "move as many damage counters on your opponent's" in text \
            and "to any of your opponent's other pokémon" in text:
        processed = set()
        while True:
            sources = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                       if pokemon.entity_id not in processed
                       and _damage_counter_count(ctx, pokemon)]
            source = await ctx.choose_pokemon(
                sources, "Choose a Pokémon to move damage from", optional=True,
            ) if sources else None
            if source is None:
                break
            processed.add(source.entity_id)
            await ctx.move_damage_counters(
                source, ctx.opponent_pokemon_in_play(),
                prompt="Move those damage counters among your opponent's Pokémon",
            )

    elif "move any number of damage counters from your opponent's benched pokémon" in text \
            and "to their active pokémon" in text:
        # Damage Collection: each damaged Bench Pokémon may contribute any
        # number of its counters to the Active.
        for source in list(ctx.opponent_bench()):
            if _damage_counter_count(ctx, source):
                await ctx.move_damage_counters(
                    source, ctx.defender,
                    prompt="Move damage counters to the Active Pokémon",
                )

    if re.search(
        r"switch all damage counters on this pokémon with those on (?:the )?defending pokémon",
        text,
    ):
        attacker_count = _damage_counter_count(ctx, ctx.attacker)
        defender_count = _damage_counter_count(ctx, ctx.defender)
        await ctx.set_damage_counters(ctx.attacker, defender_count)
        await ctx.set_damage_counters(ctx.defender, attacker_count)

    bench_transfer = re.search(
        r"move all damage counters from 1 of your benched(?: [a-z]+)? pokémon "
        r"to (?:your opponent's active|(?:the )?defending) pokémon", text,
    )
    if bench_transfer:
        sources = [pokemon for pokemon in ctx.my_bench()
                   if _damage_counter_count(ctx, pokemon)]
        if "ancient pokémon" in bench_transfer.group(0):
            sources = [pokemon for pokemon in sources if "Ancient" in (
                getattr(def_for(pokemon.archetype_id), "subtypes", None) or [])]
        source = await ctx.choose_pokemon(sources, "Choose a damaged Pokémon") \
            if sources else None
        if source is not None:
            await ctx.move_damage_counters(source, ctx.defender)

    bench_to_any = re.search(
        r"move all damage counters from 1 of your benched(?: [a-z]+)? pokémon "
        r"to 1 of your opponent's pokémon", text,
    )
    if bench_to_any:
        sources = [pokemon for pokemon in ctx.my_bench()
                   if _damage_counter_count(ctx, pokemon)]
        if "ancient pokémon" in bench_to_any.group(0):
            sources = [pokemon for pokemon in sources if "Ancient" in set(
                getattr(def_for(pokemon.archetype_id), "subtypes", []) or []
            )]
        source = await ctx.choose_pokemon(sources, "Choose a damaged Pokémon") \
            if sources else None
        targets = list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(targets, "Choose a target Pokémon") \
            if source is not None and targets else None
        if target is not None:
            await ctx.move_damage_counters(source, target)

    from_each = re.search(
        r"move (all|\d+) damage counters from each of your pokémon to "
        r"(?:your opponent's active|(?:the )?defending) pokémon", text,
    )
    if from_each:
        maximum = None if from_each.group(1) == "all" else int(from_each.group(1))
        for source in list(ctx.my_pokemon_in_play()):
            if source is ctx.defender or not _damage_counter_count(ctx, source):
                continue
            await ctx.move_damage_counters(
                source, ctx.defender, max_count=maximum
            )

    any_to_any = re.search(
        r"move up to (\d+) damage counters from any of your pokémon to any of "
        r"your opponent's pokémon", text,
    )
    if any_to_any:
        remaining = int(any_to_any.group(1))
        while remaining > 0:
            sources = [pokemon for pokemon in ctx.my_pokemon_in_play()
                       if _damage_counter_count(ctx, pokemon)]
            source = await ctx.choose_pokemon(
                sources, "Choose a Pokémon to move damage from", optional=True
            ) if sources else None
            if source is None:
                break
            targets = list(ctx.opponent_pokemon_in_play())
            target = await ctx.choose_pokemon(targets, "Choose a Pokémon to receive damage") \
                if targets else None
            if target is None:
                break
            moved = min(remaining, _damage_counter_count(ctx, source))
            await ctx.move_damage_counters(source, target, max_count=moved)
            remaining -= moved

    equal_counters = re.search(
        r"put damage counters on 1 of your opponent's pokémon equal to the "
        r"number of damage counters on this pokémon", text,
    )
    if equal_counters:
        targets = list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if targets else None
        if target is not None:
            await ctx.deal_damage(
                _damage_counter_count(ctx, ctx.attacker) * 10,
                target=target, apply_modifiers=False, as_counters=True,
            )

    one_counter_transfer = re.search(
        r"move (\d+) damage counters? from 1 of your pokémon to 1 of your "
        r"opponent's pokémon", text,
    )
    if one_counter_transfer:
        sources = [pokemon for pokemon in ctx.my_pokemon_in_play()
                   if _damage_counter_count(ctx, pokemon)]
        source = await ctx.choose_pokemon(sources, "Choose a damaged Pokémon") \
            if sources else None
        targets = list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if source is not None and targets else None
        if target is not None:
            await ctx.move_damage_counters(
                source, target, max_count=int(one_counter_transfer.group(1))
            )

    if "move any number of damage counters from your opponent's pokémon " \
            "to their other pokémon in any way you like" in text:
        while True:
            sources = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                       if _damage_counter_count(ctx, pokemon)]
            source = await ctx.choose_pokemon(
                sources, "Choose a Pokémon to move damage from", optional=True,
            ) if sources else None
            if source is None:
                break
            targets = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                       if pokemon is not source]
            target = await ctx.choose_pokemon(
                targets, "Choose a Pokémon to receive damage",
            ) if targets else None
            if target is None:
                break
            available = _damage_counter_count(ctx, source)
            choice = await ctx.choose(
                "How many damage counters should move?",
                [str(value) for value in range(1, available + 1)],
            )
            moved = await ctx.move_damage_counters(
                source, target, max_count=choice + 1,
            )
            if moved <= 0:
                break
            # A headless opponent always selects the first optional target;
            # without an explicit Done action it would move the same counter
            # back and forth forever.  Make one useful deterministic move for
            # AI players while human players retain the repeat-until-Done UI.
            if ctx.session.players[ctx.player_id].__class__.__name__ == "AIPlayer":
                break

    # Recover variants use either the source's printed name or "this Pokémon"
    # and must pay exactly once before healing.
    recover_payment = re.search(
        r"discard (?:an|a) (?:[a-z]+ )?energy "
        r"(?:attached to|from) (?:this pokémon|[a-z0-9 .'-]+) and "
        r"(?:heal all damage from it|remove all damage counters from [a-z0-9 .'-]+|"
        r"remove (\d+) damage counters? from [a-z0-9 .'-]+)", text,
    )
    if recover_payment:
        paid = await ctx.discard_energy_units_from(
            ctx.attacker, 1, partial=False)
        if paid:
            amount = ctx.max_hp(ctx.attacker) if recover_payment.group(1) is None \
                else int(recover_payment.group(1)) * 10
            await ctx.heal(amount, ctx.attacker)
        prepaid_discard = True

    # Energy/card discards printed as after-effects.
    m = re.search(
        r"discard (up to )?(\d+|an|a|all) "
        r"(?:(basic|grass|fire|water|lightning|psychic|fighting|darkness|metal|"
        r"fairy) )?energy(?: cards?)? (?:attached to|from) this pokémon",
        text,
    )
    if m and not prepaid_discard:
        raw_count, type_word = m.group(2), m.group(3)
        ptype = getattr(PokemonTypes, (type_word or "").upper(), None)
        pred = is_basic_energy if type_word == "basic" else \
            (lambda e: energy_provides_type(e, ptype.value)) if ptype else None
        if raw_count == "all":
            cards = [energy for energy in ctx.attached_energies(ctx.attacker)
                     if pred is None or pred(energy)]
            await ctx.discard_cards(cards)
        else:
            count = 1 if raw_count in ("a", "an") else int(raw_count)
            await ctx.discard_energy_units_from(
                ctx.attacker, count, predicate=pred, partial=True,
            )
    elif "discard all energy attached to this pokémon" in text \
            or "discard all energy from this pokémon" in text:
        await ctx.discard_cards(ctx.attached_energies(ctx.attacker))
    else:
        named_energy = re.search(
            r"discard (\d+|an|a|all) "
            r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|"
            r"fairy) )?energy (?:attached to|from) "
            r"([a-z0-9 &'’-]+?)(?= and (?:heal|remove)|\.|$)", text,
        )
        if named_energy and named_energy.group(3).strip(" .").casefold() \
                == _name(ctx.attacker).casefold():
            if named_energy.group(1) == "all":
                predicate = _energy_predicate(named_energy.group(2)) \
                    if named_energy.group(2) else is_energy_card
                await ctx.discard_cards([
                    energy for energy in ctx.attached_energies(ctx.attacker)
                    if predicate(energy)
                ])
            else:
                count = 1 if named_energy.group(1) in ("a", "an") \
                    else int(named_energy.group(1))
                predicate = _energy_predicate(named_energy.group(2)) \
                    if named_energy.group(2) else None
                await ctx.discard_energy_units_from(
                    ctx.attacker, count, predicate=predicate, partial=True,
                )

    first_instruction = text.split(".", 1)[0]
    combined_types = [word for word in (
        "grass", "fire", "water", "lightning", "psychic", "fighting",
        "darkness", "metal", "fairy",
    ) if re.search(rf"\b{word}\b", first_instruction)]
    if first_instruction.startswith("discard ") and len(combined_types) >= 2 \
            and "energy" in first_instruction \
            and "from your hand" not in first_instruction:
        for word in combined_types:
            await ctx.discard_energy_units_from(
                ctx.attacker, 1, predicate=_energy_predicate(word), partial=True,
            )
        prepaid_discard = True
    direct_defender_energy = re.search(
        r"discard (up to )?(\d+|an|a|all) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|"
        r"special) )?energy(?: cards?)? (?:attached to|from) "
        r"(?:the )?defending pokémon(?: ex)?", text,
    )
    if direct_defender_energy and not (
        "if heads" in text and not heads
    ) and not (
        "if tails" in text and heads
    ) and not (
        "if you do" in text and "you may discard" in text
        and not optional_source_paid
    ):
        raw_count = direct_defender_energy.group(2)
        kind = direct_defender_energy.group(3)
        predicate = is_special_energy if kind == "special" else \
            _energy_predicate(kind) if kind else is_energy_card
        matching = [energy for energy in ctx.attached_energies(ctx.defender)
                    if predicate(energy)]
        count = len(matching) if raw_count == "all" else \
            1 if raw_count in ("a", "an") else int(raw_count)
        if matching and count:
            await ctx.discard_energy_from(
                ctx.defender, min(count, len(matching)), predicate=predicate,
                minimum=0 if direct_defender_energy.group(1) else None,
            )

    opponent_energy_discard = re.search(
        r"discard (up to )?(\d+|an|a) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|special) )?"
        r"energy from (?:1 of |each of )?your opponent's pokémon",
        text,
    )
    if opponent_energy_discard:
        count = 1 if opponent_energy_discard.group(2) in ("a", "an") \
            else int(opponent_energy_discard.group(2))
        kind = opponent_energy_discard.group(3)
        predicate = is_special_energy if kind == "special" else \
            _energy_predicate(kind) if kind else is_energy_card
        holders = [p for p in ctx.opponent_pokemon_in_play()
                   if any(predicate(e) for e in ctx.attached_energies(p))]
        if "each of your opponent's pokémon" in opponent_energy_discard.group(0):
            for holder in holders:
                await ctx.discard_energy_from(holder, count, predicate=predicate)
        else:
            remaining = count
            while remaining > 0 and holders:
                pool = [e for p in holders for e in ctx.attached_energies(p)
                        if predicate(e)]
                chosen = await _choose_one(
                    ctx, pool, "Choose an Energy to discard",
                    optional=bool(opponent_energy_discard.group(1)),
                ) if pool else None
                if chosen is None:
                    break
                await ctx.discard_cards([chosen])
                remaining -= 1

    fixed_board_energy = re.search(
        r"discard (\d+) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
        r"energy from your pokémon", text,
    )
    if fixed_board_energy:
        count = int(fixed_board_energy.group(1))
        predicate = _energy_predicate(fixed_board_energy.group(2)) \
            if fixed_board_energy.group(2) else is_energy_card
        energies = [energy for pokemon in ctx.my_pokemon_in_play()
                    for energy in ctx.attached_energies(pokemon)
                    if predicate(energy)]
        maximum = min(count, len(energies))
        picks = await ctx.choose_cards(
            energies, maximum, minimum=maximum,
            prompt="Choose Energy cards to discard",
        ) if maximum else []
        if picks:
            await ctx.discard_cards(picks)

    if "discard an energy attached to 1 of your opponent's pokémon" in text:
        energies = [energy for pokemon in ctx.opponent_pokemon_in_play()
                    for energy in ctx.attached_energies(pokemon)]
        chosen = await _choose_one(
            ctx, energies, "Choose an Energy to discard",
        ) if energies else None
        if chosen is not None:
            await ctx.discard_cards([chosen])

    if "discard all energy from the defending pokémon" in text:
        await ctx.discard_cards(list(ctx.attached_energies(ctx.defender)))

    # Plain self-mill after-effects (Dragon Pulse and similar). Attacks that
    # inspect and attach from the milled cards are handled below as one atomic
    # instruction, so do not consume their cards here.
    self_top_discard = re.search(
        r"discard the top (?:(\d+) cards?|card) of your deck", text,
    )
    if self_top_discard and "attach" not in text and not prepaid_top_discard:
        count = int(self_top_discard.group(1) or 1)
        await ctx.discard_cards(ctx.deck_top(count))

    if "discard a team rocket's energy from this pokémon" in text:
        paid = await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda energy: _name(energy) == "Team Rocket's Energy",
        )
        if paid and "discard the defending pokémon and all attached cards" in text:
            await ctx.discard_cards(full_stack(ctx.defender))

    if "discard this pokémon and all attached cards" in text \
            or "discard this pokémon and all cards attached to it" in text:
        await ctx.discard_cards(full_stack(ctx.attacker))

    if "discard all cards from both active pokémon" in text:
        attachments = []
        for pokemon in (ctx.attacker, ctx.defender):
            if pokemon is not None:
                attachments.extend(full_stack(pokemon)[1:])
        if attachments:
            await ctx.discard_cards(attachments)

    # Draw/mill/recovery.
    m = re.search(r"draw (\d+|a) cards?", text)
    conditional_hand_draw = "if you do, draw" in text \
        and "discard" in text and "from your hand" in text
    if m and (not conditional_hand_draw or hand_discard_paid):
        await ctx.draw_cards(1 if m.group(1) == "a" else int(m.group(1)))
    if "put a card from your hand on the bottom of your deck" in text:
        hand = list(ctx.hand())
        chosen = await _choose_one(
            ctx, hand, "Choose a card to put on the bottom of your deck",
        ) if hand else None
        if chosen is not None:
            await ctx.put_on_bottom_of_deck(chosen)
    if "put a number of cards up to the number of heads from your discard pile into your hand" in text:
        candidates = list(ctx.discard_pile())
        maximum = min(heads or 0, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose cards from your discard pile",
        ) if maximum else []
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    if "put all electropower cards from your discard pile into your hand" in text:
        cards = [card for card in ctx.discard_pile()
                 if _name(card).casefold() == "electropower"]
        if cards:
            await ctx.put_in_hand(cards, reveal=True)
    m = re.search(
        r"discard the top (?:(\d+) cards?|card) (?:of|from) your opponent's deck",
        text,
    )
    if m:
        count = int(m.group(1) or 1)
        await ctx.discard_cards(ctx.deck_top(count, ctx.opponent_id))

    draw_until = re.search(r"draw cards until you have (\d+) cards in your hand", text)
    if draw_until:
        if "discard any number of cards from your hand" in text:
            hand = list(ctx.hand())
            picks = await ctx.choose_cards(
                hand, len(hand), minimum=0,
                prompt="Choose cards to discard",
            ) if hand else []
            await ctx.discard_cards(picks)
        await ctx.draw_until(int(draw_until.group(1)))

    # Information-only one-card peeks still need an actual reveal.  Optional
    # discard/bottom/shuffle decisions are resolved from the same card so its
    # identity never changes while the player is deciding.
    if "look at the top card of your deck" in text:
        cards = ctx.deck_top(1)
        if cards:
            await ctx.reveal_cards(cards, to_player=ctx.player_id)
            if "may discard that card" in text \
                    and await ctx.ask_yes_no("Discard that card?"):
                await ctx.discard_cards(cards)
            elif "may put that card on the bottom" in text \
                    and await ctx.ask_yes_no("Put that card on the bottom of your deck?"):
                await ctx.put_on_bottom_of_deck(cards[0])
            elif "may shuffle your deck" in text \
                    and await ctx.ask_yes_no("Shuffle your deck?"):
                await ctx.shuffle_deck()
    if "look at the top card of your opponent's deck" in text:
        cards = ctx.deck_top(1, ctx.opponent_id)
        if cards:
            await ctx.reveal_cards(cards, to_player=ctx.player_id)
            if "may have your opponent shuffle" in text \
                    and await ctx.ask_yes_no("Shuffle your opponent's deck?"):
                await ctx.shuffle_deck(ctx.opponent_id)

    if "look at your opponent's hand" in text:
        hand = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        if "put a card you find there in the lost zone" in text and hand:
            chosen = await _choose_one(ctx, hand, "Choose a card")
            if chosen is not None:
                await ctx.move_to_lost_zone([chosen])

    arbitrary_recovery = re.search(
        r"put (?:an?|any 1) (item|supporter|trainer|energy)? ?card from your "
        r"discard pile (?:into your hand|on top of your deck)", text,
    )
    if arbitrary_recovery:
        kind = arbitrary_recovery.group(1)
        predicate = {
            "item": is_item_card,
            "supporter": is_supporter_card,
            "trainer": is_trainer_card,
            "energy": is_energy_card,
        }.get(kind, lambda card: True)
        candidates = [card for card in ctx.discard_pile() if predicate(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a card") \
            if candidates else None
        if chosen is not None:
            if "show it to your opponent" in text:
                await ctx.reveal_cards([chosen])
            if "top of your deck" in text:
                await ctx.put_on_top_of_deck(chosen)
            else:
                await ctx.put_in_hand([chosen], reveal=True)

    typed_energy_recovery = re.search(
        r"put an? (?:basic )?(grass|fire|water|lightning|psychic|fighting|"
        r"darkness|metal) energy card from your discard pile into your hand",
        text,
    )
    if typed_energy_recovery:
        predicate = _energy_predicate(typed_energy_recovery.group(1))
        candidates = [card for card in ctx.discard_pile() if predicate(card)]
        chosen = await _choose_one(ctx, candidates, "Choose an Energy card") \
            if candidates else None
        if chosen is not None:
            await ctx.put_in_hand([chosen], reveal=True)

    search_discard = re.search(
        r"search your discard pile for (?:up to )?(\d+|any 1|an|a) "
        r"(.+?)(?:,| and) (?:show it to your opponent, and )?put (?:it|them) "
        r"(?:into your hand|on top of your deck)", text,
    )
    if search_discard:
        count = 1 if search_discard.group(1) in ("any 1", "an", "a") \
            else int(search_discard.group(1))
        descriptor = search_discard.group(2)
        predicate = _ability_search_predicate(descriptor)
        candidates = [card for card in ctx.discard_pile()
                      if predicate is None or predicate(card)]
        maximum = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum,
            minimum=0 if "up to" in search_discard.group(0) else maximum,
            prompt="Choose cards from your discard pile",
        ) if maximum else []
        if picks and "show it to your opponent" in text:
            await ctx.reveal_cards(picks)
        if "top of your deck" in text:
            for card in picks:
                await ctx.put_on_top_of_deck(card)
        else:
            await ctx.put_in_hand(picks, reveal="show" in text)
    m = re.search(
        r"put (\d+|an|a) item cards? from your discard pile into your hand", text
    )
    if m:
        cards = [c for c in ctx.discard_pile() if is_item_card(c)]
        requested = 1 if m.group(1) in ("a", "an") else int(m.group(1))
        picks = await ctx.choose_cards(
            cards, min(requested, len(cards)), prompt="Choose Item cards"
        ) if cards else []
        await ctx.put_in_hand(picks, reveal=True)
    recovered = re.search(
        r"put (?:up to )?(\d+|an|a) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal) )?"
        r"(pokémon|supporter|trainer|basic energy|energy) cards? from your discard pile into your hand",
        text,
    )
    if recovered:
        count = 1 if recovered.group(1) in ("a", "an") else int(recovered.group(1))
        type_word, kind = recovered.group(2), recovered.group(3)

        def predicate(card):
            if kind == "pokémon":
                if not is_pokemon_card(card):
                    return False
                if type_word:
                    ptype = getattr(PokemonTypes, type_word.upper(), None)
                    return ptype is not None and ptype.value in (
                        card.get_attribute(AttrID.POKEMON_TYPES) or []
                    )
                return True
            if kind == "supporter":
                return is_supporter_card(card)
            if kind == "trainer":
                return is_trainer_card(card)
            if kind == "basic energy":
                return is_basic_energy(card)
            return is_energy_card(card)

        candidates = [card for card in ctx.discard_pile() if predicate(card)]
        maximum = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum,
            minimum=0 if "up to" in text else maximum,
            prompt="Choose cards from your discard pile",
        ) if maximum else []
        await ctx.put_in_hand(picks, reveal=True)

    recovered_loose = re.search(
        r"put (?:up to )?(\d+|an|a) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal) )?"
        r"pokémon from your discard pile into your hand",
        text,
    )
    if recovered_loose:
        count = 1 if recovered_loose.group(1) in ("a", "an") \
            else int(recovered_loose.group(1))
        ptype = getattr(
            PokemonTypes, (recovered_loose.group(2) or "").upper(), None)
        cards = [c for c in ctx.discard_pile()
                 if is_pokemon_card(c)
                 and (ptype is None or ptype.value in
                      (c.get_attribute(AttrID.POKEMON_TYPES) or []))]
        maximum = min(count, len(cards))
        picks = await ctx.choose_cards(
            cards, maximum, minimum=0 if "up to" in recovered_loose.group(0)
            else maximum, prompt="Choose Pokémon from your discard pile",
        ) if maximum else []
        await ctx.put_in_hand(picks, reveal=True)

    if "shuffle a card from your discard pile into your deck" in text:
        candidates = list(ctx.discard_pile())
        chosen = await _choose_one(ctx, candidates, "Choose a card") \
            if candidates else None
        if chosen is not None:
            await ctx.shuffle_into_deck([chosen])

    shuffle_recovered = re.search(
        r"shuffle (?:up to )?(\d+|an|a) (.+?) cards? from your discard pile into your deck",
        text,
    )
    if shuffle_recovered:
        count = 1 if shuffle_recovered.group(1) in ("a", "an") \
            else int(shuffle_recovered.group(1))
        predicate = _ability_search_predicate(shuffle_recovered.group(2))
        candidates = [c for c in ctx.discard_pile()
                      if predicate is None or predicate(c)]
        maximum = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum,
            minimum=0 if "up to" in shuffle_recovered.group(0) else maximum,
            prompt="Choose cards to shuffle into your deck",
        ) if maximum else []
        if picks:
            await ctx.shuffle_into_deck(picks)

    plain_shuffle_recovery = re.search(
        r"shuffle (\d+) (?:([a-z]+) )?(pokémon|cards) from your discard pile "
        r"into your deck", text,
    )
    if plain_shuffle_recovery:
        count = int(plain_shuffle_recovery.group(1))
        type_word = plain_shuffle_recovery.group(2)
        kind = plain_shuffle_recovery.group(3)
        candidates = list(ctx.discard_pile())
        if kind == "pokémon":
            candidates = [card for card in candidates if is_pokemon_card(card)]
            ptype = getattr(PokemonTypes, (type_word or "").upper(), None)
            if ptype is not None:
                candidates = [card for card in candidates if _is_type(card, ptype)]
        maximum = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=maximum,
            prompt="Choose cards to shuffle into your deck",
        ) if maximum else []
        if picks:
            await ctx.shuffle_into_deck(picks)

    bottom_recovery = re.search(
        r"put (\d+) cards from your discard pile on the bottom of your deck", text,
    )
    if bottom_recovery:
        count = min(int(bottom_recovery.group(1)), len(ctx.discard_pile()))
        picks = await ctx.choose_cards(
            ctx.discard_pile(), count, minimum=count, ordered=True,
            prompt="Choose cards for the bottom of your deck",
        ) if count else []
        for card in picks:
            await ctx.put_on_bottom_of_deck(card)

    handled_top_selection = False
    top_selection = re.search(
        r"(?:look at|reveal) the top (\d+) cards of your deck", text,
    )
    if top_selection and any(phrase in text for phrase in (
        "put any number of pokémon you find there onto your bench",
        "put any number of basic pokémon you find there onto your bench",
        "choose as many basic pokémon as you like and put them onto your bench",
        "you may put any number of pokémon you find there onto your bench",
        "choose 1 pokémon you find there",
        "reveal any number of pokémon you find there and put them into your hand",
        "reveal any number of pokémon you find there, and put them into your hand",
        "attach any number of energy cards you find there",
        "attach as many lightning energy cards you find there as you like",
        "attach any number of metal energy cards you find there",
        "attach any number of basic energy cards you find there",
    )):
        handled_top_selection = True
        viewed = ctx.deck_top(int(top_selection.group(1)))
        picks = []
        if "onto your bench" in text:
            candidates = [card for card in viewed if is_pokemon_card(card)]
            if "basic pokémon" in text:
                candidates = [card for card in candidates if is_basic_pokemon(card)]
            capacity = max(
                0, effective_bench_capacity(ctx.board, ctx.player_id)
                - len(ctx.my_bench()),
            )
            maximum = min(capacity, len(candidates))
            picks = await ctx.choose_cards(
                candidates if capacity else [], max(1, maximum), minimum=0,
                prompt="Choose Pokémon for your Bench", display_cards=viewed,
            ) if viewed else []
            for card in picks:
                await ctx.bench_pokemon(card)
        elif "put them into your hand" in text or "put it into your hand" in text:
            candidates = [card for card in viewed if is_pokemon_card(card)]
            maximum = len(candidates) if "any number" in text else min(1, len(candidates))
            picks = await ctx.choose_cards(
                candidates, max(1, maximum),
                minimum=0 if "any number" in text else maximum,
                prompt="Choose Pokémon to put into your hand", display_cards=viewed,
            ) if viewed else []
            if "reveal any number" in text or "show it to your opponent" in text:
                await ctx.reveal_cards(picks)
            await ctx.put_in_hand(picks, reveal=False)
        elif "attach" in text and "energy" in text:
            candidates = [card for card in viewed if is_energy_card(card)]
            if "basic energy" in text:
                candidates = [card for card in candidates if is_basic_energy(card)]
            for word, ptype in (
                ("lightning", PokemonTypes.LIGHTNING),
                ("metal", PokemonTypes.METAL),
            ):
                if f"{word} energy" in text:
                    candidates = [card for card in candidates
                                  if energy_provides_type(card, ptype.value)]
            picks = await ctx.choose_cards(
                candidates, max(1, len(candidates)), minimum=0,
                prompt="Choose Energy cards to attach", display_cards=viewed,
            ) if viewed else []
            for energy in picks:
                targets = [ctx.attacker] if "to this pokémon" in text else \
                    list(ctx.my_pokemon_in_play())
                target = targets[0] if len(targets) == 1 else \
                    await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                    if targets else None
                if target is not None:
                    await ctx.attach_energy(energy, target)
        leftovers = [card for card in viewed if card not in picks]
        if "discard the other cards" in text:
            await ctx.discard_cards(leftovers)
        elif "shuffle the other cards" in text:
            await ctx.shuffle_deck()

    # Viewing/reordering the top of either deck is private to the chooser but
    # still changes pile order when the card says to put them back in order.
    top_look = re.search(
        r"look at the top (\d+) cards? of (either player's|your opponent's|your) deck",
        text,
    )
    if top_look and not handled_top_selection:
        count = int(top_look.group(1))
        owner = ctx.player_id
        if top_look.group(2) == "your opponent's":
            owner = ctx.opponent_id
        elif top_look.group(2) == "either player's":
            choice = await ctx.choose(
                "Choose a deck", ["Your deck", "Opponent's deck"])
            owner = ctx.player_id if choice == 0 else ctx.opponent_id
        if "put them back" in text or "put them back on top" in text:
            await ctx.reorder_deck_top(count, player_id=owner)
        else:
            await ctx.reveal_cards(
                ctx.deck_top(count, owner), to_player=ctx.player_id)

    top_pick = re.search(
        r"look at the top (\d+) cards? of your deck(?:\.| and)? .*?put (\d+|one) of them into your hand",
        text,
    )
    if top_pick:
        top = ctx.deck_top(int(top_pick.group(1)))
        count = 1 if top_pick.group(2) == "one" else int(top_pick.group(2))
        picks = await ctx.choose_cards(
            top, min(count, len(top)), minimum=min(count, len(top)),
            prompt="Choose cards to put into your hand",
        ) if top else []
        await ctx.put_in_hand(picks, reveal=False)
        leftovers = [c for c in top if c not in picks]
        if "discard the other" in text:
            await ctx.discard_cards(leftovers)
        elif leftovers:
            await ctx.shuffle_into_deck(leftovers)

    if any(phrase in text for phrase in (
        "discard a stadium in play", "discard that stadium",
        "discard that stadium card",
    )):
        await ctx.discard_stadium()

    if text.startswith("look through your deck"):
        cards = list(ctx.deck())
        if cards:
            await ctx.session.prompt_view_cards(
                ctx.player_id, ctx.source.entity_id, cards,
                prompt="Your deck",
            )
        await ctx.shuffle_deck()

    if "reveal cards from the top of your deck until you reveal an item card" in text:
        revealed = []
        found = None
        for card in reversed(list(ctx.deck())):
            revealed.append(card)
            if is_item_card(card):
                found = card
                break
        if revealed:
            await ctx.reveal_cards(revealed)
        if found is not None:
            await ctx.put_in_hand([found], reveal=True)
        leftovers = [card for card in revealed if card is not found]
        if leftovers:
            await ctx.shuffle_into_deck(leftovers)

    # Deck-search attacks. Searches preserve private information unless the
    # card explicitly says to reveal the result.
    if "search your deck for" in text:
        search_allowed = not ("if heads" in text and not heads)
        if search_allowed and "card that evolves from" in text \
                and "put it onto" in text:
            target = ctx.attacker
            if text.startswith("choose 1 of your pokémon"):
                target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(),
                                                  "Choose a Pokémon to evolve")
            required_name = None
            if "if shelmet is in play" in text:
                required_name = "Shelmet"
            elif "if karrablast is in play" in text:
                required_name = "Karrablast"
            if required_name and not any(_name(p) == required_name
                                         for p in ctx.my_pokemon_in_play()):
                target = None
            if target is not None:
                logic = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                picks = await ctx.search_deck(
                    lambda c: is_evolution_pokemon(c)
                    and c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic,
                    1, minimum=0, prompt="Choose an Evolution Pokémon",
                )
                if picks:
                    await ctx.evolve_pokemon(target, picks[0])
        elif search_allowed and "put" in text and "onto your bench" in text:
            named = re.search(r"search your deck for (?:as many )?([a-zé'-]+)", text)
            wanted = named.group(1) if named else "pokémon"
            capacity = max(0, effective_bench_capacity(ctx.board, ctx.player_id)
                           - len(ctx.my_bench()))
            count = capacity if "as many" in text else min(1, capacity)
            if count:
                picks = await ctx.search_deck(
                    lambda c: is_basic_pokemon(c)
                    and (wanted == "pokémon" or _name(c).casefold() == wanted.casefold()),
                    count, minimum=0, prompt="Choose Pokémon for your Bench",
                )
                for card in picks:
                    await ctx.bench_pokemon(card)
        elif search_allowed and re.search(
                r"search your deck for .+?\bdiscard (?:it|them|those cards)", text):
            # Private deck-thinning attacks (Critical Error-GX, Slightly
            # Simmer, Spirit Compressor) discard the selected cards.  The
            # former fallback incorrectly placed those selections in hand.
            count = _ability_search_count(text)
            pred = _ability_search_predicate(text)
            picks = await ctx.search_deck(
                pred, count, minimum=0, prompt="Choose cards to discard",
            )
            await ctx.discard_cards(picks)
        elif search_allowed and "attach" in text and "energy" in text:
            # Read the quantity and the complete printed Energy descriptor
            # from the search clause.  The old numeric-only expression missed
            # the ubiquitous “for up to N” wording and silently reduced those
            # attacks to one Energy; it also treated “basic Fire Energy” as
            # unrestricted Energy.
            count = _ability_search_count(text)
            pred = _ability_search_predicate(text) or is_energy_card
            picks = await ctx.search_deck(pred, count, minimum=0,
                                          prompt="Choose Energy cards")
            candidates = list(ctx.my_bench()) if "benched" in text else \
                list(ctx.my_pokemon_in_play())
            target_type = re.search(
                r"to (?:1 of )?your (grass|fire|water|lightning|psychic|"
                r"fighting|darkness|metal|fairy|dragon) pokémon", text,
            )
            if target_type:
                wanted = getattr(PokemonTypes, target_type.group(1).upper())
                candidates = [pokemon for pokemon in candidates
                              if _is_type(pokemon, wanted)]
            one_destination = bool(re.search(r"to (?:1|one) of your ", text))
            fixed_target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Pokémon") \
                if one_destination and candidates else None
            for energy in picks:
                target = ctx.attacker if "to this pokémon" in text else \
                    fixed_target if one_destination else \
                    candidates[0] if len(candidates) == 1 else \
                    await ctx.choose_pokemon(candidates, "Choose a Pokémon") \
                    if candidates else None
                if target is not None:
                    await ctx.attach_energy(energy, target)
        elif search_allowed:
            count_match = re.search(r"for (?:any )?(\d+) ", text)
            count = int(count_match.group(1)) if count_match else 1
            if "pokémon tool" in text:
                pred = is_pokemon_tool
            elif "basic energy" in text:
                pred = is_basic_energy
            elif "fire energy" in text:
                pred = _energy_predicate("fire")
            elif "water pokémon" in text:
                pred = lambda c: _is_type(c, PokemonTypes.WATER)
            elif "dragon pokémon" in text:
                pred = lambda c: _is_type(c, PokemonTypes.DRAGON)
            elif "pokémon with fighting resistance" in text:
                pred = lambda c: is_pokemon_card(c) and c.get_attribute(
                    AttrID.RESISTANCE_TYPES) == PokemonTypes.FIGHTING.value
            elif "pokémon" in text:
                pred = is_pokemon_card
            else:
                pred = None
            picks = await ctx.search_deck(pred, count, minimum=0,
                                          prompt="Choose cards")
            await ctx.put_in_hand(picks, reveal="reveal" in text)
        await ctx.shuffle_deck()

    # Public-discard Pokémon entering either player's Bench.
    if "put a basic pokémon from your opponent's discard pile onto" in text:
        capacity = max(0, effective_bench_capacity(ctx.board, ctx.opponent_id)
                       - len(ctx.opponent_bench()))
        candidates = [card for card in ctx.discard_pile(ctx.opponent_id)
                      if is_basic_pokemon(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a Basic Pokémon") \
            if capacity and candidates else None
        if chosen is not None:
            await ctx.bench_pokemon(chosen)
            counters = re.search(r"put (\d+) damage counters on that pokémon", text)
            if counters:
                await ctx.deal_damage(
                    int(counters.group(1)) * 10, target=chosen,
                    apply_modifiers=False, as_counters=True,
                )

    if "put a basic pokémon from each player's discard pile onto its owner's bench" in text:
        for player_id in (ctx.opponent_id, ctx.player_id):
            bench = ctx.opponent_bench() if player_id == ctx.opponent_id else ctx.my_bench()
            capacity = max(0, effective_bench_capacity(ctx.board, player_id) - len(bench))
            candidates = [card for card in ctx.discard_pile(player_id)
                          if is_basic_pokemon(card)]
            chosen = await _choose_one(
                ctx, candidates, "Choose a Basic Pokémon", player_id=player_id
            ) if capacity and candidates else None
            if chosen is not None:
                await ctx.bench_pokemon(chosen)

    if "put a pokémon from your discard pile onto your bench" in text:
        capacity = max(0, effective_bench_capacity(ctx.board, ctx.player_id)
                       - len(ctx.my_bench()))
        candidates = [card for card in ctx.discard_pile() if is_pokemon_card(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a Pokémon") \
            if capacity and candidates else None
        if chosen is not None:
            await ctx.bench_pokemon(chosen)

    if "put any number of pokémon that evolve from unidentified fossil" in text:
        capacity = max(0, effective_bench_capacity(ctx.board, ctx.player_id)
                       - len(ctx.my_bench()))
        candidates = [
            card for card in ctx.discard_pile()
            if is_pokemon_card(card)
            and "unidentifiedfossil" in str(
                card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) or ""
            ).replace(" ", "").casefold()
        ]
        picks = await ctx.choose_cards(
            candidates, min(capacity, len(candidates)), minimum=0,
            prompt="Choose Pokémon for your Bench",
        ) if candidates and capacity else []
        for card in picks:
            await ctx.bench_pokemon(card)

    # Energy acceleration from hand/discard outside deck-search wording.
    attach = re.search(
        r"attach (up to )?(\d+|an|a) "
        r"((?:basic )?(?:grass |fire |water |lightning |psychic |fighting |"
        r"darkness |metal )?)energy cards? from your (hand|discard pile)",
        text,
    )
    if attach and not ("if heads" in text and not heads):
        count = 1 if attach.group(2) in ("a", "an") else int(attach.group(2))
        pred = _energy_phrase_predicate(attach.group(3))
        zone = ctx.hand() if attach.group(4) == "hand" else ctx.discard_pile()
        cards = [card for card in zone if pred(card)]
        maximum = min(count, len(cards))
        picks = await ctx.choose_cards(
            cards, maximum,
            minimum=0 if attach.group(1) else maximum,
                                       prompt="Choose Energy cards") if cards else []
        fixed_attach_target = None
        fixed_attach_target_chosen = False
        for energy in picks:
            if "to this pokémon" in text:
                target = ctx.attacker
            else:
                candidates = ctx.my_bench() if "benched" in text else ctx.my_pokemon_in_play()
                if "team plasma" in text:
                    candidates = [p for p in candidates if _team_plasma(p)]
                target_type = re.search(
                    r"to (?:1 of )?your (grass|fire|water|lightning|psychic|"
                    r"fighting|darkness|metal|fairy|dragon) pokémon", text,
                )
                if target_type:
                    wanted = getattr(PokemonTypes, target_type.group(1).upper())
                    candidates = [p for p in candidates if _is_type(p, wanted)]
                if "benched pokémon-ex" in text:
                    candidates = [p for p in candidates if _has_subtype(p, "EX")]
                one_destination = bool(re.search(
                    r"to (?:1|one) of your ", text
                ))
                if one_destination and not fixed_attach_target_chosen:
                    fixed_attach_target = candidates[0] if len(candidates) == 1 else \
                        await ctx.choose_pokemon(candidates, "Choose a Pokémon") \
                        if candidates else None
                    fixed_attach_target_chosen = True
                target = fixed_attach_target if one_destination else \
                    candidates[0] if len(candidates) == 1 else \
                    await ctx.choose_pokemon(candidates, "Choose a Pokémon") \
                    if candidates else None
            if target is not None:
                await ctx.attach_energy(energy, target)

    heads_discard_accel = re.search(
        r"attach (?:a number|an amount) of (basic )?"
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal) )?"
        r"energy(?: cards?)? up to the number of heads from your discard pile to "
        r"your benched pokémon", text,
    )
    if heads_discard_accel:
        require_basic, type_word = heads_discard_accel.groups()
        candidates = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if require_basic:
            candidates = [card for card in candidates if is_basic_energy(card)]
        if type_word:
            candidates = [card for card in candidates
                          if _energy_predicate(type_word)(card)]
        maximum = min(heads or 0, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose Energy cards to attach",
        ) if maximum else []
        for energy in picks:
            targets = list(ctx.my_bench())
            if "pokémon-ex" in text:
                targets = [p for p in targets if _has_subtype(p, "EX")]
            target = targets[0] if len(targets) == 1 else \
                await ctx.choose_pokemon(targets, "Choose a Benched Pokémon") \
                if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)

    all_discard_accel = re.search(
        r"attach all "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal) )?"
        r"energy cards from your discard pile to your pokémon", text,
    )
    if all_discard_accel:
        predicate = _energy_predicate(all_discard_accel.group(1)) \
            if all_discard_accel.group(1) else is_energy_card
        cards = [card for card in ctx.discard_pile() if predicate(card)]
        for energy in cards:
            targets = list(ctx.my_pokemon_in_play())
            target = targets[0] if len(targets) == 1 else \
                await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)

    discard_accel = re.search(
        r"(?:search your discard pile for |choose )?(?:up to )?(\d+|all|an?|one) "
        r"((?:basic )?(?:grass |fire |water |lightning |psychic |fighting |"
        r"darkness |metal )?)energy cards?(?: from your discard pile)?.*attach "
        r"(?:them|it) to (.+)", text,
    )
    if discard_accel and "discard pile" in text:
        predicate = _energy_phrase_predicate(discard_accel.group(2))
        candidates = [card for card in ctx.discard_pile() if predicate(card)]
        amount_word = discard_accel.group(1)
        requested = len(candidates) if amount_word == "all" \
            else 1 if amount_word in ("a", "an", "one") else int(amount_word)
        if "up to the number of prize cards your opponent has taken" in text:
            requested = ctx.prizes_taken(ctx.opponent_id)
        if "up to the amount of energy attached to all of your opponent's pokémon" in text:
            requested = sum(_energy_count(ctx, pokemon)
                            for pokemon in ctx.opponent_pokemon_in_play())
        maximum = min(requested, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose Energy cards",
        ) if maximum else []
        target_phrase = discard_accel.group(3)
        source_name = _name(ctx.attacker).casefold()
        named_source = "this pokémon" in target_phrase \
            or bool(source_name and re.search(
                r"(?:^|\b)(?:to )?" + re.escape(source_name) + r"(?:\b|$)",
                target_phrase,
            ))
        targets = [ctx.attacker] if named_source else \
            list(ctx.my_bench()) if "benched" in target_phrase else \
            list(ctx.my_pokemon_in_play())
        for word, ptype in (
            ("grass", PokemonTypes.GRASS), ("fire", PokemonTypes.FIRE),
            ("water", PokemonTypes.WATER), ("lightning", PokemonTypes.LIGHTNING),
            ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
            ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
            ("fairy", PokemonTypes.FAIRY),
        ):
            if f"your {word} pokémon" in target_phrase:
                targets = [pokemon for pokemon in targets
                           if ptype.value in effective_pokemon_types(
                               ctx.board, pokemon)]
                break
        one_destination = named_source or bool(re.search(
            r"(?:to )?(?:1|one) of your ", target_phrase,
        ))
        fixed_target = targets[0] if len(targets) == 1 else \
            await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if one_destination and targets else None
        for energy in picks:
            target = fixed_target if one_destination else \
                targets[0] if len(targets) == 1 else \
                await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)

    # Tail Generator has no printed numeric maximum before "Energy cards";
    # its maximum is instead the opponent's total attached Energy.
    if "choose basic lightning energy cards from your discard pile up to the " \
            "amount of energy attached to all of your opponent's pokémon" in text:
        candidates = [
            card for card in ctx.discard_pile()
            if is_basic_energy(card)
            and energy_provides_type(card, PokemonTypes.LIGHTNING.value)
        ]
        maximum = min(
            len(candidates),
            sum(_energy_count(ctx, pokemon)
                for pokemon in ctx.opponent_pokemon_in_play()),
        )
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose Lightning Energy cards",
        ) if maximum else []
        for energy in picks:
            targets = [
                pokemon for pokemon in ctx.my_pokemon_in_play()
                if PokemonTypes.LIGHTNING.value in effective_pokemon_types(
                    ctx.board, pokemon
                )
            ]
            target = targets[0] if len(targets) == 1 else \
                await ctx.choose_pokemon(targets, "Choose a Lightning Pokémon") \
                if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)

    any_hand_accel = re.search(
        r"(?:attach|you may attach) (?:any number of|as many) "
        r"((?:basic )?(?:grass |fire |water |lightning |psychic |fighting |"
        r"darkness |metal )?)energy cards? (?:as you like )?from your hand", text,
    )
    if any_hand_accel:
        predicate = _energy_phrase_predicate(any_hand_accel.group(1))
        candidates = [card for card in ctx.hand() if predicate(card)]
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose Energy cards to attach",
        ) if candidates else []
        for energy in picks:
            targets = list(ctx.my_pokemon_in_play())
            target = targets[0] if len(targets) == 1 else \
                await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)

    opponent_discard_accel = re.search(
        r"attach (?:up to )?(\d+) energy cards from your opponent's discard "
        r"pile to (?:his or her|their) pokémon", text,
    )
    if opponent_discard_accel:
        candidates = [card for card in ctx.discard_pile(ctx.opponent_id)
                      if is_energy_card(card)]
        maximum = min(int(opponent_discard_accel.group(1)), len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose Energy cards",
        ) if maximum else []
        for energy in picks:
            targets = list(ctx.opponent_pokemon_in_play())
            target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)

    # Top-card/top-five Energy acceleration (Dig Out, Shear).
    top_discard = re.search(r"discard the top (\d+|card) .*?deck", text)
    if top_discard and "attach" in text and "energy" in text:
        count = 1 if top_discard.group(1) == "card" else int(top_discard.group(1))
        top = ctx.deck_top(count)
        await ctx.discard_cards(top)
        energy_type = "fighting" if "fighting energy" in text else "basic"
        energies = [card for card in top if _energy_predicate(energy_type)(card)]
        for energy in energies:
            target = ctx.attacker if "to this pokémon" in text else \
                await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pokémon")
            if target is not None:
                await ctx.attach_energy(energy, target)

    # Hand-reset attacks resolve their whole shuffle before the simultaneous draw.
    if "shuffle your hand into your deck" in text:
        draw = 4
        if "number of cards in your opponent's hand" in text:
            draw = ctx.hand_size(ctx.opponent_id)
        elif "if minun is on your bench" in text and any(
                _name(p) == "Minun" for p in ctx.my_bench()):
            draw = 8
        await _shuffle_hand_draw(ctx, ctx.player_id, draw)
    if "opponent shuffles his or her hand" in text and "draws 4 cards" in text:
        await _shuffle_hand_draw(ctx, ctx.opponent_id, 4)

    opponent_reset = re.search(
        r"opponent shuffles (?:his or her|their) hand into (?:his or her|their) deck "
        r"and draws? (\d+) cards", text,
    )
    if opponent_reset:
        await _shuffle_hand_draw(ctx, ctx.opponent_id,
                                 int(opponent_reset.group(1)))

    # Public-hand interactions.
    if "opponent reveals his or her hand" in text or \
            "opponent reveal his or her hand" in text or \
            "opponent reveals their hand" in text or \
            ("your opponent has" in text and "they reveal their hand" in text):
        hand = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        if "discard all item cards" in text:
            await ctx.discard_cards([c for c in hand if is_item_card(c)])
        elif "discard all supporter cards" in text:
            await ctx.discard_cards([c for c in hand if is_supporter_card(c)])
        elif re.search(r"discard 2 cards from it", text):
            count = min(2, len(hand))
            picks = await ctx.choose_cards(
                hand, count, minimum=count,
                prompt="Choose cards from your opponent's hand to discard",
            ) if count else []
            await ctx.discard_cards(picks)
        elif "discard cards you find there until" in text:
            floor = re.search(r"exactly (\d+) cards", text)
            count = max(0, len(hand) - int(floor.group(1))) if floor else 0
            picks = await ctx.choose_cards(
                hand, count, minimum=count,
                prompt="Choose cards from your opponent's hand to discard",
            ) if count else []
            await ctx.discard_cards(picks)
        elif re.search(
            r"(?:you may )?discard (?:an|a) "
            r"(?:(trainer|item|supporter|pokémon) )?(?:card )?"
            r"(?:you find there|from it)", text,
        ):
            match = re.search(
                r"(?:you may )?discard (?:an|a) "
                r"(?:(trainer|item|supporter|pokémon) )?(?:card )?"
                r"(?:you find there|from it)", text,
            )
            kind = match.group(1)
            predicate = {
                "trainer": is_trainer_card,
                "item": is_item_card,
                "supporter": is_supporter_card,
                "pokémon": is_pokemon_card,
            }.get(kind, lambda card: True)
            candidates = [card for card in hand if predicate(card)]
            picked = await _choose_one(
                ctx, candidates, "Choose a card to discard",
                optional="you may discard" in text,
            ) if candidates else None
            if picked is not None:
                await ctx.discard_cards([picked])
                if "use one of that pokémon's non-gx attacks as this attack" in text:
                    attacks = [
                        attack for attack in (
                            getattr(def_for(picked.archetype_id), "abilities", None) or []
                        ) if isinstance(attack, Attack) and not getattr(attack, "gx", False)
                    ]
                    chosen = await ctx.choose_attack_to_copy(
                        [(picked, attack) for attack in attacks], "Choose an attack",
                    ) if attacks else None
                    if chosen is not None:
                        await ctx.use_attack(chosen[1])
                elif "use the effect of that card as the effect of this attack" in text:
                    await _use_trainer_effect_as_attack(ctx, picked)
        elif "put it on the bottom" in text and hand:
            picked = await _choose_one(ctx, hand, "Choose a card")
            if picked is not None:
                await ctx.put_on_bottom_of_deck(picked)
        elif "put a basic pokémon you find there onto your opponent's bench" in text:
            candidates = [card for card in hand if is_basic_pokemon(card)]
            picked = await _choose_one(ctx, candidates, "Choose a Basic Pokémon") \
                if candidates else None
            if picked is not None:
                await ctx.bench_pokemon(picked)
                counters = re.search(r"put (\d+) damage counters on that pokémon", text)
                if counters:
                    await ctx.deal_damage(
                        int(counters.group(1)) * 10, target=picked,
                        apply_modifiers=False, as_counters=True, is_attack=False,
                    )
    if "choose a random card from your opponent's hand" in text:
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            picked = random.choice(hand)
            await ctx.reveal_cards([picked], to_player=ctx.player_id)
            if "shuffles it into" in text:
                await ctx.shuffle_into_deck([picked], player_id=ctx.opponent_id)
            elif "discard" in text:
                await ctx.discard_cards([picked])
    if "discard a random card from your opponent's hand" in text:
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            picked = random.choice(hand)
            await ctx.reveal_cards([picked])
            await ctx.discard_cards([picked])

    if text.startswith("put a pokémon from your hand face down in front of you"):
        candidates = [card for card in ctx.hand() if is_pokemon_card(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a Pokémon") \
            if candidates else None
        if chosen is not None:
            names = [
                "Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting",
                "Darkness", "Metal", "Fairy", "Dragon", "Colorless",
            ]
            guess = await ctx.choose(
                "Guess that Pokémon's type", names,
                player_id=ctx.opponent_id,
            )
            await ctx.reveal_cards([chosen])
            actual = set(chosen.get_attribute(AttrID.POKEMON_TYPES) or [])
            guessed = getattr(PokemonTypes, names[guess].upper()).value
            await ctx.draw_cards(
                4, player_id=ctx.opponent_id if guessed in actual else ctx.player_id,
            )

    # Simultaneous/plain draw attacks.
    both_draw = re.search(r"each player draws (\d+|a) cards?", text)
    if both_draw:
        count = 1 if both_draw.group(1) == "a" else int(both_draw.group(1))
        await ctx.draw_cards(count)
        await ctx.draw_cards(count, player_id=ctx.opponent_id)
    if "each player draws and reveals the top card of his or her deck" in text:
        for player_id in (ctx.player_id, ctx.opponent_id):
            cards = ctx.deck_top(1, player_id)
            if cards:
                await ctx.draw_cards(1, player_id=player_id)
                await ctx.reveal_cards(cards)
    if "draw cards until you have the same number of cards in your hand as your opponent" in text:
        await ctx.draw_until(ctx.hand_size(ctx.opponent_id))

    # Opponent-selected or random hand loss.
    hand_floor = re.search(
        r"discard (?:random )?cards from your opponent's hand .*until (?:he or she|they) "
        r"(?:has|have) (\d+) cards", text)
    if hand_floor:
        hand = list(ctx.hand(ctx.opponent_id))
        excess = max(0, len(hand) - int(hand_floor.group(1)))
        if excess:
            chosen = random.sample(hand, excess) if "random" in text else \
                await ctx.choose_cards(
                    hand, excess, prompt="Choose cards to discard",
                    player_id=ctx.opponent_id)
            await ctx.discard_cards(chosen)
    if "your opponent discards a card from" in text \
            or "your opponent puts a card from" in text and "bottom" in text:
        hand = list(ctx.hand(ctx.opponent_id))
        chosen = await _choose_one(
            ctx, hand, "Choose a card", player_id=ctx.opponent_id) if hand else None
        if chosen is not None:
            if "bottom" in text:
                await ctx.put_on_bottom_of_deck(chosen)
            else:
                await ctx.discard_cards([chosen])

    opponent_fixed_discard = re.search(
        r"your opponent (?:chooses|discards) (\d+) cards from their hand", text,
    )
    if opponent_fixed_discard:
        hand = list(ctx.hand(ctx.opponent_id))
        count = min(int(opponent_fixed_discard.group(1)), len(hand))
        picks = await ctx.choose_cards(
            hand, count, minimum=count, prompt="Choose cards to discard",
            player_id=ctx.opponent_id,
        ) if count else []
        if "shuffles those cards into their deck" in text:
            await ctx.shuffle_into_deck(picks, player_id=ctx.opponent_id)
        else:
            await ctx.discard_cards(picks)

    random_shuffle = re.search(
        r"choose (\d+) random cards from your opponent's hand.*shuffles them into their deck",
        text,
    )
    if random_shuffle:
        hand = list(ctx.hand(ctx.opponent_id))
        picks = random.sample(hand, min(int(random_shuffle.group(1)), len(hand)))
        if picks:
            await ctx.reveal_cards(picks)
            await ctx.shuffle_into_deck(picks, player_id=ctx.opponent_id)

    opponent_coin_discard = re.search(
        r"opponent flips (\d+) coins.*for each tails.*discards a card from",
        text,
    )
    if opponent_coin_discard:
        results = await ctx.flip_coins(int(opponent_coin_discard.group(1)), ctx.ability.title)
        count = min(sum(not bool(result) for result in results),
                    ctx.hand_size(ctx.opponent_id))
        if count:
            await ctx.discard_from_hand(
                count, player_id=ctx.opponent_id,
                prompt="Choose cards to discard",
            )

    if "choose a player. that player shuffles their hand into their deck and draws 4 cards" in text:
        index = await ctx.choose("Choose a player", ["You", "Opponent"])
        chosen_player = ctx.player_id if index == 0 else ctx.opponent_id
        await _shuffle_hand_draw(ctx, chosen_player, 4)

    if "each player either draws or discards cards until that player has 4 cards" in text:
        for player_id in (ctx.opponent_id, ctx.player_id):
            size = ctx.hand_size(player_id)
            if size < 4:
                await ctx.draw_cards(4 - size, player_id=player_id)
            elif size > 4:
                await ctx.discard_from_hand(
                    size - 4, player_id=player_id,
                    prompt="Choose cards to discard",
                )

    # Public discard recovery, including mixed Item/Tool and arbitrary-card
    # wordings used by older sets and GX attacks.
    recovery = re.search(
        r"put (?:up to )?(\d+) (?:in any combination of )?(.+?) "
        r"(?:cards? )?from your discard pile into your hand", text)
    if recovery:
        count, descriptor = int(recovery.group(1)), recovery.group(2)
        candidates = list(ctx.discard_pile())
        if "item" in descriptor or "pokémon tool" in descriptor:
            candidates = [card for card in candidates if
                          ("item" in descriptor and is_item_card(card)) or
                          ("pokémon tool" in descriptor and is_pokemon_tool(card))]
        elif "supporter" in descriptor:
            candidates = [card for card in candidates if is_supporter_card(card)]
        elif "energy" in descriptor:
            candidates = [card for card in candidates if is_energy_card(card)]
        elif "pokémon" in descriptor:
            candidates = [card for card in candidates if is_pokemon_card(card)]
        maximum = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0 if "up to" in text else maximum,
            prompt="Choose cards from your discard pile") if maximum else []
        await ctx.put_in_hand(picks, reveal=True)

    # Put Basic/typed Pokemon from a public discard directly onto the Bench.
    bench_from_discard = re.search(
        r"put (?:up to )?(\d+|a) (?:in any combination of )?(.+?) pokémon"
        r"(?:-[a-z]+)? from (?:either player's|your) discard pile onto (?:its owner's|your) bench",
        text)
    if bench_from_discard:
        maximum = 1 if bench_from_discard.group(1) == "a" \
            else int(bench_from_discard.group(1))
        descriptor = bench_from_discard.group(2)
        pools = list(ctx.discard_pile())
        if "either player's" in text:
            pools += list(ctx.discard_pile(ctx.opponent_id))
        candidates = [card for card in pools if is_pokemon_card(card)]
        if "basic" in descriptor:
            candidates = [card for card in candidates if is_basic_pokemon(card)]
        for word, ptype in (("fire", PokemonTypes.FIRE),
                            ("psychic", PokemonTypes.PSYCHIC),
                            ("dragon", PokemonTypes.DRAGON)):
            if word in descriptor:
                candidates = [card for card in candidates if _is_type(card, ptype)]
        picks = await ctx.choose_cards(
            candidates, min(maximum, len(candidates)), minimum=0,
            prompt="Choose Pokémon for the Bench") if candidates else []
        for pokemon in picks:
            await ctx.bench_pokemon(pokemon)

    # All-damage heals not covered by the numeric templates.
    if "heal all damage from 1 of your benched pokémon" in text:
        candidates = [p for p in ctx.my_bench() if _damaged(ctx, p)]
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") \
            if candidates else None
        if target is not None:
            await ctx.heal(ctx.max_hp(target), target)
    if "heal all damage from all of your" in text \
            or "heal all damage from each of your" in text:
        candidates = list(ctx.my_pokemon_in_play())
        for word, ptype in (("water", PokemonTypes.WATER),
                            ("tera", None), ("basic", None)):
            if f"your {word} pokémon" in text:
                if ptype is not None:
                    candidates = [p for p in candidates if _is_type(p, ptype)]
                elif word == "basic":
                    candidates = [p for p in candidates if is_basic_pokemon(p)]
                elif word == "tera":
                    candidates = [p for p in candidates if "Tera" in set(
                        getattr(def_for(p.archetype_id), "subtypes", []) or [])]
                break
        for pokemon in candidates:
            await ctx.heal(ctx.max_hp(pokemon), pokemon)

    # Attached Tool/Special Energy cleanup across one or both boards.
    if "discard" in text and ("pokémon tool" in text or "special energy" in text):
        opposing_only = "your opponent's" in text or "defending pokémon" in text
        pokemon = ctx.opponent_pokemon_in_play() if opposing_only else \
            ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        attachments = [
            card for target in pokemon for card in full_stack(target)[1:]
            if ("pokémon tool" in text and is_pokemon_tool(card))
            or ("special energy" in text and is_special_energy(card))
        ]
        if "defending pokémon" in text:
            attachments = [card for card in full_stack(ctx.defender)[1:]
                           if ("pokémon tool" in text and is_pokemon_tool(card))
                           or ("special energy" in text and is_special_energy(card))]
        maximum = len(attachments)
        up_to = re.search(r"discard up to (\d+)", text)
        if up_to:
            maximum = min(maximum, int(up_to.group(1)))
            attachments = await ctx.choose_cards(
                attachments, maximum, minimum=0,
                prompt="Choose cards to discard") if attachments else []
        elif maximum == 1 or "discard all" in text:
            pass
        elif attachments:
            chosen = await _choose_one(ctx, attachments, "Choose a card to discard")
            attachments = [chosen] if chosen is not None else []
        await ctx.discard_cards(attachments)

    # Typed Energy removal from the Defending Pokemon.
    energy_remove = re.search(
        r"discard an? (grass|fire|water|lightning|psychic|fighting|darkness|metal)? ?"
        r"energy (?:card )?attached to (?:the )?defending pokémon", text)
    if energy_remove:
        ptype = getattr(PokemonTypes, (energy_remove.group(1) or "").upper(), None)
        await ctx.discard_energy_from(
            ctx.defender, 1,
            predicate=(lambda card, ptype=ptype: energy_provides_type(
                card, ptype.value)) if ptype is not None else None)

    # Choice between two Special Conditions.
    special_choice = re.search(r"choose either (asleep|poisoned) or (asleep|poisoned)", text)
    if special_choice and ctx.defender is not None:
        words = list(special_choice.groups())
        picked = await ctx.choose("Choose a Special Condition", words)
        await ctx.apply_special_condition(ctx.defender, condition_map[words[picked]])

    # Information-only peeks must still expose the cards to the chooser.
    if "look at your face-down prize cards" in text:
        area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        await ctx.reveal_cards(list(area.children) if area else [],
                               to_player=ctx.player_id)
    if "look at 1 of your face-down prize cards" in text:
        area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        cards = list(area.children) if area else []
        chosen = await _choose_one(ctx, cards, "Choose a Prize card") \
            if cards else None
        if chosen is not None:
            await ctx.reveal_cards([chosen], to_player=ctx.player_id)
    if "look at 1 of your opponent's face-down prize cards" in text:
        area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
        cards = list(area.children) if area else []
        chosen = await _choose_one(ctx, cards, "Choose a Prize card") if cards else None
        if chosen is not None:
            await ctx.reveal_cards([chosen], to_player=ctx.player_id)

    if "turn all of your prize cards face up" in text:
        area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        prizes = list(area.children) if area else []
        if prizes:
            await ctx.reveal_cards(prizes)
            for prize in prizes:
                prize.publicly_revealed = True

    take_prize = re.search(r"(?:take|and take) (?:a|1|one) prize card", text)
    if take_prize:
        await ctx.take_prizes(1)

    if "count your prize cards and put them into your hand" in text:
        area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        prizes = list(area.children) if area else []
        count = len(prizes)
        if len(ctx.deck()) >= count:
            await ctx.put_in_hand(prizes, reveal=False)
            await ctx.put_in_prizes(ctx.deck_top(count))

    if "both players shuffle their prize cards into their decks" in text \
            and "top 3 cards" in text:
        for player_id in ctx.board.player_ids:
            area = ctx.board.find_player_area(player_id, "prizePile")
            prizes = list(area.children) if area else []
            if prizes:
                await ctx.shuffle_into_deck(prizes, player_id=player_id)
            await ctx.put_in_prizes(
                ctx.deck_top(3, player_id), player_id=player_id
            )

    add_prizes = re.search(
        r"add the top (\d+) cards? of your opponent's deck to (?:his or her|their) prize cards",
        text,
    )
    if add_prizes:
        await ctx.put_in_prizes(
            ctx.deck_top(int(add_prizes.group(1)), ctx.opponent_id),
            player_id=ctx.opponent_id,
        )

    if "add a card from your opponent's discard pile to their prize cards" in text:
        cards = list(ctx.discard_pile(ctx.opponent_id))
        chosen = await _choose_one(ctx, cards, "Choose a card") if cards else None
        if chosen is not None:
            await ctx.put_in_prizes([chosen], player_id=ctx.opponent_id)

    if "discard 1 of your prize cards" in text:
        area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        prizes = list(area.children) if area else []
        chosen = await _choose_one(ctx, prizes, "Choose a Prize card") \
            if prizes else None
        if chosen is not None:
            await ctx.reveal_cards([chosen])
            if is_energy_card(chosen):
                targets = list(ctx.my_pokemon_in_play())
                target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                    if targets else None
                if target is not None:
                    await ctx.attach_energy(chosen, target)
            else:
                await ctx.discard_cards([chosen])

    # Mass devolution attacks.
    if "devolve each of your opponent's evolved pokémon" in text:
        destination = "deck" if "shuffling the highest stage" in text else "hand"
        for pokemon in list(ctx.opponent_pokemon_in_play()):
            if is_evolution_pokemon(pokemon):
                await ctx.devolve_pokemon(pokemon, 1, destination=destination)
        if destination == "deck":
            await ctx.shuffle_deck(ctx.opponent_id)
    if "devolve as many of your benched pokémon as many times as you like" in text:
        for pokemon in list(ctx.my_bench()):
            while is_evolution_pokemon(pokemon) and await ctx.ask_yes_no(
                    f"Devolve {_name(pokemon)}?"):
                removed = await ctx.devolve_pokemon(pokemon, 1, destination="hand")
                if not removed:
                    break
    if "devolve any number of your benched pokémon as many times as you like" in text:
        candidates = [pokemon for pokemon in ctx.my_bench()
                      if is_evolution_pokemon(pokemon)]
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose Pokémon to devolve",
        ) if candidates else []
        for pokemon in picks:
            while is_evolution_pokemon(pokemon) and await ctx.ask_yes_no(
                    f"Devolve {_name(pokemon)} again?"):
                removed = await ctx.devolve_pokemon(
                    pokemon, 1, destination="hand"
                )
                if not removed:
                    break

    time_hollow = re.search(
        r"choose a number of your opponent's stage 1 or stage 2 evolved "
        r"pokémon up to the amount of energy attached to [a-z0-9 .'-]+", text,
    )
    if time_hollow:
        targets = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                   if is_evolution_pokemon(pokemon)]
        maximum = min(_energy_count(ctx, ctx.attacker), len(targets))
        picks = await ctx.choose_cards(
            targets, maximum, minimum=0,
            prompt="Choose Pokémon to devolve",
        ) if maximum else []
        for pokemon in picks:
            await ctx.devolve_pokemon(pokemon, 1, destination="hand")

    if "devolve 1 of your opponent's evolved pokémon" in text \
            and "shuffles that card into their deck" in text:
        targets = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                   if is_evolution_pokemon(pokemon)]
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon to devolve") \
            if targets else None
        if target is not None:
            await ctx.devolve_pokemon(target, 1, destination="deck")
            await ctx.shuffle_deck(ctx.opponent_id)

    # Whole stacks selected from play and returned/shuffled/discarded.
    if "put 1 of your benched pokémon and all" in text and "into your hand" in text:
        target = await ctx.choose_pokemon(ctx.my_bench(), "Choose a Benched Pokémon") \
            if ctx.my_bench() else None
        if target is not None:
            await ctx.put_in_hand(full_stack(target), reveal=False)
    if "return 1 of your pokémon and all cards attached to it" in text \
            and "your hand" in text:
        targets = list(ctx.my_pokemon_in_play())
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if targets else None
        if target is not None:
            await ctx.put_in_hand(full_stack(target), reveal=False)
    if "shuffle 1 of your benched pokémon and all attached cards into your deck" in text:
        target = await ctx.choose_pokemon(ctx.my_bench(), "Choose a Benched Pokémon") \
            if ctx.my_bench() else None
        if target is not None:
            await ctx.shuffle_into_deck(full_stack(target))
    if "choose 2 of your opponent's benched pokémon" in text \
            and "shuffle those pokémon and all attached cards" in text:
        bench = list(ctx.opponent_bench())
        picked = await ctx.choose_cards(
            bench, min(2, len(bench)), minimum=min(2, len(bench)),
            prompt="Choose Benched Pokémon") if bench else []
        await ctx.shuffle_into_deck(
            [card for pokemon in picked for card in full_stack(pokemon)],
            player_id=ctx.opponent_id)
    if "choose 1 of your opponent's benched pokémon" in text \
            and ("shuffle that pokémon and all" in text
                 or "shuffles that pokémon and all" in text):
        bench = list(ctx.opponent_bench())
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon") \
            if bench else None
        if target is not None:
            await ctx.shuffle_into_deck(full_stack(target), player_id=ctx.opponent_id)
            if "then shuffle this pokémon" in text:
                await ctx.shuffle_into_deck(full_stack(ctx.attacker))
    if "choose 1 of your opponent's pokémon" in text \
            and ("shuffles that pokémon and all cards attached to it into their deck" in text
                 or "shuffle that pokémon and all attached cards into their deck" in text) \
            and not ("if heads" in text and not heads):
        targets = list(ctx.opponent_pokemon_in_play())
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if targets else None
        if target is not None:
            await ctx.shuffle_into_deck(
                full_stack(target), player_id=ctx.opponent_id
            )
    if "put 1 of your opponent's benched pokémon and all cards attached" in text \
            and "into your opponent's hand" in text:
        bench = list(ctx.opponent_bench())
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon") \
            if bench else None
        if target is not None:
            await ctx.put_in_hand(full_stack(target), reveal=False)

    # Equivalent modern/historical stack wording.
    bench_stack_shuffle = re.search(
        r"shuffle 1 of your opponent's benched pokémon(?: that has any damage "
        r"counters on it)? and (?:all cards attached to it|all attached cards) "
        r"into their deck", text,
    )
    if bench_stack_shuffle:
        targets = list(ctx.opponent_bench())
        if "has any damage counters" in bench_stack_shuffle.group(0):
            targets = [pokemon for pokemon in targets
                       if _damage_counter_count(ctx, pokemon)]
        target = await ctx.choose_pokemon(targets, "Choose a Benched Pokémon") \
            if targets else None
        if target is not None:
            await ctx.shuffle_into_deck(full_stack(target), player_id=ctx.opponent_id)

    bench_stack_hand = re.search(
        r"(?:choose (\d+) of |put (\d+) of )(?:your )?opponent's benched pokémon.*"
        r"all cards attached to (?:them|it).*into (?:your )?opponent's hand", text,
    )
    if bench_stack_hand:
        count = int(bench_stack_hand.group(1) or bench_stack_hand.group(2) or 1)
        bench = list(ctx.opponent_bench())
        count = min(count, len(bench))
        picks = await ctx.choose_cards(
            bench, count, minimum=count, prompt="Choose Benched Pokémon"
        ) if count else []
        for target in picks:
            await ctx.put_in_hand(full_stack(target), reveal=False)

    if "choose 1 of your opponent's benched pokémon" in text \
            and "put that pokémon and all cards attached to it back to your opponent's hand" in text:
        targets = list(ctx.opponent_bench())
        target = await ctx.choose_pokemon(targets, "Choose a Benched Pokémon") \
            if targets else None
        if target is not None:
            await ctx.put_in_hand(full_stack(target), reveal=False)

    if "put any number of your pokémon in play and all cards attached to them into your hand" in text:
        candidates = list(ctx.my_pokemon_in_play())
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose Pokémon to return to your hand",
        ) if candidates else []
        for target in picks:
            await ctx.put_in_hand(full_stack(target), reveal=False)

    if "the defending pokémon and all cards attached to it in the lost zone" in text \
            or "opponent's active pokémon and all cards attached to it in the lost zone" in text:
        await ctx.move_to_lost_zone(full_stack(ctx.defender))
    if "put this pokémon and all cards attached to it in the lost zone" in text:
        await ctx.move_to_lost_zone(full_stack(ctx.attacker))

    lost_attacker_energy = re.search(
        r"put (1|all) energy(?: cards?)? (?:attached to|from) "
        r"(?:this pokémon|[a-z0-9 &'’.-]+) in the lost zone", text,
    )
    if lost_attacker_energy:
        energies = list(ctx.attached_energies(ctx.attacker))
        if lost_attacker_energy.group(1) == "all":
            picks = energies
        else:
            chosen = await _choose_one(
                ctx, energies, "Choose an Energy to put in the Lost Zone",
            ) if energies else None
            picks = [chosen] if chosen is not None else []
        if picks:
            await ctx.move_to_lost_zone(picks)

    lost_defender_energy = re.search(
        r"put (\d+|an|a) energy(?: cards?)? (?:attached to|from) "
        r"(?:the )?defending pokémon in the lost zone", text,
    )
    if lost_defender_energy:
        count = 1 if lost_defender_energy.group(1) in ("a", "an") \
            else int(lost_defender_energy.group(1))
        energies = list(ctx.attached_energies(ctx.defender))
        picks = await ctx.choose_cards(
            energies, min(count, len(energies)),
            minimum=min(count, len(energies)),
            prompt="Choose Energy cards to put in the Lost Zone",
        ) if energies else []
        if picks:
            await ctx.move_to_lost_zone(picks)

    if "put the top card of your opponent's deck in the lost zone" in text:
        await ctx.move_to_lost_zone(ctx.deck_top(1, ctx.opponent_id))

    if "put a card from your hand in the lost zone" in text:
        chosen = await _choose_one(
            ctx, list(ctx.hand()), "Choose a card to put in the Lost Zone",
        ) if ctx.hand() else None
        if chosen is not None:
            await ctx.move_to_lost_zone([chosen])
            if "if you do, draw 3 cards" in text:
                await ctx.draw_cards(3)

    if "pokémon you find there up to the number of psychic energy attached" in text \
            and "put the pokémon you chose in the lost zone" in text:
        hand = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        candidates = [card for card in hand if is_pokemon_card(card)]
        maximum = min(
            len(candidates), _energy_count(ctx, ctx.attacker, "psychic"),
        )
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose Pokémon to put in the Lost Zone",
        ) if maximum else []
        if picks:
            await ctx.move_to_lost_zone(picks)
    if "opponent puts their active pokémon and all cards attached to it into their hand" in text:
        await ctx.put_in_hand(full_stack(ctx.defender), reveal=False)

    if "shuffle this pokémon and all attached cards into your deck" in text:
        await ctx.shuffle_into_deck(full_stack(ctx.attacker))

    if "shuffle all energy from each of your opponent's pokémon into their deck" in text:
        cards = [energy for pokemon in ctx.opponent_pokemon_in_play()
                 for energy in ctx.attached_energies(pokemon)]
        if cards:
            await ctx.shuffle_into_deck(cards, player_id=ctx.opponent_id)

    if "you may have your opponent shuffle their deck" in text \
            and await ctx.ask_yes_no("Shuffle your opponent's deck?"):
        await ctx.shuffle_deck(ctx.opponent_id)

    astonish = re.search(
        r"(?:choose (\d+) cards?|if heads, choose (\d+) card) from your "
        r"opponent's hand without looking.*shuffle (?:those cards|that card) "
        r"into (?:his or her|their) deck", text,
    )
    if astonish and not ("if heads" in text and not heads):
        count = int(astonish.group(1) or astonish.group(2) or 1)
        hand = list(ctx.hand(ctx.opponent_id))
        picks = random.sample(hand, min(count, len(hand))) if hand else []
        if picks:
            await ctx.reveal_cards(picks, to_player=ctx.player_id)
            await ctx.shuffle_into_deck(picks, player_id=ctx.opponent_id)

    shuffle_discard_energy = re.search(
        r"(?:then, )?shuffle (?:those|the) "
        r"(?:(basic )?(grass|fire|water|lightning|psychic|fighting|darkness|metal)? ?"
        r"energy cards?) into your deck", text,
    )
    if shuffle_discard_energy:
        require_basic, type_word = shuffle_discard_energy.groups()
        cards = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if require_basic:
            cards = [card for card in cards if is_basic_energy(card)]
        if type_word:
            predicate = _energy_predicate(type_word)
            cards = [card for card in cards if predicate(card)]
        if cards:
            await ctx.shuffle_into_deck(cards)
    elif "then, shuffle those cards into your deck" in text \
            and "energy card" in text and "discard pile" in text:
        cards = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if "basic energy" in text:
            cards = [card for card in cards if is_basic_energy(card)]
        for word in (
            "grass", "fire", "water", "lightning", "psychic", "fighting",
            "darkness", "metal", "fairy",
        ):
            if f"{word} energy" in text:
                cards = [card for card in cards if _energy_predicate(word)(card)]
                break
        if cards:
            await ctx.shuffle_into_deck(cards)

    if "shuffle each player's active pokémon and all attached cards into their deck" in text:
        for target in (ctx.attacker, ctx.defender):
            if target is not None:
                await ctx.shuffle_into_deck(
                    full_stack(target), player_id=target.owning_player_id
                )

    if "shuffle all cards attached to each player's pokémon into that player's deck" in text:
        for player_id in ctx.board.player_ids:
            attachments = [card for pokemon in ctx.board.pokemon_in_play(player_id)
                           for card in full_stack(pokemon)[1:]]
            if attachments:
                await ctx.shuffle_into_deck(attachments, player_id=player_id)

    if "choose 3 of your opponent's benched pokémon" in text \
            and "didn't choose" in text and "shuffle" in text:
        bench = list(ctx.opponent_bench())
        keep_count = min(3, len(bench))
        kept = await ctx.choose_cards(
            bench, keep_count, minimum=keep_count,
            prompt="Choose Pokémon to keep on the Bench",
        ) if keep_count else []
        for target in [pokemon for pokemon in bench if pokemon not in kept]:
            await ctx.shuffle_into_deck(full_stack(target), player_id=ctx.opponent_id)

    discard_targets = re.search(
        r"(?:discard|choose) (\d+) of your opponent's pokémon and all cards "
        r"attached to it", text,
    )
    if discard_targets:
        targets = list(ctx.opponent_pokemon_in_play())
        count = min(int(discard_targets.group(1)), len(targets))
        picks = await ctx.choose_cards(
            targets, count, minimum=count, prompt="Choose Pokémon to discard",
        ) if count else []
        for target in picks:
            await ctx.discard_cards(full_stack(target))
    if "shuffle your opponent's active pokémon and all cards attached" in _norm(
            getattr(ctx.ability, "game_text", "")):
        if ctx.opponent_bench():
            await ctx.shuffle_into_deck(
                full_stack(ctx.defender), player_id=ctx.opponent_id)
    raw_text = _norm(getattr(ctx.ability, "game_text", ""))
    if "your opponent shuffles their active pokémon and all cards attached" in raw_text:
        requires_last_gx = "used a gx attack during their last turn" in raw_text
        used_gx = False
        if requires_last_gx:
            for _entity_id, archetype_id, attack_title in \
                    ctx.session.turn_state.attacks_used_last_turn:
                definition = def_for(archetype_id)
                attack = next((candidate for candidate in (
                    getattr(definition, "abilities", None) or []
                ) if isinstance(candidate, Attack)
                    and candidate.title == attack_title), None)
                if attack is not None and getattr(attack, "gx", False):
                    used_gx = True
                    break
        if not requires_last_gx or used_gx:
            await ctx.shuffle_into_deck(
                full_stack(ctx.defender), player_id=ctx.opponent_id
            )
    discard_active_stack = _norm(getattr(ctx.ability, "game_text", ""))
    if any(phrase in discard_active_stack for phrase in (
            "discard your opponent's active pokémon and all cards attached",
            "discard your opponent's active pokémon and all attached cards",
    )):
        needs_loudred = "didn't evolve from loudred during this turn" in raw_text
        evolved_from_loudred = any(
            _name(card).casefold() == "loudred"
            for card in full_stack(ctx.attacker)[1:]
        ) and ctx.session.turn_state.entered_play_turn.get(
            ctx.attacker.entity_id
        ) == ctx.session.turn_state.turn_number
        if not needs_loudred or evolved_from_loudred:
                await ctx.discard_cards(full_stack(ctx.defender))

    if "devolve" in text and "evolved pokémon" in text \
            and "your benched pokémon" not in text:
        candidates = [
            pokemon for pokemon in ctx.opponent_pokemon_in_play()
            if any(isinstance(card, PokemonEntity)
                   for card in full_stack(pokemon)[1:])
        ]
        if "defending pokémon" in text:
            target = ctx.defender if ctx.defender in candidates else None
        else:
            target = await ctx.choose_pokemon(
                candidates, "Choose an evolved Pokémon",
            ) if candidates else None
        if target is not None:
            stages = sum(isinstance(card, PokemonEntity)
                         for card in full_stack(target)[1:])
            await ctx.devolve_pokemon(
                target, steps=stages if "all of the evolution cards" in text else 1,
            )

    if "devolve any number of your benched pokémon as many times as you like" in text:
        candidates = [
            pokemon for pokemon in ctx.my_bench()
            if any(isinstance(card, PokemonEntity)
                   for card in full_stack(pokemon)[1:])
        ]
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Choose Pokémon to devolve",
        ) if candidates else []
        for target in picks:
            stages = sum(isinstance(card, PokemonEntity)
                         for card in full_stack(target)[1:])
            if stages <= 0:
                continue
            if stages == 1:
                steps = 1
            else:
                choice = await ctx.choose(
                    "How many times should this Pokémon devolve?",
                    [str(value) for value in range(1, stages + 1)],
                )
                steps = choice + 1
            await ctx.devolve_pokemon(target, steps=steps)

    # Consolidate Energy from the Bench onto the attacker.
    if ("move any number of energy from your benched pokémon to this pokémon" in text
            or "move as many energy as you like from your benched pokémon to this pokémon" in text):
        await ctx.move_energy_freely(
            ctx.my_bench(), [ctx.attacker], max_count=None,
            prompt="Choose Energy to move")

    # Cards/stacks leaving play.
    if "shuffle this pokémon and all cards attached to it into your deck" in text:
        await ctx.shuffle_into_deck(full_stack(ctx.attacker))
    source_name = _name(ctx.attacker).casefold()
    if source_name and re.search(
        rf"shuffle {re.escape(source_name)} and all cards attached to it back into your deck",
        text,
    ):
        await ctx.shuffle_into_deck(full_stack(ctx.attacker))
    if "opponent shuffles the defending pokémon and all cards attached" in text:
        await ctx.shuffle_into_deck(full_stack(ctx.defender), player_id=ctx.opponent_id)
    if "return this pokémon and all cards attached to it to your hand" in text:
        if "you may" not in text or await ctx.ask_yes_no("Return this Pokémon to your hand?"):
            await ctx.put_in_hand(full_stack(ctx.attacker), reveal=False)
    if (
        "put this pokémon and all attached cards into your hand" in text
        or "put this pokémon and all cards attached to it into your hand" in text
    ):
        await ctx.put_in_hand(full_stack(ctx.attacker), reveal=False)
    if source_name and re.search(
            rf"return {re.escape(source_name)} and all cards attached to it to your hand",
            text):
        await ctx.put_in_hand(full_stack(ctx.attacker), reveal=False)
    if "put this pokémon into your hand" in text \
            and "discard all cards attached to this pokémon" in text:
        evolution_cards, attachments = split_pokemon_stack(ctx.attacker)
        if attachments:
            await ctx.discard_cards(attachments)
        await ctx.put_in_hand(evolution_cards, reveal=False)
    if "devolve the defending pokémon" in text:
        await ctx.devolve_pokemon(ctx.defender, 1, destination="hand")

    # Recurring attacks return one or more attached Energy cards.  Historical
    # printings alternate freely between "put ... into" and "return ... to";
    # resolve both wordings from the actual stack and let the player choose
    # which cards move when more than one candidate exists.
    own_energy_to_hand = re.search(
        r"(?:you may )?(?:put|return) (all|\d+|an|a) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
        r"energy(?: cards?)? (?:attached to|from) (?:this pokémon|[a-z0-9 &'’.-]+) "
        r"(?:into|to) your hand",
        text,
    )
    if own_energy_to_hand:
        raw_count, type_word = own_energy_to_hand.groups()
        predicate = _energy_predicate(type_word) if type_word else is_energy_card
        candidates = [energy for energy in ctx.attached_energies(ctx.attacker)
                      if predicate(energy)]
        count = len(candidates) if raw_count == "all" else \
            1 if raw_count in ("a", "an") else int(raw_count)
        count = min(count, len(candidates))
        minimum = 0 if "you may" in own_energy_to_hand.group(0) else count
        picks = await ctx.choose_cards(
            candidates, count, minimum=minimum,
            prompt="Choose Energy cards to put into your hand",
        ) if count else []
        if picks:
            await ctx.put_in_hand(picks, reveal=False)

    opposing_energy_to_hand = re.search(
        r"(?:you may )?(?:put|return) (all|\d+|an|a) "
        r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
        r"energy(?: cards?)? attached to (?:(?:the )?defending pokémon"
        r"(?: stage [12])?|your opponent's active(?: stage [12])? pokémon) "
        r"(?:into|to) (?:their|your opponent's) hand",
        text,
    )
    if opposing_energy_to_hand and ctx.defender is not None:
        raw_count, type_word = opposing_energy_to_hand.groups()
        predicate = _energy_predicate(type_word) if type_word else is_energy_card
        candidates = [energy for energy in ctx.attached_energies(ctx.defender)
                      if predicate(energy)]
        count = len(candidates) if raw_count == "all" else \
            1 if raw_count in ("a", "an") else int(raw_count)
        count = min(count, len(candidates))
        minimum = 0 if "you may" in opposing_energy_to_hand.group(0) else count
        picks = await ctx.choose_cards(
            candidates, count, minimum=minimum,
            prompt="Choose Energy cards to return to your opponent's hand",
        ) if count else []
        if picks:
            await ctx.put_in_hand(picks, reveal=False)

    # Explicit knockout attacks.  These bypass damage calculation but still
    # enter the ordinary simultaneous-KO/prize resolver through ctx.knockouts.
    if ctx.defender is not None:
        defender_stage = ctx.defender.get_attribute(AttrID.STAGE)
        defender_conditions = ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        counters = _damage_counter_count(ctx, ctx.defender)
        should_ko = False
        if "defending pokémon is affected by a special condition, it is knocked out" in text:
            should_ko = bool(defender_conditions)
        if "defending pokémon is asleep, it is knocked out" in text:
            should_ko = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP] \
                in defender_conditions
        if "defending pokémon is a basic pokémon, it is knocked out" in text:
            should_ko = defender_stage == PokemonStage.BASIC.value
        if "defending pokémon has any special energy attached, it is knocked out" in text:
            should_ko = any(is_special_energy(e)
                            for e in ctx.attached_energies(ctx.defender))
        if "defending pokémon is an ultra beast, it is knocked out" in text:
            should_ko = "Ultra Beast" in (
                getattr(def_for(ctx.defender.archetype_id), "subtypes", None) or []
            )
        if "and knock out the defending pokémon" in text:
            should_ko = hand_discard_paid
        threshold = re.search(
            r"defending pokémon has (?:exactly |)(\d+) or more damage counters .*knocked out",
            text,
        )
        if threshold:
            should_ko = counters >= int(threshold.group(1))
        exact = re.search(
            r"defending pokémon has exactly (\d+) damage counters .*knocked out", text
        )
        if exact:
            should_ko = counters == int(exact.group(1))
        if should_ko:
            await ctx.knock_out(ctx.defender)

    if "discard an energy from the defending pokémon ex" in text \
            and ctx.defender is not None:
        subtypes = set(getattr(
            def_for(ctx.defender.archetype_id), "subtypes", None
        ) or [])
        if "ex" in subtypes:
            await ctx.discard_energy_from(ctx.defender, 1)

    hand_ko_cost = re.search(
        r"discard (\d+) basic ([a-z]+) energy cards from your hand, and knock "
        r"out (?:the defending|your opponent's active) pokémon", text,
    )
    if hand_ko_cost:
        count = int(hand_ko_cost.group(1))
        ptype = getattr(PokemonTypes, hand_ko_cost.group(2).upper(), None)
        candidates = [card for card in ctx.hand()
                      if is_basic_energy(card) and ptype is not None
                      and energy_provides_type(card, ptype.value)]
        if len(candidates) >= count:
            picks = await ctx.choose_cards(
                candidates, count, minimum=count,
                prompt="Choose Energy cards to discard",
            )
            await ctx.discard_cards(picks)
            await ctx.knock_out(ctx.defender)

    basic_ko = re.search(
        r"knock out 1 of your opponent's basic pokémon that isn't a pokémon-gx", text,
    )
    if basic_ko:
        targets = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                   if is_basic_pokemon(pokemon)
                   and "GX" not in (getattr(def_for(pokemon.archetype_id),
                                             "subtypes", None) or [])]
        target = await ctx.choose_pokemon(targets, "Choose a Basic Pokémon") \
            if targets else None
        if target is not None:
            await ctx.knock_out(target)

    low_hp_ko = re.search(
        r"knock out each of your opponent's pokémon that has (\d+) hp or less remaining",
        text,
    )
    if low_hp_ko:
        threshold_hp = int(low_hp_ko.group(1))
        for target in list(ctx.opponent_pokemon_in_play()):
            if target.get_attribute(AttrID.HP, 0) <= threshold_hp:
                await ctx.knock_out(target)
    if "both active pokémon are knocked out" in text:
        await ctx.knock_out(ctx.attacker)
        await ctx.knock_out(ctx.defender)

    if "if you use this attack when you have exactly 1 prize card remaining, you win" in text \
            or "if you use this attack when you have only 1 prize card left, you win" in text:
        prizes = ctx.board.find_player_area(ctx.player_id, "prizePile")
        if prizes is not None and len(prizes.children) == 1:
            await ctx.win_game("Attack alternate win condition")

    if "has the least hp remaining" in text and "is knocked out" in text:
        candidates = [p for p in ctx.my_pokemon_in_play()
                      + ctx.opponent_pokemon_in_play() if p is not ctx.attacker]
        if candidates:
            least = min(p.get_attribute(AttrID.HP, 0) for p in candidates)
            tied = [p for p in candidates if p.get_attribute(AttrID.HP, 0) == least]
            target = tied[0] if len(tied) == 1 else \
                await ctx.choose_pokemon(tied, "Choose the Pokémon to Knock Out")
            if target is not None:
                await ctx.knock_out(target)

    # Move attached Energy as directed by the attack, using real board cards.
    # These clauses have kept the same rule but use several generations of
    # wording ("an Energy", "an Energy card", printed Pokémon name, etc.).
    source_to_bench = re.search(
        r"move (all|\d+|an|a) "
        r"(?:(basic|grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
        r"energy(?: cards?)? (?:attached to|from) "
        r"(?:this pokémon|[a-z0-9 &'’.-]+) to 1 of your benched pokémon",
        text,
    )
    if source_to_bench and ctx.my_bench():
        raw_count, descriptor = source_to_bench.groups()
        predicate = is_basic_energy if descriptor == "basic" else \
            _energy_predicate(descriptor) if descriptor else is_energy_card
        candidates = [energy for energy in ctx.attached_energies(ctx.attacker)
                      if predicate(energy)]
        count = len(candidates) if raw_count == "all" else \
            1 if raw_count in ("a", "an") else int(raw_count)
        count = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, count, minimum=count, prompt="Choose Energy to move",
        ) if count else []
        bench = list(ctx.my_bench())
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon",
        )
        if target is not None:
            for energy in picks:
                await ctx.move_energy(energy, target)
    elif re.search(
            r"move (?:all|any amount of|any number of) "
            r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
            r"energy from this pokémon to your benched pokémon in any way",
            text):
        type_match = re.search(
            r"move (?:all|any amount of|any number of) ([a-z]+) energy", text,
        )
        predicate = _energy_predicate(type_match.group(1)) if type_match else None
        await ctx.move_energy_freely(
            [ctx.attacker], ctx.my_bench(), predicate=predicate,
            prompt="Choose Energy to move",
        )
    elif re.search(
            r"move (?:any amount of|any number of) "
            r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
            r"energy from your pokémon to your other pokémon in any way",
            text):
        type_match = re.search(
            r"move (?:any amount of|any number of) ([a-z]+) energy", text,
        )
        predicate = _energy_predicate(type_match.group(1)) if type_match else None
        in_play = list(ctx.my_pokemon_in_play())
        await ctx.move_energy_freely(
            in_play, in_play, predicate=predicate, prompt="Choose Energy to move",
        )
    elif "move as many" in text and "energy attached to your pokémon" in text:
        wanted = None
        for word, kind in (("grass", PokemonTypes.GRASS),
                           ("darkness", PokemonTypes.DARKNESS),
                           ("metal", PokemonTypes.METAL)):
            if f"as many {word} energy" in text:
                wanted = kind
        moved_ids = set()
        while True:
            energies = [e for p in ctx.my_pokemon_in_play()
                        for e in ctx.attached_energies(p)
                        if e.entity_id not in moved_ids
                        if wanted is None or energy_provides_type(e, wanted.value)]
            energy = await _choose_one(ctx, energies, "Choose an Energy to move",
                                       optional=True) if energies else None
            if energy is None:
                break
            targets = [p for p in ctx.my_pokemon_in_play()
                       if p is not carrier_pokemon(energy)]
            target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if targets else None
            if target is None:
                break
            await ctx.move_energy(energy, target)
            moved_ids.add(energy.entity_id)
    elif "move all energy attached to this pokémon to 1 of your benched" in text:
        target = await ctx.choose_pokemon(ctx.my_bench(), "Choose a Benched Pokémon") \
            if ctx.my_bench() else None
        if target is not None:
            for energy in list(ctx.attached_energies(ctx.attacker)):
                await ctx.move_energy(energy, target)
    elif re.search(
            r"move an? energy(?: card)? (?:attached to|from) the defending pokémon "
            r"to 1 of (?:your opponent's|their|his or her) benched pokémon",
            text):
        energy = await _choose_one(ctx, ctx.attached_energies(ctx.defender),
                                   "Choose an Energy") \
            if ctx.attached_energies(ctx.defender) else None
        target = await ctx.choose_pokemon(ctx.opponent_bench(), "Choose a Benched Pokémon") \
            if energy is not None and ctx.opponent_bench() else None
        if target is not None:
            await ctx.move_energy(energy, target)

    elif re.search(
            r"move an? (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
            r"energy from 1 of your benched pokémon to this pokémon", text):
        type_word = re.search(r"move an? ([a-z]+) energy", text).group(1)
        predicate = _energy_predicate(type_word)
        energies = [energy for pokemon in ctx.my_bench()
                    for energy in ctx.attached_energies(pokemon)
                    if predicate(energy)]
        energy = await _choose_one(ctx, energies, "Choose an Energy") \
            if energies else None
        if energy is not None:
            await ctx.move_energy(energy, ctx.attacker)

    elif (
            "move an energy" in text and "opponent's pokémon to another" in text
            or "attached to the defending pokémon to another" in text
            or "move an energy card attached to 1 of your opponent's pokémon to another" in text
            or "move an energy from 1 of your opponent's benched pokémon to another" in text
    ):
        sources = list(ctx.opponent_bench()) if (
            "from 1 of your opponent's benched pokémon" in text
        ) else list(ctx.opponent_pokemon_in_play())
        energies = [energy for pokemon in sources
                    for energy in ctx.attached_energies(pokemon)]
        energy = await _choose_one(ctx, energies, "Choose an Energy") \
            if energies else None
        holder = carrier_pokemon(energy) if energy is not None else None
        targets = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                   if pokemon is not holder]
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if energy is not None and targets else None
        if target is not None:
            await ctx.move_energy(energy, target)
            moved_damage = re.search(
                r"put (\d+) damage counters on the pokémon you moved the energy to",
                text,
            )
            if moved_damage:
                await ctx.deal_damage(
                    int(moved_damage.group(1)) * 10, target=target,
                    apply_modifiers=False, as_counters=True,
                )

    if "put all energy attached to this pokémon into your hand" in text:
        await ctx.put_in_hand(list(ctx.attached_energies(ctx.attacker)), reveal=False)

    if "discard all energy from both active pokémon" in text:
        await ctx.discard_cards(
            list(ctx.attached_energies(ctx.attacker))
            + list(ctx.attached_energies(ctx.defender))
        )

    typed_all_discard = re.search(
        r"discard all (grass|fire|water|lightning|psychic|fighting|darkness|metal) "
        r"energy from this pokémon", text,
    )
    if typed_all_discard:
        ptype = getattr(PokemonTypes, typed_all_discard.group(1).upper())
        cards = [energy for energy in ctx.attached_energies(ctx.attacker)
                 if energy_provides_type(energy, ptype.value)]
        await ctx.discard_cards(cards)
        if "discard a card from the top of your opponent's deck for each energy" in text:
            await ctx.discard_cards(ctx.deck_top(len(cards), ctx.opponent_id))

    # Tool movement uses the same direct-on-board picker as Energy movement.
    if "move a pokémon tool card attached to 1 of either player's pokémon" in text:
        tools = [card for player_id in ctx.board.player_ids
                 for pokemon in ctx.board.pokemon_in_play(player_id)
                 for card in full_stack(pokemon)[1:] if is_pokemon_tool(card)]
        tool = await _choose_one(ctx, tools, "Choose a Pokémon Tool") \
            if tools else None
        holder = carrier_pokemon(tool) if tool is not None else None
        targets = [pokemon for pokemon in ctx.board.pokemon_in_play(
            holder.owning_player_id if holder is not None else ctx.player_id)
            if pokemon is not holder and not _has_tool(pokemon)]
        target = await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if tool is not None and targets else None
        if target is not None:
            await ctx.attach_card(tool, target)

    # One-turn defensive/offensive riders.
    source_name = _name(ctx.attacker).casefold()
    reduction = re.search(
        r"damage done to (?:this pokémon|" + re.escape(source_name)
        + r") by attacks is reduced by (\d+)", text,
    )
    if reduction:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, _BWTurnShield(int(reduction.group(1))))
    reduction = re.search(
        r"during your opponent's next turn, this pokémon takes (\d+) less damage from attacks",
        text,
    )
    if reduction:
        allowed = True
        if "you may discard all future booster energy capsules" in text:
            allowed = await ctx.ask_yes_no(
                "Discard all Future Booster Energy Capsules?"
            )
            if allowed:
                capsules = [
                    card for card in full_stack(ctx.attacker)[1:]
                    if _name(card).casefold() == "future booster energy capsule"
                ]
                await ctx.discard_cards(capsules)
        if allowed:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker, _BWTurnShield(int(reduction.group(1))))
    reduction = re.search(r"damage done by attacks from the defending pokémon is reduced by (\d+)", text)
    if reduction:
        ctx.add_passive_through_opponents_turn(
            ctx.defender, _BWTurnShield(int(reduction.group(1)), outgoing=True))
    reduction = re.search(
        r"(?:the )?defending pokémon's attacks do (\d+) less damage", text
    ) or re.search(
        r"attacks used by the defending pokémon do (\d+) less damage", text
    )
    if reduction:
        ctx.add_passive_through_opponents_turn(
            ctx.defender, _BWTurnShield(int(reduction.group(1)), outgoing=True)
        )
    increase = re.search(r"damage done to this pokémon by attacks is increased by (\d+)", text)
    if increase:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, _BWTurnShield(int(increase.group(1)), increase=True))
    threshold = re.search(r"prevent that attack's damage.*if that damage is (\d+) or less", text)
    if threshold:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, _BWTurnShield(threshold=int(threshold.group(1))))
    protection_text = (
        "during your opponent's next turn" in text
        and (
            "prevent all damage" in text
            or "prevent all effects of attacks" in text
            or "prevent all damage from and effects of attacks" in text
            or "prevent all effects of attacks used by your opponent's pokémon" in text
        )
    )
    protection_allowed = True
    if protection_text and "if heads" in text:
        protection_allowed = bool(heads)
        if "if all of them are heads" in text:
            protection_allowed = coin_count is not None and heads == coin_count
    if protection_text and "knocked out by damage from this attack" in text:
        protection_allowed = ctx.defender in ctx.knockouts
    if protection_text and "if this pokémon has at least 1 extra energy" in text:
        printed_cost = sum((getattr(ctx.ability, "cost", None) or {}).values())
        protection_allowed = _energy_count(ctx, ctx.attacker) >= printed_cost + 1
    if protection_text and "if you played lillie's full force" in text:
        protection_allowed = any(
            name.casefold() == "lillie's full force"
            for _, name, _ in ctx.session.turn_state.trainers_played
        )

    if protection_text and protection_allowed:
        protects_damage = "damage" in text and "damage is not an effect" not in text
        protects_effects = (
            "effects of attacks" in text or "effects of your opponent's attacks" in text
        )
        attacker_predicate = None
        if "attacks from basic pokémon" in text:
            attacker_predicate = lambda pokemon: pokemon is not None \
                and pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        elif "attacks from dragon pokémon" in text:
            attacker_predicate = lambda pokemon: pokemon is not None \
                and PokemonTypes.DRAGON.value in effective_pokemon_types(
                    ctx.board, pokemon)
        elif "attacks from pokémon-gx and pokémon-ex" in text:
            attacker_predicate = lambda pokemon: pokemon is not None \
                and bool({"GX", "EX"}.intersection(
                    set(subtypes_for(pokemon.archetype_id) or [])))

        protects_all_mine = (
            "each of your pokémon" in text
            or "each of your future pokémon" in text
        )
        if protects_all_mine:
            target_predicate = None
            if "future pokémon" in text:
                target_predicate = lambda pokemon: "Future" in set(
                    subtypes_for(pokemon.archetype_id) or [])
            ctx.add_temporary_player_passive(
                ctx.player_id,
                _BWPlayerAttackShield(
                    ctx.player_id, damage=protects_damage,
                    effects=protects_effects,
                    target_predicate=target_predicate,
                    attacker_predicate=attacker_predicate,
                    active_source_id=ctx.attacker.entity_id
                    if "if this pokémon is no longer your active" in text else None,
                ),
                ctx.session.turn_state.turn_number + 1,
            )
        else:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker,
                _BWTurnShield(
                    prevent_all=protects_damage and protects_effects,
                    damage_only=protects_damage and not protects_effects,
                    effects_only=protects_effects and not protects_damage,
                    attacker_predicate=attacker_predicate,
                ),
            )
    if not protection_text \
            and "prevent all damage done to this pokémon by attacks from basic pokémon" in text:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            _BWTurnShield(
                prevent_all=True,
                attacker_predicate=lambda pokemon: pokemon is not None
                and pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value,
            ),
        )
    if "during your opponent's next turn, this pokémon has no weakness" in text:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, _BWTurnShield(no_weakness=True))

    if "during your next turn, if the defending pokémon is damaged by an attack" in text \
            and "knocked out" in text:
        ctx.add_passive_through_own_next_turn(
            ctx.defender, _BWKnockOutIfDamaged()
        )

    retaliation = re.search(
        r"during your opponent's next turn, if this pokémon is damaged by an "
        r"attack.*put (\d+) damage counters on the attacking pokémon", text,
    )
    if retaliation:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            _BWRetaliateWhenDamaged(counters=int(retaliation.group(1))),
        )
    if "put damage counters on the attacking pokémon equal to the damage done to this pokémon" in text:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, _BWRetaliateWhenDamaged(mirror_damage=True)
        )
    if "if this pokémon is knocked out by damage from an attack" in text \
            and "discard an energy attached to the attacking pokémon" in text:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            _BWRetaliateWhenDamaged(discard_attacker_energy=True),
        )

    if "at the end of your opponent's next turn" in text \
            and ("defending pokémon will be knocked out" in text
                 or "defending pokémon and all" in text):
        target_id = ctx.defender.entity_id
        owner_id = ctx.player_id
        discard_instead = "discard the defending pokémon" in text

        def still_defending(board):
            target = board.get_entity(target_id)
            return isinstance(target, PokemonEntity) and _is_active(target)

        async def finish_delayed(session):
            target = session.board_state.get_entity(target_id)
            if not isinstance(target, PokemonEntity):
                return
            delayed = EffectContext(session, owner_id, target, None)
            if discard_instead:
                await delayed.discard_cards(full_stack(target))
            else:
                await delayed.knock_out(target)
            if delayed._messages:
                await session._flush_effect_runs(delayed)
            if delayed.knockouts:
                await session.resolve_knockouts(delayed)

        ctx.schedule_at_checkup(1, finish_delayed, guard=still_defending)

    named_reduction = re.search(
        r"during your opponent's next turn, ?any damage done to [a-z0-9 .'-]+ "
        r"by attacks is reduced by (\d+)", text,
    )
    if named_reduction:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, _BWTurnShield(int(named_reduction.group(1)))
        )

    next_base = re.search(
        r"during your next turn, (?:this pokémon's |[a-z0-9 .'-]+')?"
        r"([a-z0-9 '-]+) attack's base damage is (\d+)", text,
    )
    if next_base:
        ctx.add_passive_through_own_next_turn(
            ctx.attacker,
            _BWTemporaryCombatRule(
                attack_title=next_base.group(1).strip(),
                base_damage=int(next_base.group(2)),
            ),
        )

    next_instead = re.search(
        r"during your next turn, (?:this pokémon's )?([a-z0-9 '-]+) attack "
        r"does (\d+) damage instead of \d+", text,
    )
    if next_instead:
        ctx.add_passive_through_own_next_turn(
            ctx.attacker,
            _BWTemporaryCombatRule(
                attack_title=next_instead.group(1).strip(),
                base_damage=int(next_instead.group(2)),
            ),
        )

    next_named_boost = re.search(
        r"during your next turn, (?:this pokémon's )?([a-z0-9 '-]+) attack "
        r"does (\d+) more damage", text,
    )
    if next_named_boost:
        ctx.add_passive_through_own_next_turn(
            ctx.attacker,
            _BWTemporaryCombatRule(
                attack_title=next_named_boost.group(1).strip(),
                damage_boost=int(next_named_boost.group(2)),
            ),
        )

    next_all_boost = re.search(
        r"during your next turn, (?:each of )?this pokémon's attacks? do(?:es)? "
        r"(\d+) more damage", text,
    )
    if next_all_boost:
        ctx.add_passive_through_own_next_turn(
            ctx.attacker,
            _BWTemporaryCombatRule(damage_boost=int(next_all_boost.group(1))),
        )

    defending_next_boost = re.search(
        r"during your next turn, (?:any damage done to |)the? ?defending "
        r"pokémon (?:by attacks )?is increased by (\d+)", text,
    ) or re.search(
        r"during your next turn, (?:the )?defending pokémon takes (\d+) "
        r"more damage from attacks", text,
    )
    if defending_next_boost:
        ctx.add_passive_through_own_next_turn(
            ctx.defender,
            _BWTemporaryCombatRule(
                damage_taken_add=int(defending_next_boost.group(1))
            ),
        )

    if "as long as this" in text and "active pokémon" in text \
            and "each of its attacks does 100 more damage" in text:
        ctx.add_temporary_passive(
            ctx.attacker,
            _BWTemporaryCombatRule(damage_boost=100, unique_key="dragon-dance"),
        )

    if "during your next turn, this pokémon has no retreat cost" in text:
        ctx.add_passive_through_own_next_turn(
            ctx.attacker, _BWTemporaryCombatRule(retreat_zero=True)
        )

    retreat_surcharge = re.search(
        r"during your opponent's next turn, the defending pokémon's retreat "
        r"cost is (?:colorless )?(\d+ )?more", text,
    )
    if retreat_surcharge:
        ctx.add_passive_through_opponents_turn(
            ctx.defender,
            _BWTemporaryCombatRule(retreat_add=int(
                (retreat_surcharge.group(1) or "1").strip()
            )),
        )
    elif "during your opponent's next turn, the defending pokémon's retreat cost is colorless more" in text:
        ctx.add_passive_through_opponents_turn(
            ctx.defender, _BWTemporaryCombatRule(retreat_add=1)
        )

    if "during your opponent's next turn" in text \
            and "attack cost of each of the defending pokémon's attacks is colorless more" in text:
        ctx.add_passive_through_opponents_turn(
            ctx.defender, _BWTemporaryCombatRule(attack_cost_add=1)
        )

    weakness_change = re.search(
        r"defending pokémon's weakness is now "
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon|colorless)",
        text,
    )
    if weakness_change:
        chosen = getattr(PokemonTypes, weakness_change.group(1).upper())
        expiry = None if "until the defending pokémon leaves the active spot" in text \
            else ctx.session.turn_state.turn_number + 2
        ctx.add_temporary_passive(
            ctx.defender, _BWTemporaryCombatRule(weakness_type=chosen), expiry
        )

    choose_weakness = re.search(
        r"choose grass, fire, water, lightning, psychic, fighting, darkness, metal",
        text,
    )
    if choose_weakness and (
            "defending pokémon's weakness" in text
            or "its weakness is now that type" in text):
        names = ["Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting",
                 "Darkness", "Metal"]
        if "dragon type" in text:
            names.append("Dragon")
        if "colorless type" in text:
            names.append("Colorless")
        index = await ctx.choose("Choose a Weakness", names)
        expiry = None if "until the defending pokémon leaves the active spot" in text \
            else ctx.session.turn_state.turn_number + 2
        ctx.add_temporary_passive(
            ctx.defender,
            _BWTemporaryCombatRule(
                weakness_type=getattr(PokemonTypes, names[index].upper())
            ),
            expiry,
        )

    choose_self_type = re.search(
        r"choose grass, fire, water, lightning, psychic, fighting, darkness, metal",
        text,
    )
    if choose_self_type and "this pokémon is that type" in text:
        names = ["Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting",
                 "Darkness", "Metal"]
        index = await ctx.choose("Choose a type", names)
        ctx.add_passive_through_own_next_turn(
            ctx.attacker,
            _BWTemporaryPokemonType(getattr(PokemonTypes, names[index].upper())),
        )

    # Player-scoped next-turn/permanent rules.
    if "opponent can't play any trainer cards" in text:
        ctx.lock_plays(ctx.opponent_id, is_trainer_card)
    if "opponent can't play any supporter cards" in text:
        ctx.lock_plays(ctx.opponent_id, is_supporter_card)
    if "opponent can't play any cards from their hand" in text:
        ctx.lock_plays(ctx.opponent_id, lambda card: True)
    item_lock = (
        "can't play any item cards" in text
        and ("if heads" not in text or bool(heads))
    )
    if item_lock:
        ctx.lock_plays(ctx.opponent_id, is_item_card)
    if "can't play any stadium cards" in text:
        ctx.lock_plays(ctx.opponent_id, is_stadium_card)
    if "can't play any pokémon tool, special energy, or stadium cards" in text:
        ctx.lock_plays(
            ctx.opponent_id,
            lambda card: is_pokemon_tool(card) or is_special_energy(card)
            or is_stadium_card(card),
        )
    if "can't play any pokémon from" in text and "to evolve" in text:
        target_only = "evolve the defending pokémon" in text
        defender_id = ctx.defender.entity_id if ctx.defender is not None else None

        def evolution_lock(card, target_only=target_only, defender_id=defender_id):
            if not is_evolution_pokemon(card):
                return False
            if not target_only:
                return True
            # The normal play validator supplies the prospective target on
            # cards selected for evolution.  If it is not available yet, the
            # lock must conservatively hide the card rather than leak a route
            # around B Cancel/Time Freeze.
            target_id = getattr(card, "_prospective_evolution_target_id", None)
            return target_id is None or target_id == defender_id

        ctx.lock_plays(ctx.opponent_id, evolution_lock)
    if "can't play any pokémon that has an ability" in text:
        ctx.lock_plays(
            ctx.opponent_id,
            lambda card: is_pokemon_card(card) and any(
                isinstance(entry, Ability) and not isinstance(entry, Attack)
                for entry in (getattr(def_for(card.archetype_id), "abilities", None) or [])
            ),
        )
    if "choose item cards or supporter cards" in text \
            and "can't play any of the chosen cards" in text:
        choice = await ctx.choose("Choose the card type to block", ["Item", "Supporter"])
        ctx.lock_plays(
            ctx.opponent_id, is_item_card if choice == 0 else is_supporter_card,
        )
    if "each player can't play any supporter or stadium cards" in text:
        expiry = ctx.session.turn_state.turn_number + 2
        predicate = lambda card: is_supporter_card(card) or is_stadium_card(card)
        for player_id in (ctx.player_id, ctx.opponent_id):
            ctx.lock_plays(player_id, predicate, through_turn=expiry)
    if "during your opponent's next turn, their pokémon can't attack" in text:
        ctx.add_temporary_player_passive(
            ctx.opponent_id,
            _BWPlayerCombatRule(ctx.opponent_id, attacks_blocked=True),
            ctx.session.turn_state.turn_number + 1,
        )
    if "during your next turn, ignore all energy in the attack costs of grass pokémon and fire pokémon" in text:
        ctx.add_temporary_player_passive(
            ctx.player_id,
            _BWPlayerCombatRule(
                ctx.player_id,
                free_attack_types={PokemonTypes.GRASS.value, PokemonTypes.FIRE.value},
            ),
            ctx.session.turn_state.turn_number + 2,
        )
    if "for the rest of this game, your pokémon's attacks do 30 more damage" in text:
        has_extra_water = _energy_count(ctx, ctx.attacker, "water") > 0
        ctx.add_temporary_player_passive(
            ctx.player_id,
            _BWPlayerCombatRule(
                ctx.player_id, damage_boost=30,
                extra_prizes=1 if has_extra_water else 0,
            ),
            None,
        )
    if "for the rest of this game, your metal pokémon take 30 less damage" in text:
        ctx.add_temporary_player_passive(
            ctx.player_id,
            _BWPlayerCombatRule(
                ctx.player_id, damage_reduction=30,
                damage_reduction_types={PokemonTypes.METAL.value},
            ),
            None,
        )

    if "for the rest of this game, your opponent can't use any gx attacks" in text:
        ctx.lock_gx_attacks(ctx.opponent_id)

    if "discard any stadium card in play" in text:
        await ctx.discard_stadium()

    if "whenever your opponent flips a coin during his or her next turn, treat it as tails" in text:
        ctx.force_coins_through_next_turn(ctx.opponent_id, False)

    if "whenever your opponent plays a trainer card from his or her hand during " \
            "his or her next turn" in text and "that card has no effect" in text:
        ctx.require_trainer_flip(ctx.opponent_id)

    if "during your opponent's next turn" in text \
            and "attach an energy card from their hand to the defending pokémon" in text \
            and "their turn ends" in text:
        ctx.end_turn_if_energy_attached_to(ctx.defender)

    if "if the defending pokémon is knocked out during your next turn, take 2 more prize cards" in text:
        ctx.add_passive_through_own_next_turn(
            ctx.defender,
            _BWPrizeRule(ctx.player_id, bonus=2),
        )

    if "during your opponent's next turn, if this pokémon is knocked out" in text \
            and "can't take any prize cards for it" in text:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            _BWPrizeRule(ctx.opponent_id, suppress=True),
        )

    if "put 10 damage counters instead of 1 on that pokémon between turns" in text:
        ctx.add_temporary_passive(
            ctx.defender, _BWPoisonCounterRule(replacement=10)
        )
    poison_extra = re.search(
        r"put (\d+) more damage counters on that pokémon between turns", text,
    )
    if poison_extra:
        ctx.add_temporary_passive(
            ctx.defender,
            _BWPoisonCounterRule(extra=int(poison_extra.group(1))),
        )

    if getattr(ctx.ability, "title", "") == "Barrier" \
            and "can't be used" in text:
        ctx.session.turn_state.lock_attack(
            ctx.attacker.entity_id, ctx.ability.ability_id
        )

    # Torment/Amnesia/Encore select attacks from the actual Defending Pokémon.
    if "choose 1 of the defending pokémon's attack" in text \
            and "use it as this attack" not in text and ctx.defender is not None:
        attacks = [ability for ability in
                   (getattr(def_for(ctx.defender.archetype_id), "abilities", None) or [])
                   if isinstance(ability, Attack)]
        picked = await ctx.choose_attack_to_copy(
            [(ctx.defender, attack) for attack in attacks], "Choose an attack") \
            if attacks else None
        if picked is not None:
            chosen = picked[1]
            for attack in attacks:
                lock = attack is chosen if "can't use that attack" in text else attack is not chosen
                if lock:
                    ctx.session.turn_state.lock_attack(
                        ctx.defender.entity_id, attack.ability_id)

    # Switching/retreat/attack locks.
    switched_target = None
    if "you may have your opponent switch" in text \
            and "active pokémon" in text and ctx.opponent_bench() \
            and await ctx.ask_yes_no("Have your opponent switch their Active Pokémon?"):
        bench = list(ctx.opponent_bench())
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id,
        )
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
            switched_target = target
    if "switch the defending pokémon with 1 of your opponent's benched pokémon" in text \
            and ctx.opponent_bench():
        target = await ctx.choose_pokemon(ctx.opponent_bench(),
                                          "Choose your opponent's new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
            switched_target = target
    if (
        "opponent switches his or her active pokémon with 1 of his or her benched pokémon" in text
        or "opponent switches their active pokémon with 1 of their benched pokémon" in text
        or "opponent switches the defending pokémon with 1 of his or her benched pokémon" in text
        or "opponent chooses 1 of their benched pokémon and switches it with the defending pokémon" in text
        or "opponent chooses 1 of their benched pokémon and switches it with their active pokémon" in text
        or "switch 1 of your opponent's benched pokémon with their active pokémon" in text
        or "switch 1 of your opponent's benched pokémon with his or her active pokémon" in text
        or "switch 1 of your opponent's benched pokémon with the defending pokémon" in text
        or "switch in 1 of your opponent's benched pokémon to the active spot" in text
    ) and ctx.opponent_bench():
        target = await ctx.choose_pokemon(
            ctx.opponent_bench(), "Choose your opponent's new Active Pokémon"
        )
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
            switched_target = target
    if ("switch out your opponent's active pokémon to the bench" in text
            or "switch out the defending pokémon to the bench" in text) \
            and ctx.opponent_bench():
        target = await ctx.choose_pokemon(
            ctx.opponent_bench(), "Choose your new Active Pokémon",
            player_id=ctx.opponent_id,
        )
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
            switched_target = target
    if switched_target is not None:
        if switch_damage:
            await ctx.deal_damage(
                int(switch_damage.group(1)), target=switched_target,
                apply_modifiers=True,
            )
        switched_conditions = {
            "asleep": SpecialConditions.ASLEEP,
            "burned": SpecialConditions.BURNED,
            "confused": SpecialConditions.CONFUSED,
            "paralyzed": SpecialConditions.PARALYZED,
            "poisoned": SpecialConditions.POISONED,
        }
        for word, condition in switched_conditions.items():
            if f"new active pokémon is now {word}" in text or (
                    f"that pokémon is now {word}" in text
                    and (heads is None or heads > 0 or "if heads" not in text)):
                poison = 1
                if condition == SpecialConditions.POISONED:
                    stronger = re.search(
                        r"put (\d+) damage counters instead of 1", text,
                    )
                    poison = int(stronger.group(1)) if stronger else 1
                await ctx.apply_special_condition(
                    switched_target, condition, poison_counters=poison,
                )
        if "new active pokémon can't retreat" in text:
            ctx.lock_retreat(switched_target)
    self_switch = re.search(
        r"switch this pokémon with 1 of your benched(?: (grass|fire|water|"
        r"lightning|psychic|fighting|darkness|metal|fairy))? pokémon", text,
    )
    if self_switch and ctx.my_bench():
        candidates = list(ctx.my_bench())
        if self_switch.group(1):
            ptype = getattr(PokemonTypes, self_switch.group(1).upper())
            candidates = [pokemon for pokemon in candidates
                          if ptype.value in effective_pokemon_types(
                              ctx.board, pokemon)]
        target = await ctx.choose_pokemon(candidates, "Choose your new Active Pokémon") \
            if candidates else None
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    source_name = _name(ctx.attacker).casefold()
    if source_name and f"switch {source_name} with 1 of your benched pokémon" in text \
            and ctx.my_bench():
        target = await ctx.choose_pokemon(
            ctx.my_bench(), "Choose your new Active Pokémon"
        )
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)

    if "switch all damage counters on this pokémon with those on the defending pokémon" in text:
        attacker_count = _damage_counter_count(ctx, ctx.attacker)
        defender_count = _damage_counter_count(ctx, ctx.defender)
        await ctx.set_damage_counters(ctx.attacker, defender_count)
        await ctx.set_damage_counters(ctx.defender, attacker_count)
    # Attack prohibitions.  Lock every printed attack, not only the attack
    # currently being resolved: "this Pokémon can't attack" is broader than
    # "can't use this attack".
    source_name = _name(ctx.attacker).casefold()
    self_cannot_attack = bool(re.search(
        r"(?:during your next turn, (?:this pokémon|" + re.escape(source_name)
        + r") can't attack|(?:this pokémon|" + re.escape(source_name)
        + r"|it) can't attack during your next turn)",
        text,
    )) if source_name else "this pokémon can't attack during your next turn" in text
    if self_cannot_attack:
        should_lock = True
        prefix = text[:text.find("can't attack")]
        if "if tails" in prefix:
            should_lock = heads == 0
        elif "if heads" in prefix:
            should_lock = bool(heads)
        if should_lock:
            lock_all_attacks(ctx, ctx.attacker)

    if "during your next turn, your pokémon can't attack" in text:
        ctx.add_temporary_player_passive(
            ctx.player_id,
            _BWPlayerCombatRule(ctx.player_id, attacks_blocked=True),
            ctx.session.turn_state.turn_number + 2,
        )
    if "pokémon that have 2 or less energy attached can't attack" in text:
        ctx.add_temporary_player_passive(
            ctx.opponent_id,
            _BWPlayerCombatRule(ctx.opponent_id, max_attack_energy=2),
            ctx.session.turn_state.turn_number + 1,
        )

    defender_cannot_attack = bool(re.search(
        r"(?:the defending pokémon|it) can't attack during your opponent's next turn|"
        r"during your opponent's next turn, the defending pokémon can't attack",
        text,
    ))
    if defender_cannot_attack and ctx.defender is not None:
        should_lock = True
        prefix = text[:text.find("can't attack")]
        if "if heads" in prefix:
            should_lock = bool(heads)
        elif "if tails" in prefix:
            should_lock = heads == 0
        if "defending pokémon is a basic pokémon" in text:
            should_lock = should_lock and is_basic_pokemon(ctx.defender)
        if "defending pokémon is an evolution pokémon" in text:
            should_lock = should_lock and is_evolution_pokemon(ctx.defender)
        if "defending pokémon is a pokémon-ex" in text:
            should_lock = should_lock and "EX" in set(
                subtypes_for(ctx.defender.archetype_id) or [])
        if "defending pokémon is a darkness or fairy pokémon" in text:
            live_types = set(effective_pokemon_types(ctx.board, ctx.defender))
            should_lock = should_lock and bool(live_types.intersection({
                PokemonTypes.DARKNESS.value, PokemonTypes.FAIRY.value,
            }))
        if should_lock:
            lock_defender_attacks(ctx)

    # Retreat locks have the same reversed-word-order variants as attack
    # locks, plus named/self restrictions on Roost/Take It Easy.
    defender_cannot_retreat = bool(re.search(
        r"(?:during your opponent's next turn, )?(?:the defending pokémon|"
        r"that pokémon|it)(?: is now [a-z]+ and)? can't retreat"
        r"(?: during your opponent's next turn)?",
        text,
    ))
    if defender_cannot_retreat and ctx.defender is not None:
        ctx.lock_retreat(ctx.defender)
    self_cannot_retreat = bool(re.search(
        r"(?:during your next turn, )?(?:this pokémon|" + re.escape(source_name)
        + r") can't retreat(?: during your next turn)?",
        text,
    )) if source_name else "this pokémon can't retreat during your next turn" in text
    if self_cannot_retreat:
        ctx.lock_retreat(
            ctx.attacker,
            through_turn=ctx.session.turn_state.turn_number + 2,
        )
    if "tries to attack during your opponent's next turn" in text \
            and "flips a coin" in text:
        ctx.require_attack_flip(ctx.defender)
    if re.search(r"this pokémon can't use .+ during your next turn", text):
        ctx.session.turn_state.lock_attack(
            ctx.attacker.entity_id, ctx.ability.ability_id)


async def bw_legacy_ability(ctx):
    """Recurring activated/triggered BW Ability text not needing a passive."""
    text = _norm(getattr(ctx.ability, "game_text", ""))
    optional = "you may" in text
    if "took this pokémon as a face-down prize card" in text:
        bench = ctx.board.find_player_area(ctx.player_id, "bench")
        if ctx.source not in ctx.hand() or bench is None \
                or len(bench.children) >= effective_bench_capacity(
                    ctx.board, ctx.player_id):
            ctx.suppress_announce = True
            return
        if optional and not await ctx.ask_yes_no(f"Use {ctx.ability.title}?"):
            ctx.suppress_announce = True
            return
        if not await ctx.bench_pokemon(ctx.source):
            return
        if "flip a coin" not in text \
                or (await ctx.flip_coins(1, ctx.ability.title))[0]:
            await ctx.take_prizes(1)
        return
    # Clicking an activated Ability is already the player's confirmation.
    # Only automatic triggers need the explicit yes/no choice.
    if optional and getattr(ctx.ability, "trigger", None) \
            and not await ctx.ask_yes_no(f"Use {ctx.ability.title}?"):
        return

    # A clicked activated Ability is the player's confirmation, but its
    # printed discard remains mandatory.  Pay it before any generic benefit
    # branch so ``if you do`` cannot resolve for free.
    if getattr(ctx.ability, "trigger", None) is None \
            and not await _pay_shared_ability_discard_cost(ctx, text):
        ctx.suppress_announce = True
        return

    # Energy Grace is an optional self-KO cost followed by one fixed,
    # non-Pokémon-EX destination.  Resolve it before broad text families:
    # those used to move the Energy but neither knocked Milotic Out nor
    # enforced its target restriction.
    if "knock out this pokémon" in text \
            and "attach 3 basic energy from your discard pile" in text \
            and "excluding pokémon-ex" in text:
        targets = [
            pokemon for pokemon in ctx.my_pokemon_in_play()
            if pokemon is not ctx.source and not _has_subtype(pokemon, "EX")
        ]
        candidates = [card for card in ctx.discard_pile()
                      if is_basic_energy(card)]
        if not targets or not candidates:
            return
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Choose a Pokémon")
        if target is None:
            return
        maximum = min(3, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=maximum,
            prompt="Choose basic Energy cards",
        )
        await ctx.knock_out(ctx.source)
        for energy in picks:
            await ctx.attach_energy(energy, target)
        return

    # The original catalog encoded these first-turn powers as continuous
    # passives.  The loader now repairs their classification; keep their
    # complete effects here so clicking them performs the printed action.
    if "search your deck for a spewpa and a vivillon" in text:
        groups = await ctx.search_deck_groups(
            [
                (lambda card: is_pokemon_card(card)
                 and _name(card).casefold() == "spewpa", 1, "Spewpa"),
                (lambda card: is_pokemon_card(card)
                 and _name(card).casefold() == "vivillon", 1, "Vivillon"),
            ],
            prompt="Choose Spewpa and Vivillon",
        )
        picked = [card for group in groups for card in group]
        if picked:
            await ctx.put_in_hand(picked, reveal=True)
        await ctx.shuffle_deck()
        return

    if "leave your opponent's active pokémon confused" in text:
        active = ctx.opponent_active()
        if active is not None:
            await ctx.apply_special_condition(
                active, SpecialConditions.CONFUSED)
        return

    if "choose a basic pokémon you find there, except any ditto" in text \
            and "put the chosen pokémon in its place" in text:
        picks = await ctx.search_deck(
            lambda card: is_basic_pokemon(card)
            and _name(card).casefold() != "ditto",
            1, minimum=0, prompt="Choose a Basic Pokémon",
        )
        if picks:
            await ctx.identity_swap(
                ctx.source, picks[0], destination="discard", transfer=False)
        await ctx.shuffle_deck()
        return

    # Named discard triggers resolve only for the Trainer printed in their
    # condition; a generic hand-discard event carries that cause on the ctx.
    discarded_by = getattr(ctx, "discarded_by", None)
    discarded_name = _name(discarded_by).casefold() if discarded_by else ""
    if "this pokémon is discarded from your deck by an effect" in text:
        if getattr(ctx, "discarded_from", None) == "deck" \
                and getattr(ctx, "discarding_player_id", None) == ctx.opponent_id \
                and ctx.session.turn_state.active_player_id == ctx.opponent_id:
            await ctx.discard_cards(ctx.deck_top(8, ctx.opponent_id))
        return
    if "discard this pokémon with the effect of roxie" in text:
        if discarded_name == "roxie":
            for pokemon in list(ctx.opponent_pokemon_in_play()):
                await ctx.deal_damage(
                    10, target=pokemon, apply_modifiers=False,
                    as_counters=True, is_attack=False)
        return
    if "discard this pokémon with the effect of giovanni's exile" in text:
        if discarded_name == "giovanni's exile":
            await ctx.discard_cards(ctx.deck_top(1, ctx.opponent_id))
        return
    if "discarded with the effect of jessie & james" in text:
        if discarded_name == "jessie & james":
            hand = list(ctx.hand(ctx.opponent_id))
            chosen = await _choose_one(
                ctx, hand, "Choose a card to discard",
                player_id=ctx.opponent_id) if hand else None
            if chosen is not None:
                await ctx.discard_cards([chosen])
        return

    # A Pokemon card can explicitly turn itself into an attached Special
    # Energy (Battery / Buzzap Thunder).  Keep the physical Pokemon entity so
    # its printed art remains visible, while ENERGY_INFO makes the cost engine
    # count the printed two Lightning units.
    if ("attach this card" in text or "attach it" in text) \
            and "as a special energy card" in text:
        targets = list(ctx.my_pokemon_in_play())
        named = re.search(r"to (?:1|one) of your ([a-z0-9 -]+?) as a special", text)
        if named and "lightning pokémon" not in named.group(1):
            names = {
                part.strip().replace("pokémon", "")
                for part in re.split(r"\s+or\s+", named.group(1))
            }
            targets = [p for p in targets if any(
                wanted and wanted in _name(p).casefold() for wanted in names
            )]
        elif "lightning pokémon" in text:
            targets = [p for p in targets if _is_type(p, PokemonTypes.LIGHTNING)]
        targets = [p for p in targets if p is not ctx.source]
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Choose a Pokémon") if targets else None
        if target is None:
            return
        if "knock out this pokémon" in text:
            attachments = full_stack(ctx.source)[1:]
            if attachments:
                await ctx.discard_cards(attachments)
            # Buzzap awards the printed Prize even though the Electrode card
            # remains in play as Energy instead of entering the discard pile.
            await ctx.take_prizes(1, player_id=ctx.opponent_id)
        ctx.source._acts_as_attachment = True
        ctx.source.set_attribute(AttrID.IS_SPECIAL_ENERGY, True)
        ctx.source.set_attribute(AttrID.ENERGY_INFO, {
            "options": [[PokemonTypes.LIGHTNING.value,
                         PokemonTypes.LIGHTNING.value]],
        })
        await ctx.attach_card(ctx.source, target)
        return

    # Named Energy attachment powers (Balloon Therapy and future exact-name
    # variants).  The name is public in the hand, so an unusable activation is
    # gated by standard_ability_condition.
    named_hand_energy = re.search(
        r"attach an? ([a-z0-9' -]+ energy) card from your hand to", text)
    elemental_names = {
        f"{word} energy" for word in (
            "grass", "fire", "water", "lightning", "psychic", "fighting",
            "darkness", "metal", "fairy", "special",
        )
    }
    if named_hand_energy and "basic " not in named_hand_energy.group(1) \
            and named_hand_energy.group(1).strip() not in elemental_names:
        wanted = named_hand_energy.group(1).strip().casefold()
        energies = [card for card in ctx.hand()
                    if _name(card).casefold() == wanted]
        energy = await _choose_one(ctx, energies, f"Choose {wanted.title()}") \
            if energies else None
        targets = list(ctx.my_pokemon_in_play())
        target = targets[0] if energy is not None and len(targets) == 1 \
            else await ctx.choose_pokemon(targets, "Choose a Pokémon") \
            if energy is not None and targets else None
        if energy is not None and target is not None:
            await ctx.attach_energy(energy, target)
        return

    # Clairvoyant Sense: the Energy and target are chosen directly from the
    # hand/board, and drawing is conditional on the attachment succeeding.
    if "attach a basic psychic energy card from your hand to 1 of your benched pokémon" in text:
        energies = [card for card in ctx.hand()
                    if is_basic_energy(card)
                    and energy_provides_type(card, PokemonTypes.PSYCHIC.value)]
        bench = list(ctx.my_bench())
        energy = await _choose_one(
            ctx, energies, "Choose a Basic Psychic Energy") if energies else None
        target = bench[0] if energy is not None and len(bench) == 1 \
            else await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon") \
            if energy is not None and bench else None
        if energy is not None and target is not None \
                and await ctx.attach_energy(energy, target):
            await ctx.draw_cards(2)
        return

    # Shining Vine observes the Energy attachment that already happened; it
    # must not attach a second Energy while resolving the trigger.
    if "when you attach a grass energy card from your hand to it" in text \
            and "switch 1 of your opponent's benched pokémon" in text:
        receiver = getattr(ctx, "energy_receiver", None)
        energy = getattr(ctx, "attached_energy", None)
        if receiver is ctx.source \
                and getattr(ctx, "attaching_player_id", None) == ctx.player_id \
                and energy is not None \
                and energy_provides_type(energy, PokemonTypes.GRASS.value):
            bench = list(ctx.opponent_bench())
            target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench, "Choose your opponent's new Active Pokémon"
            ) if bench else None
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        return

    # Recurring typed acceleration powers (Rain Dance, Magnetic Circuit,
    # Secret Spring, Mega Boost, Nurture and Heal, etc.).  Earlier code had a
    # Fire-only fallback and accidentally interpreted names such as
    # "Lightning Energy" as a proper card name, leaving the other types inert.
    typed_hand_attach = re.search(
        r"attach an? (grass|fire|water|lightning|psychic|fighting|darkness|"
        r"metal|fairy|special) energy card from your hand to (.+?)(?:\.|$)",
        text,
    )
    if typed_hand_attach:
        word, target_text = typed_hand_attach.groups()
        if word == "special":
            energies = [card for card in ctx.hand() if is_special_energy(card)]
        else:
            ptype = getattr(PokemonTypes, word.upper(), None)
            energies = [
                card for card in ctx.hand()
                if is_energy_card(card) and ptype is not None
                and energy_provides_type(card, ptype.value)
            ]
        energy = await _choose_one(
            ctx, energies, f"Choose a {word.title()} Energy"
        ) if energies else None
        if energy is None:
            return
        targets = list(ctx.my_pokemon_in_play())
        if "this pokémon" in target_text \
                or _name(ctx.source).casefold() in target_text:
            targets = [ctx.source]
        elif "mega evolution pokémon" in target_text:
            targets = [
                pokemon for pokemon in targets
                if "Mega" in (subtypes_for(pokemon.archetype_id) or [])
                or "MEGA" in (subtypes_for(pokemon.archetype_id) or [])
                or "SV_Mega" in (subtypes_for(pokemon.archetype_id) or [])
            ]
        else:
            type_target = re.search(
                r"your (grass|fire|water|lightning|psychic|fighting|darkness|"
                r"metal|fairy|dragon) pokémon", target_text,
            )
            if type_target:
                wanted_type = getattr(PokemonTypes, type_target.group(1).upper())
                targets = [
                    pokemon for pokemon in targets
                    if wanted_type.value in effective_pokemon_types(
                        ctx.board, pokemon
                    )
                ]
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Choose a Pokémon"
        ) if targets else None
        if target is None:
            return
        await ctx.attach_energy(energy, target)
        heal = re.search(r"heal (\d+) damage from that pokémon", text)
        if heal:
            await ctx.heal(int(heal.group(1)), target)
        return

    # Skiploom replaces itself with Jumpluff from the deck; cards that were
    # under Skiploom go to the Lost Zone with it and Jumpluff enters fresh.
    if "put this pokémon and all cards attached to it in the lost zone" in text \
            and "put that jumpluff in its place" in text:
        picks = await ctx.search_deck(
            lambda card: is_pokemon_card(card)
            and _name(card).casefold() == "jumpluff",
            1, minimum=0, prompt="Choose Jumpluff",
        )
        if picks:
            await ctx.identity_swap(
                ctx.source, picks[0], destination="lostZone", transfer=False)
        await ctx.shuffle_deck()
        return

    # Bench self-removal powers preserve the printed destination order.
    if "discard the bottom card of your deck" in text \
            and "put this pokémon on top of your deck" in text:
        deck = list(ctx.deck())
        if not deck:
            return
        await ctx.discard_cards([deck[0]])
        attachments = full_stack(ctx.source)[1:]
        if attachments:
            await ctx.discard_cards(attachments)
        await ctx.put_on_top_of_deck(ctx.source)
        return

    # Public-discard Basic recovery directly onto the Bench (Gentle Fin).
    if "basic pokémon with 70 hp or less from your discard pile onto your bench" in text:
        candidates = [card for card in ctx.discard_pile()
                      if is_basic_pokemon(card)
                      and int(card.get_attribute(AttrID.HP) or 0) <= 70]
        chosen = await _choose_one(ctx, candidates, "Choose a Basic Pokémon") \
            if candidates else None
        if chosen is not None:
            await ctx.bench_pokemon(chosen)
        return

    # Evolution-triggered opposing Energy relocation (Magical Flick).
    if "move an energy from your opponent's active pokémon" in text \
            and "to 1 of their benched pokémon" in text:
        active = ctx.opponent_active()
        energies = ctx.attached_energies(active) if active is not None else []
        energy = await _choose_one(ctx, energies, "Choose an Energy to move") \
            if energies else None
        bench = list(ctx.opponent_bench())
        target = bench[0] if energy is not None and len(bench) == 1 \
            else await ctx.choose_pokemon(
                bench, "Choose your opponent's Benched Pokémon") \
            if energy is not None and bench else None
        if energy is not None and target is not None:
            await ctx.move_energy(energy, target)
        return

    # Evolution-triggered Shedinja recovery.
    if "put a shedinja from your discard pile onto your bench" in text:
        candidates = [card for card in ctx.discard_pile()
                      if is_pokemon_card(card)
                      and _name(card).casefold() == "shedinja"]
        chosen = await _choose_one(ctx, candidates, "Choose Shedinja") \
            if candidates else None
        if chosen is not None:
            await ctx.bench_pokemon(chosen)
        return

    # Unown RETURN: move every attached Energy from one chosen Pokemon back
    # to its owner's hand, preserving Special Energy identity.
    if "return all energy attached to 1 of your pokémon to your hand" in text:
        candidates = [p for p in ctx.my_pokemon_in_play()
                      if ctx.attached_energies(p)]
        target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
            candidates, "Choose a Pokémon") if candidates else None
        if target is not None:
            await ctx.put_in_hand(ctx.attached_energies(target), reveal=False)
        return

    # Opponent-discard entry powers (Red Eyes).
    if "put a basic pokémon from your opponent's discard pile onto their bench" in text:
        candidates = [card for card in ctx.discard_pile(ctx.opponent_id)
                      if is_basic_pokemon(card)]
        chosen = await _choose_one(
            ctx, candidates, "Choose a Basic Pokémon",
            player_id=ctx.opponent_id,
        ) if candidates else None
        if chosen is not None:
            await ctx.bench_pokemon(chosen)
        return

    # Evolution entry deck mill (Untamed One).
    if "you must discard the top 5 cards of your deck" in text:
        await ctx.discard_cards(ctx.deck_top(5))
        return

    # Pokemon that become Tools retain a narrow attached passive and cease to
    # be top-level Pokemon.  Their old stack is discarded before attachment.
    if "attach it to 1 of your pokémon as a pokémon tool card" in text:
        candidates = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
        target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
            candidates, "Choose a Pokémon") if candidates else None
        if target is None:
            return
        attachments = full_stack(ctx.source)[1:]
        if attachments:
            await ctx.discard_cards(attachments)
        ctx.source._acts_as_attachment = True
        ctx.source.set_attribute(AttrID.TRAINER_TYPE, TrainerType.POKEMON_TOOL.value)
        ctx.source._attached_passive = _BWAttachedPokemonRule(
            fewer_prizes=1 if "takes 1 fewer prize card" in text else 0,
            block_mega_damage="mega evolution pokémon" in text,
        )
        await ctx.attach_card(ctx.source, target)
        if "discard this card at the end of your opponent's turn" in text:
            ctx.schedule_discard_at_checkup(ctx.source, 1)
        return

    # Palafin's Zero to Hero searches a fresh identity from the deck, carries
    # its complete state across, and returns this printing to the deck.
    if "search your deck for a palafin ex and switch it with this pokémon" in text:
        picks = await ctx.search_deck(
            lambda card: is_pokemon_card(card)
            and _name(card).casefold() == "palafin ex",
            1, minimum=0, prompt="Choose Palafin ex",
        )
        if picks:
            await ctx.identity_swap(
                ctx.source, picks[0], destination="deck", transfer=True)
        await ctx.shuffle_deck()
        return

    # ------------------------------------------------------------------
    # Cross-generation wording shared by the bulk-imported catalogs.  Keep
    # these broad rules before the old title-specific fallbacks: otherwise a
    # perfectly ordinary modern printing can return successfully without
    # changing game state.

    # Pokemon Dolls can remove themselves from play.  Attachments always go
    # to the discard; Lillie's Poke Doll itself goes to the deck bottom while
    # Robo Substitute/Snorlax Doll are discarded.
    if "at any time during your turn" in text and (
            "discard this card from play" in text
            or "put it on the bottom of your deck" in text):
        attachments = list(full_stack(ctx.source)[1:])
        if attachments:
            await ctx.discard_cards(attachments)
        if "put it on the bottom of your deck" in text:
            await ctx.put_on_bottom_of_deck(ctx.source)
        else:
            await ctx.discard_cards([ctx.source])
        return

    # Random opposing-hand disruption (Flower Picking / Wicked Tail).  The
    # server chooses the random cards, reveals exactly those cards, and then
    # returns them to the opponent's deck.
    if "random card" in text and "from your opponent's hand" in text \
            and ("shuffles them into their deck" in text
                 or "shuffles it into their deck" in text):
        count = int((re.search(r"choose (\d+) random", text) or [None, 1])[1])
        if "flip 2 coins" in text:
            count = sum(await ctx.flip_coins(2, ctx.ability.title))
        hand = list(ctx.hand(ctx.opponent_id))
        chosen = random.sample(hand, min(count, len(hand))) if count and hand else []
        if chosen:
            await ctx.reveal_cards(chosen)
            await ctx.shuffle_into_deck(chosen, player_id=ctx.opponent_id)
        if "your turn ends" in text:
            ctx.ends_turn = True
        return

    # Form changes preserve the whole in-play stack and return the previous
    # form to the hand (Aegislash and Wishiwashi-GX).
    if "switch this pokémon with" in text and "in your hand" in text \
            and ("any cards attached" in text or "any attached cards" in text):
        named = re.search(r"with an? ([a-z0-9' -]+?) in your hand", text)
        wanted = named.group(1).strip() if named else ""
        candidates = [
            card for card in ctx.hand()
            if is_pokemon_card(card) and wanted in _name(card).casefold()
        ]
        chosen = await _choose_one(ctx, candidates, "Choose a Pokémon") \
            if candidates else None
        if chosen is not None:
            await ctx.identity_swap(ctx.source, chosen, destination="hand", transfer=True)
        return

    # Alternate win-condition Unown.  They are deliberately evaluated only
    # after their printed public condition is true.
    if "you win this game" in text:
        wins = (
            "66 or more damage counters" in text and sum(
                _damage_counter_count(ctx, pokemon) for pokemon in ctx.my_bench()
            ) >= 66
            or "35 or more cards in your hand" in text and len(ctx.hand()) >= 35
            or "12 or more supporter cards in the lost zone" in text and sum(
                is_supporter_card(card) for card in ctx.lost_zone(ctx.opponent_id)
            ) >= 12
        )
        if wins:
            await ctx.win_game(ctx.ability.title)
        return

    # Composite entry switches must transfer Energy first and then perform
    # the printed switch.  A generic Energy-move branch used to consume these
    # texts before the switch could happen.
    if any(title in text for title in (
            "move any number of lightning energy from your other pokémon",
            "move any number of basic energy attached to your pokémon",
            "move any number of water energy from your other pokémon")) \
            and "switch" in text \
            and "if you do, move any number of water energy" not in text:
        sources = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
        predicate = None
        if "lightning energy" in text:
            predicate = lambda energy: energy_provides_type(
                energy, PokemonTypes.LIGHTNING.value)
        elif "water energy" in text:
            predicate = lambda energy: energy_provides_type(
                energy, PokemonTypes.WATER.value)
        elif "basic energy" in text:
            predicate = is_basic_energy
        # The enclosing on-play "you may" prompt is the decline path.  Once
        # accepted, "if you do" requires at least one Energy before the
        # switch, while subsequent Energy choices remain optional.
        moved = []
        used = set()
        while True:
            pool = [
                energy for pokemon in sources
                for energy in ctx.attached_energies(pokemon)
                if energy.entity_id not in used
                and (predicate is None or predicate(energy))
            ]
            picked = await ctx.choose_cards(
                pool, 1, minimum=None if not moved else 0,
                prompt="Choose Energy to move",
            ) if pool else []
            if not picked:
                break
            energy = picked[0]
            used.add(energy.entity_id)
            if await ctx.move_energy(energy, ctx.source):
                moved.append((energy, ctx.source))
        if (moved or "if you do" not in text) and ctx.source in ctx.my_bench():
            await ctx.switch_active(ctx.player_id, ctx.source)
        return

    # Legendary Ascent has the inverse printed order: Ho-Oh enters the Bench,
    # becomes Active, and only then consolidates Water Energy onto itself.
    if "switch it with your active pokémon" in text \
            and "if you do, move any number of water energy" in text:
        if ctx.source not in ctx.my_bench():
            return
        await ctx.switch_active(ctx.player_id, ctx.source)
        await ctx.move_energy_freely(
            [p for p in ctx.my_pokemon_in_play() if p is not ctx.source],
            [ctx.source],
            predicate=lambda energy: energy_provides_type(
                energy, PokemonTypes.WATER.value),
            max_count=None,
            prompt="Choose Water Energy to move",
        )
        return

    # Fighting Tag moves every Fighting Energy off the current Active before
    # promoting Machamp.  The generic Energy-transfer branch used to return
    # before the required switch.
    if "if machamp is on your bench" in text \
            and "move all fighting energy attached to your active" in text:
        active = ctx.my_active()
        if ctx.source not in ctx.my_bench() or active is None:
            return
        moved = []
        for energy in list(ctx.attached_energies(active)):
            if energy_provides_type(energy, PokemonTypes.FIGHTING.value) \
                    and await ctx.move_energy(energy, ctx.source):
                moved.append((energy, ctx.source))
        if moved:
            await ctx.switch_active(ctx.player_id, ctx.source)
        return

    # Bench/Active movement powers.
    if any(phrase in text for phrase in (
            "if this pokémon is on your bench, you may switch it with your active",
            "choose a water pokémon on your bench and switch it with your active",
            "switch your active tag team pokémon with 1 of your benched pokémon",
            "if this pokémon is on the bench, switch it with your active pokémon. or,")):
        if "choose a water pokémon" in text:
            candidates = [p for p in ctx.my_bench() if _is_type(p, PokemonTypes.WATER)]
        elif "tag team" in text:
            # The Active is the named TAG TEAM; its replacement may be any
            # Benched Pokemon.
            candidates = list(ctx.my_bench())
        elif ctx.source in ctx.my_bench():
            candidates = [ctx.source]
        else:
            candidates = list(ctx.my_bench())
        target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
            candidates, "Choose your new Active Pokémon") if candidates else None
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
        return

    # Hand-only self-entry powers.  Staging the card on the Bench and then
    # using the shared switch primitive preserves all movement triggers and
    # animation ordering.
    hand = getattr(ctx, "hand", lambda: [])
    if ctx.source in hand() and any(phrase in text for phrase in (
            "play this pokémon as your new active pokémon",
            "put this pokémon onto your bench")):
        allowed = True
        if "opponent has any stage 2 pokémon" in text:
            allowed = any(
                p.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value
                for p in ctx.opponent_pokemon_in_play()
            )
        if "more prize cards remaining" in text:
            own_prizes = ctx.board.find_player_area(ctx.player_id, "prizePile")
            opposing_prizes = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
            allowed = len(own_prizes.children if own_prizes else []) > len(
                opposing_prizes.children if opposing_prizes else [])
        if allowed and await ctx.bench_pokemon(ctx.source) \
                and "new active pokémon" in text:
            await ctx.switch_active(ctx.player_id, ctx.source)
        return

    # Inspect the opponent's deck and discard any Items found there.
    if "top 6 cards of your opponent's deck" in text \
            and "discard any number of item cards" in text:
        viewed = ctx.deck_top(6, ctx.opponent_id)
        await ctx.reveal_cards(viewed, to_player=ctx.player_id)
        items = [card for card in viewed if is_item_card(card)]
        picked = await ctx.choose_cards(
            items, len(items), minimum=0,
            prompt="Choose Item cards to discard", display_cards=viewed,
        ) if items else []
        await ctx.discard_cards(picked)
        await ctx.shuffle_deck(ctx.opponent_id)
        return

    # Direct devolution powers (Ancient Wing / Initialize).
    if "devolve" in text and "highest stage evolution card" in text:
        targets = [p for p in ctx.opponent_pokemon_in_play()
                   if is_evolution_pokemon(p)]
        if "each of your opponent's evolved pokémon" in text:
            for target in list(targets):
                await ctx.devolve_pokemon(target, 1, destination="hand")
        else:
            target = await ctx.choose_pokemon(
                targets, "Choose an evolved Pokémon") if targets else None
            if target is not None:
                await ctx.devolve_pokemon(target, 1, destination="hand")
        return

    # Move existing opposing damage counters rather than placing new ones.
    move_counters = re.search(
        r"move (\d+) damage counters from 1 of your opponent's pokémon to another",
        text,
    )
    if move_counters:
        sources = [p for p in ctx.opponent_pokemon_in_play() if _damaged(ctx, p)]
        source = await ctx.choose_pokemon(
            sources, "Choose a Pokémon with damage counters") if sources else None
        targets = [p for p in ctx.opponent_pokemon_in_play() if p is not source]
        target = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to receive the damage counters") \
            if source is not None and targets else None
        if source is not None and target is not None:
            await ctx.move_damage_counters(
                source, target, min(int(move_counters.group(1)),
                                    _damage_counter_count(ctx, source)))
        return

    # Costs that discard an Energy from the hand without a following draw.
    if "discard a water energy card from your hand" in text \
            and not any(word in text for word in ("if you do", "in order to")):
        await ctx.discard_from_hand(
            1, predicate=lambda card: _energy_type(card, PokemonTypes.WATER),
            prompt="Choose a Water Energy to discard",
        )
        return

    # Swap a hand card with the top card of the deck while keeping both
    # identities private (Evidence Gathering).
    if "switch a card from your hand with the top card of your deck" in text:
        top = next(iter(ctx.deck_top(1)), None)
        chosen = await _choose_one(ctx, ctx.hand(), "Choose a card from your hand") \
            if top is not None else None
        if chosen is not None and top is not None:
            await ctx.put_on_top_of_deck(chosen)
            await ctx.put_in_hand([top], reveal=False)
        return

    # Look at the top card and optionally discard it (Excavate / Snack Seek).
    if "look at the top card of your deck" in text \
            and "you may discard that card" in text:
        top = next(iter(ctx.deck_top(1)), None)
        if top is not None:
            await ctx.reveal_cards([top], to_player=ctx.player_id)
            if await ctx.ask_yes_no("Discard that card?"):
                await ctx.discard_cards([top])
        return

    # Simple Special-Condition cures (CURE / Happiness Supplement).
    if "remove all special conditions from your active pokémon" in text:
        await ctx.cure_all_conditions(ctx.my_active())
        return
    if "remove a special condition from your active pokémon" in text:
        active = ctx.my_active()
        if active is not None:
            heal = re.search(r"heal (\d+) damage", text)
            if heal:
                await ctx.heal(int(heal.group(1)), active)
            for condition in SpecialConditions:
                if condition is not SpecialConditions.UNSET \
                        and await ctx.cure_condition(active, condition):
                    break
        if "discard this pokémon" in text and ctx.source in ctx.hand():
            await ctx.discard_cards([ctx.source])
        return

    # Evolution shields share one lifetime and protect both damage and attack
    # effects through the opponent's next turn.
    if "prevent all" in text and "opponent's" in text \
            and ("until the end of your opponent's next turn" in text
                 or "during your opponent's next turn" in text):
        ctx.add_passive_through_opponents_turn(
            ctx.source, _BWTurnShield(prevent_all=True))
        return

    # All-type healing powers.
    feast = re.search(r"heal (\d+) damage from each of your ([a-z]+) pokémon", text)
    if feast:
        ptype = getattr(PokemonTypes, feast.group(2).upper(), None)
        if ptype is not None:
            for pokemon in ctx.my_pokemon_in_play():
                if _is_type(pokemon, ptype):
                    await ctx.heal(int(feast.group(1)), pokemon)
        return

    # Tool search directly onto the Ability's source.
    if "search your deck for a pokémon tool card and attach it to this pokémon" in text:
        picks = await ctx.search_deck(
            is_pokemon_tool, 1, minimum=0, prompt="Choose a Pokémon Tool")
        if picks:
            await ctx.attach_card(picks[0], ctx.source)
        await ctx.shuffle_deck()
        return

    # Discard-an-Energy damage boosts (Incendiary Song).
    boost = re.search(
        r"discard a basic ([a-z]+) energy card from your hand.*"
        r"attacks used by your pokémon do (\d+) more damage", text,
    )
    if boost:
        ptype = getattr(PokemonTypes, boost.group(1).upper(), None)
        paid = await ctx.discard_from_hand(
            1,
            predicate=lambda card, ptype=ptype: ptype is not None
            and is_basic_energy(card)
            and energy_provides_type(card, ptype.value),
            prompt=f"Choose a {boost.group(1).title()} Energy to discard",
        )
        if paid:
            ctx.add_turn_damage_modifier(TurnDamageModifier(
                amount=int(boost.group(2)), player_id=ctx.player_id))
        return

    # Energy-costed gust (Jet Geyser).
    if "discard a water energy card from your hand" in text \
            and "your opponent switches their active" in text:
        paid = await ctx.discard_from_hand(
            1, predicate=lambda card: _energy_type(card, PokemonTypes.WATER),
            prompt="Choose a Water Energy to discard",
        )
        if paid:
            bench = list(ctx.opponent_bench())
            target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench, "Choose the new Active Pokémon",
                player_id=ctx.opponent_id) if bench else None
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        return

    # Attach one of each of two printed basic Energy types from the hand
    # (Hurricane Charge / Pyro Dance).
    pair_hand = re.search(
        r"attach a (?:basic )?([a-z]+) energy card, a (?:basic )?([a-z]+) "
        r"energy card, or 1 of each from your hand", text,
    )
    if pair_hand:
        choices = []
        for word in pair_hand.groups():
            ptype = getattr(PokemonTypes, word.upper(), None)
            candidates = [
                card for card in ctx.hand()
                if is_basic_energy(card) and ptype is not None
                and energy_provides_type(card, ptype.value)
            ]
            if candidates:
                picked = await _choose_one(
                    ctx, candidates, f"Choose a {word.title()} Energy")
                if picked is not None:
                    choices.append(picked)
        for energy in choices:
            targets = list(ctx.my_pokemon_in_play())
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon") if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
        return

    # Search one basic Energy of each named type and distribute them
    # independently (Strong Charge / X-Boot).
    if "search your deck for" in text and "attach them" in text \
            and len(re.findall(
                r"(?:basic )?(?:grass|fire|water|lightning|psychic|fighting|"
                r"darkness|metal) energy card", text)) >= 2:
        type_words = re.findall(
            r"(?:basic )?(grass|fire|water|lightning|psychic|fighting|darkness|metal) "
            r"energy card", text,
        )
        picks = []
        for word in dict.fromkeys(type_words):
            ptype = getattr(PokemonTypes, word.upper())
            found = await ctx.search_deck(
                lambda card, ptype=ptype: is_basic_energy(card)
                and energy_provides_type(card, ptype.value),
                1, minimum=0, prompt=f"Choose a {word.title()} Energy",
            )
            picks.extend(found)
        for energy in picks:
            targets = list(ctx.my_pokemon_in_play())
            if "psychic pokémon and metal pokémon" in text:
                targets = [p for p in targets if any(t in effective_pokemon_types(
                    ctx.board, p) for t in (
                        PokemonTypes.PSYCHIC.value, PokemonTypes.METAL.value))]
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon") if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
        await ctx.shuffle_deck()
        return

    # Evolution-triggered discard rescue for both players (Lifeboat).
    if "each player puts a basic pokémon from their discard pile onto their bench" in text:
        for pid in (ctx.opponent_id, ctx.player_id):
            discard = ctx.discard_pile(pid)
            basics = [card for card in discard if is_basic_pokemon(card)]
            target = await _choose_one(
                ctx, basics, "Choose a Basic Pokémon", player_id=pid) \
                if basics else None
            if target is not None:
                await ctx.bench_pokemon(target)
        return

    # Supporter recovery to deck/hand.
    if "supporter card from your discard pile on top of your deck" in text:
        candidates = [card for card in ctx.discard_pile() if is_supporter_card(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a Supporter") \
            if candidates else None
        if chosen is not None:
            await ctx.put_on_top_of_deck(chosen)
        return
    if "supporter card from your opponent's discard pile into their hand" in text:
        candidates = [card for card in ctx.discard_pile(ctx.opponent_id)
                      if is_supporter_card(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a Supporter") \
            if candidates else None
        if chosen is not None:
            await ctx.put_in_hand([chosen], reveal=True)
        return

    # Exchange a face-down Prize with the top card of a deck without exposing
    # either identity (Mischievous Trick / Pantomime).
    if "switch 1 of your face-down prize cards with the top card of your deck" in text:
        prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        prizes = list(prize_area.children) if prize_area else []
        top = next(iter(ctx.deck_top(1)), None)
        prize = await _choose_one(ctx, prizes, "Choose a Prize card") \
            if prizes and top is not None else None
        if prize is not None:
            await ctx.put_on_top_of_deck(prize)
            await ctx.put_in_prizes([top])
        return

    # Deck-top manipulation powers.
    if "top 2 cards of your deck" in text and "your opponent chooses 1" in text:
        viewed = ctx.deck_top(2)
        await ctx.reveal_cards(viewed)
        chosen = await _choose_one(
            ctx, viewed, "Choose a card", player_id=ctx.opponent_id) \
            if viewed else None
        if chosen is not None:
            await ctx.put_in_hand([chosen], reveal=True)
            other = next((card for card in viewed if card is not chosen), None)
            if other is not None:
                await ctx.put_on_bottom_of_deck(other)
        return
    if "top 2 cards of your opponent's deck" in text \
            and "put the other card on the bottom" in text:
        viewed = ctx.deck_top(2, ctx.opponent_id)
        await ctx.reveal_cards(viewed, to_player=ctx.player_id)
        keep = await _choose_one(ctx, viewed, "Choose the card to leave on top") \
            if viewed else None
        other = next((card for card in viewed if card is not keep), None)
        if other is not None:
            await ctx.put_on_bottom_of_deck(other)
        if keep is not None:
            await ctx.put_on_top_of_deck(keep)
        return
    if "top card of your opponent's deck on the bottom" in text:
        top = next(iter(ctx.deck_top(1, ctx.opponent_id)), None)
        if top is not None:
            await ctx.put_on_bottom_of_deck(top)
        return

    # Hand reset powers.
    if "either player" in text and "shuffles" in text \
            and "hand into" in text and "draws 4 cards" in text:
        pick = await ctx.choose(
            "Choose a player", ["You", "Your opponent"], use_panel=False)
        pid = ctx.player_id if pick == 0 else ctx.opponent_id
        await ctx.shuffle_into_deck(list(ctx.hand(pid)), player_id=pid)
        await ctx.draw_cards(4, player_id=pid)
        return
    if "opponent shuffles their hand and puts it on the bottom" in text:
        moved = await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
        if moved:
            draw = re.search(r"they draw (\d+) cards", text)
            await ctx.draw_cards(
                int(draw.group(1)) if draw else 4,
                player_id=ctx.opponent_id,
            )
        return
    if "shuffle your hand and put it on the bottom of your deck" in text:
        moved = await ctx.hand_to_bottom_of_deck(ctx.player_id)
        if moved:
            draw = re.search(r"draw (?:a|one|(\d+)) cards?", text)
            await ctx.draw_cards(
                int(draw.group(1)) if draw and draw.group(1) else 1
            )
        return
    opponent_reset = re.search(
        r"opponent shuffle(?:s)? (?:his or her|their) hand into "
        r"(?:his or her|their) deck and draw(?:s)? (\d+) cards", text,
    )
    if opponent_reset:
        await ctx.shuffle_into_deck(
            list(ctx.hand(ctx.opponent_id)), player_id=ctx.opponent_id)
        await ctx.draw_cards(int(opponent_reset.group(1)), player_id=ctx.opponent_id)
        return
    if "opponent shuffle" in text and "hand into" in text \
            and "card for each of" in text and "remaining prize cards" in text:
        await ctx.shuffle_into_deck(
            list(ctx.hand(ctx.opponent_id)), player_id=ctx.opponent_id)
        prizes = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
        await ctx.draw_cards(
            len(prizes.children) if prizes is not None else 0,
            player_id=ctx.opponent_id,
        )
        return

    # Stadium-discard acceleration (Grind Up / Teleport Room).
    if "discard any stadium card in play" in text and "if you do" in text:
        stadium = await ctx.discard_stadium()
        if stadium is None:
            return
        if "attach up to 3" in text and "energy cards from your hand" in text:
            candidates = [
                card for card in ctx.hand()
                if is_energy_card(card) and any(energy_provides_type(card, t.value)
                    for t in (PokemonTypes.FIRE, PokemonTypes.METAL))
            ]
            picks = await ctx.choose_cards(
                candidates, min(3, len(candidates)), minimum=0,
                prompt="Choose Fire or Metal Energy") if candidates else []
            for energy in picks:
                await ctx.attach_energy(energy, ctx.source)
        elif "stadium card with a different name from your discard pile" in text:
            candidates = [card for card in ctx.discard_pile()
                          if card.get_attribute(AttrID.TRAINER_TYPE)
                          and _name(card).casefold() != _name(stadium).casefold()
                          and "stadium" in set(str(v).casefold() for v in (
                              getattr(def_for(card.archetype_id), "subtypes", []) or []))]
            chosen = await _choose_one(ctx, candidates, "Choose a Stadium") \
                if candidates else None
            if chosen is not None:
                area = ctx.board.find_global_area("activeStadium")
                if area is not None:
                    position = len(area.children)
                    ctx.board.move_card(chosen.entity_id, area.entity_id)
                    ctx._queue_intro_and_move(chosen, area.entity_id, position)
        return

    # Blazing Energy changes every attached Energy on the owner's side for
    # the rest of the current turn, including later attachments.
    if "all energy attached to your pokémon are fire energy" in text:
        ctx.add_temporary_player_passive(
            ctx.player_id,
            _BWTemporaryEnergyType(ctx.player_id, PokemonTypes.FIRE),
            ctx.session.turn_state.turn_number,
        )
        return

    # Freely redistribute Energy already in play (Celebration Wind).
    if "move as many energy cards attached to your pokémon as you like" in text:
        pokemon = list(ctx.my_pokemon_in_play())
        await ctx.move_energy_freely(
            pokemon, pokemon, max_count=None, prompt="Choose Energy to move")
        return

    # Active-entry Energy consolidation powers.
    if "move any amount of" in text and "energy from your" in text \
            and "to your active pokémon" in text:
        predicate = None
        for word, ptype in (
                ("fire", PokemonTypes.FIRE), ("water", PokemonTypes.WATER),
                ("lightning", PokemonTypes.LIGHTNING),
                ("metal", PokemonTypes.METAL)):
            if f"{word} energy" in text:
                predicate = lambda energy, ptype=ptype: energy_provides_type(
                    energy, ptype.value)
                break
        active = ctx.my_active()
        if active is not None:
            await ctx.move_energy_freely(
                [p for p in ctx.my_bench() if p is not active], [active],
                predicate=predicate, max_count=None,
                prompt="Choose Energy to move",
            )
        return

    # End-of-turn and Checkup effects.
    if "at the end of your turn" in text and "discard the top" in text:
        count = int((re.search(r"top (\d+) cards", text) or [None, 1])[1])
        await ctx.discard_cards(ctx.deck_top(count))
        return
    if "during pokémon checkup" in text and "put 1 damage counter" in text:
        if _is_active(ctx.source) and ctx.opponent_active() is not None:
            await ctx.deal_damage(
                10, target=ctx.opponent_active(), apply_modifiers=False,
                as_counters=True, is_attack=False)
        return

    # Top-five Trainer selection followed by Sleep (Stellar Wish).
    if "top 5 cards of your deck" in text and "reveal a trainer card" in text:
        viewed = ctx.deck_top(5)
        candidates = [card for card in viewed if is_trainer_card(card)]
        chosen = await _choose_one(ctx, candidates, "Choose a Trainer card",
                                   optional=True) if candidates else None
        if chosen is not None:
            await ctx.put_in_hand([chosen], reveal=True)
        await ctx.shuffle_deck()
        await ctx.apply_special_condition(ctx.source, SpecialConditions.ASLEEP)
        return

    # Healing that requires discarding an attached Special Energy.
    if "discard a special energy from this pokémon" in text \
            and "heal 80 damage" in text:
        candidates = [e for e in ctx.attached_energies(ctx.source)
                      if is_special_energy(e)]
        chosen = await _choose_one(ctx, candidates, "Choose a Special Energy") \
            if candidates else None
        if chosen is not None:
            await ctx.discard_cards([chosen])
            await ctx.heal(80, ctx.source)
        return

    # Temporary printed type changes.
    type_change = re.search(
        r"(?:this pokémon's|[a-z0-9' -]+?'s) type is "
        r"(grass|fire|water|lightning|psychic|"
        r"fighting|darkness|metal) until the end of your turn", text)
    if type_change:
        ptype = getattr(PokemonTypes, type_change.group(1).upper())
        ctx.add_temporary_passive(
            ctx.source, _BWTemporaryPokemonType(ptype),
            ctx.session.turn_state.turn_number)
        return

    # Bench-only single-target healing.
    bench_heal = re.search(r"heal (\d+) damage from 1 of your benched pokémon", text)
    if bench_heal:
        candidates = [p for p in ctx.my_bench() if _damaged(ctx, p)]
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") \
            if candidates else None
        if target is not None:
            await ctx.heal(int(bench_heal.group(1)), target)
        return

    # Keep exactly three chosen Benched Pokemon (Weed Out).
    if "choose 3 of your benched pokémon" in text \
            and "discard your other benched pokémon" in text:
        bench = list(ctx.my_bench())
        keep = await ctx.choose_cards(
            bench, min(3, len(bench)), minimum=min(3, len(bench)),
            prompt="Choose Pokémon to keep") if bench else []
        for pokemon in [p for p in bench if p not in keep]:
            await ctx.discard_cards(full_stack(pokemon))
        return

    # Hand-origin lost-zone peek (Mountain Pass).
    if ctx.source in ctx.hand() and "put this pokémon in the lost zone" in text \
            and "top card of your opponent's deck" in text:
        top = next(iter(ctx.deck_top(1, ctx.opponent_id)), None)
        await ctx.move_to_lost_zone([ctx.source])
        if top is not None:
            await ctx.reveal_cards([top], to_player=ctx.player_id)
            if is_supporter_card(top) and await ctx.ask_yes_no(
                    "Put that Supporter in the Lost Zone?"):
                await ctx.move_to_lost_zone([top])
        return

    # Search for any card, shuffle, then leave the chosen card on top.
    if "search your deck for a card" in text \
            and "put that card on top" in text:
        picks = await ctx.search_deck(
            None, 1, minimum=1, prompt="Choose a card to put on top"
        )
        await ctx.shuffle_deck()
        if picks:
            await ctx.put_on_top_of_deck(picks[0])
        return

    # Look/reorder effects.  A player may also be named explicitly; the deck
    # owner's client makes the private ordering choice.
    reorder = re.search(
        r"look at the top (\d+) cards? of (your|your opponent's|either player's|"
        r"that player's) deck.*put them back (?:on top )?.*in any order",
        text,
    )
    if reorder:
        count = int(reorder.group(1))
        owner = ctx.player_id
        if reorder.group(2) in ("your opponent's", "that player's"):
            owner = ctx.opponent_id
        # "Either player's" needs a choice in the live client.  Choosing the
        # acting player's deck is the deterministic AI fallback.
        await ctx.reorder_deck_top(count, player_id=owner)
        return

    # Plain information-only looks still need to reveal the actual cards to
    # the acting player instead of behaving as no-ops.
    look_top = re.search(
        r"look at the top (?:(\d+) cards?|card) of (your|your opponent's) deck",
        text,
    )
    if look_top and not any(word in text for word in (
            "attach", "discard", "put ", "shuffle", "choose")):
        count = int(look_top.group(1) or 1)
        owner = ctx.opponent_id if look_top.group(2) == "your opponent's" \
            else ctx.player_id
        await ctx.reveal_cards(ctx.deck_top(count, owner), to_player=ctx.player_id)
        return

    # Put searched Basic/named Pokemon directly onto the Bench.
    if "search your deck" in text and "put it onto your bench" in text \
            or "search your deck" in text and "put them onto your bench" in text:
        count = _ability_search_count(text)
        predicate = _ability_search_predicate(text)
        if "restored pokémon" in text:
            predicate = lambda card: is_pokemon_card(card) and (
                "RESTORED" in {
                    str(value).upper() for value in
                    (getattr(def_for(card.archetype_id), "subtypes", []) or [])
                }
            )
        names = re.search(
            r"search your deck for (?:up to \d+ )?([a-z0-9' -]+?)(?:,| and) put",
            text,
        )
        if names and not any(noun in names.group(1) for noun in (
                "pokémon", "energy", "card")):
            wanted = {part.strip() for part in re.split(r"\s+or\s+", names.group(1))}
            predicate = lambda card, wanted=wanted: _name(card).casefold() in wanted
        picks = await ctx.search_deck(
            predicate, count, minimum=0, prompt="Choose Pokémon for your Bench"
        )
        for pokemon in picks:
            if len(ctx.my_bench()) >= effective_bench_capacity(ctx.board, ctx.player_id):
                break
            await ctx.bench_pokemon(pokemon)
        await ctx.shuffle_deck()
        return

    # Search-and-discard acceleration setup (Fresh Squeezed/Dig Dig Dig).
    if "search your deck for" in text and "basic" in text \
            and "energy" in text and "discard them" in text:
        count = _ability_search_count(text)
        picks = await ctx.search_deck(
            _ability_search_predicate(text), count, minimum=0,
            prompt="Choose Energy cards to discard",
        )
        await ctx.discard_cards(picks)
        await ctx.shuffle_deck()
        return

    # Search the deck for an Evolution and put it directly on this Pokemon.
    if "search your deck for a card that evolves from this pokémon" in text \
            or "search your deck for an unfezant" in text:
        logic = ctx.source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        names = {"unfezant", "unfezant ex"} if "unfezant" in text else None
        def can_evolve(card):
            if not is_evolution_pokemon(card):
                return False
            return (
                names is not None and _name(card).casefold() in names
            ) or card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic
        picks = await ctx.search_deck(
            can_evolve, 1, minimum=0, prompt="Choose an Evolution Pokémon"
        )
        if picks:
            await ctx.evolve_pokemon(ctx.source, picks[0])
            counters = re.search(r"(?:put|place) (\d+) damage counters? on", text)
            if counters:
                await ctx.deal_damage(
                    int(counters.group(1)) * 10, target=picks[0],
                    apply_modifiers=False, as_counters=True, is_attack=False,
                )
        await ctx.shuffle_deck()
        return

    # Evolution powers that choose the card from hand (Ascension DNA,
    # Quick-Ripening Herb, Spiteful Evolution).
    if "in your hand that evolves from" in text \
            or "card in your hand that evolves from this pokémon" in text \
            or "stage 2 card in your hand that evolves from" in text:
        target = ctx.source
        if "choose 1 of your basic pokémon" in text:
            basics = [pokemon for pokemon in ctx.my_pokemon_in_play()
                      if is_basic_pokemon(pokemon)]
            target = await ctx.choose_pokemon(
                basics, "Choose a Basic Pokémon"
            ) if basics else None
        if target is None:
            return
        logic = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        # Ascension DNA is printed on Eevee-GX but explicitly asks for a card
        # that evolves from *Eevee*.  Do not derive that relationship from the
        # source's own EeveeGX logic name.  Other versions of this wording use
        # "this/that Pokémon" and continue to use the selected target.
        named_base = re.search(
            r"in your hand that evolves from ([a-z0-9 .'-]+?)(?:,| you may|\.)",
            text,
        )
        if named_base and named_base.group(1) not in ("this pokémon", "that pokémon"):
            wanted = named_base.group(1).strip().casefold()
            base_definition = next((
                definition for definition in CARD_DEFS_BY_GUID.values()
                if (getattr(definition, "display_name", "") or "").casefold()
                    == wanted
                and definition.extra_attributes.get(
                    str(AttrID.EVOLUTION_LOGIC_NAME.value)
                )
            ), None)
            if base_definition is not None:
                logic = base_definition.extra_attributes[
                    str(AttrID.EVOLUTION_LOGIC_NAME.value)
                ]["value"]
        candidates = [
            card for card in ctx.hand()
            if is_evolution_pokemon(card)
            and evolves_from(card.archetype_id, logic)
        ]
        if "stage 2 card" in text:
            candidates = [card for card in candidates
                          if card.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value]
        chosen = await _choose_one(ctx, candidates, "Choose an Evolution Pokémon") \
            if candidates else None
        if chosen is not None:
            if "heal all damage" in text:
                await ctx.heal(ctx.max_hp(target), target)
            await ctx.evolve_pokemon(target, chosen)
            counters = re.search(r"(?:put|place) (\d+) damage counters? on", text)
            if counters:
                await ctx.deal_damage(
                    int(counters.group(1)) * 10, target=chosen,
                    apply_modifiers=False, as_counters=True, is_attack=False,
                )
        return

    # Modern condition wording uses "make"/"leave" instead of "is now".
    condition_words = (
        ("asleep", SpecialConditions.ASLEEP),
        ("burned", SpecialConditions.BURNED),
        ("confused", SpecialConditions.CONFUSED),
        ("paralyzed", SpecialConditions.PARALYZED),
        ("poisoned", SpecialConditions.POISONED),
    )
    if any(
        phrase in text for phrase in (
            "make your opponent's active pokémon", "leave your opponent's active pokémon",
            "both active pokémon confused", "both active pokémon poisoned",
        )
    ) or "both active pokémon" in text and any(
            word in text for word, _ in condition_words):
        for word, condition in condition_words:
            if word not in text:
                continue
            targets = [ctx.opponent_active()]
            if f"both active pokémon {word}" in text \
                    or "both active pokémon" in text and word in text \
                    or f"leave both active pokémon {word}" in text:
                targets = [ctx.my_active(), ctx.opponent_active()]
            for target in targets:
                if target is not None and not (
                        "except for grass pokémon" in text
                        and _is_type(target, PokemonTypes.GRASS)):
                    await ctx.apply_special_condition(target, condition)
        return

    # Checkup add-ons and replacements for Burn/Poison/Confusion.
    if "between turns" in text or "during pokémon checkup" in text:
        source_active = _is_active(ctx.source)
        opponent = ctx.opponent_active()
        if opponent is not None and source_active:
            conditions = set(opponent.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
            amount = 0
            if "burned pokémon" in text and \
                    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.BURNED] in conditions:
                replacement = re.search(r"put (\d+) damage counters instead of 2", text)
                extra = re.search(r"put (\d+) more damage counters", text)
                amount = (int(replacement.group(1)) - 2 if replacement else
                          int(extra.group(1)) if extra else 0)
            elif "poisoned pokémon" in text and \
                    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED] in conditions:
                replacement = re.search(r"put (\d+) damage counters instead of 1", text)
                extra = re.search(r"put (\d+) more damage counters", text)
                amount = (int(replacement.group(1)) - 1 if replacement else
                          int(extra.group(1)) if extra else 0)
            elif "confused pokémon" in text and \
                    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED] in conditions:
                amount = int((re.search(r"put (\d+) damage counters", text)
                              or [None, 0])[1])
            elif "remains asleep" in text \
                    and CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP] in set(
                        ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
                    ):
                amount = int((re.search(r"put (\d+) damage counters", text)
                              or [None, 0])[1])
            if amount > 0:
                await ctx.deal_damage(
                    amount * 10, target=opponent, apply_modifiers=False,
                    as_counters=True, is_attack=False,
                )
                return

    # Information and hand-disruption abilities.
    if "both you and your opponent reveal your hands" in text:
        await ctx.reveal_hand(ctx.player_id, ctx.player_id)
        await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        return
    if any(phrase in text for phrase in (
            "opponent reveal their hand", "opponent reveals their hand",
            "look at your opponent's hand")):
        revealed = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        if "discard a card" in text or "choose a card" in text and "discard it" in text:
            chosen = await _choose_one(ctx, revealed, "Choose a card to discard") \
                if revealed else None
            if chosen is not None:
                await ctx.discard_cards([chosen])
        elif "shuffle them into their deck" in text:
            count = int((re.search(r"choose (\d+)", text) or [None, 1])[1])
            chosen = await ctx.choose_cards(
                revealed, min(count, len(revealed)), minimum=min(count, len(revealed)),
                prompt="Choose cards to shuffle into the deck",
            ) if revealed else []
            await ctx.shuffle_into_deck(chosen, player_id=ctx.opponent_id)
        elif "put any number of basic pokémon" in text:
            candidates = [card for card in revealed if is_basic_pokemon(card)]
            free = max(0, effective_bench_capacity(ctx.board, ctx.opponent_id)
                       - len(ctx.opponent_bench()))
            picks = await ctx.choose_cards(
                candidates, min(free, len(candidates)), minimum=0,
                prompt="Choose Basic Pokémon for your opponent's Bench",
            ) if candidates and free else []
            for pokemon in picks:
                await ctx.bench_pokemon(pokemon)
        elif "put a basic pokémon you find there onto your opponent's bench" in text:
            candidates = [card for card in revealed if is_basic_pokemon(card)]
            chosen = await _choose_one(ctx, candidates, "Choose a Basic Pokémon") \
                if candidates else None
            if chosen is not None:
                await ctx.bench_pokemon(chosen)
                counters = re.search(r"put (\d+) damage counters on that pokémon", text)
                if counters:
                    await ctx.deal_damage(
                        int(counters.group(1)) * 10, target=chosen,
                        apply_modifiers=False, as_counters=True, is_attack=False,
                    )
        return

    # A large family simply retrieves named/typed public-discard cards.
    if "from your discard pile" in text and "into your hand" in text:
        count = int((re.search(r"(?:put|choose) (?:up to )?(\d+)", text)
                     or [None, 1])[1])
        candidates = list(ctx.discard_pile())
        predicate = _ability_search_predicate(text)
        if predicate is not None:
            candidates = [card for card in candidates if predicate(card)]
        named = re.search(
            r"put (?:up to \d+|\d+|an?|the) ([a-z0-9' -]+?) cards? from",
            text,
        )
        if named and not any(noun in named.group(1) for noun in (
                "pokémon", "energy", "trainer", "supporter", "item")):
            wanted = named.group(1).strip().casefold()
            candidates = [card for card in candidates
                          if _name(card).casefold() == wanted]
        maximum = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0 if "up to" in text else maximum,
            prompt="Choose cards from your discard pile",
        ) if maximum else []
        await ctx.put_in_hand(picks, reveal=True)
        return

    # Direct removal of opposing Energy/Tools on play/evolution.
    if "discard a special energy from" in text \
            or "discard an energy attached to your opponent's active" in text:
        pool = [
            energy for pokemon in ctx.opponent_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon)
            if "special energy" not in text or is_special_energy(energy)
        ]
        if "opponent's active" in text:
            active = ctx.opponent_active()
            pool = [energy for energy in (ctx.attached_energies(active) if active else [])
                    if "special energy" not in text or is_special_energy(energy)]
        chosen = await _choose_one(ctx, pool, "Choose an Energy to discard") \
            if pool else None
        if chosen is not None:
            await ctx.discard_cards([chosen])
        return

    if "discard all pokémon tool cards attached to your opponent's active" in text:
        active = ctx.opponent_active()
        tools = [card for card in full_stack(active)[1:] if is_pokemon_tool(card)] \
            if active is not None else []
        await ctx.discard_cards(tools)
        return

    # Direct counter placement on several/all opposing Pokemon.
    # Sand Slammer is automatic and only works while Flygon is Active. Keep
    # it ahead of the generic spread selector, which used to swallow it.
    if "between turns" in text \
            and "damage counter on each of your opponent's pokémon" in text:
        if _is_active(ctx.source):
            for pokemon in list(ctx.opponent_pokemon_in_play()):
                await ctx.deal_damage(
                    10, target=pokemon, apply_modifiers=False,
                    as_counters=True, is_attack=False,
                )
        else:
            ctx.suppress_announce = True
        return

    if "damage counters on your opponent's pokémon-gx and pokémon-ex in any way" in text:
        count = int((re.search(r"put (\d+) damage counters", text)
                     or [None, 0])[1])
        targets = [
            pokemon for pokemon in ctx.opponent_pokemon_in_play()
            if "GX" in (subtypes_for(pokemon.archetype_id) or [])
            or _pokemon_ex(pokemon)
        ]
        await ctx.place_damage_counters(count, targets)
        return

    spread = re.search(
        r"(?:choose (\d+) of your opponent's (benched )?pokémon and )?"
        r"put (\d+) damage counters? on each", text,
    )
    if spread:
        pool = ctx.opponent_bench() if spread.group(2) else ctx.opponent_pokemon_in_play()
        count = int(spread.group(1) or len(pool))
        targets = list(pool) if count >= len(pool) else await ctx.choose_cards(
            pool, min(count, len(pool)), minimum=min(count, len(pool)),
            prompt="Choose Pokémon to receive damage counters",
        ) if pool else []
        for target in targets:
            await ctx.deal_damage(
                int(spread.group(3)) * 10, target=target,
                apply_modifiers=False, as_counters=True, is_attack=False,
            )
        return

    distribute = re.search(
        r"put (\d+) damage counters on your opponent's .* in any way you like",
        text,
    )
    if distribute:
        pool = ctx.opponent_pokemon_in_play()
        if "pokémon-gx and pokémon-ex" in text:
            pool = [pokemon for pokemon in pool if _pokemon_ex(pokemon) or
                    "GX" in (getattr(def_for(pokemon.archetype_id), "subtypes", []) or [])]
        for _ in range(int(distribute.group(1))):
            target = await ctx.choose_pokemon(pool, "Choose a Pokémon") if pool else None
            if target is None:
                break
            await ctx.deal_damage(
                10, target=target, apply_modifiers=False,
                as_counters=True, is_attack=False,
            )
        return

    # Whirlpool Suction is a three-part action.  Resolve the gust first, then
    # discard this Pokémon's attachments and return only its top card to the
    # deck bottom.  A broad gust branch previously swallowed the last clauses.
    if "have your opponent switch their active pokémon" in text \
            and "discard all cards attached to this pokémon" in text \
            and "put it on the bottom of your deck" in text:
        bench = list(ctx.opponent_bench())
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose the new Active Pokémon",
            player_id=ctx.opponent_id,
        ) if bench else None
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
            attachments = list(full_stack(ctx.source)[1:])
            if attachments:
                await ctx.discard_cards(attachments)
            await ctx.put_on_bottom_of_deck(ctx.source)
        return

    # Common self/opponent switches, including Active-only wording.
    if "switch this pokémon with your active pokémon" in text \
            or "switch it with your active pokémon" in text:
        if ctx.source in ctx.my_bench():
            await ctx.switch_active(ctx.player_id, ctx.source)
        return
    if "have your opponent switch" in text and "active pokémon" in text:
        bench = ctx.opponent_bench()
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose the new Active Pokémon", player_id=ctx.opponent_id
        ) if bench else None
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
        return

    # Repeated Energy-transfer powers (Psychic Transfer, Wash Out, Fire Off,
    # Solar Transfer, Happy Switch and their exact reprints).
    if "move" in text and "energy from 1 of your" in text \
            and "pokémon" in text:
        sources = ctx.my_pokemon_in_play()
        targets = ctx.my_pokemon_in_play()
        if "benched pokémon to your active" in text:
            sources, targets = ctx.my_bench(), [ctx.my_active()]
        elif "other pokémon to this pokémon" in text:
            sources = [p for p in sources if p is not ctx.source]
            targets = [ctx.source]
        type_match = re.search(
            r"move (?:a|an|any amount of|as many)? ?"
            r"(grass|fire|water|lightning|psychic|fighting|darkness|metal) energy",
            text,
        )
        predicate = None
        if type_match:
            ptype = getattr(PokemonTypes, type_match.group(1).upper())
            predicate = lambda energy, ptype=ptype: energy_provides_type(
                energy, ptype.value
            )
        await ctx.move_energy_freely(
            [p for p in sources if p is not None],
            [p for p in targets if p is not None], predicate=predicate,
            max_count=None if any(word in text for word in (
                "as often", "any amount", "as many")) else 1,
            prompt="Choose Energy to move",
        )
        return

    # All-damage healing printed on evolution abilities.
    if "heal all damage from" in text:
        candidates = [p for p in ctx.my_pokemon_in_play() if _damaged(ctx, p)]
        if "active grass pokémon" in text:
            active = ctx.my_active()
            candidates = [active] if active is not None and _is_type(
                active, PokemonTypes.GRASS) else []
        if "each of your evolution pokémon" in text:
            candidates = [p for p in candidates if is_evolution_pokemon(p)]
            healed = list(candidates)
            for pokemon in candidates:
                await ctx.heal(ctx.max_hp(pokemon), pokemon)
            for pokemon in healed:
                await ctx.discard_cards(ctx.attached_energies(pokemon))
            return
        target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to heal"
        ) if candidates else None
        if target is not None:
            await ctx.heal(ctx.max_hp(target), target)
            if "discard all energy" in text:
                await ctx.discard_cards(ctx.attached_energies(target))
        return

    if ctx.ability.title in ("Rough Skin", "Reflexive Retaliation"):
        attacker = getattr(ctx, "damaged_by", None)
        if attacker is not None and _is_active(ctx.source) \
                and attacker.owning_player_id != ctx.player_id:
            await ctx.deal_damage(20, target=attacker, apply_modifiers=False,
                                  as_counters=True)
        return

    if ctx.ability.title == "Electromagnetic Wall":
        receiver = getattr(ctx, "energy_receiver", None)
        attaching = getattr(ctx, "attaching_player_id", None)
        if receiver is not None and attaching == ctx.opponent_id \
                and receiver.owning_player_id == ctx.opponent_id \
                and _is_active(ctx.source):
            await ctx.deal_damage(30, target=receiver, apply_modifiers=False,
                                  as_counters=True)
        return

    if ctx.ability.title == "Aftermath":
        if ctx.ko_from_attack:
            await ctx.discard_cards(ctx.deck_top(3, ctx.opponent_id))
        return

    if ctx.ability.title == "Spiteful Spirit":
        attacker = getattr(ctx, "ko_attacker", None)
        if ctx.ko_from_attack and ctx.was_active_at_ko and attacker is not None:
            await ctx.apply_special_condition(attacker, SpecialConditions.CONFUSED)
            await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)
        return

    if ctx.ability.title == "Busybody":
        active = ctx.my_active()
        if active is None:
            return
        await ctx.heal(10, active)
        for condition in SpecialConditions:
            if condition == SpecialConditions.UNSET:
                continue
            if await ctx.cure_condition(active, condition):
                break
        await ctx.discard_cards([ctx.source])
        return

    if ctx.ability.title == "Transform":
        candidates = [card for card in ctx.hand()
                      if is_basic_pokemon(card) and card is not ctx.source]
        chosen = await _choose_one(ctx, candidates, "Choose a Basic Pokémon") \
            if candidates else None
        if chosen is not None:
            # Identity swap preserves damage, conditions, attachments and turn
            # stamps exactly as Transform requires. Ditto leaves to the discard
            # as the engine's neutral identity-swap backing card.
            await ctx.identity_swap(ctx.source, chosen, destination="discard",
                                    transfer=True)
        return

    if ctx.ability.title == "Moon Guidance":
        if not (await ctx.flip_coins(1, "Moon Guidance"))[0]:
            return
        pairs = []
        for pokemon in ctx.my_pokemon_in_play():
            logic = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
            for card in ctx.deck():
                if is_evolution_pokemon(card) \
                        and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic:
                    pairs.append((pokemon, card))
        if pairs:
            cards = list(dict.fromkeys(card for _, card in pairs))
            picked = await ctx.search_deck(
                lambda card, valid={candidate.entity_id for candidate in cards}:
                    card.entity_id in valid,
                1, minimum=0,
                prompt="Choose an Evolution Pokémon",
            )
            chosen = picked[0] if picked else None
            if chosen is not None:
                targets = [pokemon for pokemon, card in pairs if card is chosen]
                target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                    targets, "Choose a Pokémon to evolve")
                if target is not None:
                    await ctx.evolve_pokemon(target, chosen)
        await ctx.shuffle_deck()
        return

    if "heal 10 damage from each of your pokémon" in text:
        for pokemon in list(ctx.my_pokemon_in_play()):
            await ctx.heal(10, pokemon)
        return
    between_heal = re.search(r"between turns, heal (\d+) damage from this pokémon", text)
    if between_heal:
        await ctx.heal(int(between_heal.group(1)), ctx.source)
        return

    if "attach a fire energy card from your hand to 1 of your pokémon" in text:
        energies = [c for c in ctx.hand() if _energy_type(c, PokemonTypes.FIRE)]
        energy = await _choose_one(ctx, energies, "Choose a Fire Energy") \
            if energies else None
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(),
                                          "Choose a Pokémon") \
            if energy is not None else None
        if energy is not None and target is not None:
            await ctx.attach_energy(energy, target)
        return

    if ctx.ability.title == "Rebirth":
        if not (await ctx.flip_coins(1, "Rebirth"))[0]:
            return
        if not await ctx.bench_pokemon(ctx.source):
            return
        selected, used_types = [], set()
        while len(selected) < 3:
            candidates = []
            for card in ctx.discard_pile():
                if not is_basic_energy(card):
                    continue
                types = set(card.get_attribute(AttrID.POKEMON_TYPES) or [])
                if types and not (types & used_types):
                    candidates.append(card)
            if not candidates:
                break
            card = await _choose_one(ctx, candidates,
                                     "Choose a basic Energy of a different type")
            if card is None:
                break
            selected.append(card)
            used_types.update(card.get_attribute(AttrID.POKEMON_TYPES) or [])
        for card in selected:
            await ctx.attach_energy(card, ctx.source)
        return

    if "opponent discard cards from his or her hand until" in text:
        match = re.search(r"until he or she has (\d+) cards", text)
        keep = int(match.group(1)) if match else 4
        excess = max(0, ctx.hand_size(ctx.opponent_id) - keep)
        if excess:
            await ctx.discard_from_hand(
                excess, player_id=ctx.opponent_id,
                prompt=f"Choose {excess} cards to discard",
            )
        return

    if "return this pokémon and all cards attached to it to your hand" in text:
        await ctx.put_in_hand(full_stack(ctx.source), reveal=False)
        return

    if "return umbreon and all cards attached to it to your hand" in text:
        if (await ctx.flip_coins(1, ctx.ability.title))[0]:
            await ctx.put_in_hand(full_stack(ctx.source), reveal=False)
        return

    if "look at the top 2 cards of your deck" in text:
        if "choose 1 of them" in text or "put 1 of them into your hand" in text:
            top = ctx.deck_top(2)
            chosen = await _choose_one(ctx, top, "Choose a card to put into your hand") \
                if top else None
            if chosen is not None:
                await ctx.put_in_hand([chosen], reveal=False)
                other = next((card for card in top if card is not chosen), None)
                if other is not None:
                    if "discard the other card" in text:
                        await ctx.discard_cards([other])
                    elif "put the other card on the bottom" in text:
                        await ctx.put_on_bottom_of_deck(other)
        else:
            await ctx.reorder_deck_top(min(2, len(ctx.deck())))
        return

    if "put a card from your hand on the bottom of your deck" in text \
            and "draw cards until you have" in text:
        hand = list(ctx.hand())
        chosen = await _choose_one(ctx, hand, "Choose a card for the deck bottom") \
            if hand else None
        if chosen is not None:
            await ctx.put_on_bottom_of_deck(chosen)
            count = int((re.search(r"until you have (\d+) cards", text)
                         or [None, 5])[1])
            await ctx.draw_until(count)
        return

    if "discard 1 card from your hand" in text and "draw 2 cards" in text:
        paid = await ctx.discard_from_hand(1, prompt="Choose a card to discard")
        if paid:
            await ctx.draw_cards(2)
        return

    if ctx.ability.title == "Cursed Shadow":
        await ctx.place_damage_counters(3, ctx.opponent_pokemon_in_play())
        return

    if ctx.ability.title == "Six Feet Under":
        await ctx.knock_out(ctx.source)
        await ctx.place_damage_counters(3, ctx.opponent_pokemon_in_play())
        return

    if "flip a coin" in text:
        heads = bool((await ctx.flip_coins(1, ctx.ability.title))[0])
        if "if heads, switch in 1 of your opponent's benched pokémon" in text:
            bench = list(ctx.opponent_bench())
            target = await ctx.choose_pokemon(
                bench, "Choose your opponent's new Active Pokémon"
            ) if heads and bench else None
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
                if "new active pokémon is now confused" in text:
                    await ctx.apply_special_condition(
                        ctx.opponent_active(), SpecialConditions.CONFUSED)
            return
        if "put an energy attached to your opponent's active pokémon into their hand" in text:
            active = ctx.opponent_active()
            energies = ctx.attached_energies(active) if active is not None else []
            chosen = await _choose_one(ctx, energies, "Choose an Energy") \
                if heads and energies else None
            if chosen is not None:
                await ctx.put_in_hand([chosen], reveal=False)
            return
        if "search your discard pile for a trainer card" in text \
                and "put it on top of your deck" in text:
            candidates = [card for card in ctx.discard_pile()
                          if is_trainer_card(card)]
            chosen = await _choose_one(ctx, candidates, "Choose a Trainer card") \
                if heads and candidates else None
            if chosen is not None:
                await ctx.reveal_cards([chosen])
                await ctx.put_on_top_of_deck(chosen)
            return
        if "put a card from your discard pile on top of your deck" in text:
            candidates = list(ctx.discard_pile())
            chosen = await _choose_one(ctx, candidates, "Choose a card") \
                if heads and candidates else None
            if chosen is not None:
                await ctx.put_on_top_of_deck(chosen)
            if "your turn ends" in text:
                ctx.ends_turn = True
            return
        if "put an item card from your discard pile on top of your deck" in text:
            candidates = [card for card in ctx.discard_pile()
                          if is_item_card(card)]
            chosen = await _choose_one(ctx, candidates, "Choose an Item card") \
                if heads and candidates else None
            if chosen is not None:
                await ctx.put_on_top_of_deck(chosen)
            return
        condition = next((special for word, special in (
            ("burned", SpecialConditions.BURNED),
            ("asleep", SpecialConditions.ASLEEP),
            ("confused", SpecialConditions.CONFUSED),
            ("paralyzed", SpecialConditions.PARALYZED),
            ("poisoned", SpecialConditions.POISONED),
        ) if f"defending pokémon is now {word}" in text), None)
        if condition is not None:
            if heads and ctx.opponent_active() is not None:
                await ctx.apply_special_condition(ctx.opponent_active(), condition)
            return
        if "if heads, discard an energy attached to your opponent's active" in text:
            if heads and ctx.opponent_active() is not None:
                await ctx.discard_energy_from(ctx.opponent_active(), 1)
            return
        if "if heads, heal 30 damage from your active" in text:
            if heads and ctx.my_active() is not None:
                await ctx.heal(30, ctx.my_active())
            return
        if "if heads, your opponent's active pokémon is now asleep" in text:
            target = ctx.opponent_active() if heads else ctx.my_active()
            if target is not None:
                await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)
            return
        if ctx.ability.title == "Giant Fan":
            if heads:
                target = await ctx.choose_pokemon(
                    ctx.opponent_pokemon_in_play(), "Choose an opponent's Pokémon")
                if target is not None:
                    await ctx.shuffle_into_deck(full_stack(target),
                                                player_id=ctx.opponent_id)
            return

    if "opponent's active pokémon with 1 of his or her benched pokémon" in text \
            or "switch 1 of your opponent's benched pokémon with his or her active" in text:
        if ctx.opponent_bench():
            target = await ctx.choose_pokemon(ctx.opponent_bench(),
                                              "Choose the new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        return

    if "switch your active pokémon with 1 of your benched pokémon" in text:
        if ctx.my_bench():
            target = await ctx.choose_pokemon(ctx.my_bench(), "Choose your new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
        if ctx.opponent_bench():
            target = await ctx.choose_pokemon(ctx.opponent_bench(),
                                              "Choose the opponent's new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        return

    if "opponent reveal his or her hand" in text:
        await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        return

    if "heal 20 damage from 1 of your pokémon that has any grass energy" in text:
        candidates = [p for p in ctx.my_pokemon_in_play()
                      if _damaged(ctx, p) and any(
                          energy_provides_type(e, PokemonTypes.GRASS.value)
                          for e in ctx.attached_energies(p))]
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") \
            if candidates else None
        if target is not None:
            await ctx.heal(20, target)
        return

    if "search your deck for a fire energy card and attach it" in text:
        picks = await ctx.search_deck(
            lambda c: _energy_type(c, PokemonTypes.FIRE), 1, minimum=0,
            prompt="Choose a Fire Energy",
        )
        if picks:
            target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(),
                                              "Choose a Pokémon")
            if target is not None:
                await ctx.attach_energy(picks[0], target)
                await ctx.deal_damage(10, target=target, apply_modifiers=False,
                                      as_counters=True)
        await ctx.shuffle_deck()
        return

    if "opponent's active pokémon is now confused and poisoned" in text:
        target = ctx.opponent_active()
        if target is not None:
            await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)
            await ctx.apply_special_condition(target, SpecialConditions.POISONED)
        return

    m = re.search(r"draw cards until you have (\d+) cards", text)
    if m:
        await ctx.draw_until(int(m.group(1)))
        return
    m = re.search(r"draw (\d+) cards", text)
    if m:
        await ctx.draw_cards(int(m.group(1)))
        return
    m = re.search(r"heal (\d+) damage from (?:1 of )?your pokémon", text)
    if m:
        candidates = [p for p in ctx.my_pokemon_in_play() if _damaged(ctx, p)]
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") if candidates else None
        if target is not None:
            await ctx.heal(int(m.group(1)), target)
        return
    if "search your deck for" in text and re.search(
            r"put (?:it|them|those cards) (?:in|into) your hand", text):
        count = _ability_search_count(text)
        pred = _ability_search_predicate(text)
        picks = await ctx.search_deck(
            pred, count, minimum=0,
            prompt=(
                f"Choose up to {count} cards" if count > 1
                else "Choose a card"
            ),
        )
        await ctx.put_in_hand(
            picks,
            reveal=("reveal" in text or "show it to your opponent" in text),
        )
        await ctx.shuffle_deck()
        if picks and "this pokémon is knocked out" in text:
            await ctx.knock_out(ctx.source)
        return
    if "discard the top" in text and "opponent's deck" in text:
        count = int((re.search(r"top (\d+)", text) or [None, 1])[1])
        await ctx.discard_cards(ctx.deck_top(count, ctx.opponent_id))
        return
    if "move 1 damage counter" in text:
        # Shady Move chooses the damaged source first, then any other Pokémon
        # in play as the destination.  Passing the whole source list into the
        # primitive treated that list as one Pokémon and crashed max-HP lookup.
        pokemon = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        sources = [candidate for candidate in pokemon if _damaged(ctx, candidate)]
        source = await ctx.choose_pokemon(
            sources, "Choose a Pokémon with a damage counter"
        ) if sources else None
        targets = [candidate for candidate in pokemon if candidate is not source]
        target = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to receive the damage counter"
        ) if source is not None and targets else None
        if source is not None and target is not None:
            await ctx.move_damage_counters(source, target, 1)
        return
    if "move a" in text and "energy attached" in text:
        ptype = None
        for word, enum in (("darkness", PokemonTypes.DARKNESS),
                           ("metal", PokemonTypes.METAL),
                           ("grass", PokemonTypes.GRASS)):
            if f"move a {word} energy" in text:
                ptype = enum
        energies = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
                    if ptype is None or energy_provides_type(e, ptype.value)]
        energy = await _choose_one(ctx, energies, "Choose an Energy to move") if energies else None
        if energy is not None:
            targets = [p for p in ctx.my_pokemon_in_play()
                       if p is not carrier_pokemon(energy)]
            target = await ctx.choose_pokemon(targets, "Choose a Pokémon") if targets else None
            if target is not None:
                await ctx.move_energy(energy, target)
        return

    # ------------------------------------------------------------------
    # Cross-era recurring Ability families.  The generated SM/SV catalogs
    # deliberately share this interpreter with BW; keep broad English rules
    # here so one implementation covers every exact reprint.

    # Retaliation after an opposing attack damaged this Pokemon.
    attacker = getattr(ctx, "damaged_by", None)
    if attacker is not None and attacker.owning_player_id != ctx.player_id:
        counters = re.search(
            r"(?:put|place) (\d+) damage counters? on the attacking pokémon",
            text,
        )
        if counters and _is_active(ctx.source):
            await ctx.deal_damage(
                int(counters.group(1)) * 10, target=attacker,
                apply_modifiers=False, as_counters=True, is_attack=False,
            )
            return
        if "attacking pokémon is now poisoned" in text and _is_active(ctx.source):
            await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)
            return
        if "attacking pokémon is now burned" in text and _is_active(ctx.source):
            await ctx.apply_special_condition(attacker, SpecialConditions.BURNED)
            return
        if "damage counters on the attacking pokémon equal to the damage done" in text \
                and _is_active(ctx.source):
            amount = max(0, int(getattr(ctx, "damage_amount", 0) or 0))
            if amount:
                await ctx.deal_damage(
                    amount, target=attacker, apply_modifiers=False,
                    as_counters=True, is_attack=False)
            return
        if "discard an energy from the attacking pokémon" in text \
                and _is_active(ctx.source):
            await ctx.discard_energy_from(attacker, 1)
            return

    # Energy-attachment observers (Conductivity, Gnawing Curse, Buddy Pulse).
    receiver = getattr(ctx, "energy_receiver", None)
    if receiver is not None and getattr(ctx, "attaching_player_id", None) == ctx.opponent_id:
        counters = re.search(
            r"put (\d+) damage counters? on that pokémon", text
        )
        if counters:
            await ctx.deal_damage(
                int(counters.group(1)) * 10, target=receiver,
                apply_modifiers=False, as_counters=True, is_attack=False,
            )
            return

    # Generic healing powers.
    heal_amount = re.search(r"heal (\d+) damage", text)
    if heal_amount:
        amount = int(heal_amount.group(1))
        if "from each of your pokémon" in text:
            for pokemon in ctx.my_pokemon_in_play():
                await ctx.heal(amount, pokemon)
            return
        if "from each of your benched" in text:
            candidates = list(ctx.my_bench())
            if "basic pokémon" in text:
                candidates = [p for p in candidates if is_basic_pokemon(p)]
            for pokemon in candidates:
                await ctx.heal(amount, pokemon)
            return
        if "from your active" in text:
            target = ctx.my_active()
            if target is not None:
                await ctx.heal(amount, target)
            return
        if "from this pokémon" in text:
            await ctx.heal(amount, ctx.source)
            return
        if "from 1 of your pokémon" in text:
            candidates = [p for p in ctx.my_pokemon_in_play() if _damaged(ctx, p)]
            for word, ptype in (
                ("grass", PokemonTypes.GRASS), ("fire", PokemonTypes.FIRE),
                ("water", PokemonTypes.WATER), ("lightning", PokemonTypes.LIGHTNING),
                ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
                ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
            ):
                if f"has any {word} energy" in text:
                    candidates = [p for p in candidates if any(
                        energy_provides_type(e, ptype.value)
                        for e in ctx.attached_energies(p)
                    )]
            target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") \
                if candidates else None
            if target is not None:
                await ctx.heal(amount, target)
            return

    if "recovers from all special conditions" in text:
        target = ctx.my_active() if "active pokémon" in text else ctx.source
        if target is not None:
            await ctx.cure_all_conditions(target)
        return

    # Draw powers, including the common Active bonus wording.
    if "each player draws a card" in text:
        await ctx.draw_cards(1)
        await ctx.draw_cards(1, player_id=ctx.opponent_id)
        return
    draw = re.search(r"(?:you may )?draw (\d+|a) cards?", text)
    if draw:
        count = 1 if draw.group(1) == "a" else int(draw.group(1))
        if "if this pokémon is in the active spot, draw 1 more" in text \
                and _is_active(ctx.source):
            count += 1
        await ctx.draw_cards(count)
        return

    # Self-damage acceleration (Roaring Resolve / Scar Charge) is one atomic
    # instruction: place the counters, search the printed Energy type, attach
    # every selected card, then shuffle.  The broad self-counter fallback
    # below used to return after only the first clause.
    self_charge = re.search(
        r"(?:put|place) (\d+) damage counters? on this pokémon\. if you do, "
        r"search your deck for up to (\d+) "
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
        r"energy cards? and attach them to this pokémon",
        text,
    )
    if self_charge:
        counters, count, type_word = self_charge.groups()
        await ctx.deal_damage(
            int(counters) * 10, target=ctx.source,
            apply_modifiers=False, as_counters=True, is_attack=False,
        )
        ptype = getattr(PokemonTypes, type_word.upper())
        picks = await ctx.search_deck(
            lambda card: is_energy_card(card)
            and energy_provides_type(card, ptype.value),
            int(count), minimum=0,
            prompt=f"Choose {type_word.title()} Energy",
        )
        for energy in picks:
            await ctx.attach_energy(energy, ctx.source)
        await ctx.shuffle_deck()
        return

    # Direct counters from activated/on-play Abilities.
    counters = re.search(
        r"(?:put|place) (\d+) damage counters? on (\d+|1) of your opponent's (benched )?pokémon",
        text,
    )
    if counters:
        count = int(counters.group(2))
        pool = ctx.opponent_bench() if counters.group(3) else ctx.opponent_pokemon_in_play()
        picks = await ctx.choose_cards(
            pool, min(count, len(pool)), minimum=min(count, len(pool)),
            prompt="Choose Pokémon to receive damage counters",
        ) if pool else []
        for target in picks:
            await ctx.deal_damage(
                int(counters.group(1)) * 10, target=target,
                apply_modifiers=False, as_counters=True, is_attack=False,
            )
        return
    counters = re.search(r"put (\d+) damage counters? on this pokémon", text)
    if counters:
        await ctx.deal_damage(
            int(counters.group(1)) * 10, target=ctx.source,
            apply_modifiers=False, as_counters=True, is_attack=False,
        )
        return

    # Switch/pull abilities.  The owner chooses the replacement when the text
    # says to switch the Active out; targeted Gust effects are chosen by the
    # acting player.
    if "switch out your opponent's active pokémon to the bench" in text:
        bench = ctx.opponent_bench()
        target = await ctx.choose_pokemon(
            bench, "Choose the new Active Pokémon", player_id=ctx.opponent_id
        ) if len(bench) > 1 else bench[0] if bench else None
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
        return
    if re.search(r"switch (?:in )?1 of your opponent's benched .*pokémon", text):
        bench = list(ctx.opponent_bench())
        if "basic pokémon" in text:
            bench = [p for p in bench if is_basic_pokemon(p)]
        target = await ctx.choose_pokemon(
            bench, "Choose your opponent's new Active Pokémon"
        ) if bench else None
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
            if "new active pokémon is now confused" in text:
                await ctx.apply_special_condition(
                    ctx.opponent_active(), SpecialConditions.CONFUSED)
        return

    # Move an Energy already in play.  ``move_energy_freely`` keeps special
    # Energy identity and unit value intact.
    move_any_to_self = re.search(
        r"move any (?:amount|number) of "
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
        r"energy (?:from your other pokémon|attached to your pokémon) to "
        r"(?:this pokémon|it)", text,
    )
    if move_any_to_self:
        ptype = getattr(PokemonTypes, move_any_to_self.group(1).upper())
        await ctx.move_energy_freely(
            [p for p in ctx.my_pokemon_in_play() if p is not ctx.source],
            [ctx.source],
            predicate=lambda energy: energy_provides_type(energy, ptype.value),
            max_count=None,
            prompt="Choose Energy to move",
        )
        return
    if "move an energy from 1 of your other pokémon to this pokémon" in text:
        sources = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
        await ctx.move_energy_freely(
            sources, [ctx.source], max_count=1,
            prompt="Choose an Energy to move",
        )
        return
    if "move any number of" in text and "energy" in text \
            and "other pokémon" in text:
        sources = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
        await ctx.move_energy_freely(
            sources, [ctx.source], max_count=None,
            prompt="Choose Energy to move",
        )
        return

    # Return an attached Tool to hand (Drive Change / Change Clothes).
    if "put a pokémon tool card attached" in text and "into your hand" in text:
        holders = [ctx.source] if "this pokémon" in text else ctx.my_pokemon_in_play()
        tools = [card for holder in holders for card in full_stack(holder)[1:]
                 if is_pokemon_tool(card)]
        chosen = await _choose_one(ctx, tools, "Choose a Pokémon Tool") \
            if tools else None
        if chosen is not None:
            await ctx.put_in_hand([chosen], reveal=False)
        return

    if "shuffle this pokémon and all cards attached to it into your deck" in text \
            or "shuffle it and all cards attached to it into your deck" in text:
        await ctx.shuffle_into_deck(full_stack(ctx.source))
        return
    if "discard all cards attached to this pokémon and return it to your hand" in text:
        evolution_cards, attachments = split_pokemon_stack(ctx.source)
        await ctx.discard_cards(attachments)
        await ctx.put_in_hand(evolution_cards, reveal=False)
        return

    # Top-of-deck Energy acceleration (Powerful Squall, Fully Blooming
    # Energy, Tri Howl and their many reprints).
    top = re.search(r"look at the top (\d+) cards of your deck", text)
    if top and "attach" in text and "energy" in text:
        viewed = ctx.deck_top(int(top.group(1)))
        candidates = [card for card in viewed if is_energy_card(card)]
        if "basic energy" in text:
            candidates = [card for card in candidates if is_basic_energy(card)]
        for word, ptype in (
            ("grass", PokemonTypes.GRASS), ("fire", PokemonTypes.FIRE),
            ("water", PokemonTypes.WATER), ("lightning", PokemonTypes.LIGHTNING),
            ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
            ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
        ):
            if f"{word} energy" in text:
                candidates = [card for card in candidates
                              if energy_provides_type(card, ptype.value)]
                break
        picks = await ctx.choose_cards(
            candidates, max(1, len(candidates)), minimum=0,
            prompt="Choose Energy cards to attach", display_cards=viewed,
        ) if viewed else []
        for energy in picks:
            targets = [ctx.source] if "to this pokémon" in text else ctx.my_pokemon_in_play()
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
        remaining = [card for card in viewed if card not in picks]
        if "discard the other cards" in text:
            await ctx.discard_cards(remaining)
        else:
            await ctx.shuffle_deck()
        return

    discarded_top = re.search(r"discard the top (?:(\d+) cards?|card) of your deck", text)
    if discarded_top and "attach a basic energy card from your discard pile " \
            "to this pokémon" in text:
        # Stormy Winds discards three cards as its cost, then chooses exactly
        # one Basic Energy from the entire discard pile.  It does not attach
        # every Energy among the cards just discarded.
        count = int(discarded_top.group(1) or 1)
        await ctx.discard_cards(ctx.deck_top(count))
        candidates = [
            card for card in ctx.discard_pile() if is_basic_energy(card)
        ]
        energy = await _choose_one(
            ctx, candidates, "Choose a basic Energy card"
        ) if candidates else None
        if energy is not None:
            await ctx.attach_energy(energy, ctx.source)
        return
    if discarded_top and "attach" in text and "energy" in text:
        count = int(discarded_top.group(1) or 1)
        viewed = ctx.deck_top(count)
        await ctx.discard_cards(viewed)
        candidates = [card for card in viewed if is_energy_card(card)]
        if "basic energy" in text:
            candidates = [card for card in candidates if is_basic_energy(card)]
        if "fire energy" in text:
            candidates = [card for card in candidates
                          if energy_provides_type(card, PokemonTypes.FIRE.value)]
        for energy in candidates:
            targets = [ctx.source] if "to this pokémon" in text \
                or "attach it to slugma" in text else ctx.my_pokemon_in_play()
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
                heal = re.search(r"heal (\d+) damage from that pokémon", text)
                if heal:
                    await ctx.heal(int(heal.group(1)), target)
        return

    # Typed Energy acceleration from hand/discard/deck.
    energy_clause = re.search(
        r"(?:(up to) (\d+)|(\d+)|(?:an?|1)) "
        r"(?:(basic|special) )?"
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy)? ?"
        r"energy(?: cards?)? from your (hand|discard pile)",
        text,
    )
    if energy_clause and "attach" in text:
        count = int(energy_clause.group(2) or energy_clause.group(3) or 1)
        qualifier, type_word, zone = (
            energy_clause.group(4), energy_clause.group(5), energy_clause.group(6)
        )
        pool = list(ctx.hand()) if zone == "hand" else list(ctx.discard_pile())
        candidates = [card for card in pool if is_energy_card(card)]
        if qualifier == "basic":
            candidates = [card for card in candidates if is_basic_energy(card)]
        elif qualifier == "special":
            candidates = [card for card in candidates if is_special_energy(card)]
        if type_word:
            ptype = getattr(PokemonTypes, type_word.upper(), None)
            candidates = [card for card in candidates if ptype is not None
                          and energy_provides_type(card, ptype.value)]
        maximum = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum,
            minimum=0 if energy_clause.group(1) or "you may" in text else maximum,
            prompt="Choose Energy cards",
        ) if maximum else []
        for energy in picks:
            targets = list(ctx.my_pokemon_in_play())
            if "to this pokémon" in text:
                targets = [ctx.source]
            elif "to your active pokémon" in text:
                targets = [ctx.my_active()] if ctx.my_active() is not None else []
            elif "benched" in text:
                targets = list(ctx.my_bench())
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
                heal = re.search(r"heal (\d+) damage from that pokémon", text)
                if heal:
                    await ctx.heal(int(heal.group(1)), target)
        return

    discard_search = re.search(
        r"(?:search your discard pile for|attach) (?:up to (\d+)|"
        r"(\d+)|an?|1) (.+?) energy cards? (?:from your discard pile )?"
        r"(?:and attach|to)",
        text,
    )
    if discard_search and "attach" in text:
        count = int(discard_search.group(1) or discard_search.group(2) or 1)
        descriptor = discard_search.group(3)
        candidates = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if "basic" in descriptor:
            candidates = [card for card in candidates if is_basic_energy(card)]
        allowed_types = []
        for word, ptype in (
            ("grass", PokemonTypes.GRASS), ("fire", PokemonTypes.FIRE),
            ("water", PokemonTypes.WATER), ("lightning", PokemonTypes.LIGHTNING),
            ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
            ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
        ):
            if word in descriptor:
                allowed_types.append(ptype)
        if allowed_types:
            candidates = [card for card in candidates if any(
                energy_provides_type(card, ptype.value) for ptype in allowed_types
            )]
        maximum = min(count, len(candidates))
        picks = await ctx.choose_cards(
            candidates, maximum, minimum=0,
            prompt="Choose Energy cards",
        ) if maximum else []
        for energy in picks:
            targets = [ctx.source] if "to this pokémon" in text else ctx.my_pokemon_in_play()
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
        return

    deck_energy = re.search(
        r"search your deck for (?:up to (\d+)|an?|1) "
        r"(?:(basic) )?"
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy)? ?"
        r"energy cards? and attach",
        text,
    )
    if deck_energy:
        count = int(deck_energy.group(1) or 1)
        basic_only, type_word = deck_energy.group(2), deck_energy.group(3)
        def predicate(card):
            if not is_energy_card(card) or (basic_only and not is_basic_energy(card)):
                return False
            ptype = getattr(PokemonTypes, type_word.upper(), None) if type_word else None
            return ptype is None or energy_provides_type(card, ptype.value)
        picks = await ctx.search_deck(
            predicate, count, minimum=0, prompt="Choose Energy cards"
        )
        for energy in picks:
            targets = [ctx.source] if "to this pokémon" in text else ctx.my_pokemon_in_play()
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target)
        await ctx.shuffle_deck()
        return

    # Straightforward opponent discard/condition families.
    if "discard an energy from your opponent's active pokémon" in text:
        active = ctx.opponent_active()
        if active is not None:
            await ctx.discard_energy_from(active, 1)
        return
    for word, condition in (
        ("asleep", SpecialConditions.ASLEEP),
        ("burned", SpecialConditions.BURNED),
        ("confused", SpecialConditions.CONFUSED),
        ("paralyzed", SpecialConditions.PARALYZED),
        ("poisoned", SpecialConditions.POISONED),
    ):
        if f"opponent's active pokémon is now {word}" in text:
            target = ctx.opponent_active()
            if target is not None:
                await ctx.apply_special_condition(target, condition)
            return
