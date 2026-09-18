"""Shared fallbacks for the current Standard-era card catalog.

The hand-written card modules remain authoritative.  The catalog importer uses
the helpers in this module only for cards which do not have a bespoke Python
implementation yet.  The rules-text interpreter deliberately works with real
board entities, so searches, attachments and moves use the same selectors and
animations as the rest of the simulator.
"""

from __future__ import annotations

import random
import re
from typing import Optional

from spirit.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonStage, PokemonTypes,
    SpecialConditions,
)
from spirit.game.card_effects.bw_era import (
    _ability_attached_energy_discard_cost,
    _ability_cost_handled_inline,
    _ability_hand_discard_cost,
    bw_legacy_ability,
    bw_legacy_attack,
    bw_legacy_passive,
)
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import (
    Ability, Activations, Attack, Triggers, def_for, evolves_from,
)
from spirit.game.session.passives import (
    Passive, TurnDamageModifier, effective_max_hp, effective_pokemon_types,
    effective_bench_capacity,
)
from spirit.game.session.effects import (
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


# Pokemon attacks and Abilities share the mature recurring-text interpreter
# built for the fully imported Black & White catalog.  The aliases give new
# modules era-neutral names and let us extend the implementation here later
# without rewriting generated cards.
standard_attack = bw_legacy_attack
standard_ability = bw_legacy_ability
standard_passive = bw_legacy_passive


class _DevolutionEvolutionLock(Passive):
    def blocks_evolution(self, player_id, target, carrier):
        return target is carrier


def standard_ability_source_zone(text: str) -> Optional[str]:
    """Only an explicit location of the bearer permits an out-of-play action.

    Drawing cards *in your hand* and using cards *in your discard pile* do
    not put the Ability's bearer there. Last-card entry powers are different.
    """
    text = _norm(text)
    if re.search(r"(?:if|while) this pokémon is in your discard pile", text):
        return "discard"
    if re.search(r"if this pokémon is (?:in your hand|the last card in your hand)", text):
        return "hand"
    return None


def normalize_standard_card_definition(definition) -> None:
    """Repair behavior classification on mechanically imported Pokémon.

    The source JSON calls every named Pokémon rule an Ability, but the engine
    must distinguish continuous passives, event triggers and clicked powers.
    Early bulk imports attached ``standard_ability`` to all three, leaving
    continuous effects inert (and occasionally exposing them from a discard
    pile merely because their text mentioned one).  Normalize only shared-
    interpreter abilities; bespoke scripts remain authoritative.
    """
    for ability in getattr(definition, "abilities", ()) or ():
        if isinstance(ability, Attack):
            if ability.effect is bw_legacy_attack:
                from spirit.game.card_effects.attack_requirements import install_attack_requirement
                install_attack_requirement(ability)
            continue
        shared_effect = ability.effect is bw_legacy_ability
        shared_passive = ability.effect is None and ability.passive is not None \
            and ability.passive.__class__.__name__ == "_BWTextPassive"
        if not shared_effect and not shared_passive:
            continue
        text = _norm(ability.game_text)
        # Imported printings must share the same per-player cap as authored
        # printings, not just a once-per-turn flag on each individual card.
        shared_limit = re.search(
            r"you (?:can't|cannot) use more than (?:1|one) (.+?) ability "
            r"(?:each|during your) turn", text,
        )
        if shared_limit and shared_limit.group(1) == _norm(ability.title):
            ability.shared_once_per_turn = ability.title
        continuous = any(phrase in text for phrase in (
            "damage counters instead of", "more damage counters on your opponent's poisoned",
            "more damage counter on your opponent's poisoned",
            "more damage counters on your opponent's burned",
            "more damage counter on your opponent's burned",
            "damage counters on your opponent's confused pokémon between turns",
            "if this pokémon remains asleep between turns",
            "if this pokémon is asleep, flip 2 coins instead of 1",
            "after you flip any coins for an attack",
        ))
        # An on-entry effect can establish stronger Poison for later Checkup.
        # That reminder does not turn Hazardous Evolution into a global aura.
        if continuous and standard_trigger(text) not in (Triggers.ON_PLAY, Triggers.ON_EVOLVE):
            ability.effect = None
            ability.trigger = None
            ability.activation = None
            ability.usable_from = None
            ability.passive = ability.passive or bw_legacy_passive(text)
            continue
        inferred_trigger = standard_trigger(text)
        inferred_activation = standard_activation(text)
        if (shared_passive and inferred_trigger == Triggers.ON_ENERGY_ATTACHED) \
                or ability.title.casefold() == "kinesis":
            # These are observers, not callbacks on the newly played card.
            # Energy Evolution / Energy Signal watch an already in-play
            # carrier, while Kinesis belongs to the Alakazam-EX that becomes
            # the lower evolution card.  Converting them to declared triggers
            # removes the carrier from active_passives before their event and
            # silently disables the printed effect.
            ability.effect = None
            ability.trigger = None
            ability.activation = None
            ability.usable_from = None
            ability.passive = ability.passive or bw_legacy_passive(text)
            continue
        if inferred_trigger is not None:
            # Every inferred event needs an executable callback.  Older code
            # only migrated the two discard triggers, leaving imported rules
            # authored as ``Ability(passive=standard_passive(...))`` with a
            # trigger marker but no effect to run (prize, end-turn and move
            # events were silently inert).
            ability.effect = bw_legacy_ability
            ability.passive = None
            ability.trigger = inferred_trigger
            ability.activation = None
            # ON_PLAY/ON_EVOLVE describe where the card came from, not an
            # out-of-play action the player may click repeatedly.
            ability.usable_from = standard_ability_source_zone(text)
        elif inferred_activation is not None:
            ability.effect = bw_legacy_ability
            ability.passive = None
            ability.activation = inferred_activation
            ability.trigger = None
            ability.usable_from = standard_ability_source_zone(text)
            if ability.condition is None:
                ability.condition = standard_ability_condition(text)
        else:
            ability.effect = None
            ability.trigger = None
            ability.activation = None
            ability.usable_from = None
            ability.passive = ability.passive or bw_legacy_passive(text)
            if "when you are setting up to play" in text \
                    and "as your active pokémon" in text:
                definition.setup_as_active = True
                definition.setup_as_bench = "or on your bench" in text
                definition.setup_second_player_only = "if you go second" in text


def steam_up_condition(board, player_id, pokemon=None) -> bool:
    """Steam Up is only offered while its Fire Energy cost can be paid."""
    hand = board.find_player_area(player_id, "hand")
    return any(
        is_energy_card(card)
        and energy_provides_type(card, PokemonTypes.FIRE.value)
        for card in (hand.children if hand is not None else [])
    )


async def steam_up(ctx):
    discarded = await ctx.discard_from_hand(
        1,
        predicate=lambda card: is_energy_card(card)
        and energy_provides_type(card, PokemonTypes.FIRE.value),
    )
    if not discarded:
        return
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        amount=30,
        player_id=ctx.player_id,
        source_predicate=lambda pokemon: (
            pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
            and PokemonTypes.FIRE.value
            in effective_pokemon_types(ctx.board, pokemon)
        ),
    ))


async def karen_effect(ctx):
    """Shuffle each player's discarded Pokemon into that player's deck."""
    for player_id in ctx.board.player_ids:
        discard = ctx.board.find_player_area(player_id, "discard")
        cards = [card for card in list(discard.children) if is_pokemon_card(card)]
        if cards:
            await ctx.shuffle_into_deck(cards, player_id=player_id)


def karen_condition(board, player_id, source=None) -> bool:
    return any(
        any(is_pokemon_card(card) for card in discard.children)
        for pid in board.player_ids
        if (discard := board.find_player_area(pid, "discard")) is not None
    )


async def hex_maniac_effect(ctx):
    state = ctx.session.turn_state
    state.abilities_disabled_through_turn = max(
        state.abilities_disabled_through_turn, state.turn_number + 1
    )


def _opponent_id(board, player_id):
    return next((pid for pid in board.player_ids if pid != player_id), None)


def _in_area(card, area_name: str) -> bool:
    parent = getattr(card, "parent", None)
    return parent is not None and parent.get_attribute(AttrID.NAME) == area_name


class _TemporaryDamageRule(Passive):
    """Side/target scoped damage rule created by a Trainer card."""

    def __init__(self, owner_id: str, amount: int = 0, *, prevent=False,
                 target_id=None, target_predicate=None, attacker_predicate=None):
        self.owner_id = owner_id
        self.amount = amount
        self.prevent = prevent
        self.target_id = target_id
        self.target_predicate = target_predicate
        self.attacker_predicate = attacker_predicate

    def _matches(self, calc):
        return (
            calc.is_attack
            and calc.target.owning_player_id == self.owner_id
            and (self.target_id is None or calc.target.entity_id == self.target_id)
            and (self.target_predicate is None or self.target_predicate(calc.target))
            and (self.attacker_predicate is None
                 or self.attacker_predicate(calc.attacker))
        )

    def modify_damage_taken(self, calc, carrier):
        if self.amount and self._matches(calc):
            calc.amount = max(0, calc.amount - self.amount)

    def prevents_damage(self, calc, carrier):
        return self.prevent and self._matches(calc)


class _TemporaryRetreatRule(Passive):
    def __init__(self, player_id: str, predicate):
        self.player_id = player_id
        self.predicate = predicate

    def blocks_retreat(self, pokemon, carrier):
        return pokemon.owning_player_id == self.player_id and self.predicate(pokemon)


class _TemporaryAttackRule(Passive):
    """Side-wide attack prohibition which also covers later entrants."""

    def __init__(self, player_id: str):
        self.player_id = player_id

    def blocks_attacks(self, pokemon, carrier):
        return pokemon.owning_player_id == self.player_id


def _basic_energy_types(card) -> set[int]:
    return {
        pokemon_type.value for pokemon_type in PokemonTypes
        if pokemon_type not in (PokemonTypes.UNSET, PokemonTypes.COLORLESS)
        and energy_provides_type(card, pokemon_type.value)
    } if is_basic_energy(card) else set()


def ability_position_allowed(board, player_id, source, game_text: str) -> bool:
    """Check position prerequisites both in the menu and at resolution time."""
    clause = _norm(game_text).split("you may", 1)[0]
    definition = def_for(getattr(source, "archetype_id", None)) if source is not None else None
    name = (getattr(definition, "display_name", "") or "").casefold()
    if name:
        clause = clause.replace(name, "this pokémon")
    if re.search(r"(?:if|while|as long as) this pokémon is (?:your active pokémon|in the active spot)", clause):
        if board is None or source is None or board.active_pokemon(player_id) is not source:
            return False
    if "if this pokémon is on your bench" in clause:
        if board is None:
            return False
        bench = board.find_player_area(player_id, "bench")
        if source is None or bench is None or source not in bench.children:
            return False
    return True


def standard_ability_condition(game_text: str):
    """Public-information legality gate for a shared activated Ability."""
    text = _norm(game_text)

    def condition(board, player_id, source=None):
        state = getattr(board, "turn_state", None)
        opponent_id = _opponent_id(board, player_id)
        hand_area = board.find_player_area(player_id, "hand")
        discard_area = board.find_player_area(player_id, "discard")
        deck_area = board.find_player_area(player_id, "deck")
        hand = list(hand_area.children) if hand_area is not None else []
        discard = list(discard_area.children) if discard_area is not None else []
        own = list(board.pokemon_in_play(player_id))
        opposing = list(board.pokemon_in_play(opponent_id)) if opponent_id else []

        def card_name(card):
            definition = def_for(getattr(card, "archetype_id", None))
            return (getattr(definition, "display_name", "") or "").casefold()

        def has_bench_space(pid):
            bench = board.find_player_area(pid, "bench")
            from spirit.game.session.passives import effective_bench_capacity
            return bench is not None and len(bench.children) < \
                effective_bench_capacity(board, pid)

        # Legacy Poké-Powers print their own status restriction; modern
        # Abilities (and powers without this sentence) must remain usable.
        if re.search(r"this power (?:can't|cannot) be used if .+ is affected by a special condition", text) \
                and source is not None and source.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return False

        # Position clauses placed before the optional action are real
        # activation requirements.  Do not confuse them with a later bonus
        # clause such as Tasting (which may draw from the Bench and draws one
        # extra only while Active).
        activation_clause = text.split("you may", 1)[0]
        source_name = card_name(source) if source is not None else ""
        if source_name:
            activation_clause = activation_clause.replace(source_name, "this pokémon")
        if not ability_position_allowed(board, player_id, source, text):
            return False
        from spirit.game.card_effects.lost_zone import hand_energy_payment, payment_candidates
        lost_payment = hand_energy_payment(text)
        if lost_payment and (len(payment_candidates(hand, lost_payment)) < int(lost_payment[1])
                             or board.active_pokemon(opponent_id) is None):
            return False
        if "you win this game" in text and not alternate_win_condition_met(
                board, player_id, text):
            return False
        # A discard payment alone is not a benefit.  Draw-only powers such
        # as Trade/Power Draw need at least one card left to draw.  Do not
        # apply this to shuffle-and-draw or effects with another benefit.
        draw_only = re.search(r"\bdraw (?:\d+|a) cards?\.", text) and not any(
            word in text for word in (
                "shuffle", "attach", "damage", "heal", "search", "switch",
                "play it", "put it", "onto your bench",
            )
        )
        if draw_only and (deck_area is None or not deck_area.children):
            return False
        from spirit.game.card_effects.hgss_era import hgss_power_condition
        hgss_legal = hgss_power_condition(board, player_id, source, text)
        if hgss_legal is not None:
            return hgss_legal
        became_active_this_turn = any(phrase in activation_clause for phrase in (
            "if this pokémon was on the bench and became your active pokémon this turn",
            "when this pokémon moves from your bench to become your active pokémon",
        ))
        if became_active_this_turn:
            if source is None or board.active_pokemon(player_id) is not source \
                    or state is None \
                    or state.became_active_turn.get(source.entity_id) != state.turn_number:
                return False

        # First-turn powers are a special activation window rather than an
        # ordinary once-per-turn Ability.  Turns 1 and 2 are respectively the
        # first turns of the player going first and the player going second.
        if "once during your first turn" in text:
            if state is None or state.active_player_id != player_id \
                    or state.turn_number not in (1, 2):
                return False
        if "only if you go second" in text \
                and (state is None or state.turn_number != 2):
            return False
        if "if this pokémon is in the active spot" in text:
            # Total Freedom-style Abilities explicitly offer two alternative
            # locations: Bench -> Active *or* Active -> Bench.  Treating the
            # second clause as a global Active-only prerequisite hid the
            # Ability whenever the card was on the Bench.
            dual_position_switch = (
                "if this pokémon is on the bench" in text
                and "switch it with your active pokémon" in text
                and "or, if this pokémon is in the active spot" in text
            )
            if dual_position_switch:
                active = board.active_pokemon(player_id)
                bench = board.find_player_area(player_id, "bench")
                source_on_bench = bench is not None and source in bench.children
                source_is_active = active is source
                if not (
                    source_on_bench and active is not None
                    or source_is_active and bench is not None and bench.children
                ):
                    return False
            elif source is None or board.active_pokemon(player_id) is not source:
                return False

        if "search your deck" in text and (deck_area is None or not deck_area.children):
            return False

        # Excited Heal requires a modern Mega Evolution ex in play, not a
        # legacy Mega EX or just any Grass Pokemon. Check live types as well.
        mega_requirement = re.search(
            r"if you have any (grass|fire|water|lightning|psychic|fighting|"
            r"darkness|metal|fairy|dragon|colorless) mega evolution pokémon ex in play",
            activation_clause,
        )
        if mega_requirement:
            wanted = getattr(PokemonTypes, mega_requirement.group(1).upper())
            if not any(
                "SV_Mega" in (getattr(def_for(p.archetype_id), "subtypes", ()) or ())
                and wanted.value in effective_pokemon_types(board, p)
                for p in own
            ):
                return False

        draw_until = re.search(r"draw cards until you have (\d+) cards", text)
        if draw_until:
            cost = _ability_hand_discard_cost(text)
            paid = (len(hand) if cost[0] is None else cost[0]) if cost else 0
            if "put a card from your hand on the bottom of your deck" in text:
                if not hand:
                    return False
                paid += 1
            if len(hand) - paid >= int(draw_until.group(1)) or deck_area is None or not deck_area.children:
                return False
        if "draw a card" in text and "discard" not in text and (deck_area is None or not deck_area.children):
            return False

        # Afterburner's older word order puts the zone before the Energy.
        discard_attach = re.search(
            r"search your discard pile for (?:an?|1) (\w+) energy card and attach", text)
        if discard_attach:
            ptype = getattr(PokemonTypes, discard_attach.group(1).upper(), None)
            if not any(is_energy_card(card) and (ptype is None or
                       energy_provides_type(card, ptype.value)) for card in discard):
                return False

        if ("attach this card" in text or "attach it" in text) \
                and "as a special energy card" in text:
            targets = [pokemon for pokemon in own if pokemon is not source]
            if "vikavolt" in text:
                targets = [pokemon for pokemon in targets
                           if "vikavolt" in card_name(pokemon)]
            elif "lightning pokémon" in text:
                targets = [pokemon for pokemon in targets
                           if PokemonTypes.LIGHTNING.value in
                           effective_pokemon_types(board, pokemon)]
            if not targets:
                return False

        named_energy = re.search(
            r"attach an? ([a-z0-9' -]+ energy) card from your hand", text)
        elemental_names = {
            f"{word} energy" for word in (
                "grass", "fire", "water", "lightning", "psychic",
                "fighting", "darkness", "metal", "fairy", "special",
            )
        }
        if named_energy and "basic " not in named_energy.group(1) \
                and named_energy.group(1).strip() not in elemental_names:
            wanted = named_energy.group(1).strip().casefold()
            if not any(card_name(card) == wanted for card in hand):
                return False

        if "basic pokémon with 70 hp or less from your discard pile onto your bench" in text:
            if not has_bench_space(player_id) or not any(
                    is_basic_pokemon(card)
                    and int(card.get_attribute(AttrID.HP) or 0) <= 70
                    for card in discard):
                return False

        if "put a shedinja from your discard pile onto your bench" in text:
            if not has_bench_space(player_id) or not any(
                    card_name(card) == "shedinja" for card in discard):
                return False

        if "put a basic pokémon from your opponent's discard pile onto their bench" in text:
            opposing_discard_area = board.find_player_area(opponent_id, "discard") \
                if opponent_id else None
            opposing_discard = list(opposing_discard_area.children) \
                if opposing_discard_area is not None else []
            if not opponent_id or not has_bench_space(opponent_id) or not any(
                    is_basic_pokemon(card) for card in opposing_discard):
                return False

        if "discard the bottom card of your deck" in text \
                and (deck_area is None or not deck_area.children):
            return False

        if "return all energy attached to 1 of your pokémon to your hand" in text \
                and not any(board.attached_energies(pokemon) for pokemon in own):
            return False

        if "attach it to 1 of your pokémon as a pokémon tool card" in text \
                and not any(pokemon is not source for pokemon in own):
            return False

        if "search your deck for a palafin ex" in text and not any(
                card_name(card) == "palafin ex" for card in
                (deck_area.children if deck_area is not None else [])):
            return False

        if "in your hand that evolves from" in text \
                or "card in your hand that evolves from this pokémon" in text \
                or "stage 2 card in your hand that evolves from" in text:
            targets = [source]
            if "choose 1 of your basic pokémon" in text:
                targets = [pokemon for pokemon in own if is_basic_pokemon(pokemon)]
            legal = False
            for target in targets:
                if target is None:
                    continue
                logic = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                named_base = re.search(
                    r"in your hand that evolves from ([a-z0-9 .'-]+?)"
                    r"(?:,| you may|\.)", text,
                )
                if named_base and named_base.group(1) not in (
                        "this pokémon", "that pokémon"):
                    wanted = named_base.group(1).strip().casefold()
                    base = next((
                        pokemon for pokemon in own
                        if card_name(pokemon) == wanted
                    ), None)
                    if base is not None:
                        logic = base.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                    else:
                        # The named Basic need not itself be in play (Eevee-GX
                        # and Ascension DNA).  Its canonical logic name is the
                        # printed name for all imported evolution lines.
                        logic = named_base.group(1).strip().title()
                for card in hand:
                    if not is_evolution_pokemon(card) or not evolves_from(
                            card.archetype_id, logic):
                        continue
                    if "stage 2 card" in text and card.get_attribute(
                            AttrID.STAGE) != PokemonStage.STAGE2.value:
                        continue
                    legal = True
                    break
            if not legal:
                return False
        if "discard 1 card from your hand" in text and not hand:
            return False

        # Public costs must make an activated Ability unavailable before it
        # is clicked.  This mirrors the shared payment path and prevents a
        # benefit from resolving when its required discard cannot be made.
        if not _ability_cost_handled_inline(text):
            hand_cost = _ability_hand_discard_cost(text)
            if hand_cost is not None and hand_cost[0] is not None:
                count, predicate = hand_cost
                if sum(1 for card in hand if predicate(card)) < count:
                    return False
            attached_cost = _ability_attached_energy_discard_cost(text)
            if attached_cost is not None:
                count, predicate = attached_cost
                attached = board.attached_energies(source) if source is not None else []
                if sum(1 for energy in attached if predicate(energy)) < count:
                    return False
        if "pokémon tool card attached" in text and "into your hand" in text:
            if not any(is_pokemon_tool(card) for pokemon in own
                       for card in full_stack(pokemon)[1:]):
                return False
        if re.search(r"\bmove\b", text) and "energy" in text and "pokémon" in text:
            if not any(board.attached_energies(pokemon) for pokemon in own):
                return False
            if len(own) < 2:
                return False
        if "switch" in text and "opponent" in text:
            bench = board.find_player_area(opponent_id, "bench") if opponent_id else None
            if bench is None or not bench.children:
                return False
        if re.search(r"discard an energy (?:from|attached to) your opponent's active", text):
            active = board.active_pokemon(opponent_id) if opponent_id else None
            if active is None or not board.attached_energies(active):
                return False
        if "heal" in text:
            candidates = own
            if "active" in text:
                active = board.active_pokemon(player_id)
                candidates = [active] if active is not None else []
            if not any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
                       for p in candidates):
                return False

        counter_target = re.search(
            r"(?:put|place) \d+ damage counters? on 1 of your opponent's (benched )?pokémon(-ex|-gx)?",
            text)
        if counter_target:
            targets = list(board.pokemon_in_play(opponent_id)) if opponent_id else []
            if counter_target.group(1):
                targets = [p for p in targets if _in_area(p, "bench")]
            if counter_target.group(2):
                subtype = counter_target.group(2)[1:].upper()
                targets = [p for p in targets if subtype in
                           (getattr(def_for(p.archetype_id), "subtypes", ()) or ())]
            if not targets:
                return False

        if re.search(r"remove (?:all|\d+) damage counters? from", text):
            targets = [board.active_pokemon(player_id)] if "from your active pokémon" in text else own
            if not any(p is not None and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
                       for p in targets):
                return False

        energy_clause = re.search(
            r"energy(?: cards?)? from your (hand|discard pile)", text
        )
        if energy_clause and "attach" in text:
            zone = hand if energy_clause.group(1) == "hand" else discard
            candidates = [card for card in zone if is_energy_card(card)]
            if "basic energy" in text:
                candidates = [card for card in candidates if is_basic_energy(card)]
            if "special energy" in text:
                candidates = [card for card in candidates if is_special_energy(card)]
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
            if not candidates:
                return False
            if "to 1 of your benched pokémon" in text:
                bench = board.find_player_area(player_id, "bench")
                if bench is None or not bench.children:
                    return False
            if "excluding pokémon-ex" in text:
                legal_targets = [pokemon for pokemon in own
                                 if pokemon is not source
                                 and "EX" not in (
                                     getattr(def_for(pokemon.archetype_id),
                                             "subtypes", ()) or ())]
                if not legal_targets:
                    return False
        return True

    condition.__name__ = "standard_ability_text_condition"
    return condition


