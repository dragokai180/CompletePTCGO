"""Trubbish (BW - Noble Victories 48/101).

Basic Psychic Pokemon. HP 60, weakness Psychic x2, no resistance, retreat 1.

  Garbage Collection [C]     Put a card from your discard pile on top of
                             your deck.
  Sludge Bomb        [PC] 20

Garbage Collection is the deck's answer to over-discarding: Battle
Compressor and Ultra Ball dump the pieces, this puts one back where the
next draw finds it. put_on_top_of_deck is the same primitive Cyllene uses
for its discard-to-top clause.

The English print drops the Japanese card's "reveal it" step. Nothing is
lost by that here -- the discard pile is a public zone, so the opponent has
already seen every card that could be chosen.

There is nothing to do with an empty discard pile, so the attack checks for
that rather than opening a chooser with no candidates.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def garbage_collection(ctx):
    """Put a card from your discard pile on top of your deck."""
    pile = ctx.discard_pile()
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1, minimum=1,
        prompt="Choose a card to put on top of your deck",
    )
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = PokemonCardDef(
    guid="f39ba71c-54a4-57ba-8cdd-f9a419c53cfd",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    display_name="Trubbish",
    searchable_by=["Trubbish", "Basic"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=568,
    abilities=[
        Attack(
            title="Garbage Collection",
            game_text="Put a card from your discard pile on top of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=garbage_collection,
        ),
        Attack(
            title="Sludge Bomb",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
