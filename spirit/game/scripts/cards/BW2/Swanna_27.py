from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import discard_own_energy, hide

card = PokemonCardDef(
    guid="839a607e-2fc8-5d43-b66b-134286849550",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name",
    display_name="Swanna",
    searchable_by=["Swanna","Stage 1","Swanna"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    abilities=[
        Attack(
            title="Wing Dance",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=hide,
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy attached to this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=discard_own_energy,
        ),
    ],
)
