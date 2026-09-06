"""Field Blower (SM - Guardians Rising 125/145).

Item.

  "Choose up to 2 in any combination of Pokemon Tool cards and Stadium cards
   in play (yours or your opponent's) and discard them."

Tool Scrapper with a wider target list. The list itself already existed as
_tools_and_stadium in card_effects/trainers.py, where Lost Vacuum uses it to
pick its single Lost Zone target; Field Blower takes up to 2 of the same
candidates and discards them instead.

The chooser prompt is the client's own string for this card
(playmat.prompt.sm2_125.fieldblower, "Choose Pokemon Tool or Stadium cards
to discard."), so it comes out localized rather than as an English literal.

"up to 2" with minimum=1: an Item that discards nothing would be a dead
play, and the condition already keeps the card unplayable when the board
holds neither a Tool nor a Stadium.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import field_blower, tools_or_stadium_in_play

card = ItemCardDef(
    guid="082b68b0-2d81-5a61-b768-9ede95750cbf",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieldBlower.Name",
    display_name="Field Blower",
    searchable_by=["Field Blower", "Item", "FieldBlower"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=field_blower,
    condition=tools_or_stadium_in_play,
)
