from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, TrainerType, Rarities
from spirit.game.card_effects.pokemon import is_energy_card


TENACITY_GUID = "baa71d04-6a75-4a86-bb38-47e0c579cfdc"


def _is_stadium_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


async def colresss_tenacity(ctx):
    stadiums, energies = await ctx.search_deck_groups(
        [
            (_is_stadium_card, 1, "Stadium card"),
            (is_energy_card, 1, "Energy card"),
        ],
        prompt="Search your deck for a Stadium card and an Energy card",
    )
    if not stadiums or not energies:
        return
    await ctx.put_in_hand(stadiums + energies, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid=TENACITY_GUID,
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColresssTenacity.Name",
    display_name="Colress's Tenacity",
    searchable_by=["Colress's Tenacity", "Supporter", "ColresssTenacity"],
    subtypes=["Supporter"],
    collector_number=57,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=colresss_tenacity,
)

