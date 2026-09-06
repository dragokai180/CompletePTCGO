"""Darkrai-GX (SM - Burning Shadows 88/147, JP SM2+ Awakened Heroes).

Basic Darkness Pokemon-GX. HP 180, weakness Fighting x2, resistance
Psychic -20, retreat 2.

  Restoration          Ability. Once during your turn, if this Pokemon is
                       in your discard pile, you may put it onto your
                       Bench. Then, attach a [D] Energy card from your
                       discard pile to this Pokemon.
  Dark Cleave   [DDC]  130  This attack's damage isn't affected by
                       Resistance.
  Dead End-GX   [DDC]       If your opponent's Active Pokemon is affected
                       by a Special Condition, that Pokemon is Knocked
                       Out. (You can't use more than 1 GX attack in a
                       game.)

Restoration is Ho-Oh V's Reviving Flame minus the turn-ending clause: the
same usable_from="discard" path, gated on Bench room, with the Energy
attach mandatory (minimum=1) rather than "up to". It reads "a [D] Energy
card", so is_energy_of_type covers Special Darkness Energy too -- the
house convention for the symbol wording, as on Tapu Koko {*}.

A lock only reaches Restoration if its text names the discard pile.
Path to the Peak says "in play" and leaves it alone; Garbotoxin and the
XY5 Silent Lab we ship ("in play, in each player's hand, and in each
player's discard pile") both shut it off, through
blocks_out_of_play_abilities. Note the SM2 Silent Lab reprint is "in
play" only -- ours is the older, wider one.

Dark Cleave only waives Resistance, so it is a plain deal_damage with
ignore_resistance -- not ignore_effects_attack, which would also strip
the defender's damage-reduction effects that this card never mentions.

Dead End-GX is an effect Knock Out, not damage: it bypasses HP, shields
that only reduce damage, and Weakness/Resistance alike, and it leaves the
"Knocked Out by damage from an attack" ledger untouched.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import (
    attach_from_discard, requires_bench_space,
)
from spirit.game.session.effects import is_energy_of_type


def _darkness_energy(card) -> bool:
    return is_energy_of_type(card, PokemonTypes.DARKNESS)


async def restoration(ctx):
    """Once per turn from the discard: Bench this Pokemon, then attach a
    Darkness Energy from the discard to it."""
    if not await ctx.ask_yes_no("Put this Pokémon onto your Bench?"):
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    await attach_from_discard(predicate=_darkness_energy, count=1,
                              target="self", minimum=1)(ctx)


async def dark_cleave(ctx):
    """130, unaffected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def dead_end_gx(ctx):
    """Knocks the Defending Pokemon Out outright if it has any Special
    Condition on it."""
    defender = ctx.defender
    if defender is None:
        return
    if not (defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        return
    await ctx.knock_out(defender)


card = PokemonCardDef(
    guid="09c4eaab-9238-5512-b696-0da3d5c18ad8",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiGX.Name",
    display_name="Darkrai-GX",
    searchable_by=["Darkrai-GX", "Basic", "GX", "DarkraiGX"],
    subtypes=["Basic", "GX"],
    collector_number=88,
    set_code="SM3",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Ability(
            title="Restoration",
            game_text="Once during your turn (before your attack), if this Pokémon is in your discard pile, you may put it onto your Bench. Then, attach a Darkness Energy card from your discard pile to this Pokémon.",
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_bench_space(1),
            effect=restoration,
        ),
        Attack(
            title="Dark Cleave",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=dark_cleave,
        ),
        Attack(
            title="Dead End-GX",
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, that Pokémon is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            gx=True,
            effect=dead_end_gx,
        ),
    ],
)
