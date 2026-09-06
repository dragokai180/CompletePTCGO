from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities, TrainerType
from spirit.game.session.effects import is_item_card, is_supporter_card


def _secret_box_condition(board, player_id, card) -> bool:
    # Must discard 3 other cards from hand => at least 4 cards including
    # Secret Box itself.
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) >= 4


def _is_pokemon_tool_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value


def _is_stadium_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


async def secret_box_effect(ctx):
    # Pay the discard cost: discard 3 other cards from your hand.
    discarded = await ctx.discard_from_hand(
        3,
        minimum=3,
        exclude=[ctx.source],
        prompt="Choose 3 cards to discard for Secret Box",
    )
    if not discarded or len(discarded) != 3:
        return

    items, tools, supporters, stadiums = await ctx.search_deck_groups(
        [
            (is_item_card, 1, "Item card"),
            (_is_pokemon_tool_card, 1, "Pokémon Tool card"),
            (is_supporter_card, 1, "Supporter card"),
            (_is_stadium_card, 1, "Stadium card"),
        ],
        prompt="Search your deck for 1 Item card, 1 Pokémon Tool, 1 Supporter card, and 1 Stadium card.",
    )
    await ctx.put_in_hand(items + tools + supporters + stadiums, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="1c7233ec-0746-4f36-853e-cbafc411dffb",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SecretBox.Name",
    display_name="Secret Box",
    searchable_by=["Secret Box", "Item", "ACE SPEC", "SecretBox"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=163,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Ace,
    condition=_secret_box_condition,
    effect=secret_box_effect,
)

