"""Mysterious Treasure (SM - Forbidden Light 113/131).

  "Discard a card from your hand. If you do, search your deck for a Psychic
   or Dragon Pokemon, reveal it, and put it into your hand. Then, shuffle
   your deck."

Mega Signal's search with a different predicate, behind Quick Ball's cost:
the discard comes first and gates the rest ("if you do"), and
hand_size_at_least(2) keeps the card off the table when there is nothing to
pay with. The search itself is the shared search_to_hand rather than a
re-spelling of search / put_in_hand / shuffle -- reveal=True because the
text says "reveal it".
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import hand_size_at_least
from spirit.game.session.effects import is_pokemon_card

_WANTED_TYPES = (PokemonTypes.PSYCHIC.value, PokemonTypes.DRAGON.value)

_search = search_to_hand(
    lambda card: _is_psychic_or_dragon(card), count=1, minimum=0, reveal=True,
    prompt="Choose a Psychic or Dragon Pokémon to put into your hand.",
)


def _is_psychic_or_dragon(card) -> bool:
    if not is_pokemon_card(card):
        return False
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return any(t in _WANTED_TYPES for t in types)


async def mysterious_treasure(ctx):
    """Pay a card from hand, then fetch a Psychic or Dragon Pokémon."""
    if not await ctx.discard_from_hand(
            1, prompt="Discard a card for Mysterious Treasure"):
        return
    await _search(ctx)


card = ItemCardDef(
    guid="e4c0fe58-9836-570d-8aa9-22fd1452d245",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousTreasure.Name",
    display_name="Mysterious Treasure",
    searchable_by=["Mysterious Treasure", "Item", "MysteriousTreasure"],
    subtypes=["Item"],
    collector_number=113,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=mysterious_treasure,
    condition=hand_size_at_least(2),
)
