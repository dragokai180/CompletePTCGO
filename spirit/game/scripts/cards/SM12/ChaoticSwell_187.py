"""Chaotic Swell (SM - Cosmic Eclipse 187/236).

Stadium.

  "Whenever either player plays a Stadium card from their hand, discard that
   Stadium card after discarding this one. (The new Stadium card has no
   effect.)"

Nothing else in the pool works like this, and it does not fit a Passive: by
the time the replacement lands, this card has already left play, so there is
no carrier left to answer a hook. It is a property of the OUTGOING Stadium
instead -- StadiumCardDef(discards_replacement=True), which
_execute_play_stadium reads off the Stadium already in play, before the swap.

The order the card prints is the order the engine performs: this one goes to
its owner's discard first, the replacement lands in the Stadium slot (so the
animation reads as a Stadium being played), and then the replacement is
discarded too. The board is left with no Stadium at all.

"(The new Stadium card has no effect.)" is the skipped resolve_trainer_effect
call. Its passive never gets a window either -- nothing happens between the
card landing and being discarded -- so a come-into-play Stadium like Parallel
City is fully neutralised, both halves.

A dual Stadium played into this is one play, so both halves are swept.
"""

from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="53ff5d70-7635-5aad-b190-be61c579151d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaoticSwell.Name",
    display_name="Chaotic Swell",
    searchable_by=["Chaotic Swell", "Stadium", "ChaoticSwell"],
    subtypes=["Stadium"],
    collector_number=187,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    discards_replacement=True,
)
