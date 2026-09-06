from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card, is_water_energy_card
from spirit.game.session.effects import is_water_pokemon


def _is_basic_water_energy(card):
    return is_basic_energy_card(card) and is_water_energy_card(card)


async def great_haul_net(ctx):
    """Choose 1 or both: shuffle up to 3 Water Pokemon and/or up to 3 Basic
    Water Energy cards from your discard pile into your deck."""
    pokemon = [c for c in ctx.discard_pile() if is_water_pokemon(c)]
    energy = [c for c in ctx.discard_pile() if _is_basic_water_energy(c)]
    picks_p = await ctx.choose_cards(
        pokemon, 3, minimum=0,
        prompt="Choose up to 3 Water Pokémon to shuffle into your deck.",
    ) if pokemon else []
    picks_e = await ctx.choose_cards(
        energy, 3, minimum=0,
        prompt="Choose up to 3 Basic Water Energy cards to shuffle into your deck.",
    ) if energy else []
    picks = picks_p + picks_e
    if picks:
        await ctx.shuffle_into_deck(picks)


card = ItemCardDef(
    guid="bbbbda91-40aa-5f8f-9ee0-f3eb1bcb6e14",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatHaulNet.Name",
    display_name="Great Haul Net",
    searchable_by=["Great Haul Net","Item","GreatHaulNet"],
    subtypes=["Item"],
    collector_number=78,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=great_haul_net,
)
