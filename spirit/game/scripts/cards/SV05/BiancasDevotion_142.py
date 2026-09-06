from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.session.passives import effective_max_hp


def _bianca_targets(board, player_id):
    return [
        p for p in board.pokemon_in_play(player_id)
        if p.get_attribute(AttrID.HP, 0) <= 30
        and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
    ]


def biancas_devotion_playable(board, player_id):
    return bool(_bianca_targets(board, player_id))


async def biancas_devotion(ctx):
    """Heal all damage from 1 of your Pokémon that has 30 HP or less remaining."""
    target = await ctx.choose_pokemon(
        _bianca_targets(ctx.board, ctx.player_id),
        "Choose a Pokémon with 30 HP or less remaining",
    )
    if target is None:
        return
    await ctx.heal(ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0), target)


card = SupporterCardDef(
    guid="ac8f036b-069f-5396-ba3b-3449c4bbf9bb",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BiancasDevotion.Name",
    display_name="Bianca's Devotion",
    searchable_by=["Bianca's Devotion","Supporter","BiancasDevotion"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=biancas_devotion,
    condition=biancas_devotion_playable,
)
