from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    AttrID, PokemonStage, PokemonTypes, Rarities, TrainerType,
)


async def scorching_earth(ctx):
    """40. If the opponent has a Stadium, discard it; if you do, they can't
    play Stadiums during their next turn."""
    await ctx.deal_damage()
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        discarded = await ctx.discard_stadium()
        if discarded is not None:
            ctx.lock_plays(
                ctx.opponent_id,
                lambda c: c.get_attribute(AttrID.TRAINER_TYPE)
                == TrainerType.STADIUM.value,
            )


card = PokemonCardDef(
    guid="e831ca8e-3e36-5711-85d9-ccd3c2a60baa",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu","Basic","ChiYu"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    family_id=1004,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Scorching Earth",
            game_text="If your opponent has a Stadium in play, discard it. If you do, your opponent can't play any Stadium cards from their hand during their next turn.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=scorching_earth,
        ),
    ],
)
