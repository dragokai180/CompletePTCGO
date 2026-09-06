"""Arven (SV - Scarlet & Violet 166/198), the Japanese card's Pepper.

  "Search your deck for an Item card and a Pokemon Tool card, reveal them,
   and put them into your hand. Then, shuffle your deck."

Irida with a different pair of filters: one search_deck_groups browser with
two labeled slots, then put_in_hand(reveal=True) and a shuffle. The groups
cannot overlap here -- an Item is TrainerType.ITEM and a Tool is
TrainerType.POKEMON_TOOL -- so the "first matching group claims the card"
rule in search_deck_groups never has to break a tie.

No condition: like every other deck-search card in the pool, it stays
playable when the deck holds neither half, and the search simply finds
nothing.
"""

from spirit.game.card_effects.trainers import arven
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="d6fb7dbd-209c-56bb-a4db-61810295affb",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Arven.Name",
    display_name="Arven",
    searchable_by=["Arven", "Supporter", "Pepper"],
    subtypes=["Supporter"],
    collector_number=166,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=arven,
)
