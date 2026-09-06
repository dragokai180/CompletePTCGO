from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_basic_pokemon, is_evolution_pokemon


async def brocks_scouting(ctx):
    """Search for up to 2 Basic Pokémon or 1 Evolution Pokémon into hand."""
    want_basics = await ctx.ask_yes_no(
        "Search for up to 2 Basic Pokémon? (No = 1 Evolution Pokémon)"
    )
    if want_basics:
        picks = await ctx.search_deck(
            is_basic_pokemon, count=2, minimum=0,
            prompt="Choose up to 2 Basic Pokémon to put into your hand.",
        )
    else:
        picks = await ctx.search_deck(
            is_evolution_pokemon, count=1, minimum=0,
            prompt="Choose an Evolution Pokémon to put into your hand.",
        )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="1f8cabd2-07ba-585f-b8c1-11d39a5c0a62",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksScouting.Name",
    display_name="Brock's Scouting",
    searchable_by=["Brock's Scouting", "Supporter", "BrocksScouting"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=brocks_scouting,
)
