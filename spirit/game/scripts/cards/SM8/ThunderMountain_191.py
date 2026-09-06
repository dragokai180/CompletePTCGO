"""Thunder Mountain ◇ (SM - Lost Thunder 191/214).

Stadium, Prism Star. The first Prism Star card in the pool, so it brings the
rule with it.

  "The attacks of Lightning Pokemon (both yours and your opponent's) cost
   [L] less."
  "Whenever any player plays an Item or Supporter card from their hand,
   prevent all effects of that card done to this Stadium card."
  Prism Star rule: only 1 with the same name per deck, and a Prism Star card
  that would go to the discard pile goes to the Lost Zone instead.

The Lost Zone half is general, not card-specific: data_utils.discard_area_name
answers "discard" or "lostZone" from the subtypes, and every path that
discards asks it -- the effect layer's _move_to_public_pile, the Stadium
replaced when the next one is played, and Chaotic Swell's sweep. So this card
reaches the Lost Zone however it leaves play.

The Item/Supporter shield is a new Passive hook, blocks_trainer_effects.
Field Blower and Lost Vacuum build their targets from _tools_and_stadium,
which now skips a shielded Stadium, so neither can touch this.

Chaotic Swell still discards it: Chaotic Swell is a Stadium, not an Item or
a Supporter, so the shield does not apply -- and being a Prism Star, this
card lands in the Lost Zone rather than the discard.

The deck-building half of the rule lives in game/rules.py beside the ACE
SPEC limit, which is the same shape: at most 1 Prism Star card with a given
NAME, where ACE SPEC allows 1 in the whole deck.

The display name carries "{*}", not a literal diamond. That is the client's
own placeholder for the Prism Star glyph -- its shipped cards read "Cyrus
{*}" -- and the server serves each display_name to the client as a
localization override, so this is the string the renderer actually sees.
"""

from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import ThunderMountainPassive

card = StadiumCardDef(
    passive=ThunderMountainPassive(),
    guid="1485ad3a-47aa-5606-bf5c-8f4df4389ca2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThunderMountainPrismStar.Name",
    display_name="Thunder Mountain {*}",
    searchable_by=["Thunder Mountain", "Stadium", "Prism Star", "ThunderMountain"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=191,
    set_code="SM8",
    rarity=Rarities.Prism,
)
