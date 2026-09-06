"""Marshadow (SM - Unbroken Bonds 81/214).

Basic Psychic Pokemon. HP 80, weakness Darkness x2, resistance Fighting -20,
retreat cost 1.

  Resetting Hole (Ability)  Once during your turn (before your attack), if
                        this Pokemon is on your Bench, you may discard any
                        Stadium card in play. If you do, discard this
                        Pokemon and all cards attached to it.
  Red Knuckles     [C] 10+  If your opponent's Active Pokemon is an Ultra
                        Beast, this attack does 60 more damage.

Pidgeot V's Vanishing Wings is the same shape -- ONCE_PER_TURN, a bench-only
condition, then the Pokemon removes itself with everything attached. The
differences: Chien-Pao's stadium discard happens first and gates the rest
("if you do"), and the stack goes to the discard rather than the deck, so
this uses discard_cards(full_stack(...)) the way Scoop Up Net and Lost
Vacuum do -- remove_self_from_play has no 'discard' destination, and none is
needed here because a Benched Pokemon leaving play never empties the Active
spot.

The condition also requires a Stadium: with none in play the Ability can do
nothing at all, so offering it would only burn the once-per-turn use.

No card in this pool carries the "Ultra Beast" subtype yet, so Red Knuckles
always deals its printed 10 for now. The check is written against subtypes
so it starts working the day an Ultra Beast is added.
"""

from spirit.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, subtypes_for,
)
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.session.effects import full_stack


def _on_bench_with_stadium(board, player_id, pokemon) -> bool:
    if in_active_spot(board, player_id, pokemon):
        return False
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


def _defender_is_ultra_beast(ctx) -> bool:
    defender = ctx.defender
    return defender is not None \
        and "Ultra Beast" in subtypes_for(defender.archetype_id)


async def resetting_hole(ctx):
    """Discard the Stadium in play; if that happened, discard this Pokémon
    and everything attached to it."""
    if ctx.stadium_in_play() is None:
        return
    if not await ctx.ask_yes_no("Discard the Stadium in play?"):
        return
    if await ctx.discard_stadium() is None:
        return
    await ctx.discard_cards(full_stack(ctx.source))


card = PokemonCardDef(
    guid="a904f2ff-10bd-58f9-a800-fd6cfd5e66d2",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=802,
    abilities=[
        Ability(
            title="Resetting Hole",
            game_text=(
                "Once during your turn (before your attack), if this "
                "Pokémon is on your Bench, you may discard any Stadium "
                "card in play. If you do, discard this Pokémon and all "
                "cards attached to it."
            ),
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench_with_stadium,
            effect=resetting_hole,
        ),
        Attack(
            title="Red Knuckles",
            game_text=(
                "If your opponent's Active Pokémon is an Ultra Beast, "
                "this attack does 60 more damage."
            ),
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(_defender_is_ultra_beast, 60),
        ),
    ],
)
