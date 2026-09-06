from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_hand, place_counters


async def psychic_draw(ctx):
    """Once during your turn, when you play this Pokémon from your hand to
    evolve 1 of your Pokémon, you may use this Ability. Draw 3 cards."""
    if await ctx.ask_yes_no("Draw 3 cards?"):
        await ctx.draw_cards(3)

card = PokemonCardDef(
    guid="29097bd7-5d59-5c9a-87a9-52b4614b677b",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name",
    display_name="Alakazam",
    searchable_by=["Alakazam","Stage 2","Alakazam"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Psychic Draw",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Draw 3 cards.",
            trigger=Triggers.ON_EVOLVE,
            effect=psychic_draw,
        ),
        Attack(
            title="Powerful Hand",
            game_text="Place 2 damage counters on your opponent's Active Pokémon for each card in your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(lambda ctx: 2 * count_hand()(ctx)),
        ),
    ],
)
