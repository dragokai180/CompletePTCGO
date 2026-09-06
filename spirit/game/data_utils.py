import importlib.util
import json
import os
import uuid
from typing import Any, Callable, Optional, List, Dict
from spirit.game.attributes import AttrID, CardType, TrainerType, PokemonStage, PokemonTypes, ProductType, AbilityTypes, Rarities, CLIENT_POKEMON_TYPE_NAMES, FoilMasks, FoilEffects
from spirit.game.text_encoding import fix_mojibake, fix_mojibake_list, with_ascii_aliases

_ABILITY_ID_NAMESPACE = uuid.UUID("a3f2c6e8-9d41-4d7a-8b5f-2e7c90d13a64")
_REPRINT_GUID_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_DNS, "spiritptcgo.card.reprint")
_SIBLING_CARD_CACHE: Dict[str, "CardDefinition"] = {}


def ability_id_for(card_guid: str, slot: int) -> str:
    """Deterministic GUID for a card's ability/attack slot (must be a GUID: the client runs new Guid(id))."""
    return str(uuid.uuid5(_ABILITY_ID_NAMESPACE, f"{card_guid}:ability:{slot}"))


def reprint_guid(set_code: str, collector_number: int, base_guid: str) -> str:
    """Stable GUID for an alternate printing of an existing card."""
    return str(uuid.uuid5(
        _REPRINT_GUID_NAMESPACE,
        f"{set_code.upper()}:{int(collector_number)}:{base_guid.lower()}",
    ))


def sibling_card(caller_file: str, sibling_filename: str) -> "CardDefinition":
    """Load `card` from another script in the same set folder (for reprint stubs)."""
    path = os.path.join(os.path.dirname(os.path.abspath(caller_file)), sibling_filename)
    cached = _SIBLING_CARD_CACHE.get(path)
    if cached is not None:
        return cached
    if not os.path.isfile(path):
        raise FileNotFoundError(f"sibling card script not found: {path}")
    module_name = f"_sibling_card_{abs(hash(path))}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"could not load sibling card script: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "card"):
        raise AttributeError(f"{sibling_filename} does not define card")
    _SIBLING_CARD_CACHE[path] = module.card
    return module.card


def _clone_ability(ability: "Ability") -> "Ability":
    """Copy an Ability/Attack, sharing effect callables; clears ability_id."""
    if isinstance(ability, Attack):
        clone: Ability = Attack(
            title=ability.title,
            game_text=ability.game_text,
            cost=dict(ability.cost),
            damage=ability.damage,
            damage_operator=ability.damage_operator,
            ability_type=ability.ability_type,
            effect=ability.effect,
            vstar=ability.vstar,
            locks_next_turn=ability.locks_next_turn,
            condition=ability.condition,
            usable_first_turn=ability.usable_first_turn,
            usable_despite_conditions=ability.usable_despite_conditions,
        )
    else:
        clone = Ability(
            title=ability.title,
            game_text=ability.game_text,
            ability_type=ability.ability_type,
            effect=ability.effect,
            trigger=ability.trigger,
            activation=ability.activation,
            vstar=ability.vstar,
            passive=ability.passive,
            condition=ability.condition,
            shared_once_per_turn=ability.shared_once_per_turn,
            ends_turn=ability.ends_turn,
            usable_from=ability.usable_from,
        )
    clone.is_granted = ability.is_granted
    return clone


def _attr_value(definition: "CardDefinition", attr_id: AttrID, default: Any = None) -> Any:
    spec = definition.extra_attributes.get(str(attr_id.value))
    if not isinstance(spec, dict):
        return default
    return spec.get("value", default)


