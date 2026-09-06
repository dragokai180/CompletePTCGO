from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (
    has_pokemon_or_basic_energy_in_discard,
    pokemon_or_basic_energy,
)

async def max_rod(ctx):
    """Put up to 5 in any combination of Pokémon and Basic Energy cards from
    your discard pile into your hand."""
    candidates = pokemon_or_basic_energy(ctx.discard_pile())
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates,
        5,
        minimum=0,
        prompt="Choose up to 5 Pokémon and/or Basic Energy cards to put into your hand.",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = ItemCardDef(
    guid="f41f9293-664f-5755-844a-4212f9380446",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRod.Name",
    display_name="Max Rod",
    searchable_by=["Max Rod", "Item", "ACE SPEC", "MaxRod"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=116,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Ace,
    condition=has_pokemon_or_basic_energy_in_discard,
    effect=max_rod,
)