def alternate_win_condition_met(board, player_id, game_text: str) -> bool:
    """Unown's public thresholds are costs to activate, not just effect checks."""
    text = _norm(game_text)
    if "35 or more cards in your hand" in text:
        hand = board.find_player_area(player_id, "hand")
        return hand is not None and len(hand.children) >= 35
    if "66 or more damage counters" in text:
        bench = board.find_player_area(player_id, "bench")
        return bench is not None and sum(
            max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
            for pokemon in bench.children
        ) >= 66
    if "12 or more supporter cards in the lost zone" in text:
        opponent = _opponent_id(board, player_id)
        lost = board.find_player_area(opponent, "lostZone") if opponent else None
        return lost is not None and sum(is_supporter_card(card) for card in lost.children) >= 12
    return False


def royal_flash_condition(board, player_id, source=None) -> bool:
    opponent_id = _opponent_id(board, player_id)
    active = board.active_pokemon(opponent_id) if opponent_id else None
    bench = board.find_player_area(opponent_id, "bench") if opponent_id else None
    return bool(active and bench and bench.children and board.attached_energies(active))


async def royal_flash(ctx):
    if not (await ctx.flip_coins(1, "Royal Flash"))[0]:
        return
    active = ctx.opponent_active()
    energies = ctx.attached_energies(active) if active is not None else []
    energy = await _choose_one(ctx, energies, "Choose an Energy to move")
    if energy is None or not ctx.opponent_bench():
        return
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose your opponent's Benched Pokémon"
    )
    if target is not None:
        await ctx.move_energy(energy, target)


async def goodnight_babies(ctx):
    for active in (ctx.my_active(), ctx.opponent_active()):
        if active is not None:
            await ctx.apply_special_condition(active, SpecialConditions.ASLEEP)


def purifying_fire_condition(board, player_id, source=None) -> bool:
    return bool(
        source is not None
        and source.get_attribute(AttrID.HP, 0) < effective_max_hp(board, source)
        and any(
            is_basic_energy(energy)
            and energy_provides_type(energy, PokemonTypes.FIRE.value)
            for energy in board.attached_energies(source)
        )
    )


async def purifying_fire(ctx):
    await ctx.heal(50, ctx.source)


def giant_water_shuriken_condition(board, player_id, source=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(
        source is not None and _in_area(source, "activePokemonArea")
        and any(
            is_energy_card(card)
            and energy_provides_type(card, PokemonTypes.WATER.value)
            for card in (hand.children if hand is not None else [])
        )
    )


async def giant_water_shuriken(ctx):
    discarded = await ctx.discard_from_hand(
        1,
        predicate=lambda card: is_energy_card(card)
        and energy_provides_type(card, PokemonTypes.WATER.value),
    )
    if discarded:
        target = await ctx.choose_pokemon(
            ctx.opponent_pokemon_in_play(), "Choose a Pokémon for 6 damage counters")
        if target is not None:
            await ctx.deal_damage(60, target=target, as_counters=True,
                                  apply_modifiers=False, is_attack=False)


def hyper_transfer_condition(board, player_id, source=None) -> bool:
    pokemon = list(board.pokemon_in_play(player_id))
    return len(pokemon) > 1 and any(
        is_basic_energy(energy)
        for holder in pokemon for energy in board.attached_energies(holder)
    )


async def hyper_transfer(ctx):
    pokemon = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(
        pokemon, pokemon, predicate=is_basic_energy, max_count=1,
        prompt="Choose a basic Energy to move",
    )


def stand_in_condition(board, player_id, source=None) -> bool:
    return bool(
        source is not None and _in_area(source, "bench")
        and board.active_pokemon(player_id) is not None
    )


async def stand_in(ctx):
    await ctx.switch_active(ctx.player_id, ctx.source)


def energy_color_condition(board, player_id, source=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children and board.pokemon_in_play(player_id))


async def energy_color(ctx):
    if not (await ctx.flip_coins(1, "Energy Color"))[0]:
        return
    picks = await ctx.search_deck(
        is_basic_energy, 1, minimum=0, prompt="Choose a basic Energy"
    )
    if picks:
        targets = ctx.my_pokemon_in_play()
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Choose a Pokémon"
        )
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


def second_coat_condition(board, player_id, source=None) -> bool:
    active = board.active_pokemon(player_id)
    discard = board.find_player_area(player_id, "discard")
    if active is None or discard is None:
        return False
    attached = [energy for energy in board.attached_energies(active)
                if is_basic_energy(energy)]
    discarded = [energy for energy in discard.children if is_basic_energy(energy)]
    return any(
        _basic_energy_types(old).isdisjoint(_basic_energy_types(new))
        for old in attached for new in discarded
    )


async def second_coat(ctx):
    active = ctx.my_active()
    attached = [energy for energy in ctx.attached_energies(active)
                if is_basic_energy(energy)] if active is not None else []
    old = await _choose_one(ctx, attached, "Choose the Energy to replace")
    if old is None:
        return
    old_types = _basic_energy_types(old)
    candidates = [
        energy for energy in ctx.discard_pile()
        if is_basic_energy(energy)
        and old_types.isdisjoint(_basic_energy_types(energy))
    ]
    new = await _choose_one(ctx, candidates, "Choose a different basic Energy")
    if new is None:
        return
    await ctx.discard_cards([old])
    await ctx.attach_energy(new, active, counts_as_attachment=False)


def abyssal_hand_condition(board, player_id, source=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) < 5


async def abyssal_hand(ctx):
    await ctx.draw_until(5)


def _norm(text: str) -> str:
    normalized = re.sub(
        r"\[\s*\[\s*([a-z]+)\s*\]\s*\]", r"\1",
        (text or "")
        .replace("Pok�mon", "Pokémon")
        .replace("’", "'")
        .lower(),
    )
    return " ".join(normalized.split())


def _card_name(card) -> str:
    from spirit.game.data_utils import def_for

    definition = def_for(getattr(card, "archetype_id", None))
    return (getattr(definition, "display_name", "") or "").strip()


def _card_subtypes(card) -> set[str]:
    definition = def_for(getattr(card, "archetype_id", None))
    return {str(value).casefold() for value in
            (getattr(definition, "subtypes", []) or [])}


def _opponent_switch_targets_on_board(board, player_id: str, text: str):
    """Return the public Benched targets named by a Trainer's switch text.

    Catcher effects are not deck searches: whether a legal target exists is
    public information and must gate the card before any printed cost is paid.
    Keep the target filtering shared by legality and resolution so cards such
    as Great Catcher cannot light up for, or select, an ordinary Pokémon.
    """
    opponent_id = _opponent_id(board, player_id)
    bench = board.find_player_area(opponent_id, "bench") \
        if opponent_id is not None else None
    targets = list(bench.children) if bench is not None else []

    if re.search(r"pok.mon-gx or pok.mon-ex", text):
        targets = [pokemon for pokemon in targets
                   if _card_subtypes(pokemon).intersection({"gx", "ex"})]
    elif re.search(r"benched pok.mon-gx", text):
        targets = [pokemon for pokemon in targets
                   if "gx" in _card_subtypes(pokemon)]
    elif re.search(r"benched pok.mon-ex", text):
        targets = [pokemon for pokemon in targets
                   if "ex" in _card_subtypes(pokemon)]
    elif re.search(r"benched pok.mon v(?:\s|\.|,|$)", text):
        targets = [pokemon for pokemon in targets
                   if "v" in _card_subtypes(pokemon)]
    elif "benched mega evolution pokémon" in text:
        targets = [pokemon for pokemon in targets
                   if _card_subtypes(pokemon).intersection({"mega", "sv_mega"})]
    elif "benched basic pokémon" in text:
        targets = [pokemon for pokemon in targets if is_basic_pokemon(pokemon)]
    elif "benched evolution pokémon" in text:
        targets = [pokemon for pokemon in targets
                   if is_evolution_pokemon(pokemon)]

    remaining_hp = re.search(
        r"benched pok.mon that has (\d+) hp or less remaining", text,
    )
    if remaining_hp:
        maximum = int(remaining_hp.group(1))
        targets = [pokemon for pokemon in targets
                   if int(pokemon.get_attribute(AttrID.HP, 0) or 0) <= maximum]
    return targets


def _definition_has_type(archetype_id: Optional[str], pokemon_type: PokemonTypes) -> bool:
    """Read a historical KO ledger's card type without a live entity."""
    definition = def_for(archetype_id)
    spec = getattr(definition, "extra_attributes", {}).get(
        str(AttrID.POKEMON_TYPES.value), {}
    )
    values = spec.get("value", []) if isinstance(spec, dict) else []
    if isinstance(values, str):
        import json
        try:
            values = json.loads(values)
        except (TypeError, ValueError):
            values = []
    return pokemon_type.value in (values or [])


def _pokemon_has_type(board, pokemon, pokemon_type: PokemonTypes) -> bool:
    return pokemon_type.value in effective_pokemon_types(board, pokemon)


def _trainer_energy_targets_on_board(board, player_id: str, text: str):
    """Attachment destinations described by a generated Trainer's text."""
    bench_area = board.find_player_area(player_id, "bench")
    targets = list(bench_area.children) if "benched" in text \
        else list(board.pokemon_in_play(player_id))
    if "active" in text and "benched" not in text:
        active = board.active_pokemon(player_id)
        targets = [active] if active is not None else []
    if "future pokémon" in text:
        targets = [p for p in targets if "future" in _card_subtypes(p)]
    if "team aqua pokémon" in text:
        targets = [p for p in targets if "team aqua" in _card_subtypes(p)
                   or _card_name(p).casefold().startswith("team aqua's ")]
    if "team magma pokémon" in text:
        targets = [p for p in targets if "team magma" in _card_subtypes(p)
                   or _card_name(p).casefold().startswith("team magma's ")]
    if "stage 2" in text:
        targets = [p for p in targets
                   if p.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value]
    if "mega evolution pokémon" in text:
        # Mega Turbo and equivalent cards name a card class, not merely any
        # Pokémon in play.  This belongs in the shared target resolver because
        # the generic public-zone attachment branch runs before the older
        # card-specific fallback below it.
        targets = [p for p in targets if _card_subtypes(p).intersection({
            "mega", "sv_mega",
        })]
    matching_types = []
    for word, pokemon_type in (
        ("grass", PokemonTypes.GRASS), ("fire", PokemonTypes.FIRE),
        ("water", PokemonTypes.WATER), ("lightning", PokemonTypes.LIGHTNING),
        ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
        ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
        ("fairy", PokemonTypes.FAIRY), ("dragon", PokemonTypes.DRAGON),
    ):
        if re.search(rf"(?:benched |stage 2 )?{word}(?:,|,? or| pokémon)", text):
            matching_types.append(pokemon_type)
    if matching_types:
        targets = [p for p in targets if any(
            _pokemon_has_type(board, p, pokemon_type)
            for pokemon_type in matching_types
        )]
    named = re.search(
        r"to 1 of your ([a-z0-9-gxex, or' -]+?)(?:\.| pokémon)", text
    )
    if named and any(sep in named.group(1) for sep in (",", " or ")):
        names = {part.strip().casefold() for part in
                 re.split(r",\s*|\s+or\s+", named.group(1)) if part.strip()}
        targets = [p for p in targets if _card_name(p).casefold() in names]
    return targets


def _trainer_energy_targets(ctx, text: str):
    return _trainer_energy_targets_on_board(ctx.board, ctx.player_id, text)


def _mandatory_hand_discard_cost(text: str):
    """Return the public hand-discard cost that precedes a Trainer's effect.

    Imported cards often express this as part of a single paragraph (rather
    than in a bespoke script).  Only clauses before the first result action
    are costs; optional ``may``/``up to`` discards and post-draw discards are
    deliberately excluded.
    """
    first_result = min(
        (index for marker in (
            "search your deck", "look at the top", "look at the bottom",
            "draw ", "attach ", "put a card from", "shuffle your hand",
        ) if (index := text.find(marker)) >= 0),
        default=len(text),
    )
    for match in re.finditer(
        r"discard (a|an|another|\d+) (.+?) from your hand", text,
    ):
        if match.start() > first_result:
            continue
        prefix = text[max(0, match.start() - 24):match.start()]
        phrase = match.group(0)
        if "may " in prefix or "up to" in phrase:
            continue
        raw_count = match.group(1)
        descriptor = re.sub(
            r"\s+cards?$", "", match.group(2).strip()
        ).removeprefix("other ")
        return (1 if raw_count in {"a", "an", "another"} else int(raw_count),
                descriptor)
    return None


def _hand_discard_predicate(board, descriptor: str):
    """Translate a printed discard-cost noun into a hand-card predicate."""
    descriptor = (descriptor or "").casefold()
    if "basic energy" in descriptor:
        return is_basic_energy
    if "special energy" in descriptor:
        return is_special_energy
    typed_energy = re.search(
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
        r"energy", descriptor,
    )
    if typed_energy:
        ptype = getattr(PokemonTypes, typed_energy.group(1).upper())
        return lambda card: is_energy_card(card) and energy_provides_type(
            card, ptype.value
        )
    if "energy" in descriptor:
        return is_energy_card
    typed_pokemon = re.search(
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|"
        r"dragon|colorless) pokémon", descriptor,
    )
    if typed_pokemon:
        ptype = getattr(PokemonTypes, typed_pokemon.group(1).upper())
        return lambda card: is_pokemon_card(card) and _pokemon_has_type(
            board, card, ptype
        )
    if "pokémon" in descriptor:
        return is_pokemon_card
    return None


def _type_predicate(word: str):
    word = (word or "").strip().lower()
    if word == "basic":
        return is_basic_energy
    pokemon_type = getattr(PokemonTypes, word.upper(), None)
    if pokemon_type is None:
        return is_energy_card
    return lambda card: is_energy_card(card) and energy_provides_type(
        card, pokemon_type.value
    )


def _search_predicate(text: str):
    """Best recurring deck-search predicate from English printed text."""
    recovery = re.search(r"(?:put|shuffle) ((?:up to )?(?:\d+|an?) .+?) from your discard pile", text)
    if recovery:
        # A recovery restriction starts at the instruction, not its earlier
        # cost (e.g. Molayne discards Metal but recovers a Trainer).
        text = recovery.group(1)
    from spirit.game.card_effects.search_descriptors import specific_search_predicate
    specific = specific_search_predicate(text)
    if specific is not None:
        return specific
    # A typed discard cost is not a restriction on the subsequent search
    # (Crasher Wake / Adaman). Recovery descriptors have no such prefix.
    if "search your deck for " in text:
        text = text.split("search your deck for ", 1)[1].split(".", 1)[0]
    if "tag team cards" in text:
        # TAG TEAM includes Supporters, not only Pokemon-GX.
        return lambda card: "tag team" in _card_subtypes(card)
    # Test compound/typed phrases before their broad components.  In
    # particular, Electric Generator says both "Basic Lightning Energy" and
    # "Lightning Pokémon"; the old broad "basic energy" branch therefore
    # accepted every Basic Energy type.
    if (
        "pokémon or energy" in text
        or "pokemon or energy" in text
        or "energy or pokémon" in text
        or "energy or pokemon" in text
    ):
        return lambda card: is_pokemon_card(card) or is_energy_card(card)
    typed_energy = re.search(
        r"(?:(basic) )?"
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) "
        r"energy",
        text,
    )
    if typed_energy:
        provides_type = _type_predicate(typed_energy.group(2))
        if typed_energy.group(1):
            return lambda card: is_basic_energy(card) and provides_type(card)
        return provides_type
    if "basic energy" in text:
        return is_basic_energy
    if "special energy" in text:
        return is_special_energy
    if "energy card" in text or "energy cards" in text:
        return is_energy_card
    if "pokémon tool" in text:
        return is_pokemon_tool
    if "helix fossil omanyte, dome fossil kabuto, or old amber aerodactyl" in text:
        return lambda card: _card_name(card).casefold() in {
            'helix fossil omanyte', 'dome fossil kabuto', 'old amber aerodactyl'}
    if "supporter" in text:
        return is_supporter_card
    if "item card" in text:
        return is_item_card
    if "trainer card" in text:
        return is_trainer_card
    if "basic pokémon" in text:
        hp_match = re.search(r"with (\d+) hp or less", text)
        if hp_match:
            maximum = int(hp_match.group(1))
            return lambda card: is_basic_pokemon(card) and int(
                card.get_attribute(AttrID.HP, 0) or 0
            ) <= maximum
        return is_basic_pokemon
    if "evolution pokémon" in text:
        return is_evolution_pokemon
    typed_pokemon = re.search(
        r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|"
        r"dragon|colorless) pokémon",
        text,
    )
    if typed_pokemon:
        pokemon_type = getattr(PokemonTypes, typed_pokemon.group(1).upper(), None)
        if pokemon_type is not None:
            return lambda card: is_pokemon_card(card) and pokemon_type.value in (
                card.get_attribute(AttrID.POKEMON_TYPES) or []
            )
    if "pokémon" in text:
        return is_pokemon_card
    return None


def _requested_count(text: str, default: int = 1) -> int:
    for pattern in (
        r"search your deck for (?:(?:up to|any) )?(\d+)",
        r"choose (?:up to )?(\d+)",
        r"put (?:up to )?(\d+)",
    ):
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))
    return default


async def _choose_one(ctx, cards, prompt: str, *, optional: bool = False,
                      player_id: Optional[str] = None):
    cards = list(cards)
    if not cards:
        return None
    picks = await ctx.choose_cards(
        cards, 1, minimum=0 if optional else None,
        prompt=prompt, player_id=player_id,
    )
    return picks[0] if picks else None


async def _generic_search(ctx, text: str, *, count_override: int | None = None) -> bool:
    """Resolve the common search families.  Returns whether it handled one."""
    if "search your deck" not in text:
        return False

    count = _requested_count(text) if count_override is None else count_override
    # Friend Ball uses types visible on the opposing field, not every Pokemon.
    if "with the same type as 1 of your opponent's pokémon in play" in text:
        types = {kind for pokemon in ctx.opponent_pokemon_in_play()
                 for kind in effective_pokemon_types(ctx.board, pokemon)}
        predicate = lambda card: is_pokemon_card(card) and bool(
            types.intersection(card.get_attribute(AttrID.POKEMON_TYPES) or []))
    else:
        predicate = _search_predicate(text)
    if "onto your bench" in text or "on your bench" in text:
        card_predicate = predicate
        predicate = lambda card: (
            (card_predicate is None or card_predicate(card))
            and (not is_pokemon_card(card) or ctx.can_bench_pokemon(card))
        )
    # A private search for a specified kind may fail even when a matching
    # card exists. An unrestricted "search for N cards" still requires N.
    reveals = "reveal" in text or "show it to your opponent" in text
    optional_search = "you may search your deck" in text
    minimum = 0 if predicate is not None or reveals or "up to" in text or optional_search else count
    picks = await ctx.search_deck(
        predicate,
        count=count,
        minimum=minimum,
        prompt="Choose cards from your deck",
        reveal_result=reveals,
    )

    if "onto your bench" in text or "on your bench" in text:
        for card in picks:
            if is_basic_pokemon(card):
                await ctx.bench_pokemon(card)
    elif "attach" in text and "energy" in text:
        for energy in picks:
            candidates = ctx.my_pokemon_in_play()
            target = (
                ctx.source
                if "to this pokémon" in text and ctx.source in candidates
                else await ctx.choose_pokemon(candidates, "Choose a Pokémon")
                if candidates
                else None
            )
            if target is not None:
                await ctx.attach_energy(energy, target)
    elif "discard" in text and "put" not in text:
        await ctx.discard_cards(picks)
    elif "on top of" in text:
        for card in reversed(picks):
            await ctx.put_on_top_of_deck(card)
    else:
        await ctx.put_in_hand(picks, reveal=reveals)

    await ctx.shuffle_deck()
    return True


def _top_deck_count(text: str) -> Optional[int]:
    match = re.search(
        r"(?:look at|reveal) the top (?:(\d+) cards?|card) of "
        r"(?:your|your opponent's|either player's) deck",
        text,
    )
    if not match:
        return None
    return int(match.group(1) or 1)


