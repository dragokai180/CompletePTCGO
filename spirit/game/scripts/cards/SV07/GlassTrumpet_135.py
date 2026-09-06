from spirit.game.data_utils import ItemCardDef, subtypes_for
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_benched_colorless(pokemon) -> bool:
    parent = pokemon.parent
    if parent is None or parent.get_attribute(AttrID.NAME) != "bench":
        return False
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.COLORLESS.value in types


def _has_tera_in_play(board, player_id) -> bool:
    return any(
        "Tera" in subtypes_for(p.archetype_id)
        for p in board.pokemon_in_play(player_id)
    )


def _glass_trumpet_condition(board, player_id) -> bool:
    if not _has_tera_in_play(board, player_id):
        return False
    discard = board.find_player_area(player_id, "discard")
    if not discard or not any(is_basic_energy_card(c) for c in discard.children):
        return False
    return any(_is_benched_colorless(p) for p in board.pokemon_in_play(player_id))


async def glass_trumpet(ctx):
    """Choose up to 2 Benched [C] Pokémon; attach a Basic Energy from discard
    to each."""
    candidates = [p for p in ctx.my_bench() if _is_benched_colorless(p)]
    if not candidates:
        return
    targets = await ctx.choose_cards(
        candidates, 2, minimum=0,
        prompt="Choose up to 2 of your Benched Colorless Pokémon.",
    )
    for target in targets:
        energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not energies:
            break
        picks = await ctx.choose_cards(
            energies, 1,
            prompt="Choose a Basic Energy to attach.",
        )
        if picks:
            await ctx.attach_energy(picks[0], target)


card = ItemCardDef(
    guid="e172c8bb-ad92-5da8-9857-5c95e92dd1e4",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlassTrumpet.Name",
    display_name="Glass Trumpet",
    searchable_by=["Glass Trumpet", "Item", "GlassTrumpet"],
    subtypes=["Item"],
    collector_number=135,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_glass_trumpet_condition,
    effect=glass_trumpet,
)
