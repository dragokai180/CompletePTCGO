from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import big_swing, hypnostrike, shred, stellar_guidance

card = PokemonCardDef(
    guid="751f28df-bfdf-50e8-b190-53b2f3b7bcb0",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke","Basic","Slowpoke"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Big Yawn",
            game_text="Both this Pokémon and the Defending Pokémon are now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=hypnostrike,
        ),
        Attack(
            title="Shot in the Dark",
            game_text="Flip 2 coins. If either of them is tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=big_swing,
        ),
    ],
)
