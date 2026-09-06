from spirit.game.data_utils import (
    PokemonCardDef, Attack, Ability, Triggers, ability_id_for, ABILITIES_BY_ID,
)
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities

_GUID = "9dd4452a-256e-58b8-92d9-8c65f10179d0"


async def _shellnado_spin_trigger(ctx):
    """Fires on ON_DAMAGED_BY_ATTACK (put counters if still within the window)
    and on BETWEEN_TURNS (cleans up the grant once the window has passed)."""
    pokemon = ctx.source
    until = getattr(pokemon, "_shellnado_spin_until", None)
    if ctx.damaged_by is not None:
        if until is not None and ctx.session.turn_state.turn_number == until:
            await ctx.deal_damage(
                120, target=ctx.damaged_by, apply_modifiers=False, as_counters=True
            )
        return
    if until is not None and ctx.session.turn_state.turn_number >= until:
        pokemon._shellnado_spin_until = None
        entries = [
            e for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
            if not (isinstance(e, dict)
                    and e.get("abilityID") == SHELLNADO_SPIN_GRANTED.ability_id)
        ]
        await ctx.session._broadcast_entity_attribute(
            pokemon, AttrID.PIE_ABILITIES, entries
        )


SHELLNADO_SPIN_GRANTED = Ability(
    title="Shellnado Spin",
    game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), place 12 damage counters on the Attacking Pokémon.",
    trigger=(Triggers.ON_DAMAGED_BY_ATTACK, Triggers.BETWEEN_TURNS),
    effect=_shellnado_spin_trigger,
)
SHELLNADO_SPIN_GRANTED.ability_id = ability_id_for(_GUID, 99)
ABILITIES_BY_ID[SHELLNADO_SPIN_GRANTED.ability_id] = SHELLNADO_SPIN_GRANTED


async def shellnado_spin(ctx):
    """180. During your opponent's next turn, if this Pokémon is damaged by an
    attack (even if this Pokémon is Knocked Out), place 12 damage counters
    on the Attacking Pokémon."""
    await ctx.deal_damage()
    ctx.attacker._shellnado_spin_until = ctx.session.turn_state.turn_number + 1
    entries = list(ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != SHELLNADO_SPIN_GRANTED.ability_id
           for e in entries if isinstance(e, dict)):
        entries.append(SHELLNADO_SPIN_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(
            ctx.attacker, AttrID.PIE_ABILITIES, entries
        )


card = PokemonCardDef(
    guid=_GUID,
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSlowbroex.Name",
    display_name="Mega Slowbro ex",
    searchable_by=["Mega Slowbro ex","Stage 1","ex","SV_Mega","MegaSlowbroex"],
    subtypes=["Stage 1","ex","SV_Mega"],
    collector_number=31,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Shellnado Spin",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), place 12 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=180,
            effect=shellnado_spin,
        ),
    ],
)