def _top_pick_count(text: str, available: int) -> tuple[int, int]:
    """Return (maximum, minimum) for a supported top-of-deck selection."""
    # Item cards from older eras append a rules reminder such as "You may play
    # as many Item cards as you like during your turn".  It describes how many
    # copies of the Item may be played, not how many cards its effect selects.
    # Max Elixir therefore attaches one Energy even though that reminder also
    # contains "as many".
    selection_text = text.split("you may play as many item cards", 1)[0]
    if "any number" in selection_text or "as many" in selection_text:
        return available, 0
    for pattern in (
        r"attach up to (\d+)",
        r"reveal up to (\d+)",
        r"choose (?:any |up to )?(\d+)",
        r"put (\d+) of them into your hand",
    ):
        match = re.search(pattern, text)
        if match:
            count = int(match.group(1))
            optional = "up to" in match.group(0)
            return count, 0 if optional else count
    # A filtered look at part of a private deck may always fail to find a
    # matching card, even though the server itself knows the identities.
    return 1, 0


def _attachment_targets(ctx, text: str):
    if "to this pokémon" in text:
        return [ctx.source] if ctx.source in ctx.my_pokemon_in_play() else []

    candidates = (
        ctx.my_bench()
        if "on your bench" in text or "to your benched" in text
        else ctx.my_pokemon_in_play()
    )
    if "basic pokémon on your bench" in text:
        candidates = [pokemon for pokemon in candidates if is_basic_pokemon(pokemon)]

    typed_target = re.search(
        r"benched (grass|fire|water|lightning|psychic|fighting|darkness|metal|"
        r"fairy|dragon|colorless) pokémon",
        text,
    )
    if typed_target:
        pokemon_type = getattr(PokemonTypes, typed_target.group(1).upper(), None)
        if pokemon_type is not None:
            candidates = [
                pokemon for pokemon in candidates
                if pokemon_type.value in (
                    pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
                )
            ]
    return candidates


async def _finish_top_deck_cards(ctx, text: str, viewed, chosen):
    """Place the viewed-but-unselected cards exactly where the text says."""
    chosen_ids = {card.entity_id for card in chosen}
    remaining = [card for card in viewed if card.entity_id not in chosen_ids]
    if "discard the other card" in text:
        await ctx.discard_cards(remaining)
    elif (
        "shuffle the other cards and put them on the bottom" in text
        or "shuffle other cards and put them on the bottom" in text
        or "shuffle the other cards and put them on bottom" in text
    ):
        random.shuffle(remaining)
        for card in remaining:
            await ctx.put_on_bottom_of_deck(card)
    elif "shuffle the other cards" in text:
        await ctx.shuffle_deck()
    elif "put the other cards back in any order" in text and remaining:
        await ctx.reorder_deck_top(len(remaining))


async def _generic_top_deck(ctx, text: str) -> bool:
    """Resolve recurring Trainer effects that inspect a deck's top cards.

    The previous fallback silently did nothing for this whole family.  Keep
    the viewed group private to its owner, show every inspected card in the
    chooser, and make only legal finds selectable.
    """
    count = _top_deck_count(text)
    if count is None or "opponent's deck" in text or "either player's deck" in text:
        return False

    viewed = ctx.deck_top(count)
    if not viewed:
        return True

    attaches_energy = "attach" in text and "energy" in text
    puts_in_hand = "into your hand" in text
    puts_on_bench = "onto your bench" in text or "on your bench" in text
    if not (attaches_energy or puts_in_hand or puts_on_bench):
        return False

    # "put N of them" and "choose any N cards" are unrestricted.  Looking at
    # the entire printed text for a type used to mistake the standard Item
    # reminder ("play as many Item cards...") for Acro Bike's filter.
    unrestricted = bool(re.search(
        r"put \d+ of them into your hand|choose any \d+ cards", text
    ))
    predicate = None if unrestricted else _search_predicate(text)
    eligible = [card for card in viewed if predicate is None or predicate(card)]
    if puts_on_bench and not attaches_energy and not puts_in_hand:
        eligible = [card for card in eligible if ctx.can_bench_pokemon(card)]
    if "a pokémon and a trainer card" in text:
        groups = await ctx.choose_card_groups(
            (
                (is_pokemon_card, 1, "Choose a Pokémon."),
                (is_trainer_card, 1, "Choose a Trainer card."),
            ),
            viewed,
            prompt="Choose a Pokémon and a Trainer card",
        )
        chosen = [card for group in groups for card in group]
    else:
        maximum, minimum = _top_pick_count(text, len(eligible))
        # Keep one browser slot even when the inspected cards contain no
        # legal find. The deck is private information, so effects such as
        # Max Elixir must still let the player see every looked-at card and
        # then finish with no selection. prompt_card_chooser clamps the
        # required amount to the actual selectable set.
        maximum = max(1, maximum)
        minimum = min(minimum, len(eligible))
        if "look at the top" in text and "reveal the top" not in text \
                and (predicate is not None or "reveal" in text):
            minimum = 0
        chosen = await ctx.choose_cards(
            eligible,
            maximum,
            minimum=minimum,
            prompt="Choose cards",
            display_cards=viewed,
        )

    if attaches_energy:
        targets = _attachment_targets(ctx, text)
        for energy in chosen:
            target = (
                targets[0]
                if len(targets) == 1
                else await ctx.choose_pokemon(targets, "Choose a Pokémon")
                if targets
                else None
            )
            if target is not None:
                await ctx.attach_energy(energy, target)
    elif puts_on_bench:
        for pokemon in chosen:
            await ctx.bench_pokemon(pokemon)
    else:
        await ctx.put_in_hand(
            chosen,
            reveal="reveal" in text or "show" in text,
        )

    await _finish_top_deck_cards(ctx, text, viewed, chosen)
    return True


def _faba_targets(board, player_id):
    """Opponent's attachments and any Trainer-targetable Stadium."""
    from spirit.game.card_effects.trainers import _tools_and_stadium
    opponent_id = _opponent_id(board, player_id)
    targets = [card for card in _tools_and_stadium(board)
               if is_stadium_card(card)
               or card.parent.owning_player_id == opponent_id]
    if opponent_id:
        for pokemon in board.pokemon_in_play(opponent_id):
            targets.extend(card for card in board.attached_energies(pokemon)
                           if is_special_energy(card))
    return targets


