from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.trainers import is_basic_energy_card


NIGHT_STRETCHER_GUID = "5373ca9e-2b8b-49d2-9758-ed83cfe47924"


async def night_stretcher(ctx):
    candidates = [
        c for c in ctx.discard_pile()
        if is_pokemon_card(c) or is_basic_energy_card(c)
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates,
        1,
        minimum=1,
        prompt="Choose a Pokémon or Basic Energy card to put into your hand.",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = ItemCardDef(
    guid=NIGHT_STRETCHER_GUID,
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightStretcher.Name",
    display_name="Night Stretcher",
    searchable_by=["Night Stretcher", "Item", "NightStretcher"],
    subtypes=["Item"],
    collector_number=61,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=night_stretcher,
)

