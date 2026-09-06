from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import (
    is_basic_pokemon,
    is_stage1_pokemon,
    is_stage2_pokemon,
)


async def dawn(ctx):
    """Search your deck for a Basic Pokémon, a Stage 1 Pokémon, and a Stage 2
    Pokémon, reveal them, and put them into your hand. Then, shuffle your deck."""
    picks = []
    for predicate, prompt in (
        (is_basic_pokemon, "Choose a Basic Pokémon to put into your hand."),
        (is_stage1_pokemon, "Choose a Stage 1 Pokémon to put into your hand."),
        (is_stage2_pokemon, "Choose a Stage 2 Pokémon to put into your hand."),
    ):
        picks.extend(await ctx.search_deck(
            predicate, count=1, minimum=0, prompt=prompt,
        ))
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="cdcb61ab-7c9b-5c5b-abcd-b28d55b971b5",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dawn.Name",
    display_name="Dawn",
    searchable_by=["Dawn", "Supporter", "Dawn"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=dawn,
)