def standard_trainer_effect(game_text: str):
    """Create a playable fallback for a non-passive Trainer's printed text.

    Bespoke/reprinted Trainers never reach this function.  It intentionally
    covers broad, deterministic templates and leaves unfamiliar clauses as a
    harmless no-op rather than marking the card unimplemented in the client.
    """
    normalized = _trainer_rules_text(game_text)

    async def effect(ctx):
        text = normalized
        paid_hand_discard = False
        from spirit.game.card_effects.sm_searches import resolve_sm_search
        if await resolve_sm_search(ctx):
            return
        if "your zygarde-gx can use its gx attack" in text:
            # Discarding is not an "if you do" cost. A protected Prism Star
            # stays in play, but the independent GX permission still applies.
            if ctx.stadium_in_play() is not None:
                await ctx.discard_stadium()
                ctx.session.turn_state.gx_repeat_names_this_turn.setdefault(
                    ctx.player_id, set()).add("zygarde-gx")
            return
        if "heal 120 damage from the pokémon you moved to your bench" in text:
            outgoing = ctx.my_active()
            if outgoing is None or not ctx.my_bench():
                return
            paid = []
            hand = [c for c in ctx.hand() if c is not ctx.source]
            if len(hand) >= 2 and outgoing.get_attribute(AttrID.HP, 0) < ctx.max_hp(outgoing) \
                    and await ctx.ask_yes_no("Discard 2 cards to heal the switched Pokémon?"):
                paid = await ctx.choose_cards(hand, 2, minimum=2,
                                               prompt="Choose 2 cards to discard")
                await ctx.discard_cards(paid)
            target = await ctx.choose_pokemon(ctx.my_bench(), "Choose your new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
                if len(paid) == 2:
                    await ctx.heal(120, outgoing)
            return
        if "you may also search for a pokémon tool card and a special energy card" in text:
            hand = [c for c in ctx.hand() if c is not ctx.source]
            paid = []
            if len(hand) >= 2 and await ctx.ask_yes_no(
                    "Discard 2 cards to also search for a Pokémon Tool and Special Energy?"):
                paid = await ctx.choose_cards(hand, 2, minimum=2,
                                               prompt="Choose 2 cards to discard")
                await ctx.discard_cards(paid)
            groups = [(is_stadium_card, 1, "Stadium")]
            if len(paid) == 2:
                groups.extend([(is_pokemon_tool, 1, "Pokémon Tool"),
                               (is_special_energy, 1, "Special Energy")])
            selections = await ctx.search_deck_groups(groups, prompt="Choose cards to reveal")
            await ctx.put_in_hand([c for group in selections for c in group], reveal=True)
            await ctx.shuffle_deck()
            return
        if "you can't choose cynthia & caitlin" in text:
            # Pay the optional cost before recovery, so the newly discarded
            # card cannot be selected and the recovered card cannot pay it.
            candidates = [c for c in ctx.discard_pile()
                          if is_supporter_card(c)
                          and _card_name(c).casefold() != "cynthia & caitlin"]
            hand = [c for c in ctx.hand() if c is not ctx.source]
            paid = []
            if hand and ctx.deck() and await ctx.ask_yes_no(
                    "Discard a card to draw 3 cards?"):
                paid = await ctx.choose_cards(hand, 1, minimum=1,
                                               prompt="Choose a card to discard")
                await ctx.discard_cards(paid)
            chosen = await _choose_one(ctx, candidates, "Choose a Supporter") \
                if candidates else None
            if chosen is not None:
                await ctx.put_in_hand([chosen], reveal=True)
            if paid:
                await ctx.draw_cards(3)
            return
        if text.startswith('you may play 2 puzzle of time cards at once'):
            copies = [card for card in ctx.hand() if card is not ctx.source
                      and _card_name(card).casefold() == 'puzzle of time']
            pool = [card for card in ctx.discard_pile() if card is not ctx.source]
            paired = bool(copies and pool) and (
                not ctx.deck() or await ctx.ask_yes_no('Play a second Puzzle of Time?'))
            if paired:
                # Both played Items are unavailable to their own recovery effect.
                await ctx.discard_cards([copies[0]])
                count = min(2, len(pool))
                picks = await ctx.choose_cards(pool, count, minimum=count,
                                               prompt='Choose cards to recover')
                await ctx.put_in_hand(picks, reveal=True)
            elif ctx.deck():
                await ctx.reorder_deck_top(3)
            return
        from spirit.game.card_effects.hgss_era import resolve_hgss_trainer
        if await resolve_hgss_trainer(ctx):
            return

        # Choice and coin cards must resolve one complete printed branch
        # before broad discard/search patterns consume only half of it.
        if text.startswith("choose 1:") and "put a judge card from your discard pile" in text:
            judges = [card for card in ctx.discard_pile()
                      if _card_name(card).casefold() == "judge"]
            deck = ctx.board.find_player_area(ctx.player_id, "deck")
            options = []
            if deck is not None and deck.children:
                options.append("Draw a card")
            if judges:
                options.append("Put a Judge into your hand")
            if not options:
                return
            index = await ctx.choose("Choose an effect", options) if len(options) > 1 else 0
            if options[index] == "Draw a card":
                await ctx.draw_cards(1)
            else:
                chosen = await _choose_one(ctx, judges, "Choose a Judge")
                if chosen is not None:
                    await ctx.put_in_hand([chosen], reveal=True)
            return
        if text.startswith("choose 1: • put a basic energy card from your discard"):
            energies = [card for card in ctx.discard_pile()
                        if is_basic_energy(card)]
            option = await ctx.choose(
                "Choose an effect",
                ["Put 1 Basic Energy into your hand",
                 "Shuffle 3 Basic Energy into your deck"],
            )
            if option == 0:
                chosen = await _choose_one(ctx, energies, "Choose a Basic Energy") \
                    if energies else None
                if chosen is not None:
                    await ctx.put_in_hand([chosen], reveal=True)
            else:
                count = min(3, len(energies))
                chosen = await ctx.choose_cards(
                    energies, count, minimum=count,
                    prompt="Choose Basic Energy cards",
                ) if count else []
                await ctx.shuffle_into_deck(chosen)
            return

        if text.startswith("count your prize cards, shuffle them, and put them on the bottom"):
            prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
            prizes = list(prize_area.children) if prize_area is not None else []
            random.shuffle(prizes)
            for prize in prizes:
                await ctx.put_on_bottom_of_deck(prize)
            await ctx.put_in_prizes(ctx.deck_top(len(prizes)))
            return

        if text.startswith("discard the top 7 cards of your deck") \
                and "item cards" in text:
            viewed = ctx.deck_top(7)
            await ctx.discard_cards(viewed)
            await ctx.put_in_hand(
                [card for card in viewed if is_item_card(card)], reveal=True
            )
            return

        if text.startswith("flip a coin. if heads, choose 1 of your opponent's benched"):
            if (await ctx.flip_coins(1, _card_name(ctx.source)))[0]:
                bench = list(ctx.opponent_bench())
                target = await ctx.choose_pokemon(
                    bench, "Choose your opponent's new Active Pokémon"
                ) if bench else None
                if target is not None:
                    await ctx.switch_active(ctx.opponent_id, target)
            return

        if text.startswith("flip a coin. if heads, heal 60 damage"):
            if (await ctx.flip_coins(1, _card_name(ctx.source)))[0]:
                candidates = [p for p in ctx.my_pokemon_in_play()
                              if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
                target = await ctx.choose_pokemon(
                    candidates, "Choose a Pokémon to heal"
                ) if candidates else None
                if target is not None:
                    await ctx.heal(60, target)
                    await ctx.cure_all_conditions(target)
            return

        if text.startswith("flip a coin. if heads, return 1 of your pokémon"):
            if (await ctx.flip_coins(1, _card_name(ctx.source)))[0]:
                candidates = list(ctx.my_pokemon_in_play())
                target = candidates[0] if len(candidates) == 1 \
                    else await ctx.choose_pokemon(
                        candidates, "Choose a Pokémon to return"
                    ) if candidates else None
                if target is not None:
                    await ctx.put_in_hand(full_stack(target), reveal=False)
            return

        if text.startswith("flip a coin. if heads, search your discard pile for a pokémon"):
            heads = bool((await ctx.flip_coins(1, _card_name(ctx.source)))[0])
            predicate = is_pokemon_card if heads else (
                is_item_card if "for an item card" in text or "for a item card" in text
                else is_trainer_card)
            candidates = [card for card in ctx.discard_pile()
                          if predicate(card)]
            chosen = await _choose_one(
                ctx, candidates,
                "Choose a Pokémon" if heads else "Choose an Item card",
            ) if candidates else None
            if chosen is not None:
                await ctx.reveal_cards([chosen])
                await ctx.put_on_top_of_deck(chosen)
            return

        if text.startswith("you can play this card only if you took it as a face-down prize"):
            if (await ctx.flip_coins(1, _card_name(ctx.source)))[0]:
                await ctx.take_prizes(1)
            return

        if text.startswith("put 2 cards from your hand on the bottom of your deck"):
            hand = list(ctx.hand())
            chosen = await ctx.choose_cards(
                hand, 2, minimum=2, prompt="Choose 2 cards for the deck bottom"
            ) if len(hand) >= 2 else []
            if len(chosen) == 2:
                for card in chosen:
                    await ctx.put_on_bottom_of_deck(card)
                await ctx.draw_cards(4)
            return

        if text.startswith("put a card from your hand on the bottom of your deck") \
                and "draw cards until you have 5" in text:
            chosen = await _choose_one(
                ctx, ctx.hand(), "Choose a card for the deck bottom"
            ) if ctx.hand() else None
            if chosen is not None:
                await ctx.put_on_bottom_of_deck(chosen)
                await ctx.draw_until(5)
            return

        if text.startswith("put an energy attached to your opponent's active pokémon into their hand"):
            active = ctx.opponent_active()
            energies = ctx.attached_energies(active) if active is not None else []
            chosen = await _choose_one(ctx, energies, "Choose an Energy") \
                if energies else None
            if chosen is not None:
                await ctx.put_in_hand([chosen], reveal=False)
                own = [card for card in ctx.hand() if is_energy_card(card)]
                attach = await _choose_one(ctx, own, "Choose an Energy to attach") \
                    if own else None
                if attach is not None and ctx.my_active() is not None:
                    await ctx.attach_energy(attach, ctx.my_active())
            return

        if "search your deck for up to 2 basic energy cards" in text \
                and "your pokémon can't attack" in text:
            picks = await ctx.search_deck(
                is_basic_energy, 2, minimum=0,
                prompt="Choose Basic Energy cards",
            )
            target = await ctx.choose_pokemon(
                ctx.my_pokemon_in_play(), "Choose a Pokémon"
            ) if picks and ctx.my_pokemon_in_play() else None
            if target is not None:
                for energy in picks:
                    await ctx.attach_energy(energy, target)
            await ctx.shuffle_deck()
            ctx.add_temporary_player_passive(
                ctx.player_id, _TemporaryAttackRule(ctx.player_id),
                ctx.session.turn_state.turn_number,
            )
            return

        if text.startswith("switch your active pokémon with 1 of your benched pokémon") \
                and "heal" in text:
            outgoing = ctx.my_active()
            bench = list(ctx.my_bench())
            target = await ctx.choose_pokemon(
                bench, "Choose your new Active Pokémon"
            ) if bench else None
            if target is None or outgoing is None:
                return
            await ctx.switch_active(ctx.player_id, target)
            if "discard 2 other cards" in text:
                if len(ctx.hand()) >= 2 and await ctx.ask_yes_no(
                        "Discard 2 cards to heal 120 damage?"):
                    paid = await ctx.discard_from_hand(
                        2, prompt="Choose 2 cards to discard"
                    )
                    if len(paid) == 2:
                        await ctx.heal(120, outgoing)
            else:
                await ctx.heal(30, outgoing)
            return

        if text.startswith("turn 1 of your opponent's face-down prize cards face up"):
            prizes_area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
            prizes = list(prizes_area.children) if prizes_area is not None else []
            prize = await _choose_one(ctx, prizes, "Choose a Prize card") \
                if prizes else None
            hand = list(ctx.hand(ctx.opponent_id))
            random_card = random.choice(hand) if hand else None
            if prize is not None:
                await ctx.reveal_cards([prize])
                prize.publicly_revealed = True
            if random_card is not None:
                await ctx.reveal_cards([random_card])
            if prize is not None and random_card is not None \
                    and await ctx.ask_yes_no("Switch the revealed cards?"):
                await ctx.put_in_hand([prize], reveal=True)
                await ctx.put_in_prizes(
                    [random_card], player_id=ctx.opponent_id
                )
            return

        if "custom catcher cards at once" in text:
            copies = [card for card in ctx.hand()
                      if _card_name(card).casefold() == "custom catcher"]
            can_pair = bool(copies and ctx.opponent_bench())
            deck = ctx.board.find_player_area(ctx.player_id, "deck")
            can_draw = bool(deck and deck.children) and len(ctx.hand()) < 3
            use_pair = can_pair and (not can_draw or await ctx.ask_yes_no(
                "Play a second Custom Catcher?"
            ))
            if use_pair:
                await ctx.discard_cards([copies[0]])
                bench = list(ctx.opponent_bench())
                target = await ctx.choose_pokemon(
                    bench, "Choose your opponent's new Active Pokémon"
                ) if bench else None
                if target is not None:
                    await ctx.switch_active(ctx.opponent_id, target)
            elif can_draw:
                await ctx.draw_until(3)
            return

        if "mixed herbs cards at once" in text:
            copies = [card for card in ctx.hand()
                      if _card_name(card).casefold() == "mixed herbs"]
            active = ctx.my_active()
            can_single = active is not None and bool(active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
            use_pair = bool(copies) and (not can_single or await ctx.ask_yes_no(
                "Play a second Mixed Herbs?"
            ))
            if active is not None:
                if use_pair:
                    await ctx.discard_cards([copies[0]])
                    await ctx.heal(90, active)
                    await ctx.cure_all_conditions(active)
                else:
                    conditions = list(
                        active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
                    )
                    if conditions:
                        await ctx.cure_condition(active, conditions[0])
            return

        # Identity replacement must precede broad discard/search templates.
        # Ogre's Mask is the lowercase-SV ``ex`` form, distinct from XY's
        # uppercase ``EX`` but represented by the same physical stack swap.
        if 'has "ogerpon" in its name' in text \
                and "switch it with 1 of your pokémon ex in play" in text:
            incoming = [card for card in ctx.discard_pile()
                        if is_pokemon_card(card)
                        and "ogerpon" in _card_name(card).casefold()
                        and "ex" in _card_subtypes(card)]
            targets = [pokemon for pokemon in ctx.my_pokemon_in_play()
                       if "ogerpon" in _card_name(pokemon).casefold()
                       and "ex" in _card_subtypes(pokemon)]
            chosen = await _choose_one(ctx, incoming, "Choose an Ogerpon ex") \
                if incoming else None
            target = await ctx.choose_pokemon(
                targets, "Choose the Ogerpon ex to replace"
            ) if chosen is not None and targets else None
            if target is not None:
                await ctx.identity_swap(
                    target, chosen, destination="discard", transfer=True
                )
            return

        # Guessing Trainers need an explicit public reveal.  The legacy
        # client has no free-text answer node, so the opponent confirms whether
        # their spoken guess was correct after the acting player gives the
        # printed clue.
        quiz_show = text.startswith(
            "put a pokémon from your hand face down in front of you"
        ) and "opponent guesses the name of that pokémon" in text
        tyme_quiz = text.startswith(
            "tell your opponent the name of a pokémon in your hand"
        ) and "opponent guesses that pokémon's hp" in text
        if quiz_show or tyme_quiz:
            candidates = [card for card in ctx.hand() if is_pokemon_card(card)]
            chosen = await _choose_one(ctx, candidates, "Choose a Pokémon") \
                if candidates else None
            if chosen is not None:
                prompt = "Was the Pokémon guess correct?" if quiz_show \
                    else "Was the HP guess correct?"
                correct = await ctx.choose(
                    prompt, ["Yes", "No"], player_id=ctx.opponent_id
                ) == 0
                await ctx.reveal_cards([chosen])
                await ctx.draw_cards(
                    4, player_id=ctx.opponent_id if correct else ctx.player_id
                )
            return

        # Legend Box is not an ordinary one-card top-deck search: both physical
        # halves with the same LEGEND name must be present.  Reveal all ten,
        # create the stack on the Bench, attach every revealed Energy, then
        # shuffle every unused card back into the deck.
        if text.startswith("reveal the top 10 cards of your deck") \
                and "both halves of a pokémon legend" in text:
            from spirit.game.legend import legend_pairs
            viewed = ctx.deck_top(10)
            if viewed:
                await ctx.reveal_cards(viewed)
            legends = [card for card in viewed
                       if "legend" in _card_subtypes(card)]
            pairs = legend_pairs(legends)
            selected = None
            if pairs:
                first = await _choose_one(
                    ctx, [pair[0] for pair in pairs], "Choose a Pokémon LEGEND"
                )
                selected = next((pair for pair in pairs if pair[0] is first), None)
            top = None
            if selected is not None:
                top, bottom = selected
                top = await ctx.put_legend(top, bottom)
                if top is not None:
                    for energy in [card for card in viewed if is_energy_card(card)]:
                        await ctx.attach_energy(energy, top)
                else:
                    top = None
            # Unused cards never left the deck; shuffle randomizes their order
            # and re-hides every revealed identity.
            await ctx.shuffle_deck()
            if top is not None:
                # Ocean Grow says "into play", not "from your hand". Finish
                # Legend Box (including its shuffle) before this entry power.
                await ctx.flush_choreography()
                await ctx.session._fire_triggered_abilities(
                    ctx.player_id, top, Triggers.ON_PLAY)
            return

        # HeartGold & SoulSilver Items that attach themselves predate the
        # modern Pokemon Tool subtype.  They remain physical attachments for
        # their printed duration and therefore cannot use the ordinary
        # one-shot Item cleanup path.
        if text.startswith("attach defender to 1 of your pokémon"):
            targets = list(ctx.my_pokemon_in_play())
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None and await ctx.attach_card(ctx.source, target):
                ctx.add_temporary_passive(
                    ctx.source,
                    _TemporaryDamageRule(
                        ctx.player_id, amount=20, target_id=target.entity_id,
                    ),
                    ctx.session.turn_state.turn_number + 1,
                )
                ctx.schedule_discard_at_checkup(ctx.source, 1)
            return

        if text.startswith("attach pluspower to 1 of your pokémon"):
            targets = list(ctx.my_pokemon_in_play())
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Pokémon"
            ) if targets else None
            if target is not None and await ctx.attach_card(ctx.source, target):
                ctx.add_turn_damage_modifier(TurnDamageModifier(
                    amount=10, player_id=ctx.player_id,
                    source_entity_id=target.entity_id,
                ))
                ctx.schedule_discard_at_checkup(ctx.source, 0)
            return

        # Multi-step Supporters whose optional second paragraph cannot be
        # inferred from one generic draw/discard regex.
        if text.startswith("discard 3 cards from the top of each player's deck"):
            hand = [c for c in ctx.hand() if c is not ctx.source]
            paid = []
            if len(hand) >= 3 and max(len(ctx.my_bench()), len(ctx.opponent_bench())) > 3 \
                    and await ctx.ask_yes_no(
                    "Discard 3 cards to reduce both Benches to 3 Pokémon?"):
                paid = await ctx.choose_cards(hand, 3, minimum=3,
                                               prompt="Choose 3 cards to discard")
                await ctx.discard_cards(paid)
            await ctx.discard_cards(ctx.deck_top(3, ctx.opponent_id))
            await ctx.discard_cards(ctx.deck_top(3, ctx.player_id))
            if paid:
                if len(paid) == 3:
                    for pid in (ctx.opponent_id, ctx.player_id):
                        bench = (ctx.opponent_bench() if pid == ctx.opponent_id
                                 else ctx.my_bench())
                        excess = max(0, len(bench) - 3)
                        chosen = await ctx.choose_cards(
                            bench, excess, minimum=excess,
                            prompt="Choose Benched Pokémon to discard",
                            player_id=pid,
                        ) if excess else []
                        for pokemon in chosen:
                            await ctx.discard_cards(full_stack(pokemon))
            return

        if text.startswith("discard up to 2 of your benched pokémon"):
            candidates = [pokemon for pokemon in ctx.my_bench()
                          if pokemon.get_attribute(AttrID.HP, 0)
                          >= effective_max_hp(ctx.board, pokemon)]
            chosen = await ctx.choose_cards(
                candidates, min(2, len(candidates)), minimum=0,
                prompt="Choose Benched Pokémon to discard",
            ) if candidates else []
            for pokemon in chosen:
                await ctx.discard_cards(full_stack(pokemon))
            return

        if "damage from your ultra beasts' attacks isn't affected" in text:
            ctx.ignore_own_target_effects(subtype="Ultra Beast")
            return

        if "all of your pokémon take 30 less damage" in text:
            ctx.add_temporary_player_passive(
                ctx.player_id,
                _TemporaryDamageRule(ctx.player_id, amount=30),
                ctx.session.turn_state.turn_number + 1,
            )
            return

        if "their poisoned pokémon can't retreat" in text:
            poisoned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
            ctx.add_temporary_player_passive(
                ctx.opponent_id,
                _TemporaryRetreatRule(
                    ctx.opponent_id,
                    lambda pokemon: poisoned in (
                        pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
                    ),
                ),
                ctx.session.turn_state.turn_number + 1,
            )
            return

        if text.startswith("flip 2 coins. for each heads, discard 2 cards"):
            heads_count = sum(await ctx.flip_coins(2, _card_name(ctx.source)))
            if heads_count:
                await ctx.discard_cards(ctx.deck_top(2 * heads_count, ctx.opponent_id))
            return

        if text.startswith("heal 20 damage and remove a special condition"):
            active = ctx.my_active()
            if active is not None:
                await ctx.heal(20, active)
                conditions = list(active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
                if conditions:
                    await ctx.cure_condition(active, conditions[0])
            return

        # Choose one inspected card as the future top card.  The selected
        # identity never leaves the deck and all other inspected cards are
        # included in the shuffle.
        top_choice = re.search(
            r"look at the top (\d+) cards of (your opponent's|either player's) deck "
            r"and choose 1 of them", text,
        )
        if top_choice:
            sides = [ctx.opponent_id] if top_choice.group(2) == "your opponent's" \
                else [ctx.player_id, ctx.opponent_id]
            sides = [pid for pid in sides if ctx.deck(pid)]
            if not sides:
                return
            index = await ctx.choose("Which deck?", [
                "Yours" if pid == ctx.player_id else "Opponent's" for pid in sides
            ]) if len(sides) > 1 else 0
            owner = sides[index]
            viewed = ctx.deck_top(int(top_choice.group(1)), owner)
            chosen = await _choose_one(ctx, viewed, "Choose the top card") \
                if viewed else None
            await ctx.shuffle_deck(owner)
            if chosen is not None:
                await ctx.put_on_top_of_deck(chosen)
            return

        if text.startswith("look at the top 5 cards of your deck and discard any number"):
            viewed = ctx.deck_top(5)
            chosen = await ctx.choose_cards(
                viewed, len(viewed), minimum=0,
                prompt="Choose cards to discard", display_cards=viewed,
            ) if viewed else []
            await ctx.discard_cards(chosen)
            remaining = [card for card in viewed if card not in chosen]
            if len(remaining) > 1:
                await ctx.reorder_deck_top(len(remaining))
            return

        # Optional hand-discard draw Supporters.  The discard is the chosen
        # quantity, not merely flavor text before an unconditional draw.
        optional_discard_draw = re.search(
            r"discard (?:up to (\d+)|any number of) (.+?) from your hand\. "
            r"(?:then, )?draw (\d+) cards for each card you discarded", text,
        )
        if optional_discard_draw:
            maximum = int(optional_discard_draw.group(1) or len(ctx.hand()))
            descriptor = re.sub(
                r"\s+cards?$", "", optional_discard_draw.group(2).strip()
            )
            predicate = _hand_discard_predicate(ctx.board, descriptor)
            candidates = [card for card in ctx.hand()
                          if predicate is None or predicate(card)]
            if "aren't pokémon-gx or pokémon-ex" in descriptor:
                candidates = [card for card in candidates
                              if is_pokemon_card(card)
                              and not {"gx", "ex"}.intersection(_card_subtypes(card))]
            if "ultra beast" in descriptor:
                candidates = [card for card in candidates
                              if "ultra beast" in _card_subtypes(card)]
            picks = await ctx.choose_cards(
                candidates, min(maximum, len(candidates)), minimum=0,
                prompt="Choose cards to discard",
            ) if candidates else []
            await ctx.discard_cards(picks)
            await ctx.draw_cards(int(optional_discard_draw.group(3)) * len(picks))
            return

        if "you may discard any number of cards from your hand" in text \
                and "draw cards until you have" in text:
            hand = list(ctx.hand())
            picks = await ctx.choose_cards(
                hand, len(hand), minimum=0, prompt="Choose cards to discard",
            ) if hand else []
            await ctx.discard_cards(picks)
            target = re.search(r"draw cards until you have (\d+) cards", text)
            if target:
                await ctx.draw_until(int(target.group(1)))
            return

        if text.startswith("look at your face-down prize cards and put 1 of them"):
            prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
            prizes = list(prize_area.children) if prize_area is not None else []
            chosen = await _choose_one(ctx, prizes, "Choose a Prize card") \
                if prizes else None
            if chosen is not None:
                await ctx.put_in_hand([chosen], reveal=False)
                await ctx.put_in_prizes([ctx.source])
                random.shuffle(prize_area.children)
            return

        if text.startswith("look at your face-down prize cards. you may reveal an ultra beast"):
            prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
            prizes = list(prize_area.children) if prize_area is not None else []
            # Looking at the Prize pile is itself part of Beast Ball's effect.
            # The chooser must see every Prize before deciding whether to take
            # an Ultra Beast; revealing only the eventual candidate leaked the
            # predicate result without actually presenting the private zone.
            if prizes:
                await ctx.reveal_cards(prizes, to_player=ctx.player_id)
            ultra_beasts = [card for card in prizes
                            if is_pokemon_card(card)
                            and "ultra beast" in _card_subtypes(card)]
            chosen = await _choose_one(
                ctx, ultra_beasts, "Choose an Ultra Beast", optional=True,
            ) if ultra_beasts else None
            if chosen is not None:
                await ctx.put_in_hand([chosen], reveal=True)
                await ctx.put_in_prizes([ctx.source])
            if prize_area is not None:
                await ctx.shuffle_prizes()
            return

        if text.startswith("move up to 3 damage counters from 1 of your opponent's"):
            sources = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                       if pokemon.get_attribute(AttrID.HP, 0)
                       < effective_max_hp(ctx.board, pokemon)]
            source = await ctx.choose_pokemon(
                sources, "Choose a Pokémon with damage"
            ) if sources else None
            targets = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                       if pokemon is not source]
            target = await ctx.choose_pokemon(
                targets, "Choose the Pokémon receiving the damage"
            ) if source is not None and targets else None
            if source is not None and target is not None:
                available = min(
                    3, (effective_max_hp(ctx.board, source)
                        - source.get_attribute(AttrID.HP, 0)) // 10,
                )
                if available:
                    amount = 1 + await ctx.choose(
                        "How many damage counters?",
                        [str(value) for value in range(1, available + 1)],
                    )
                    await ctx.move_damage_counters(source, target, amount)
            return

        if text.startswith("put 2 cards from your hand in the lost zone"):
            paid = await ctx.choose_cards(
                ctx.hand(), 2, minimum=2, prompt="Choose 2 cards"
            ) if len(ctx.hand()) >= 2 else []
            if len(paid) == 2:
                await ctx.move_to_lost_zone(paid)
                await ctx.draw_cards(1)
            return

        if "put a basic pokémon from your opponent's discard pile onto" in text:
            candidates = [card for card in ctx.discard_pile(ctx.opponent_id)
                          if is_basic_pokemon(card)]
            chosen = await _choose_one(ctx, candidates, "Choose a Basic Pokémon") \
                if candidates else None
            if chosen is not None:
                await ctx.bench_pokemon(chosen)
            return

        if text.startswith("remove all effects of attacks on"):
            state = ctx.session.turn_state
            affected = set(ctx.board.player_ids) if "each player" in text \
                else {ctx.player_id}
            affected_ids = {
                pokemon.entity_id for pid in affected
                for pokemon in ctx.board.pokemon_in_play(pid)
            }
            state.remove_attack_effects(affected, affected_ids)
            ctx.board.temporary_passives = [
                passive for passive in ctx.board.temporary_passives
                if not passive.from_attack or (
                    passive.player_id not in affected
                    and passive.carrier_entity_id not in affected_ids)
            ]
            return

        if text == "shuffle your deck!":
            await ctx.shuffle_deck()
            return

        if "switch 1 of your opponent's benched mega evolution pokémon" in text:
            targets = [pokemon for pokemon in ctx.opponent_bench()
                       if "MEGA" in {value.upper() for value in _card_subtypes(pokemon)}]
            target = await ctx.choose_pokemon(targets, "Choose a Mega Evolution Pokémon") \
                if targets else None
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
            return

        if text.startswith("the next time you flip any number of coins"):
            result = await ctx.choose("Choose the first result", ["Heads", "Tails"])
            ctx.force_next_coin_result(result == 0)
            return

        if text.startswith("you can play this card only if there is any stadium"):
            if await ctx.discard_stadium() is not None:
                ctx.session.turn_state.gx_used.discard(ctx.player_id)
            return

        if "you can play this card only if you discard a darkness pokémon" in text:
            darkness = [card for card in ctx.hand()
                        if is_pokemon_card(card) and _pokemon_has_type(
                            ctx.board, card, PokemonTypes.DARKNESS)]
            paid = await _choose_one(ctx, darkness, "Choose a Darkness Pokémon") \
                if darkness else None
            if paid is None:
                return
            await ctx.discard_cards([paid])
            candidates = _faba_targets(ctx.board, ctx.player_id)
            chosen = await _choose_one(ctx, candidates, "Choose a card to discard") \
                if candidates else None
            if chosen is not None:
                await ctx.discard_cards([chosen])
            return

        if "during this turn, you can play 3 supporter cards" in text:
            ctx.set_supporter_limit(3)
            return

        if text.startswith("you can play this card only if your active pokémon is a water"):
            bench = list(ctx.opponent_bench())
            keep_count = min(2, len(bench))
            keep = await ctx.choose_cards(
                bench, keep_count, minimum=keep_count,
                prompt="Choose 2 Benched Pokémon to keep",
                player_id=ctx.opponent_id,
            ) if keep_count else []
            for pokemon in [entry for entry in bench if entry not in keep]:
                await ctx.shuffle_into_deck(
                    full_stack(pokemon), player_id=ctx.opponent_id
                )
            return

        if "prevent all damage done to your ultra beasts" in text:
            ctx.add_temporary_player_passive(
                ctx.player_id,
                _TemporaryDamageRule(
                    ctx.player_id, prevent=True,
                    target_predicate=lambda pokemon: "ultra beast" in _card_subtypes(pokemon),
                ),
                ctx.session.turn_state.turn_number + 1,
            )
            return

        if text.startswith("you can play this card only if your opponent's active pokémon is a basic"):
            active = ctx.opponent_active()
            energies = ctx.attached_energies(active) if active is not None else []
            chosen = await _choose_one(ctx, energies, "Choose an Energy") \
                if energies else None
            if chosen is not None:
                await ctx.put_on_top_of_deck(chosen)
            return

        if "discard an energy from 1 of your opponent's pokémon" in text:
            discard_cost = _mandatory_hand_discard_cost(text)
            if discard_cost is not None:
                count, descriptor = discard_cost
                paid = await ctx.discard_from_hand(
                    count,
                    predicate=_hand_discard_predicate(ctx.board, descriptor),
                    prompt="Choose cards to discard",
                )
                if len(paid) != count:
                    return
            energies = [energy for pokemon in ctx.opponent_pokemon_in_play()
                        for energy in ctx.attached_energies(pokemon)]
            chosen = await _choose_one(ctx, energies, "Choose an Energy") \
                if energies else None
            if chosen is not None:
                await ctx.discard_cards([chosen])
            return

        if "take 3 more prize cards" in text:
            ctx.add_extra_prize_watcher(
                attacker_predicate=lambda pokemon: _card_name(pokemon).startswith("N's "),
                prizes=3,
            )
            return

        # Coin-gated cards resolve the flip before their ordinary instruction.
        multi_coin = re.match(
            r"flip (\d+) coins\. (for each heads,|if both of them are heads,) (.+)", text)
        if multi_coin:
            flips = await ctx.flip_coins(int(multi_coin.group(1)), _card_name(ctx.source))
            count = sum(bool(flip) for flip in flips)
            if multi_coin.group(2).startswith("if both"):
                count = 1 if count == int(multi_coin.group(1)) else 0
            if count == 0:
                return
            instruction = multi_coin.group(3)
            if "search your deck" in instruction:
                await _generic_search(ctx, instruction, count_override=count)
                return
            if instruction.startswith("put an evolution pokémon from your discard pile"):
                pool = [card for card in ctx.discard_pile() if is_evolution_pokemon(card)]
                count = min(count, len(pool))
                picks = await ctx.choose_cards(pool, count, minimum=count,
                            prompt="Choose Evolution Pokémon") if count else []
                await ctx.put_in_hand(picks, reveal=True)
                return
            if instruction.startswith("shuffle an electropower card from your discard pile"):
                pool = [card for card in ctx.discard_pile() if _card_name(card).casefold() == "electropower"]
                count = min(count, len(pool))
                picks = await ctx.choose_cards(pool, count, minimum=count,
                            prompt="Choose Electropower cards") if count else []
                if picks:
                    await ctx.shuffle_into_deck(picks)
                return
        heads = None
        if "flip a coin" in text:
            heads = bool((await ctx.flip_coins(1, _card_name(ctx.source)))[0])
            if "if heads" in text and not heads:
                return

        # Mandatory costs must resolve before a deck consultation.  They used
        # to sit after the early return for search/look effects, which made
        # cards such as Misty's Determination and Morgan free to play.
        discard_cost = _mandatory_hand_discard_cost(text)
        if discard_cost is not None:
            count, descriptor = discard_cost
            paid = await ctx.discard_from_hand(
                count,
                predicate=_hand_discard_predicate(
                    getattr(ctx, "board", None), descriptor
                ),
                prompt="Choose cards to discard",
            )
            if len(paid) != count:
                return
            paid_hand_discard = True
        if text.startswith("discard your hand and search your deck"):
            await ctx.discard_cards(list(ctx.hand()))
        if "discard dana, evelyn, and nita from your hand" in text:
            hand = list(ctx.hand())
            named = []
            for required_name in ("dana", "evelyn", "nita"):
                match = next(
                    (card for card in hand
                     if _card_name(card).lower() == required_name
                     and card not in named),
                    None,
                )
                if match is None:
                    return
                named.append(match)
            await ctx.discard_cards(named)

        # Direct Energy acceleration from a public zone.  The old importer
        # generated a callable for these cards but the shared interpreter only
        # understood deck searches, so Aqua Patch/Reboot Pod-style effects
        # resolved without moving anything.
        attach_from = re.search(
            r"attach (?:(?:up to )?(\d+) |an? )?(?:(basic|special) )?"
            r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
            r"energy(?: cards?)? from your (hand|discard pile)",
            text,
        )
        if attach_from:
            explicit_count = attach_from.group(1)
            qualifier, type_word, zone = (
                attach_from.group(2), attach_from.group(3), attach_from.group(4)
            )
            pool = list(ctx.hand()) if zone == "hand" else list(ctx.discard_pile())
            energies = [card for card in pool if is_energy_card(card)]
            if qualifier == "basic":
                energies = [card for card in energies if is_basic_energy(card)]
            elif qualifier == "special":
                energies = [card for card in energies if is_special_energy(card)]
            if type_word:
                ptype = getattr(PokemonTypes, type_word.upper())
                energies = [card for card in energies
                            if energy_provides_type(card, ptype.value)]
            targets = _trainer_energy_targets(ctx, text)
            count = len(targets) if "to each of your" in text \
                else int(explicit_count or 1)
            maximum = min(count, len(energies))
            picks = await ctx.choose_cards(
                energies, maximum,
                minimum=0 if "up to" in text else maximum,
                prompt="Choose Energy cards",
            ) if maximum and targets else []
            if "to each of your" in text:
                remaining_targets = list(targets)
                for energy in picks:
                    target = remaining_targets[0] if len(remaining_targets) == 1 else \
                        await ctx.choose_pokemon(remaining_targets, "Choose a Pokémon")
                    if target in remaining_targets:
                        await ctx.attach_energy(energy, target)
                        remaining_targets.remove(target)
            else:
                one_destination = bool(re.search(
                    r"to (?:1|one) of your ", text
                ))
                fixed_target = targets[0] if len(targets) == 1 else \
                    await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                    if one_destination and targets else None
                for energy in picks:
                    target = fixed_target or await ctx.choose_pokemon(
                        targets, "Choose a Pokémon"
                    )
                    if target is not None:
                        await ctx.attach_energy(energy, target)
            draw_after_attach = re.search(
                r"if (?:you do|you attached any energy in this way), draw (\d+) cards?",
                text,
            )
            if picks and draw_after_attach:
                await ctx.draw_cards(int(draw_after_attach.group(1)))
            return

        # Older wording omits "card" and may put the usage restriction before
        # the instruction (Zinnia).  It is still the same physical operation.
        attach_from = re.search(
            r"attach (?:up to (\d+) |an? )?(?:basic )?"
            r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy)? ?"
            r"energy from your (hand|discard pile)", text,
        )
        if attach_from:
            count = int(attach_from.group(1) or 1)
            type_word, zone = attach_from.group(2), attach_from.group(3)
            pool = list(ctx.hand()) if zone == "hand" else list(ctx.discard_pile())
            energies = [card for card in pool if is_energy_card(card)]
            if "basic energy" in attach_from.group(0):
                energies = [card for card in energies if is_basic_energy(card)]
            if type_word:
                ptype = getattr(PokemonTypes, type_word.upper())
                energies = [card for card in energies
                            if energy_provides_type(card, ptype.value)]
            targets = _trainer_energy_targets(ctx, text)
            maximum = min(count, len(energies))
            picks = await ctx.choose_cards(
                energies, maximum, minimum=0 if "up to" in text else maximum,
                prompt="Choose Energy cards",
            ) if maximum and targets else []
            one_destination = bool(re.search(r"to (?:1|one) of your ", text))
            fixed_target = targets[0] if len(targets) == 1 else \
                await ctx.choose_pokemon(targets, "Choose a Pokémon") \
                if one_destination and targets else None
            for energy in picks:
                target = fixed_target or await ctx.choose_pokemon(
                    targets, "Choose a Pokémon")
                if target is not None:
                    await ctx.attach_energy(energy, target)
            draw_after_attach = re.search(
                r"if (?:you do|you attached any energy in this way), draw (\d+) cards?",
                text,
            )
            if picks and draw_after_attach:
                await ctx.draw_cards(int(draw_after_attach.group(1)))
            return

        # Rare Candy's pre-2011 wording can choose either a Stage 1 or Stage 2
        # from hand and evolves directly, bypassing normal timing rules.
        if text.startswith("choose 1 of your basic pokémon in play") \
                and "counts as evolving" in text:
            basics = []
            compatible = {}
            for pokemon in ctx.my_pokemon_in_play():
                if not is_basic_pokemon(pokemon):
                    continue
                logic = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                evolutions = [
                    card for card in ctx.hand()
                    if is_evolution_pokemon(card)
                    and evolves_from(card.archetype_id, logic)
                ]
                if evolutions:
                    basics.append(pokemon)
                    compatible[pokemon.entity_id] = evolutions
            target = await ctx.choose_pokemon(
                basics, "Choose a Basic Pokémon"
            ) if basics else None
            if target is not None:
                chosen = await _choose_one(
                    ctx, compatible.get(target.entity_id, []),
                    "Choose an Evolution Pokémon",
                )
                if chosen is not None:
                    await ctx.evolve_pokemon(target, chosen)
            return

        # Identity swaps preserve all attachments, damage and turn stamps.
        if "switch it with 1 of your pokémon in play" in text \
                and "any attached cards, damage counters" in text:
            candidates = list(ctx.discard_pile())
            if "basic darkness pokémon" in text:
                candidates = [card for card in candidates
                              if is_basic_pokemon(card)
                              and _pokemon_has_type(ctx.board, card, PokemonTypes.DARKNESS)]
            if 'has "ogerpon" in its name' in text:
                candidates = [card for card in candidates
                              if "ogerpon" in _card_name(card).casefold()
                              and "ex" in _card_subtypes(card)]
            incoming = await _choose_one(ctx, candidates, "Choose a Pokémon") \
                if candidates else None
            targets = list(ctx.my_pokemon_in_play())
            if 'has "ogerpon" in its name' in text:
                targets = [pokemon for pokemon in targets
                           if "ogerpon" in _card_name(pokemon).casefold()
                           and "ex" in _card_subtypes(pokemon)]
            outgoing = await ctx.choose_pokemon(
                targets, "Choose the Pokémon to replace"
            ) if incoming is not None and targets else None
            if outgoing is not None:
                await ctx.identity_swap(outgoing, incoming, destination="discard",
                                        transfer=True)
            return

        # Devolution Trainers choose the in-play stack itself.  Evolution
        # cards leave from the top one by one so the retained Basic keeps all
        # attachments and damage.
        if text.startswith("devolve 1 of your evolved"):
            candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                          if is_evolution_pokemon(pokemon)]
            if "psychic pokémon" in text:
                candidates = [pokemon for pokemon in candidates
                              if _pokemon_has_type(ctx.board, pokemon,
                                                   PokemonTypes.PSYCHIC)]
            target = await ctx.choose_pokemon(
                candidates, "Choose an evolved Pokémon"
            ) if candidates else None
            if target is not None:
                steps = max(1, sum(is_evolution_pokemon(card)
                                   for card in full_stack(target)))
                stack = full_stack(target)
                area = target.parent
                if "any number of evolution cards" in text and steps > 1:
                    steps = 1 + await ctx.choose("How many Evolution cards to remove?",
                                                [str(n) for n in range(1, steps + 1)])
                await ctx.devolve_pokemon(
                    target, steps=steps,
                    destination="deck" if "shuffling" in text else "hand",
                )
                if "shuffling" in text:
                    await ctx.shuffle_deck()
                if "can't evolve this turn" in text:
                    remaining = next((c for c in stack if c.parent is area), None)
                    if remaining is not None:
                        ctx.add_temporary_passive(remaining, _DevolutionEvolutionLock(),
                                                 ctx.session.turn_state.turn_number)
            return

        # Multi-coin healing such as Moomoo Milk.  Each heads is a distinct
        # printed heal increment, but the HP move is sent as one operation.
        multi_coin_heal = re.search(
            r"flip (\d+) coins.*for each heads, (?:remove (\d+) damage counters|"
            r"heal (\d+) damage)", text,
        )
        if multi_coin_heal:
            candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                          if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)]
            target = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to heal"
            ) if candidates else None
            if target is not None:
                results = await ctx.flip_coins(
                    int(multi_coin_heal.group(1)), _card_name(ctx.source)
                )
                per = int(multi_coin_heal.group(2) or 0) * 10 \
                    if multi_coin_heal.group(2) else int(multi_coin_heal.group(3) or 0)
                await ctx.heal(per * sum(bool(result) for result in results), target)
            return

        if text.startswith("discard any stadium card in play"):
            stadium = ctx.stadium_in_play()
            if stadium is not None:
                await ctx.discard_cards([stadium])
            elif "if you do" in text:
                return
            if "opponent discards 3 cards" in text:
                hand = ctx.hand(ctx.opponent_id)
                picks = await ctx.choose_cards(
                    hand, min(3, len(hand)), minimum=min(3, len(hand)),
                    prompt="Choose cards to discard",
                    player_id=ctx.opponent_id,
                ) if hand else []
                await ctx.discard_cards(picks)
            if "then, draw a card" in text:
                await ctx.draw_cards(1)
            return

        if text.startswith("discard an energy attached to your opponent's active"):
            active = ctx.opponent_active()
            if active is not None:
                await ctx.discard_energy_from(active, 1)
            return

        if text.startswith("your opponent shuffles his or her hand into his or her deck"):
            await ctx.shuffle_into_deck(
                list(ctx.hand(ctx.opponent_id)), player_id=ctx.opponent_id
            )
            await ctx.draw_cards(4, player_id=ctx.opponent_id)
            return

        if "each player shuffles his or her hand into his or her deck" in text:
            await ctx.shuffle_into_deck(list(ctx.hand()), player_id=ctx.player_id)
            await ctx.shuffle_into_deck(
                list(ctx.hand(ctx.opponent_id)), player_id=ctx.opponent_id
            )
            await ctx.draw_cards(6)
            await ctx.draw_cards(3, player_id=ctx.opponent_id)
            return

        if text.startswith("shuffle 3 pokémon tool cards from your discard pile"):
            candidates = [card for card in ctx.discard_pile()
                          if is_pokemon_tool(card)]
            count = min(3, len(candidates))
            picks = await ctx.choose_cards(
                candidates, count, minimum=count,
                prompt="Choose Pokémon Tools to shuffle into your deck",
            ) if candidates else []
            await ctx.shuffle_into_deck(picks)
            return

        if text.startswith("put a pokémon from your discard pile on top of your deck"):
            candidates = [card for card in ctx.discard_pile()
                          if is_pokemon_card(card)]
            chosen = await _choose_one(ctx, candidates, "Choose a Pokémon")
            if chosen is not None:
                await ctx.put_on_top_of_deck(chosen)
            return

        if text.startswith("attach a basic energy card from your discard pile to 1 of your mega"):
            energies = [card for card in ctx.discard_pile()
                        if is_basic_energy(card)]
            targets = [
                pokemon for pokemon in ctx.my_pokemon_in_play()
                if "MEGA" in (getattr(def_for(pokemon.archetype_id), "subtypes", []) or [])
            ]
            energy = await _choose_one(ctx, energies, "Choose a basic Energy")
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Mega Evolution Pokémon"
            ) if targets else None
            if energy is not None and target is not None:
                await ctx.attach_energy(energy, target)
            return

        if text.startswith("attach 2 fire energy cards from your discard pile"):
            energies = [
                card for card in ctx.discard_pile()
                if is_energy_card(card)
                and energy_provides_type(card, PokemonTypes.FIRE.value)
            ]
            targets = [
                pokemon for pokemon in ctx.my_pokemon_in_play()
                if PokemonTypes.FIRE.value in effective_pokemon_types(
                    ctx.board, pokemon
                )
            ]
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, "Choose a Fire Pokémon"
            ) if targets else None
            if target is not None:
                count = min(2, len(energies))
                picks = await ctx.choose_cards(
                    energies, count, minimum=count,
                    prompt="Choose Fire Energy cards",
                ) if count else []
                for energy in picks:
                    await ctx.attach_energy(energy, target)
            return

        if text.startswith("discard all pokémon tool cards attached to each of your opponent's"):
            tools = [
                tool for tool, pokemon in ctx.tools_in_play()
                if pokemon.owning_player_id == ctx.opponent_id
            ]
            await ctx.discard_cards(tools)
            return

        if text.startswith("choose a pokémon tool or special energy card attached"):
            lost_zone = "lost zone" in text
            candidates = _faba_targets(ctx.board, ctx.player_id) if lost_zone else [
                card for pid in ctx.board.player_ids
                for pokemon in ctx.board.pokemon_in_play(pid)
                for card in pokemon.children
                if is_pokemon_tool(card) or is_special_energy(card)]
            chosen = await _choose_one(ctx, candidates,
                "Choose a card to put in the Lost Zone" if lost_zone else "Choose a card to discard")
            if chosen is not None:
                if lost_zone:
                    await ctx.move_to_lost_zone([chosen])
                else:
                    await ctx.discard_cards([chosen])
            return

        if text.startswith("put 1 pokémon into your hand. (discard all cards attached"):
            candidates = ctx.my_pokemon_in_play()
            target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
                candidates, "Choose a Pokémon"
            ) if candidates else None
            if target is not None:
                evolution_cards, attachments = split_pokemon_stack(target)
                await ctx.discard_cards(attachments)
                await ctx.put_in_hand(evolution_cards, reveal=False)
            return

        if text.startswith("each player shuffles all cards in his or her discard pile"):
            for pid in ctx.board.player_ids:
                await ctx.shuffle_into_deck(
                    list(ctx.discard_pile(pid)), player_id=pid
                )
            return

        if await _generic_search(ctx, text):
            return

        if await _generic_top_deck(ctx, text):
            return

        # Prize reset effects keep the count and randomize the replacement
        # cards; none of the identities are announced in the history.
        if "count" in text and "prize cards" in text \
                and "take that many cards from the top of your deck" in text:
            prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
            prizes = list(prize_area.children) if prize_area is not None else []
            count = len(prizes)
            if prizes:
                await ctx.shuffle_into_deck(prizes)
            replacements = ctx.deck_top(count)
            await ctx.put_in_prizes(replacements)
            return

        # Bottom-of-deck consultation (fossils, Dusk Ball, Underground
        # Expedition).  Deck bottom is index 0 in the server model.
        bottom = re.search(r"look at the bottom (\d+) cards of your deck", text)
        if bottom:
            deck = list(ctx.deck())
            viewed = deck[:int(bottom.group(1))]
            predicate = _search_predicate(text)
            # Fossils name a species rather than saying "Pokemon". Do not
            # mistake the trailing Item reminder for the requested card type.
            named = re.search(r"reveal an? ([^.]+?) you find there", text)
            if named and "onto your bench" in text:
                wanted_name = named.group(1)
                predicate = lambda card: is_pokemon_card(card) and _card_name(card).casefold() == wanted_name
            eligible = [card for card in viewed if predicate is None or predicate(card)]
            count = 2 if "put 2 of them into your hand" in text else 1
            if "onto your bench" in text:
                eligible = [card for card in eligible if ctx.can_bench_pokemon(card)]
                free = max(0, effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()))
                count = min(count, free)
            selectable = eligible if count > 0 else []
            picks = await ctx.choose_cards(
                selectable, max(1, min(count, len(eligible))),
                minimum=0 if predicate is not None or "reveal" in text or "you may" in text
                else min(count, len(eligible)),
                prompt="Choose cards", display_cards=viewed,
            ) if viewed else []
            if picks and "reveal" in text:
                await ctx.reveal_cards(picks)
            if "onto your bench" in text:
                for card in picks:
                    await ctx.bench_pokemon(card)
            else:
                await ctx.put_in_hand(picks, reveal="reveal" in text)
            remaining = [card for card in viewed if card not in picks]
            if "shuffle the other cards" in text:
                # Put the inspected remainder back before shuffling so every
                # unchosen identity remains in the deck.
                await ctx.shuffle_deck()
            elif "bottom of your deck in any order" in text:
                for card in remaining:
                    await ctx.put_on_bottom_of_deck(card)
            return

        # Information/order-only top-deck effects not consumed by
        # _generic_top_deck because they do not move a card to another zone.
        top_order = re.search(
            r"look at the top (\d+) cards? of (your|your opponent's|either player's) "
            r"deck.*put (?:them|as many of them as you like) back", text,
        )
        if top_order:
            pid = ctx.opponent_id if top_order.group(2) == "your opponent's" \
                else ctx.player_id
            if top_order.group(2) == "either player's":
                side = await ctx.choose("Choose a deck", ["Your deck", "Opponent's deck"])
                pid = ctx.player_id if side == 0 else ctx.opponent_id
            await ctx.reorder_deck_top(int(top_order.group(1)), player_id=pid)
            return
        if "look at the top card of either player's deck" in text:
            sides = [pid for pid in (ctx.player_id, ctx.opponent_id) if ctx.deck(pid)]
            if not sides:
                return
            index = await ctx.choose("Choose a deck", [
                "Your deck" if pid == ctx.player_id else "Opponent's deck"
                for pid in sides
            ]) if len(sides) > 1 else 0
            card = (ctx.deck_top(1, player_id=sides[index]) or [None])[0]
            if card is not None:
                await ctx.reveal_cards([card], to_player=ctx.player_id)
                if await ctx.ask_yes_no("Discard this card?"):
                    await ctx.discard_cards([card])
            return

        # Shuffle a fixed number of hand cards into the deck, then draw.
        if "shuffle a card from your hand into your deck. if you do, draw" in text:
            candidates = list(ctx.hand())
            chosen = await _choose_one(
                ctx, candidates, "Choose a card to shuffle into your deck"
            ) if candidates else None
            if chosen is not None:
                await ctx.shuffle_into_deck([chosen])
                draw = re.search(r"if you do, draw (\d+) cards?", text)
                if draw:
                    await ctx.draw_cards(int(draw.group(1)))
            return

        hand_shuffle = re.search(r"shuffle (\d+) cards from your hand into your deck", text)
        if hand_shuffle:
            count = int(hand_shuffle.group(1))
            picks = await ctx.choose_cards(
                ctx.hand(), count, minimum=count,
                prompt="Choose cards to shuffle into your deck",
            )
            await ctx.shuffle_into_deck(picks)
            draw = re.search(r"then, draw (\d+|a) cards?", text)
            if draw:
                await ctx.draw_cards(1 if draw.group(1) == "a" else int(draw.group(1)))
            return

        # Both-player hand resets and fixed same-size redraws.
        if "each player counts the cards in their hand" in text \
                and "draws that many cards" in text:
            sizes = {pid: ctx.hand_size(pid) for pid in ctx.board.player_ids}
            for pid in ctx.board.player_ids:
                await ctx.shuffle_into_deck(list(ctx.hand(pid)), player_id=pid)
            for pid, count in sizes.items():
                await ctx.draw_cards(count, player_id=pid)
            return
        if "your opponent counts the cards in their hand" in text \
                and "draw that many cards" in text:
            count = ctx.hand_size(ctx.opponent_id)
            await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
            await ctx.draw_cards(count, player_id=ctx.opponent_id)
            return
        if "each player shuffles their hand and puts it on the bottom" in text:
            moved = 0
            for pid in ctx.board.player_ids:
                moved += await ctx.hand_to_bottom_of_deck(pid)
            # Iono checks both hands collectively, after resolving movement.
            # An empty hand still draws if the other player returned cards.
            if "if either player put any cards" in text and not moved:
                return
            for pid in ctx.board.player_ids:
                prizes = ctx.board.find_player_area(pid, "prizePile")
                await ctx.draw_cards(len(prizes.children) if prizes else 0, player_id=pid)
            return
        if "opponent shuffles their hand into their deck" in text \
                and "remaining prize cards" in text:
            await ctx.shuffle_into_deck(
                list(ctx.hand(ctx.opponent_id)), player_id=ctx.opponent_id
            )
            prizes = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
            await ctx.draw_cards(
                len(prizes.children) if prizes else 0,
                player_id=ctx.opponent_id,
            )
            return

        # Explicit hand reveals must still open the real viewer even if the
        # card makes no subsequent choice (Hand Scope/Alph Lithograph).
        if "opponent reveals" in text and "hand" in text \
                or "look at your opponent's hand" in text:
            revealed = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
            opposing_discard = re.search(
                r"discard (?:up to )?(\d+) (item|energy) cards? "
                r"(?:from it|you find there)", text,
            )
            if opposing_discard:
                count, kind = int(opposing_discard.group(1)), opposing_discard.group(2)
                predicate = is_item_card if kind == "item" else is_energy_card
                candidates = [card for card in revealed if predicate(card)]
                picks = await ctx.choose_cards(
                    candidates, min(count, len(candidates)),
                    minimum=0 if "up to" in opposing_discard.group(0)
                    else min(count, len(candidates)),
                    prompt="Choose cards to discard",
                ) if candidates else []
                await ctx.discard_cards(picks)
            elif "choose a card you find there and put it on the bottom" in text:
                chosen = await _choose_one(ctx, revealed, "Choose a card") \
                    if revealed else None
                if chosen is not None:
                    await ctx.put_on_bottom_of_deck(chosen)
                    if "opponent may draw a card" in text and await ctx.ask_yes_no(
                        "Draw a card?", player_id=ctx.opponent_id
                    ):
                        await ctx.draw_cards(1, player_id=ctx.opponent_id)
            elif "choose an energy card you find there and put it on the bottom" in text:
                candidates = [card for card in revealed if is_energy_card(card)]
                chosen = await _choose_one(ctx, candidates, "Choose an Energy") \
                    if candidates else None
                if chosen is not None:
                    await ctx.put_on_bottom_of_deck(chosen)
            elif "put a pokémon you find there on the bottom" in text:
                candidates = [card for card in revealed if is_pokemon_card(card)]
                chosen = await _choose_one(ctx, candidates, "Choose a Pokémon") \
                    if candidates else None
                if chosen is not None:
                    await ctx.put_on_bottom_of_deck(chosen)
            elif "draw 2 cards for each supporter card you find there" in text:
                await ctx.draw_cards(2 * sum(is_supporter_card(c) for c in revealed))
            elif "draw a card for each pokémon you find there" in text:
                await ctx.draw_cards(sum(is_pokemon_card(c) for c in revealed))
            elif "put a basic pokémon you find there onto your opponent's bench" in text:
                basics = [card for card in revealed if is_basic_pokemon(card)]
                chosen = await _choose_one(ctx, basics, "Choose a Basic Pokémon") \
                    if basics else None
                if chosen is not None:
                    await ctx.bench_pokemon(chosen)
                    if "switch in that pokémon to the active spot" in text:
                        await ctx.switch_active(ctx.opponent_id, chosen)
            elif "discard as many cards as you like from your hand" in text:
                picks = await ctx.choose_cards(
                    ctx.hand(), len(ctx.hand()), minimum=0,
                    prompt="Choose cards to discard",
                )
                await ctx.discard_cards(picks)
                await ctx.draw_cards(len(picks))
            elif "put any number of basic pokémon" in text:
                basics = [card for card in revealed if is_basic_pokemon(card)]
                maximum = min(len(basics), max(0, 5 - len(ctx.opponent_bench())))
                picks = await ctx.choose_cards(
                    basics, maximum, minimum=0,
                    prompt="Choose Basic Pokémon for your opponent's Bench",
                ) if maximum else []
                for pokemon in picks:
                    await ctx.bench_pokemon(pokemon)
            return

        # Flower Shop Lady selects two separate categories, not three cards
        # from their union. Resolve as much of each public category as possible.
        if "search your discard pile for 3 pokémon and 3 basic energy cards" in text:
            picked = []
            for predicate, label in ((is_pokemon_card, "Pokémon"),
                                     (is_basic_energy, "basic Energy cards")):
                pool = [card for card in ctx.discard_pile() if predicate(card)]
                count = min(3, len(pool))
                if count:
                    picked.extend(await ctx.choose_cards(
                        pool, count, minimum=count, prompt=f"Choose {label}"))
            if picked:
                await ctx.reveal_cards(picked)
                await ctx.shuffle_into_deck(picked)
            return

        # Public discard -> deck/hand families whose wording begins with
        # "search your discard pile" or "shuffle N in any combination".
        if text.startswith("shuffle a pokémon and a pokémon tool card from your discard pile"):
            picks = []
            for predicate, label in ((is_pokemon_card, "Pokémon"), (is_pokemon_tool, "Pokémon Tool")):
                pool = [card for card in ctx.discard_pile() if predicate(card)]
                chosen = await _choose_one(ctx, pool, f"Choose a {label}") if pool else None
                if chosen is not None:
                    picks.append(chosen)
            if picks:
                await ctx.shuffle_into_deck(picks)
            return
        if "discard pile" in text and "shuffle" in text \
                and "into your deck" in text:
            count = _requested_count(text, default=1)
            explicit = re.search(r"(?:search your discard pile for|shuffle) (\d+)", text)
            if explicit:
                count = int(explicit.group(1))
            candidates = list(ctx.discard_pile())
            predicate = _search_predicate(text)
            if predicate is not None:
                candidates = [card for card in candidates if predicate(card)]
            # Combined Pokemon + Basic Energy clauses need a union, not the
            # first broad noun encountered by _search_predicate.
            if "pokémon and basic energy" in text \
                    or "pokémon and 3 basic energy" in text:
                candidates = [card for card in ctx.discard_pile()
                              if is_pokemon_card(card) or is_basic_energy(card)]
            maximum = min(count, len(candidates))
            picks = await ctx.choose_cards(
                candidates, maximum,
                minimum=0 if "up to" in text else maximum,
                prompt="Choose cards to shuffle into your deck",
            ) if maximum else []
            await ctx.shuffle_into_deck(picks)
            return

        if "search your discard pile for" in text \
                and ("put them into your hand" in text
                     or "put it into your hand" in text):
            count = _requested_count(text)
            candidates = list(ctx.discard_pile())
            predicate = _search_predicate(text)
            if predicate is not None:
                candidates = [card for card in candidates if predicate(card)]
            if "can't choose junk arm" in text:
                candidates = [card for card in candidates
                              if _card_name(card).casefold() != "junk arm"]
            maximum = min(count, len(candidates))
            picks = await ctx.choose_cards(
                candidates, maximum, minimum=maximum,
                prompt="Choose cards from your discard pile",
            ) if maximum else []
            await ctx.put_in_hand(picks, reveal=True)
            return

        # Remove one or all attached cards of a printed category.
        if "discard a special energy from each of your opponent's pokémon" in text:
            cards = []
            for pokemon in ctx.opponent_pokemon_in_play():
                candidates = [energy for energy in ctx.attached_energies(pokemon)
                              if is_special_energy(energy)]
                chosen = await _choose_one(ctx, candidates, "Choose a Special Energy") \
                    if candidates else None
                if chosen is not None:
                    cards.append(chosen)
            await ctx.discard_cards(cards)
            return

        if "discard all pokémon tools and special energy" in text:
            cards = [
                card for pokemon in ctx.opponent_pokemon_in_play()
                for card in full_stack(pokemon)[1:]
                if is_pokemon_tool(card) or is_special_energy(card)
            ]
            await ctx.discard_cards(cards)
            if "discard a stadium" in text:
                await ctx.discard_stadium()
            return

        # Remove selected own Bench stacks (Giovanni's Exile/Weed Out-like
        # Supporters).  A whole stack moves in one grouped animation.
        bench_discard = re.search(r"discard up to (\d+) of your benched pokémon", text)
        if bench_discard:
            candidates = list(ctx.my_bench())
            if "no damage counters" in text:
                candidates = [p for p in candidates
                              if p.get_attribute(AttrID.HP, 0) == ctx.max_hp(p)]
            maximum = min(int(bench_discard.group(1)), len(candidates))
            picks = await ctx.choose_cards(
                candidates, maximum, minimum=0,
                prompt="Choose Benched Pokémon to discard",
            ) if maximum else []
            for pokemon in picks:
                await ctx.discard_cards(full_stack(pokemon))
            return

        # Return/shuffle one complete in-play stack.
        if "put 1 of your basic pokémon and all attached cards into your hand" in text:
            candidates = [p for p in ctx.my_pokemon_in_play() if is_basic_pokemon(p)]
            target = await ctx.choose_pokemon(candidates, "Choose a Basic Pokémon") \
                if candidates else None
            if target is not None:
                await ctx.put_in_hand(full_stack(target), reveal=False)
            return
        if "put 1 of your pokémon in play into your hand" in text \
                and "discard all cards attached" in text:
            candidates = list(ctx.my_pokemon_in_play())
            target = await ctx.choose_pokemon(candidates, "Choose a Pokémon") \
                if candidates else None
            if target is not None:
                evolution_cards, attachments = split_pokemon_stack(target)
                await ctx.discard_cards(attachments)
                await ctx.put_in_hand(evolution_cards, reveal=False)
            return

        # Move an opposing attached Energy to the specified public zone.
        if "energy attached to your opponent's active pokémon" in text:
            active = ctx.opponent_active()
            energies = ctx.attached_energies(active) if active is not None else []
            energy = await _choose_one(ctx, energies, "Choose an Energy") \
                if energies else None
            if energy is not None:
                if "into their hand" in text:
                    await ctx.put_in_hand([energy], reveal=False)
                elif "on top of their deck" in text:
                    await ctx.put_on_top_of_deck(energy)
                elif "discard" in text:
                    await ctx.discard_cards([energy])
                if "if you do, attach an energy card from your hand" in text:
                    own = [card for card in ctx.hand() if is_energy_card(card)]
                    chosen = await _choose_one(ctx, own, "Choose an Energy") \
                        if own else None
                    if chosen is not None and ctx.my_active() is not None:
                        await ctx.attach_energy(chosen, ctx.my_active())
            return

        if "put an energy attached to 1 of your opponent's pokémon into their hand" in text:
            energies = [energy for pokemon in ctx.opponent_pokemon_in_play()
                        for energy in ctx.attached_energies(pokemon)]
            chosen = await _choose_one(ctx, energies, "Choose an Energy") \
                if energies else None
            if chosen is not None:
                await ctx.put_in_hand([chosen], reveal=False)
            return

        if "put as many energy attached to your pokémon as you like into your hand" in text:
            energies = [energy for pokemon in ctx.my_pokemon_in_play()
                        for energy in ctx.attached_energies(pokemon)]
            picks = await ctx.choose_cards(
                energies, len(energies), minimum=0,
                prompt="Choose Energy to return to your hand",
            ) if energies else []
            await ctx.put_in_hand(picks, reveal=False)
            return

        # Stadium return differs from discard: preserve its identity and owner.
        if "return any stadium card in play to its player's hand" in text:
            stadium = ctx.stadium_in_play()
            if stadium is not None:
                await ctx.put_in_hand([stadium], reveal=False)
            return

        # Effects which explicitly reveal Prize cards (Alph Lithograph).
        if text in {
            "look at all of your face down prize cards!",
            "look at your face-down prize cards.",
        }:
            prizes = ctx.board.find_player_area(ctx.player_id, "prizePile")
            await ctx.reveal_cards(
                list(prizes.children) if prizes is not None else [],
                to_player=ctx.player_id,
            )
            return

        if (
            "prize cards" in text and "face up" in text
            and (text.startswith("look at") or "turns all" in text)
        ):
            for pid in ctx.board.player_ids:
                prizes = ctx.board.find_player_area(pid, "prizePile")
                if prizes is None:
                    continue
                # Introduce the cards to every client while they are still
                # hidden.  Marking them public first made ``reveal_cards``
                # believe that no viewer needed an update, so the server knew
                # the cards were face up but the opponent did not receive
                # their identities.
                await ctx.reveal_cards(list(prizes.children))
                for prize in prizes.children:
                    prize.publicly_revealed = True
            return

        # Simple current-turn damage boosts (Black Belt and descendants).
        current_boost = re.search(
            r"during this turn, (?:each of )?your active pokémon's attacks does "
            r"(\d+) more damage", text,
        )
        if current_boost:
            ctx.add_turn_damage_modifier(TurnDamageModifier(
                amount=int(current_boost.group(1)), player_id=ctx.player_id,
                source_predicate=lambda pokemon: pokemon is ctx.my_active(),
            ))
            return

        # Seeker returns one complete Bench stack for each player, in printed
        # order (acting player first).
        if "each player returns 1 of his or her benched pokémon" in text:
            for pid in (ctx.player_id, ctx.opponent_id):
                bench = ctx.my_bench() if pid == ctx.player_id else ctx.opponent_bench()
                target = await ctx.choose_pokemon(
                    bench, "Choose a Benched Pokémon", player_id=pid
                ) if bench else None
                if target is not None:
                    await ctx.put_in_hand(full_stack(target), reveal=False)
            return

        # Missing Clover's one-copy mode is a real information action; the
        # four-copy aggregate is dealt with by the existing multi-card player.
        if "missing clover" in text and "look at the top card" in text:
            top = ctx.deck_top(1)
            if top:
                await ctx.reveal_cards(top, to_player=ctx.player_id)
            return

        if "put a card from your opponent's discard pile on the bottom" in text:
            candidates = list(ctx.discard_pile(ctx.opponent_id))
            chosen = await _choose_one(ctx, candidates, "Choose a card") \
                if candidates else None
            if chosen is not None:
                await ctx.put_on_bottom_of_deck(chosen)
            return

        # Move Energy between two specific board roles.
        if "move an energy from 1 of your benched pokémon to your active pokémon" in text:
            sources = list(ctx.my_bench())
            targets = [ctx.my_active()] if ctx.my_active() is not None else []
            await ctx.move_energy_freely(
                sources, targets, max_count=1, prompt="Choose an Energy to move"
            )
            return
        if "move up to 2 energy from 1 of your tag team pokémon" in text:
            sources = [pokemon for pokemon in ctx.my_pokemon_in_play()
                       if "tag team" in _card_subtypes(pokemon)]
            await ctx.move_energy_freely(
                sources, ctx.my_pokemon_in_play(), max_count=2,
                single_source=True, single_destination=True,
                prompt="Choose Energy to move",
            )
            return
        if "move a special energy from 1 of your opponent's pokémon to another" in text:
            pokemon = list(ctx.opponent_pokemon_in_play())
            await ctx.move_energy_freely(
                pokemon, pokemon, predicate=is_special_energy, max_count=1,
                prompt="Choose a Special Energy to move",
            )
            return
        if "move any number of water energy from your pokémon" in text:
            await ctx.move_energy_freely(
                ctx.my_pokemon_in_play(), ctx.my_pokemon_in_play(),
                predicate=lambda card: is_energy_card(card)
                and energy_provides_type(card, PokemonTypes.WATER.value),
                max_count=None, prompt="Choose Water Energy to move",
            )
            return

        # Return attached Tools to hand (Tool Retriever).
        tool_return = re.search(r"choose up to (\d+) pokémon tool cards attached", text)
        if tool_return and "into your hand" in text:
            tools = [tool for tool, pokemon in ctx.tools_in_play()
                     if pokemon.owning_player_id == ctx.player_id]
            maximum = min(int(tool_return.group(1)), len(tools))
            picks = await ctx.choose_cards(
                tools, maximum, minimum=0,
                prompt="Choose Pokémon Tools to return",
            ) if maximum else []
            await ctx.put_in_hand(picks, reveal=False)
            return

        # Each-player effects retain the printed player order.
        each_discard = re.search(r"each player discards (\d+) cards from their hand", text)
        if each_discard:
            count = int(each_discard.group(1))
            for pid in (ctx.opponent_id, ctx.player_id):
                hand = list(ctx.hand(pid))
                amount = min(count, len(hand))
                picks = await ctx.choose_cards(
                    hand, amount, minimum=amount,
                    prompt="Choose cards to discard", player_id=pid,
                ) if amount else []
                await ctx.discard_cards(picks)
            return
        if "each player may draw up to" in text:
            count = int((re.search(r"up to (\d+) cards", text) or [None, 0])[1])
            for pid in (ctx.player_id, ctx.opponent_id):
                chosen = await ctx.choose(
                    "How many cards do you want to draw?",
                    [str(value) for value in range(count + 1)],
                    player_id=pid,
                )
                await ctx.draw_cards(chosen, player_id=pid)
            return
        if "each player puts a pokémon from" in text \
                and "discard pile into" in text and "hand" in text:
            for pid in (ctx.opponent_id, ctx.player_id):
                candidates = [card for card in ctx.discard_pile(pid)
                              if is_pokemon_card(card)]
                chosen = await _choose_one(
                    ctx, candidates, "Choose a Pokémon", player_id=pid
                ) if candidates else None
                if chosen is not None:
                    await ctx.put_in_hand([chosen], reveal=True)
            return
        if "each player puts a pokémon from his or her discard pile" in text:
            for pid in (ctx.opponent_id, ctx.player_id):
                candidates = [card for card in ctx.discard_pile(pid)
                              if is_pokemon_card(card)]
                chosen = await _choose_one(
                    ctx, candidates, "Choose a Pokémon", player_id=pid
                ) if candidates else None
                if chosen is not None:
                    await ctx.put_in_hand([chosen], reveal=True)
            return

        if "count the cards in your hand" in text \
                and "draw that many cards plus 1" in text:
            count = ctx.hand_size()
            await ctx.shuffle_into_deck(list(ctx.hand()))
            await ctx.draw_cards(count + 1)
            return

        # Count-dependent draws not matched by a literal "draw N" regex.
        if "draw a card for each of your opponent's mega evolution" in text:
            count = sum("mega" in _card_subtypes(pokemon)
                        for pokemon in ctx.opponent_pokemon_in_play())
            await ctx.draw_cards(count)
            return

        # Random hand disruption reveals exactly the selected physical cards.
        if "choose a random card from your opponent's hand" in text:
            hand = list(ctx.hand(ctx.opponent_id))
            if hand:
                card = random.choice(hand)
                await ctx.reveal_cards([card], to_player=ctx.player_id)
                if "if it's a supporter card, discard it" in text \
                        and is_supporter_card(card):
                    await ctx.discard_cards([card])
            return

        # Accompanying Flute: every inspected card is revealed, then selected
        # Basics enter the opponent's available Bench spaces together.
        if "reveal the top" in text and "opponent's deck" in text \
                and "basic pokémon" in text and "onto their bench" in text:
            count = int((re.search(r"top (\d+) cards", text) or [None, 1])[1])
            viewed = ctx.deck_top(count, ctx.opponent_id)
            await ctx.reveal_cards(viewed)
            basics = [card for card in viewed if is_basic_pokemon(card)]
            free = max(0, 5 - len(ctx.opponent_bench()))
            picks = await ctx.choose_cards(
                basics, min(free, len(basics)), minimum=0,
                prompt="Choose Basic Pokémon for your opponent's Bench",
            ) if basics and free else []
            for pokemon in picks:
                await ctx.bench_pokemon(pokemon)
            await ctx.shuffle_deck(ctx.opponent_id)
            return

        choose_heal = re.search(
            r"choose up to (\d+) of your pokémon and heal (\d+) damage from "
            r"each of them", text,
        )
        if choose_heal:
            candidates = [p for p in ctx.my_pokemon_in_play()
                          if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
            maximum = min(int(choose_heal.group(1)), len(candidates))
            picks = await ctx.choose_cards(
                candidates, maximum, minimum=0,
                prompt="Choose Pokémon to heal",
            ) if maximum else []
            for pokemon in picks:
                await ctx.heal(int(choose_heal.group(2)), pokemon)
            return

        # Heal each matching Pokemon, not merely one target.
        each_heal = re.search(
            r"heal (\d+) damage from each of your "
            r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy)? ?pokémon",
            text,
        )
        if each_heal:
            amount, type_word = int(each_heal.group(1)), each_heal.group(2)
            candidates = list(ctx.my_pokemon_in_play())
            if type_word:
                ptype = getattr(PokemonTypes, type_word.upper())
                candidates = [p for p in candidates
                              if _pokemon_has_type(ctx.board, p, ptype)]
            attached_type = re.search(
                r"that has any (grass|fire|water|lightning|psychic|fighting|"
                r"darkness|metal|fairy) energy attached", text,
            )
            if attached_type:
                ptype = getattr(PokemonTypes, attached_type.group(1).upper())
                candidates = [p for p in candidates if any(
                    energy_provides_type(card, ptype.value)
                    for card in ctx.attached_energies(p)
                )]
            for pokemon in candidates:
                await ctx.heal(amount, pokemon)
            return

        # Switch Raft heals the Pokemon that moved to the Bench, not the new
        # Active.  Preserve that identity before executing the swap.
        if "switch your active water pokémon" in text and "heal 30 damage" in text:
            outgoing = ctx.my_active()
            if outgoing is not None and _pokemon_has_type(
                    ctx.board, outgoing, PokemonTypes.WATER) and ctx.my_bench():
                target = await ctx.choose_pokemon(
                    ctx.my_bench(), "Choose your new Active Pokémon"
                )
                if target is not None:
                    await ctx.switch_active(ctx.player_id, target)
                    await ctx.heal(30, outgoing)
            return

        if "discard your hand" in text:
            await ctx.discard_cards(list(ctx.hand()))
        elif "shuffle your hand into your deck" in text:
            await ctx.shuffle_into_deck(list(ctx.hand()), player_id=ctx.player_id)

        if "draw a number of cards equal to the number of cards in your opponent's hand" in text:
            await ctx.draw_cards(ctx.hand_size(ctx.opponent_id))
            return

        draw_until = re.search(r"draw cards until you have (\d+) cards", text)
        if draw_until:
            target = int(draw_until.group(1))
            first_turn_bonus = re.search(r"if it's your first turn, draw cards until you have (\d+)", text)
            if first_turn_bonus and ctx.session.turn_state.turn_number in (1, 2):
                target = int(first_turn_bonus.group(1))
            await ctx.draw_until(target)
            return
        draw = re.search(r"draw (\d+) cards", text)
        if draw:
            await ctx.draw_cards(int(draw.group(1)))

        if "switch your active pokémon" in text and ctx.my_bench():
            target = await ctx.choose_pokemon(
                ctx.my_bench(), "Choose your new Active Pokémon"
            )
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
        if (
            "switch in 1 of your opponent's benched pokémon" in text
            or "switch 1 of your opponent's benched pokémon" in text
        ) and ctx.opponent_bench():
            targets = _opponent_switch_targets_on_board(
                ctx.board, ctx.player_id, text,
            )
            target = await ctx.choose_pokemon(
                targets, "Choose your opponent's new Active Pokémon"
            ) if targets else None
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)

        heal_all = "heal all damage from 1 of your pokémon" in text
        heal = re.search(r"heal (\d+) damage from (?:1 of )?your pokémon", text)
        if heal_all or heal:
            candidates = [
                pokemon for pokemon in ctx.my_pokemon_in_play()
                if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)
            ]
            remaining_hp = re.search(r"that has (\d+) hp or less remaining", text)
            if remaining_hp:
                maximum = int(remaining_hp.group(1))
                candidates = [p for p in candidates
                              if p.get_attribute(AttrID.HP, 0) <= maximum]
            attached_type = re.search(
                r"that has any (grass|fire|water|lightning|psychic|fighting|"
                r"darkness|metal|fairy) energy attached", text,
            )
            if attached_type:
                ptype = getattr(PokemonTypes, attached_type.group(1).upper())
                candidates = [p for p in candidates if any(
                    energy_provides_type(card, ptype.value)
                    for card in ctx.attached_energies(p)
                )]
            target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal") \
                if candidates else None
            if target is not None:
                amount = ctx.max_hp(target) if heal_all else int(heal.group(1))
                await ctx.heal(amount, target)
                if "remove all special conditions" in text:
                    await ctx.cure_all_conditions(target)

        # Public discard recovery; an "up to" selection may intentionally fail.
        if "from your discard pile" in text and "into your hand" in text:
            count = _requested_count(text)
            candidates = list(ctx.discard_pile())
            predicate = _search_predicate(text)
            if predicate is not None:
                candidates = [card for card in candidates if predicate(card)]
            picks = await ctx.choose_cards(
                candidates, min(count, len(candidates)),
                minimum=0 if "up to" in text else None,
                prompt="Choose cards from your discard pile",
            ) if candidates else []
            await ctx.put_in_hand(picks, reveal=True)

        discard_match = re.search(r"discard (a|an|another|\d+) (.+?) from your hand", text)
        if discard_match and "you may discard" not in text and not paid_hand_discard:
            raw_count = discard_match.group(1)
            count = 1 if raw_count in {"a", "an", "another"} else int(raw_count)
            descriptor = re.sub(
                r"\s+cards?$", "", discard_match.group(2).strip()
            ).removeprefix("other ")
            await ctx.discard_from_hand(
                count,
                predicate=_hand_discard_predicate(ctx.board, descriptor),
                prompt="Choose cards to discard",
            )

        if "opponent reveals their hand" in text or "opponent reveal their hand" in text:
            revealed = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
            opposing_discard = re.search(
                r"discard (?:up to )?(\d+) (item|energy) cards? "
                r"(?:from it|you find there)", text,
            )
            if opposing_discard:
                count, kind = int(opposing_discard.group(1)), opposing_discard.group(2)
                predicate = is_item_card if kind == "item" else is_energy_card
                candidates = [card for card in revealed if predicate(card)]
                picks = await ctx.choose_cards(
                    candidates, min(count, len(candidates)),
                    minimum=0 if "up to" in opposing_discard.group(0)
                    else min(count, len(candidates)),
                    prompt="Choose cards to discard",
                ) if candidates else []
                await ctx.discard_cards(picks)
            elif "choose a card you find there and put it on the bottom" in text:
                chosen = await _choose_one(ctx, revealed, "Choose a card") \
                    if revealed else None
                if chosen is not None:
                    await ctx.put_on_bottom_of_deck(chosen)
                    if "opponent may draw a card" in text and await ctx.ask_yes_no(
                        "Draw a card?", player_id=ctx.opponent_id
                    ):
                        await ctx.draw_cards(1, player_id=ctx.opponent_id)
            elif "draw 2 cards for each supporter card you find there" in text:
                await ctx.draw_cards(2 * sum(is_supporter_card(c) for c in revealed))
            elif "draw a card for each pokémon you find there" in text:
                await ctx.draw_cards(sum(is_pokemon_card(c) for c in revealed))
            elif "put a basic pokémon you find there onto your opponent's bench" in text:
                basics = [card for card in revealed if is_basic_pokemon(card)]
                chosen = await _choose_one(ctx, basics, "Choose a Basic Pokémon") \
                    if basics else None
                if chosen is not None:
                    await ctx.bench_pokemon(chosen)
                    if "switch in that pokémon to the active spot" in text:
                        await ctx.switch_active(ctx.opponent_id, chosen)

        # ------------------------------------------------------------------
        # Recurring families which are neither searches nor fixed draws.

        # Mill effects (self/opponent/both).  Resolve as one grouped move so
        # all discarded cards share one animation bracket.
        mill = re.search(r"discard the top (\d+) cards? of (.+?) deck", text)
        if mill:
            count, owner_words = int(mill.group(1)), mill.group(2)
            if "each player's" in owner_words:
                await ctx.discard_cards(ctx.deck_top(count, ctx.player_id))
                await ctx.discard_cards(ctx.deck_top(count, ctx.opponent_id))
            else:
                pid = ctx.opponent_id if "opponent" in owner_words else ctx.player_id
                await ctx.discard_cards(ctx.deck_top(count, pid))

        # Variable draw counts printed against visible board state.
        if "draw a card for each of your opponent's benched" in text:
            await ctx.draw_cards(len(ctx.opponent_bench()))
        elif "draw a card for each of your opponent's pokémon in play" in text:
            await ctx.draw_cards(len(ctx.opponent_pokemon_in_play()))
        elif "draw a card for each of your" in text and "pokémon in play" in text:
            # Typed/subtype filtering is intentionally conservative: every
            # matching printed word must be present in the definition/type.
            candidates = ctx.my_pokemon_in_play()
            for word, ptype in (
                ("grass", PokemonTypes.GRASS), ("fire", PokemonTypes.FIRE),
                ("water", PokemonTypes.WATER), ("lightning", PokemonTypes.LIGHTNING),
                ("psychic", PokemonTypes.PSYCHIC), ("fighting", PokemonTypes.FIGHTING),
                ("darkness", PokemonTypes.DARKNESS), ("metal", PokemonTypes.METAL),
                ("dragon", PokemonTypes.DRAGON), ("colorless", PokemonTypes.COLORLESS),
            ):
                if f"your {word} pokémon" in text:
                    candidates = [p for p in candidates if ptype.value in
                                  effective_pokemon_types(ctx.board, p)]
            await ctx.draw_cards(len(candidates))
        elif "draw cards until you have the same number" in text:
            difference = max(0, ctx.hand_size(ctx.opponent_id) - ctx.hand_size())
            if difference:
                await ctx.draw_cards(difference)

        # Active/every-Pokemon healing and condition removal are not covered
        # by the targeted "1 of your Pokemon" branch above.
        active_heal = re.search(
            r"heal (\d+) damage from your active "
            r"(?:(?:grass|fire|water|lightning|psychic|fighting|darkness|"
            r"metal|fairy|dragon|colorless) )?pokémon",
            text,
        )
        if active_heal and ctx.my_active() is not None:
            await ctx.heal(int(active_heal.group(1)), ctx.my_active())
        all_heal = re.search(r"heal (\d+) damage from each pokémon", text)
        if all_heal:
            for pid in ctx.board.player_ids:
                for pokemon in ctx.board.pokemon_in_play(pid):
                    await ctx.heal(int(all_heal.group(1)), pokemon)
        if "remove all special conditions from your active pokémon" in text \
                and ctx.my_active() is not None:
            await ctx.cure_all_conditions(ctx.my_active())
        elif "remove a special condition from your active pokémon" in text \
                and ctx.my_active() is not None:
            active = ctx.my_active()
            conditions = list(active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
            if conditions:
                await ctx.cure_condition(active, conditions[0])

        # Direct Special Conditions from Items/Supporters.
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
            if f"your active pokémon is now {word}" in text:
                target = ctx.my_active()
                if target is not None:
                    await ctx.apply_special_condition(target, condition)

        # Broad switch wording across older templating generations.
        if "switch 1 of your active pokémon with 1 of your benched pokémon" in text \
                and ctx.my_bench():
            target = await ctx.choose_pokemon(
                ctx.my_bench(), "Choose your new Active Pokémon"
            )
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
        if (
            "opponent switches his or her active pokémon" in text
            or "switch out your opponent's active pokémon to the bench" in text
        ) and ctx.opponent_bench():
            bench = _opponent_switch_targets_on_board(
                ctx.board, ctx.player_id, text,
            )
            target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench, "Choose a new Active Pokémon", player_id=ctx.opponent_id
            ) if bench else None
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)

        # Energy and damage movement keeps the physical selected card/counters
        # on the board, rather than resolving through copy dialogs.
        if (
            re.search(r"move (?:a|an|(?:up to )?\d+|any (?:number|amount) of) .*energy", text)
            and (
                "attached" in text
                or "from 1 of your pokémon" in text
            )
            and "energy" in text
            and "another of your pokémon" in text
        ):
            sources = ctx.my_pokemon_in_play()
            targets = ctx.my_pokemon_in_play()
            maximum = re.search(r"move (?:up to )?(\d+)\b", text)
            unlimited = re.search(r"move any (?:number|amount) of\b", text)
            # Missing a numeric digit does not mean unlimited: "a/an Energy"
            # is exactly one physical card (not its provided Energy units).
            limit = int(maximum.group(1)) if maximum else None if unlimited else 1
            await ctx.move_energy_freely(
                sources, targets,
                predicate=is_basic_energy if "basic energy" in text else None,
                max_count=limit,
                single_source=bool(re.search(r"(?:from|attached(?: to)?) 1 of", text)),
                single_destination=True,
                prompt="Choose Energy to move",
            )
        moved_damage = re.search(
            r"move (\d+) damage counters? from 1 of (your|your opponent's) "
            r"pokémon to another", text,
        )
        if moved_damage:
            pool = ctx.my_pokemon_in_play() if moved_damage.group(2) == "your" \
                else ctx.opponent_pokemon_in_play()
            sources = [p for p in pool if p.get_attribute(AttrID.HP, 0)
                       < effective_max_hp(ctx.board, p)]
            source = await ctx.choose_pokemon(sources, "Choose a damaged Pokémon") \
                if sources else None
            targets = [p for p in pool if p is not source]
            target = await ctx.choose_pokemon(targets, "Choose the target Pokémon") \
                if source is not None and targets else None
            if target is not None:
                await ctx.move_damage_counters(
                    source, target, int(moved_damage.group(1))
                )

        # Scoop/shuffle a whole evolution stack.  Which pieces remain together
        # is dictated by the printed destination.
        if "pokémon" in text and "all cards attached to it" in text \
                and "into your hand" in text:
            candidates = list(ctx.my_pokemon_in_play())
            if "basic pokémon" in text:
                candidates = [p for p in candidates if is_basic_pokemon(p)]
            if "damage counters" in text and "that has" in text:
                candidates = [p for p in candidates if p.get_attribute(AttrID.HP, 0)
                              < effective_max_hp(ctx.board, p)]
            target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
                candidates, "Choose a Pokémon"
            ) if candidates else None
            if target is not None:
                await ctx.put_in_hand(full_stack(target), reveal=False)
        if "shuffle 1 of your pokémon and all cards attached to it into your deck" in text:
            candidates = list(ctx.my_pokemon_in_play())
            target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
                candidates, "Choose a Pokémon"
            ) if candidates else None
            if target is not None:
                await ctx.shuffle_into_deck(full_stack(target))

        # Public-zone moves that do not consult a private deck.
        if "special energy" in text and "opponent's pokémon" in text \
                and "lost zone" in text:
            energies = [energy for pokemon in ctx.opponent_pokemon_in_play()
                        for energy in ctx.attached_energies(pokemon)
                        if is_special_energy(energy)]
            chosen = await _choose_one(ctx, energies, "Choose a Special Energy")
            if chosen is not None:
                await ctx.move_to_lost_zone([chosen])
        if "put a card from your opponent's discard pile into their hand" in text:
            chosen = await _choose_one(
                ctx, ctx.discard_pile(ctx.opponent_id), "Choose a card",
                player_id=ctx.player_id,
            )
            if chosen is not None:
                await ctx.put_in_hand([chosen], reveal=True)

        # Temporary damage boosts for the current turn.
        boost = re.search(r"during this turn, your (.+?) attacks do (\d+) more damage", text)
        if boost:
            descriptor, amount = boost.group(1), int(boost.group(2))
            def source_predicate(pokemon):
                if "lightning pokémon's" in descriptor:
                    return PokemonTypes.LIGHTNING.value in effective_pokemon_types(
                        ctx.board, pokemon
                    )
                if "ultra beasts'" in descriptor:
                    return "Ultra Beast" in (getattr(
                        def_for(pokemon.archetype_id), "subtypes", []
                    ) or [])
                return True
            ctx.add_turn_damage_modifier(TurnDamageModifier(
                amount=amount, player_id=ctx.player_id,
                source_predicate=source_predicate,
            ))

    effect.__name__ = "standard_trainer_text_effect"
    # Keep the turn-ending rule on the callable rather than at dozens of
    # early-return sites above.  resolve_trainer_effect applies it after the
    # effect resolves and gives continuous exceptions (Metagross's Extend) a
    # chance to suppress it.
    effect.printed_ends_turn = "your turn ends" in normalized
    # A generated printing may omit an explicit ``condition=`` argument.
    # TrainerCardDef reads this attribute and installs the same conservative
    # public-information gate automatically.
    effect.play_condition = standard_trainer_condition(game_text)
    return effect


