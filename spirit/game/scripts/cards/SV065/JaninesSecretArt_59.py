from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.trainers import (
    is_basic_energy_card, is_darkness_pokemon,
)


def _is_basic_darkness_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.DARKNESS.value in types


def janine_condition(board, player_id):
    return any(is_darkness_pokemon(p) for p in board.pokemon_in_play(player_id))


async def janines_secret_art(ctx):
    """Choose up to 2 Darkness Pokémon; attach a Basic Darkness Energy from
    the deck to each. If the Active received Energy, it is Poisoned."""
    darkness = [p for p in ctx.my_pokemon_in_play() if is_darkness_pokemon(p)]
    if not darkness:
        return
    picks = await ctx.choose_cards(
        darkness, min(2, len(darkness)), minimum=0,
        prompt="Choose up to 2 Darkness Pokémon",
    )
    active = ctx.my_active()
    attached_to_active = False
    for pokemon in picks:
        energies = await ctx.search_deck(
            _is_basic_darkness_energy, count=1, minimum=0,
            prompt="Choose a Basic Darkness Energy card to attach.",
        )
        if not energies:
            continue
        await ctx.attach_energy(energies[0], pokemon)
        if pokemon is active:
            attached_to_active = True
    await ctx.shuffle_deck()
    if attached_to_active and active is not None:
        await ctx.apply_special_condition(active, SpecialConditions.POISONED)


card = SupporterCardDef(
    guid="cec08525-6f8d-5c01-9bbf-c988a0fa91c9",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JaninesSecretArt.Name",
    display_name="Janine's Secret Art",
    searchable_by=["Janine's Secret Art","Supporter","JaninesSecretArt"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=janines_secret_art,
    condition=janine_condition,
)
