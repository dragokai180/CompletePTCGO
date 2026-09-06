"""Klefki (Scarlet & Violet 96/198).

Basic Psychic Pokemon. HP 70, weakness Metal x2, retreat 1.

  Mischievous Lock (Ability)  As long as this Pokemon is in the Active
                        Spot, Basic Pokemon in play (both yours and your
                        opponent's) have no Abilities, except for
                        Mischievous Lock.
  Joust            [C] 10  Before doing damage, discard all Pokemon Tools
                        from your opponent's Active Pokemon.

Iron Thorns ex's Initialization with a different filter: same
blocks_abilities passive, same is_in_active_spot gate, same
"skip the carrier itself" guard. Where Iron Thorns keys on has_rule_box
and spares Future Pokemon, this keys on the Basic stage and spares any
Pokemon that itself has Mischievous Lock.

blocks_abilities is per-Pokemon, not per-Ability, so the "except for
Mischievous Lock" clause is read as "except Pokemon carrying it" -- which
is the same thing in practice, since Mischievous Lock is the only Ability
those Pokemon have. The carrier is excluded by entity id first, so the
lock never silences itself.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, TrainerType,
)
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _has_mischievous_lock(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    return any(
        getattr(a, "title", "") == "Mischievous Lock"
        for a in (getattr(definition, "abilities", None) or [])
    )


class _MischievousLockPassive(Passive):
    """Klefki: while this Pokémon is Active, Basic Pokémon have no Abilities."""

    def blocks_abilities(self, pokemon, carrier):
        if not is_in_active_spot(carrier):
            return False
        if pokemon.entity_id == carrier.entity_id:
            return False
        if pokemon.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
            return False
        return not _has_mischievous_lock(pokemon)


async def joust(ctx):
    """Discard the defender's Pokémon Tools, then deal the printed damage."""
    defender = ctx.defender
    if defender is not None:
        tools = [
            c for c in defender.children
            if c.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES
        ]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="89880af6-0eed-5f26-9e32-b3ecf21d3841",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=707,
    abilities=[
        Ability(
            title="Mischievous Lock",
            game_text=(
                "As long as this Pokémon is in the Active Spot, Basic "
                "Pokémon in play (both yours and your opponent's) have "
                "no Abilities, except for Mischievous Lock."
            ),
            passive=_MischievousLockPassive(),
        ),
        Attack(
            title="Joust",
            game_text=(
                "Before doing damage, discard all Pokémon Tools from "
                "your opponent's Active Pokémon."
            ),
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=joust,
        ),
    ],
)
