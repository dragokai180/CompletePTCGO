"""Trainers' Mail (XY - Roaring Skies 92/108).

  "Look at the top 4 cards of your deck. You may reveal a Trainer card you
   find there (except Trainers' Mail) and put it into your hand. Shuffle
   the other cards back into your deck."

Bug Catching Set's shape with a different filter and a count of 1:
deck_top(n) to look, the eligible subset offered through choose_cards with
`display_cards` set to the whole peek (so the client shows all 4 while only
the legal picks are selectable), then shuffle_deck() puts the rest back.

minimum=0 because the card says "you may" -- looking at 4 cards and taking
nothing is a legal resolution, and it is the only one available when none
of the 4 is an eligible Trainer.

The self-exclusion is by printed name rather than archetype id: the clause
names the card, so every printing of Trainers' Mail is excluded from every
other printing's peek, not just this exact one.
"""

from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_trainer_card

_SELF_NAME = "Trainers' Mail"


def _eligible_trainer(card) -> bool:
    if not is_trainer_card(card):
        return False
    definition = def_for(card.archetype_id)
    return (getattr(definition, "display_name", None) or "") != _SELF_NAME


async def trainers_mail(ctx):
    """Look at the top 4; you may take a Trainer other than this card."""
    top = ctx.deck_top(4)
    eligible = [c for c in top if _eligible_trainer(c)]
    if eligible:
        picks = await ctx.choose_cards(
            eligible, 1, minimum=0,
            prompt="Choose a Trainer card to put into your hand.",
            display_cards=top,
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="221140c0-b4a0-53e0-bf40-1ec7ae9aff90",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainersMail.Name",
    display_name="Trainers' Mail",
    searchable_by=["Trainers' Mail", "Item", "TrainersMail"],
    subtypes=["Item"],
    collector_number=92,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=trainers_mail,
)
