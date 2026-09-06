from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities


def _prism_tower_condition(board, player_id, stadium):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len(hand.children) >= 2


async def _prism_tower_effect(ctx):
    discarded = await ctx.discard_from_hand(
        2, prompt="Discard 2 cards from your hand to draw a card.",
    )
    if len(discarded) < 2:
        return
    await ctx.draw_cards(1)


PRISM_TOWER_ABILITY = Ability(
    title="Prism Tower",
    game_text="Once during each player's turn, that player may discard 2 cards from their hand in order to draw a card.",
    activation=Activations.ONCE_PER_TURN,
    condition=_prism_tower_condition,
    effect=_prism_tower_effect,
)

card = StadiumCardDef(
    guid="b858c975-bc9e-5532-abe3-f34868d55237",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PrismTower.Name",
    display_name="Prism Tower",
    searchable_by=["Prism Tower","Stadium","PrismTower"],
    subtypes=["Stadium"],
    collector_number=80,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    ability=PRISM_TOWER_ABILITY,
)