def _trainer_rules_text(game_text: str) -> str:
    # HGSS Supporters prepend a card-type reminder. It is not part of the
    # effect: its word "Supporter" must not become a deck-search predicate.
    text = _norm(game_text)
    # A subclass reminder must never become an Item/Supporter search filter.
    text = re.sub(r"you may play as many (?:item|pokémon tool) cards as you like.*$", "", text).strip()
    return re.sub(
        r"^you can play only one supporter card each turn\. when you play this card, "
        r"put it next to your active pokémon\. when your turn ends, discard this card\. ?",
        "", text)


def standard_trainer_condition(game_text: str):
    """Conservative legality checks for generated Trainer implementations.

    Deck contents are private information, so a search Trainer remains legal
    whenever the deck itself is non-empty.  Public-zone and explicit cost
    requirements, on the other hand, are known before the card is played and
    must keep the card out of the action map when they cannot be satisfied.
    """
    text = _trainer_rules_text(game_text)

    def cards(board, player_id: str, area_name: str):
        area = board.find_player_area(player_id, area_name)
        return list(area.children) if area is not None else []

    def condition(board, player_id: str, card=None):
        if card is not None:
            from spirit.game.card_effects.sm_searches import search_permission
            permission = search_permission(board, player_id, _card_name(card))
            if permission is not None:
                return permission
        hand = [entry for entry in cards(board, player_id, "hand") if entry is not card]
        deck = cards(board, player_id, "deck")
        discard = cards(board, player_id, "discard")
        opponent_id = _opponent_id(board, player_id)
        opponent_discard = cards(board, opponent_id, "discard") if opponent_id else []
        opponent_hand = cards(board, opponent_id, "hand") if opponent_id else []
        if text.startswith("choose a pokémon tool or special energy card attached") and "lost zone" in text:
            return bool(_faba_targets(board, player_id))
        if "you can't choose cynthia & caitlin" in text:
            return any(is_supporter_card(c)
                       and _card_name(c).casefold() != "cynthia & caitlin"
                       for c in discard) or bool(hand and deck)
        if "look at the top card of either player's deck" in text:
            return bool(deck or (opponent_id and cards(board, opponent_id, "deck")))
        if text.startswith('you may play 2 puzzle of time cards at once'):
            return bool(deck) or bool(
                any(_card_name(entry).casefold() == 'puzzle of time' for entry in hand)
                and any(entry is not card for entry in discard))
        own_in_play = list(board.pokemon_in_play(player_id))
        opposing_in_play = list(board.pokemon_in_play(opponent_id)) \
            if opponent_id else []
        if text.startswith("remove all effects of attacks on"):
            from spirit.game.session.passives import has_removable_attack_effects
            affected = set(board.player_ids) if "each player" in text else {player_id}
            return has_removable_attack_effects(board, affected)
        own_bench_area = board.find_player_area(player_id, "bench")
        opposing_bench_area = board.find_player_area(opponent_id, "bench") \
            if opponent_id else None
        own_bench = list(own_bench_area.children) if own_bench_area else []
        opposing_bench = list(opposing_bench_area.children) \
            if opposing_bench_area else []

        if "heal 120 damage from the pokémon you moved to your bench" in text:
            return bool(own_bench and board.active_pokemon(player_id))
        if text.startswith("discard 3 cards from the top of each player's deck"):
            return bool(deck or cards(board, opponent_id, "deck")) or (
                len(hand) >= 3 and max(len(own_bench), len(opposing_bench)) > 3)

        # Alternative effects are OR, not cumulative prerequisites.  In
        # particular a recovery option must not disable an available draw.
        if text.startswith("choose 1:") and "put a judge card from your discard pile" in text:
            return bool(deck) or any(_card_name(entry).casefold() == "judge" for entry in discard)

        if re.fullmatch(r"draw (?:a|\d+) cards?\.", text):
            return bool(deck)
        if text.startswith("draw ") and not any(word in text for word in (
            "damage", "heal", "attach", "switch", "shuffle", "discard",
            "search", "reveal", "look", "attacks", "during this turn",
        )) and not deck:
            return False
        # "Up to" permits choosing fewer targets, not playing a pure public
        # recovery with no eligible target at all.  Composite alternatives
        # are deliberately excluded from this anchored pattern.
        public_recovery = re.match(
            r"^(?:put|shuffle) (?:up to )?(?:\d+|an?) "
            r"(.+?) from your discard pile", text,
        )
        if public_recovery:
            predicate = _search_predicate(public_recovery.group(1))
            if not any(predicate(entry) if predicate is not None else True for entry in discard):
                return False
        until = re.match(r"draw cards until you have (\d+) cards in your hand\.", text)
        if until:
            limit = int(until.group(1))
            bonus = re.search(r"if it's your first turn, draw cards until you have (\d+)", text)
            state = getattr(board, "turn_state", None)
            if bonus and state is not None and state.turn_number in (1, 2):
                limit = int(bonus.group(1))
            if not deck or len(hand) >= limit:
                return False
        if "if you can't draw any cards in this way, you can't play this card" in text and not deck:
            return False
        if "only if you have 4 or fewer other cards in your hand" in text:
            if len(hand) > 4 or not deck:
                return False
        stage_gate = re.search(r"only if your opponent's active pokémon is a stage ([12]) pokémon", text)
        if stage_gate:
            active = board.active_pokemon(opponent_id)
            if active is None or active.get_attribute(AttrID.STAGE) != int(stage_gate.group(1)):
                return False
            if "draw" in text and not deck:
                return False
        if "shuffle an electropower card from your discard pile" in text:
            return any(_card_name(entry).casefold() == "electropower" for entry in discard)

        # Searching a non-empty private deck may legally fail even when no
        # matching card is actually present.
        if text.startswith('choose an energy card from your hand') and not any(is_energy_card(c) for c in hand):
            return False
        if text.startswith('choose 1 pokémon in your hand') and not any(is_pokemon_card(c) for c in hand):
            return False
        if 'discard all trainer and stadium cards' in text or 'discard all item and stadium cards' in text:
            stadium_area = board.find_global_area('activeStadium')
            if not (stadium_area is not None and stadium_area.children) and not any(
                    is_item_card(c) for p in own_in_play + opposing_in_play for c in full_stack(p)[1:]):
                return False
        if "search your deck" in text and not deck:
            return False
        if _top_deck_count(text) is not None:
            # The resource belongs to the deck named by the inspection,
            # not necessarily to the player using the Trainer (Hiker/Ice Axe).
            inspected = re.search(
                r"(?:look at|reveal) the top (?:\d+ cards?|card) of "
                r"(your|your opponent's|either player's) deck", text,
            ).group(1)
            opposing_deck = cards(board, opponent_id, "deck") if opponent_id else []
            available = (deck or opposing_deck) if inspected == "either player's" \
                else opposing_deck if inspected == "your opponent's" else deck
            if not available:
                return False

        if text.startswith("choose 1: • put a basic energy card from your discard") \
                and not any(is_basic_energy(entry) for entry in discard):
            return False
        if text.startswith("flip a coin. if heads, choose 1 of your opponent's benched") \
                and not opposing_bench:
            return False
        if text.startswith("flip a coin. if heads, return 1 of your pokémon") \
                and not own_in_play:
            return False
        if text.startswith("flip a coin. if heads, search your discard pile for a pokémon") \
                and not any(is_pokemon_card(entry) or (
                    is_item_card(entry) if "item card" in text else is_trainer_card(entry))
                            for entry in discard):
            return False

        if "can't choose junk arm" in text and not any(
                is_item_card(entry) and _card_name(entry).casefold() != "junk arm"
                for entry in discard):
            return False
        if "search your discard pile for 3 pokémon and 3 basic energy cards" in text:
            return any(is_pokemon_card(entry) or is_basic_energy(entry) for entry in discard)
        if text.startswith("put 2 cards from your hand on the bottom of your deck") \
                and len(hand) < 2:
            return False
        if text.startswith("put a card from your hand on the bottom of your deck") \
                and not hand:
            return False
        if text.startswith("put an energy attached to your opponent's active pokémon into their hand"):
            active = board.active_pokemon(opponent_id) if opponent_id else None
            if active is None or not board.attached_energies(active) \
                    or not any(is_energy_card(entry) for entry in hand):
                return False
        if "search your deck for up to 2 basic energy cards" in text \
                and "your pokémon can't attack" in text and not own_in_play:
            return False
        if "custom catcher cards at once" in text:
            has_second = any(
                _card_name(entry).casefold() == "custom catcher"
                for entry in hand
            )
            return bool(deck and len(hand) < 3) or bool(has_second and opposing_bench)
        if "mixed herbs cards at once" in text:
            active = board.active_pokemon(player_id)
            has_second = any(
                _card_name(entry).casefold() == "mixed herbs"
                for entry in hand
            )
            damaged = active is not None and active.get_attribute(
                AttrID.HP, 0) < effective_max_hp(board, active)
            conditioned = active is not None and bool(
                active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            )
            if not conditioned and not (has_second and damaged):
                return False

        discard_cost = _mandatory_hand_discard_cost(text)
        if discard_cost is not None:
            count, descriptor = discard_cost
            predicate = _hand_discard_predicate(board, descriptor)
            eligible = [entry for entry in hand
                        if predicate is None or predicate(entry)]
            if len(eligible) < count:
                return False
            if "draw a card for each of your opponent's benched pokémon" in text \
                    and (not deck or not opposing_bench):
                return False
            refill = re.search(r"draw cards until you have (\d+) cards in your hand", text)
            if refill and (not deck or len(hand) - count >= int(refill.group(1))):
                return False

        opponent_switch = bool(
            re.search(
                r"switch(?: in)? 1 of your opponent's benched pok.mon",
                text,
            )
            or "switch out your opponent's active pokémon to the bench" in text
            or "opponent switches his or her active pokémon" in text
        )
        own_switch = (
            "switch your active pokémon with 1 of your benched pokémon" in text
            or "switch 1 of your active pokémon with 1 of your benched pokémon" in text
        )
        coin_switch_alternative = (
            "if heads" in text and "if tails" in text
            and opponent_switch and own_switch
        )
        switch_targets = _opponent_switch_targets_on_board(
            board, player_id, text,
        ) if opponent_switch else []
        if opponent_switch and "custom catcher cards at once" not in text \
                and not switch_targets \
                and not (coin_switch_alternative and own_bench):
            return False
        if own_switch and not own_bench \
                and not (text.startswith("choose 1:") and "draw" in text) \
                and not (coin_switch_alternative and switch_targets):
            return False

        if "each player returns 1 of his or her benched pokémon" in text \
                and not own_bench and not opposing_bench:
            return False

        if "discard an energy from 1 of your opponent's pokémon" in text \
                and not any(
                    board.attached_energies(pokemon)
                    for pokemon in opposing_in_play
                ):
            return False

        moves_own_energy = (
            "move" in text and "energy" in text
            and "your pokémon" in text
            and "another of your pokémon" in text
        )
        if moves_own_energy:
            movable = [
                energy for pokemon in own_in_play
                for energy in board.attached_energies(pokemon)
                if "basic energy" not in text or is_basic_energy(energy)
            ]
            if len(own_in_play) < 2 or not movable:
                return False

        if text.startswith("remove all special conditions from your active pokémon"):
            active = board.active_pokemon(player_id)
            if active is None or not active.get_attribute(
                    AttrID.SPECIAL_CONDITIONS):
                return False

        if "put 1 of your pokémon that has any damage counters on it" in text \
                and not any(
                    pokemon.get_attribute(AttrID.HP, 0)
                    < effective_max_hp(board, pokemon)
                    for pokemon in own_in_play
                ):
            return False
        if text.startswith("discard your hand and search your deck") and not hand:
            return False
        if "shuffle a card from your hand into your deck. if you do" in text \
                and not hand:
            return False

        if "top 3 cards of your opponent's deck" in text:
            opponent_deck = cards(board, opponent_id, "deck") if opponent_id else []
            if not opponent_deck:
                return False

        if text.startswith("discard up to 2 of your benched pokémon") and not any(
            pokemon.get_attribute(AttrID.HP, 0) >= effective_max_hp(board, pokemon)
            for pokemon in own_bench
        ):
            return False


        if text.startswith("draw cards until you have the same number") \
                and len(hand) >= len(opponent_hand):
            return False

        if text.startswith("each player puts a pokémon from") \
                or text.startswith("each player puts a pokémon from his or her"):
            if not any(is_pokemon_card(entry)
                       for entry in discard + opponent_discard):
                return False

        if text.startswith("heal 20 damage and remove a special condition"):
            active = board.active_pokemon(player_id)
            if active is None:
                return False
            damaged = active.get_attribute(AttrID.HP, 0) \
                < effective_max_hp(board, active)
            conditioned = bool(active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
            if not damaged and not conditioned:
                return False

        typed_heal = re.search(
            r"heal \d+ damage from (?:each of your|your active) "
            r"(grass|fire|water|lightning|psychic|fighting|darkness|metal|"
            r"fairy|dragon|colorless) pokémon", text,
        )
        if typed_heal:
            ptype = getattr(PokemonTypes, typed_heal.group(1).upper())
            candidates = own_in_play if "each of your" in text else [
                board.active_pokemon(player_id)
            ]
            if not any(
                pokemon is not None
                and ptype.value in effective_pokemon_types(board, pokemon)
                and pokemon.get_attribute(AttrID.HP, 0)
                    < effective_max_hp(board, pokemon)
                for pokemon in candidates
            ):
                return False

        attached_heal = re.search(
            r"heal \d+ damage from (?:each of )?(?:1 of )?your pokémon "
            r"that has any (grass|fire|water|lightning|psychic|fighting|"
            r"darkness|metal|fairy) energy attached", text,
        )
        if attached_heal:
            ptype = getattr(PokemonTypes, attached_heal.group(1).upper())
            if not any(
                pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)
                and any(energy_provides_type(energy, ptype.value)
                        for energy in board.attached_energies(pokemon))
                for pokemon in own_in_play
            ):
                return False

        remaining_heal = re.search(
            r"heal \d+ damage from (?:1 of )?your pokémon that has "
            r"(\d+) hp or less remaining", text,
        )
        if remaining_heal and not any(
            pokemon.get_attribute(AttrID.HP, 0) <= int(remaining_heal.group(1))
            and pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)
            for pokemon in own_in_play
        ):
            return False

        if text.startswith("move up to 3 damage counters from 1 of your opponent's"):
            if len(opposing_in_play) < 2 or not any(
                pokemon.get_attribute(AttrID.HP, 0)
                < effective_max_hp(board, pokemon)
                for pokemon in opposing_in_play
            ):
                return False

        if text.startswith("put 2 cards from your hand in the lost zone") \
                and len(hand) < 2:
            return False

        if "put a basic pokémon from your opponent's discard pile onto" in text:
            if not any(is_basic_pokemon(entry) for entry in opponent_discard):
                return False
            from spirit.game.session.passives import effective_bench_capacity
            if len(opposing_bench) >= effective_bench_capacity(board, opponent_id):
                return False

        if "special energy" in text and "opponent's pokémon" in text \
                and "lost zone" in text and not any(
                    is_special_energy(energy)
                    for pokemon in opposing_in_play
                    for energy in board.attached_energies(pokemon)
                ):
            return False

        if "switch 1 of your opponent's benched mega evolution pokémon" in text \
                and not any("MEGA" in {value.upper() for value in _card_subtypes(p)}
                            for p in opposing_bench):
            return False

        if text.startswith("you can play this card only if there is any stadium"):
            stadium = board.find_global_area("activeStadium")
            if stadium is None or not stadium.children:
                return False

        if "you can play this card only if you discard a darkness pokémon" in text:
            has_cost = any(
                is_pokemon_card(entry)
                and _pokemon_has_type(board, entry, PokemonTypes.DARKNESS)
                for entry in hand
            )
            has_target = bool(_faba_targets(board, player_id))
            if not has_cost or not has_target:
                return False

        if "during this turn, you can play 3 supporter cards" in text \
                or "only if you have more prize cards left than your opponent" in text \
                or "only if you have more prize cards remaining than your opponent" in text:
            own_prizes = cards(board, player_id, "prizePile")
            opposing_prizes = cards(board, opponent_id, "prizePile")
            if len(own_prizes) <= len(opposing_prizes):
                return False

        if text.startswith("you can play this card only if your active pokémon is a water"):
            active = board.active_pokemon(player_id)
            allowed = {PokemonTypes.WATER.value, PokemonTypes.METAL.value}
            if active is None or not allowed.intersection(
                    effective_pokemon_types(board, active)) or len(opposing_bench) <= 2:
                return False

        if "opponent has exactly 3 prize cards remaining" in text:
            if len(cards(board, opponent_id, "prizePile")) != 3:
                return False

        if text.startswith("you can play this card only if your opponent's active pokémon is a basic"):
            active = board.active_pokemon(opponent_id)
            if active is None or not is_basic_pokemon(active) \
                    or not board.attached_energies(active):
                return False

        if "any of your pokémon were knocked out during your opponent's last turn" in text \
                or "1 of your pokémon was knocked out during your opponent's last turn" in text:
            state = getattr(board, "turn_state", None)
            if state is None or not state.pokemon_lost_last_turn(player_id):
                return False

        if "1 of your fairy pokémon was knocked out during your opponent's last turn" in text:
            state = getattr(board, "turn_state", None)
            ledger = state.pokemon_lost_last_turn(player_id) if state else []
            if not any(_definition_has_type(
                    entry.get("archetype_id"), PokemonTypes.FAIRY
            ) for entry in ledger):
                return False

        if "only if you go second, and only on your first turn" in text:
            state = getattr(board, "turn_state", None)
            if state is None or state.turn_number != 2:
                return False

        if "n's darmanitan" in text and "n's zekrom in play" in text:
            names = {_card_name(pokemon).casefold() for pokemon in own_in_play}
            required = {
                "n's darmanitan", "n's zoroark ex", "n's vanilluxe",
                "n's klinklang", "n's reshiram", "n's zekrom",
            }
            if not required.issubset(names):
                return False

        # Public Energy acceleration must have both a card in the named zone
        # and a legal in-play destination.  This catches entire imported
        # families that previously lit up and then did nothing.
        attachment = re.search(
            r"attach (?:(?:up to )?\d+ |an? )?(?:(basic|special) )?"
            r"(?:(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) )?"
            r"energy(?: cards?)? from your (hand|discard pile)", text,
        )
        if attachment:
            qualifier, type_word, zone_name = attachment.groups()
            zone = hand if zone_name == "hand" else discard
            energies = [entry for entry in zone if is_energy_card(entry)]
            if qualifier == "basic":
                energies = [entry for entry in energies if is_basic_energy(entry)]
            elif qualifier == "special":
                energies = [entry for entry in energies if is_special_energy(entry)]
            if type_word:
                ptype = getattr(PokemonTypes, type_word.upper())
                energies = [entry for entry in energies
                            if energy_provides_type(entry, ptype.value)]
            # This is the effect, not an activation cost: attach as many of
            # the printed number as possible (e.g. Blacksmith with one Fire).
            if not energies or not _trainer_energy_targets_on_board(
                    board, player_id, text):
                return False

        if text.startswith("choose 1 of your basic pokémon in play") \
                and "counts as evolving" in text:
            valid = False
            for pokemon in board.pokemon_in_play(player_id):
                if not is_basic_pokemon(pokemon):
                    continue
                logic = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                if any(is_evolution_pokemon(entry)
                       and entry.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic
                       for entry in hand):
                    valid = True
                    break
            if not valid:
                return False

        if "switch it with 1 of your pokémon in play" in text \
                and "any attached cards, damage counters" in text:
            candidates = [entry for entry in discard if is_pokemon_card(entry)]
            targets = list(own_in_play)
            if "basic darkness pokémon" in text:
                candidates = [entry for entry in candidates
                              if is_basic_pokemon(entry)
                              and _pokemon_has_type(board, entry, PokemonTypes.DARKNESS)]
            if 'has "ogerpon" in its name' in text:
                candidates = [entry for entry in candidates
                              if "ogerpon" in _card_name(entry).casefold()
                              and "ex" in _card_subtypes(entry)]
                targets = [entry for entry in targets
                           if "ogerpon" in _card_name(entry).casefold()
                           and "ex" in _card_subtypes(entry)]
            if not candidates or not targets:
                return False

        if text.startswith("devolve 1 of your evolved") and not any(
                is_evolution_pokemon(pokemon)
                for pokemon in board.pokemon_in_play(player_id)):
            return False

        if text.startswith("discard a card from your hand. if you do") and not hand:
            return False
        if "discard dana, evelyn, and nita from your hand" in text:
            names = {_card_name(entry).lower() for entry in hand}
            if not {"dana", "evelyn", "nita"}.issubset(names):
                return False

        if text.startswith("discard any stadium card in play") and "if you do" in text:
            if not any(is_stadium_card(c) for c in _faba_targets(board, player_id)):
                return False

        if text.startswith("discard an energy attached to your opponent's active"):
            active = board.active_pokemon(opponent_id) if opponent_id else None
            if active is None or not board.attached_energies(active):
                return False

        if "discard a special energy from each of your opponent's pokémon" in text:
            if not any(
                is_special_energy(energy)
                for pokemon in board.pokemon_in_play(opponent_id)
                for energy in board.attached_energies(pokemon)
            ):
                return False

        if "discard all pokémon tools and special energy" in text:
            stadium = board.find_global_area("activeStadium")
            if not any(
                is_pokemon_tool(card) or is_special_energy(card)
                for pokemon in board.pokemon_in_play(opponent_id)
                for card in full_stack(pokemon)[1:]
            ) and not (stadium and stadium.children):
                return False

        if "pokémon tool cards attached to your pokémon" in text \
                and "into your hand" in text:
            if not any(
                is_pokemon_tool(card)
                for pokemon in board.pokemon_in_play(player_id)
                for card in full_stack(pokemon)[1:]
            ):
                return False

        if "move an energy from 1 of your benched pokémon to your active" in text:
            bench = board.find_player_area(player_id, "bench")
            if not any(board.attached_energies(pokemon)
                       for pokemon in (bench.children if bench else [])):
                return False

        if "move up to 2 energy from 1 of your tag team pokémon" in text:
            if len(own_in_play) < 2 or not any(
                "tag team" in _card_subtypes(pokemon)
                and board.attached_energies(pokemon)
                for pokemon in own_in_play
            ):
                return False

        if "move a special energy from 1 of your opponent's pokémon" in text:
            opposing = list(board.pokemon_in_play(opponent_id))
            if len(opposing) < 2 or not any(
                is_special_energy(energy) for pokemon in opposing
                for energy in board.attached_energies(pokemon)
            ):
                return False

        if "put an energy attached to 1 of your opponent's pokémon into their hand" in text:
            if not any(board.attached_energies(pokemon)
                       for pokemon in board.pokemon_in_play(opponent_id)):
                return False

        if "return any stadium card in play" in text:
            stadium = board.find_global_area("activeStadium")
            if stadium is None or not stadium.children:
                return False

        if "put a card from your opponent's discard pile" in text \
                and not opponent_discard:
            return False

        if text.startswith("shuffle 3 pokémon tool cards from your discard pile") \
                and not any(is_pokemon_tool(entry) for entry in discard):
            return False

        if text.startswith("put a pokémon from your discard pile on top of your deck") \
                and not any(is_pokemon_card(entry) for entry in discard):
            return False

        if text.startswith("attach a basic energy card from your discard pile to 1 of your mega"):
            has_energy = any(is_basic_energy(entry) for entry in discard)
            has_target = any(
                "MEGA" in (getattr(def_for(pokemon.archetype_id), "subtypes", []) or [])
                for pokemon in board.pokemon_in_play(player_id)
            )
            if not has_energy or not has_target:
                return False

        if text.startswith("attach 2 fire energy cards from your discard pile"):
            has_energy = any(
                is_energy_card(entry)
                and energy_provides_type(entry, PokemonTypes.FIRE.value)
                for entry in discard
            )
            has_target = any(
                PokemonTypes.FIRE.value in effective_pokemon_types(board, pokemon)
                for pokemon in board.pokemon_in_play(player_id)
            )
            if not has_energy or not has_target:
                return False

        if text.startswith("discard all pokémon tool cards attached to each of your opponent's"):
            if not any(
                is_pokemon_tool(attachment)
                for pokemon in board.pokemon_in_play(opponent_id)
                for attachment in getattr(pokemon, "children", [])
            ):
                return False

        if text.startswith("choose a pokémon tool or special energy card attached"):
            if not any(
                is_pokemon_tool(attachment) or is_special_energy(attachment)
                for pid in board.player_ids
                for pokemon in board.pokemon_in_play(pid)
                for attachment in getattr(pokemon, "children", [])
            ):
                return False

        if text.startswith("put 1 pokémon into your hand. (discard all cards attached") \
                and not board.pokemon_in_play(player_id):
            return False

        if text.startswith("each player shuffles all cards in his or her discard pile") \
                and not discard and not opponent_discard:
            return False

        # Max Elixir / Electric Generator style Items need a publicly valid
        # attachment destination.  The presence of a matching Energy in the
        # inspected cards remains private and deliberately is not checked.
        if "look at the top" in text and "attach" in text and "energy" in text:
            candidates = list(board.pokemon_in_play(player_id))
            if "on your bench" in text or "to your benched" in text:
                bench = board.find_player_area(player_id, "bench")
                candidates = list(bench.children) if bench is not None else []
            if "basic pokémon on your bench" in text:
                candidates = [pokemon for pokemon in candidates
                              if is_basic_pokemon(pokemon)]
            typed_target = re.search(
                r"benched (grass|fire|water|lightning|psychic|fighting|darkness|"
                r"metal|fairy|dragon|colorless) pokémon",
                text,
            )
            if typed_target:
                pokemon_type = getattr(
                    PokemonTypes, typed_target.group(1).upper(), None
                )
                if pokemon_type is not None:
                    candidates = [
                        pokemon for pokemon in candidates
                        if pokemon_type.value in (
                            pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
                        )
                    ]
            if not candidates:
                return False

        cost = re.search(
            r"discard (\d+) (?:other )?cards? from your hand (?:in order|to) ",
            text,
        )
        if cost and len(hand) < int(cost.group(1)):
            return False
        if "you can use this card only if it is the last card in your hand" in text \
                and hand:
            return False

        if "switch your active water pokémon" in text:
            active = board.active_pokemon(player_id)
            if active is None or PokemonTypes.WATER.value not in \
                    effective_pokemon_types(board, active) or not own_bench:
                return False

        legacy_heal = 'remove' in text and 'damage counters' in text and 'your pokémon' in text
        if ("heal" in text and "your pokémon" in text) or legacy_heal:
            if not any(
                int(pokemon.get_attribute(AttrID.HP, 0) or 0)
                < effective_max_hp(board, pokemon)
                or (
                    "special condition" in text
                    and bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
                )
                for pokemon in board.pokemon_in_play(player_id)
            ):
                return False

        if "from your discard pile" in text or "search your discard pile" in text:
            search_clause = re.search(r"search your discard pile for (.+?)(?:\.|,|$)", text)
            attach_clause = re.search(r"attach (.+?) from your discard pile", text)
            # Recipient subtypes and ACE SPEC reminders do not describe the
            # discarded Energy (Reboot Pod: a Basic Energy, not a Future ACE SPEC).
            descriptor = attach_clause.group(1) if attach_clause else \
                search_clause.group(1) if search_clause else text
            predicate = _search_predicate(descriptor)
            candidates = [entry for entry in discard
                          if predicate is None or predicate(entry)]
            if attach_clause and not _trainer_energy_targets_on_board(board, player_id, text):
                return False
            if not candidates and "up to" not in text:
                return False
        return True

    condition.__name__ = "standard_trainer_text_condition"
    return condition


