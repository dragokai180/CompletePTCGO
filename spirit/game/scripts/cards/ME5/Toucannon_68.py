from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per


async def aerial_draw(ctx):
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="1a2da5ca-af4f-5a1e-873f-8dbe440cf52b",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toucannon.Name",
    display_name="Toucannon",
    searchable_by=["Toucannon","Stage 2","Toucannon"],
    subtypes=["Stage 2"],
    collector_number=68,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    family_id=731,
    abilities=[
        Ability(
            title="Aerial Draw",
            game_text="Once during your turn, you may use this Ability. Draw a card.",
            activation=Activations.ONCE_PER_TURN,
            effect=aerial_draw,
        ),
        Attack(
            title="Feather Rondo",
            game_text="This attack does 20 more damage for each Benched Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_bench("both"), 20, base=60),
        ),
    ],
)