def reprint(
    base: "CardDefinition",
    *,
    collector_number: int,
    rarity: Optional[int] = None,
    guid: Optional[str] = None,
    set_code: Optional[str] = None,
    key: Optional[str] = None,
    regulation_mark: Optional[str] = None,
) -> "CardDefinition":
    """Another printing of `base`: new GUID / collector number / rarity, same mechanics.

    Same-set secret rares omit `set_code`. Cross-set reprints (e.g. Ultra Ball
    in a later format) pass the new set as `set_code`/`key`.

    Pair each reprint with matching art:
      spirit/assets/cards/<SET>/<SameStem>_<collector_number>.png
    and a thin stub script of the same basename that calls this helper.
    """
    new_set = set_code if set_code is not None else base.set_code
    new_key = key if key is not None else (set_code if set_code is not None else base.key)
    new_reg = regulation_mark if regulation_mark is not None else base.regulation_mark
    new_guid = guid or reprint_guid(new_set, collector_number, base.guid)
    new_rarity = base.rarity if rarity is None else rarity
    abilities = [_clone_ability(a) for a in getattr(base, "abilities", []) or []]

    if isinstance(base, PokemonCardDef):
        types_raw = json.loads(_attr_value(base, AttrID.POKEMON_TYPES, "[]") or "[]")
        weak_raw = json.loads(_attr_value(base, AttrID.WEAKNESS_TYPES, "[]") or "[]")
        evolves_raw = _attr_value(base, AttrID.EVOLVES_FROM)
        evolves_from = None
        if isinstance(evolves_raw, str) and evolves_raw.startswith("{"):
            try:
                evolves_from = json.loads(evolves_raw).get("id")
            except Exception:
                evolves_from = None
        return PokemonCardDef(
            guid=new_guid,
            key=new_key,
            name=base.name,
            collector_number=collector_number,
            set_code=new_set,
            rarity=new_rarity,
            hp=int(_attr_value(base, AttrID.HP, 0) or 0),
            elements=[PokemonTypes(t) for t in types_raw],
            stage=PokemonStage(int(_attr_value(base, AttrID.STAGE, 0) or 0)),
            retreat_cost=int(_attr_value(base, AttrID.RETREAT_COST, 1) or 1),
            weakness_type=PokemonTypes(weak_raw[0]) if weak_raw else PokemonTypes.UNSET,
            weakness_amount=int(_attr_value(base, AttrID.WEAKNESS_AMOUNT, 2) or 2),
            resistance_type=PokemonTypes(int(_attr_value(base, AttrID.RESISTANCE_TYPES, PokemonTypes.UNSET.value))),
            resistance_amount=int(_attr_value(base, AttrID.RESISTANCE_AMOUNT, 30) or 30),
            evolves_from=evolves_from,
            family_id=_attr_value(base, AttrID.FAMILY_ID),
            abilities=abilities,
            display_name=base.display_name,
            searchable_by=list(base.searchable_by or []),
            subtypes=list(base.subtypes or []),
            regulation_mark=new_reg,
            passive=getattr(base, "passive", None),
            unplayable_from_hand=bool(getattr(base, "unplayable_from_hand", False)),
            setup_as_active=bool(getattr(base, "setup_as_active", False)),
        )

    if isinstance(base, TrainerCardDef):
        trainer_type = TrainerType(int(_attr_value(base, AttrID.TRAINER_TYPE, TrainerType.ITEM.value)))
        kwargs = dict(
            guid=new_guid,
            key=new_key,
            name=base.name,
            collector_number=collector_number,
            set_code=new_set,
            rarity=new_rarity,
            trainer_type=trainer_type,
            effect=getattr(base, "effect", None),
            condition=getattr(base, "condition", None),
            abilities=abilities,
            display_name=base.display_name,
            searchable_by=list(base.searchable_by or []),
            subtypes=list(base.subtypes or []),
            regulation_mark=new_reg,
        )
        if isinstance(base, FossilItemCardDef):
            return FossilItemCardDef(
                hp=int(_attr_value(base, AttrID.HP, 0) or 0),
                passive=getattr(base, "passive", None),
                **{k: v for k, v in kwargs.items() if k != "trainer_type"},
            )
        if isinstance(base, StadiumCardDef):
            return StadiumCardDef(
                passive=getattr(base, "passive", None),
                ability=getattr(base, "ability", None),
                companion=getattr(base, "companion", None),
                **{k: v for k, v in kwargs.items() if k != "trainer_type"},
            )
        if isinstance(base, PokemonToolCardDef):
            return PokemonToolCardDef(
                **{k: v for k, v in kwargs.items() if k != "trainer_type"},
                passive=getattr(base, "passive", None),
                granted_abilities=[
                    _clone_ability(a) for a in getattr(base, "granted_abilities", []) or []
                ],
                attach_to=getattr(base, "attach_to", None),
            )
        if isinstance(base, ItemCardDef):
            return ItemCardDef(**{k: v for k, v in kwargs.items() if k != "trainer_type"})
        if isinstance(base, SupporterCardDef):
            return SupporterCardDef(**{k: v for k, v in kwargs.items() if k != "trainer_type"})
        return TrainerCardDef(**kwargs)

    if isinstance(base, EnergyCardDef):
        energy_info = json.loads(_attr_value(base, AttrID.ENERGY_INFO, '{"options": []}') or '{"options": []}')
        options = energy_info.get("options") or [[PokemonTypes.COLORLESS.value]]
        provides = [[PokemonTypes(t) for t in option] for option in options]
        types_raw = json.loads(_attr_value(base, AttrID.POKEMON_TYPES, "[]") or "[]")
        energy_type = PokemonTypes(types_raw[0]) if types_raw else PokemonTypes.COLORLESS
        return EnergyCardDef(
            guid=new_guid,
            key=new_key,
            name=base.name,
            collector_number=collector_number,
            set_code=new_set,
            rarity=new_rarity,
            energy_type=energy_type,
            is_special=bool(_attr_value(base, AttrID.IS_SPECIAL_ENERGY, False)),
            provides=provides,
            attach_to=getattr(base, "attach_to", None),
            discard_if_invalid=getattr(base, "discard_if_invalid", False),
            attach_condition=getattr(base, "attach_condition", None),
            attach_cost=getattr(base, "attach_cost", None),
            on_attach=getattr(base, "on_attach", None),
            on_carrier_knocked_out=getattr(base, "on_carrier_knocked_out", None),
            on_discarded_by_carrier_attack=getattr(
                base, "on_discarded_by_carrier_attack", None),
            passive=getattr(base, "passive", None),
            granted_abilities=[
                _clone_ability(a) for a in getattr(base, "granted_abilities", []) or []
            ],
            display_name=base.display_name,
            searchable_by=list(base.searchable_by or []),
            subtypes=list(base.subtypes or []),
            regulation_mark=new_reg,
        )

    raise TypeError(f"reprint() unsupported for {type(base).__name__}")


class _Unimplemented:
    """Marker for card text whose effect has not been scripted yet."""
    def __repr__(self):
        return "unimplemented"

unimplemented = _Unimplemented()

# ability_id -> Ability/Attack definition, filled by PokemonCardDef; the game
# session resolves an attack reply's actionID through this map.
ABILITIES_BY_ID: Dict[str, "Ability"] = {}

# archetype guid (lowercase) -> trainer effect coroutine, filled by
# TrainerCardDef; trainers have no PIE_ABILITIES slot to hang effects on.
TRAINER_EFFECTS_BY_GUID: Dict[str, Any] = {}

# archetype guid (lowercase) -> CardDefinition, filled by every CardDefinition;
# the session engine reads behavior (passives, conditions, subtypes) off it.
CARD_DEFS_BY_GUID: Dict[str, "CardDefinition"] = {}


def def_for(archetype_id: Optional[str]) -> Optional["CardDefinition"]:
    """The CardDefinition behind an entity's archetype GUID, if scripted."""
    return CARD_DEFS_BY_GUID.get((archetype_id or "").lower())


def subtypes_for(archetype_id: Optional[str]) -> List[str]:
    definition = def_for(archetype_id)
    return definition.subtypes if definition else []


def is_prism_star(archetype_id) -> bool:
    return "Prism Star" in subtypes_for(archetype_id)


def discard_area_name(archetype_id) -> str:
    """Where a card goes when it would be discarded.

    Prism Star rule: "If a Prism Star card would go to the discard pile, put
    it in the Lost Zone instead." Every path that discards has to ask, not
    just the scripted effects -- a Stadium replaced by the next one is moved
    by the executor directly.
    """
    return "lostZone" if is_prism_star(archetype_id) else "discard"


# Rule-box subtypes and the prizes an attacker takes for knocking one out.
# "EX" is the XY-era uppercase rule box; "ex" is the SV-era lowercase rule box.
# "MEGA" is XY Mega Evolution; "SV_Mega" is Mega Evolution Pokémon ex (3 prizes).
_MULTI_PRIZE_SUBTYPES = {
    "V": 2, "VSTAR": 2, "V-UNION": 3, "VMAX": 3, "GX": 2, "EX": 2, "ex": 2,
    "SV_Mega": 3,
}
_RULE_BOX_SUBTYPES = set(_MULTI_PRIZE_SUBTYPES) | {"Radiant"}


