from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6b39a1d9-fc16-5709-84bd-9d50112b4558",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terapagos.Name",
    display_name="Terapagos",
    searchable_by=["Terapagos", "Basic", "Terapagos"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=1024,
    abilities=[
        Attack(
            title="Prism Charge",
            game_text="Search your deck for up to 3 Basic Energy cards of different types and attach them to your Tera Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Hard Tackle",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
