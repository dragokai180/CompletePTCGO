from spirit.game.data_utils import SupporterCardDef, is_pokemon_ex, subtypes_for
from spirit.game.attributes import AttrID, Rarities
from spirit.game.session.passives import effective_max_hp


def _is_mega_ex(pokemon):
    return "SV_Mega" in subtypes_for(pokemon.archetype_id) and is_pokemon_ex(
        pokemon.archetype_id)


def wally_condition(board, player_id):
    return any(
        _is_mega_ex(p) and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in board.pokemon_in_play(player_id)
    )


async def wallys_compassion(ctx):
    """Heal all damage from 1 of your Mega Evolution Pokémon ex. If you
    healed any damage in this way, put all Energy attached to that Pokémon
    into your hand."""
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if _is_mega_ex(p) and p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Mega Evolution Pokémon ex to heal"
    )
    if target is None:
        return
    damage = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
    if damage <= 0:
        return
    await ctx.heal(damage, target)
    energies = list(ctx.attached_energies(target))
    if energies:
        await ctx.put_in_hand(energies, reveal=False)


card = SupporterCardDef(
    guid="b5b6f139-5b2a-588b-9fe9-dac5663ec536",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WallysCompassion.Name",
    display_name="Wally's Compassion",
    searchable_by=["Wally's Compassion","Supporter","WallysCompassion"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=wallys_compassion,
    condition=wally_condition,
)
