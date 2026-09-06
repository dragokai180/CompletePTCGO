from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_psychic_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.PSYCHIC.value
    )


def _is_psychic_pokemon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.PSYCHIC.value in types


def _wondrous_patch_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    has_energy = bool(discard) and any(_is_basic_psychic_energy(c) for c in discard.children)
    bench = board.find_player_area(player_id, "bench")
    has_bench = bool(bench) and any(_is_psychic_pokemon(p) for p in bench.children)
    return has_energy and has_bench


async def wondrous_patch(ctx):
    """Attach a Basic Psychic Energy card from your discard pile to 1 of your
    Benched Psychic Pokémon."""
    energy = [c for c in ctx.discard_pile() if _is_basic_psychic_energy(c)]
    bench = [p for p in ctx.my_bench() if _is_psychic_pokemon(p)]
    if not energy or not bench:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a Basic Psychic Energy card to attach.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Psychic Pokémon")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = ItemCardDef(
    guid="6f13739e-b910-5ab1-841c-ddde84ebb3cd",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousPatch.Name",
    display_name="Wondrous Patch",
    searchable_by=["Wondrous Patch", "Item", "WondrousPatch"],
    subtypes=["Item"],
    collector_number=94,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=wondrous_patch,
    condition=_wondrous_patch_condition,
)
