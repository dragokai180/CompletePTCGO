from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def phoebe(ctx):
    """This turn, your Pokemon VMAX's attack damage ignores effects on the opponent's Active."""
    ctx.ignore_own_target_effects(subtype="VMAX")


card = SupporterCardDef(
    guid="fce91074-8148-5961-a839-e905d8dfb156",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Phoebe.Name",
    display_name="Phoebe",
    searchable_by=["Phoebe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    effect=phoebe,
)
