from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card


async def find_a_friend(ctx):
    """Search your deck for a Pokémon, reveal it, and put it into your hand.
    Then, shuffle your deck."""
    picks = await ctx.search_deck(
        predicate=is_pokemon_card,
        count=1,
        minimum=0,
        prompt="Choose a Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="1b502ea4-8a96-4634-894e-39ee40083256",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    display_name="Applin",
    searchable_by=["Applin", "Basic", "Applin"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=840,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text=(
                "Search your deck for a Pokémon, reveal it, and put it into "
                "your hand. Then, shuffle your deck."
            ),
            cost={PokemonTypes.COLORLESS: 1},
            effect=find_a_friend,
        ),
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
    ],
)

