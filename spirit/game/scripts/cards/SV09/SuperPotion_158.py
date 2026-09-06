from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import requires_damaged_pokemon


async def super_potion(ctx):
    """Heal 60 damage from 1 of your Pokémon. If you healed any damage in this
    way, discard an Energy from that Pokémon."""
    candidates = [
        pokemon for pokemon in ctx.my_pokemon_in_play()
        if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
    if target is None:
        return
    healed = await ctx.heal(60, target)
    if healed:
        await ctx.discard_energy_from(
            target, 1, prompt="Discard an Energy from that Pokémon",
        )


card = ItemCardDef(
    guid="b81031be-c19d-5c53-bab4-175f89fe8d30",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion","Item","SuperPotion"],
    subtypes=["Item"],
    collector_number=158,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=super_potion,
    condition=requires_damaged_pokemon(),
)
