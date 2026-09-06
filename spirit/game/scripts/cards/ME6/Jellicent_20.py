from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import deck_nonempty


def _can_draw(board, player_id, pokemon=None):
    return deck_nonempty(board, player_id)


async def deep_draw(ctx):
    """Draw a card. If you do, you may put a card from your hand on the
    bottom of your deck."""
    if not await ctx.draw_cards(1):
        return
    if not ctx.hand():
        return
    if not await ctx.ask_yes_no("Put a card from your hand on the bottom of your deck?"):
        return
    picks = await ctx.choose_cards(
        ctx.hand(), 1, minimum=0,
        prompt="Choose a card to put on the bottom of your deck.",
    )
    if picks:
        await ctx.put_on_bottom_of_deck(picks[0])


card = PokemonCardDef(
    guid="7fd8b63c-5c77-5c57-b947-78656a14afbb",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent","Stage 1","Jellicent"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Ability(
            title="Deep Draw",
            game_text="You may use this Ability once during your turn. Draw a card. If you do, you may put a card from your hand on the bottom of your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_can_draw,
            effect=deep_draw,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
