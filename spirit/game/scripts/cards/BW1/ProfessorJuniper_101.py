from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import professors_research

async def professor_juniper(ctx):
    """Discard your hand and draw 7 cards. You may play only 1 Supporter card
    during your turn (before your attack)."""
    await professors_research(ctx)
    # Unmatched clause: "You may play only 1 Supporter card during your turn (before your attack)."

card = SupporterCardDef(
    guid="d2619164-a038-5106-9538-099ae9ea958f",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorJuniper.Name",
    display_name="Professor Juniper",
    searchable_by=["Professor Juniper","Supporter","ProfessorJuniper"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=professor_juniper
)
