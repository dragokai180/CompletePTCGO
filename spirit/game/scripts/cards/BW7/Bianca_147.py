from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect

async def bianca(ctx):
    """Draw cards until you have 6 cards in your hand. You may play only 1
    Supporter card during your turn (before your attack)."""
    await draw_until_effect(6)(ctx)
    # Unmatched clause: "You may play only 1 Supporter card during your turn (before your attack)."

card = SupporterCardDef(
    guid="ce41c09a-a66c-5959-98cd-954962c857d0",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bianca.Name",
    display_name="Bianca",
    searchable_by=["Bianca","Supporter","Bianca"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="BW7",
    rarity=Rarities.RareUltra,
    effect=draw_until_effect(6)
)
