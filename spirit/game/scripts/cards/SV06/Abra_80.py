from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.session.effects import full_stack


async def teleporter(ctx):
    """Once during your turn, if Active, shuffle this Pokémon and all attached
    cards into your deck."""
    if not await ctx.ask_yes_no(
        "Shuffle this Pokémon and all attached cards into your deck?"
    ):
        return
    was_active = ctx.source is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(ctx.source), ctx.player_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="4dde62bb-a606-5bbb-8ef5-0c7321889feb",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    display_name="Abra",
    searchable_by=["Abra","Basic","Abra"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    family_id=63,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Teleporter",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may shuffle it and all attached cards into your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=teleporter,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
