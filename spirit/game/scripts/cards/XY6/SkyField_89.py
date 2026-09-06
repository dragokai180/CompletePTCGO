"""Sky Field (XY - Roaring Skies 89/108).

  "Each player can have up to 8 Benched Pokemon. If this Stadium card
   stops being in play, each player discards Benched Pokemon until they
   have 5 Benched Pokemon. The owner of this card discards first."

Both halves are already engine-level, so the card is just the capacity
number:

  bench_capacity  8 for BOTH players, unconditionally -- unlike Area Zero
                  Underdepths (Tera in play) and Eternatus VMAX (its own
                  side, all-Darkness), which return None when their gate
                  fails. effective_bench_capacity takes the smallest
                  override, and only one Stadium is ever in play, so
                  nothing competes this down to 5.
  the shrink      enforce_bench_capacity() already runs when a Stadium
                  leaves play and makes every over-capacity player pick
                  and discard the excess -- a discard, not a Knock Out
                  (no prizes, no ON_KNOCKED_OUT). That is the Collapsed
                  Stadium ruling and it is what this card needs too.

One deviation: "the owner of this card discards first". _enforce_bench_
capacity_once orders the players active-first, not owner-first, for every
card that uses it. Both players still discard down to 5 and each still
chooses their own Pokemon, so only the order of the two prompts differs;
changing it would mean reordering the shared helper for Collapsed Stadium
as well.
"""

from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class SkyFieldPassive(Passive):
    """Each player can have up to 8 Benched Pokemon."""

    def bench_capacity(self, player_id, carrier):
        return 8


card = StadiumCardDef(
    guid="81f06034-e5c6-5c67-b544-9600c2591bfe",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyField.Name",
    display_name="Sky Field",
    searchable_by=["Sky Field", "Stadium", "SkyField"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=SkyFieldPassive(),
)
