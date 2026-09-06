from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, Rarities, TrainerType
from spirit.game.session.effects import is_special_energy


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_pokemon_tool_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


def _ruffian_targets(board, player_id):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return []
    out = []
    for pokemon in board.pokemon_in_play(opponent):
        tools = [c for c in pokemon.children if _is_pokemon_tool_card(c)]
        specials = [c for c in pokemon.children if is_special_energy(c)]
        if tools and specials:
            out.append(pokemon)
    return out


def ruffian_condition(board, player_id):
    return bool(_ruffian_targets(board, player_id))


async def ruffian(ctx):
    """Discard a Pokémon Tool and a Special Energy from 1 of your opponent's Pokémon."""
    candidates = _ruffian_targets(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose your opponent's Pokémon"
    )
    if target is None:
        return
    tools = [c for c in target.children if _is_pokemon_tool_card(c)]
    specials = [c for c in target.children if is_special_energy(c)]
    tool_picks = await ctx.choose_cards(
        tools, 1, prompt="Choose a Pokémon Tool to discard.",
    )
    energy_picks = await ctx.choose_cards(
        specials, 1, prompt="Choose a Special Energy to discard.",
    )
    await ctx.discard_cards((tool_picks or []) + (energy_picks or []))


card = SupporterCardDef(
    guid="cd7a3c9b-c3d3-5383-9a11-381909c30235",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ruffian.Name",
    display_name="Ruffian",
    searchable_by=["Ruffian", "Supporter", "Ruffian"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=ruffian_condition,
    effect=ruffian,
)
