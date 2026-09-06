"""Special Charge (XY - Steam Siege 105/114).

Item.

  "Shuffle 2 Special Energy cards from your discard pile into your deck."

Super Rod's shape with a different filter, so the two now share
shuffle_from_discard and differ only in the predicate, the count and the
wording of the "up to".

Super Rod was errata'd to "up to 3" and passes up_to=True; this card prints
a flat "Shuffle 2", so it takes exactly 2, or the whole pile when the
discard cannot supply 2. That is what choose_cards does with no minimum.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_has, special_charge
from spirit.game.session.effects import is_special_energy

card = ItemCardDef(
    guid="ee453dd2-a4f6-5919-b5bd-83cf7435124b",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpecialCharge.Name",
    display_name="Special Charge",
    searchable_by=["Special Charge", "Item", "SpecialCharge"],
    subtypes=["Item"],
    collector_number=105,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    effect=special_charge,
    condition=discard_has(is_special_energy),
)
