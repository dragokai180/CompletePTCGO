from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6d6f3e9b-34d0-52d1-aa8d-007aabb92650",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLatiasex.Name",
    display_name="Mega Latias ex",
    searchable_by=["Mega Latias ex", "Basic", "MegaLatiasex"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title="Illusory Impulse",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=300,
            effect=standard_attack,
        ),
    ],
)
