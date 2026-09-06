"""Unown (XY - Ancient Origins 30/98).

Basic Psychic Pokemon. HP 60, weakness Psychic x2, no resistance, retreat 1.

  Farewell Letter       Ability. Once during your turn (before your attack),
                        if this Pokemon is on your Bench, you may discard
                        this Pokemon and all cards attached to it (this does
                        not count as a Knock Out). If you do, draw a card.
  Hidden Power  [C]  10

Farewell Letter is remove_self_from_play with a discard destination, which
this card is the first to need -- the factory already had hand, deck and
lost_zone. Self-removal is never a Knock Out in this engine: no prize is
taken and no knockout trigger fires, which is exactly what the
parenthetical asks for, so nothing extra is needed to honour it.

The Bench requirement is a real gate, not flavour: an Unown in the Active
Spot may not use this, which is what requires_benched() checks. Combined
with ONCE_PER_TURN that also keeps the offer from lingering -- the ability
removes its own Pokemon from play, so it cannot come up twice anyway.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import (
    remove_self_from_play, requires_benched,
)

_discard_self = remove_self_from_play(destination="discard", optional=True)


async def farewell_letter(ctx):
    """Discard this Benched Pokemon and everything attached, then draw 1."""
    before = ctx.source.parent
    await _discard_self(ctx)
    if ctx.source.parent is before:      # the player declined
        return
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="3fab86ca-52a6-5664-b8d0-6f2f6f670b27",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="Farewell Letter",
            game_text="Once during your turn (before your attack), if this Pokémon is on your Bench, you may discard this Pokémon and all cards attached to it (this does not count as a Knock Out). If you do, draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_benched(),
            effect=farewell_letter,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
