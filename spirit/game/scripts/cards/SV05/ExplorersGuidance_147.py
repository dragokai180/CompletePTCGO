from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="74b89390-d8d9-5a35-a024-bb8c0eb9b4d7",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExplorersGuidance.Name",
    display_name="Explorer's Guidance",
    searchable_by=["Explorer's Guidance", "Supporter", "Ancient", "ExplorersGuidance"],
    subtypes=["Supporter", "Ancient"],
    collector_number=147,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=look_at_top(
        6, take=2, rest="discard",
        prompt="Choose 2 cards to put into your hand. Discard the other cards.",
    ),
)
