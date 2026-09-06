"""Squawkabilly ex (Scarlet & Violet Black Star Promo 160).

Basic Colorless Pokemon ex. HP 160, weakness Lightning x2, resistance
Fighting -30, retreat 1.

  Squawk and Seize (Ability)  Once during your first turn, you may
                        discard your hand and draw 6 cards. You can't use
                        more than 1 Squawk and Seize Ability during your
                        turn.
  Motivate         [C] 20  Attach up to 2 Basic Energy cards from your
                        discard pile to 1 of your Benched Pokemon.

Squawk and Seize is Fan Rotom's Fan Call wearing Dedenne-GX's body:

  the gate     Fan Call's exact trio -- Activations.ONCE_PER_TURN,
               shared_once_per_turn (the "no more than 1 <name> Ability
               during your turn" clause), and a first-turn condition.
               Note this is an ACTIVATED Ability, not an ON_PLAY trigger
               like Dedechange: the card says "once during your first
               turn", with no "when you play this Pokemon" window, so
               benching it early and using it later in that turn is legal.
               The predicate is defined locally, the way Fan Rotom and
               Terapagos ex each define their own.
  the body     Dedenne-GX's Dedechange -- an optional discard-your-hand-
               then-draw-6.

Squawkabilly ex is printed in Paldea Evolved (169/193) and Paldean Fates
(75/091), but neither of those sets exists in sets.json; the SV Black Star
Promo printing is the one this server can actually bundle art for, and
SVP is already legal in Expanded, so nothing else has to change.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_players_first_turn(board, player_id, pokemon=None) -> bool:
    """True on this player's first turn (turn 1 going first, turn 2 going
    second) -- the same read Fan Rotom's Fan Call uses."""
    ts = getattr(board, "turn_state", None)
    return ts is not None and ts.turn_number <= 2


async def squawk_and_seize(ctx):
    """You may discard your hand and draw 6 cards."""
    if not await ctx.ask_yes_no("Discard your hand and draw 6 cards?"):
        return
    await ctx.discard_cards(ctx.hand())
    await ctx.draw_cards(6)


async def motivate(ctx):
    """20, then attach up to 2 basic Energy from the discard to a Benched."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    for energy in picks:
        await ctx.attach_energy(energy, target)


card = PokemonCardDef(
    guid="4983962f-7cf7-5f1a-9773-bda644ad9507",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabillyex.Name",
    display_name="Squawkabilly ex",
    searchable_by=["Squawkabilly ex", "Basic", "ex", "Squawkabillyex"],
    subtypes=["Basic", "ex"],
    collector_number=160,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=931,
    abilities=[
        Ability(
            title="Squawk and Seize",
            game_text=(
                "Once during your first turn, you may discard your hand "
                "and draw 6 cards. You can't use more than 1 Squawk and "
                "Seize Ability during your turn."
            ),
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Squawk and Seize",
            condition=_is_players_first_turn,
            effect=squawk_and_seize,
        ),
        Attack(
            title="Motivate",
            game_text=(
                "Attach up to 2 Basic Energy cards from your discard "
                "pile to 1 of your Benched Pokémon."
            ),
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=motivate,
        ),
    ],
)
