from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6c02b85b-0e4d-5d5f-92f8-0584e57ea8a4",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Avalugg.Name",
    display_name="Avalugg",
    searchable_by=["Avalugg", "Stage 1", "Avalugg"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    family_id=712,
    abilities=[
        Attack(
            title="Iceberg Breaker",
            game_text="Discard the top 6 cards of your deck, and this attack does 60 damage for each Basic Water Energy card you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Frost Stamp",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
