from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def recon_directive(ctx):
    """Look at the top 2 cards; put 1 into your hand and the other on
    the bottom of your deck."""
    top = ctx.deck_top(2)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1,
        prompt="Choose 1 of the top 2 cards to put into your hand.",
        display_cards=top,
    )
    if not picks:
        return
    chosen = picks[0]
    await ctx.put_in_hand([chosen], reveal=False)
    remaining = [c for c in top if c is not chosen]
    if remaining:
        await ctx.put_on_bottom_of_deck(remaining[0])


card = PokemonCardDef(
    guid="177b666d-9e56-4c45-90cf-981cbd51672c",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    display_name="Drakloak",
    searchable_by=["Drakloak", "Stage 1", "Drakloak"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    family_id=885,
    abilities=[
        Ability(
            title="Recon Directive",
            game_text=(
                "Once during your turn, you may look at the top 2 cards of "
                "your deck and put 1 of them into your hand. Put the other "
                "card on the bottom of your deck."
            ),
            activation=Activations.ONCE_PER_TURN,
            effect=recon_directive,
        ),
        Attack(
            title="Dragon Headbutt",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=70,
        ),
    ],
)

