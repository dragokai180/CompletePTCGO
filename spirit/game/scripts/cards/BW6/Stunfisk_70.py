from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter, steamroll

card = PokemonCardDef(
    guid="cfb4e171-6f83-5e7f-9e79-5155d79f34e8",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk","Basic","Stunfisk"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Muddy Water",
            game_text="Does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=steamroll,
        ),
        Attack(
            title="Rumble",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=dark_clamp,
        ),
    ],
)
