from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack
from spirit.game.card_effects.passives_common import is_in_active_spot


async def run_away_draw(ctx):
    """Draw 3 cards. If you drew any, shuffle this Pokémon and all attached
    cards into your deck."""
    drawn = await ctx.draw_cards(3)
    if not drawn:
        return
    was_active = is_in_active_spot(ctx.source)
    await ctx.shuffle_into_deck(full_stack(ctx.source), ctx.player_id)
    if not was_active:
        return

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.player_id):
            screen_name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(
                ctx.opponent_id, f"{screen_name} has no Pokémon left"
            )

    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="952db3e7-161e-52bb-be67-17ed965eea7e",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dudunsparce.Name",
    display_name="Dudunsparce",
    searchable_by=["Dudunsparce", "Stage 1", "Dudunsparce"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    family_id=206,
    abilities=[
        Ability(
            title="Run Away Draw",
            game_text="Once during your turn, you may draw 3 cards. If you drew any cards in this way, shuffle this Pokémon and all attached cards into your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=run_away_draw,
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
