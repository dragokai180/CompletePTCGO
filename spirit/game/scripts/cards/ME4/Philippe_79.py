from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_metal_energy_card, is_basic_energy_card


def _is_basic_metal_energy(card):
    return is_basic_energy_card(card) and is_metal_energy_card(card)


def _is_metal_pokemon(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.METAL.value in types


def _philippe_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    has_energy = bool(discard) and any(_is_basic_metal_energy(c) for c in discard.children)
    has_metal = any(_is_metal_pokemon(p) for p in board.pokemon_in_play(player_id))
    return has_energy and has_metal


async def philippe(ctx):
    """Attach up to 2 Basic Metal Energy cards from your discard pile to 1 of
    your Metal Pokemon."""
    energy = [c for c in ctx.discard_pile() if _is_basic_metal_energy(c)]
    targets = [p for p in ctx.my_pokemon_in_play() if _is_metal_pokemon(p)]
    if not energy or not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your Metal Pokémon")
    if target is None:
        return
    picks = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 Basic Metal Energy cards to attach.",
    )
    for card in picks:
        await ctx.attach_energy(card, target)


card = SupporterCardDef(
    guid="57f2936a-751b-5173-9e7c-962bae1a441f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Philippe.Name",
    display_name="Philippe",
    searchable_by=["Philippe","Supporter","Philippe"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=philippe,
    condition=_philippe_condition,
)
