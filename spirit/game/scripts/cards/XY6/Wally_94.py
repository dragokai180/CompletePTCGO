"""Wally (XY - Roaring Skies 94/108).

Supporter.

  "Search your deck for a card that evolves from 1 of your Pokemon
   (excluding Pokemon-EX) and put it onto that Pokemon. (This counts as
   evolving that Pokemon.) Shuffle your deck afterward. You can use this
   card during your first turn or on a Pokemon that was put into play this
   turn."

Pokemon Breeder's Nurturing with one target instead of two, and with both
timing rules struck out. That Supporter filters its candidates by
entered_play_turn and gates itself on turn_number > 2; Wally's last
sentence waives exactly those two, so neither appears here, and
ctx.evolve_pokemon already bypasses the may-evolve rules on its own.

"a card that evolves from" is the direct pre-evolution, so this matches
EVOLUTION_LOGIC_FROM against the target's own name -- not the whole-line
evolves_from() that Rare Candy needs to skip a stage.

The exclusion is on the Pokemon being evolved, not on what it evolves
into, and it is the XY-era uppercase rule box only: "Pokemon-EX" and the
SV-era "Pokemon ex" are separate mechanics, and text naming one does not
reach the other. So _is_pokemon_EX checks the "EX" subtype alone rather
than data_utils.is_pokemon_ex, which deliberately bundles both eras for
the SV cards whose own text is lowercase. Nothing in the pool carries
"EX" yet, so today the clause only documents the rule; widening it to
lowercase "ex" would also stop Wally Mega Evolving an SV Mega Evolution
Pokemon ex, which is the modern echo of the interaction the clause was
printed to prevent.
"""

from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import AttrID, Rarities


def _is_pokemon_EX(pokemon) -> bool:
    """The XY-era uppercase rule box only -- see the module note."""
    return "EX" in subtypes_for(pokemon.archetype_id)


def _wally_targets(pokemon_in_play):
    return [p for p in pokemon_in_play if not _is_pokemon_EX(p)]


def _wally_condition(board, player_id):
    return bool(_wally_targets(board.pokemon_in_play(player_id)))


async def wally(ctx):
    """Choose one of your Pokemon that is not a Pokemon-EX, search the deck
    for its direct evolution, and evolve it -- at any point in the game and
    even on a Pokemon played this turn."""
    candidates = _wally_targets(ctx.my_pokemon_in_play())
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to evolve"
    )
    if target is None:
        return
    logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return
    picks = await ctx.search_deck(
        lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
        count=1, minimum=0,
        prompt="Choose a card that evolves from that Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="8d4936df-2de0-5d10-8fec-9cc3596d8db0",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wally.Name",
    display_name="Wally",
    searchable_by=["Wally", "Supporter"],
    subtypes=["Supporter"],
    collector_number=94,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=wally,
    condition=_wally_condition,
)
