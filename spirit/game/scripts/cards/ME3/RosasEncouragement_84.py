from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import more_prizes_remaining_than_opponent
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_stage2_pokemon


def _rosas_condition(board, player_id):
    if not more_prizes_remaining_than_opponent(board, player_id):
        return False
    discard = board.find_player_area(player_id, "discard")
    has_energy = bool(discard) and any(is_basic_energy_card(c) for c in discard.children)
    has_stage2 = any(is_stage2_pokemon(p) for p in board.pokemon_in_play(player_id))
    return has_energy and has_stage2


async def rosas_encouragement(ctx):
    """You can use this card only if you have more Prize cards remaining than
    your opponent. Attach up to 2 Basic Energy cards from your discard pile
    to 1 of your Stage 2 Pokémon."""
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    targets = [p for p in ctx.my_pokemon_in_play() if is_stage2_pokemon(p)]
    if not energy or not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your Stage 2 Pokémon")
    if target is None:
        return
    picks = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 Basic Energy cards to attach.",
    )
    for card in picks:
        await ctx.attach_energy(card, target)


card = SupporterCardDef(
    guid="d999eb9a-921a-5d50-abc7-a907f4d7b9a8",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RosasEncouragement.Name",
    display_name="Rosa's Encouragement",
    searchable_by=["Rosa's Encouragement", "Supporter", "RosasEncouragement"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=rosas_encouragement,
    condition=_rosas_condition,
)
