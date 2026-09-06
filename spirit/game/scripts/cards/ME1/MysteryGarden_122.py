from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_energy_card


def _is_psychic_pokemon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.PSYCHIC.value in types


def mystery_garden_condition(board, player_id, stadium=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_energy_card(c) for c in hand.children)


async def mystery_garden(ctx):
    """Discard an Energy from hand, then draw until the hand has as many
    cards as you have Psychic Pokémon in play."""
    discarded = await ctx.discard_from_hand(
        1, predicate=is_energy_card,
        prompt="Discard an Energy card from your hand",
    )
    if not discarded:
        return
    psychic = sum(1 for p in ctx.my_pokemon_in_play() if _is_psychic_pokemon(p))
    await ctx.draw_until(psychic)


MYSTERY_GARDEN_ABILITY = Ability(
    title="Mystery Garden",
    game_text="Once during each player's turn, that player may discard an Energy card from their hand in order to draw cards until they have as many cards in their hand as they have Psychic Pokémon in play.",
    activation=Activations.ONCE_PER_TURN,
    effect=mystery_garden,
    condition=mystery_garden_condition,
)


card = StadiumCardDef(
    guid="242afd0a-05d4-5ab4-be56-29ca112022f3",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryGarden.Name",
    display_name="Mystery Garden",
    searchable_by=["Mystery Garden","Stadium","MysteryGarden"],
    subtypes=["Stadium"],
    collector_number=122,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    ability=MYSTERY_GARDEN_ABILITY,
)