def is_pokemon_v(archetype_id: Optional[str]) -> bool:
    """Pokemon V of any kind (V, VSTAR, VMAX, V-UNION)."""
    return any(s in ("V", "VSTAR", "VMAX", "V-UNION") for s in subtypes_for(archetype_id))


def is_pokemon_ex(archetype_id: Optional[str]) -> bool:
    """Pokemon-ex of either era (lowercase SV "ex" or uppercase XY "EX")."""
    return any(s in ("ex", "EX") for s in subtypes_for(archetype_id))


def has_rule_box(archetype_id: Optional[str]) -> bool:
    return any(s in _RULE_BOX_SUBTYPES for s in subtypes_for(archetype_id))


def prize_value(archetype_id: Optional[str]) -> int:
    """Prizes taken when this Pokemon is knocked out."""
    return max(
        [_MULTI_PRIZE_SUBTYPES[s] for s in subtypes_for(archetype_id)
         if s in _MULTI_PRIZE_SUBTYPES],
        default=1,
    )


def _string_attr(definition: Optional["CardDefinition"], attr_id: AttrID) -> Optional[str]:
    spec = definition.extra_attributes.get(str(attr_id.value)) if definition else None
    return spec.get("value") if isinstance(spec, dict) else None


# EVOLUTION_LOGIC_NAME -> CardDefinition index, rebuilt lazily when new card
# scripts register (reprints share a name; any def in the line works).
_LOGIC_NAME_INDEX: Dict[str, "CardDefinition"] = {}
_LOGIC_NAME_INDEX_SIZE = -1


def evolves_from_chain(archetype_id: Optional[str]) -> List[str]:
    """EVOLUTION_LOGIC_NAME lineage below a card, direct pre-evolution first
    (Blastoise -> ["Wartortle", "Squirtle"]), walking EVOLUTION_LOGIC_FROM."""
    global _LOGIC_NAME_INDEX_SIZE
    if _LOGIC_NAME_INDEX_SIZE != len(CARD_DEFS_BY_GUID):
        _LOGIC_NAME_INDEX.clear()
        for d in CARD_DEFS_BY_GUID.values():
            logic_name = _string_attr(d, AttrID.EVOLUTION_LOGIC_NAME)
            if logic_name:
                _LOGIC_NAME_INDEX.setdefault(logic_name, d)
        _LOGIC_NAME_INDEX_SIZE = len(CARD_DEFS_BY_GUID)
    chain: List[str] = []
    definition = def_for(archetype_id)
    for _ in range(8):  # depth cap doubles as a cycle guard
        from_name = _string_attr(definition, AttrID.EVOLUTION_LOGIC_FROM)
        if not from_name or from_name in chain:
            break
        chain.append(from_name)
        definition = _LOGIC_NAME_INDEX.get(from_name)
    return chain


def evolves_from(archetype_id: Optional[str], base_logic_name: str) -> bool:
    """Whether a card's evolution line includes `base_logic_name` anywhere
    below it (Rare Candy: Stage2 over a Basic two steps down)."""
    return base_logic_name in evolves_from_chain(archetype_id)


class Triggers:
    """Events the game session fires scripted abilities on (Ability.trigger)."""
    ON_PLAY = "on_play"  # the Pokemon is played from hand onto the bench
    ON_EVOLVE = "on_evolve"  # the Pokemon evolves into this card
    ON_KNOCKED_OUT = "on_knocked_out"  # this Pokemon is Knocked Out
    BETWEEN_TURNS = "between_turns"  # fires on every Pokemon Checkup
    # An opponent's attack damaged this Pokemon (Rocky Helmet); the trigger
    # ctx carries damaged_by / damage_amount / pre_hit_hp.
    ON_DAMAGED_BY_ATTACK = "on_damaged_by_attack"
    # Either player manually attached an Energy from hand (Arctozolt); ctx
    # carries attaching_player_id / attached_energy / energy_receiver.
    ON_ENERGY_ATTACHED = "on_energy_attached"
    # This Pokemon moved into the Active spot (Cinderace Libero); fires at
    # most once per entity per turn.
    ON_MOVE_TO_ACTIVE = "on_move_to_active"
    # Another of the owner's Pokemon was Knocked Out (Exp. Share); fires
    # BEFORE the KO'd stack moves (energies still attached); ctx carries
    # ko_pokemon / ko_from_attack / ko_attacker.
    ON_ALLY_KNOCKED_OUT = "on_ally_knocked_out"
    # Either player manually put a Basic from hand onto their Bench (Gapejaw
    # Bog); ctx carries benching_player_id / benched_pokemon.
    ON_POKEMON_BENCHED = "on_pokemon_benched"
    # This card was drawn by the beginning-of-turn draw (Lombre "Top Entry");
    # fires after the card lands in hand (approximation of "before you put it
    # into your hand").
    ON_TURN_DRAWN = "on_turn_drawn"
    # This card was just taken as a face-down Prize into hand (Dream Ball).
    ON_TAKEN_AS_PRIZE = "on_taken_as_prize"
    # Another of the owner's Pokemon evolved via a hand-played evolution card
    # (Eevee "Resonant Evolution"); ctx carries evolved_pokemon / evolved_from.
    ON_ALLY_EVOLVED = "on_ally_evolved"
    # Fires for each of the turn player's in-play Pokemon after their turn
    # ends, before the checkup (Radiant Venusaur "Sunny Bloom").
    END_OF_TURN = "end_of_turn"
    # This card was discarded from its owner's hand by an OPPOSING player's
    # effect (Amoonguss "Surprise Spores"); fires via the acting ctx's
    # deferred_actions, after that effect's choreography flushes.
    ON_DISCARDED_FROM_HAND = "on_discarded_from_hand"


class Activations:
    """How a non-triggered ability is used (Ability.activation)."""
    ONCE_PER_TURN = "once_per_turn"  # offered as a selectable action, once per turn
    # Usable any number of times per turn; MUST pair with a condition= that
    # gates no-op uses, or the offer never disappears.
    UNLIMITED = "unlimited"

