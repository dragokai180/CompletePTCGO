"""Dedenne-GX (SM - Unbroken Bonds 57/214).

Basic Lightning Pokemon-GX. HP 160, weakness Fighting x2, resistance
Metal -20, retreat cost 1.

  Dedechange (Ability)  When you play this Pokemon from your hand onto
                        your Bench during your turn, you may discard your
                        hand and draw 6 cards. You can't use more than 1
                        Dedechange Ability each turn.
  Static Shock     [LC] 50
  Tingly Return-GX [LC] 50  Your opponent's Active Pokemon is now
                        Paralyzed. Put this Pokemon and all cards attached
                        to it into your hand. (You can't use more than 1
                        GX attack in a game.)

Three existing shapes, one per piece:

  Dedechange   Crobat V's Dark Asset exactly -- Triggers.ON_PLAY for the
               "when you play this from your hand onto your Bench" window,
               plus shared_once_per_turn, which is the engine's hook for
               "you can't use more than 1 <named> Ability each turn" (the
               name is shared across every printing, so two different
               Dedenne-GX prints still only get one use between them).
               The body is Hisuian Zoroark VSTAR's Phantom Star with 6
               instead of 7: an optional discard-hand-then-draw. Dedenne
               is on the Bench by the time this resolves, so ctx.hand()
               already excludes it.
  Tingly Return-GX
               condition_attack Paralyzes the defender and then runs its
               `also` hook. gx=True is what makes the engine enforce the
               once-per-game GX restriction (see SM5/DialgaGX_100.py); the
               effect itself only has to resolve.
  the scoop    remove_self_from_play("hand"), the shared helper Meowth
               ex's Tuck Tail uses. It owns the promote-or-lose handling
               for the vacated Active slot, so this card must not re-derive
               it. Note the damage=0: that helper deals the printed damage
               itself, so condition_attack has to be told not to deal it
               too -- the 50 comes from the helper, once.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import remove_self_from_play


async def dedechange(ctx):
    """On play from hand: you may discard your hand and draw 6 cards."""
    if not await ctx.ask_yes_no("Discard your hand and draw 6 cards?"):
        return
    await ctx.discard_cards(ctx.hand())
    await ctx.draw_cards(6)


card = PokemonCardDef(
    guid="f3ddc3fc-cba3-5b83-af3b-6784927a8848",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DedenneGX.Name",
    display_name="Dedenne-GX",
    searchable_by=["Dedenne-GX", "Basic", "GX", "DedenneGX"],
    subtypes=["Basic", "GX"],
    collector_number=57,
    set_code="SM10",
    rarity=Rarities.RareHoloGX,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    # The only Metal resistance and the only non-30 amount in the pool (the
    # rest are Fighting/Grass at -30), so it was the prime suspect for a
    # deck-save KeyNotFoundException here -- wrongly: the client saves this
    # card fine. The real cause was elsewhere (a Pokemon with no family_id
    # is missing from the map EvolutionsRenderUtil reads). Verified working.
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Ability(
            title="Dedechange",
            game_text=(
                "When you play this Pokémon from your hand onto your "
                "Bench during your turn, you may discard your hand and "
                "draw 6 cards. You can't use more than 1 Dedechange "
                "Ability each turn."
            ),
            trigger=Triggers.ON_PLAY,
            shared_once_per_turn="Dedechange",
            effect=dedechange,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Tingly Return-GX",
            game_text=(
                "Your opponent's Active Pokémon is now Paralyzed. Put "
                "this Pokémon and all cards attached to it into your "
                "hand. (You can't use more than 1 GX attack in a game.)"
            ),
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            gx=True,
            effect=condition_attack(
                SpecialConditions.PARALYZED,
                damage=0,  # the printed 50 is dealt by remove_self_from_play
                also=remove_self_from_play("hand"),
            ),
        ),
    ],
)
