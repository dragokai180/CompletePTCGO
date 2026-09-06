"""Rescue Stretcher (SM - Guardians Rising 130/145).

Item.

  "Choose 1:
   - Put a Pokemon from your discard pile into your hand.
   - Shuffle 3 Pokemon from your discard pile into your deck."

The two halves are Night Stretcher and Super Rod narrowed to Pokemon:
mode 1 is a single pick into the hand, mode 2 is shuffle_from_discard with
a flat count. Flat, not up_to -- the printed text has no "up to", so
choose_cards takes exactly 3, or the whole pile when it holds fewer, the
same reading Special Charge gets. That also means mode 2 stays offered
with 1 or 2 Pokemon in the discard; it is a bad choice there, not an
illegal one.

Serena's shape for the menu: only ask when there is anything to ask
about. Here that is just "is there a Pokemon in the discard at all",
which is also the playability condition, so once the card is playable
both modes are live and the menu always appears.

The client ships its own strings for this card, so the two buttons and
the shuffle prompt go in as localization keys rather than English
literals -- the Field Blower treatment. The pick-into-hand prompt has no
card-specific key, so it borrows the generic one.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.trainers import shuffle_from_discard
from spirit.game.session.effects import is_pokemon_card

_shuffle_three = shuffle_from_discard(
    is_pokemon_card, 3,
    "playmat.prompt.sm2_130.rescuestretcherreturntodeck",
)


async def rescue_stretcher(ctx):
    """Choose 1: one Pokemon from the discard to hand, or shuffle 3 back."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if not pokemon:
        return
    choice = await ctx.choose(
        "Choose 1:",
        [
            "playmat.buttonlabel.sm2_130.rescuestretcher.1",
            "playmat.buttonlabel.sm2_130.rescuestretcher.2",
        ],
    )
    if choice == 1:
        await _shuffle_three(ctx)
        return
    picks = await ctx.choose_cards(
        pokemon, 1, minimum=1,
        prompt="playmat.prompt.choosepokemonforhand.single",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = ItemCardDef(
    guid="8f36a4cb-83a1-56a5-b674-68bc025c73db",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item", "RescueStretcher"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=rescue_stretcher,
    condition=requires_discard(is_pokemon_card, 1),
)