# PIE_ABILITIES abilityType doubles as the JsonFx type hint: it must be a
# PieAbilityDescription subclass CLASS NAME (DwdModelAnalyzer.TypeHintedClasses
# is keyed by type.Name; an int crashes archetype deserialization at login).
ABILITY_TYPE_HINTS = {
    AbilityTypes.ATTACK: "Attack",
    AbilityTypes.NON_DAMAGING_ATTACK: "Attack",
    AbilityTypes.POKE_ABILITY: "PokeAbility",
    AbilityTypes.POKE_POWER: "PokePower",
    AbilityTypes.POKE_BODY: "PokeBody",
    AbilityTypes.TECHNICAL_MACHINE: "TechnicalMachine",
    AbilityTypes.ANCIENT_TRAIT: "AncientTrait",
}

class Ability:
    """Represents a Pokemon Ability (Poke-Power, Poke-Body, etc.)

    `effect` is the scripted behavior: an `async def effect(ctx)` coroutine
    (see spirit/game/session/effects.py for the ctx API), the `unimplemented`
    marker, or None for attacks with no extra effect (vanilla damage).

    `condition(board, player_id, pokemon) -> bool` gates offering the ability
    at all (an ability that would do nothing may not be used).
    """
    def __init__(
        self,
        title: str,
        game_text: str = "",
        ability_type: AbilityTypes = AbilityTypes.POKE_ABILITY,
        effect: Optional[Any] = None,
        trigger: Optional[str] = None,
        activation: Optional[str] = None,
        vstar: bool = False,
        gx: bool = False,
        passive: Optional[Any] = None,
        condition: Optional[Callable] = None,
        shared_once_per_turn: Optional[str] = None,
        ends_turn: bool = False,
        usable_from: Optional[str] = None
    ):
        self.title = title
        # 'hand' | 'discard': offered while the card sits in that zone instead
        # of in play (Pyukumuku, Beedrill, Gengar). Hand gets AbilitySelection
        # + OutOfPlay; discard uses OutOfPlay.
        self.usable_from = usable_from
        self.game_text = game_text
        self.ability_type = ability_type
        self.effect = effect
        # "You can't use more than 1 <name> Ability each turn": a turn-scoped
        # lock shared by name across every copy in play (Dark Asset).
        # None = the plain per-entity limit.
        self.shared_once_per_turn = shared_once_per_turn
        # A Triggers value (or a tuple/list of them): the session runs `effect`
        # on that event instead of offering the ability as a selectable action.
        self.trigger = trigger
        # "If you use this Ability, your turn ends" (Rotom V Instant Charge).
        self.ends_turn = ends_turn
        # An Activations value: the ability is offered as a selectable action.
        self.activation = activation
        # VSTAR Powers are usable once per game and flip the playmat marker.
        self.vstar = vstar
        # GX attacks are usable once per game (Pokemon-GX rule box).
        self.gx = gx
        # A passives.Passive for continuous effects (active while in play).
        self.passive = passive
        self.condition = condition
        # Assigned by the owning CardDefinition; must match SelectableAction.actionID.
        self.ability_id: Optional[str] = None
        # True when granted by an attached Tool (Forest Seal Stone): the ability
        # lives on the tool, not the Pokemon, so Path to the Peak can't lock it.
        self.is_granted: bool = False

    def on_use(self, fn: Callable) -> Callable:
        """Decorator alternative to the effect= parameter."""
        self.effect = fn
        return fn

    def has_trigger(self, trigger: str) -> bool:
        """Whether this ability fires on `trigger` (self.trigger may be a
        single Triggers value or a tuple/list of them)."""
        if self.trigger is None:
            return False
        if isinstance(self.trigger, (tuple, list, set, frozenset)):
            return trigger in self.trigger
        return self.trigger == trigger

    def to_dict(self) -> dict:
        d = {
            "abilityType": ABILITY_TYPE_HINTS.get(self.ability_type, "PokeAbility"),
            "title": {"id": self.title},
            "gameText": {"id": self.game_text}
        }
        if self.ability_id:
            d["abilityID"] = self.ability_id
        if self.vstar:
            # AbilityButtonRenderer styles the VSTAR button when buttonOverride
            # equals this exact string (decoded from the client string blob).
            d["buttonOverride"] = "abilityVSTAR"
        return d

class Attack(Ability):
    """Represents a Pokemon Attack."""
    def __init__(
        self,
        title: str,
        game_text: str = "",
        cost: Optional[Dict[PokemonTypes, int]] = None,
        damage: int = 0,
        damage_operator: str = "", # e.g. "+", "x"
        ability_type: AbilityTypes = AbilityTypes.ATTACK,
        effect: Optional[Any] = None,
        vstar: bool = False,
        gx: bool = False,
        locks_next_turn: bool = False,
        condition: Optional[Callable] = None,
        usable_first_turn: bool = False,
        usable_despite_conditions: bool = False
    ):
        super().__init__(title, game_text, ability_type, effect, vstar=vstar,
                         gx=gx, condition=condition)
        self.cost = cost or {}
        self.damage = damage
        self.damage_operator = damage_operator
        # "During your next turn, this Pokemon can't use <this attack>."
        self.locks_next_turn = locks_next_turn
        # Exempt from the "going first can't attack on turn 1" rule (Indeedee).
        self.usable_first_turn = usable_first_turn
        # Offered even while the user is Asleep/Paralyzed (Windup Arm-style).
        self.usable_despite_conditions = usable_despite_conditions

    def to_dict(self) -> dict:
        d = super().to_dict()
        # Cost keys must be client enum NAMES: { "Colorless": 2 } -- dictionary
        # keys coerce to PokemonTypes by name, numeric strings crash login.
        formatted_cost = {
            CLIENT_POKEMON_TYPE_NAMES[k]: v for k, v in self.cost.items()
        }
        d.update({
            "cost": formatted_cost,
            "damage": self.damage,
            "amountOperator": self.damage_operator
        })
        return d

# Rarities whose print covers the whole card face in foil (full arts, rule-box
# ultras, secrets); everything else foils only the art window.
_FULL_FOIL_RARITIES = {
    Rarities.RareHoloEX, Rarities.RareHoloGX, Rarities.RareHoloV,
    Rarities.RareHoloVMAX, Rarities.RareHoloVSTAR, Rarities.ChrRareHolo,
    Rarities.ChrRareHoloV, Rarities.ChrRareSecret, Rarities.ChrRareUltra,
    Rarities.RareUltra, Rarities.RareSecret, Rarities.RareRainbow,
    Rarities.Legendary, Rarities.ExtraRare,
}


