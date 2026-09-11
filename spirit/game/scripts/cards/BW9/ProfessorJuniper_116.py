from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import professors_research

async def professor_juniper(ctx):
    """Discard your hand and draw 7 cards. You may play only 1 Supporter card
    during your turn (before your attack)."""
    await professors_research(ctx)
    # Unmatched clause: "You may play only 1 Supporter card during your turn (before your attack)."

card = SupporterCardDef(
    guid="a8435051-9202-5c3c-9a68-6e32b1d9303a",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorJuniper.Name",
    display_name="Professor Juniper",
    searchable_by=["Professor Juniper","Supporter","ProfessorJuniper"],
    subtypes=["Supporter"],
    collector_number=116,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    effect=professor_juniper
)
