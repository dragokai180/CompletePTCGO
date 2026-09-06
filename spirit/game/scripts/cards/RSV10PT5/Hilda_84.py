from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty, is_energy_card
from spirit.game.session.effects import is_evolution_pokemon


async def hilda(ctx):
    """Search the deck for an Evolution Pokémon and an Energy card."""
    evolution, energy = await ctx.search_deck_groups(
        [
            (is_evolution_pokemon, 1, "Evolution Pokémon"),
            (is_energy_card, 1, "Energy card"),
        ],
        prompt="Search your deck for an Evolution Pokémon and an Energy card",
    )
    picks = evolution + energy
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="0805f37c-37cf-5367-87a0-5621ad772ea6",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hilda.Name",
    display_name="Hilda",
    searchable_by=["Hilda","Supporter","Hilda"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=hilda,
    condition=deck_nonempty,
)
