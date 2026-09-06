from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, SpecialConditions
from spirit.game.card_effects.trainers import is_darkness_pokemon


async def dark_bell(ctx):
    """Both Active non-Darkness Pokemon are now Confused."""
    for pokemon in (ctx.my_active(), ctx.opponent_active()):
        if pokemon is not None and not is_darkness_pokemon(pokemon):
            await ctx.apply_special_condition(pokemon, SpecialConditions.CONFUSED)


card = ItemCardDef(
    guid="1ba045ba-0a51-556c-a326-6328e3550ed7",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkBell.Name",
    display_name="Dark Bell",
    searchable_by=["Dark Bell","Item","DarkBell"],
    subtypes=["Item"],
    collector_number=75,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=dark_bell,
)
