from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card, is_energy_card
from spirit.game.session.effects import is_special_energy


def _is_basic_fire_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIRE.value)


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
    )


def _blowtorch_targets(board, player_id):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    targets = []
    if opponent:
        for pokemon in board.pokemon_in_play(opponent):
            for child in pokemon.children:
                if _is_tool(child) or (is_energy_card(child) and is_special_energy(child)):
                    targets.append(child)
    stadium_area = board.find_global_area("activeStadium")
    targets.extend(stadium_area.children if stadium_area else [])
    return targets


def blowtorch_condition(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(_is_basic_fire_energy(c) for c in hand.children):
        return False
    return bool(_blowtorch_targets(board, player_id))


async def blowtorch(ctx):
    """Discard a Basic Fire Energy from hand, then discard a Tool or Special
    Energy from 1 of your opponent's Pokémon, or a Stadium in play."""
    discarded = await ctx.discard_from_hand(
        1, predicate=_is_basic_fire_energy,
        prompt="Discard a Basic Fire Energy card",
    )
    if not discarded:
        return
    targets = _blowtorch_targets(ctx.board, ctx.player_id)
    if not targets:
        return
    picks = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose a Pokémon Tool, Special Energy, or Stadium to discard.",
    )
    await ctx.discard_cards(picks)


card = ItemCardDef(
    guid="0397f63f-37f4-5feb-bbdb-40d7cedd0414",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blowtorch.Name",
    display_name="Blowtorch",
    searchable_by=["Blowtorch","Item","Blowtorch"],
    subtypes=["Item"],
    collector_number=86,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=blowtorch,
    condition=blowtorch_condition,
)