class Foil:
    """Holo/foil treatment for a card archetype.

    mask picks the foil texture family (Reverse rides wp_ph bundles, everything
    else wp_std); effects[0] picks the client's Resources foil material, extra
    effects render on the second foil layer (wp_secondary bundle).

    style shapes GENERATED masks only ('auto'/'full'/'window'/'reverse', see
    foil_mask_gen) -- an extracted/hand-authored _foil PNG always wins.
    """
    def __init__(
        self,
        mask: FoilMasks = FoilMasks.HOLO,
        effects: Optional[List[FoilEffects]] = None,
        intensity: Optional[int] = None,
        style: str = "auto",
    ):
        self.mask = mask
        self.effects = effects or [FoilEffects.SWHOLO]
        self.intensity = intensity
        self.style = style

    def resolve_style(self, rarity: Optional[int] = None, subtypes: Optional[List[str]] = None) -> str:
        if self.style != "auto":
            return self.style
        if self.mask == FoilMasks.REVERSE:
            return "reverse"
        if rarity in _FULL_FOIL_RARITIES or any(
            s in ("V", "VMAX", "VSTAR", "V-UNION", "Radiant") for s in (subtypes or [])
        ):
            return "full"
        return "window"

    def mask_kind(self) -> str:
        """wp_ bundle kind the client requests this card's primary mask from
        (CardImageRenderer.SetupFoilTexture precedence)."""
        if self.effects[0] == FoilEffects.CRACKED_ICE:
            return "pcd"
        if self.mask == FoilMasks.REVERSE:
            return "ph"
        return "std"

    def to_attributes(self) -> dict:
        # Primary effect rides 200610 (client puts the single attr at index 0,
        # then appends the 200611 array); IsFoil derives client-side.
        attrs = {
            str(AttrID.FOIL_MASK.value): {"type": "int", "value": self.mask.value},
            str(AttrID.FOIL_EFFECT.value): {"type": "int", "value": self.effects[0].value},
            str(AttrID.FOIL_EFFECTS.value): {
                "type": "json",
                "value": json.dumps([e.value for e in self.effects[1:]]),
            },
        }
        if self.intensity is not None:
            attrs[str(AttrID.FOIL_INTENSITY.value)] = {"type": "int", "value": self.intensity}
        return attrs


class CardDefinition:
    """Base class for all card definitions."""
    def __init__(
        self,
        guid: str,
        key: str,
        name: str,
        collector_number: int,
        set_code: str,
        rarity: int,
        display_name: Optional[str] = None,
        searchable_by: Optional[List[str]] = None,
        subtypes: Optional[List[str]] = None,
        attributes: Optional[dict] = None,
        regulation_mark: Optional[str] = None,
        foil: Optional[Foil] = None,
    ):
        self.guid = guid
        self.key = key
        self.name = name
        self.collector_number = collector_number
        self.set_code = set_code
        self.rarity = rarity
        self.display_name = fix_mojibake(display_name) if display_name else display_name
        self.searchable_by = with_ascii_aliases(
            fix_mojibake_list(searchable_by), self.display_name
        )
        self.subtypes = fix_mojibake_list(subtypes)
        self.extra_attributes = dict(attributes or {})
        # Server-only metadata for format/legality tooling. Do NOT emit this as
        # AttrID.REGULATION_MARK (202260): on the PTCGO client that ID is a
        # Dictionary attribute, and a string like "H" fails EntityIntroduced
        # deserialization (Char -> KeyValuePair), which breaks opening hands.
        self.regulation_mark = regulation_mark
        self.foil = foil
        if foil is not None:
            self.extra_attributes.update(foil.to_attributes())
        # Continuous effect while in play/attached (tools, special energies).
        self.passive: Optional[Any] = None
        CARD_DEFS_BY_GUID[guid.lower()] = self

    def to_archetype_dict(self) -> dict:
        """Converts the definition to the dictionary format expected by the server's ArchetypeFound packet."""
        # Start with base attributes
        attrs = {
            str(AttrID.NAME.value): {"type": "json", "value": json.dumps({"id": self.name})},
            str(AttrID.SET_KEY.value): {"type": "string", "value": self.set_code},
            str(AttrID.SET_CACHE_KEY.value): {"type": "string", "value": self.set_code},
            str(AttrID.COLLECTOR_NUMBER.value): {"type": "int", "value": self.collector_number},
            str(AttrID.IMAGE_URL.value): {"type": "string", "value": str(self.collector_number).zfill(3)},
            str(AttrID.RARITY.value): {"type": "int", "value": self.rarity},
            str(AttrID.PRODUCT_TYPE.value): {"type": "int", "value": ProductType.SINGLES.value},
            str(AttrID.COLLECTION_ID.value): {"type": "string", "value": self.guid},
        }

        # Apply card-type specific attributes from subclasses or extra_attributes
        for k, v in self.extra_attributes.items():
            attrs[str(k)] = v

        # Ensure Card Logic Name (200630 / EVOLUTION_LOGIC_NAME) is ALWAYS populated to prevent client null key crashes on attachments
        if str(AttrID.EVOLUTION_LOGIC_NAME.value) not in attrs:
            own_name_part = self.name.split(".")[-2] if "direwolfdigital" in self.name else self.name
            attrs[str(AttrID.EVOLUTION_LOGIC_NAME.value)] = {
                "type": "string", "value": own_name_part
            }

        return {
            "guid": self.guid,
            "key": self.key,
            "display_name": self.display_name,
            "searchable_by": self.searchable_by,
            "attributes": attrs
        }

