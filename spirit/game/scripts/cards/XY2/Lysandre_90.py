"""Lysandre (XY - Flashfire 90/106).

Supporter.

  "Switch 1 of your opponent's Benched Pokemon with his or her Active
   Pokemon."

Word for word Boss's Orders, so it shares the effect and the condition.
It does NOT share the card name: "Lysandre" and "Boss's Orders" are two
names, and the 4-copy limit counts each on its own -- 4 of each in one
deck is legal. The subtitled prints of Boss's Orders are what would fold
into that card's count (see the note on Professor's Research); the only
one is Boss's Orders (Ghetsis), which this pool does not carry. There
has never been an English "Boss's Orders (Lysandre)".
"""

from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="dde7530d-fc38-57a1-bd17-db10eb2c458f",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lysandre.Name",
    display_name="Lysandre",
    searchable_by=["Lysandre", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    effect=bosss_orders,
    condition=opponent_has_bench,
)
