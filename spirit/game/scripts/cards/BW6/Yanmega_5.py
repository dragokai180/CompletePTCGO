from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import hide

card = PokemonCardDef(
    guid="40da687b-8034-5712-8c8f-fccd2cc15b23",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name="Yanmega",
    searchable_by=["Yanmega","Stage 1","Yanmega"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=hide,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