def standard_stadium_ability(game_text: str):
    """Return a clickable once-per-turn Stadium Ability when text calls for it."""
    text = _norm(game_text)
    if not (
        "once during each player's turn" in text
        or "once during your turn" in text
        or "once during the turn of the player" in text
    ):
        return None
    from spirit.game.card_effects.trainer_followup import healing_stadium_ability
    if "heal 10 damage from each of their pokémon" in text \
            and "their turn ends" in text:
        return healing_stadium_ability(game_text, 10, all_targets=True, end_turn=True)
    if "heal 30 damage from each of his or her water pokémon and lightning pokémon" in text:
        return healing_stadium_ability(
            game_text, 30, (PokemonTypes.WATER.value, PokemonTypes.LIGHTNING.value),
            all_targets=True)
    if "heal 60 damage and remove all special conditions from 1 of their grass pokémon" in text:
        return healing_stadium_ability(game_text, 60, (PokemonTypes.GRASS.value,), cure=True)
    if "active pokémon is asleep" in text and "heal 30 damage" in text:
        return healing_stadium_ability(game_text, 30, requires_sleep=True)
    from spirit.game.card_effects.sm_stadiums import stadium_effect_for_text
    return Ability(
        title="Stadium Effect",
        game_text=game_text,
        activation=Activations.ONCE_PER_TURN,
        effect=stadium_effect_for_text(game_text) or standard_ability,
    )


