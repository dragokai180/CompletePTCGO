from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import AttrID, Rarities, TrainerType
from spirit.game.session.passives import effective_max_hp


def community_center_condition(board, player_id, stadium):
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return False
    if not any(
        trainer_type == TrainerType.SUPPORTER.value
        for _, _, trainer_type in ts.trainers_played
    ):
        return False
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in board.pokemon_in_play(player_id)
    )


async def community_center_ability(ctx):
    """If you played a Supporter this turn, heal 10 from each of your Pokémon."""
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(10, pokemon)


card = StadiumCardDef(
    guid="2601659d-2b82-5c70-a0a4-717bf6924eb0",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CommunityCenter.Name",
    display_name="Community Center",
    searchable_by=["Community Center","Stadium","CommunityCenter"],
    subtypes=["Stadium"],
    collector_number=146,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Community Center",
        game_text="Once during each player's turn, if they played a Supporter card from their hand this turn, they may heal 10 damage from each of their Pokémon.",
        activation=Activations.ONCE_PER_TURN,
        effect=community_center_ability,
        condition=community_center_condition,
    ),
)
