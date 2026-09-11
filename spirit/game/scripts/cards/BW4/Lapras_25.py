from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, recoil_attack
from spirit.game.card_effects.support_common import search_to_bench

card = PokemonCardDef(
    guid="52e0eca3-1dc7-52be-ba5f-e6e04ac2d261",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras","Basic","Lapras"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=recoil_attack(20),
        ),
    ],
)