def standard_trigger(game_text: str):
    """Infer an engine trigger for recurring Ability/Tool wording."""
    from spirit.game.data_utils import Triggers

    text = _norm(game_text)
    if re.search(r"(?:when you )?discard this pokémon with the effect of", text) \
            or "this pokémon is discarded with the effect of" in text \
            or "this pokémon is discarded from your hand by an effect" in text:
        return Triggers.ON_DISCARDED_FROM_HAND
    if "this pokémon is discarded from your deck by an effect" in text:
        return Triggers.ON_DISCARDED
    if "took this pokémon as a face-down prize card" in text:
        return Triggers.ON_TAKEN_AS_PRIZE
    if (
        "when you play this pokémon from your hand onto your bench" in text
        or re.search(r"when you (?:put|play) .+ from your hand (?:onto|to) your bench", text)
        or "when you put lugia legend into play" in text
    ):
        return Triggers.ON_PLAY
    if (
        "when you play this pokémon from your hand to evolve" in text
        or re.search(r"when you play .+ from your hand to evolve", text)
    ):
        return Triggers.ON_EVOLVE
    if "when this pokémon is knocked out" in text:
        return Triggers.ON_KNOCKED_OUT
    if "damaged by an attack" in text and (
        "attacking pokémon" in text or "when this pokémon" in text
    ):
        return Triggers.ON_DAMAGED_BY_ATTACK
    if "whenever" in text and "attaches an energy" in text:
        return Triggers.ON_ENERGY_ATTACHED
    if "when you attach" in text and "energy card from your hand" in text:
        return Triggers.ON_ENERGY_ATTACHED
    if "moves from the active spot to the bench" in text:
        return Triggers.ON_MOVE_TO_BENCH
    if "moves to the active spot" in text or \
            "moves from your bench to the active spot" in text:
        return Triggers.ON_MOVE_TO_ACTIVE
    if "at the end of your turn" in text or "at the end of each player's turn" in text:
        return Triggers.END_OF_TURN
    if "between turns" in text or "during pokémon checkup" in text:
        return Triggers.BETWEEN_TURNS
    return None


