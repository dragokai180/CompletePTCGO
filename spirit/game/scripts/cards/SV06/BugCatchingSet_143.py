from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_grass_pokemon(card) -> bool:
    if not is_pokemon_card(card):
        return False
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.GRASS.value in types


def _is_basic_grass_energy(card) -> bool:
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.GRASS.value
    )


async def bug_catching_set(ctx):
    top = ctx.deck_top(7)
    eligible = [
        c for c in top if _is_grass_pokemon(c) or _is_basic_grass_energy(c)
    ]
    if eligible:
        picks = await ctx.choose_cards(
            eligible,
            2,
            minimum=0,
            prompt="Choose up to 2 cards from the top 7.",
            display_cards=top,
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="66bb95d2-f011-44b4-92b8-e61abec2a3e3",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BugCatchingSet.Name",
    display_name="Bug Catching Set",
    searchable_by=["Bug Catching Set", "Item"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=bug_catching_set,
)