class PokemonCardDef(CardDefinition):
    def __init__(
        self,
        guid: str,
        key: str,
        name: str,
        collector_number: int,
        set_code: str,
        rarity: int,
        hp: int,
        elements: List[PokemonTypes],
        stage: PokemonStage = PokemonStage.BASIC,
        retreat_cost: int = 1,
        weakness_type: PokemonTypes = PokemonTypes.UNSET,
        weakness_amount: int = 2, # Multiplicative I.E. 2x
        resistance_type: PokemonTypes = PokemonTypes.UNSET,
        resistance_amount: int = 30, # Reduces damage TAKEN I.E. -30
        evolves_from: Optional[str] = None,
        family_id: Optional[int] = None,
        abilities: Optional[List[Ability]] = None,
        display_name: Optional[str] = None,
        searchable_by: Optional[List[str]] = None,
        subtypes: Optional[List[str]] = None,
        attributes: Optional[dict] = None,
        regulation_mark: Optional[str] = None,
        passive: Optional[Any] = None,
        unplayable_from_hand: bool = False,
        setup_as_active: bool = False,
        foil: Optional[Foil] = None
    ):
        super().__init__(
            guid, key, name, collector_number, set_code, rarity,
            display_name, searchable_by, subtypes, attributes,
            regulation_mark=regulation_mark,
            foil=foil,
        )
        # Card-level continuous effect while this Pokemon is top-level in play
        # (attack-rules passives, e.g. Swanna); distinct from Ability(passive=).
        self.passive = passive
        # Shedinja: never offered as a hand bench-play (enters play by effect).
        self.unplayable_from_hand = unplayable_from_hand
        # Luxray CZ's Explosiveness: may be placed as the opening Active
        # despite its stage (setup only; bench plays stay Basics-only).
        self.setup_as_active = setup_as_active

        # Add Pokemon-specific defaults to extra_attributes
        self.extra_attributes.update({
            str(AttrID.CARD_TYPE.value): {"type": "int", "value": CardType.POKEMON.value},
            str(AttrID.HP.value): {"type": "int", "value": hp},
            str(AttrID.STAGE.value): {"type": "int", "value": stage.value},
            str(AttrID.POKEMON_TYPES.value): {"type": "json", "value": json.dumps([t.value for t in elements])},
            str(AttrID.RETREAT_COST.value): {"type": "int", "value": retreat_cost},
            str(AttrID.WEAKNESS_TYPES.value): {"type": "json", "value": json.dumps([weakness_type.value] if weakness_type != PokemonTypes.UNSET else [])},
            str(AttrID.RESISTANCE_TYPES.value): {"type": "int", "value": resistance_type.value},
        })

        if weakness_type != PokemonTypes.UNSET:
            self.extra_attributes.update({
                str(AttrID.WEAKNESS_OPERATOR.value): {"type": "string", "value": "x"},
                str(AttrID.WEAKNESS_AMOUNT.value): {"type": "int", "value": weakness_amount},
            })

        if resistance_type != PokemonTypes.UNSET:
            self.extra_attributes.update({
                str(AttrID.RESISTANCE_OPERATOR.value): {"type": "string", "value": "-"},
                str(AttrID.RESISTANCE_AMOUNT.value): {"type": "int", "value": resistance_amount},
            })

        # The client uses P.F.C (200630) to identify the card's own logic name in the evolution chain
        own_name_part = name.split(".")[-2] if "direwolfdigital" in name else name
        self.extra_attributes[str(AttrID.EVOLUTION_LOGIC_NAME.value)] = {
            "type": "string", "value": own_name_part
        }

        if evolves_from:
            self.extra_attributes[str(AttrID.EVOLVES_FROM.value)] = {
                "type": "json", "value": json.dumps({"id": evolves_from})
            }
            # The client uses P.F.F (200640) to link the visual evolution arrows in the deck builder.
            # Usually this is just the literal Name of the pokemon it evolves from.
            name_part = evolves_from.split(".")[-2] if "direwolfdigital" in evolves_from else evolves_from
            self.extra_attributes[str(AttrID.EVOLUTION_LOGIC_FROM.value)] = {
                "type": "string", "value": name_part
            }

        if family_id:
            self.extra_attributes[str(AttrID.FAMILY_ID.value)] = {
                "type": "int", "value": family_id
            }

        # Handle Abilities and Attacks
        self.abilities: List[Ability] = abilities or []
        if abilities:
            ability_list = []
            for idx, a in enumerate(abilities):
                if not a.ability_id:
                    a.ability_id = ability_id_for(guid, idx)
                ABILITIES_BY_ID[a.ability_id] = a
                ability_list.append(a.to_dict())
            self.extra_attributes[str(AttrID.PIE_ABILITIES.value)] = {
                "type": "json", "value": json.dumps(ability_list)
            }
        else:
            self.extra_attributes[str(AttrID.PIE_ABILITIES.value)] = {
                "type": "json", "value": "[]"
            }

class TrainerCardDef(CardDefinition):
    """`effect` is the scripted behavior run when the card is played: an
    `async def effect(ctx)` coroutine (see spirit/game/session/effects.py),
    the `unimplemented` marker, or None for cards with no effect scripted.

    `condition(board, player_id) -> bool` gates when the card may be played
    at all (e.g. Ultra Ball needs 2 other cards in hand to discard); a
    3-arg `condition(board, player_id, card)` also gets the hand copy (Nugget).
    """
    def __init__(
        self,
        guid: str,
        key: str,
        name: str,
        collector_number: int,
        set_code: str,
        rarity: int,
        trainer_type: TrainerType,
        effect: Optional[Any] = None,
        condition: Optional[Callable] = None,
        abilities: Optional[List[Ability]] = None,
        display_name: Optional[str] = None,
        searchable_by: Optional[List[str]] = None,
        subtypes: Optional[List[str]] = None,
        attributes: Optional[dict] = None,
        regulation_mark: Optional[str] = None,
        usable_first_turn: bool = False,
        foil: Optional[Foil] = None,
    ):
        super().__init__(
            guid, key, name, collector_number, set_code, rarity,
            display_name, searchable_by, subtypes, attributes,
            regulation_mark=regulation_mark,
            foil=foil,
        )
        self.effect = effect
        self.condition = condition
        # Exempt from the "no Supporters on turn 1" rule (Team Rocket's Proton).
        self.usable_first_turn = usable_first_turn
        # Trainers have no PIE_ABILITIES slot; declared abilities register for
        # the session's trigger scans only (Dream Ball's ON_TAKEN_AS_PRIZE).
        self.abilities: List[Ability] = abilities or []
        for idx, a in enumerate(self.abilities):
            if not a.ability_id:
                a.ability_id = ability_id_for(guid, idx + 100)  # slot 0 = StadiumCardDef.ability
            ABILITIES_BY_ID[a.ability_id] = a
        if effect is not None:
            TRAINER_EFFECTS_BY_GUID[guid.lower()] = effect
        self.extra_attributes.update({
            str(AttrID.CARD_TYPE.value): {"type": "int", "value": CardType.TRAINER.value},
            str(AttrID.TRAINER_TYPE.value): {"type": "int", "value": trainer_type.value},
        })

class ItemCardDef(TrainerCardDef):
    def __init__(self, **kwargs):
        kwargs['trainer_type'] = TrainerType.ITEM
        super().__init__(**kwargs)

