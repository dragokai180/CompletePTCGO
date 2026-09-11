from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities

async def devour(ctx):
    """For each of your Durant in play, discard the top card of your opponent's
    deck."""
    count = sum(
        1 for p in ctx.my_pokemon_in_play()
        if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Durant"
    )
    if count:
        await ctx.discard_cards(ctx.deck_top(count, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="f1a8f96c-a6e2-582c-88aa-4c89c0bc299a",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant","Basic","Durant"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Devour",
            game_text="For each of your Durant in play, discard the top card of your opponent's deck.",
            cost={PokemonTypes.METAL: 1},
            effect=devour,
        ),
        Attack(
            title="Vice Grip",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
