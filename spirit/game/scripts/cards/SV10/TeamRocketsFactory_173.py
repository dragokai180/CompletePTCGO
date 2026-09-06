from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, TrainerType


def _team_rocket_supporter_played(board, player_id, stadium=None) -> bool:
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return False
    for archetype_id, name, trainer_type in ts.trainers_played:
        if trainer_type == TrainerType.SUPPORTER.value and "Team Rocket" in (name or ""):
            return True
    return False


async def team_rockets_factory(ctx):
    """If you played a Team Rocket Supporter this turn, draw 2 cards."""
    await ctx.draw_cards(2)


card = StadiumCardDef(
    guid="57d502b1-8f81-5212-a009-a321067ea92d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsFactory.Name",
    display_name="Team Rocket's Factory",
    searchable_by=["Team Rocket's Factory", "Stadium", "TeamRocketsFactory"],
    subtypes=["Stadium"],
    collector_number=173,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Team Rocket's Factory",
        game_text="Once during each player's turn, if they played a Supporter card that has \"Team Rocket\" in its name from their hand this turn, they may draw 2 cards.",
        activation=Activations.ONCE_PER_TURN,
        condition=_team_rocket_supporter_played,
        effect=team_rockets_factory,
    ),
)
