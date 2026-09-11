from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus

async def intuition(ctx):
    if await ctx.ask_yes_no("Draw 2 cards?"):
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="9e0013d9-f88c-511b-b690-ac6cd29065cf",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario","Stage 1","Lucario"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    abilities=[
        Ability(
            title="Intuition",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may draw 2 cards.",
            trigger=Triggers.ON_EVOLVE,
            effect=intuition,
        ),
        Attack(
            title="Fast Punch",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
