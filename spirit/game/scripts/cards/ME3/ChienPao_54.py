from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="94439f45-2db4-5eed-b978-dad5c1dc8efb",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChienPao.Name",
    display_name="Chien-Pao",
    searchable_by=["Chien-Pao", "Basic", "ChienPao"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=1002,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Rising Blade",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
