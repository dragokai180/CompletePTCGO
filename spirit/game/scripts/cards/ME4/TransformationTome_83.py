from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import thorton, thorton_condition


def _named(card, name):
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == name


def _playable(board, player_id, card):
    """Needs a 2nd Transformation Tome in hand, a Basic in discard, and a
    Basic in play."""
    hand = board.find_player_area(player_id, "hand")
    has_pair = any(
        c.entity_id != card.entity_id and _named(c, "Transformation Tome")
        for c in (hand.children if hand else [])
    )
    return has_pair and thorton_condition(board, player_id)


async def transformation_tome(ctx):
    """Play 2 at once: discard the 2nd copy, then switch a Basic from the
    discard pile with 1 of your Basics in play. Attachments, damage,
    Special Conditions, turns in play, and other effects stay on the new
    Pokémon."""
    pair = next(
        (c for c in ctx.hand()
         if c.entity_id != ctx.source.entity_id
         and _named(c, "Transformation Tome")),
        None,
    )
    if pair is None:
        return
    await ctx.discard_cards([pair])
    await thorton(ctx)


card = ItemCardDef(
    guid="f18b04f2-0260-565c-92d0-09eda43f788a",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TransformationTome.Name",
    display_name="Transformation Tome",
    searchable_by=["Transformation Tome","Item","TransformationTome"],
    subtypes=["Item"],
    collector_number=83,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=_playable,
    effect=transformation_tome,
)
