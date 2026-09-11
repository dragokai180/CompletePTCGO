from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot

def _is_basic_darkness_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.DARKNESS.value in types

def _is_benched_darkness_pokemon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return not is_in_active_spot(pokemon) and PokemonTypes.DARKNESS.value in types

def _dark_patch_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    bench_children = bench.children if bench else []
    if not any(_is_benched_darkness_pokemon(p) for p in bench_children):
        return False
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_is_basic_darkness_energy(c) for c in discard.children)

async def dark_patch(ctx):
    """Attach a basic Darkness Energy card from your discard pile to 1 of your
    Benched Darkness Pokemon. You may play as many Item cards as you like
    during your turn (before your attack)."""
    energy = [c for c in ctx.discard_pile() if _is_basic_darkness_energy(c)]
    bench = [p for p in ctx.my_bench() if _is_benched_darkness_pokemon(p)]
    if not energy or not bench:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a basic Darkness Energy card to attach.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your Benched Darkness Pokémon"
    )
    if target is not None:
        await ctx.attach_energy(picks[0], target)

card = ItemCardDef(
    guid="c44bc391-e593-5306-890a-219ff24b55e3",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkPatch.Name",
    display_name="Dark Patch",
    searchable_by=["Dark Patch","Item","DarkPatch"],
    subtypes=["Item"],
    collector_number=93,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=dark_patch,
    condition=_dark_patch_condition
)