class FossilItemCardDef(ItemCardDef):
    """Item played as if it were a Basic Colorless Pokemon (fossils).

    The archetype stays a Trainer-Item (real PTCGO shape: deck-builder
    grouping, Item locks, mulligan/setup exclusion); plays_as_pokemon makes
    the board entity a PokemonEntity so it benches, evolves, takes damage and
    offers its PIE abilities like a Basic while in play.
    """
    plays_as_pokemon = True

    def __init__(self, hp: int, passive: Optional[Any] = None, **kwargs):
        super().__init__(**kwargs)
        self.passive = passive
        self.extra_attributes.update({
            str(AttrID.HP.value): {"type": "int", "value": hp},
            str(AttrID.STAGE.value): {"type": "int", "value": PokemonStage.BASIC.value},
            str(AttrID.POKEMON_TYPES.value): {
                "type": "json", "value": json.dumps([PokemonTypes.COLORLESS.value])
            },
            str(AttrID.RETREAT_COST.value): {"type": "int", "value": 0},
            str(AttrID.PIE_ABILITIES.value): {
                "type": "json",
                "value": json.dumps([a.to_dict() for a in self.abilities]),
            },
        })


class SupporterCardDef(TrainerCardDef):
    def __init__(self, **kwargs):
        kwargs['trainer_type'] = TrainerType.SUPPORTER
        super().__init__(**kwargs)

class StadiumCardDef(TrainerCardDef):
    """`passive` is the stadium's continuous effect while in play (a
    passives.Passive). `ability` is an Ability offered once during EACH
    player's turn while the stadium is in play (Training Court).
    `companion(board, player_id, card)` returns a second hand card that
    must be played into the stadium slot together (Legendary Ocean Trench).
    `discards_replacement` is Chaotic Swell: the Stadium played over this one
    is discarded straight after it and never gets its effect."""
    def __init__(self, passive: Optional[Any] = None,
                 ability: Optional["Ability"] = None,
                 companion: Optional[Callable] = None,
                 discards_replacement: bool = False, **kwargs):
        kwargs['trainer_type'] = TrainerType.STADIUM
        super().__init__(**kwargs)
        self.passive = passive
        self.ability = ability
        self.companion = companion
        self.discards_replacement = discards_replacement
        if ability is not None:
            if not ability.ability_id:
                ability.ability_id = ability_id_for(self.guid, 0)
            ABILITIES_BY_ID[ability.ability_id] = ability

class PokemonToolCardDef(TrainerCardDef):
    """`passive` is the tool's continuous effect while attached (a
    passives.Passive); `effect` stays unused for plain stat tools.
    `granted_abilities` are Abilities the tool grants its holder while
    attached (Forest Seal Stone). `attach_to(pokemon_entity) -> bool`
    restricts legal attach targets (Hero's Medal)."""
    def __init__(self, passive: Optional[Any] = None,
                 granted_abilities: Optional[List[Ability]] = None,
                 attach_to: Optional[Callable] = None, **kwargs):
        kwargs['trainer_type'] = TrainerType.POKEMON_TOOL
        super().__init__(**kwargs)
        self.passive = passive
        self.attach_to = attach_to
        self.granted_abilities: List[Ability] = granted_abilities or []
        for idx, a in enumerate(self.granted_abilities):
            if not a.ability_id:
                a.ability_id = ability_id_for(self.guid, idx)
            a.is_granted = True
            ABILITIES_BY_ID[a.ability_id] = a

class EnergyCardDef(CardDefinition):
    """Special-energy behavior hooks:

    provides         -- ENERGY_INFO options, a list of alternatives each being
                        the list of types provided at once (Double Turbo:
                        [[C, C]]; Aurora: one single-type option per type).
    attach_to        -- predicate(pokemon_entity) -> bool restricting legal
                        attach targets ("This card can only be attached to..."
                        card text only; type-gated benefits belong in the
                        passive/on_attach, not here).
    discard_if_invalid -- the card also prints "if it is attached to anything
                        else, discard this card" (Double Dragon Energy, Team
                        Rocket's Energy). Re-checks attach_to after an effect
                        moves or attaches the card, not just when it is played
                        from hand; opt-in because a bare attach_to restriction
                        does not by itself discard.
    attach_condition -- predicate(board, player_id) -> bool gating whether the
                        attach may be offered at all (Aurora needs another
                        card in hand to discard).
    attach_cost      -- async (ctx) -> bool run before the attach resolves;
                        returning False cancels the attach (Aurora's discard).
    on_attach        -- async (ctx) run after attaching from hand (Capture's
                        search, Speed Lightning's draw). ctx.source is the
                        energy, ctx.attached_to the Pokemon.
    on_discarded_by_carrier_attack -- async (ctx, energy, pokemon) queued after
                        an attack used by the attached Pokemon discards this
                        card (Boomerang Energy). Runs in deferred_actions after
                        the attack, so the Pokemon is still in play if it lived.
    passive          -- continuous effect while attached (a passives.Passive).
    granted_abilities -- Abilities the energy grants its holder while attached
                        (Spiky Energy's ON_DAMAGED_BY_ATTACK), mirrored onto
                        PIE_ABILITIES like Pokemon Tool grants.
    """
    def __init__(
        self,
        guid: str,
        key: str,
        name: str,
        collector_number: int,
        set_code: str,
        rarity: int,
        energy_type: PokemonTypes = PokemonTypes.COLORLESS,
        is_special: bool = False,
        provides: Optional[List[List[PokemonTypes]]] = None,
        attach_to: Optional[Callable] = None,
        discard_if_invalid: bool = False,
        attach_condition: Optional[Callable] = None,
        attach_cost: Optional[Any] = None,
        on_attach: Optional[Any] = None,
        on_carrier_knocked_out: Optional[Any] = None,
        on_discarded_by_carrier_attack: Optional[Any] = None,
        passive: Optional[Any] = None,
        granted_abilities: Optional[List[Ability]] = None,
        display_name: Optional[str] = None,
        searchable_by: Optional[List[str]] = None,
        subtypes: Optional[List[str]] = None,
        attributes: Optional[dict] = None,
        regulation_mark: Optional[str] = None,
        foil: Optional[Foil] = None,
    ):
        super().__init__(
            guid, key, name, collector_number, set_code, rarity,
            display_name, searchable_by, subtypes, attributes,
            regulation_mark=regulation_mark,
            foil=foil,
        )
        self.energy_type = energy_type
        self.attach_to = attach_to
        self.discard_if_invalid = discard_if_invalid
        self.attach_condition = attach_condition
        self.attach_cost = attach_cost
        self.on_attach = on_attach
        # async (ctx) run when the carrier Pokemon is Knocked Out by an
        # opponent's attack (Gift Energy's draw); ctx.source is the energy.
        self.on_carrier_knocked_out = on_carrier_knocked_out
        # async (ctx, energy, pokemon) after the carrier's attack discards this
        # card (Boomerang Energy reattach).
        self.on_discarded_by_carrier_attack = on_discarded_by_carrier_attack
        self.passive = passive
        self.granted_abilities: List[Ability] = granted_abilities or []
        for idx, a in enumerate(self.granted_abilities):
            if not a.ability_id:
                a.ability_id = ability_id_for(guid, idx)
            a.is_granted = True
            ABILITIES_BY_ID[a.ability_id] = a

        options = [[t.value for t in option] for option in provides] \
            if provides else [[energy_type.value]]
        self.extra_attributes.update({
            str(AttrID.CARD_TYPE.value): {"type": "int", "value": CardType.ENERGY.value},
            str(AttrID.POKEMON_TYPES.value): {"type": "json", "value": json.dumps([energy_type.value])},
            # ENERGY_INFO (201040) expects a JSON object with "options": [[type]]
            str(AttrID.ENERGY_INFO.value): {
                "type": "json",
                "value": json.dumps({"options": options})
            },
        })

        if is_special:
            self.extra_attributes[str(AttrID.IS_SPECIAL_ENERGY.value)] = {
                "type": "bool", "value": True
            }

