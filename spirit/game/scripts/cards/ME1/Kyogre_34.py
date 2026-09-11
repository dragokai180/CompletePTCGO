from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="29e3891e-f14a-5b12-abc1-73143ff22fa0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=382,
    abilities=[
        Attack(
            title="Riptide",
            game_text="This attack does 20 damage for each Basic Water Energy card in your discard pile. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Swirling Waves",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
