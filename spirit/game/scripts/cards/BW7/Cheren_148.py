from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

async def cheren(ctx):
    """Draw 3 cards. You may play only 1 Supporter card during your turn
    (before your attack)."""
    await draw_attack(3)(ctx)
    # Unmatched clause: "You may play only 1 Supporter card during your turn (before your attack)."

card = SupporterCardDef(
    guid="7bc7295f-d685-5dec-bd72-24d31c38f2cd",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cheren.Name",
    display_name="Cheren",
    searchable_by=["Cheren","Supporter","Cheren"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="BW7",
    rarity=Rarities.RareUltra,
    effect=draw_attack(3)
)