def default_pack_rarity_attribute() -> dict:
    """Attr 202250 (a.g[]): the guaranteed-rarity breakdown shown in the pack "i" info popup.
    Mirrors BoosterPack.open's rarity slots. rarityIcon coerces from the enum int (like RARITY)."""
    slots = [
        (Rarities.Common, "deckbuilder.cardfilters.rarity.common", 4),
        (Rarities.Uncommon, "deckbuilder.cardfilters.rarity.uncommon", 3),
        (Rarities.Rare, "deckbuilder.cardfilters.rarity.rare", 1),
    ]
    value = [
        {"rarityIcon": rarity.value, "rarityName": {"id": loc_key}, "count": count}
        for rarity, loc_key, count in slots
    ]
    return {"type": "json", "value": json.dumps(value)}


class ProductDef:
    """Base class for all product definitions (Packs, Decks, etc.)"""
    def __init__(
        self,
        guid: str,
        key: str,
        name: str,
        product_type: ProductType = ProductType.UNSET,
        image_url: Optional[str] = None,
        catalog_id: Optional[str] = None,
        attributes: Optional[dict] = None
    ):
        self.guid = guid
        self.key = key
        self.name = name
        self.product_type = product_type
        self.image_url = image_url
        self.catalog_id = catalog_id
        self.extra_attributes = attributes or {}

    def to_archetype_dict(self) -> dict:
        # 1. Base mandatory attributes for all products
        attrs = {
            str(AttrID.NAME.value): {"type": "json", "value": json.dumps({"id": self.name})},
            str(AttrID.SET_KEY.value): {"type": "string", "value": self.key},
            str(AttrID.PRODUCT_TYPE.value): {"type": "int", "value": self.product_type.value},
            # SET_CACHE_KEY (200580) and EXPANSION (10020) are critical for client indexing
            str(AttrID.SET_CACHE_KEY.value): {"type": "string", "value": self.key},
            str(AttrID.EXPANSION.value): {"type": "string", "value": self.key},
            str(AttrID.SET_NUMBER.value): {"type": "int", "value": 1},
        }

        # 2. Image Lookup (Attribute 10510 and 10520) - CRITICAL to prevent Deck Builder crash and allow local cached AssetBundle rendering bypass in Shop
        if self.image_url:
            attrs[str(AttrID.IMAGE_URL.value)] = {"type": "string", "value": self.image_url}
            # Extract relative image name (e.g., "bw1_booster.png" or "http://127.0.0.1:8000/products/bw1_booster.png" -> "bw1_booster")
            base_name = os.path.basename(self.image_url)
            image_name = os.path.splitext(base_name)[0].lower()
            attrs[str(AttrID.IMAGE_NAME.value)] = {"type": "string", "value": image_name}
        else:
            # Fallback to GUID or key if no image specified
            attrs[str(AttrID.IMAGE_URL.value)] = {"type": "string", "value": self.guid}
            attrs[str(AttrID.IMAGE_NAME.value)] = {"type": "string", "value": self.guid}

        # 3. Catalog ID (Attribute 10570)
        if self.catalog_id:
            attrs[str(AttrID.CATALOG_ID.value)] = {"type": "string", "value": self.catalog_id}
        else:
            attrs[str(AttrID.CATALOG_ID.value)] = {"type": "string", "value": self.guid}

        # 4. Merge extra attributes
        for k, v in self.extra_attributes.items():
            attrs[str(k)] = v

        # 5. Packs need rarity odds (202250) or the info popup NREs; scripts may override.
        if self.product_type == ProductType.PACKS and str(AttrID.PACK_RARITY_DATA.value) not in attrs:
            attrs[str(AttrID.PACK_RARITY_DATA.value)] = default_pack_rarity_attribute()

        return {
            "guid": self.guid,
            "key": self.key,
            "attributes": attrs
        }

class BoosterPackDef(ProductDef):
    def __init__(self, **kwargs):
        kwargs['product_type'] = ProductType.PACKS
        super().__init__(**kwargs)

class DeckDef(ProductDef):
    def __init__(self, **kwargs):
        kwargs['product_type'] = ProductType.DECKS
        super().__init__(**kwargs)

class CoinDef(ProductDef):
    def __init__(self, **kwargs):
        kwargs['product_type'] = ProductType.COINS
        super().__init__(**kwargs)

class DeckBoxDef(ProductDef):
    def __init__(self, **kwargs):
        kwargs['product_type'] = ProductType.DECK_BOX
        super().__init__(**kwargs)

class SleeveDef(ProductDef):
    def __init__(self, **kwargs):
        kwargs['product_type'] = ProductType.SLEEVE
        super().__init__(**kwargs)
