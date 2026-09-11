from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import hide

card = PokemonCardDef(
    guid="5ef2d8fb-a5d2-5002-8ab0-60cd4eb6f248",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    display_name="Kakuna",
    searchable_by=["Kakuna","Stage 1","Kakuna"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            effect=hide,
        ),
    ],
)
