from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import shady_dealings


def _has_tera_in_play(board, player_id) -> bool:
    return any(
        "Tera" in subtypes_for(p.archetype_id)
        for p in board.pokemon_in_play(player_id)
    )


async def jewel_seeker(ctx):
    """On evolve: if you have any Tera Pokémon in play, you may search for up
    to 2 Trainer cards."""
    if not _has_tera_in_play(ctx.board, ctx.player_id):
        return
    if not await ctx.ask_yes_no(
        "Search your deck for up to 2 Trainer cards?"
    ):
        return
    await shady_dealings(2)(ctx)


card = PokemonCardDef(
    guid="6d7fb176-e285-508e-8e3f-2259ff603526",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1", "Noctowl"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Ability(
            title="Jewel Seeker",
            game_text=(
                "Once during your turn, when you play this Pokémon from your "
                "hand to evolve 1 of your Pokémon, if you have any Tera Pokémon "
                "in play, you may search your deck for up to 2 Trainer cards, "
                "reveal them, and put them into your hand. Then, shuffle your deck."
            ),
            trigger=Triggers.ON_EVOLVE,
            effect=jewel_seeker,
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
