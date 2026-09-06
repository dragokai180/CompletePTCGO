from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_supporter_card
from spirit.game.card_effects.passives_common import is_in_active_spot


async def attract_customers(ctx):
    """Once during your turn (while Active): look at top 6, put supporter into hand."""
    top = ctx.deck_top(6)
    supporters = [c for c in top if is_supporter_card(c)]
    if supporters:
        picks = await ctx.choose_cards(
            supporters,
            1,
            minimum=0,
            prompt="Choose a Supporter card to put into your hand.",
            display_cards=top,
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    # Regardless of whether you found a Supporter, return the other cards.
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ee07a70c-8119-464c-aaa6-33ba0833904a",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name",
    display_name="Tatsugiri",
    searchable_by=["Tatsugiri", "Basic", "Tatsugiri"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    abilities=[
        Ability(
            title="Attract Customers",
            game_text=(
                "Once during your turn, if this Pokémon is in the Active Spot, "
                "you may look at the top 6 cards of your deck, reveal a Supporter "
                "card you find there, and put it into your hand. Shuffle the "
                "other cards back into your deck."
            ),
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: is_in_active_spot(pokemon),
            effect=attract_customers,
        ),
        Attack(
            title="Surf",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)