def standard_activation(game_text: str):
    text = _norm(game_text)
    if "as often as you like during your turn" in text \
            or "at any time during your turn" in text:
        return Activations.UNLIMITED
    if "once during your turn" in text \
            or "once during your first turn" in text:
        return Activations.ONCE_PER_TURN
    return None


async def standard_energy_on_attach(ctx):
    """Recurring Special Energy attachment effects for generated cards."""
    definition = getattr(ctx, "definition", None)
    text = _norm(getattr(definition, "game_text", ""))
    # Generated definitions currently store the text on this callback so the
    # hook remains stateless per physical Energy card.
    text = _norm(getattr(standard_energy_on_attach, "game_text", text))
    draw = re.search(r"when you attach this card.*draw (\d+) cards", text)
    if draw:
        await ctx.draw_cards(int(draw.group(1)))


def energy_on_attach(game_text: str):
    text = _norm(game_text)

    async def effect(ctx):
        draw = re.search(r"when you attach this card.*draw (\d+) cards", text)
        if draw:
            await ctx.draw_cards(int(draw.group(1)))
        heal = re.search(r"when you attach this card.*heal (\d+) damage", text)
        if heal and ctx.attached_to is not None:
            await ctx.heal(int(heal.group(1)), ctx.attached_to)
        if "when you attach this card" in text \
                and "put 1 damage counter on that pokémon" in text \
                and ctx.attached_to is not None:
            await ctx.deal_damage(
                10, target=ctx.attached_to, is_attack=False, as_counters=True
            )
        if ctx.attached_to is not None and "recovers from being asleep, confused, or paralyzed" in text:
            for condition in (
                SpecialConditions.ASLEEP,
                SpecialConditions.CONFUSED,
                SpecialConditions.PARALYZED,
            ):
                await ctx.cure_condition(ctx.attached_to, condition)
        if ctx.attached_to is not None \
                and "attach this card from your hand to 1 of your benched pokémon" in text \
                and "switch that pokémon with your active pokémon" in text:
            if ctx.attached_to in ctx.my_bench():
                await ctx.switch_active(ctx.player_id, ctx.attached_to)
        if ctx.attached_to is not None \
                and "attach this card from your hand to your active pokémon" in text \
                and "switch that pokémon with 1 of your benched pokémon" in text:
            active = ctx.board.active_pokemon(ctx.player_id)
            bench = ctx.my_bench()
            if active is ctx.attached_to and bench:
                chosen = await ctx.choose_cards(
                    bench, 1, prompt="Choose a new Active Pokémon"
                )
                if chosen:
                    await ctx.switch_active(ctx.player_id, chosen[0])

    effect.__name__ = "standard_energy_on_attach"
    return effect


def energy_attach_to(game_text: str):
    """Target predicate for type/team-restricted Special Energy."""
    text = _norm(game_text)
    type_match = re.search(
        r"can only be attached to (grass|fire|water|lightning|psychic|"
        r"fighting|darkness|metal|fairy|dragon) pokémon",
        text,
    )
    team_match = re.search(r"can only be attached to team (aqua|magma) pokémon", text)

    def predicate(pokemon):
        if type_match:
            pokemon_type = getattr(PokemonTypes, type_match.group(1).upper(), None)
            return pokemon_type is not None and pokemon_type.value in (
                pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            )
        if team_match:
            definition = def_for(pokemon.archetype_id)
            label = f"Team {team_match.group(1).title()}"
            return label in (getattr(definition, "subtypes", []) or [])
        return True

    predicate.__name__ = "standard_energy_attach_target"
    return predicate


async def splash_energy_on_ko(ctx):
    """Return Splash Energy's Knocked Out Water Pokemon to its owner's hand."""
    pokemon = getattr(ctx, "knocked_out_pokemon", None)
    if pokemon is None:
        return
    stack = getattr(ctx, "knocked_out_stack", None) or [pokemon]
    evolution_cards, _ = split_pokemon_stack(pokemon, stack)
    discard = ctx.discard_pile(ctx.player_id)
    await ctx.put_in_hand(
        [card for card in evolution_cards if card in discard], reveal=False
    )
